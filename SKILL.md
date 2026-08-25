---
name: intentional-qa
description: Run self-contained, evidence-backed website QA using focused subskills for responsiveness, links, forms, functional journeys, accessibility, console and network health, performance, SEO, visual consistency, and client-visible security. Use one subskill for a targeted check or Full QA to chain the entire suite; report by default and do not modify the site unless explicitly asked.
---

# Intentional QA

Intentional QA is a standalone website-QA suite. It contains its own operating rules, test procedures, severity model, evidence requirements, and reporting format. Do not load or invoke another skill to complete its work.

## Select a subskill

Route to the smallest requested subskill and read only its module plus [shared-rules.md](references/shared-rules.md):

- **Responsiveness Check:** layout and interaction behavior across widths. Read [responsiveness.md](references/modules/responsiveness.md).
- **Broken Link Check:** crawl links and assets, redirects, fragments, and failures. Read [broken-links.md](references/modules/broken-links.md).
- **Form Test:** form discovery, validation, usability, accessibility, and authorized delivery. Read [forms.md](references/modules/forms.md).
- **Functional Journey Test:** navigation and important end-to-end user goals. Read [functional-journeys.md](references/modules/functional-journeys.md).
- **Accessibility Check:** keyboard, semantics, labels, focus, contrast, and common WCAG risks. Read [accessibility.md](references/modules/accessibility.md).
- **Console & Network Check:** client errors, failed requests, resilience, and third-party noise. Read [console-network.md](references/modules/console-network.md).
- **Performance Check:** repeatable lab measurements and causal inspection. Read [performance.md](references/modules/performance.md).
- **SEO & Metadata Check:** crawlability signals, metadata, headings, schema indicators, and shareability. Read [seo-metadata.md](references/modules/seo-metadata.md).
- **Visual & Content Consistency:** hierarchy, spacing, imagery, copy, states, and cross-template consistency. Read [visual-content.md](references/modules/visual-content.md).
- **Security & Privacy Surface Check:** non-invasive, client-visible hygiene only. Read [security-privacy.md](references/modules/security-privacy.md).
- **Full QA:** chain every subskill and produce one deduplicated release report. Read [full-qa.md](references/modules/full-qa.md) and every module it routes to.

If the request names several checks, run those modules in a sensible sequence. “Full audit,” “full website audit,” “full QA,” or “Full QA suite” selects Full QA.

## Shared execution contract

Before testing, read [shared-rules.md](references/shared-rules.md). Preserve these invariants:

- Testing is read-only unless the user explicitly requests a fix.
- Use the built-in browser for rendered or interactive work.
- Use only provided WordPress authentication; try WP-CLI first for `.local` sites and ManageWP for Sessionwise.
- Do not create leads, accounts, orders, payments, bookings, emails, deletions, or other side effects without explicit authorization.
- Collect observable evidence and manually verify automated findings before classifying them as defects.
- Never convert Blocked, Not run, sampled, or inferred results into Pass.
- Keep functional failures, visual concerns, and unconfirmed observations distinct.

## Invocation examples

```text
Use $intentional-qa in Responsiveness Check mode on https://example.com.
```

```text
Use $intentional-qa to test every public form without submitting live data.
```

```text
Use $intentional-qa Full QA on this local site and produce an interview-demo report.
```

## Output

For one subskill, give its scope, coverage, findings, confirmed passes, and limitations. For multiple modules or Full QA, read [report-format.md](references/report-format.md) and produce one deduplicated report. Create a file only when the user requests an artifact or when the audit is large enough that a durable report is materially useful.

## Maintenance

The installed global folder is the canonical source. When the user requests an Intentional QA update, read [maintenance.md](references/maintenance.md), edit and validate this global skill first, then commit and push the complete change to its configured GitHub remote.
