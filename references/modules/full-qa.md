# Full QA

Full QA is the orchestrator subskill. It chains every Intentional QA module and produces one release-oriented report.

## Sequence

1. Read `../shared-rules.md` and record environment, authorization, critical journeys, known changes, and prohibited actions.
2. Build one normalized URL/template inventory. Reuse it across modules rather than crawling independently each time.
3. Create a screenshot coverage plan from that inventory: required templates, viewports, journey checkpoints, form states, and expected visual findings. Use stable evidence filenames.
4. Run Broken Link Check early to expose unreachable pages and assets.
5. Run Functional Journey Test and Form Test while capturing console/network and required screenshot evidence.
6. Run Responsiveness Check across the shared template sample and exercise important responsive interactions.
7. Run Accessibility Check alongside the same critical journeys and rendered states.
8. Run Visual & Content Consistency, SEO & Metadata, Performance, and Security & Privacy Surface checks.
9. Manually review every cited screenshot, verify automated candidates, deduplicate findings by root cause, and assign severity.
10. Read `../report-format.md` and produce one report with a release recommendation and evidence links.

Read every module file in this directory before executing Full QA.

## Reuse evidence

One interaction or screenshot may support several modules, but each conclusion must remain distinct. For example, a mobile menu test can provide responsive, accessibility, functional, visual, screenshot, and console evidence. Do not rerun it solely to create separate screenshots unless the first evidence is insufficient.

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
- Reviewed screenshot evidence for every visually dependent finding plus representative template/viewport/state passes. A visually dependent conclusion with no usable capture remains an evidence gap, not a fully verified result.

## Interview-demo addendum

Explain:

- what AI accelerated: inventory, risk-based test drafting, repetitive probes, artifact collection, and duplicate clustering;
- what required tester judgment: authorization, business risk, expected behavior, visual quality, false-positive review, and release recommendation;
- what belongs in CI: stable link, smoke, form-validation, accessibility, and regression checks;
- what remains exploratory: new features, ambiguous workflows, usability, real-device behavior, and novel failure modes.

Include one example where automated evidence was misleading or incomplete and how manual verification corrected it.
