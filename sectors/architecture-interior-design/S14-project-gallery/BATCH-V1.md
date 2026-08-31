# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S14`
- Section Name: `Project Gallery`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S14-001` | Universal / Safe | AUTHORED | `raw/ARC-S14-001.html` |
| `ARC-S14-002` | Premium / Editorial | AUTHORED | `raw/ARC-S14-002.html` |
| `ARC-S14-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S14-003.html` |
| `ARC-S14-004` | Conversion-led | AUTHORED | `raw/ARC-S14-004.html` |
| `ARC-S14-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S14-005.html` |

## Authoring Direction

**No reference images were supplied.** Authored to brief in the sector's established register and
checked against the studies already in the sector so no device is reused. See the S02 / S13 / S14 /
S24 boundary table in `../S13-featured-project-case-study/BATCH-V1.md`: this section is image-led.
`S02` indexes projects with metadata and `S13` features one project in depth; `S14` shows the work
itself and captions it.

### The slot problem

This is the one section in the catalog where **media is the content**. Every study is therefore
mostly empty slot, which creates two risks the batch is designed around:

- **A gallery of empty rectangles is unreviewable.** So each study varies its slot *proportions*
  deliberately rather than repeating one ratio, and states the ratio in each slot label — the shape
  of the arrangement is legible even with nothing in it. The exception is `003`, where a single
  shared ratio is the point.
- **A gallery invites captions that claim.** Captions here name a placeholder project record and a
  view. No client, address, date, cost, area, award or completed-project claim appears in any of
  the five, and a scan confirms it.

## Study Records

### ARC-S14-001 — Universal / Safe

- **Structural intent / archetype:** A captioned wall of work at four sizes, so the arrangement has
  a rhythm rather than a repeat.
- **Layout model:** A split head over a six-column grid carrying eight cells at four span widths
  (`span 6` at 21:9, `span 4` at 16:9, `span 3` at 4:3, `span 2` at 3:4), each with a caption
  pairing the project record and the view.
- **Density:** Medium. Eight images.
- **Media mode:** Eight empty cells at four spans.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Six columns → four at 1024px → two at 768px → one at 480px, with each
  span class remapped at every step so no cell ever lands narrower than half the grid.
- **Composer value:** The safest binding target — a repeatable `{image, record, view, span}`
  collection. The span field is what stops a filled gallery reading as a contact sheet.
- **Limitation / content ceiling:** Eight cells is the tested arrangement; the four span sizes are
  hand-balanced and a ninth cell needs the sequence re-tuned.

### ARC-S14-002 — Premium / Editorial

- **Structural intent / archetype:** A sequence, not a grid. One plate at a time, at the size a
  monograph would print it, with the caption on a hairline beneath.
- **Layout model:** A ruled head over four stacked plates at alternating proportions — 3:2, 4:5,
  21:9, 1:1 — with the two portrait plates inset to a narrower measure, the last of them pushed to
  the right margin. Captions are three-track: plate number, description, project record.
- **Density:** Low. Four images.
- **Media mode:** Four large empty plates, deliberately at four different proportions.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The inset margins widen at 1280px and 1024px and are dropped entirely at
  768px, because a margin that no longer exists cannot hold an inset plate; the wide plate relaxes
  to 16:9 at the same width.
- **Composer value:** The premium register, and the only study here where plate proportion and
  position are per-image content rather than grid settings.
- **Limitation / content ceiling:** Four plates. The sequence is composed, not generated: adding a
  fifth means deciding its proportion and its margin by hand.

### ARC-S14-003 — Dense / Information-heavy

- **Structural intent / archetype:** The contact sheet. Everything at one size, numbered, with a
  keyed legend — the sheet a practice actually looks at when choosing what to publish.
- **Layout model:** A bordered sheet with a monospace head, a six-column grid of eighteen frames
  **all at 3:2**, each numbered in its corner, and a three-column keyed legend listing all eighteen
  with the project record each belongs to.
- **Density:** High — eighteen frames, the largest media set in the sector.
- **Media mode:** Eighteen empty frames at a single shared ratio. Uniformity is the device: a
  contact sheet compares, and a sheet of mixed crops cannot.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Frames step 6 → 4 → 3 → 2 columns and the legend 3 → 2 → 1, so the sheet
  stays a sheet rather than becoming a stack of large images.
- **Composer value:** The highest-capacity option and the closest to how a practice stores images:
  a flat numbered set with a lookup, rather than a curated arrangement.
- **Limitation / content ceiling:** Eighteen frames at six columns is the tested shape. Frames are
  small by design and carry no caption of their own — the legend is not optional here, it is how
  the sheet is read.

### ARC-S14-004 — Conversion-led

- **Structural intent / archetype:** Interrupt the looking once, while it is still happening, with
  the only thing the studio is asking for.
- **Layout model:** A split head over a three-cell gallery row, a full-width inverted band carrying
  a project-book offer at `1.35fr / 1fr`, then a second three-cell row continuing the same grid.
- **Density:** Medium. Six images.
- **Media mode:** Six empty cells at 4:3, split three above and three below the band.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Rows go 3 → 2 columns at 768px with the third cell spanning and widening
  to 16:9, then single-column at 480px; the band stacks at 1024px.
- **Composer value:** The conversion register. Placing the offer *between* rows rather than after
  them is the study's whole argument, and it gives Composer an interstitial slot most gallery
  models do not have.
- **Limitation / content ceiling:** Three cells per row and one band. A second interstitial would
  turn the gallery into an advert with pictures.
- **Policy note:** the offer is a project book, which a studio can actually send. It states no page
  count, no delivery time and no cost, because none can be true of a placeholder.

### ARC-S14-005 — Sector-native / Distinctive

- **Structural intent / archetype:** Ordered by scale rather than by project or date. An architect
  reads work from the situation inward — site, building, room, detail — and a gallery arranged that
  way says what the practice pays attention to.
- **Layout model:** A bordered sheet with a monospace head and preamble, then four scale bands. Each
  band is a `clamp(96px, 13vw, 168px) / 1fr` grid: a scale stop on the left with a tick, a rule and
  a label, and the images taken at that scale on the right. Band proportions narrow as the scale
  closes — 21:9 at Situation, 3:2 at Building, 4:3 at Room, 1:1 at Detail.
- **Density:** Medium-high. Nine images across four bands.
- **Media mode:** Nine empty areas, sized so the ordering is visible in the images themselves and
  not only in the axis labels.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The axis stop moves from a left column to a rule above its own band at
  768px — its `::before` rotates from a vertical rule to a horizontal one — rather than shrinking
  to an unreadable column. Bands then go two-up and finally single-column.
- **Composer value:** The identity option, and an eleventh sector-native register for the sector.
  Its content model adds one field most gallery models lack: a scale for each image, which is what
  makes the ordering possible.
- **Limitation / content ceiling:** Four scales and nine images. The narrowing proportions are the
  device, so a band filled with the wrong crop breaks the reading — a detail shot at 21:9 in the
  Situation band would undo the whole arrangement.

## Research Metadata

- **Sources:** None. Authored to brief.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five ways a practice shows
  images — a captioned wall at mixed sizes, a printed sequence, the working contact sheet, a wall
  interrupted by an offer, and an arrangement ordered by scale.
- **Differentiation notes:** Five distinct geometries and, unusually for this catalog, five distinct
  *media strategies*: mixed spans, alternating inset proportions, one shared ratio, split rows, and
  proportions that narrow with scale. Grounds differ: near-white, warm paper, contact-sheet paper,
  warm with a dark band, and drawing paper. No study uses JavaScript.
- **Sector-interpretation note:** Because media is the content here, the batch's real design work
  was in the slot proportions rather than the surrounding chrome. That is recorded under the slot
  problem above.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, no inline
  SVG, and no inline `style` attribute in any of the five files.
- Network calls: NONE.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Gallery cell ×8 | `ARC-S14-001` | Eight views across five project records | Still image at four ratios: 21:9, 16:9, 4:3, 3:4 | Each slot label states its ratio; every cell is captioned with record and view. |
| Plate ×4 | `ARC-S14-002` | Four sequenced plates | Still image at 3:2, 4:5, 21:9, 1:1 — proportion is per-plate content | Portrait plates are inset to a narrower measure at wide widths and released below 768px. |
| Frame ×18 | `ARC-S14-003` | A full contact sheet | Still image, **all at 3:2** | The shared ratio is required, not stylistic: mixed crops cannot be compared. Frames carry numbers only; the legend supplies the caption. |
| Gallery cell ×6 | `ARC-S14-004` | Six views split by the offer band | Still image, 4:3 (16:9 for the spanning third cell at 768px) | Labelled and captioned; the band between the rows is content, not a slot. |
| Scale image ×9 | `ARC-S14-005` | Nine images distributed across four scale bands | Still image, ratio **set by the band**: 21:9 site, 3:2 building, 4:3 room, 1:1 detail | Filling a band with a crop from another scale breaks the ordering, which is the study's only content requirement. |

No study contains a photograph, a logo, a client mark, or any fabricated evidence. Filling these
slots means using photography the studio holds the rights to, credited where the photographer
requires it.

## QA

- **ID validation: PASS.** All five IDs exist with matching `<meta name="study-id">`,
  `data-study-id`, scoped root class and filename. Every element `id` is namespaced.
- **Raw-format validation: PASS.** Five standalone `.html` files; tag balance, nesting and unique-id
  checks pass. Scans for unscoped CSS rules and inline `style` attributes both return zero.
- **Accessibility QA: PASS.** One `<h1>` per study and no heading-level jumps. Every
  `aria-labelledby` resolves, every `<a>` carries an `href`, the `003` frame grid carries an
  `aria-label` describing what it is, `:focus-visible` styling is present in all five with an amber
  ring inside the dark band, and every study carries a `prefers-reduced-motion` block. Contrast
  measured on 12 pairs against each study's own ground: all text ≥ 4.5:1 (lowest 6.56:1) and all
  interactive borders ≥ 3:1 (lowest 4.03:1).
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder. Two layouts change behaviour rather than
  shrinking: `002` drops its inset plate margins at 768px, and `005` rotates its scale axis from a
  left column to a rule above each band. No horizontal scroll anywhere.
- **Dependency validation: PASS.** Zero matches across all five files.
- **Claim-policy validation: PASS.** Visible text scanned for client, address, date, cost, area and
  award claims, currency symbols, percentages, square-measure units and company suffixes. The only
  match is the word "client" inside two studies' own disclaimer sentences.
- **Structural-diversity validation: PASS.** Five distinct geometries and five distinct media
  strategies, checked against the sector's earlier studies by recorded metadata.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- The slot problem above is the thing to read before filling this section. In particular: `003`
  requires one shared ratio, and `005` requires the crop to match the band it sits in.
- `ARC-S14-005` adds an eleventh sector-native register — ordering by scale.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
- Workspace roll-up counters in `planning/` still read `NOT_STARTED` for this sector and need a
  separate workspace-level pass.
