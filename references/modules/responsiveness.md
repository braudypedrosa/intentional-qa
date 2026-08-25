# Responsiveness Check

Audit rendered layout and interactive behavior across mobile, tablet, laptop, and wide desktop widths.

## Coverage

1. Inventory unique templates and critical journeys using the shared scope rules.
2. Test project breakpoints when known; otherwise use 390, 768, 1024, and 1440 CSS pixels.
3. Add widths immediately below and above a breakpoint when the transition looks fragile.
4. Inspect every unique template at mobile and desktop. For tablet and laptop, test every template on small sites or state the representative sample.

Use a real viewport resize. If unavailable, a temporary same-origin iframe harness at the exact CSS width is acceptable. Never scale a screenshot or use CSS transforms as viewport evidence. Remove temporary files after the audit.

## Rendered probes

At each tested page and width, collect viewport width, document `clientWidth`, document `scrollWidth`, broken images, clipped text candidates, visible control sizes, navigation/footer presence, and console errors.

Useful page-context probe:

```js
const doc = document;
const overflow = doc.documentElement.scrollWidth > doc.documentElement.clientWidth;
const brokenImages = [...doc.images].filter(img => !img.complete || !img.naturalWidth);
const clippedText = [...doc.querySelectorAll('h1,h2,h3,p,a,button,label')]
  .filter(el => el.scrollWidth > el.clientWidth + 1);
```

Manually review candidates. Hidden drawers, badges, inline links, and intentional accessible truncation can produce false positives.

## Visual and interaction inspection

- Header, navigation mode, footer stacking, content order, hierarchy, type scale, line length, section spacing, and dead space.
- Grid recomposition, tables, filters, carts, dialogs, carousels, sticky elements, image crops, and aspect ratios.
- Horizontal overflow, clipping, overlap, missing content, and fixed controls covering essential content.
- Roughly 44 by 44 CSS-pixel pointer area for primary touch controls; smaller targets may pass when spacing and context compensate.
- Menus, filters, forms, carts, dialogs, and primary calls to action must remain usable by pointer and keyboard at their responsive widths.

A site is not “fully responsive” based only on one desktop and one mobile screenshot.

## Output

Report failures by page and exact width, concerns separately, confirmed passes, interaction/console results, coverage totals such as “12 pages x 4 widths = 48 renders,” and any untested widths or templates.
