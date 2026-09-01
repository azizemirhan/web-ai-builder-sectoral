# BATCH V1

## Batch Identity

- Sector: `Automotive`
- Prefix: `AUTO`
- Section ID: `AUTO-S01`
- Section Name: `Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `AUTO-S01-001` | Universal / Safe | AUTHORED | `raw/AUTO-S01-001.html` |
| `AUTO-S01-002` | Premium / Editorial | AUTHORED | `raw/AUTO-S01-002.html` |
| `AUTO-S01-003` | Structured / Visual Modular | AUTHORED | `raw/AUTO-S01-003.html` |
| `AUTO-S01-004` | Conversion-led | AUTHORED | `raw/AUTO-S01-004.html` |
| `AUTO-S01-005` | Art-directed / Distinctive | AUTHORED | `raw/AUTO-S01-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md`. These are the current
direction names; the earlier "Dense / Information-heavy" and "Sector-native / Distinctive"
readings are not used anywhere in this batch. Study IDs never change with a direction name.

## Authoring Direction

Five visual-research images were supplied with the authoring request, with a locked
reference-to-study mapping. They were used as **structural and visual research**, not as pixel
targets: composition, hierarchy, media proportion, type scale, spatial relationships, action
placement, layering and crop strategy were taken; brand, wordmark, wording, vehicle photography,
model identity and every numeric claim were not.

| Study | Reference | What was taken | What was deliberately not taken |
| --- | --- | --- | --- |
| `AUTO-S01-001` | Reference 2 — vehicle on open landscape, one stacked heading, one restrained action | Clarity, vehicle dominance, very low copy count | Its overlay layout, its rental content model, its wording |
| `AUTO-S01-002` | Reference 4 — vehicle on a mountain road, bright cinematic frame, restrained action pair | Cinematic restraint, whitespace, two-action register | Its brand, its German-language voice, its arrangement |
| `AUTO-S01-003` | Reference 3 — one vehicle image plus grouped supporting callouts | The organising idea: one vehicle field plus a small set of grouped modules | Its metric density — six-plus numeric specifications became zero |
| `AUTO-S01-004` | Reference 1 — lifestyle frame, heavy headline, high-visibility action, secondary play action | The action hierarchy and its weight in the composition | Its rental content model, its wording, its brand |
| `AUTO-S01-005` | Reference 5 — dark composition, dramatic crop, floating detail card, oversized bottom type | The layering logic: statement, dominant media, floating card, oversized type layer that the media crops into | Its arrangement, its wordmark, its vehicle, its copy |

**No study reproduces a supplied screenshot, embeds one, or loads one remotely.** Every image
area is a reserved, intentionally empty media slot.

**Section-shell check.** All five references are full web pages carrying site headers,
navigation, logos and page chrome. None of that appears in any study: these are hero components
only, per the section-shell rule in `standards/01-AUTHORING-STANDARD.md`.

## Study Records

### AUTO-S01-001 — Universal / Safe

- **Structural intent / archetype:** The dependable, broadly reusable automotive hero. Reads as
  an automotive site immediately without any experimental device, and is the easiest of the five
  to bind to arbitrary content.
- **Layout model:** Bounded split hero inside a 1440px shell on a light ground. Two columns at
  `0.86fr / 1.14fr` — text left, a dominant rounded media panel right — vertically centred, with
  a shell `min-height` of `clamp(560px, 66vh, 700px)`. Left column runs eyebrow, two-line
  heading, one supporting sentence, one filled primary action beside one underlined secondary
  link, then a short note under a hairline rule. This is the only study of the five that uses a
  side-by-side text/media split.
- **Content density:** Low. Six content regions, 57 visible words.
- **Media relationship:** One reserved media area, rounded 18px, `min-height: clamp(330px, 38vw,
  520px)`, stretched to the full column height so it stays the dominant visual element. No text
  sits over it.
- **Interaction:** None. The file contains no `<script>` element.
- **Responsive behaviour:** Single column at 1024px, where the panel takes a `2 / 1` proportion
  so the stacked hero stays close to one screen; `3 / 2` at 768px and `4 / 3` at 480px, with the
  corner radius stepping 18 → 16 → 14px. The primary action goes full-width at 480px. Text
  precedes media in source order, so the heading still leads the stacked composition. Measured
  heights: 635 / 589 / 988 / 879 / 793 / 763 / 766px.
- **Composer value:** The safe default for the role. Small, obvious field set — eyebrow, heading,
  one paragraph, primary action, secondary link, one note, one image.
- **Content ceiling / limitation:** One image and no supporting information zone. A heading
  beyond about seven words loses the two-line rhythm the column is built on; at 320px it becomes
  three lines. The note is the only expansion point and holds roughly twenty-five words.
- **Reference interpretation:** Reference 2's clarity and vehicle dominance, restated as a split
  rather than as an overlay. No rental semantics survive.
- **Document metaphor used:** NO.

### AUTO-S01-002 — Premium / Editorial

- **Structural intent / archetype:** Cinematic campaign hero on a bright ground. Closer to a
  luxury automotive campaign frame than to a dealership page: typography and media carry it, and
  the copy count is deliberately minimal.
- **Layout model:** Full-bleed stage, `min-height: clamp(600px, 88vh, 880px)`, as a flex column.
  The media area is absolutely positioned across the whole stage; the copy field is held in the
  left band at `max-width: min(680px, 52%)` and vertically centred; a hairline caption rail sits
  on the bottom edge carrying one short line and a continue marker. Two understated actions:
  one solid, one outlined — both square, not pill, to keep the register restrained.
- **Content density:** Low. 35 visible words — the second-lowest of the batch.
- **Media relationship:** One reserved full-bleed media area with a built-in horizontal scrim.
  The scrim holds ≥ 0.90 across the whole copy band and falls to zero by 90%, which is what
  communicates the intended crop: copy left, vehicle right. The slot tone is set darker than the
  scrim so the reserved region reads as a reserved region while it is empty. The vertical slot
  label runs up the right margin.
- **Interaction:** None. No `<script>` element.
- **Responsive behaviour:** The copy field narrows to `min(560px, 64%)` at 1024px with the scrim
  ramp moved to match. At 768px the composition transforms rather than shrinks: the stage takes a
  `clamp(480px, 128vw, 640px)` height, the copy moves to the bottom band, the scrim turns
  vertical and opens the top of the frame for the photograph, and the slot label returns to
  horizontal at the top right. Below 480px the scrim reaches full strength earlier because the
  copy occupies a larger share of a short frame. Actions go full-width and the rail stacks at
  480px. Measured heights: 792 / 704 / 630 / 640 / 550 / 499 / 506px.
- **Composer value:** The premium register. Very small field set with high impact — eyebrow, a
  two-line heading, one paragraph, two actions, one rail line, one image.
- **Content ceiling / limitation:** Depends on a strong photograph with its subject right of
  centre; the scrim protects contrast but cannot rescue a badly composed image. The heading holds
  two short lines — a third breaks the vertical balance against the rail. No list, module or
  information zone at all, which is the point of the direction and also its ceiling.
- **Reference interpretation:** Reference 4's cinematic restraint and its two-action register.
  Its brand, its German-language voice and its arrangement were not used.
- **Document metaphor used:** NO.

### AUTO-S01-003 — Structured / Visual Modular

- **Structural intent / archetype:** The organised, information-capable hero — capacity carried
  by a module grid and a media rhythm, not by copy volume or by specification density.
- **Layout model:** Three bands on a light ground inside a 1440px shell. Band 1 is an intro at
  `1.3fr / 0.85fr` — eyebrow and heading left, one sentence and one link right, baseline-aligned.
  Band 2 is one wide primary vehicle media field, `min-height: clamp(210px, 21vw, 300px)`, read
  as a deliberately cinematic crop. Band 3 is a three-up module row; each module is its own
  detail media area above an index, a one-word title and one short line.
- **Content density:** Medium — the highest capacity of the batch at 78 visible words, but spread
  across three modules rather than concentrated in prose.
- **Media relationship:** Four reserved media areas — one wide primary field plus one per module.
  **Text never sits over media anywhere in this study**, which is one of its structural
  differences from the other four.
- **Interaction:** None. No `<script>` element.
- **Responsive behaviour:** A three-stage module ladder, not a stack-and-shrink. The intro goes
  single column at 1024px and the primary field takes `21 / 9`. At 900px the module row becomes a
  single column of horizontal rows separated by rules — media column `0.38fr`, `3 / 2` — so three
  modules stay compact instead of becoming three tall cards. At 560px the module media becomes a
  fixed 96px square and at 360px an 80px square, which is what keeps the phone height at
  890–931px instead of the ~1600px the naive vertical stack produced. Measured heights: 919 /
  840 / 1024 / 1203 / 913 / 890 / 931px.
- **Composer value:** The capacity option for the role. It exposes a repeatable three-item module
  collection, each with its own media slot, plus an intro block and one link — the structure most
  model-overview content actually needs.
- **Content ceiling / limitation:** Three modules is the design, and four is the maximum before
  the row loses its rhythm at 1280px. Module titles must stay one or two words and module lines
  one short sentence; the 96px media column at phone widths sets that limit. It is the tallest
  study of the five at every width, so it is the weakest choice where the hero must fit one
  screen.
- **Reference interpretation:** Reference 3's organised visual information, with its metric
  density removed rather than reduced — see the claims section below.
- **Document metaphor used:** NO. There is no specification table, comparison table, dashboard,
  schedule or data sheet. The `01` / `02` / `03` indices are ordinal labels on three modules, not
  document notation.

### AUTO-S01-004 — Conversion-led

- **Structural intent / archetype:** The hero where the next action materially shapes the
  composition. One coherent conversion intent — book a test drive — expressed as a structural
  band rather than as a button dropped into a layout.
- **Layout model:** Full-bleed dark stage, `min-height: clamp(600px, 88vh, 860px)`, as a flex
  column. The copy is held low-left at `max-width: min(820px, 66%)` with an uppercase two-line
  display heading. A solid full-width action band sits on the bottom edge above a hairline,
  carrying the primary pill action, a secondary play action with a circular disc, and one short
  supporting line pushed to the right. The band is the study's defining device.
- **Content density:** Low-medium. 50 visible words.
- **Media relationship:** One reserved full-bleed media area with a two-axis scrim. The slot tone
  is set lighter than the stage so the reserved region reads while it is empty; the slot label
  sits top right, clear of the copy.
- **Interaction:** None. No `<script>` element and **no form** — conversion is expressed as a
  visible action hierarchy, so the study captures no data and carries no data-handling
  implications.
- **Responsive behaviour:** At 1024px the supporting line drops to its own full-width row inside
  the band so the two actions keep their prominence. At 768px the stage releases to intrinsic
  height and the scrim drops its horizontal layer, so the vertical layer is strengthened to
  protect the copy on its own. At 480px the primary action goes full-width; because the band is
  in flow at the bottom of the hero rather than fixed, it never takes over the mobile screen —
  the hero is 511–573px tall on a phone. Measured heights: 792 / 704 / 676 / 504 / 511 / 537 /
  573px.
- **Composer value:** The conversion register. Clear primary/secondary hierarchy in a band that
  maps to one primary action, one secondary action and one supporting line, with the content
  region above it left free.
- **Content ceiling / limitation:** One conversion intent only; a second primary action would
  destroy the band's hierarchy. The supporting line holds about fifteen words before it wraps
  into the action row at 1280px. At 320px the second heading line wraps to two rows — the
  composition stays readable and nothing is clipped, but the intended two-line rhythm becomes
  three lines at that width.
- **Reference interpretation:** Reference 1's action hierarchy and its weight in the frame. Its
  rental content model and wording were not used.
- **Document metaphor used:** NO.

### AUTO-S01-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The most visually distinctive study of the batch, with the
  distinctiveness coming from art direction — crop, layering, scale and lighting register —
  rather than from any technical or document device.
- **Layout model:** Layered near-black stage. A two-column frame at `0.9fr / 1.5fr` holds the
  copy block top-left (eyebrow, a two-line statement whose second line carries the accent, one
  pill action) and a dominant vehicle media field right. A floating detail card is absolutely
  positioned over the media's top-right corner, carrying its own small media area, a title, one
  line and a labelled circular action. An oversized typographic layer spans the full width in the
  row below at `clamp(3.4rem, 19vw, 17rem)`, pulled up behind the media by a negative margin and
  cropped by the stage's bottom edge. Four explicit z-layers: word 0, media 1, copy 2, card 3.
- **Content density:** Low — 30 visible words, deliberately the lowest of the batch.
- **Media relationship:** Two reserved media areas — one dominant vehicle field and one small
  detail field inside the floating card. The vehicle field crops into the oversized word, which
  is the composition's central relationship; it is legible with both areas empty.
- **Interaction:** None. No `<script>` element.
- **Responsive behaviour:** A deliberate three-stage simplification. At 1024px the frame goes
  single column and the media takes `16 / 9`, but the card **stays overlaid** and the word's
  negative pull is increased so it clears the new row gap — measured overlap holds at 104px at
  1440 through 49px at 681px. At 680px, the width below which the media can no longer hold the
  card, the card leaves the overlay and becomes a compact horizontal module with a square media
  slot, and the word's overlap is released so it crops into nothing rather than into the card.
  At 480px the card's media column narrows to 84px and the action goes full-width. The oversized
  word is `white-space: nowrap` on a `19vw` ramp, so it scales rather than clipping: 274px at
  1440 and 61px at 320, with no horizontal overflow at any width. Measured heights: 630 / 581 /
  900 / 700 / 787 / 774 / 714px.
- **Composer value:** The identity option. Its distinctive regions — the accent statement line,
  the floating detail card and the oversized typographic layer — are all bindable, and the word
  is drawn from the statement rather than being a marque, so it stays content rather than
  branding.
- **Content ceiling / limitation:** The statement must be two short lines and the oversized word
  a single word of roughly four to eight characters; longer strings force the `19vw` ramp down
  far enough to lose the effect. Exactly one floating card — a second has nowhere to sit. The
  layering is a wide-width device, and below 680px the study reads as a strong dark stack rather
  than as a layered composition; that is the intended narrow-width form, not a fallback.
- **Reference interpretation:** Reference 5's layering logic and typographic scale. Its
  arrangement, its wordmark, its vehicle and its copy were not used.
- **Document metaphor used:** NO. No blueprint, engineering drawing, specification sheet,
  dashboard or technical notation appears; the distinctiveness is crop, scale, layering and
  lighting register.

## Structural Diversity

The five differ in layout topology, media topology, content placement, information capacity,
interaction of the action hierarchy with the composition, and responsive strategy — not in
styling.

| | 001 | 002 | 003 | 004 | 005 |
| --- | --- | --- | --- | --- | --- |
| Topology | Bounded split | Full-bleed stage | Three-band module system | Full-bleed stage + bottom band | Layered stage |
| Ground | Light neutral | Bright ivory | White | Dark charcoal | Near-black |
| Media areas | 1 | 1 | 4 | 1 | 2 |
| Media placement | Right panel | Full-bleed | Wide band + per-module | Full-bleed | Dominant right field + card field |
| Text over media | No | Yes | **No** | Yes | No |
| Copy position | Left column | Left band, centred | On page ground, above media | Low-left | Top-left |
| Visible words | 57 | 35 | 78 | 50 | 30 |
| Actions | 1 pill + 1 link | 2 square, equal weight | 1 text link | 1 pill + 1 disc, in a band | 1 pill + 1 card action |
| Distinctive device | — | Directional scrim as crop | Module grid | Action band | Oversized type layer the media crops into |
| Narrow-width move | Stack, text first | Copy to lower band, scrim turns vertical | Modules to compact rows, then fixed square media | Band stays in flow, action full-width | Card leaves overlay, overlap released |
| Desktop height (1440) | 635px | 792px | 919px | 792px | 630px |

No two share a topology, a media count, a ground or a narrow-width strategy. `001` is the only
side-by-side split; `003` is the only study where text never sits over media and the only one
with a module collection; `004` is the only one whose action hierarchy is a structural band;
`005` is the only layered composition; `002` is the only study where a scrim is used to
communicate the crop rather than only to protect contrast.

## Research Metadata

- **Sources:** Five visual-research images supplied with the authoring request, with a locked
  reference-to-study mapping. Described here as supplied visual research; the referenced sites
  and brands are not the authors of these studies and none of their trademarks appear in the
  output.
- **Research date:** 2026-09-01
- **Structural direction rationale:** The supplied mapping was followed exactly. Each reference
  was already serving the direction it was mapped to — landscape clarity to Universal, cinematic
  restraint to Premium/Editorial, grouped supporting modules to Structured/Visual Modular, action
  weight to Conversion-led, and layered dark art direction to Art-directed/Distinctive.
- **Differentiation notes:** See the diversity table above. The set was reviewed against the
  "five versions of text left, car right" failure mode: only `001` uses that topology.
- **Visual-first check:** Every study is carried by composition. `002` and `005` hold the
  lowest word counts and the strongest compositions. `003` has the highest capacity, and it
  passes the direction's own test — removing half its copy leaves the module grid, the media
  rhythm and the three-band structure intact, so its distinctiveness does not come from text.
  No study derives its difference from having more copy.
- **Document-metaphor justification:** NONE. No study uses a technical or professional document
  metaphor. Sheet, issue, revision, NTS, scale, dossier and register notation, technical matrices,
  drawing frames, blueprint language and engineering-document styling are absent from all five.
  Automotive character comes from vehicle media, crop, motion, detail relationships, lighting
  register, type and action hierarchy.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `<iframe>`, `@import`, `src=`, `url()`, webfont
  or `data:` image in any file. All type uses system font stacks; the only vector content is two
  small inline glyphs (the play triangle in `004`, the arrow in `005`), both `aria-hidden` and
  `focusable="false"`.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form `action`.
- Browser storage: NONE.
- Embedded reference screenshots: NONE.
- JavaScript necessity: NONE. All five studies are static and none contains a `<script>`
  element. The standard permits vanilla JavaScript where genuinely necessary; no behaviour in
  this batch required it.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Vehicle media | `AUTO-S01-001` | Primary vehicle or lifestyle image beside the statement | Still image, landscape; 2:1 at 1024px, 3:2 at 768px, 4:3 at 480px | Empty tonal panel with one quiet text label. Layout is complete with no image; no text overlays it. |
| Campaign media | `AUTO-S01-002` | Dominant cinematic frame, subject right of centre | Still image, landscape, ≥ 1800px wide | Horizontal scrim already in place across the copy band, so overlay text keeps contrast whatever the photograph is. Slot tone is darker than the scrim so the reserved area reads while empty. Label is page text, not alt text. |
| Vehicle media | `AUTO-S01-003` | Wide primary vehicle crop between the intro and the modules | Still image, wide landscape; 21:9 at 1024px, 16:9 at 768px | Empty tonal panel with one label. No text overlays it at any width. |
| Detail media ×2, Interior detail media ×1 | `AUTO-S01-003` | One supporting crop per module | Still image; 16:9, 3:2 at 900px, 1:1 at 560px | Empty tonal panels with quiet labels; each module stays readable with its media empty. |
| Lifestyle media | `AUTO-S01-004` | Dominant lifestyle frame behind the copy and above the action band | Still image, landscape, ≥ 1800px wide | Two-axis scrim already in place. Slot tone is lighter than the stage so the reserved area reads while empty. The action band is opaque and independent of the media. |
| Vehicle media | `AUTO-S01-005` | Dominant vehicle field that crops into the oversized type layer | Still image, landscape; 16:9 at 1024px, 4:3 at 480px | Empty tonal panel. The crop relationship with the type layer is structural and reads with the slot empty. |
| Interior detail media | `AUTO-S01-005` | Small detail crop inside the floating card | Still image; 16:10, 1:1 below 680px | Empty tonal panel with a quiet label. The slot is preserved at every width — the narrow-width simplification changes its proportion, it does not drop it. |

Nine reserved media areas across five studies. Every one is deliberately empty; that is intended
output, not a defect. No study contains a photograph, a logo, a marque, a badge or any fabricated
evidence. Licensing and provenance metadata is not applicable because no third-party asset is
referenced; it becomes required if these slots are filled before ingestion.

## Claims

Verified by extracting the visible text of all five studies and scanning it.

- Fabricated automotive specifications: **NONE.** No range, battery, charging, power,
  acceleration, top speed, emissions or efficiency figure appears in any study. Reference 3
  carries six-plus such metrics; `AUTO-S01-003` carries none — `Range`, `Charging` and `Interior`
  are module topics with one neutral line each, not values.
- Prices, monthly payments, finance, lease or trade-in terms: **NONE.**
- Discounts, offers, countdowns, scarcity or "limited time" framing: **NONE.**
- Awards, rankings, certifications, safety ratings, accreditations: **NONE.**
- Availability, stock counts, model years, delivery times: **NONE.**
- Real brands, marques, model names, logos or trademarks: **NONE.** The oversized word in `005`
  is a word from that study's own statement, not an invented marque.
- The only digits in the visible text of the whole batch are the `01` / `02` / `03` module
  indices in `AUTO-S01-003`.

## QA

- **ID validation: PASS.** All five planned IDs exist. Each file carries a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a `data-direction` attribute, a scoped
  root class, and a filename in the `AUTO-S01-NNN.html` form required by
  `standards/02-NAMING-AND-ID-STANDARD.md`. Every element `id` is namespaced with its study ID,
  so several studies can share one document without collision.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Section-shell check: PASS.** No `<header>`, `<nav>` or `<footer>` element and no `banner`,
  `navigation` or `contentinfo` role in any file. No logo, wordmark, primary navigation,
  announcement bar or site chrome, although all five references contain such elements.
- **Accessibility QA: PASS.** Verified by script and by review: exactly one `<h1>` per study with
  no heading-level jumps, a `<main>` landmark in all five, every `<a>` carrying a resolvable
  in-document `href`, every decorative SVG marked `aria-hidden` and `focusable="false"`, and
  visible `:focus-visible` styling with a measured focus ring in all five. A
  `prefers-reduced-motion` block is present in all five, disabling the hover transitions that are
  the only motion in the batch. No state is communicated by colour alone. All interactive targets
  measure ≥ 24px on both axes at every tested width, and the primary actions are ≥ 44px high.
  Contrast measured on 48 text and UI pairs: all body, label and heading text ≥ 4.5:1 (lowest
  5.35:1) and all non-text interactive borders ≥ 3:1 (lowest 3.91:1).
- **Overlay contrast independence: PASS.** `002` and `004` are the only studies with text over
  media. Both were measured against the worst-case photograph rather than against the placeholder
  tone — a fully dark image under `002`'s light scrim and a fully white image under `004`'s dark
  scrim — at every scrim stop across the copy band, at desktop and at each narrow-width ramp. All
  pairs pass. Three initial failures were found and fixed before sign-off: `002`'s desktop
  horizontal scrim (2.54:1 on the eyebrow and lead), `002`'s rail, which sat past the end of the
  gradient and now carries its own backdrop, and `004`'s ≤ 768px scrim (3.5:1 on the heading),
  which lost the horizontal layer with the column change.
- **Responsive QA: PASS at 1440, 1280, 1024, 768, 430, 390 and 320px,** measured in a real
  browser rather than by static review. At every study and every width: `scrollWidth` equals the
  viewport width, so there is no horizontal overflow anywhere in the set; no element renders
  outside the viewport bounds; no interactive target falls below 24px. All grid children use
  `minmax(0, …)` and all heading sizes use `clamp()`. Breakpoint ladders differ per study and are
  documented in each record above. One documented behaviour: at 320px only, `004`'s second
  heading line wraps to two rows — nothing is clipped and no overflow results, but the intended
  two-line rhythm becomes three lines at that width.
- **Height check: PASS.** Desktop heights at 1440px are 635 / 792 / 919 / 792 / 630px — following
  the structural direction rather than a single forced height, and all within a realistic
  first-screen range. `002` and `004` use bounded `vh` treatments that release to intrinsic
  height below 768px; no study relies on a fixed pixel height.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `data:image`, `fetch(`, `XMLHttpRequest`,
  `integrity`, `crossorigin`, `localStorage` and `<script`. Zero matches across all five files.
- **Copy-policy validation: PASS.** See the claims section above.
- **Structural-diversity validation: PASS.** See the diversity table above.
- **Visible-copy check: PASS.** No authoring, research, policy or compliance explanation appears
  in any visible composition. All of it is in the head comment blocks, the `<meta>` research
  fields and this document. Media slot labels are short, quiet and part of the reserved-area
  convention rather than explanatory notes.
- **Not run here:** assistive-technology testing, real-device testing, reduced-motion behaviour
  under a real user preference, and Design Lab capture. Those belong to Design Lab QA.

## Notes

- First authored section in the Automotive sector. It follows the raw-study conventions set by
  Architecture: a metadata comment block plus `<meta>` research fields in `<head>`, a namespaced
  root element carrying `data-study-id` and `data-direction`, element ids prefixed with the study
  ID, and a commented two-line host baseline as the only unscoped CSS. `data-direction` and
  `<meta name="direction">` are added alongside the existing `territory` field so the current
  direction names are recorded without breaking the contact-sheet generator, which reads
  `territory`.
- All five studies are zero-JavaScript.
- `review/index.html` was **not** regenerated with this batch. The contact-sheet generator sweeps
  every sector, and the Architecture Phase 3 rework has that pipeline suspended and is using the
  committed sheet as its fixed visual review source. Regenerating here would move that reference
  under an in-flight review. The sheet should be regenerated once Phase 3 closes, which will pick
  up this batch.
- No review, normalisation, survivor-selection or promotion decision is recorded in this
  document. Direction labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`,
  not production enums.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` are
  catalog-wide bookkeeping and were left untouched; they need a separate workspace-level pass.
