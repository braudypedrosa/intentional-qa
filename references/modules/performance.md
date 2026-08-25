# Performance Check

Measure representative pages consistently, identify dominant causes, and avoid false precision.

## Coverage and measurement

- Select representative homepage, listing/archive, detail, form, and application templates plus critical journeys.
- Use the same environment, cache condition, viewport/device profile, throttling, and measurement method for comparisons.
- Record whether evidence is lab or field data. Never present lab results as real-user field performance.
- When tools provide them, record LCP, CLS, INP or TBT as a lab proxy, FCP, transfer size, request count, and long tasks.
- Repeat noisy tests and report a median or representative run. Note authentication, local/staging infrastructure, extensions, and third parties that affect results.

## Diagnose

Inspect the LCP element/resource, layout-shift sources, main-thread work, render-blocking resources, oversized or incorrectly dimensioned media, fonts, unused payload, caching/compression signals, lazy loading, request waterfalls, and third-party cost.

A slow response or score is a finding only with its conditions and evidence. Do not infer a root cause from a score alone or compare unlike profiles.

## Output

Provide a measurement table by URL/template and profile, followed by verified causes ranked by likely user impact. Separate confirmed regressions, environment limitations, and optimization opportunities.
