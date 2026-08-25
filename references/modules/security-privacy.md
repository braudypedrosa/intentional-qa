# Security & Privacy Surface Check

Perform passive, client-visible hygiene checks only. This is not penetration testing or a security certification.

## Checks

- HTTPS, mixed content, insecure form actions, unsafe external links, sensitive values in URLs, and obvious cookie attributes visible to the browser.
- Accidental secrets, tokens, personal data, stack traces, debug output, directory paths, source maps, or private endpoints exposed in HTML, JavaScript, requests, or console output.
- Consent controls and whether non-essential requests appear before consent when the requested scope includes privacy behavior.
- Basic authorization boundaries only with test roles/accounts provided by the user. Confirm that direct navigation does not expose another role's visible data.
- Error pages and API responses for excessive implementation detail or personal data.

Do not brute-force credentials, enumerate users, scan ports, bypass controls, exploit vulnerabilities, send destructive payloads, or broaden the target beyond the supplied site. Stop and report when meaningful verification would require penetration-testing authorization.

## Evidence and output

Redact sensitive values. Describe where and how the exposure appears, its reproducibility and user impact, and the minimum evidence needed for remediation. Mark inaccessible role checks Blocked rather than Pass.
