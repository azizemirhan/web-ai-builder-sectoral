# BATCH V1

## Batch Identity

- Sector: `Automotive`
- Prefix: `AUTO`
- Section ID: `AUTO-S02`
- Section Name: `Vehicle / Service Categories`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `AUTO-S02-001` | Universal / Safe | AUTHORED | `raw/AUTO-S02-001.html` |
| `AUTO-S02-002` | Premium / Editorial | AUTHORED | `raw/AUTO-S02-002.html` |
| `AUTO-S02-003` | Structured / Visual Modular | AUTHORED | `raw/AUTO-S02-003.html` |
| `AUTO-S02-004` | Conversion-led | AUTHORED | `raw/AUTO-S02-004.html` |
| `AUTO-S02-005` | Art-directed / Distinctive | AUTHORED | `raw/AUTO-S02-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md`. These are the current
direction names; the earlier "Dense / Information-heavy" and "Sector-native / Distinctive"
readings are not used anywhere in this batch. Study IDs never change with a direction name.

## Section Role and the S03 Boundary

**AUTO-S02 contains CATEGORY-LEVEL navigation and discovery.** It answers one question: *which
vehicle or service category should I explore?* The visitor leaves this section having chosen a
kind of thing, not a thing.

**AUTO-S03 (Featured Vehicles) owns SPECIFIC VEHICLE / INVENTORY preview.** Individual vehicles,
stock, prices, finance, mileage, model years, transmission, specifications and availability all
belong there and are deliberately absent from every study here.

Correct in S02: `SUV`, `Electric`, `Performance`, `Touring`, `Commercial`, `Maintenance`,
`Diagnostics`, `Tyres`, `Body & Paint`, and — in `003` — one level of sub-category such as
`Compact`, `Seven seat`, `Full electric`, `Plug-in hybrid`, `Coupe`, `Estate`.

Not present anywhere in this batch: a model name, a price, a monthly payment, a finance rate, a
mileage or model-year figure, a transmission type, a stock count, an availability statement, a
range or power figure, or any card that represents one vehicle.

`003` is the only study that goes below the top category level. Its second level is still a
category — a body shape or a drivetrain type — not a model, and it carries no figures. That is
the deepest this section goes.

The boundary is enforced by a scan, not only by review: the visible text of all five studies is
checked for currency symbols and for the tokens `mileage`, `miles`, `VIN`, `automatic`,
`manual transmission`, `hp`, `bhp`, `mpg`, `kWh`, `0-60`, `in stock`, `available now`,
`model year`, `from only`, `per month` and `APR`. Zero matches.

## Study Records

### AUTO-S02-001 — Universal / Safe

- **Category model:** Vehicle categories — SUV, Sedan, Electric, Performance. Four, deliberately.
- **Structural intent:** The dependable, broadly reusable category section. Reads immediately as
  automotive category navigation and would suit a dealer, an automotive group or a
  manufacturer-style site without modification.
- **Layout model:** Equal four-up grid inside a 1440px shell on white. Header row carries the
  eyebrow and heading left, a supporting sentence and an "All categories" link right. Each card
  is a single `<a>` wrapping media, name, one descriptor and an Explore affordance, with an
  explicit `auto auto 1fr auto` row track so every Explore link lands on one baseline whatever
  the descriptor length. Minimal chrome: no borders, no card backgrounds — the media does the
  work.
- **Density:** Low. 75 visible words across four categories.
- **Media mode:** One reserved media area per category, 4:3, rounded 12px — four areas.
- **Interaction:** None. No `<script>`. Hover darkens the media and underlines the name; focus
  outlines the whole card.
- **Responsive strategy:** 4 up → 2 up at 1024 → one column at 520, where each card becomes a
  **horizontal row** (38% media beside the text) rather than a stacked 4:3 card. That decision is
  deliberate: a stacked single column of 4:3 cards measured roughly twice the height for no gain
  in scannability. Media column narrows to 34% at 360. Measured: 724 / 667 / 1192 / 1042 / 976 /
  971 / 993px.
- **Composer value:** The safe default for the role. A flat, repeatable collection of four
  identical fields — media, name, descriptor, link — which is the easiest shape in the batch to
  bind to arbitrary category data, and the only one that tolerates a changing category count.
- **Content ceiling / limitation:** Built for four categories; six would need a second row and
  eight would lose the single-screen read. Descriptors must stay one short sentence. There is no
  hierarchy between categories — every one carries identical weight, which is the point and also
  the limit.
- **Relationship to S03:** Category level only. Cards represent kinds of vehicle; nothing in the
  card shape can hold a price, a specification or a stock state.
- **Document metaphor used:** NO.

### AUTO-S02-002 — Premium / Editorial

- **Category model:** Vehicle categories — Electric, Performance, Touring, Utility.
- **Structural intent:** A range showcase rather than a card grid. The reading rhythm is closer to
  a model-family campaign than to dealership navigation, and the category media dominates.
- **Layout model:** Asymmetric twelve-column grid on a warm ivory ground. The four categories take
  four different column spans (7 / 4 / 4 / 7), four different media proportions (2:1, 1:1, 4:5,
  21:9) and two different vertical offsets, so no two entries share a size, a shape or a
  baseline. Index numeral above the crop, oversized category name below it, one descriptor, one
  restrained rule-underlined Explore affordance. A `max-height` ceiling on the crops stops one
  portrait entry from setting the height of a whole row.
- **Density:** Low. 77 visible words — barely more than `001`, across a section twice the height,
  which is the visual-first check for this study.
- **Media mode:** One reserved media area per category — four areas, four crops.
- **Interaction:** None. No `<script>`.
- **Responsive strategy:** The asymmetry survives rather than flattening. At 900 the grid becomes
  six columns with spans of 4 / 2 / 2 / 4 — still two unequal columns per row, still offset —
  which is what keeps the tablet height at 1165px instead of the ~3080px the naive single-column
  stack produced. Only below 560, where a two-track row would leave the display type in an
  unreadable column, does it go to one column, and there the rhythm moves from width to
  proportion: four full-width entries, no two crops alike. Measured: 1746 / 1597 / 1350 / 1165 /
  1819 / 1763 / 1646px.
- **Composer value:** The premium register for the role. Its field set is the same four fields as
  `001`, but the slots are positionally distinct, so a content model can deliberately promote one
  category over another — capacity for editorial hierarchy that `001` cannot express.
- **Content ceiling / limitation:** Exactly four entries; the grid is composed, not generated, and
  a fifth has no place to sit without redrawing it. Category names must be one word — the display
  size assumes it. It is the tallest study of the five at phone widths (1763px at 390) because
  four large editorial compositions genuinely cost that; `001` answers the same four categories in
  971px. That is the trade this direction makes, and it is the reason to choose `001` where
  section height matters.
- **Relationship to S03:** Category level only. Nothing in the entry shape can hold a vehicle.
- **Document metaphor used:** NO.

### AUTO-S02-003 — Structured / Visual Modular

- **Category model:** Vehicle categories — SUV, Electric, Performance, Touring — each opening onto
  two sub-categories. Twelve category routes in total.
- **Structural intent:** The capacity study. It demonstrates the corrected reading of 003: more
  category capacity carried by a **visual system**, not by more copy, more fields or more
  technical information.
- **Layout model:** A category navigator. A tab row selects a category; the selected category
  fills a mosaic panel laid out as `"lead info" / "lead subs"` — one dominant media field on the
  left spanning both rows, an information block top right, and two sub-category modules bottom
  right, each its own square media area and name.
- **Density:** Low-medium. 115 visible words is the highest in the batch, but it is spread across
  twelve category routes, so per route it is the lowest. Removing half the copy leaves the tab
  row, the mosaic and the media rhythm intact — the direction's own test.
- **Media mode:** Three reserved media areas per panel — one dominant, two sub-category — twelve
  in the document, three visible at a time.
- **Interaction:** Vanilla JS tab pattern. Roving tabindex, Arrow/Home/End keys, `aria-selected`,
  `aria-controls`. **Selected state is carried by a fill, a heavier weight and a bar under the
  label — never by colour alone.** Verified in a browser: click, arrow-wrap in both directions,
  Home and End all move selection and focus correctly, and exactly one panel is visible in every
  state.
- **Responsive strategy:** The selected category stays dominant at every width. Tabs wrap rather
  than scroll, so no control can go off-screen. At 1024 the mosaic becomes one column — lead,
  info, then the two sub-modules side by side — and the lead takes 16:9, then 3:2 at 768 and 4:3
  at 480. The two sub-modules stay a two-up row at every width; they never become a stack.
  Measured: 832 / 779 / 1514 / 1297 / 1059 / 1033 / 945px.
- **Composer value:** The highest-capacity option for the role and the only one with a second
  level. It exposes a repeatable category collection where each category owns a dominant media
  slot, a descriptor, a primary link and a nested collection of sub-categories — the shape most
  real automotive range taxonomies actually have.
- **Content ceiling / limitation:** Four or five tabs before the row wraps to two lines at 1280;
  exactly two sub-categories per category, since the bottom-right cell is a two-up grid and a
  third would either shrink below a usable size or push the panel past the lead. Sub-category
  names must be one or two words. It carries the batch's only JavaScript dependency for its full
  behaviour.
- **Progressive enhancement:** The markup ships every panel visible and the script hides the
  unselected ones at init. Verified with the script removed: all four panels render and all twelve
  category names remain readable and reachable. An author `display: grid` on the panel initially
  defeated the UA `[hidden]` rule and rendered all four panels at once — a `.panel[hidden]` rule
  now turns them off explicitly.
- **Relationship to S03:** The sub-category level is the closest this batch comes to S03 and it
  stops short deliberately — `Compact`, `Seven seat`, `Full electric`, `Plug-in hybrid`, `Coupe`,
  `Convertible`, `Estate`, `Grand tourer` are body shapes and drivetrain types, not models, and
  none carries a figure.
- **Document metaphor used:** NO. No filter dashboard, checkbox matrix, comparison table or
  specification block; the switcher is four pills and the panel is a media mosaic.

### AUTO-S02-004 — Conversion-led

- **Category model:** Service categories — Maintenance, Diagnostics, Tyres, Body & Paint. One
  coherent scenario, service discovery. No vehicle categories are mixed in.
- **Structural intent:** The study where choosing the category *is* the conversion. The next
  action is not a fixed button on the section — it is a consequence of the choice.
- **Layout model:** A choice rail beside a live action panel on a dark ground. The rail is four
  selectable rows, each an indicator, a name, a short descriptor and a chevron. The panel holds a
  reserved service media area above a title, a line and the primary action. Selecting a category
  rewrites all four: the media label, the title, the line and the CTA text, so the button reads
  `Book a maintenance visit`, `Book a diagnostic check`, `Book a tyre appointment` or
  `Book a body repair assessment`.
- **Density:** Low. 78 visible words.
- **Media mode:** One reserved service media area, relabelled by the current choice.
- **Interaction:** Vanilla JS radiogroup. Roving tabindex, arrow keys in both axes, Home/End,
  `aria-checked`, and a polite live region on the panel so the change is announced. **Selected
  state uses a panel fill, a thick left bar and a filled indicator dot — never colour alone.**
  Verified in a browser: click and keyboard both move the selection and rewrite all four panel
  fields, and the choice buttons keep their own markup intact through every switch.
- **Responsive strategy:** One column below 900 with the choices first and the panel they produce
  second, so the category/action relationship stays in reading order. Row height and padding
  tighten at 560 where the primary action also goes full width; the action never leaves the panel
  it belongs to. Measured: 1054 / 974 / 788 / 1210 / 1117 / 1158 / 1176px.
- **Composer value:** The conversion register for the role. Each category owns a name, a short
  descriptor, a panel line, a media slot and — the part no other study has — **its own action
  label**, which is what lets one section route to four different destinations without four
  different layouts.
- **Content ceiling / limitation:** Four choices; six makes the rail taller than the panel beside
  it at 1280 and breaks the pairing. Descriptors are two lengths — a short one in the rail and a
  slightly longer one in the panel — and both must stay one sentence. There is **no form and no
  field capture**: conversion is a visible action hierarchy only, so a real booking flow needs a
  downstream section.
- **Progressive enhancement:** With the script removed, all four categories and their descriptors
  render and the panel shows the default category with its action — verified. The choice controls
  are inert without JavaScript, which is the documented degradation.
- **Relationship to S03:** Service categories cannot collide with S03 at all — this study routes
  toward workshop work, not toward vehicles. No turnaround times, prices, quotes, warranty terms
  or certifications appear.
- **Document metaphor used:** NO. It is a choice rail, not a form, an intake sheet or a job card.

### AUTO-S02-005 — Art-directed / Distinctive

- **Category model:** Vehicle categories — SUV, Electric, Performance, Touring, Commercial. Five,
  the largest top-level set in the batch.
- **Structural intent:** The most memorable route into the range. Distinctiveness comes from crop,
  scale, sequencing and composition — the category names *are* the typography and the navigation
  at the same time.
- **Layout model:** A horizontal category rail on a full-bleed near-black stage, monochrome. Five
  tall cinematic crops on a **staggered baseline**, alternating between 3:4 and 4:5 proportions,
  each carrying an index at the top left, an arrow mark at the top right and the category name set
  oversized and uppercase across the foot of the crop. The run continues past the right edge so
  the fifth panel is deliberately cropped — the peek is the affordance.
- **Density:** Very low. 34 visible words in the whole section, the lowest in the batch: an index
  and a name per panel, plus the heading and one scroll hint.
- **Media mode:** One reserved media area per category — five areas, two proportions.
- **Interaction:** Native horizontal scroll with `scroll-snap-type: x mandatory` and
  `scroll-padding-inline` matched to the shell measure. **No JavaScript.** The rail is a labelled
  scrollable region (`role="region"`, `tabindex="0"`) so it is keyboard operable, and every panel
  is a real link, so tabbing through the categories scrolls the rail. `overscroll-behavior-x:
  contain` keeps the swipe out of the page's history gesture.
- **Responsive strategy:** The rail is kept at every width, because a swipe run is the native
  narrow-width form of this archetype rather than a device that has to be replaced. What changes
  is the measure: panels go from `clamp(232px, 21vw, 330px)` to `clamp(220px, 34vw, 300px)` at
  900, then to 74vw at 560 and 78vw at 360, so the peek widens and the continuation becomes more
  obvious as the screen narrows. The stagger and the crop alternation are dropped below 560, where
  they would only cost height. Verified scrollable at all seven widths, with the page itself never
  scrolling horizontally. Measured: 717 / 645 / 541 / 580 / 643 / 603 / 551px — the shortest and
  most stable study of the five.
- **Composer value:** The identity option, and the cheapest per category: a category needs only a
  name, an index and one crop to enter the rail, so the collection extends without redrawing the
  layout — the opposite of `002`.
- **Content ceiling / limitation:** Category names must be single words; the oversized uppercase
  setting assumes it and `Commercial` is already at the width limit of a 232px panel. There is no
  room for a descriptor, so the category names have to be self-explanatory — this study cannot
  carry an unfamiliar taxonomy. Horizontal scroll is discoverable but not free: the peek and the
  hint line are doing that work, and a category that never gets scrolled to is less visible than
  one in `001`'s grid.
- **Relationship to S03:** Category level only. A panel holds a name and a crop; it has nowhere to
  put a vehicle, a price or a specification.
- **Document metaphor used:** NO. No technical diagram, dashboard, blueprint or specification
  language; the distinctiveness is crop, scale, stagger and sequence.

## Structural Diversity

| | 001 | 002 | 003 | 004 | 005 |
| --- | --- | --- | --- | --- | --- |
| Topology | Equal four-up grid | Asymmetric 12-col showcase | Tabbed mosaic navigator | Choice rail + action panel | Staggered horizontal rail |
| Category system | Vehicle | Vehicle | Vehicle + sub-category | **Service** | Vehicle |
| Categories shown | 4 | 4 | 4 (+8 sub) | 4 | 5 |
| Ground | White | Warm ivory | Cool light grey | Dark charcoal | Near-black, monochrome |
| Media areas | 4 | 4 | 12 (3 visible) | 1 | 5 |
| Media proportion | One (4:3) | Four different | Two (16:9 + 1:1) | One (16:10) | Two, alternating |
| Hierarchy between categories | None — all equal | Composed, unequal | One dominant, rest hidden | One selected, rest listed | Sequential, all equal |
| Interaction | None | None | JS tabs | JS radiogroup + live CTA | Native scroll-snap |
| CTA behaviour | Per-card Explore | Per-entry Explore | One per selected category | **Rewritten by the choice** | Whole panel is the link |
| Visible words | 75 | 77 | 115 | 78 | 34 |
| Narrow-width move | Grid → 2 up → horizontal rows | 12-col → 6-col → 1 col | Mosaic → stack, lead stays dominant | Rail above the panel it drives | Rail kept, peek widened |
| Height at 1440 | 724px | 1746px | 832px | 1054px | 717px |

No two studies share a topology, a media count, a media proportion system, an interaction model or
a narrow-width strategy. `001` is the only equal grid; `002` is the only composed asymmetry; `003`
is the only one with a second category level and the only one that hides content behind a control;
`004` is the only service taxonomy and the only one whose action text is a function of the
selection; `005` is the only horizontal sequence and the only one with no descriptors at all.
Three of the five put category media in fundamentally different relationships to the type — beside
it, above it, and behind it.

## Research Metadata

- **Sources:** None supplied. All five authored to the section brief.
- **Research date:** 2026-09-01
- **Structural direction rationale:** The section role is discovery, so the five directions were
  read as five different answers to *how does a person choose*: scan a grid (`001`), be shown a
  composed range (`002`), narrow down through a system (`003`), be routed by their own need
  (`004`), or move through a sequence (`005`).
- **Differentiation notes:** See the diversity table. The set was checked against the "five grids
  with different CSS" failure mode; only `001` is a grid of equal cards.
- **Visual-first check:** Every study is carried by composition. `005` holds the strongest
  composition on the fewest words in the batch. `003` has the most words but the most routes, and
  passes the direction's own test — remove half its copy and the tab system, the mosaic and the
  media rhythm still carry it. No study derives its difference from having more text.
- **Document-metaphor justification:** NONE. No study uses a technical or professional document
  metaphor. No specification table, comparison table, filter dashboard, checkbox matrix,
  spreadsheet, job card or intake sheet appears in any of the five.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `<iframe>`, `@import`, `src=`, `url()`, webfont or
  `data:` image in any file. All type uses system font stacks. There is no SVG in this batch; the
  only glyphs are HTML entities, all `aria-hidden` where decorative.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form `action`.
- Browser storage: NONE.
- JavaScript necessity: `001`, `002` and `005` contain no `<script>` at all. `003` and `004` each
  carry one inline script, both of which earn their place — the tab pattern in `003` is the
  archetype, and the contextual action in `004` is the direction. Both are vanilla, scoped to their
  own study root, and both degrade to complete readable content with the script removed.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Category media ×4 | `AUTO-S02-001` | One crop per vehicle category | Still image, 4:3 at every width | Empty tonal panel with one quiet label; the card reads completely with no image, and no text overlays it. |
| Category media ×4 | `AUTO-S02-002` | One crop per category, four different proportions | Still image — 2:1, 1:1, 4:5 and 21:9, re-proportioned at 900 and 560 | Empty tonal panels with quiet labels. The proportion difference is structural and survives the empty state. |
| Category media ×4 (lead) | `AUTO-S02-003` | Dominant crop for the selected category | Still image, landscape; 16:9 at 1024, 3:2 at 768, 4:3 at 480 | Empty tonal panel; one visible at a time, the rest inside hidden panels. |
| Detail media ×8 (sub-category) | `AUTO-S02-003` | One crop per sub-category | Still image, 1:1 | Empty tonal panels with a smaller label; two visible at a time. |
| Service media ×1 | `AUTO-S02-004` | Crop for the currently chosen service category | Still image, 16:10 (4:3 below 560) | Empty tonal panel. Its label is rewritten by the choice, so the slot names which category it is standing in for even while empty. |
| Category media ×5 | `AUTO-S02-005` | Tall cinematic crop per category | Still image, portrait; 3:4 and 4:5 alternating, unified below 560 | Empty tonal panel with a quiet centred label. The oversized category name sits over the foot of the crop and is legible against the empty slot tone at 14.69:1. |

Twenty-two reserved media areas across five studies; nine visible simultaneously at most, in
`003`'s document as a whole. Every area is deliberately empty — intended output, not a defect. No
study contains a photograph, a logo, a manufacturer mark, a badge or any fabricated evidence.
Licensing and provenance metadata is not applicable because no third-party asset is referenced; it
becomes required if these slots are filled before ingestion.

## Claims

Verified by extracting the visible text of all five studies and scanning it.

- Prices, monthly payments, finance rates, lease terms, discounts: **NONE.**
- Performance, range, power, acceleration, fuel-economy or emissions figures: **NONE.**
- Availability, stock counts, model years, delivery or turnaround times: **NONE.**
- Awards, rankings, certifications, accreditations, warranty or guarantee terms: **NONE.**
- Real brands, manufacturer marks, model names or trademarks: **NONE.**
- The only digits in the visible text of the whole batch are the ordinal indices `01`–`04` in
  `AUTO-S02-002` and `01`–`05` in `AUTO-S02-005`.
- Category names are generic taxonomy — body shapes, drivetrain types and workshop disciplines —
  which are descriptive terms, not claims.

## QA

- **ID validation: PASS.** All five planned IDs exist. Each file carries a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a `data-direction` attribute, a scoped
  root class, and a filename in the `AUTO-S02-NNN.html` form required by
  `standards/02-NAMING-AND-ID-STANDARD.md`. All 13 element ids across the batch are namespaced
  with their study ID and unique.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance and nesting check
  clean on all five. All CSS is namespaced to the study root class; the only unscoped rules are a
  documented two-line standalone host baseline. One invalid nesting was found and fixed during
  authoring: `005` had an `<h2>` inside a `<span>`, which is not valid content — the crop wrapper
  is now a `<div>`.
- **Section-shell check: PASS.** No `<header>`, `<nav>` or `<footer>` element and no `banner`,
  `navigation` or `contentinfo` role in any file. No logo, wordmark, site navigation, announcement
  bar, hero or page chrome. Each study begins with its own section heading.
- **Semantic check (section role): PASS.** Every study answers *which category should I explore?*
  and none answers *which individual vehicle should I buy?* No study is an inventory preview, a
  price list, a comparison table or a specification table. See the S03 boundary section above for
  the enforced token scan.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study with no skipped heading levels; every
  `<a>` carries a resolvable in-document `href`; every `<button>` carries `type="button"`; every
  `aria-controls` and `aria-labelledby` reference resolves to a real id; no fake clickable `<div>`
  anywhere — categories are `<a>` where they navigate and `<button>` where they change section
  content. Visible `:focus-visible` styling in all five, `prefers-reduced-motion` in all five
  disabling the hover transitions that are the only motion in the batch. **No selected or checked
  state is communicated by colour alone:** `003` adds a fill, a heavier weight and a bar under the
  label; `004` adds a fill, a thick left bar and a filled indicator dot; both also expose
  `aria-selected` / `aria-checked`. Every interactive target measures at least 24px on both axes at
  all seven widths, and primary controls are 44px or taller. Contrast measured on 49 text and UI
  pairs: all text ≥ 4.5:1 (lowest 5.05:1) and all non-text controls, indicators and borders ≥ 3:1
  (lowest 3.66:1). One failure was found and fixed — `005`'s scrollbar thumb measured 2.34:1
  against the stage and is now 3.93:1, which matters because that thumb is part of what tells a
  viewer the rail scrolls.
- **Interaction QA: PASS**, verified by driving both studies in a real browser rather than by
  reading the source. `003`: click selects, ArrowLeft/ArrowRight wrap in both directions, Home and
  End jump correctly, focus follows selection, roving tabindex reads `0,-1,-1,-1`, and exactly one
  panel is visible in every state. `004`: click and arrow keys both move the selection and rewrite
  the panel title, descriptor, media label and CTA text together, and the choice buttons keep their
  own indicator, name and chevron intact through every switch. Two real defects were found this way
  and fixed: `003`'s author `display: grid` was defeating the UA `[hidden]` rule so all four panels
  rendered at once, and `004`'s `[data-desc]` selector was resolving to the first choice **button**
  rather than the panel paragraph, so the script was overwriting that button's markup.
- **Progressive-enhancement QA: PASS.** Both scripted studies were re-tested with their `<script>`
  removed. `003` renders all four panels and keeps all twelve category names readable and
  reachable. `004` renders all four service choices with their descriptors and shows the default
  category in the panel with its action. Neither degrades to an empty or broken section.
- **Responsive QA: PASS at 1440, 1280, 1024, 768, 430, 390 and 320px,** measured in a real browser.
  At every study and every width: `scrollWidth` equals the viewport width, so the page never
  scrolls horizontally; no element renders outside the viewport bounds; no interactive target falls
  below 24px. `005`'s rail is confirmed internally scrollable at all seven widths, so its
  continuation affordance is real rather than assumed. Breakpoint ladders differ per study and are
  documented in each record above. Two height problems were found and fixed: `002` measured 3080px
  at 768 before its tablet tier was rebuilt as a two-column grid, and `003` measured 5059px at 1024
  because of the `[hidden]` defect.
- **Height check: PASS.** Section heights at 1440 are 724 / 1746 / 832 / 1054 / 717px — following
  each structural direction rather than a single forced height. `002` is deliberately the most
  spacious and its cost is recorded as a limitation in its own record.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `data:image`, `fetch(`, `XMLHttpRequest`,
  `integrity`, `crossorigin`, `localStorage`, `sessionStorage` and external `<script src>`. Zero
  matches across all five files.
- **Copy-policy validation: PASS.** See the claims section above.
- **Structural-diversity validation: PASS.** See the diversity table above.
- **Visible-copy check: PASS.** No authoring, research, policy or compliance explanation appears in
  any visible composition. All of it is in the head comment blocks, the `<meta>` research fields
  and this document. Media slot labels are short, quiet and part of the reserved-area convention.
- **Not run here:** assistive-technology testing, real-device and touch testing, reduced-motion
  behaviour under a real user preference, and Design Lab capture. Those belong to Design Lab QA.

## Notes

- Second authored section in the Automotive sector. It follows the section-study conventions
  already set in this workspace — a `div` study root carrying `data-study-id` and `data-direction`,
  a `<section aria-labelledby>` inside it, `<h1>` for the section heading and `<h2>`/`<h3>` for
  items, no `<main>` landmark, and a commented two-line host baseline as the only unscoped CSS.
  `data-direction` and `<meta name="direction">` sit alongside the existing `territory` field so
  the current direction names are recorded without breaking the contact-sheet generator, which
  reads `territory`.
- `review/index.html` was **not** regenerated with this batch, for the same reason recorded in
  `AUTO-S01`: the contact-sheet generator sweeps every sector, and the Architecture Phase 3 rework
  has that pipeline suspended and is using the committed sheet as its fixed visual review source.
  It should be regenerated once Phase 3 closes, which will pick up both Automotive batches.
- No review, normalisation, survivor-selection or promotion decision is recorded in this document.
  Direction labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`, not
  production enums.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` are
  catalog-wide bookkeeping and were left untouched; they need a separate workspace-level pass.
