# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S06`
- Section Name: `Design Process`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S06-001` | Universal / Safe | AUTHORED | `raw/ARC-S06-001.html` |
| `ARC-S06-002` | Premium / Editorial | AUTHORED | `raw/ARC-S06-002.html` |
| `ARC-S06-003` | Structured / Visual Modular | AUTHORED (reworked) | `raw/ARC-S06-003.html` |
| `ARC-S06-004` | Conversion-led | AUTHORED | `raw/ARC-S06-004.html` |
| `ARC-S06-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S06-005.html` |

## Authoring Direction

**No reference images were supplied for this section.** The five topologies were designed to
brief rather than derived from references, which changes how diversity was controlled: instead
of inheriting five different layouts, each study had to be checked against the other four *and*
against the twenty-seven studies already authored in `ARC-S01`–`ARC-S05`, so the section does not
repeat a device the sector has already used.

The devices deliberately avoided, because they are already carrying other sections: the
drawing-sheet plate index (`ARC-S01-005`, `ARC-S04-005`), the bento field (`ARC-S04-003`,
`ARC-S03-007`), the horizontal scroll rail with controls (`ARC-S03-004`), the icon-and-rule list
panel (`ARC-S05-003`), and the numbered specification clause body (`ARC-S05-005`).

Image areas are left empty as in every previous section. `ARC-S06-005` carries no media area at
all, which is a deliberate decision recorded under Media Slots.

## Study Records

### ARC-S06-001 — Universal / Safe

- **Structural intent / archetype:** The plainest readable process: four stages side by side on a
  single line, each ending in something the client signs off.
- **Layout model:** A two-part heading block (`1.1fr / 1fr`, heading against an explanatory
  paragraph) above a four-column step row. Each step is a list item with a `border-top` that joins
  its neighbours into one continuous rule, and a dot pinned to that rule by `::before`. Steps run
  stage number, title, description, and an "Ends with" definition pair. A wide media band closes
  the section.
- **Density:** Medium. Four stages with a deliverable each.
- **Media mode:** One empty wide media band (21:9).
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Heading stacks and steps go 4 → 2 columns at 1024px, where the band
  narrows to 16:9; band to 3:2 at 768px and 4:3 at 480px, where steps become a single column. The
  connecting rule survives every arrangement because it is drawn per step rather than as one
  element behind them.
- **Composer value:** The safest binding target in the section. Four repeating items of number,
  title, description and one label/value pair, plus a heading, a paragraph and one image — a field
  set that maps onto almost any process content model.
- **Limitation / content ceiling:** Four stages; five breaks the row at 1280px and reads badly at
  the two-column fallback. Descriptions run to about twenty-five words. There is no room for
  per-stage responsibilities or outputs beyond the single pair.

### ARC-S06-002 — Premium / Editorial

- **Structural intent / archetype:** The process as a sequence worth reading slowly. Each stage
  gets a full row, an oversized serif numeral, and an image of its own.
- **Layout model:** A centred heading block above a timeline whose spine is drawn by a
  `::before` on the list. Each stage is a `1fr / clamp(48px, 7vw, 96px) / 1fr` grid with a node
  dot centred on the spine; odd stages put text left and media right, even stages reverse it with
  `:nth-child(even)`. Stage numerals are set in the serif at up to `3rem` in the spine tone.
- **Density:** Low-medium. Four stages, one paragraph each.
- **Media mode:** Four empty media areas, one per stage.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** At 768px the spine moves from the centre to the left edge, every stage
  reverts to a single left-aligned column with the node at its top, and the alternation is
  switched off rather than being allowed to produce ragged half-width text. Media steps 4:3 →
  16:9 → 3:2.
- **Composer value:** The premium register, and the only study in the section that gives every
  stage equal visual weight and its own image. Suits studios whose process is part of the sales
  argument rather than a reassurance footnote.
- **Limitation / content ceiling:** Four stages is the practical maximum — the alternating rhythm
  needs an even count and the section is already tall at four. One paragraph per stage; no room
  for outputs, responsibilities, or deliverable lists. The tallest study in the section by a wide
  margin.

### ARC-S06-003 — Structured / Visual Modular

- **Structural intent / archetype:** The process shown rather than tabulated. One large lead media
  field establishes the work, then five equal phase modules carry the sequence.
- **Layout model:** A short head over a full-width lead media area (21:9), above a five-column grid
  of phase modules. Each module is a 4:3 media area, a CSS-counter numeral, a short title and one
  line of copy. No rules, no boxes, no field lists — the grid and the media rhythm carry the
  structure.
- **Density:** Low. Five phases, one line each; roughly ninety visible words.
- **Media mode:** Six empty areas — one large lead area plus one per phase.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Five columns → at 1024px a six-track grid where the first three modules
  span two tracks and the last two span three, so the second row is filled rather than orphaned and
  its two media areas widen to 16:9 → at 768px two columns with the fifth module spanning the full
  width at 16:9 → one column at 480px with every phase area at 16:9 and the lead at 3:2. The grid
  adapts to the five-stage content model; the content model is not cut to fit the grid. Nothing is
  hidden at any width and there is no horizontal scroll.
- **Composer value:** A repeatable `{image, title, line}` phase collection with a lead image above
  it — the highest-capacity option in this section that stays visual, and the one that binds most
  directly to a media-led CMS model. The span rules absorb an odd item count without leaving a gap.
- **Limitation / content ceiling:** Five or six phases; beyond that the five-up row is too narrow at
  1440px and needs a second row. One line per phase — a second sentence reintroduces the density
  this study was reworked to remove.
- **Rework record:** Replaces a five-row dossier treatment (stage number, description, a three-pair
  metadata block and a small thumbnail, separated by hairlines). Preserved: the five-stage
  progression — brief and site, concept design, developed design, technical design, site and
  handover — the per-phase media relationship and the progressive responsive ladder. Removed: the
  dossier row language, the `Output / Studio does / You provide` metadata pairs, the monospace field
  labels and the long per-stage copy.

### ARC-S06-004 — Conversion-led

- **Structural intent / archetype:** The process read as an onboarding sequence, where the call to
  action is not a banner bolted on at the end but the final rung of the ladder — the next step in
  the same list.
- **Layout model:** A `0.82fr / 1.25fr` grid. The left column is sticky and holds eyebrow,
  heading, a short reassurance paragraph and one media area. The right column is a five-rung
  ladder of filled cards, each a `clamp(46px, 5vw, 62px) / 1fr` grid of rung number beside title
  and text. The fifth rung inverts to the dark fill and carries a filled button and a text link.
- **Density:** Medium.
- **Media mode:** One empty media area in the sticky column.
- **Interaction:** None. No `<script>` element. Conversion is carried by sequence and hierarchy —
  one filled button, one text link, inside the last rung.
- **Responsive strategy:** The column un-sticks and the grid stacks at 1024px, where the media
  widens to 16:9 (3:2 at 768px, 4:3 at 360px). Rungs lose their number column and go single-track
  at 480px, where the button goes full width.
- **Composer value:** The conversion register for the section, and the only layout here where the
  CTA inherits the numbering — which is what makes it read as a step rather than an advert. The
  sticky column also keeps the section's argument on screen while the ladder is read.
- **Limitation / content ceiling:** Five rungs including the CTA, so four real steps. The sticky
  column needs a ladder tall enough to travel against; with three rungs the stickiness does
  nothing. The dark final rung assumes the section is not already sitting on a dark ground.

### ARC-S06-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The project programme — the bar chart a practice issues
  alongside a fee proposal, showing which workstreams run in which stage. It is the document an
  architecture client actually receives, so the section is set as that document rather than as a
  marketing summary of it.
- **Layout model:** A bordered sheet with a hairline outline offset. A head row carries the
  eyebrow, title and a sheet reference; the body is a real `<table>` whose `colspan` cells render
  as programme bars across five phase columns (Brief, Concept, Developed, Technical, Site); a
  four-cell sheet foot closes it. Seven workstream rows, the last spanning all five phases.
- **Density:** Medium-high.
- **Media mode:** **None.** This is the only study in the sector with no media area. A programme
  is a drawing-office document, and giving it a photographic slot would misrepresent what it is.
  Recorded here so the absence is not read as an oversight during ingestion.
- **Interaction:** None. No `<script>` element. Below 768px the programme becomes a labelled,
  keyboard-focusable scroll region (`role="region"` + `tabindex="0"`) with a 660px minimum, so no
  phase column is ever dropped.
- **Responsive strategy:** First column width and bar padding tighten at 1280px and 1024px; the
  sheet foot steps 4 → 2 → 1 columns, re-assigning right and bottom borders at each step; the
  table enters its scroll region at 768px; sheet padding and outline offset step down at 360px.
- **Composer value:** The identity option, and structurally unlike anything else in the sector —
  it is the only two-dimensional layout, mapping workstreams against phases rather than listing
  stages in one direction. Gives Composer a repeatable workstream collection with a start phase
  and an end phase.
- **Limitation / content ceiling:** Five phases and about seven workstreams; more of either and
  the bars become too narrow to hold their own labels. Horizontal scrolling on phones is a
  deliberate trade. The programme convention is legible to a client who has worked with a practice
  before and may need explaining to a first-time domestic client.

## Research Metadata

- **Sources:** None. This section was authored to brief with no reference images.
- **Research date:** 2026-08-30
- **Structural territory rationale:** The five default territories were mapped onto the five ways a
  practice actually communicates process — a single line of stages for the general case, a slow
  editorial sequence for the premium case, a dossier for clients who want to know their own
  obligations, an onboarding ladder where the process itself is the sales argument, and the issued
  programme document for the discipline-native case.
- **Differentiation notes:** Five distinct geometries: a horizontal joined row, a vertical
  centre-spine alternation, stacked four-track dossier rows, a sticky column beside a filled
  ladder, and a two-dimensional phase table. Only one study is two-dimensional; only one has no
  media; only one inverts a card; only one uses a serif; only one scrolls. Stage counts differ
  (4 / 4 / 5 / 5 / 7 workstreams). Grounds differ: warm off-white, warm paper, cool grey, white,
  and drawing paper. No study uses JavaScript.
- **Sector-interpretation note:** Process sections commonly state durations ("2–3 weeks per
  stage"). No study states a duration, a fee, or a response time anywhere, since none of those can
  be true of a placeholder. Where a reference layout would have carried a duration, the cell
  carries a deliverable or a phase name instead.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, and no
  inline SVG anywhere in this batch. All type uses system font stacks.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Wide band | `ARC-S06-001` | One image closing the stage row | Still image, 21:9 (16:9 at 1024px, 3:2 at 768px, 4:3 at 480px) | Empty tonal surface with a quiet label and a `<figcaption>` stating that no completed project is implied. |
| Stage image ×4 | `ARC-S06-002` | One image per stage, alternating sides | Still image, 4:3 (16:9 at 768px, 3:2 at 480px) | Labelled empty areas; each stage's text is complete without its image. |
| Lead area | `ARC-S06-003` | One large image establishing the work above the phase grid | Still image, 21:9 (16:9 at 1024px, 3:2 at 480px) | Labelled empty area; the phase sequence reads without it. |
| Phase area ×5 | `ARC-S06-003` | One image per phase module | Still image, 4:3 (16:9 for the last two modules at 1024px, for the fifth at 768px, and for all five at 480px) | Labelled empty areas; each phase's title and line are complete without its image. |
| Column image | `ARC-S06-004` | One image in the sticky reassurance column | Still image, 4:3 (16:9 at 1024px, 3:2 at 768px) | Labelled empty area; the ladder is independent of it. |
| — | `ARC-S06-005` | **No media slot by design.** A programme is a document, not an image | — | Deliberate absence, recorded so it is not treated as an unfilled slot. |

No study contains a photograph, a logo, a client mark, or any fabricated evidence. Licensing and
provenance metadata is not applicable to this batch because no third-party asset is referenced;
it becomes required if these slots are filled before ingestion.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S06-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps; `<ol>` used
  wherever the content is a sequence, so stage order is conveyed structurally and not only by the
  numerals; every `aria-labelledby` reference resolving to a real id; every `<a>` carrying an
  `href`; the `005` programme built as a real table with `<caption>` and `scope`-qualified column
  and row headers; visible `:focus-visible` styling in all five, with an amber ring inside the
  inverted rung; and a `prefers-reduced-motion` block in all five. Contrast measured on 23 text
  and UI colour pairs: all text ≥ 4.5:1 (lowest 6.28:1) and all interactive borders ≥ 3:1 (lowest
  3.36:1). Nothing is signalled by colour or geometry alone — the `001` connecting rule and the
  `002` spine and numerals are decorative, and every `005` programme bar states its own span in
  words inside the cell, so the chart can be read without seeing the bars.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; 430 and 390 resolve through
  the 480 rules and 320 through the 360 rules. The 1280 rules in `002` and `005` were missing on
  the first pass, flagged by the structural check, and added before sign-off. Grid children use
  `minmax(0, …)`, type and spacing use `clamp()`. Two layouts change behaviour rather than merely
  shrinking: `002` moves its spine from centre to edge and switches off alternation at 768px, and
  `003` steps its phase grid from five columns to a 3 + 2 span arrangement to two to one, widening
  the modules that would otherwise be orphaned and re-proportioning both its lead and its phase
  media as it goes, so no area is ever reduced to a sliver. The only horizontal scroll in
  the batch is the `005` programme, which is intentional, labelled and keyboard reachable.
  Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Copy-policy validation: PASS.** Visible text extracted and scanned for awards, certifications,
  accreditations, rankings, percentages, guarantees, ratings, testimonial language, fees, prices,
  client counts, and — specific to this section — durations in days, weeks or months. The only
  numeric strings in visible text are the study ID in each `<title>` and the stage numbers.
- **Structural-diversity validation: PASS.** Five distinct geometries, checked against each other
  and against the twenty-seven studies already authored in `ARC-S01`–`ARC-S05`, so no device is
  reused across sections. No study is a cosmetic variation of another.
- **Rework QA — `ARC-S06-003`: PASS.** Re-validated after the rework: one `<h1>` and five `<h2>`s
  with no level jump; `<ol>`/`<li>` retained so phase order is structural and the CSS-counter
  numerals are presentational only; `aria-labelledby` resolving; no `<script>`; zero external,
  remote or `url()` references; CSS scoped to `.arc-s06-003` apart from the two-line host baseline;
  the 1280 / 1024 / 768 / 480 / 360 ladder intact with `minmax(0, …)` on every grid track. Contrast
  re-measured on the reduced palette: body and phase copy `#53565c` on `#f4f4f2` at 6.67:1, slot
  labels `#4b4d51` on `#dedddb` at 7.04:1, titles near-maximal — all text ≥ 4.5:1, and the study
  now carries no bordered or interactive component. Visible copy fell from 187 words to 93. Rendered and checked at 1440, 1280, 1024, 768, 430,
  390 and 320px.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- This is the first section in the sector authored without reference images. Diversity was
  therefore controlled explicitly rather than inherited, and the devices deliberately avoided are
  listed under Authoring Direction so a later reviewer can see what the set was measured against.
- `ARC-S06-005` is the first study in the sector with no media area at all. That is a deliberate
  decision about what a programme is, recorded in the Media Slots table so it is not read as an
  incomplete study.
- Section studies carry the section title as the document `<h1>` and stage titles as `<h2>`,
  following the convention set in `ARC-S03`. `ARC-S06-005` has no `<h2>` because its stages are
  table headers rather than headings.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
