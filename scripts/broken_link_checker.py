#!/usr/bin/env python3
"""Bounded same-origin link and asset checker for Intentional QA.

Uses only the Python standard library. It crawls HTML pages on the seed origin,
checks discovered external targets once, and emits JSON for manual verification.
"""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import time
from collections import deque
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urldefrag, urljoin, urlsplit, urlunsplit
from urllib.request import Request, build_opener


TRACKING_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
LINK_ATTRS = {
    "a": "href",
    "area": "href",
    "audio": "src",
    "embed": "src",
    "form": "action",
    "iframe": "src",
    "img": "src",
    "link": "href",
    "script": "src",
    "source": "src",
    "track": "src",
    "video": "src",
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = LINK_ATTRS.get(tag.lower())
        if not attr:
            return
        values = dict(attrs)
        value = values.get(attr)
        if value:
            self.links.append((tag.lower(), value.strip()))
        if tag.lower() in {"img", "source"} and values.get("srcset"):
            for candidate in values["srcset"].split(","):
                url = candidate.strip().split(" ", 1)[0]
                if url:
                    self.links.append((f"{tag.lower()}-srcset", url))


def normalize(url: str, keep_query: bool = True) -> str:
    url, _fragment = urldefrag(url)
    parts = urlsplit(url)
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    port = parts.port
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    path = parts.path or "/"
    query = ""
    if keep_query and parts.query:
        pairs = [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith("utm_") and key.lower() not in TRACKING_KEYS
        ]
        query = urlencode(sorted(pairs))
    return urlunsplit((scheme, host, path, query, ""))


def fetch(opener, url: str, timeout: float, user_agent: str) -> dict:
    request = Request(url, headers={"User-Agent": user_agent, "Accept": "text/html,*/*;q=0.8"})
    started = time.monotonic()
    try:
        with opener.open(request, timeout=timeout) as response:
            body = response.read()
            content_type = response.headers.get_content_type()
            return {
                "ok": 200 <= response.status < 400,
                "status": response.status,
                "final_url": response.geturl(),
                "content_type": content_type,
                "bytes": len(body),
                "elapsed_ms": round((time.monotonic() - started) * 1000),
                "body": body if content_type in {"text/html", "application/xhtml+xml"} else b"",
                "error": None,
            }
    except HTTPError as exc:
        return {
            "ok": False,
            "status": exc.code,
            "final_url": exc.geturl(),
            "content_type": exc.headers.get_content_type() if exc.headers else None,
            "bytes": 0,
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "body": b"",
            "error": str(exc),
        }
    except (URLError, TimeoutError, ssl.SSLError, OSError) as exc:
        return {
            "ok": False,
            "status": None,
            "final_url": url,
            "content_type": None,
            "bytes": 0,
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "body": b"",
            "error": str(exc),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Bounded same-origin link and asset checker")
    parser.add_argument("url", help="Absolute HTTP(S) seed URL")
    parser.add_argument("--max-pages", type=int, default=100, help="Maximum same-origin HTML pages to crawl")
    parser.add_argument("--max-urls", type=int, default=1000, help="Maximum total URLs to check")
    parser.add_argument("--timeout", type=float, default=15.0, help="Per-request timeout in seconds")
    parser.add_argument("--user-agent", default="IntentionalQA/1.0 (+manual-verification-required)")
    parser.add_argument("--output", help="Write JSON to this path instead of stdout")
    args = parser.parse_args()

    seed = normalize(args.url)
    seed_parts = urlsplit(seed)
    if seed_parts.scheme not in {"http", "https"} or not seed_parts.netloc:
        parser.error("url must be an absolute HTTP(S) URL")
    if args.max_pages < 1:
        parser.error("--max-pages must be at least 1")
    if args.max_urls < 1:
        parser.error("--max-urls must be at least 1")

    origin = (seed_parts.scheme, seed_parts.netloc)
    opener = build_opener()
    queue = deque([seed])
    queued = {seed}
    checked: dict[str, dict] = {}
    sources: dict[str, list[dict[str, str]]] = {seed: [{"source": "seed", "tag": "seed"}]}
    crawled_pages = 0
    skipped: list[dict[str, str]] = []

    while queue:
        url = queue.popleft()
        if url in checked:
            continue
        result = fetch(opener, url, args.timeout, args.user_agent)
        body = result.pop("body")
        checked[url] = {**result, "sources": sources.get(url, [])}

        final = normalize(result["final_url"]) if result["final_url"] else url
        final_parts = urlsplit(final)
        same_origin = (final_parts.scheme, final_parts.netloc) == origin
        if not (same_origin and result["ok"] and result["content_type"] in {"text/html", "application/xhtml+xml"}):
            continue
        if crawled_pages >= args.max_pages:
            continue
        crawled_pages += 1

        page = LinkParser()
        try:
            page.feed(body.decode("utf-8", errors="replace"))
        except Exception as exc:  # HTMLParser can surface malformed character-reference errors.
            checked[url]["parse_error"] = str(exc)

        for tag, raw in page.links:
            raw_parts = urlsplit(raw)
            if raw_parts.scheme and raw_parts.scheme.lower() not in {"http", "https"}:
                skipped.append({"source": final, "tag": tag, "target": raw, "reason": "unsupported scheme"})
                continue
            target = normalize(urljoin(final, raw))
            target_parts = urlsplit(target)
            if target_parts.scheme not in {"http", "https"} or not target_parts.netloc:
                skipped.append({"source": final, "tag": tag, "target": raw, "reason": "invalid target"})
                continue
            source_record = {"source": final, "tag": tag}
            sources.setdefault(target, [])
            if source_record not in sources[target]:
                sources[target].append(source_record)
            if target not in queued and len(queued) < args.max_urls:
                queued.add(target)
                queue.append(target)
            elif target not in queued:
                skipped.append({"source": final, "tag": tag, "target": target, "reason": "max URL limit"})

    results = []
    for url, result in checked.items():
        result["sources"] = sources.get(url, result.get("sources", []))
        results.append({"url": url, **result})
    results.sort(key=lambda item: item["url"])
    summary = {
        "seed": seed,
        "origin": f"{origin[0]}://{origin[1]}",
        "max_pages": args.max_pages,
        "max_urls": args.max_urls,
        "crawled_html_pages": crawled_pages,
        "checked_urls": len(results),
        "passed": sum(1 for item in results if item["ok"]),
        "failed": sum(1 for item in results if not item["ok"]),
        "redirected": sum(1 for item in results if normalize(item["final_url"]) != item["url"]),
        "skipped": len(skipped),
    }
    payload = {"summary": summary, "results": results, "skipped": skipped}
    rendered = json.dumps(payload, indent=2, sort_keys=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered + "\n")
    else:
        print(rendered)
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
