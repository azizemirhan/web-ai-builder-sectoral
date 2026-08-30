# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S11`
- Section Name: `Materials & Sustainability`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S11-001` | Universal / Safe | AUTHORED | `raw/ARC-S11-001.html` |
| `ARC-S11-002` | Premium / Editorial | AUTHORED | `raw/ARC-S11-002.html` |
| `ARC-S11-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S11-003.html` |
| `ARC-S11-004` | Conversion-led | AUTHORED | `raw/ARC-S11-004.html` |
| `ARC-S11-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S11-005.html` |

## Authoring Direction

**No reference images were supplied.** As with `ARC-S10`, the direction was to work in the sector's
established language, so the batch inherits the house style set out in that section's batch
document — system stacks with monospace for technical labels, warm paper and cool grey grounds,
`clamp()` ramps, `minmax(0, …)` tracks, the 1280 / 1024 / 768 / 480 / 360 ladder, section title as
`<h1>`, and a closing placeholder note — and avoids every device already carrying another section.

One new mechanism enters the sector here: a **sticky in-page anchor rail** in `003`.

### The claim problem, which is worse here than anywhere else

`ARC-S09` had to avoid fabricating awards. This section has to avoid fabricating *environmental
performance*, which is the same failure with a larger consequence: a plausible-looking
certification, percentage or carbon figure on a placeholder page is greenwashing, and it is the
kind of copy that gets pasted into a live site unchanged because it reads as finished.

Four rules were applied to every study, and a scan enforces them:

- **No certification or rating scheme.** No assessment method, standard, label or accreditation is
  named — not a real one, and not a plausible invented one.
- **No figures.** No percentage, no carbon or energy value, no thickness, no U-value, no
  temperature, no count. Where a real practice would state a measured number, this batch leaves the
  field absent rather than filling it with something that looks right.
- **Methods, not results.** Materials are described by what the studio *asks of them* — that origin
  can be documented, that a part can be replaced, that a layer can be separated at end of life.
  Those are commitments a studio controls, not outcomes it would have to prove.
- **No product, brand or supplier names.** Naming a manufacturer on a placeholder page is an
  endorsement the studio never gave.

`ARC-S11-003` takes this furthest: every entry carries an **Evidence** field and every one of them
reads "To be supplied by the studio". That is the field where a practice records a declaration, a
test result or a supplier document, and filling it here with a plausible value would manufacture
exactly the evidence the section exists to carry. Leaving it visibly empty is the design.

## Study Records

### ARC-S11-001 — Universal / Safe

- **Structural intent / archetype:** The palette as a short list of squares — what the studio uses,
  where it uses it, and what it asks of each material before specifying it.
- **Layout model:** A split head over a three-column grid. Each cell is a square sample slot, a
  material name, and a two-pair definition list: "Used for" and "What we ask of it".
- **Density:** Medium. Six materials.
- **Media mode:** Six empty **square** sample areas. A square is a sample; a landscape rectangle is
  a project photograph, and the two invite different content.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Three columns → two at 1024px → one at 480px, where the square becomes
  16:10 because a full-width square on a phone pushes the caption off screen.
- **Composer value:** The safest binding target — six records of `{sample, name, use, requirement}`.
  The requirement field is what keeps the section from becoming a mood board.
- **Limitation / content ceiling:** Six materials; a seventh unbalances the three-column grid. Two
  fields each. No place for evidence, sourcing or maintenance — `003` carries those.

### ARC-S11-002 — Premium / Editorial

- **Structural intent / archetype:** The materials board as a studio actually pins one — samples at
  different sizes, unevenly weighted — beside the four questions a material has to answer.
- **Layout model:** A bordered board holding five swatches on a six-column grid at four different
  span sizes, beside a serif statement column with a numbered rule list.
- **Density:** Low-medium. Five samples, four questions.
- **Media mode:** Five empty sample areas at four sizes. The uneven sizing is the point: a board is
  pinned, not gridded.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The board's mixed sizing is abandoned at 480px — every swatch resets to
  the same square cell in two columns, with only the lead sample spanning — because five different
  span sizes on a phone produces slivers rather than samples.
- **Composer value:** The premium register, and the only study here where sample sizes are
  deliberately unequal, which is how a studio signals which material leads the palette.
- **Limitation / content ceiling:** Five samples and four questions; the board's balance is
  hand-tuned to those spans and does not generalise to six or seven. No per-material text at all —
  the board is looked at, the column is read.

### ARC-S11-003 — Dense / Information-heavy

- **Structural intent / archetype:** The written record behind the palette. What a practice would
  actually hand over: use, finish, maintenance, end-of-life, and the evidence for each.
- **Layout model:** A ruled head over a `0.3fr / 1.5fr` body. The left column is a **sticky anchor
  rail** listing the three categories with entry counts; the right column is the record, grouped
  under anchored headings, each entry a card with a five-field definition grid.
- **Density:** High — six entries × five fields, the largest content set in the section.
- **Media mode:** None. This is the record behind the palette; the samples are shown in `001` and
  `002`.
- **Interaction:** None. No `<script>` element. The rail is a list of in-page anchors, so navigating
  a long section needs nothing but links — the first sticky anchor index in the sector. Group
  headings carry `scroll-margin-top` so an anchored heading is not hidden under the sticky rail.
- **Responsive strategy:** The rail un-sticks and becomes a two-column list at 1024px, then one
  column at 480px; field pairs go two columns → one at 768px and stack label over value at 480px.
- **Composer value:** The highest-capacity option, and the only one modelling **evidence** as a
  first-class field. A content model built from this study cannot quietly omit provenance.
- **Limitation / content ceiling:** Three categories of two entries is the tested shape; the pattern
  scales but the rail's usefulness falls off past about eight categories. Five fields per entry.
- **Policy note:** every Evidence field is deliberately unfilled — see Authoring Direction.

### ARC-S11-004 — Conversion-led

- **Structural intent / archetype:** Surfaces are hard to judge on a screen, so the conversion is a
  request for something physical and checkable — a sample set and the written note that goes with
  it — rather than a claim about performance.
- **Layout model:** A tinted band holding a large sample-box area beside a heading, a four-item
  numbered contents list, and paired actions.
- **Density:** Medium.
- **Media mode:** One large empty area standing for a **physical sample box**, not a project image.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Band stacks at 1024px with the box capped at 460px; the box goes 16:10 at
  768px and 4:3 at 480px where the primary action goes full width.
- **Composer value:** The conversion register, and the only one in the sector offering a physical
  artefact. Its content model is `{contents list, primary action, secondary action}` — small, and
  entirely about what the studio will send.
- **Limitation / content ceiling:** Four contents lines. Nothing states delivery time, cost or
  availability — deliberately, since none can be true of a placeholder, so a studio must add them.
  The offer only works if the sample set and the written statement actually exist.

### ARC-S11-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The annotated section detail — the drawing a practice issues to
  show what a wall is made of, layer by layer, with numbered annotations running out to the margin.
  It is the one drawing type where materials and their order are the entire subject, which makes it
  the honest form for this section.
- **Layout model:** A bordered sheet with a monospace head and preamble, then five layer rows. Each
  row is a three-track grid: a **band** whose height is the drawn thickness of that layer, a
  **leader** (a hairline with a node) crossing the margin, and a numbered annotation. Bands share
  borders so the build-up reads as one continuous section. A key and sheet foot close it.
- **Density:** Medium-high.
- **Media mode:** None. The build-up is drawn in CSS from bands and rules; it is a drawing, not an
  image slot, and must not be replaced with a photograph.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** A leader line needs horizontal room to mean anything, so at 768px the
  leader is dropped entirely and each annotation moves under its own band — rather than leaving a
  pointer that travels a few pixels. Bands close their bottom border at that width so each still
  reads as a discrete layer.
- **Composer value:** The identity option, and an eighth distinct sector-native register for the
  sector. Its content model is an ordered `{layer, thickness weight, title, note}` list, which is
  the shape of a build-up specification.
- **Limitation / content ceiling:** Five or six layers; more and the bands lose their relative
  weight. Band heights are indicative, not to scale, and the sheet says so — a real detail would be
  drawn to scale with dimensions. Annotations run to about twenty-five words.

## Research Metadata

- **Sources:** None. Authored to brief, informed by a metadata survey of the studies already in the
  sector.
- **Research date:** 2026-08-30
- **Structural territory rationale:** Territories were mapped onto the five ways a practice presents
  material thinking — the palette for the general case, the pinned board for the premium case, the
  written record for the dense case, a physical sample set for the conversion case, and the
  annotated build-up for the discipline-native case.
- **Differentiation notes:** Five distinct geometries — a square palette grid, an unevenly spanned
  board, a sticky rail beside a grouped record, an offer band, and a layered section drawing. Media
  differs in kind, not just count: squares, mixed-span swatches, none, a sample box, and a drawing.
  Grounds differ: near-white, warm paper, cool grey, white with a tinted band, and drawing paper.
  No study uses JavaScript.
- **Sector-interpretation note:** This is the highest claim-risk section in the sector. The
  substantive design decision was what *not* to state — see the claim problem above. It is also why
  three of five studies carry no figures at all and the fourth makes their absence explicit.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, no inline
  SVG. The `005` build-up is drawn from background colours and borders.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Sample ×6 | `ARC-S11-001` | One material sample per palette entry | Still image of a **material sample**, 1:1 (16:10 at 480px) | Labelled empty areas. A square invites a sample; filling it with a project photograph changes what the section claims. |
| Board sample ×5 | `ARC-S11-002` | Five samples pinned at four sizes on one board | Still image of a material sample, spans of 4×3, 2×2, 2×1 and 3×2 cells | Labelled empty areas; the caption states the count and that sizes vary. Sizes reset to equal squares at 480px. |
| Sample box | `ARC-S11-004` | One image of the physical sample set the studio sends | Still image, 5:4 (16:10 at 768px, 4:3 at 480px) | Labelled empty area with a monospace caption; the offer list carries the content. |
| — | `ARC-S11-003` | **No media slot by design** | — | The written record; samples live in `001` and `002`. |
| — | `ARC-S11-005` | **No media slot by design** | — | The build-up is a drawing made of bands and rules. **Do not replace it with a photograph** — a photograph of a wall shows the outer layer only, which is the opposite of what the study is for. |

No study contains a photograph, a product mark, a certification label, or any fabricated evidence.
Licensing and provenance metadata is not applicable because no third-party asset is referenced; it
becomes required if these slots are filled.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S11-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting and unique-id
  checks pass on all five. All CSS is namespaced to the study root class; a scan for unscoped rules
  returns zero across the batch, excluding the documented two-line host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps — `003` runs
  three levels because its entries sit under category headings. Every `aria-labelledby` and every
  in-page anchor in `003` resolves to a real id, and its group headings carry `scroll-margin-top` so
  an anchored heading is not hidden beneath the sticky rail. Every `<a>` carries an `href`. Visible
  `:focus-visible` styling and a `prefers-reduced-motion` block in all five. Contrast measured on 13
  pairs against each study's own ground: all text ≥ 4.5:1 and all interactive borders ≥ 3:1. The
  `005` deepest layer band initially measured 4.16:1 against its label and was lightened to 4.65:1
  before sign-off.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder. Two layouts change behaviour rather than
  shrinking: `002` resets its mixed swatch spans to equal cells at 480px, and `005` drops its leader
  lines and moves each annotation under its own band at 768px. No horizontal scroll anywhere.
  Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs, `@import`,
  `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`, `crossorigin`, and
  `<script`. Zero matches across all five files.
- **Claim-policy validation: PASS — the key check for this section.** Visible text scanned for named
  assessment methods and standards, accreditation and certification language, "net zero" and
  "carbon neutral" phrasing, eco- and green- prefixed claims, percentages, carbon, energy and
  U-value figures, and named software or product vendors. The only matches are the word
  "certification" inside each study's own disclaimer sentence; every occurrence was checked in
  context and every one is a negation ("No certification, rating scheme, standard, carbon figure …
  appears"). No study states a figure of any kind.
- **Structural-diversity validation: PASS.** Five distinct geometries, checked against the earlier
  studies by their recorded `layout-model` and `interaction` metadata.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- The claim problem above should be read before any of these studies is filled. The three places it
  bites hardest: the `003` Evidence fields, which are meant to stay visibly empty until a studio has
  real documents; the `001` requirement line, which is a method and not a result; and the `005`
  build-up, which states that its bands are indicative and not to scale.
- `ARC-S11-005` adds an eighth sector-native register — the annotated build-up — alongside the
  drawing sheet, specification clause, project programme, monograph colophon, practice register,
  bibliography and schedule of services.
- `ARC-S11-003` is the first sticky in-page anchor rail in the sector.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
