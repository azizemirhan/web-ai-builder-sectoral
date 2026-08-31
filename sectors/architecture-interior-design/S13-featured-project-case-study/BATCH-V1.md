# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S13`
- Section Name: `Featured Project Case Study`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S13-001` | Universal / Safe | AUTHORED | `raw/ARC-S13-001.html` |
| `ARC-S13-002` | Premium / Editorial | AUTHORED | `raw/ARC-S13-002.html` |
| `ARC-S13-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S13-003.html` |
| `ARC-S13-004` | Conversion-led | AUTHORED | `raw/ARC-S13-004.html` |
| `ARC-S13-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S13-005.html` |

## Authoring Direction

**No reference images were supplied.** Authored to brief in the sector's established register, and
checked against the 61 studies already in the sector by their recorded `layout-model` and
`interaction` metadata so no device is reused.

### What this section is, and what it is not

Three sections in this catalog concern project work and they are easy to collapse into each other:

| Section | Holds | Shape |
| --- | --- | --- |
| `S02` Selected Projects | Many projects | An index with metadata |
| `S13` Featured Project Case Study | **One** project, in depth | A section that must be complete in a few screens |
| `S14` Project Gallery | The images themselves | Image-led, captioned |
| `S24` Project / Case Study Detail | One project | The whole **page**, not a section |

Every study here is written against that boundary. `001` says it explicitly in its own copy — a
case study that needs six paragraphs has become a project detail page.

### The claim problem

A featured case study attracts six claims at once: client, address, date, cost, area and award.
None appears in any study, and a scan for all six plus currency symbols, areas, percentages,
"completed in", "under budget" and company suffixes returns nothing. The `003` credits block is
the sharpest case: it names **roles** and leaves consultant, contractor and photographer as
placeholders, because crediting a real practice on a placeholder project would credit work nobody
did.

## Study Records

### ARC-S13-001 — Universal / Safe

- **Structural intent / archetype:** Lead image, then the facts beside the account. The most
  reusable shape for featuring one project inside a page.
- **Layout model:** Eyebrow and title over a 21:9 lead band, then a `0.42fr / 1.5fr` body pairing a
  six-row metadata rail with a two-part narrative, closed by a supporting image pair and a
  next-project link.
- **Density:** Medium.
- **Media mode:** One wide lead area plus two supporting areas.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Body stacks at 1024px where the lead goes 16:9, then 3:2 at 768px and
  4:3 at 480px where the supporting pair goes single-column and the foot stacks.
- **Composer value:** The safest binding target — one project record with `{title, six facts, two
  narrative parts, three media, one onward link}`, which is the field set most case-study content
  models already hold.
- **Limitation / content ceiling:** Six metadata rows and two narrative parts. A third part pushes
  the supporting pair below the fold and the section starts becoming a page.

### ARC-S13-002 — Premium / Editorial

- **Structural intent / archetype:** Keep the room in view while reading what was done to it. One
  image is held in place and the account travels past it.
- **Layout model:** A ruled head over a `0.92fr / 1fr` body. The media column is `position: sticky`;
  the narrative runs a controlled measure with a serif opening, a rule-bounded pull line breaking
  the column, and a four-row mark list closing it.
- **Density:** Low-medium.
- **Media mode:** One tall held media area with a caption fixed beneath it.
- **Interaction:** None. No `<script>` element. The held column is a scroll relationship rather
  than a script, and this is the first study in the sector to hold **media** — `ARC-S06-004` and
  `ARC-S09-004` hold panels of controls, `ARC-S11-003` holds a navigation rail.
- **Responsive strategy:** Holding is released entirely at 1024px, because a sticky element needs
  a taller column to travel against and below that width there is nothing to travel against.
- **Composer value:** The premium register. The smallest field set here — one image, one narrative,
  one pull line — and the only layout whose composition depends on scroll position.
- **Limitation / content ceiling:** Roughly six paragraphs before the held image runs out of column
  to hold against. One pull line. Needs an image worth holding for the length of the read.

### ARC-S13-003 — Dense / Information-heavy

- **Structural intent / archetype:** The dossier. Facts first, account second, decisions listed in
  order, credits named by role — the way a practice reads someone else's project.
- **Layout model:** A ruled head over a six-cell hairline fact grid, then a `1fr / 1.1fr` body
  pairing a three-paragraph account with a five-step decision list, a three-column credits block,
  and a closing three-plate strip.
- **Density:** High — the largest content set in the section.
- **Media mode:** Three small plates in a closing strip, captioned existing / during / detail.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Fact grid steps 6 → 3 → 2 → 1 columns; body and credits stack at 1024px
  and 768px; at 480px the decision list and every credit pair go single-column.
- **Composer value:** The highest-capacity option, and the only one modelling **credits** as a
  first-class block — the field most case-study templates omit and most practices are contractually
  required to publish.
- **Limitation / content ceiling:** Six facts, five decisions, six credits, three plates. Beyond
  that the dossier stops being readable in a section.
- **Policy note:** credits name roles, not firms; consultant, contractor and photographer are
  placeholders.

### ARC-S13-004 — Conversion-led

- **Structural intent / archetype:** A case study that closes on its own beginning. Instead of
  claiming a result, it shows the sentence the project started from and offers the same first step.
- **Layout model:** Eyebrow and title over a 21:9 band, then a two-column "how it started / where it
  went" pair — the left column carrying the opening line and a before image, the right the account —
  closed by an inverted panel at `1.3fr / 1fr` with a filled action and a text link.
- **Density:** Medium.
- **Media mode:** One wide band plus one supporting area inside the starting column.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The band steps 21:9 → 16:9 → 3:2 → 4:3; the pair stacks at 768px; the
  panel becomes one column at 1024px and its secondary link stretches at 480px.
- **Composer value:** The conversion register, and the only case study in the sector that converts
  without an outcome claim. Its content model is `{opening line, account, first-step offer}`.
- **Limitation / content ceiling:** Two columns of about three paragraphs each. The opening line has
  to be a real sentence a client said, which is the one field a studio cannot invent.
- **Policy note:** an outcome claim is the obvious temptation in a conversion-led case study, and
  the study states in its own closing note that it does not make one.

### ARC-S13-005 — Sector-native / Distinctive

- **Structural intent / archetype:** Existing and proposed, side by side. The comparison an
  architect makes on every project involving a building that already stands, and the one
  presentation where the honesty of the pairing is the whole point.
- **Layout model:** A bordered sheet with a monospace head and preamble, then two comparison
  units. Each is a matched plate pair — existing left, proposed right, **at the same ratio** — with
  a labelled header per side, a numbered annotation reading across the divide, and a four-row
  schedule of change closing the sheet.
- **Density:** Medium-high.
- **Media mode:** Four plates in two matched pairs, deliberately at one shared ratio.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The pair **never stacks** — two plates one above the other are not a
  comparison — so the plates narrow instead, going 4:3 → 1:1 at 768px → 3:4 at 480px. The schedule
  drops its reason column to a second line at 768px rather than the pair breaking.
- **Composer value:** The identity option, and a tenth distinct sector-native register for the
  sector. Its content model is a paired collection with a change schedule:
  `{existing plate, proposed plate, annotation}` plus `{ref, what changed, why}`.
- **Limitation / content ceiling:** Two pairs and four schedule rows. Both plates in a pair must be
  taken from the same position at the same ratio, and the sheet says so — an unmatched pair
  flatters the proposal instead of explaining it, which is the specific dishonesty this layout
  invites.

## Research Metadata

- **Sources:** None. Authored to brief, informed by a metadata survey of the studies already in the
  sector.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five ways a practice features
  one project — facts beside an account for the general case, a held image for the premium case, a
  dossier for the dense case, the opening conversation for the conversion case, and the
  existing/proposed comparison for the discipline-native case.
- **Differentiation notes:** Five distinct geometries — lead band with metadata rail, held sticky
  media, hairline fact grid with staged decisions, started/became pair with an inverted panel, and
  a matched comparison sheet. Grounds differ: warm off-white, warm paper, cool grey, white with a
  dark panel, and drawing paper. Only one holds media on scroll; only one refuses to stack a pair;
  no study uses JavaScript.
- **Sector-interpretation note:** The substantive decision in this section was where it stops.
  Every study is written so that it features a project rather than replacing the page about it, and
  `001` and `002` both say so in their own copy.

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
| Lead band | `ARC-S13-001` | One wide lead image for the project | Still image, 21:9 (16:9 at 1024px, 3:2 at 768px, 4:3 at 480px) | Labelled empty area with a caption stating no completed project is implied. |
| Supporting pair | `ARC-S13-001` | Two supporting images inside the narrative | Still image, 4:3 | Labelled empty areas; the narrative is complete without them. |
| Held plate | `ARC-S13-002` | One image held while the account is read | Still image, 4:5 (16:10 at 1024px, 3:2 at 768px) | Labelled empty area; holding is released below 1024px so the caption never separates from it. |
| Plate strip ×3 | `ARC-S13-003` | Existing, during and completed-detail views | Still image, 4:3 | Labelled empty areas with captions; the dossier carries the information load. |
| Band + before | `ARC-S13-004` | One wide lead plus one "before" image in the starting column | Still image, 21:9 and 16:10 | Labelled empty areas. |
| Matched pairs ×4 | `ARC-S13-005` | Two existing/proposed pairs | Still image, **both plates in a pair at the same ratio, from the same position** | This is the strictest slot in the sector: a mismatched pair is not a comparison. The sheet states the requirement and the plates share one aspect ratio at every breakpoint. |

No study contains a photograph, a logo, a client mark, or any fabricated evidence.

## QA

- **ID validation: PASS.** All five IDs exist with matching `<meta name="study-id">`,
  `data-study-id`, scoped root class and filename. Every element `id` is namespaced.
- **Raw-format validation: PASS.** Five standalone `.html` files; tag balance, nesting and unique-id
  checks pass. Scans for unscoped CSS rules and inline `style` attributes both return zero.
- **Accessibility QA: PASS.** One `<h1>` per study, no heading-level jumps — `003` runs three levels
  because its decision list sits under a section heading. Every `aria-labelledby` resolves, every
  `<a>` carries an `href`, `:focus-visible` styling is present in all five with an amber ring inside
  the dark panel, and every study carries a `prefers-reduced-motion` block. Contrast measured on 15
  pairs against each study's own ground: all text ≥ 4.5:1 (lowest 5.95:1) and all interactive
  borders ≥ 3:1 (lowest 3.68:1).
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder. Two layouts change behaviour rather than
  shrinking: `002` releases its held media at 1024px, and `005` refuses to stack its comparison
  pair at any width, narrowing the plates and dropping the schedule's reason column instead. No
  horizontal scroll anywhere.
- **Dependency validation: PASS.** Zero matches for `http:`, `https:`, `@import`, `src=`, `<link>`,
  `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest` or `<script` across all five files.
- **Claim-policy validation: PASS.** Visible text scanned for client, address, date, cost, area and
  award claims, plus currency symbols, percentages, square-measure units, "completed in", "under
  budget", company suffixes and rating language. The only matches are the words "client" and
  "award" inside each study's own disclaimer sentence and the generic phrase "a prospective
  client"; every "award" occurrence was checked at sentence level and every one is a negation.
- **Structural-diversity validation: PASS.** Five distinct geometries, checked against the sector's
  61 earlier studies by recorded metadata.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- The S02 / S13 / S14 / S24 boundary table above should be read before any of these studies is
  filled; the failure mode for this section is quietly becoming a project detail page.
- `ARC-S13-005` adds a tenth sector-native register — the existing/proposed comparison — and
  carries the sector's strictest media requirement.
- `ARC-S13-002` is the sector's first sticky **media** column.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
- Workspace roll-up counters in `planning/` still read `NOT_STARTED` for this sector and need a
  separate workspace-level pass.
