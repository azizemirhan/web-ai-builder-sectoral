# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S05`
- Section Name: `Design Philosophy`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S05-001` | Universal / Safe | AUTHORED | `raw/ARC-S05-001.html` |
| `ARC-S05-002` | Premium / Editorial | AUTHORED | `raw/ARC-S05-002.html` |
| `ARC-S05-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S05-003.html` |
| `ARC-S05-004` | Conversion-led | AUTHORED | `raw/ARC-S05-004.html` |
| `ARC-S05-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S05-005.html` |

## Authoring Direction

Five visual-direction reference images were supplied. As in `ARC-S01`, `ARC-S03`, and `ARC-S04`,
the direction was to follow the supplied layouts rather than abstract from them, and to leave
every image area empty. Each study reproduces the topology of one reference — heading treatment,
text-block placement, label position, media proportion, whitespace rhythm — retargeted to a
design philosophy section.

None of the five references is a philosophy section in its original form: four are about or
story sections and one is a "how we work" list, drawn from agency, travel, property, and
insurance marketing. Their topologies were carried across; none of their subject matter was.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S05-001` | Reference 2 | Small label over a heading with a paragraph opposite, an image pair at unequal proportions, then a margin-labelled second tier with a longer heading, two paragraph columns and a pill button |
| `ARC-S05-002` | Reference 1 | Oversized ultra-light lowercase display word with tiny labels beneath, a large accented uppercase manifesto with inline capsules, two small rounded image cards at the lower left, two short text columns at the lower right, and a corner mark |
| `ARC-S05-003` | Reference 4 | Rounded light panel with a heading, a supporting line and a badged image on the left, and a six-entry list of icon, title and description on the right |
| `ARC-S05-004` | Reference 5 | Uppercase eyebrow, three-line heading, paragraph and dark button on the left, beside one tall image, one landscape image, and a filled accent block carrying a quotation |
| `ARC-S05-005` | Reference 3 | Wide image band across the top of a dark section, then a margin label beside a long body of text whose opening sentences are set brighter than the continuation |

Three substitutions were needed to keep the batch inside the copy and media policy:

- Reference 4 advertises a free consultation on its floating badge. That is a commercial offer,
  so the badge is replaced with a neutral studio note.
- Reference 5 places a customer testimonial in its accent block. Testimonials are third-party
  evidence this workspace does not author, so the block carries an unattributed studio principle,
  labelled "Studio principle".
- Reference 1 tints selected phrases in its manifesto. The tint is kept for rhythm, but the
  sentence reads identically in a single colour, so no meaning depends on it.

## Study Records

### ARC-S05-001 — Universal / Safe

- **Structural intent / archetype:** A philosophy section in two plain tiers — a short position
  first, then a longer explanation with a way to read further. The broadly reusable default.
- **Layout model:** Tier one is a `1.05fr / 1fr` split of label-plus-heading against a supporting
  paragraph. An image pair follows at `1.2fr / 1fr` with unequal ratios (4:3 and 3:4). Tier two is
  a `0.34fr / 1.5fr` grid — a margin label beside a longer heading, two paragraph columns, and a
  pill action.
- **Density:** Medium. Two headings, four text blocks, two images, one action.
- **Media mode:** Two empty image areas at deliberately unequal proportions.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Both tiers collapse to one column at 1024px, where the margin label sits
  above its content rather than beside it. The portrait image squares up to 4:3 at 768px; the
  image pair and the paragraph columns each become single-column at 480px and the pill goes full
  width. Radius and label padding step down at 360px.
- **Composer value:** The safest binding target in the section. Two heading levels, four
  paragraphs, two images, and one link — a field set almost any content model can fill, and the
  only study here with a second tier for longer-form copy.
- **Limitation / content ceiling:** Two paragraph columns; a third breaks the tier-two measure at
  1280px. The image pair is designed as one wide plus one tall, so two landscape images lose the
  rhythm. No place for a list, a quotation, or a numbered structure.

### ARC-S05-002 — Premium / Editorial

- **Structural intent / archetype:** A manifesto page. One oversized word sets the register and a
  single accented paragraph carries the whole argument.
- **Layout model:** An ultra-light lowercase display word at `clamp(3rem, 15.5vw, 12rem)` spanning
  the measure, two tiny labels indented beneath it, then a right-aligned uppercase manifesto with
  accented phrases and two inline media capsules. A foot row at `1.15fr / 1fr` pairs two small
  rounded image cards with two short titled notes. A corner mark sits in the top right.
- **Density:** Low-medium. Deliberately the least content in the section.
- **Media mode:** Two empty rounded image cards, plus two optional inline media capsules set into
  the manifesto line. The capsules are decorative and the sentence reads correctly without them.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The manifesto switches from right- to left-aligned and the foot row
  becomes one column at 1024px. The two tiny labels stack and the capsules shrink at 480px; the
  image cards become a single column at 360px. The display word is fully fluid, so it never
  overflows at 320px.
- **Composer value:** The premium register, and the only study whose primary content is a single
  paragraph. Useful where a studio wants one strong statement rather than an explained position.
- **Limitation / content ceiling:** One display word — two words break the 15.5vw scale at 1280px.
  The manifesto holds roughly sixty words before the uppercase setting becomes tiring to read. No
  list, no action, and no route onward, so it needs a neighbouring section to carry the next step.

### ARC-S05-003 — Dense / Information-heavy

- **Structural intent / archetype:** The philosophy written out as six working positions, each
  short enough to be read at a glance and specific enough to be argued with.
- **Layout model:** A rounded light panel holding a `1fr / 1.18fr` grid. The left column runs
  heading, supporting line, and a 4:5 image area with a badge overlapping its top-right corner.
  The right column is a six-entry list, each entry a `44px / 1fr` grid of a circular icon beside a
  title and description, separated by hairlines.
- **Density:** High. The largest content set in the section — six entries with descriptions, plus
  heading, lede, image and badge.
- **Media mode:** One empty image area with an overlapping badge. Entry icons are decorative
  inline vectors, not media slots.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The grid becomes one column at 1024px where the image widens to 16:9 and
  the badge narrows; the image returns to 4:3 at 768px. At 480px the icon column narrows to 36px
  and the badge leaves its overlapping position to sit under the image as a normal block, so it
  can never cover the media on a small screen.
- **Composer value:** The highest-capacity option for this section role, and the one that maps
  most directly onto a repeatable principle collection of icon, title, and description.
- **Limitation / content ceiling:** Six entries is the designed count; more makes the list taller
  than the image column at 1440px and the panel loses its balance. Descriptions run to about
  twenty-five words. The icon set is generic geometry and would need replacing for a studio with
  its own iconography.

### ARC-S05-004 — Conversion-led

- **Structural intent / archetype:** A position stated in order to start a conversation. The
  philosophy is framed as a working method, and the section closes on an action rather than on
  more text.
- **Layout model:** A `0.86fr / 1.35fr` grid. The left column runs eyebrow, three-line heading,
  paragraph, a dark filled button and a secondary text link. The right column is a three-cell
  composition — a tall media area spanning both rows, a landscape media area, and a filled accent
  block carrying a quotation with a serif quote glyph and an attribution line.
- **Density:** Medium.
- **Media mode:** Two empty media areas, one tall and one landscape, plus one filled quotation
  block that is not a media slot.
- **Interaction:** None. No `<script>` element. Conversion is carried by hierarchy — one filled
  button, one text link — rather than by a form.
- **Responsive strategy:** The grid becomes one column at 1024px with top alignment; the tall cell
  flips to portrait at 768px; at 480px the composition becomes a single column, the tall cell
  drops its row span, and the button goes full width.
- **Composer value:** The conversion register for the section, and the only study with a
  quotation region. That region is deliberately typed as a studio principle rather than a
  testimonial, so it can be filled without sourcing third-party evidence.
- **Limitation / content ceiling:** The quotation holds about twenty-five words before the accent
  block outgrows its cell at 1280px. Three cells exactly — a fourth breaks the two-row
  composition. The accent colour is a strong brand assumption and would need retinting for most
  studio identities.

### ARC-S05-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The philosophy set as a written specification. A practice
  issues a specification when it wants a position to be binding, and this study borrows that
  convention: numbered clauses, hanging references, and a status line.
- **Layout model:** A dark sheet. A wide media band (21:9) spans the top, then a `0.42fr / 1.6fr`
  grid — a margin column holding a monospace title and a four-row reference list (Clause, Applies
  to, Revision, Status), beside a body of a bright lede followed by four numbered clauses. Each
  clause is a `clamp(46px, 5vw, 68px) / 1fr` grid of a hanging monospace reference beside a
  clause heading and text. A monospace foot rule closes the sheet.
- **Density:** Medium.
- **Media mode:** One empty wide media band.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The band steps 21:9 → 16:9 at 1024px → 3:2 at 768px → 4:3 at 360px. The
  grid becomes one column at 1024px, where the reference list becomes a two-column block, then a
  single column at 480px. Clause references move above their text at 480px rather than shrinking
  the hanging indent to an unusable width.
- **Composer value:** The identity option, and the only study in the section that carries document
  metadata — clause range, applicability, revision, status — which suits practices that publish a
  formal position. It is a deliberately different sector-native register from the drawing-sheet
  language used in `ARC-S01-005`, `ARC-S03-005`, and `ARC-S04-005`, so the sector has two
  discipline-native voices rather than one repeated.
- **Limitation / content ceiling:** Four clauses; a fifth pushes the reference column out of
  alignment with the body at 1440px. Clause text runs to about forty words. Specification
  convention reads as authoritative to an architecture audience and may read as cold or legalistic
  to a domestic client, and the dark ground commits the section to being a visual break in the page.

## Research Metadata

- **Sources:** Five visual-direction reference images supplied with the authoring request.
- **Research date:** 2026-08-30
- **Section assignment:** The references span more than one section role — four are about or story
  sections and one is a process list. The target section was confirmed as `ARC-S05 — Design
  Philosophy` before authoring.
- **Structural territory rationale:** Each reference was assigned to the territory its topology
  already served — the two-tier about block to Universal, the oversized display manifesto to
  Premium, the six-entry panel list to Dense, the statement-plus-quotation composition to
  Conversion-led (the only reference with a primary action), and the dark band-and-long-text
  section to Sector-native, where written specification convention supplies the discipline-native
  element.
- **Differentiation notes:** No two studies share a topology. Text structure differs across all
  five — paired tiers, a single manifesto paragraph, a six-entry list, a statement with a
  quotation, and numbered clauses. Media differs — an unequal image pair, two small rounded cards
  plus inline capsules, one badged portrait, a tall-plus-landscape composition, and one wide band.
  Grounds differ: warm off-white, light warm grey, white with a blue-grey panel, white, and dark.
  Type differs: neutral sans, ultra-light display with an accent tone, sans with icons, sans with
  a serif quote glyph, and sans with a monospace reference system. Density spans low-medium to
  high, and no study uses JavaScript.
- **Sector-interpretation note:** The references come from agency, travel, property, and insurance
  marketing. They were used as composition references only. No study contains products, plans,
  prices, availability, or testimonials; all content is framed as the studio's own design
  positions.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont. The only
  vector content is the six decorative icons in `003`, all `aria-hidden` and `focusable="false"`.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Image pair | `ARC-S05-001` | Two supporting images at unequal proportions | Still image, 4:3 and 3:4 (both 4:3 at 768px) | Empty tonal surfaces with quiet labels; both tiers read complete without them. |
| Card pair | `ARC-S05-002` | Two small supporting images in the foot row | Still image, 4:3 (16:10 at 360px) | Labelled empty cards, separate from the manifesto. |
| Inline capsules | `ARC-S05-002` | Two optional inline media capsules inside the manifesto line | Small still image or texture, pill-shaped | Decorative and `aria-hidden`; the sentence reads correctly whether or not they are filled. Not required. |
| Badged portrait | `ARC-S05-003` | One image beside the principle list | Still image, 4:5 (16:9 at 1024px, 4:3 at 768px) | Badge is opaque and leaves its overlapping position at 480px so it never covers the media. |
| Tall + landscape | `ARC-S05-004` | Two images beside the statement | Still image, 4:5 tall and 4:3 landscape | Labelled empty areas; the quotation block beside them is filled content, not a media slot. |
| Wide band | `ARC-S05-005` | One wide image across the top of the sheet | Still image, 21:9 (16:9 at 1024px, 3:2 at 768px) | Labelled empty band with a monospace caption; the clause body is independent of it. |

Every image area is deliberately left empty, per the authoring direction. No study contains a
photograph, a logo, a client mark, or any fabricated evidence. Licensing and provenance metadata
is not applicable to this batch because no third-party asset is referenced; it becomes required
if these slots are filled before ingestion.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S05-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study with sub-headings at `<h2>` and no
  heading-level jumps; every `aria-labelledby` reference resolving to a real id; every `<a>`
  carrying an `href`; every decorative SVG marked `aria-hidden` and `focusable="false"` (the six
  icons in `003` were flagged by the structural check and corrected before sign-off); visible
  `:focus-visible` styling in all five, with an amber ring substituted inside the dark study and
  the accent block; and a `prefers-reduced-motion` block in all five. Contrast measured on 23 text
  and UI colour pairs: all text ≥ 4.5:1 (lowest 4.52:1, the quotation attribution line) and all
  interactive borders ≥ 3:1 (lowest 3.57:1). No state is signalled by colour alone — the accented
  phrases in `002` carry no meaning beyond rhythm, and the brighter lede in `005` is a reading
  order cue, not a status.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; 430 and 390 resolve through
  the 480 rules and 320 through the 360 rules. Grid children use `minmax(0, …)`, type and spacing
  use `clamp()`, and every multi-column arrangement reduces its column count rather than shrinking
  content below a usable measure. Two overlapping elements are explicitly de-overlapped on small
  screens: the `003` badge becomes a normal block at 480px, and the `005` clause references move
  above their text rather than keeping an unusable hanging indent. No horizontal scroll anywhere.
  Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Copy-policy validation: PASS.** Visible text extracted and scanned for awards, certifications,
  accreditations, rankings, percentages, guarantees, ratings, testimonial language, free-offer
  language, currency symbols, price patterns, and client counts. The only numeric strings in
  visible text are the study ID in each `<title>` and the clause references `01.1`–`01.4` in
  `ARC-S05-005`.
- **Structural-diversity validation: PASS.** Five distinct topologies, five distinct media
  strategies, five distinct grounds, and five distinct type treatments. No study is a cosmetic
  variation of another.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- Section studies carry the section title as the document `<h1>` and sub-headings as `<h2>`,
  following the convention set in `ARC-S03`.
- `ARC-S05-004` is the first study in the sector to include a quotation region. It is typed as an
  unattributed studio principle rather than a testimonial, and the batch record says so, to keep
  the distinction visible to whoever fills it later.
- `ARC-S05-005` deliberately uses a different sector-native register — written specification
  convention — from the drawing-sheet language of `ARC-S01-005`, `ARC-S03-005`, and `ARC-S04-005`,
  so the sector does not repeat a single device across every distinctive study.
- Every image area is an empty placeholder surface carrying a short text label. The `002` inline
  capsules and the `003` icons are documented as decorative so they are not mistaken for unfilled
  media slots during ingestion.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
