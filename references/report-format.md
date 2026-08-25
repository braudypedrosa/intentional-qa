# Intentional QA report format

Keep the report readable by a CEO, product owner, and developer. Use a Markdown file when the user requests an artifact; otherwise provide the same structure in the response.

## Executive summary

- Overall verdict: Pass, Pass with concerns, Fail, or Blocked.
- Release recommendation: Go, Conditional go, or No-go, with one-sentence rationale.
- Scope and environment: target, public/authenticated coverage, run mode, date, and important constraints.
- Coverage: discovered/tested URLs, templates, viewports, journeys, forms, and any browser/device limits.
- Finding totals: Critical, High, Medium, Low, Concern, and Blocked.
- Modules run: list each Intentional QA subskill and its Pass, Fail, Blocked, or Not run status.

## Coverage matrix

Use one row per meaningful surface or journey:

| Surface or journey | URLs/templates | Checks | Result | Evidence/notes |
|---|---:|---|---|---|

Use Pass, Fail, Blocked, Not run, or Concern. Do not use blank cells to imply success.

## Module results

Summarize Responsiveness, Broken Links, Forms, Functional Journeys, Accessibility, Console & Network, Performance, SEO & Metadata, Visual & Content, and Security & Privacy. A module-level Pass requires its stated coverage; partial execution must be labeled Partial or Blocked with details.

## Findings

Give each confirmed issue a stable ID such as `QA-001`.

### QA-001: Concise observable problem

- Severity:
- Surface and URL:
- Environment/viewport:
- Preconditions:
- Steps to reproduce:
- Expected:
- Actual:
- Evidence:
- Frequency/scope:
- Severity rationale:
- Suggested next action:

Keep proposed fixes tentative unless the root cause was verified. Do not include sensitive credentials, tokens, or personal data in evidence.

## Concerns and observations

Keep subjective visual feedback, potential risks, third-party noise, and unconfirmed suspicions outside the confirmed-defect count.

## Confirmed passes

List meaningful risk areas that were actually exercised. Avoid padding the report with trivial passes.

## Gaps and blocked checks

State what was not tested, why, what access or safe environment is needed, and how the limitation affects confidence.

## Recommended follow-up

Order next actions by risk:

1. release blockers and retests;
2. high-impact fixes and regression coverage;
3. automation candidates for CI;
4. exploratory or device testing that still needs human judgment.

## Interview-demo appendix

When requested, include:

- AI contribution: inventory, risk-based test drafting, repetitive execution, artifact collection, and duplicate clustering.
- Human contribution: scope, authorization, business-risk ranking, ambiguous expected behavior, visual judgment, and go/no-go decision.
- Automation split: deterministic smoke/regression tests in CI; exploratory, usability, and new-feature investigation led by a tester.
- One concrete example where automated evidence was misleading or incomplete and how it was manually verified.
