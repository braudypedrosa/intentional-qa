# Accessibility Check

Find material accessibility barriers through automated leads and manual interaction. Do not claim WCAG conformance from an automated scan.

## Checks

- Navigate critical journeys using keyboard only; inspect focus visibility, logical order, skip links, traps, dialog containment, and focus return.
- Inspect landmarks, page language, title, one useful primary heading where appropriate, heading hierarchy, control names, labels, descriptions, error association, link purpose, table semantics, image alternatives, and live status messaging.
- Check zoom/reflow and text spacing when scope permits. Review obvious color contrast and non-color status indicators.
- Exercise menus, accordions, carousels, tabs, dialogs, filters, and forms with keyboard and exposed semantics.
- If an automated accessibility scanner is available in the current environment, run it, then manually verify every reported issue included in the report.

## Classification

Tie severity to blocked tasks, affected users, frequency, and scope. Missing semantics with no immediate visible failure can still be material; decorative images without alt text may be correctly hidden. Cite a WCAG criterion only when confident and state the tested level only when it was actually assessed.

## Output

Record the affected element, page/state, interaction sequence, observed semantic or contrast detail, user impact, scope, and verified criterion when applicable. Separate automated candidates that were not manually confirmed.
