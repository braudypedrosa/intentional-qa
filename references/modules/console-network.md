# Console & Network Check

Identify client-side failures and resilience problems during real page loads and interactions.

## Checks

- Capture uncaught exceptions, unhandled promise rejections, severe console messages, mixed content, CSP/CORS failures, source-map/debug leakage, and repeated warnings with visible impact.
- Inspect failed first-party and critical third-party requests, response status, request method, initiator/action, redirects, caching behavior, and retry loops.
- Exercise loading, empty, offline/slow, unauthorized, not-found, validation, and server-error states when tools and authorization make this safe.
- Recheck after navigation, modal changes, filters, form validation, and other dynamic updates; initial-load silence is insufficient.

Distinguish first-party defects from browser extensions, privacy blockers, local certificates, intentional analytics blocking, and transient third-party noise. A console error is a defect only when its source, reproducibility, or user impact justifies it.

## Output

Record action, page/state, request URL/method/status or concise console text, source classification, frequency, visible impact, and reproduction evidence. Group repeated messages by root cause.
