# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S01`
- Section Name: `Hero (Portfolio-led)`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S01-001` | Universal / Safe | AUTHORED | `raw/ARC-S01-001.html` |
| `ARC-S01-002` | Premium / Editorial | AUTHORED | `raw/ARC-S01-002.html` |
| `ARC-S01-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S01-003.html` |
| `ARC-S01-004` | Conversion-led | AUTHORED | `raw/ARC-S01-004.html` |
| `ARC-S01-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S01-005.html` |

## Authoring Direction

Five visual-direction reference images were supplied with the request. The direction given
during authoring was to follow the supplied layouts rather than to abstract from them, and to
leave every image area empty. Each study therefore reproduces the topology of one reference —
navigation placement, text block position, type scale, action treatment, and supporting
information zones — retargeted from property marketing to architecture and interior design
practice, with all media held as empty placeholder surfaces.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S01-001` | Reference 3 | Centred nav with a contact pill, left text column, large rounded media panel right |
| `ARC-S01-002` | Reference 1 | Full-bleed stage, wordmark left / uppercase nav right, oversized two-line heading, two pill actions, baseline rail of one paragraph plus three large-type cells |
| `ARC-S01-003` | Reference 4 | Dense uppercase nav, oversized two-line display type, badge and caption block left, stacked metadata column right, media block overlapping the type, bottom caption |
| `ARC-S01-004` | Reference 5 | Full-bleed stage, stacked two-line wordmark, nav with a contact link, light card overlapping the bottom-right corner with a circular action |
| `ARC-S01-005` | Reference 2 | Full-bleed stage, stacked mark with glyph top left, compact nav top right, corner-anchored uppercase heading block with a supporting line |

Two references carry numeric counters (Reference 1's bottom row and Reference 4's right
column). The layout position and type rhythm of those cells are preserved, but the numbers are
replaced with non-numeric labels — engagement stages in `002`, practice metadata in `003` —
because this workspace does not author statistics, awards, certifications, or
completed-project claims.

## Study Records

### ARC-S01-001 — Universal / Safe

- **Structural intent / archetype:** Split portfolio hero. The broadly reusable default: one
  statement, one image panel, two actions, and a navigation bar that suits most studios.
- **Layout model:** Three-part top bar (mark left, navigation centred, contact pill right) over
  a two-column hero at `0.82fr / 1.18fr` inside a 1440px shell. Left column runs star glyph,
  eyebrow, two-line display heading, intro, then a filled pill action beside a circled
  secondary link. Right column is a large rounded media panel.
- **Density:** Low-medium. Six content regions.
- **Media mode:** One empty media area, rounded 26px, 7:5. No image is supplied and no
  decorative artwork is drawn inside it; it carries a single quiet "Image area" label.
- **Interaction:** None. The file contains no `<script>` element.
- **Responsive strategy:** Navigation moves below the mark and left-aligns at 1024px, where the
  hero also collapses to one column and the panel re-proportions 7:5 → 16:9. Panel goes 4:3 at
  768px and the corner radius steps 26 → 20 → 16px. Primary action becomes full-width at 480px.
  Shell padding is a `clamp(20px, 3.6vw, 52px)` ramp, so 430/390/320 need no extra rules.
- **Composer value:** The safe default for the section role. Field set is small and obvious —
  eyebrow, heading, intro, primary action, secondary action, one image — which makes it the
  easiest study in the set to bind to arbitrary studio content.
- **Limitation / content ceiling:** One image and no supporting information zone. Four
  navigation items is the comfortable maximum before the centred nav wraps at 1280px. A heading
  longer than about six words loses the two-line rhythm the layout is built on.

### ARC-S01-002 — Premium / Editorial

- **Structural intent / archetype:** Cover-page hero. Oversized type over a full-bleed image,
  with a baseline rail that keeps supporting content in the first viewport.
- **Layout model:** Full-bleed stage as a flex column: masthead, centred lead block
  (two-line heading, intro, filled and outlined pill actions), and a four-cell baseline rail
  at `1.25fr / 0.58fr / 0.58fr / 0.58fr` — one paragraph plus three large-type cells.
- **Density:** Low-medium.
- **Media mode:** One empty full-bleed media area with a two-axis scrim already in place, so
  overlay text keeps its contrast when a photograph replaces the placeholder. Slot label is
  set vertically along the right margin.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** `height: 100vh` bounded by `min-height: 720px` / `max-height: 1040px`;
  below 768px the stage releases to intrinsic height, the vertical slot label returns to normal
  flow above the masthead, and the scrim switches from horizontal to vertical. The rail goes
  4 → 3 columns with the paragraph spanning full width at 1024px, and to a single column at
  360px. Actions go full-width at 480px.
- **Composer value:** The premium register. Small field set with high impact — two text regions,
  two actions, one image, and three label/value cells that read as a summary strip without
  being metrics.
- **Limitation / content ceiling:** Depends on a strong photograph; the scrim protects contrast
  but cannot rescue a busy image. Exactly three rail cells — a fourth breaks the rhythm at
  1280px. No list, index, or form capacity.

### ARC-S01-003 — Dense / Information-heavy

- **Structural intent / archetype:** Editorial index hero. Display type, flanking information
  columns, an overlapping media block, and a compact project index all inside the first
  viewport.
- **Layout model:** Dense uppercase navigation (mark / six centred links / enquiry pill) above a
  two-line uppercase display heading with the second line indented 8%. Beneath it a three-column
  body at `0.92fr / 2.2fr / 0.92fr` — badge and uppercase caption left, media centre, four-row
  metadata list right — pulled up by a negative margin so the media overlaps the type. A bottom
  rail carries a caption and a four-item project index.
- **Density:** High. The largest content set in the batch: 6 nav items, badge, caption,
  4 metadata rows, 4 index entries, plus heading and media.
- **Media mode:** One empty media area, 16:9, overlapping the display type on desktop.
- **Interaction:** None. No `<script>` element. The current page is marked with
  `aria-current="page"` rather than by colour alone.
- **Responsive strategy:** The overlap is removed at 1024px, where the body becomes two columns
  and the media re-orders above the flanking columns; the bottom rail stacks. Navigation drops
  to its own full-width row at 768px and the index goes 4 → 2 columns. At 480px the body is
  single-column, the second display line loses its indent, the media becomes 4:3, and the index
  becomes a single column.
- **Composer value:** The highest-capacity option for this section role. It exposes a repeatable
  project-record collection (ref, name, typology) plus a four-row practice metadata list — the
  two places most architecture content models actually hold data.
- **Limitation / content ceiling:** Four index entries and four metadata rows are the ceiling;
  more pushes the rail out of the first viewport. The display heading must be two short words
  per line or the 11.4vw scale overruns at 1280px. The smallest media presence of the five,
  so it is the weakest choice for a photography-led studio.

### ARC-S01-004 — Conversion-led

- **Structural intent / archetype:** Corner-card conversion hero. The image holds the page and a
  light card at the bottom-right corner carries the heading, a short paragraph, a circular
  primary action, and a secondary action cluster.
- **Layout model:** Full-bleed stage with an absolutely positioned masthead over the media
  (own gradient so navigation stays legible) and an absolutely positioned card at
  `right: 0; bottom: 0`, `width: min(620px, 50%)`, rounded on its top-left corner only. Inside
  the card, a `1fr / auto` grid places the 132px circular action beside the heading and
  paragraph, with a three-link cluster below a rule.
- **Density:** Medium.
- **Media mode:** One empty full-bleed media area.
- **Interaction:** None. No `<script>` element and no form — conversion is expressed as a
  visible action hierarchy (circular primary, three secondary links) rather than as an intake
  module, so the study stays capture-stable and carries no data-handling implications.
- **Responsive strategy:** At 1024px the stage becomes a flex column: the media area converts
  from absolute to a 16:10 block, the card becomes static and full-width with square corners,
  and the circular action moves below the text. The masthead stays absolutely positioned over
  the media at every width so its light text always sits on the media ground. Media goes 4:3 at
  768px; the circular action shrinks to 118px and the cluster stacks at 480px.
- **Composer value:** The conversion register for the section. Clear primary/secondary hierarchy
  with three named studio actions — start a project, book a consultation, discuss your space —
  and a card region that maps cleanly to a heading, a paragraph, one primary action, and a link
  list.
- **Limitation / content ceiling:** Three cluster links and roughly forty words of card copy;
  beyond that the card grows tall enough to cover the media on a 1024px-tall viewport. There is
  no field capture, so a real enquiry flow needs a downstream form section. The heading must
  stay under about eight words to hold three lines inside the card at 1280px.

### ARC-S01-005 — Sector-native / Distinctive

- **Structural intent / archetype:** Corner-anchored hero on a light ground, extended with
  drawing-sheet convention — a title block along the bottom edge and a plate reference on the
  media.
- **Layout model:** Full-bleed stage as a flex column: masthead (triangular glyph plus stacked
  monospace mark left, compact nav right), a corner-anchored heading block with an uppercase
  heading, a supporting line and two outlined actions, and a five-cell title block rail
  (Sheet, Set, Scale, Revision, Status) rendered as a definition list on the bottom edge.
- **Density:** Medium.
- **Media mode:** One empty full-bleed media area on a light ground, with a downward-fading
  white scrim so dark overlay text keeps contrast once a photograph is placed, and a plate
  reference tag near the bottom right.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Title block steps 5 → 3 → 2 → 1 columns, re-assigning right-hand
  borders at each step so no cell keeps a stray rule. The stage releases to intrinsic height at
  768px, where the plate tag returns to normal flow and the scrim is strengthened. Actions
  become full-width at 480px; the mark and nav type step down at 360px.
- **Composer value:** The identity option. It is the only study whose supporting zone is
  discipline-native rather than generic — the title block gives Composer a fixed five-field
  metadata region (sheet, set, scale, revision, status) that maps directly onto how practices
  already label work, and the light ground distinguishes it from the two dark full-bleed studies.
- **Limitation / content ceiling:** Five title-block cells exactly; the rail is the layout and
  does not tolerate a sixth without dropping to three columns early. The uppercase heading holds
  about eight words before it pushes the title block off a 700px-tall viewport. Drawing-sheet
  convention reads as deliberate to an architecture audience and may read as technical to a
  general consumer audience.

## Research Metadata

- **Sources:** Five visual-direction reference images supplied with the authoring request.
- **Research date:** 2026-08-29
- **Structural territory rationale:** Each reference was assigned to the territory its topology
  already served — the split text/panel layout to Universal, the full-bleed display-type cover
  to Premium/Editorial, the flanked display-type layout with metadata columns to Dense, the
  corner-card layout to Conversion-led, and the corner-anchored heading layout to
  Sector-native, where the drawing-sheet title block supplies the discipline-native element.
- **Differentiation notes:** No two studies share a topology. Media placement differs across all
  five — right panel, full-bleed dark, overlapping centre block, full-bleed dark with corner
  card, full-bleed light. Navigation differs — centred with pill, right uppercase, dense centred
  with utility pill, overlaid with contact emphasis, compact right. Grounds differ: two light,
  two dark, one light-warm. Type differs: neutral sans, oversized sans display, uppercase
  display, sans with a circular action, and uppercase with a monospace label system. Density
  spans low-medium to high.
- **Sector-interpretation note:** Several references are property-marketing pages. They were
  used as composition references only. No study contains listings, property specifications,
  prices, agents, or availability. All content is framed as studio practice — projects,
  typologies, scope, stages, plates, and design engagement.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont. All
  type uses system font stacks; the only vector content is two small inline glyphs (`001` star,
  `005` studio mark), both `aria-hidden`.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form `action`.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Right panel | `ARC-S01-001` | Primary project image beside the statement | Still image, 7:5 (16:9 at 1024px, 4:3 at 768px) | Empty tonal surface with a quiet "Image area" text label. Layout is complete with no image. |
| Full-bleed stage | `ARC-S01-002` | Dominant background project image | Still image, landscape, ≥1600px wide | Two-axis scrim already present, so overlay text keeps contrast when an image is placed. Slot label is page text, not alt text. |
| Overlapping block | `ARC-S01-003` | Featured project image overlapping the display type | Still image, 16:9 (4:3 at 480px) | Empty tonal surface with a text label; the overlap is removed below 1024px so nothing is obscured. |
| Full-bleed stage | `ARC-S01-004` | Background project image behind the corner card | Still image, landscape, ≥1600px wide | Masthead carries its own gradient so navigation stays legible over any replacement image. Card is opaque and independent of the media. |
| Full-bleed stage | `ARC-S01-005` | Background project image on a light ground | Still image, landscape, ≥1600px wide | Downward-fading white scrim protects the dark heading; plate tag and title block are page text. |

Every image area is deliberately left empty, per the authoring direction. No study contains a
photograph, a logo, a client mark, a badge, or any fabricated evidence. Licensing and provenance
metadata is not applicable to this batch because no third-party asset is referenced; it becomes
required if these slots are filled before ingestion.

## QA

- **ID validation: PASS.** All five planned IDs exist. Each file carries a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in
  the `ARC-S01-NNN.html` form required by `standards/02-NAMING-AND-ID-STANDARD.md`. Every
  element `id` inside a study is namespaced with its study ID, so several studies can share one
  document without collision.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Verified by script and by review: exactly one `<h1>` per study and
  no heading-level jumps, `<main>` landmark and skip link in all five, `aria-label="Primary"` on
  every navigation, every `aria-labelledby` reference resolving to a real id, every `<a>`
  carrying an `href`, every decorative SVG marked `aria-hidden` and `focusable="false"`, and
  visible `:focus-visible` styling in all five (light-on-dark studies use an amber focus ring,
  light-ground studies use blue, and `004` switches ring colour inside the light card).
  `prefers-reduced-motion` block in all five. Contrast measured on 24 text and UI colour pairs
  against the least favourable gradient stop in each study: all body and label text ≥ 4.5:1
  (lowest 5.87:1), all interactive borders ≥ 3:1 (lowest 3.21:1). Two borders initially measured
  2.94:1 and 2.05:1 and were darkened to 3.27:1 and 3.28:1 before sign-off. No state is
  communicated by colour alone — the current navigation item in `003` uses `aria-current` plus
  an underline.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; 430 and 390 resolve through
  the 480 rules and 320 through the 360 rules. All grid children use `minmax(0, …)` so no track
  can be forced wider than its container, and all heading sizes use `clamp()` so no fixed size
  can overflow 320px. Padding and gaps are `clamp()` ramps tied to viewport width. Interactive
  controls are ≥ 44px high. There is no horizontal scroll anywhere in the set. Both viewport-height
  stages (`002`, `004`) and the light stage (`005`) release to intrinsic height below 768px so
  tall content can never clip; `004`'s masthead stays positioned over the media at every width so
  its light text never lands on a light background.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Copy-policy validation: PASS.** Visible text extracted and scanned for awards,
  certifications, accreditations, rankings, counters, percentages, guarantees, ratings, client
  counts, and testimonial language. The only numeric strings in visible text are the study ID in
  each `<title>` and the placeholder index references `01`–`04` in `ARC-S01-003`. No study states
  a statistic of any kind.
- **Structural-diversity validation: PASS.** Five distinct topologies, five distinct media
  placements, five distinct navigation treatments, and three distinct ground treatments. No study
  is a cosmetic variation of another.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing,
  and reduced-motion behaviour under a real user preference. Those belong to Design Lab capture
  and QA.

## Notes

- This is the first authored section in the workspace, so it also sets the raw-study conventions:
  a metadata comment block plus `<meta>` research fields in `<head>`, a single namespaced root
  element carrying `data-study-id` and `data-territory`, all element ids prefixed with the study
  ID, and a clearly commented two-line host baseline as the only unscoped CSS.
- All five studies are zero-JavaScript. The authoring standard permits vanilla JavaScript when
  genuinely necessary; following the supplied reference layouts produced no behaviour that
  required it.
- Every image area is an empty placeholder surface carrying a short text label. No study implies
  real completed work, a real client, or a real studio; `005` states `Status: Design study` in
  its title block.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this
  document. Territory labels are the authoring targets from
  `standards/01-AUTHORING-STANDARD.md`, not production enums.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector. They were left untouched as catalog-wide bookkeeping outside
  this section's scope and need a separate workspace-level pass.
