# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S04`
- Section Name: `Project Typologies`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S04-001` | Universal / Safe | AUTHORED | `raw/ARC-S04-001.html` |
| `ARC-S04-002` | Premium / Editorial | AUTHORED | `raw/ARC-S04-002.html` |
| `ARC-S04-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S04-003.html` |
| `ARC-S04-004` | Conversion-led | AUTHORED | `raw/ARC-S04-004.html` |
| `ARC-S04-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S04-005.html` |

## Authoring Direction

Five visual-direction reference images were supplied. As in `ARC-S01` and `ARC-S03`, the
direction was to follow the supplied layouts rather than abstract from them, and to leave every
image area empty. Each study reproduces the topology of one reference — heading treatment, tile
arrangement, label placement, control placement, whitespace rhythm — retargeted to a project
typologies section.

None of the five references is a typology section in its original form: they come from property
marketing, a software product page, a construction company deck, and a developer brand deck.
Their card and tile topologies were carried across; none of their subject matter was.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S04-001` | Reference 1 | Left column of four stacked cards with one inverted to a dark fill, each with a right-aligned uppercase title, a small description and a corner arrow; tall full-height image panel on the right |
| `ARC-S04-002` | Reference 5 | Mixed italic-serif and uppercase-sans heading, a paragraph above a rule, a soft concentric graphic, a four-card row with alternating fills, and a small mark with an italic line beneath |
| `ARC-S04-003` | Reference 3 | Pill tag and right-hand label above a left heading with a marker-pen highlight, beside a bento grid of tinted cards, unequal image tiles, an accent card, a graphic, and an arrow button |
| `ARC-S04-004` | Reference 4 | Accent eyebrow tag, wide uppercase heading, three deep-blue cards each with a white geometric glyph, a description and a scope line, and a row of image tiles beneath |
| `ARC-S04-005` | Reference 2 | Numbered "02 / Catalog" label, two-line heading with an emphasised phrase, a vertical category list with one entry active, a paired image viewport, and a paragraph with circular previous / next controls |

Two substitutions were made to keep the batch inside the copy policy. Reference 5 prints a year
beside its rule; it is replaced with a neutral label. Reference 4 prints a storey-count spec line
on each card; it is replaced with a neutral scale descriptor, because a storey count on a
placeholder card reads as a capability claim.

## Study Records

### ARC-S04-001 — Universal / Safe

- **Structural intent / archetype:** The plainest possible typology list. Four named typologies in
  a vertical stack beside one image, with one card inverted so the section has a focal point.
- **Layout model:** Compact head (eyebrow + heading) above a `1fr / 0.86fr` grid — a stacked card
  column beside a full-height media panel. Each card is a grid of a right-aligned uppercase title
  over a foot row holding an uppercase description on the left and an arrow on the right. The
  second card is inverted to a dark fill and carries a "Featured" tag.
- **Density:** Medium. Four typologies with one line of description each.
- **Media mode:** One empty media area, stretched to the full height of the card stack.
- **Interaction:** None. No `<script>` element. Each card title is a stretched link, so the whole
  card is clickable while the focus ring stays on the title text — no `:has()` dependency.
- **Responsive strategy:** The media panel moves above the stack and becomes 16:9 at 1024px, 3:2 at
  768px, and 4:3 at 480px, where card titles also switch from right- to left-aligned and the foot
  row stacks. Card padding and radius step down at 360px.
- **Composer value:** The safest binding target in the section. Four repeating cards of title,
  one-line description, and link, plus a single image and an optional highlight flag — a field set
  almost any content model can fill.
- **Limitation / content ceiling:** Four cards; a fifth makes the stack taller than the media panel
  at 1440px and breaks the balance the layout depends on. Descriptions must stay to one uppercase
  line — uppercase small text is slow to read at length. Only one card should be inverted.

### ARC-S04-002 — Premium / Editorial

- **Structural intent / archetype:** Typologies framed as audiences. An editorial question heads
  the section and four cards answer it, each with a different fill so the row reads as a set
  rather than a repetition.
- **Layout model:** Three-column head at `1.5fr / 0.9fr / 0.6fr` — uppercase heading with an
  italic serif first word, a paragraph above a rule with a small label beneath, and a concentric
  ellipse graphic in the corner. Below it a four-card row with fills of paper, navy, white, and
  olive; each card holds a chip title, a description, and an empty image area pushed to the card
  foot. A serif italic signature line with a small mark closes the section.
- **Density:** Medium.
- **Media mode:** Four empty image areas, each toned to its card fill so the placeholder reads as
  part of the card rather than as a hole in it.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The graphic drops to its own full-width row at 1024px where cards go
  4 → 2; the head becomes one column and card media widens to 16:10 at 768px; cards become a
  single column with 3:2 media at 480px. Card padding and graphic width step down at 360px.
- **Composer value:** The premium register, and the only study in the section with a per-card fill
  variable. Useful where typologies are really audience segments and the section has to feel
  authored rather than tabulated.
- **Limitation / content ceiling:** Exactly four cards — the fill sequence is designed as a set and
  a fifth card repeats a fill. Chip titles must be one or two words. The italic serif and the
  four-fill palette are strong style commitments that will not suit a restrained studio identity.

### ARC-S04-003 — Dense / Information-heavy

- **Structural intent / archetype:** A bento board of typologies. Cards, images, and a drawing
  graphic share one grid so the section carries the most information per unit of height in the
  set.
- **Layout model:** A top rail (pill tag left, studio label right) above a `0.72fr / 2.2fr` grid.
  The left column holds the heading — with one word set in a marker-pen highlight — and a circular
  arrow button. The right column is a seven-tile bento driven by `grid-template-areas`: four
  typology tiles (each with a title, a description, and a scope definition pair), two empty image
  tiles that span two rows at different points in the grid, and one decorative drawing tile.
- **Density:** High.
- **Media mode:** Two empty image tiles at unequal heights, plus one decorative inline-vector tile
  that is not a media slot and should not be filled with photography.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The bento is re-declared, not reflowed: three named area maps at
  desktop, 1024px, and 480px, so tile order and spans stay deliberate at every width rather than
  falling out of source order. Row minimums drop at 768px; image tiles switch from a row-span to a
  16:10 ratio and scope pairs stack at 480px.
- **Composer value:** The highest-capacity option for this section role. Four typologies each with
  title, description, and a scope label/value pair, plus two image regions — and the bento absorbs
  a mixed content model without forcing every tile to be the same shape.
- **Limitation / content ceiling:** The area maps are hand-authored, so the tile count is fixed at
  seven; adding a typology means editing three `grid-template-areas` declarations. Descriptions
  must stay near fifteen words or tiles grow uneven. The accent fill and highlight are a strong
  visual commitment.

### ARC-S04-004 — Conversion-led

- **Structural intent / archetype:** Typologies presented as three named series with a conversion
  close. The section answers "which one is my project?" and then gives a way to ask.
- **Layout model:** Accent eyebrow tag and a wide uppercase heading above a three-card series row.
  Each card is deep blue with a white geometric glyph, a title link, a description, and a scope
  line on a rule at the card foot. A three-tile image row follows at mixed proportions (3:4, 4:3,
  4:3), and a deep-blue foot bar closes the section with a lead line, a white primary button, and
  a secondary text link.
- **Density:** Medium-high.
- **Media mode:** Three empty image tiles at mixed proportions. The card glyphs are decorative
  inline vectors, not media slots.
- **Interaction:** None. No `<script>` element. Conversion is carried by hierarchy — one filled
  button, one text link, three card links — rather than by a form.
- **Responsive strategy:** Series cards go 3 → 2 at 1024px with the third spanning both columns,
  and the first image tile drops its portrait ratio. Image tiles go 3 → 2 at 768px with the third
  spanning and widening to 21:9. Everything becomes single column at 480px, where the primary
  button goes full width. Card padding and glyph size step down at 360px.
- **Composer value:** The conversion register for the section. The three-series model maps cleanly
  onto studios that publish a defined offer set, and the foot bar gives Composer a dedicated
  conversion region separate from the typology cards.
- **Limitation / content ceiling:** Three series exactly — the heading states three, and a fourth
  card breaks both the sentence and the 2+1 tablet fallback. The scope line is one short phrase.
  The deep-blue fill is a strong brand assumption and would need retinting for a light-brand studio.

### ARC-S04-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The typology catalogue as a numbered sheet. The section is
  browsed the way a practice browses its own archive — by typology index rather than by date —
  and each entry shows a pair of plates.
- **Layout model:** A `04 / Typology catalogue` sheet number above a `0.92fr / 1.9fr` grid. The
  left column holds the heading, a catalogue note pushed to the column foot, and circular previous
  / next sheet controls. The right column holds a right-aligned vertical typology index and, below
  it, the plate viewport — two empty plate areas with monospace captions per typology, four
  typologies, eight plate states in total.
- **Density:** Medium.
- **Media mode:** Two empty plate areas per category across four categories.
- **Interaction:** Vanilla JavaScript, about seventy lines, in one IIFE scoped by
  `document.querySelector('.arc-s04-005')`. A WAI-ARIA vertical tabs pattern with roving
  `tabindex`, `aria-selected`, Arrow / Home / End keys and `hidden` panel toggling, plus previous
  / next controls that step the same selection, disable at each end, and hand focus to the
  opposite control when the pressed one becomes disabled. Selection is signalled by four
  non-colour cues at once — a caret glyph, bold weight, an underline, and a darker tone. Without
  JavaScript the first typology stays visible and every typology name remains in the document.
- **Responsive strategy:** The grid becomes one column at 1024px, where the vertical index turns
  into a wrapping horizontal row and both it and its label left-align. Plates widen to 3:2 at
  768px and become a single 4:3 column at 480px. Control diameter holds at 44px at 360px.
- **Composer value:** The identity option. It is the only study in the section that models a
  typology as a *set of plates* rather than a single card, and the only one whose content scales
  by adding categories rather than by adding cards to a fixed row — the index absorbs more
  typologies without a layout change.
- **Limitation / content ceiling:** Two plates per typology; a third breaks the paired viewport.
  Four to six typologies before the vertical index outgrows the plate area at 1440px. Only one
  typology is visible at a time, so the section is a poor choice where all typologies must be
  scannable at once, and its plate behaviour degrades to the first category if scripts are blocked.

## Research Metadata

- **Sources:** Five visual-direction reference images supplied with the authoring request.
- **Research date:** 2026-08-30
- **Section assignment:** The references span more than one section role (a feature list, a
  category catalogue, an advantages bento, a construction series deck, and an audience-segment
  row). The target section was confirmed as `ARC-S04 — Project Typologies` before authoring.
- **Structural territory rationale:** Each reference was assigned to the territory its topology
  already served — the stacked card list to Universal, the alternating-fill editorial row to
  Premium, the bento board to Dense, the three-series deck to Conversion-led (which most readily
  accepts a conversion foot), and the numbered category catalogue to Sector-native, where the
  index-and-plate model supplies the discipline-native element.
- **Differentiation notes:** No two studies share a topology. Card arrangement differs across all
  five — vertical stack, four-card row, seven-tile bento, three-card series plus tile row, and a
  switchable plate pair. Media placement differs — one full-height panel, four toned in-card
  areas, two unequal bento tiles, three mixed-ratio tiles, eight switchable plates. Only one study
  uses JavaScript. Grounds differ: light grey, warm off-white, white, cool blue-grey, and a mid
  grey-green. Type differs: neutral sans, serif-italic mixed with uppercase sans, sans with a
  highlight span, uppercase sans, and sans with a monospace index.
- **Sector-interpretation note:** Three references come from property, software, and developer
  marketing. They were used as composition references only. No study contains listings, prices,
  availability, product features, or storey counts; all content is framed as studio typologies,
  scope, series, and plates.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont. The only
  vector content is four small decorative inline SVGs (`002` ellipses and mark, `003` drawing
  tile, `004` card glyphs), all `aria-hidden` and `focusable="false"`.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: One of five. `ARC-S04-005` needs it for the ARIA tabs keyboard contract
  and the paired sheet controls. `001`, `002`, `003`, and `004` contain no `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Typology panel | `ARC-S04-001` | One image standing for the typology set | Still image, portrait on desktop (16:9 at 1024px, 3:2 at 768px, 4:3 at 480px) | Empty tonal surface with a quiet label; the card stack carries all information. |
| Card image ×4 | `ARC-S04-002` | One image per audience card | Still image, 4:3 (16:10 at 768px, 3:2 at 480px) | Each area is toned to its card fill and labelled; card text sits above it, never over it. |
| Bento image ×2 | `ARC-S04-003` | Two supporting images at unequal heights | Still image, tall (16:10 at 480px) | Labelled empty tiles. The seventh tile is a decorative drawing, not a media slot, and must not be filled with photography. |
| Series tile ×3 | `ARC-S04-004` | One image per series | Still image, 3:4 for the first and 4:3 for the others (21:9 for the third at 768px) | Labelled empty tiles; the series cards above are self-contained. |
| Plate pair ×4 | `ARC-S04-005` | Two plates per typology across four typologies | Drawing or image, 4:3 (3:2 at 768px) | Each plate is a `<figure>` with a monospace caption inside a tabpanel; plate identity is carried by text, not artwork. |

Every image area is deliberately left empty, per the authoring direction. No study contains a
photograph, a logo, a client mark, or any fabricated evidence. Licensing and provenance metadata
is not applicable to this batch because no third-party asset is referenced; it becomes required
if these slots are filled before ingestion.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in
  the `ARC-S04-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline. One invalid `<dl>` structure
  in `003` (a `<div>` wrapping only the `<dt>`) was corrected before sign-off.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study with card titles at `<h2>` and no
  heading-level jumps; every `aria-controls` and `aria-labelledby` reference resolving to a real
  id; every `<a>` carrying an `href`; every `<button>` carrying a `type` and an accessible name
  (from `aria-label` on the icon controls, from text content on the tabs); every decorative SVG
  marked `aria-hidden` and `focusable="false"`; visible `:focus-visible` styling in all five, with
  an amber ring substituted inside dark cards; and a `prefers-reduced-motion` block in all five.
  Contrast measured on 35 text and UI colour pairs, including composited chip fills computed at
  their real alpha: all text ≥ 4.5:1 (lowest 4.85:1) and all interactive borders ≥ 3:1 (lowest
  3.20:1). The idle typology-index label in `005` initially measured 3.06:1 and was darkened to
  4.85:1 before sign-off. No state is signalled by colour alone — the `001` featured card carries
  a "Featured" tag, and the `005` selected tab carries a caret, bold weight, and an underline.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; 430 and 390 resolve through
  the 480 rules and 320 through the 360 rules. Grid children use `minmax(0, …)`, type and spacing
  use `clamp()`, and every multi-column arrangement reduces its column count rather than shrinking
  cards below a usable width. The `003` bento re-declares its area map at each breakpoint so tile
  order stays deliberate. No horizontal scroll anywhere in the batch. Interactive controls are
  ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`, and
  `crossorigin`. Zero matches across all five files.
- **Copy-policy validation: PASS.** Visible text extracted and scanned for awards, certifications,
  accreditations, rankings, percentages, guarantees, ratings, testimonial language, currency
  symbols, price patterns, and quantity claims (storeys, units, projects, years, clients). The
  only numeric strings in visible text are the study ID in each `<title>` and the `04 /` sheet
  number in `ARC-S04-005`.
- **Structural-diversity validation: PASS.** Five distinct topologies, five distinct media
  strategies, five distinct grounds, and five distinct type treatments. No study is a cosmetic
  variation of another.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- Section studies carry the section title as the document `<h1>` and card titles as `<h2>`,
  following the convention set in `ARC-S03`.
- `ARC-S04-005` reuses the drawing-sheet vocabulary established by `ARC-S01-005` and `ARC-S03-005`
  — sheet numbering, a monospace index, and plate captions — so the sector has a consistent
  sector-native register across sections.
- Every image area is an empty placeholder surface carrying a short text label. The `003` drawing
  tile and the `004` card glyphs are decorative vectors and are documented as such so they are not
  mistaken for unfilled media slots during ingestion.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
