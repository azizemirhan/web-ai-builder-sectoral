# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S07`
- Section Name: `Studio About`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S07-001` | Universal / Safe | AUTHORED | `raw/ARC-S07-001.html` |
| `ARC-S07-002` | Premium / Editorial | AUTHORED | `raw/ARC-S07-002.html` |
| `ARC-S07-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S07-003.html` |
| `ARC-S07-004` | Conversion-led | AUTHORED | `raw/ARC-S07-004.html` |
| `ARC-S07-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S07-005.html` |

## Authoring Direction

Five visual-direction reference images were supplied. As in the earlier reference-led sections,
the direction was to follow the supplied layouts rather than abstract from them, and to leave
every image area empty.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S07-001` | Reference 2 | Centred label above a four-tile image mosaic beside a heading and paragraph, closed by a three-cell fact row |
| `ARC-S07-002` | Reference 1 | Top rail of small captions and labels, oversized two-line display heading overlapped by a large image with a smaller one beside it, then a bracketed label above a large belief statement with two closing captions |
| `ARC-S07-003` | Reference 4 | Deep-toned section: small label, large image left, italic-accented heading with paragraph right, four-cell fact row along the bottom paired with two small images |
| `ARC-S07-004` | Reference 3 | Oversized uppercase display statement with a bordered pill in the top-right corner, a dark round action at the lower left, and an image beside a two-column paragraph block |
| `ARC-S07-005` | Reference 5 | Oversized wordmark with a small pill beside it, one long statement with the studio name in italic, a tall image at the lower left, and a rail of short uppercase labels along the bottom |

### Policy substitutions

This section's references carried more unverifiable material than any previous set, so the
substitutions are listed individually:

- **Reference 2** counts "10 Years / 200+ Projects / 75 Reviews" in its fact row. The row and its
  rhythm are kept; the values are qualitative ("Independent / Practice").
- **Reference 4** counts "25 Projects / 100+ Awards / 240+ / 20 Years Experience". Same treatment,
  across four cells. Awards in particular are third-party evidence this workspace does not author.
- **Reference 3** makes the counter the headline: "we've crafted over 600+ unique designs". The
  oversized-statement device is kept but the claim is removed — the line now states what the studio
  works on rather than how much of it there is.
- **Reference 5** is written in superlatives: "trailblazing", "pioneers groundbreaking designs",
  "unrivalled creativity", "setting new standards". That is superlative self-assessment rather
  than description, so the statement in `005` is written plainly.
- No reference is followed into naming a studio. Every wordmark and mark reads "Studio", the
  placeholder used across the sector.

## Study Records

### ARC-S07-001 — Universal / Safe

- **Structural intent / archetype:** The standard about block: some pictures of the work, a short
  statement about the practice, and three things worth knowing. Broadly reusable.
- **Layout model:** A centred pill label above a `1.05fr / 1fr` grid — a four-tile mosaic in two
  columns with alternating 3:4 and 4:3 tiles on the left, and heading, two paragraphs and a
  three-cell fact row on the right. Fact cells set the value at display size above a small
  uppercase label, so the row keeps the reference's rhythm without carrying a number.
- **Density:** Medium.
- **Media mode:** Four empty image tiles at unequal proportions.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Grid stacks at 1024px; the two portrait tiles square up at 768px so the
  mosaic does not become a tall column; mosaic and fact row both go single-column at 480px with
  tiles at 16:10.
- **Composer value:** The safest binding target in the section — four images, a heading, two
  paragraphs and three label/value pairs, which is what most studio-about content models hold.
- **Limitation / content ceiling:** Four tiles exactly; the alternating proportions are what stop
  the mosaic reading as a plain grid, and a fifth tile breaks the pairing. Three fact cells. Two
  paragraphs before the text column outruns the mosaic at 1280px.

### ARC-S07-002 — Premium / Editorial

- **Structural intent / archetype:** The magazine opening spread. A display heading, images that
  overlap it, and one belief statement given the whole lower half.
- **Layout model:** A three-cell top rail (a caption plus two labels) over a `1.15fr / 0.5fr`
  lead grid in which the heading and the principal image occupy the *same* grid cell — the heading
  at `z-index: 2`, the image pushed down by a `clamp(56px, 8vw, 118px)` top margin so it rises
  behind the second line. A smaller portrait sits in the right column. Below, a bracketed label
  introduces a statement set at reading-display size with two captions on a closing rule.
- **Density:** Low-medium.
- **Media mode:** Two empty image areas, the larger deliberately overlapping the display heading.
- **Interaction:** None. No `<script>` element. The heading carries `pointer-events: none` so the
  overlap can never intercept a click meant for the image beneath it.
- **Responsive strategy:** The overlap is abandoned rather than scaled: at 768px heading, principal
  image and side image become three stacked rows, because an overlap that works at 1440px turns
  into an unreadable collision on a phone. Top rail collapses at 1024px and again at 480px.
- **Composer value:** The premium register. One display heading, one statement, two images and four
  short captions — a small field set with the highest visual impact in the section.
- **Limitation / content ceiling:** The display heading must be two short words; the overlap depends
  on it. The statement holds about thirty-five words. Lowest information capacity in the section,
  and the overlap makes it the study most sensitive to a change in image proportion.

### ARC-S07-003 — Dense / Information-heavy

- **Structural intent / archetype:** The full studio page compressed into one section — a picture,
  a position, four things about the practice, and two more pictures — on a deep ground that sets
  it apart from whatever sits above and below it.
- **Layout model:** A deep olive panel. A small label above a `1.12fr / 1fr` upper block (principal
  image beside a serif heading whose second line is italic, plus two paragraphs), then a rule and a
  `1.6fr / 1fr` lower block pairing a four-cell fact row with two square images.
- **Density:** High — the largest content set in the section.
- **Media mode:** One large empty image area plus two small ones.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Upper block stacks at 1024px where the fact row halves to two columns;
  images widen at 768px; fact row and image pair both become single-column at 480px. The deep
  ground means every text tone was checked against the panel rather than against white.
- **Composer value:** The highest-capacity option, and the only one in the section that runs on a
  dark ground — useful where the about section needs to read as a break in a light page.
- **Limitation / content ceiling:** Four fact cells and two paragraphs. The dark ground is a strong
  commitment and will fight a light brand; it also means any photography placed in the slots needs
  to be tonally compatible or the panel comes apart.

### ARC-S07-004 — Conversion-led

- **Structural intent / archetype:** The about section as an invitation. The statement is oversized
  enough to be the argument, and the two affordances — a quiet corner pill and a filled round
  action — are the only other things in the composition.
- **Layout model:** A `1fr / auto` head places the uppercase display statement against a bordered
  pill in the corner. Below, a three-track body at `0.55fr / 1.15fr / 1.1fr` holds the round
  "learn more" action, an image, and two paragraph columns.
- **Density:** Medium.
- **Media mode:** One empty image area between the action and the text columns.
- **Interaction:** None. No `<script>` element. Conversion is carried by hierarchy and placement:
  the filled round action sits in the reading path before the explanatory text, not after it.
- **Responsive strategy:** The body goes to two columns at 1024px with the action moved to the end
  by `order`, then to one column at 768px where it returns to the top of the flow — so the action
  is never stranded mid-sequence. The corner pill left-aligns at 768px; the round action goes full
  width at 480px.
- **Composer value:** The conversion register, and the only study here whose statement is the
  headline rather than a supporting paragraph. Two actions exactly, which keeps the choice simple.
- **Limitation / content ceiling:** The display statement holds about twelve words at 1440px before
  it pushes the body below the fold. Two paragraph columns; a third breaks the three-track balance.
  Only one image, so it is the weakest study here for a studio selling on photography.

### ARC-S07-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The colophon — the imprint page of a practice monograph, where
  the studio is described once, in full, and a rail points to the documents standing behind the
  description. It is how a practice introduces itself in print rather than in marketing.
- **Layout model:** A monospace edge label on a rule, an oversized wordmark masthead with a small
  pill set against it, a `0.4fr / 1.55fr` body aligning a tall plate to the baseline of a single
  long statement, and a three-cell colophon rail of monospace links divided by hairlines.
- **Density:** Low-medium.
- **Media mode:** One empty tall plate at the lower left.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The body stacks at 768px with the plate re-ordered *below* the statement
  and capped at 320px wide, so the section still opens on words rather than on a placeholder; the
  colophon rail becomes a single column with its dividers switched from vertical to horizontal.
- **Composer value:** The identity option, and a different sector-native register from the
  drawing-sheet language of `ARC-S01-005` / `ARC-S04-005`, the specification clauses of
  `ARC-S05-005`, and the programme table of `ARC-S06-005` — so the sector now has four distinct
  discipline-native devices rather than one repeated. Gives Composer one statement field and a
  repeatable rail of named studio documents.
- **Limitation / content ceiling:** One paragraph, about seventy words; the whole design rests on
  that paragraph being worth reading. Three rail entries before the dividers crowd. A colophon
  reads as considered to an audience that knows the convention and as sparse to one that does not,
  and the oversized wordmark assumes the studio name is short.

## Research Metadata

- **Sources:** Five visual-direction reference images supplied with the authoring request.
- **Research date:** 2026-08-30
- **Structural territory rationale:** Each reference was assigned to the territory its topology
  already served — the mosaic-and-facts block to Universal, the overlapping display spread to
  Premium, the deep-ground panel with the fullest content set to Dense, the display statement with
  two visible affordances to Conversion-led, and the wordmark-and-statement page to Sector-native,
  where the colophon convention supplies the discipline-native element.
- **Differentiation notes:** Five distinct geometries — a two-column mosaic, an overlapping
  same-cell heading and image, a deep panel in two blocks, a three-track body under a display
  statement, and a masthead with a single statement and a rail. Media counts differ (4 / 2 / 3 /
  1 / 1). Grounds differ: white, warm off-white, deep olive, near-white, and warm paper. Type
  differs: neutral sans, sans display with a bracketed label, serif with italics, uppercase sans
  display, and sans with a monospace rail. Only one study is dark; only one overlaps; only one uses
  a monospace system. No study uses JavaScript.
- **Sector-interpretation note:** Four of the five references sell the studio with numbers or
  superlatives. Neither survives into this batch; what replaces them is description. That is
  recorded here because it is the largest single difference between these studies and the
  references they follow.

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
| Mosaic tile ×4 | `ARC-S07-001` | Four views of the work beside the statement | Still image, alternating 3:4 and 4:3 (1:1 at 768px, 16:10 at 480px) | Labelled empty tiles; the text column is complete without them. |
| Principal + side | `ARC-S07-002` | One large image overlapping the display heading, one portrait beside it | Still image, 4:3 and 3:4 (both stacked at 768px) | The heading carries `pointer-events: none`, and the overlap is removed below 768px, so the heading is never obscured or unclickable. |
| Principal + pair | `ARC-S07-003` | One large image beside the heading, two square images beside the fact row | Still image, 4:3 and 1:1 (16:10 and 4:3 at 768px) | Labelled empty areas on a deep ground; replacement photography should be tonally compatible with the panel. |
| Body image | `ARC-S07-004` | One image between the action and the text columns | Still image, 4:3 (16:10 at 768px) | Labelled empty area; the statement and the two actions carry the section. |
| Colophon plate | `ARC-S07-005` | One tall plate beside the statement | Still image, 3:4 (4:3 at 768px, capped at 320px wide) | Re-ordered below the statement on small screens so the section opens on words. |

No study contains a photograph, a logo, a client mark, or any fabricated evidence. Licensing and
provenance metadata is not applicable to this batch because no third-party asset is referenced;
it becomes required if these slots are filled before ingestion.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S07-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps; every
  `aria-labelledby` reference resolving to a real id; every `<a>` carrying an `href`; visible
  `:focus-visible` styling in all five, with an amber ring on the dark ground and the filled
  action; and a `prefers-reduced-motion` block in all five. Contrast measured on 22 text and UI
  colour pairs, with the deep-ground study checked against its own panel rather than against
  white: all text ≥ 4.5:1 (lowest 5.54:1) and all interactive borders ≥ 3:1 (lowest 3.62:1).
  Nothing is signalled by colour alone. The `002` overlap was given `pointer-events: none` on the
  heading so the stacking order cannot swallow a click.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; 430 and 390 resolve through
  the 480 rules and 320 through the 360 rules. Grid children use `minmax(0, …)`, type and spacing
  use `clamp()`. Three layouts change behaviour rather than merely shrinking: `002` abandons its
  heading/image overlap at 768px instead of scaling it, `004` moves its action with `order` at
  1024px and returns it to the top of the flow at 768px so it is never stranded mid-sequence, and
  `005` re-orders its plate below the statement. No horizontal scroll anywhere. Interactive
  controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Copy-policy validation: PASS.** Visible text extracted and scanned for awards, certifications,
  accreditations, rankings, percentages, counters, "N+" patterns, client counts, review counts,
  years-of-experience claims, and — specific to this section — the superlative vocabulary carried
  by the references. Zero matches after one rephrase: a line in `003` about how a surface weathers
  used the words "years of use", which the scanner flagged as a possible experience claim; it was
  reworded so the scan is unambiguous.
- **Structural-diversity validation: PASS.** Five distinct geometries, five distinct media
  strategies, five distinct grounds, and five distinct type treatments. No study is a cosmetic
  variation of another.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- This section required more copy intervention than any previous one: four of the five references
  sell the studio with numbers or superlatives, and none of that survives. The substitutions are
  listed individually under Authoring Direction so a reviewer can see exactly what changed and why.
- `ARC-S07-005` adds a fourth sector-native register to the sector — the monograph colophon,
  alongside the drawing sheet, the specification clause, and the project programme — so the
  distinctive studies do not converge on one device.
- Section studies carry the section title as the document `<h1>`. Only `002` has an `<h2>`, for its
  belief statement; the other four have a single heading because the section is a single statement.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
