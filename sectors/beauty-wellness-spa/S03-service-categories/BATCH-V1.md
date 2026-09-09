# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S03`
- Section Name: `Service Categories`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S03-001` | Universal / Safe | AUTHORED | `raw/WELL-S03-001.html` |
| `WELL-S03-002` | Premium / Editorial | AUTHORED | `raw/WELL-S03-002.html` |
| `WELL-S03-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S03-003.html` |
| `WELL-S03-004` | Conversion-led | AUTHORED | `raw/WELL-S03-004.html` |
| `WELL-S03-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S03-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's own role, its category set and its boundary with
`S02` are in `./README.md`.

## Authoring Direction

**One** visual-research image was supplied, with the user noting that examples of this section role
were hard to find and asking for the rest to be originated as modern designs. Following the
placement rule established in the `WELL-S02` batch, the single reference was placed at the variant
whose register it occupies, and the other four directions were authored from nothing.

| Reference | Placed at | Why |
| --- | --- | --- |
| A row of tall rounded cards, each a full-bleed light photograph with a category name and one short line over its top-left corner, running past the right edge of the frame | `001` Universal / Safe | A media-card row is the most broadly shippable answer to a categories section, and its overlay treatment is mild rather than experimental |
| — | `002`, `003`, `004`, `005` | Originated |

**What was taken from the reference:** the tall media card, the top-aligned overlay of name and
line, the rounded corner treatment, and the bright airy register.

**What was deliberately not taken:** its row runs off the right edge of the frame, which reads as
a scrolling rail. That was resolved as a **static four-up grid** instead, for two reasons: a
categories set is short enough that all four should be visible at once, and `WELL-S02-005` already
occupies the edge-bleeding scroll-rail topology in this sector. Reproducing it here would have made
two adjacent sections look like the same component.

**No study reproduces the supplied screenshot, embeds it, or loads it remotely.** Every image area
is a reserved, intentionally empty media slot.

**Section-shell check.** No global header, navigation, footer or announcement bar appears in any
study, verified by scan.

**Claims check.** The claims rule in `../WELLNESS-DESIGN-DIRECTION.md` applies, and the procedural
description rule established for `S02` applies here at category scale: a category line says what
the category **covers**, never what it achieves. No study contains an efficacy claim, percentage,
price, duration, rating, practitioner name, qualification, client or address.

**Boundary check.** The subject of every study is a category, never a treatment. Only `003`
previews treatment names inside its panels, and there they are plain routing text with no
description, no media and no action of their own — which is the category answering "what is in
here?", and is category-level navigation. See the boundary note in `./README.md`.

## Cross-section separation

`S02` and `S03` sit next to each other on a real page and their names do not distinguish
themselves, so each `S03` study was checked against its `S02` counterpart:

| Variant | `WELL-S02` | `WELL-S03` | Separation |
| --- | --- | --- | --- |
| 001 | Media-topped cards in a 3 × 2 grid, caption below the image | Full-bleed cards in a 4-up row, caption over the image | Card anatomy and column count |
| 002 | Alternating full-width rows, large media, serif names at row scale | Typographic index, oversized serif names, media reduced to a small plate | Inverted hierarchy — there media leads, here type leads |
| 003 | Mosaic of unequal panels, no internal lists | Even 2 × 2 split panels, each with an internal category preview | Regular vs irregular field; sub-lists only here |
| 004 | Master-detail picker with a selection state | Question-led chooser with no selection state and a fallback band | One swaps a panel, one routes away |
| 005 | Horizontal scroll-snap rail, bleeding past the shell, captions inside the cards | Static staggered columns, no scroll, type crossing the outside of each panel | Motion vs stillness; type inside vs across |

`002` also deliberately avoids the 01/02/03 sequence markers used by `WELL-S02-002`, so the two
editorial studies do not share a device.

## Study Records

### WELL-S03-001 — Universal / Safe

- **Structural intent / archetype:** The dependable categories row. Four cards, all visible, media
  doing the sorting.
- **Layout model:** A compact left-aligned header above a static four-column grid of 3:4 cards.
  Each card is a full-bleed reserved media field with a light gradient scrim across its top half,
  the category name and one line of coverage set over that scrim, and a round arrow pinned to the
  lower-right corner.
- **Media relationship:** Four reserved areas, each filling a whole card — the highest media-to-
  content ratio in the batch, which is correct for the role: in a categories section the images do
  the sorting and the words only confirm it.
- **Empty-state note:** The scrim runs light-to-transparent downward and the overlay text is dark,
  so the caption is legible over a pale photograph **and** over the empty tonal slot. The contrast
  was measured against the empty state, not assumed from a hypothetical image.
- **Responsive strategy:** 4 → 2 → 1 columns, with the card stepping 3:4 → 4:3 → 3:2 → 4:3 so a
  single-column card on a phone does not become a tall column of empty tone.
- **Visual-first check:** 79 visible words.

### WELL-S03-002 — Premium / Editorial

- **Structural intent / archetype:** The hierarchy inverted. In most categories sections the image
  is the largest element; here the category name is, and the media is reduced to a small plate
  beside it.
- **Layout model:** A dark warm-brown ground. A deliberately small section heading and supporting
  line sit baseline-aligned at the top — smaller than everything below them — over four full-width
  rows separated by hairline rules. Each row is a four-column grid: an oversized serif name at up
  to 4.6rem, a small square media plate, one line of coverage, and an arrow at the far right.
- **Media relationship:** Four small reserved plates, deliberately subordinate. This is the one
  study in the batch where media is not the primary sorting device, which is what makes it the
  editorial reading rather than a variation on `001`.
- **Responsive strategy:** The four-column row becomes three at 1024px with the coverage line
  dropping to a second grid row beneath the name; at 480px the arrow is removed entirely rather
  than being squeezed, since the whole row is already the link.
- **Visual-first check:** 68 visible words, the lowest in the batch.

### WELL-S03-003 — Structured / Visual Modular

- **Structural intent / archetype:** The categories section that answers the next question too.
  Each panel says what the category covers **and** shows what is inside it, without becoming a
  treatment list.
- **Layout model:** A two-by-two field of wide split panels on a sage-grey ground. Each panel is a
  0.82fr / 1.18fr split — reserved media held on the left for the full panel height, content on the
  right — running the category name, one line of coverage, a hairline-separated preview of three
  treatment names, and an onward link pinned to the panel foot.
- **Content-capacity justification:** The capacity here is the internal preview, and it is carried
  by structure: three plain names on hairlines, no description, no media, no action. Removing them
  would remove the reason this study differs from `001`, but they add roughly six words per panel —
  the study is information-capable, not text-dependent. It carries **no price table and no
  treatment menu**, which is the 003 trap named for this sector.
- **Boundary note:** This is the only study in the batch that names treatments. They are routing
  text belonging to the category, not treatments being presented — the distinction is written into
  `./README.md`.
- **Media relationship:** Four reserved areas, one per panel, tall and held to the panel edge.
- **Responsive strategy:** 2 × 2 → single column of wide panels at 1024px, keeping the media-left
  split; the split itself only collapses at 480px, where the media becomes a 16:9 band above the
  content.
- **Visual-first check:** 125 visible words, the highest in the batch and the direct result of the
  four internal previews.

### WELL-S03-004 — Conversion-led

- **Structural intent / archetype:** The section as a question. The visitor is not browsing a set,
  they are answering "what are you here for?", and the four categories are the answers.
- **Layout model:** An oversized question at up to 4.4rem occupies the top of the section, with one
  supporting line beneath it. Four equal answer targets follow in a row — each a tile with a
  reserved media band across its top, a first-person name (*My face*, *My whole body*), one line of
  coverage, and the category's own name as the onward link. A dark full-width fallback band closes
  the section.
- **Conversion behaviour, and how it stays sector-appropriate:** Nothing is collected. The targets
  are routes into a category and the fallback band opens a conversation, so the section carries a
  conversion shape without becoming a form — the trap named for `004` in
  `../WELLNESS-DESIGN-DIRECTION.md`. The composition ends on the escape hatch rather than on the
  last card, so a visitor who cannot answer the question is not left at a dead end.
- **Separation from `001`:** Both are four-up rows, so the difference was made deliberate. There
  the header is compact and the media does the sorting; here the question is the largest element in
  the composition, the targets are name-led with subordinate media bands, and the section resolves
  into a fallback route.
- **Media relationship:** Four reserved bands, deliberately shallow, subordinate to the target name.
- **Responsive strategy:** 4 → 2 → 1 targets; the fallback band stacks its text above a full-width
  action at 768px.
- **Visual-first check:** 118 visible words.

### WELL-S03-005 — Art-directed / Distinctive

- **Structural intent / archetype:** Stillness rather than motion. Four columns held at different
  heights, so the eye steps down and back up across the section instead of scanning a straight row.
- **Layout model:** A deep aubergine ground. Four columns in a cascading rhythm of vertical offsets
  — 0, large, small, largest — deliberately not a straight diagonal. Each category name is set
  oversized and pulled down by `-0.34em` so it crosses the top edge of its own media panel, with
  the panel behind it on a lower z-plane.
- **Distinctiveness, and why it is not paperwork:** The differentiation is rhythm, offset, scale
  and overlap. It reaches for none of the clinical or administrative devices in the sector
  anti-pattern list, and the colour is the one register not yet used anywhere in this sector.
- **Media relationship:** Four tall reserved panels, one per column, each crossed by its name.
- **Empty-state note:** The overlap device works because the name crosses a **tonal panel**, not a
  photograph, so it is legible in the empty state — the state the study will actually be reviewed
  in.
- **Responsive strategy:** The cascade is reduced rather than removed: 4 → 2 columns at 1024px with
  the offsets rescaled, offsets halved again at 768px, and at 480px the offsets go to zero while
  **the type-crossing-panel overlap is kept**. That overlap is the study's identity, so it survives
  every width; only the cascade, which needs side-by-side columns to exist, is dropped.
- **Visual-first check:** 70 visible words.

## Structural Diversity

| Study | Topology | Media | Type treatment | Conversion behaviour |
| --- | --- | --- | --- | --- |
| 001 | Static 4-up grid of full-bleed cards | 4, filling each card | Overlay caption on the image | Round arrow per card |
| 002 | Typographic index, 4 full-width rows | 4 small subordinate plates | Oversized serif name leads | Arrow per row |
| 003 | 2 × 2 split panels, media left | 4, held to the panel edge | Panel heading scale | Onward link per panel, plus internal preview |
| 004 | Question-led chooser + fallback band | 4 shallow bands | Oversized question dominates | Four targets and one escape route |
| 005 | Four staggered columns, type overlap | 4 tall panels crossed by type | Oversized name crosses the panel | Open link per column |

Grounds differ by study: warm white, dark warm brown, sage-grey, warm ochre, deep aubergine. Only
the aubergine is new to the sector; the other four were checked against the `S01` and `S02` batches
so no two adjacent sections share both a ground and a topology.

## Research Metadata

- **Sources:** one visual-research image supplied by the user; four directions originated at the
  user's request.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* and *Cross-section separation*.
- **Visual-first check:** 68–125 visible words per study, against 28–111 in the authored `AUTO-S02`
  batch and 93–149 in `WELL-S02`. This batch sits lower than `WELL-S02` because a category carries
  one line where a treatment carries a name and a description. No study derives its distinctiveness
  from copy volume.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>` element appears
  in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Category media ×4 | `001` — each fills a whole card, under a light gradient scrim | Still image, 3:4 stepping to 3:2 at 768px | Empty tonal surface with a quiet label; the dark overlay caption was contrast-checked against the empty tone, not only against a pale photograph |
| Category plate ×4 | `002` — a small square plate beside each oversized name | Still image, 1:1 | Empty tonal surface; the name and coverage line carry the row entirely |
| Category media ×4 | `003` — held to the left edge of each split panel, full panel height | Still image, tall, becoming a 16:9 band at 480px | Empty tonal surface; the panel's content column is independent of it |
| Category band ×4 | `004` — a shallow band across the top of each answer target | Still image, shallow band | Empty tonal surface; the target is name-led and works without it |
| Category media ×4 | `005` — a tall panel per column, crossed at its top edge by the category name | Still image, 3:4 stepping to 16:11 | Empty tonal surface; the overlap device depends on the panel's edge, not on its content, so it survives an empty slot |

Empty reserved media areas are intended output, not defects.

**Media-density note.** Every study carries exactly four areas — one per category — so none
approaches the thumbnail wall warned against in `../WELLNESS-DESIGN-DIRECTION.md`. What differs is
scale and role: full-card in `001` and `005`, panel-height in `003`, a shallow band in `004`, and a
small subordinate plate in `002`.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Tag balance verified per file, and heading elements verified to sit in
  valid flow containers rather than inside phrasing wrappers.
- Accessibility QA: **PASS, after two corrections.** Every study sets `lang`, scopes a
  `:focus-visible` ring, labels its section with `aria-labelledby`, honours
  `prefers-reduced-motion`, gives every interactive element a 44px-or-greater target, and marks
  decorative arrows `aria-hidden`. Text contrast was measured against each study's own ground
  rather than assumed, and two failures were found and fixed:
  - `005`'s reserved panels were set in `#4d3a4a` on a `#3a2b38` ground — **1.27:1**, so the media
    areas were barely distinguishable from the background and the study did not read as reserving
    media at all. Raised to `#6b5169` (**1.90:1**) with the slot label raised to `#e2d4de`
    (**4.89:1**).
  - `002`'s plate label measured **4.42:1**, just under the 4.5:1 small-text threshold. Raised to
    `#b3a390` (**5.30:1**).
- Responsive QA: **PASS.** Four authored breakpoints per study (1024 / 768 / 480 plus the
  reduced-motion query), recorded per study above — including `005`'s explicit decision about which
  half of its device survives at phone width and which does not.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** All authoring, reference and policy explanation is held in HTML
  comments and `<meta>` fields.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s03-00N` root, verified by scan.
- Claims check: **PASS.** Scanned for efficacy vocabulary, percentages, currency and durations in
  visible copy only. Clean in all five.
- Boundary check: **PASS.** No treatment is presented as the subject in any study. `003`'s internal
  previews are plain routing text only.
- Render check: **PASS, after one correction.** All five studies were rendered in headless Chrome
  at 1440px and inspected. One layout bug was found and fixed: `004`'s question carried
  `max-width: 22ch` on its wrapper rather than on the heading, so the `ch` unit resolved against the
  wrapper's 1rem font size instead of the heading's 4.4rem. The question broke to one word per line
  across five lines and pushed the answer targets far down the section. The constraint was moved
  onto the heading itself at `11ch`, which resolves the question to two lines as intended.

## Notes

- This is the third authored batch in the `WELL` sector, and the first where most of the batch was
  originated rather than derived from references.
- The section role, the four-category set and the boundary with `S02` were written into
  `./README.md` before authoring. The category set is now used consistently across `S01`, `S02` and
  `S03` so the three batches read as one site.
- The review contact sheet at `review/index.html` does not yet include any `WELL` or `AUTO` batch.
  Regenerating it currently fails on this machine because `python3` resolves to a placeholder
  rather than an interpreter. Headless Chrome, which the generator uses for measurement, is present
  and working — it was used for the render check above.
