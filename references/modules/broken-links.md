# Broken Link Check

Find broken navigational links, redirects, fragments, downloads, embeds, and page assets without treating HTTP status alone as rendered-page proof.

## Discovery

- Seed from the supplied URLs and `robots.txt`, sitemap indexes, XML sitemaps, navigation, footer, pagination, and same-origin rendered links.
- Normalize fragments and tracking parameters for fetch deduplication while retaining the original source URL and link text.
- Crawl same-origin HTML only. Check external targets but do not recursively crawl them.
- Record skipped schemes such as `mailto:`, `tel:`, `sms:`, and `javascript:` separately; validate their syntax where useful.

For a deterministic public crawl, use `../../scripts/broken_link_checker.py`. Its output is evidence to verify, not the final verdict.

## Classification

- Confirm 4xx/5xx responses, DNS/TLS failures, timeouts, redirect loops, excessive chains, and assets with failed loads.
- Treat 401/403/429 as Blocked or policy-dependent unless the page is expected to be public and manual verification confirms a defect.
- Treat HEAD/GET differences carefully; prefer a bounded GET when HEAD is unsupported.
- Verify redirects against intended destinations. A 200 final status can still be wrong when it lands on an unrelated homepage or soft 404.
- For fragment links, load the rendered final page and confirm the target ID/name exists and navigation reaches it.
- For JavaScript-rendered links or assets, verify in the built-in browser.

## Output

For each confirmed issue record source page, link text or asset, requested target, final target/status, redirect chain, failure type, user impact, and whether it is isolated or template-wide. Include totals for discovered, checked, passed, redirected, failed, blocked, and skipped URLs.
