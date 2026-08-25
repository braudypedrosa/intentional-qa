# Shared rules

Read this before any Intentional QA subskill.

## Authorization and safety

- “Audit,” “check,” “review,” and “test” authorize observation, navigation, safe field validation, screenshots, local artifacts, and non-mutating requests. They do not authorize fixes or external side effects.
- Never submit a live contact, lead, newsletter, checkout, payment, booking, account-creation, deletion, or state-changing form without explicit permission.
- On local/staging environments, use conspicuous test data. Confirm whether integrations send real email, payment, CRM, analytics, or webhook traffic before using them.
- Do not expose secrets or personal data in reports. Redact evidence while preserving reproducibility.
- Security work is passive and client-visible. Do not exploit, brute force, scan ports, bypass access controls, or send destructive payloads.

## Browser and authentication

- Use the built-in browser for browser work. Preserve active state and leave the most relevant audited page open.
- Use only a WordPress account or authenticated route provided by the user. For `.local`, try WP-CLI first. For Sessionwise, use ManageWP.
- Direct HTTP requests may support status, header, redirect, sitemap, or asset evidence. They do not prove rendered or interactive correctness.

## Coverage

- Discover scope from the supplied URLs, sitemap, navigation, footer, same-origin links, application routes, and local source when available.
- For up to 25 meaningful public pages, test every page when practical.
- For larger sites, test every critical journey and unique template, then state the representative sampling rule. A link crawl may still cover the full discovered set.
- Record excluded, redirected, authenticated, blocked, and duplicate URLs. Normalize fragments and tracking parameters without merging materially different states.
- A template sample applies to other pages only when shared rendering and behavior were verified.

## Evidence and verdicts

- Use **Pass**, **Fail**, **Blocked**, **Not run**, and **Concern** precisely.
- A defect requires observable actual behavior, expected behavior grounded in requirements or established convention, reproduction context, and impact.
- Automated output is a lead until manually verified. Distinguish browser-extension noise, third-party failures, and environment limitations from first-party defects.
- Record exact URL/state, viewport or environment, steps, expected, actual, evidence, frequency/scope, severity rationale, and suggested next action.
- Deduplicate by verified root cause. Do not merge unrelated symptoms or inflate counts per affected page.

## Screenshot evidence

- Capture a screenshot whenever a conclusion depends on rendered appearance or visible state. This includes responsive reflow, overflow, clipping, overlap, spacing, hierarchy, image crops, contrast, focus visibility, menus, dialogs, validation messages, loading/empty/error/success states, and other visually judged behavior.
- Reproduce the exact state first, then capture the exact tested viewport. Prefer a focused viewport screenshot that clearly shows the evidence; add a full-page screenshot only when page-level context materially helps.
- For a confirmed visual defect, the screenshot must show the defect itself rather than a nearby or approximate state. Record the URL, viewport, state, and stable screenshot path with the finding.
- For visually evaluated passes, capture representative evidence for each unique template and required viewport/state in scope. State the sampling rule when capturing every render would add repetition without confidence.
- A screenshot is supporting evidence, not proof by itself. Pair it with the relevant measurements, DOM/semantic inspection, interaction result, console/network evidence, or expected-behavior basis.
- Use stable filenames such as `QA-001-home-390x844-cookie-overlap.png` or `PASS-home-1440x900-header.png`. Do not overwrite evidence from a materially different state.
- Review every saved screenshot before citing it. Retake blank, obscured, stale, loading, consent-covered, or incorrectly sized captures.
- Do not include credentials, tokens, personal data, test payment details, or unrelated private content. Redact or recapture safely while preserving the behavior being documented.

## Severity

- **Critical:** security/privacy exposure, data loss, payment/authentication failure, or a primary business journey unusable for most users.
- **High:** major journey blocked, material accessibility barrier, widespread broken layout, or repeated first-party failure.
- **Medium:** important behavior degraded with a workaround, isolated responsive/accessibility failure, or meaningful template-wide metadata defect.
- **Low:** limited functional impact or minor confirmed defect.
- **Concern:** subjective weakness, plausible risk, or unconfirmed behavior outside the defect count.
