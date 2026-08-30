# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S03`
- Section Name: `Services`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S03-001` | Universal / Safe | AUTHORED | `raw/ARC-S03-001.html` |
| `ARC-S03-002` | Premium / Editorial | AUTHORED | `raw/ARC-S03-002.html` |
| `ARC-S03-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S03-003.html` |
| `ARC-S03-004` | Conversion-led | AUTHORED | `raw/ARC-S03-004.html` |
| `ARC-S03-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S03-005.html` |
| `ARC-S03-006` | Extended — Paired media-and-card rows | AUTHORED | `raw/ARC-S03-006.html` |
| `ARC-S03-007` | Extended — Corner-media bento with icon cards | AUTHORED | `raw/ARC-S03-007.html` |

## Authoring Direction

Five visual-direction reference images were supplied. As in `ARC-S01`, the direction was to
follow the supplied layouts rather than abstract from them, and to leave every image area
empty. Each study reproduces the topology of one reference — heading placement, card
proportion, label treatment, control placement, whitespace rhythm — retargeted to an
architecture and interior design services section.

Two of the references are not services sections in their original form (a project catalogue
and a studio journal). Their card-collection topology was carried across and the content model
was rewritten to services; nothing from their original subject matter was retained.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S03-001` | Reference 4 | Uppercase eyebrow, heading and paragraph in a narrow left column; two-by-two card grid with title, description, and a "Learn more" arrow link |
| `ARC-S03-002` | Reference 5 | Left editorial column with eyebrow, mixed roman/italic heading and a "view all" link; four-card row with title and caption; warm philosophy band with a statement and a right-hand principle list |
| `ARC-S03-003` | Reference 3 | Bracketed section number in a ruled left margin; heading with a "See all" arrow opposite; three-card row with category label, title, and description |
| `ARC-S03-004` | Reference 1 | Catalogue heading with a small note opposite; card row with a light chip label over each image; primary button bottom-left and circular previous / next controls bottom-right |
| `ARC-S03-005` | Reference 2 | Centred heading above a row of four tall rounded cards, each with a pill badge over the top-left corner |
| `ARC-S03-006` | Reference 6 | White sheet inset on a warm ground; narrow left column with an uppercase eyebrow, a serif heading, a paragraph and a small dark button; stacked rows each pairing a full-height photograph with a card carrying a filled icon tile, a serif title, and a description with an underlined "Learn more" link |
| `ARC-S03-007` | Reference 7 | Off-white sheet on a warm ground; eyebrow, two-line serif heading, paragraph and a compact dark "View all" button in a block above the grid; a three-by-two field whose top-left and bottom-right cells are photographs and whose other four are icon cards |

Reference 1 carries a price line inside each chip. The chip position and two-line structure are
preserved, but the price is replaced with a neutral engagement descriptor ("Concept to
completion"), because this workspace does not author pricing, statistics, awards,
certifications, or completed-project claims.

`ARC-S03-006` was authored later, from a sixth reference supplied after the first five studies
were committed. `standards/01-AUTHORING-STANDARD.md` allows variants 006–010 only where research
demonstrates a genuinely missing structural territory, so it is recorded here against that test:
in all of `001`–`005` the services occupy a grid of equal cells and any photography belongs to a
card. `006` is the first S03 topology built from repeated two-cell rows pairing a full-height
media tile with a text card, and the first with a persistent narrow heading column carrying the
action. That is a different content model rather than a restyling of an existing one, so the
extension is taken as justified. The default target for the section remains five studies; `006`
is an addition to the batch, not a replacement for any of them.

`ARC-S03-007` came from a seventh reference supplied immediately after `006`. The two references
belong to the same template family and share a palette, so the extension test was applied to
their structure rather than their styling. `006` holds the heading in a persistent narrow side
column and repeats two-cell rows that pair one media tile with one card. `007` puts the heading
in a full-width block above the grid and treats media tiles as peers of the cards inside a single
three-by-two field, placed at opposite corners so the field reads diagonally; it also carries
four services rather than three. Different heading relationship, different media role, different
card count — they are alternates rather than restylings, so `007` is recorded as justified on the
same test.

The section now holds seven studies against a default target of five. Whether all seven survive,
or whether `006` and `007` are consolidated to one, is a Design Lab review decision and is not
taken in this workspace.

## Study Records

### ARC-S03-001 — Universal / Safe

- **Structural intent / archetype:** The archetypal services block. A short intro column states
  what the studio does; a four-card grid states the services. Broadly reusable by any
  architecture or interior practice.
- **Layout model:** Two-column grid at `0.62fr / 1.6fr` inside a 1280px shell. Left column
  (eyebrow, heading, paragraph, "Discuss a project" link) is sticky against the card grid on
  desktop. Right column is a two-by-two card grid; each card is an empty 4:3 media area, a
  title, a description, and a "Learn more" arrow link.
- **Density:** Medium. Four services with a description each.
- **Media mode:** Four empty image areas, one per card, each carrying a quiet "Image area" label.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The intro un-sticks and the grid becomes one column at 1024px; card
  gaps tighten at 768px; cards become a single column with 16:10 media at 480px; corner radius
  and label padding step down at 360px. Shell padding is a `clamp(20px, 3.6vw, 48px)` ramp, so
  430/390/320 need no extra rules.
- **Composer value:** The default binding target for this section role. The field set is the one
  every services content model already has — section eyebrow, heading, intro, link, and a
  repeatable card of image, title, description, link.
- **Limitation / content ceiling:** Four cards is the designed count; six would work but the
  two-by-two rhythm and the sticky intro alignment are tuned for four. Descriptions longer than
  about thirty words break the card grid's row alignment at 1280px.

### ARC-S03-002 — Premium / Editorial

- **Structural intent / archetype:** Editorial services spread. A serif statement column sets
  the tone, a tall card row names the disciplines, and a warm band underneath carries the
  studio's principles.
- **Layout model:** Two zones. Upper zone is a `0.66fr / 2.4fr` grid — editorial column (eyebrow,
  serif heading with an italic accent, "View all services" link) beside a four-card row of 4:5
  media areas with an uppercase title and a caption line. Lower zone is a full-width warm band
  at `0.72fr / 1.5fr / 0.78fr` — a portrait media area, a serif statement with a paragraph, and a
  four-item principle list with em-dash markers.
- **Density:** Medium.
- **Media mode:** Four empty 4:5 card areas plus one empty portrait area in the band.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Upper grid stacks and the card row goes 4 → 2 at 1024px, where the band
  drops to two columns with the principle list spanning full width. Card media becomes 1:1 and
  the band becomes one column at 768px. Single-column cards with 16:10 media at 480px; the
  principle list's marker column narrows at 480px and label padding steps down at 360px.
- **Composer value:** The premium register. It is the only study in the set with a second content
  zone, so it can carry a services list and a positioning statement in one section without a
  separate philosophy block.
- **Limitation / content ceiling:** Four disciplines and four principles exactly — the band's
  three-column balance depends on the list staying short. Card captions must be one short line;
  a second line breaks the row baseline. The serif treatment is a deliberate style commitment
  and will not suit every studio.

### ARC-S03-003 — Dense / Information-heavy

- **Structural intent / archetype:** Indexed services sheet. A ruled margin holds the section
  number, and each service card carries not just a description but the scope behind it.
- **Layout model:** Two-column frame — a `clamp(64px, 8vw, 116px)` ruled margin column holding
  `[03]`, and a body column with a head row (heading plus "See all services" link), a three-card
  row, and a four-cell capability rail on a top rule. Each card is an empty 3:2 media area, a
  monospace category label, a title link, a description, and a three-row scope list
  (Stages / Output / Typologies).
- **Density:** High. The largest content set in the batch — three cards × six content items,
  plus four rail cells.
- **Media mode:** Three empty 3:2 image areas.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Cards go 3 → 2 at 1024px with the third card spanning both columns and
  widening to 21:9, and the rail goes 4 → 2. At 768px the ruled margin moves above the body as a
  full-width rule and its number left-aligns. Single-column cards and a single-column rail at
  480px; scope rows and slot labels tighten at 360px.
- **Composer value:** The highest-capacity option for this section role. The per-card scope list
  gives Composer a repeatable label/value collection inside each service, which is where
  architecture service content usually has the detail that other layouts drop.
- **Limitation / content ceiling:** Three cards and three scope rows per card. A fourth card
  breaks the margin-column proportion; a fourth scope row pushes the rail below the fold on a
  900px-tall viewport. The monospace labels and ruled margin read as deliberate but reduce the
  warmth of the section.

### ARC-S03-004 — Conversion-led

- **Structural intent / archetype:** Service catalogue with a conversion foot. Six services are
  browsable in a rail, and the section closes with a primary action rather than another link.
- **Layout model:** A rounded white panel on a tinted ground. Head row is a catalogue heading with
  a supporting note opposite. Below it a horizontally scrollable rail of six cards, each a 3:4
  empty media area with a white chip at its foot carrying the service name and an engagement
  line. Foot row pairs a filled "Start a project" button and an "All services" link on the left
  with circular previous / next controls on the right.
- **Density:** Medium-high. Six services in the first view.
- **Media mode:** Six empty 3:4 image areas, each with an overlaid chip and a slot label.
- **Interaction:** Vanilla JavaScript, about forty lines, in one IIFE scoped by
  `document.querySelector('.arc-s03-004')`. The controls scroll the rail by exactly one card
  width plus gap, disable at each end, and hand focus to the opposite control when the pressed
  one becomes disabled. The rail is itself `tabindex="0"` with an accessible name, so keyboard
  users can scroll it directly and the controls are an enhancement, not the only path. Scroll
  behaviour drops to `auto` under `prefers-reduced-motion`. The chip focus ring is promoted from
  the link to the whole chip only behind `@supports selector(:has(*))`, so browsers without
  `:has()` keep the link's own ring instead of losing it.
- **Responsive strategy:** Cards per view step 4 → 3 → 2 → 0.78 of the rail → 0.86 at
  1280/1024/480/360; card proportion goes 3:4 → 4:5 at 768px. The foot stacks and the primary
  button goes full width at 480px, with the controls right-aligned beneath it; control diameter
  drops to 44px at 360px, still meeting the touch-target floor.
- **Composer value:** The conversion register, and the only study that scales past four services
  without a layout change — the rail absorbs any number. Clear action hierarchy: one filled
  primary, one text link, two navigation controls.
- **Limitation / content ceiling:** The chip holds a title and one short line; anything longer
  overflows the card foot. Six cards is the tested count, and with four or fewer at 1440px the
  rail cannot scroll, so both controls sit disabled — the layout still reads, but the controls
  become decorative. Requires JavaScript for the controls, though not for access to the content.

### ARC-S03-005 — Sector-native / Distinctive

- **Structural intent / archetype:** Services expressed as the studio's work stages. The
  discipline-native move is that the section is a sequence, not a menu: each card is a stage
  with its own drawings and handover, and a drawing-sheet title block closes it.
- **Layout model:** Centred head (monospace eyebrow, heading, supporting paragraph) above a
  four-column plate row. Each plate is a tall 3:4.4 empty media area with a white monospace
  stage badge pinned top-left and a slot label bottom-right, followed by a title link and a
  one-line description. A four-cell title block rail (Sheet, Set, Engagement, Status) closes the
  section between rules.
- **Density:** Medium.
- **Media mode:** Four empty tall image areas, each with an overlaid stage badge.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Plates go 4 → 2 at 1024px (proportion 3:4.4 → 4:5) → 1 at 480px
  (16:10). The title block steps 4 → 2 → 1 columns, re-assigning right and bottom borders at each
  step so no cell keeps a stray rule. Badge padding and tracking tighten at 360px.
- **Composer value:** The identity option, and the one whose content model differs most from the
  others: an ordered stage collection with a badge, a title, and a description, plus a fixed
  four-field sheet block. It suits practices that sell a staged appointment rather than a list of
  offerings, and it is consistent with the drawing-sheet language already used in `ARC-S01-005`.
- **Limitation / content ceiling:** Exactly four stages; the sequence reads as complete and a
  fifth plate breaks both the row and the title block's symmetry. Descriptions must stay to one
  line. Framing services as stages will not suit studios that sell discrete, independent
  services, and the numbered sequence implies a full-service appointment.

### ARC-S03-006 — Extended / Paired media-and-card rows

- **Structural intent / archetype:** Services as a stack of paired rows. Each service gets a
  photograph of its own at full row height and a card beside it, with the section heading and its
  single action held permanently in a narrow left column.
- **Layout model:** A white sheet inset on a warm ground, itself a `0.6fr / 1.62fr` grid. The left
  column holds an uppercase eyebrow, a three-line serif heading, a short paragraph and a compact
  dark button. The right column is a list of three rows, each a `1.04fr / 1fr` pair of a media
  tile and a card. Cards run a filled icon tile, a serif title, then a description and an
  underlined "Learn more" link pinned to the card foot by `margin: auto` on the title.
- **Density:** Medium. Three services, each with an icon, a title, a description and a link.
- **Media mode:** Three empty media tiles, one per row, each filling its own grid cell at full row
  height. The four card icons are decorative inline vectors and are not media slots.
- **Interaction:** None. No `<script>` element. Each card's "Learn more" link carries a stretched
  `::after` so the whole card is clickable, and an `aria-label` naming the service so the link is
  not announced as a bare "Learn more".
- **Responsive strategy:** The heading column moves above the rows at 1024px. Each row breaks into
  a stacked media tile and card at 768px, where the tile swaps its fixed row height for a 16:10
  ratio (4:3 at 480px). Sheet padding steps 54 → 18 → 14px and the ground inset steps 56 → 10px,
  so the framing survives 320px.
- **Composer value:** The only S03 layout that gives each service a full-size image of its own,
  which suits studios whose services are best shown rather than described. The persistent heading
  column also means the section keeps one visible action no matter how far the row list is
  scrolled past.
- **Limitation / content ceiling:** Three rows is the designed count — a fourth makes the row stack
  much taller than the heading column and the balance of the sheet is lost. Descriptions run to
  about twenty words before the card foot crowds. The inset-sheet framing is a strong
  presentational commitment and assumes the section is not placed directly against another
  full-bleed block.

### ARC-S03-007 — Extended / Corner-media bento with icon cards

- **Structural intent / archetype:** Services as a single field. One heading block sits above a
  three-by-two grid in which photographs and cards are peers, and the two media tiles are pushed
  to opposite corners so the eye crosses the field diagonally rather than scanning it in rows.
- **Layout model:** An off-white sheet on a warm ground. The head block runs an uppercase eyebrow,
  a two-line serif heading, a short paragraph and a compact dark "View all" button at full width.
  Below it a `repeat(3, 1fr)` field of six cells in source order — media tile, card, card, card,
  card, media tile — so the corner placement falls out of natural flow with no area map to
  maintain. Cards run a filled icon tile, a serif title, then a description and an underlined
  "Learn more" link pinned to the card foot by `margin: auto` on the title.
- **Density:** Medium-high. Four services with icon, title, description and link, plus two media
  cells.
- **Media mode:** Two empty media tiles occupying whole grid cells at opposite corners. The four
  card icons are decorative inline vectors and are not media slots.
- **Interaction:** None. No `<script>` element. Each card's "Learn more" link carries a stretched
  `::after` so the whole card is clickable, and an `aria-label` naming the service so the link is
  not announced as a bare "Learn more".
- **Responsive strategy:** The field steps 3 → 2 columns at 1024px and to a single column at
  480px, where media tiles swap their fixed row height for a 16:10 ratio (4:3 at 360px). Because
  the corner placement comes from source order rather than an area map, no breakpoint has to
  re-declare it. Sheet padding steps 52 → 18 → 14px and the ground inset steps 34 → 8px.
- **Composer value:** The most compact way in the section to show four services and two images
  together, and the only S03 layout where media and cards share one uniform cell shape — which
  makes it the easiest to fill from a content model that does not distinguish the two.
- **Limitation / content ceiling:** The six-cell field is the design; adding a fifth service
  breaks the corner symmetry the layout depends on. Descriptions run to about twenty-five words
  before the card foot crowds. At the two-column breakpoint the diagonal reading is lost and the
  media tiles land at the start and end of the flow instead, which is coherent but no longer the
  same composition.

## Research Metadata

- **Sources:** Five visual-direction reference images supplied with the authoring request.
- **Research date:** 2026-08-29
- **Section assignment:** The references span more than one section role (a project catalogue, a
  travel-style card row, a studio journal, a services grid, and a selected-work row). The target
  section was confirmed as `ARC-S03 — Services` before authoring; `ARC-S02` was left untouched
  because a separate authoring pass already occupies it.
- **Structural territory rationale:** Each reference was assigned to the territory its topology
  already served — the intro-column services grid to Universal, the editorial column with a
  philosophy band to Premium, the ruled-margin three-card sheet to Dense, the catalogue rail with
  controls to Conversion-led, and the centred badge-card row to Sector-native, where the work-stage
  sequence and title block supply the discipline-native element.
- **Differentiation notes:** No two studies share a topology. Card counts differ (4 / 4 / 3 / 6 / 4),
  card proportions differ (4:3, 4:5, 3:2, 3:4, 3:4.4), heading alignment differs (left-column,
  editorial-column, ruled-margin, catalogue-head, centred), and only one study scrolls. Grounds
  differ: white, warm off-white with a tinted band, cool grey, tinted with a white panel, warm
  paper. Type differs: neutral sans, serif with italic accents, sans with monospace labels, sans,
  and sans with a monospace badge and title block. Density spans medium to high.
- **Sector-interpretation note:** Two references come from property and travel marketing. They were
  used as composition references only. No study contains listings, properties, destinations,
  prices, or availability; all content is framed as studio services, scope, stages, and outputs.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, and no
  inline SVG in this batch. All type uses system font stacks.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: One of seven. `ARC-S03-004` needs it for the rail controls, their
  disabled states, and focus recovery. `001`, `002`, `003`, `005`, `006`, and `007` contain no
  `<script>` element at all.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Card image ×4 | `ARC-S03-001` | One image per service card | Still image, 4:3 (16:10 at 480px) | Empty tonal surface with a quiet "Image area" label. Card is complete without it. |
| Card image ×4 | `ARC-S03-002` | One image per discipline in the row | Still image, 4:5 (1:1 at 768px, 16:10 at 480px) | Empty tonal surface with a label; title and caption sit outside the media. |
| Band portrait | `ARC-S03-002` | Studio or material image beside the statement | Still image, 4:5 (16:10 at 768px) | `<figure>` with an in-slot label; the band reads as a statement block without it. |
| Card image ×3 | `ARC-S03-003` | One image per service card | Still image, 3:2 (21:9 for the third card at 1024px) | Empty tonal surface with a monospace label; the scope list carries the information load. |
| Card image ×6 | `ARC-S03-004` | Background of each catalogue card, behind the chip | Still image, 3:4 (4:5 at 768px) | Chip is opaque white and independent of the media, so the service name is legible over any replacement image. |
| Plate image ×4 | `ARC-S03-005` | Background of each stage plate, behind the badge | Still image, 3:4.4 (4:5 at 1024px, 16:10 at 480px) | Badge is an opaque white pill; stage identity is carried by text, not by the artwork. |
| Row tile ×3 | `ARC-S03-006` | One full-height photograph per service row | Still image, filling its cell (16:10 at 768px, 4:3 at 480px) | Empty tonal surface with a quiet label; the paired card holds all information and is independent of the tile. |
| Corner tile ×2 | `ARC-S03-007` | Two photographs holding opposite corners of the field | Still image, filling its cell (16:10 at 480px, 4:3 at 360px) | Empty tonal surfaces with quiet labels; the four cards carry all information, so the field reads complete with neither tile filled. |

Every image area is deliberately left empty, per the authoring direction. No study contains a
photograph, a logo, a client mark, a badge of accreditation, or any fabricated evidence.
Licensing and provenance metadata is not applicable to this batch because no third-party asset
is referenced; it becomes required if these slots are filled before ingestion.

## QA

- **ID validation: PASS.** All five planned IDs exist, plus the extension variants `ARC-S03-006`
  and `ARC-S03-007`.
  Each file carries a matching `<meta name="study-id">`, a `data-study-id` attribute, a scoped
  root class, and a filename in the `ARC-S03-NNN.html` form required by
  `standards/02-NAMING-AND-ID-STANDARD.md`. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Seven standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all seven. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Verified by script and by review: exactly one `<h1>` per study with
  card titles at `<h2>` and no heading-level jumps, every `aria-labelledby` and `aria-controls`
  reference resolving to a real id, every `<a>` carrying an `href`, both icon-only buttons in
  `004` carrying an `aria-label` and a `type`, visible `:focus-visible` styling in all seven, and a
  `prefers-reduced-motion` block in all seven. Contrast measured on 44 text and UI colour pairs:
  all text ≥ 4.5:1 (lowest 5.42:1) and all interactive borders ≥ 3:1 (lowest 3.06:1). The only
  sub-3:1 pair is the disabled state of the `004` controls, which is exempt and is not the sole
  signal — the controls also stop scrolling and the rail position itself communicates the end.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study, `006` and `007` included, defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; 430 and 390 resolve through
  the 480 rules and 320 through the 360 rules. Grid children use `minmax(0, …)`, headings and
  spacing use `clamp()`, and every card grid reduces its column count rather than shrinking cards
  below a usable width. The only horizontal scroll in the batch is the `004` rail, which is
  intentional, labelled, and keyboard reachable. Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`, and
  `crossorigin`. Zero matches across all seven files.
- **Copy-policy validation: PASS.** Visible text extracted and scanned for awards, certifications,
  accreditations, named professional bodies, rankings, percentages, guarantees, ratings,
  testimonial language, currency symbols, and price patterns. The only numeric strings in visible
  text are the study ID in each `<title>`, the `[03]` margin index in `ARC-S03-003`, and the stage
  numbers in `ARC-S03-005`. No study states a price or a statistic.
- **Structural-diversity validation: PASS.** Seven distinct topologies, seven distinct card
  arrangements, and seven distinct heading treatments. `006` and `007` share a palette because
  their references come from one template family; they were therefore tested against each other
  on structure, and differ in heading relationship, media role, and card count. No study is a
  cosmetic variation of another.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- Section studies carry the section title as the document `<h1>` and card titles as `<h2>`. Each
  raw study is captured as a standalone document, so a document-level `h1` is correct here even
  though a services block would sit at `h2` inside an assembled page. This is the convention set
  by this batch for all non-hero sections.
- `ARC-S03-004` is the only study in this section whose controls depend on JavaScript. Content
  remains fully reachable without it: the rail is a native scroll container with its own tab stop.
- Every image area is an empty placeholder surface carrying a short text label. No study implies
  real completed work, a real client, or a real studio; `005` states `Status: Design study` in its
  title block.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- `ARC-S02` was not touched. It contains an in-progress set from a separate authoring pass with a
  different batch format; reconciling the two conventions is a sector-level decision, not a
  `S03` one.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
