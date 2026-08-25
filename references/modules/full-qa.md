# Full QA

Full QA is the orchestrator subskill. It chains every Intentional QA module and produces one release-oriented report.

## Sequence

1. Read `../shared-rules.md` and record environment, authorization, critical journeys, known changes, and prohibited actions.
2. Build one normalized URL/template inventory. Reuse it across modules rather than crawling independently each time.
3. Run Broken Link Check early to expose unreachable pages and assets.
4. Run Functional Journey Test and Form Test while capturing console/network evidence for the Console & Network module.
5. Run Responsiveness Check across the shared template sample and exercise important responsive interactions.
6. Run Accessibility Check alongside the same critical journeys and rendered states.
7. Run Visual & Content Consistency, SEO & Metadata, Performance, and Security & Privacy Surface checks.
8. Manually verify automated candidates, deduplicate findings by root cause, and assign severity.
9. Read `../report-format.md` and produce one report with a release recommendation.

Read every module file in this directory before executing Full QA.

## Reuse evidence

One interaction may support several modules, but each conclusion must remain distinct. For example, a mobile menu test can provide responsive, accessibility, functional, and console evidence. Do not rerun it solely to create separate screenshots unless the first evidence is insufficient.

## Minimum Full QA coverage

- One normalized inventory and explicit sampling rule.
- All critical journeys.
- Every public form at least through safe validation; authorized end-to-end delivery only when permitted.
- Every unique template at mobile and desktop, plus representative tablet and laptop coverage.
- Keyboard testing on critical journeys.
- Console/network capture during important interactions.
- Representative performance measurements per important template class.
- SEO/metadata and passive security/privacy checks across the inventory or a clearly stated sample.
- Error, empty, loading, and unavailable states where safely reachable.

## Interview-demo addendum

Explain:

- what AI accelerated: inventory, risk-based test drafting, repetitive probes, artifact collection, and duplicate clustering;
- what required tester judgment: authorization, business risk, expected behavior, visual quality, false-positive review, and release recommendation;
- what belongs in CI: stable link, smoke, form-validation, accessibility, and regression checks;
- what remains exploratory: new features, ambiguous workflows, usability, real-device behavior, and novel failure modes.

Include one example where automated evidence was misleading or incomplete and how manual verification corrected it.
