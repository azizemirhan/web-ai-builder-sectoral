# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S02`
- Section Name: `Treatments / Services`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S02-001` | Universal / Safe | AUTHORED | `raw/WELL-S02-001.html` |
| `WELL-S02-002` | Premium / Editorial | AUTHORED | `raw/WELL-S02-002.html` |
| `WELL-S02-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S02-003.html` |
| `WELL-S02-004` | Conversion-led | AUTHORED | `raw/WELL-S02-004.html` |
| `WELL-S02-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S02-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's own role and its boundary with `S03` are in
`./README.md`.

## Authoring Direction

**Three** visual-research images were supplied with the authoring request, and the user asked for
the remaining two studies to be originated. Unlike the `WELL-S01` batch, which used a locked
reference-to-study order, the user chose here to **place each reference at the variant whose
register it actually occupies**, and to have the two unoccupied directions authored from nothing:

| Reference | Placed at | Why |
| --- | --- | --- |
| Reference 2 — `POPULAR SERVICES` card grid | `001` Universal / Safe | An even media-topped card grid is the most broadly shippable answer to this role |
| Reference 1 — brand identity presentation board | `003` Structured / Visual Modular | Its only transferable idea is a mosaic of unequal interlocking panels, which is the modular territory |
| Reference 3 — edge-bleeding horizontal card rail | `005` Art-directed / Distinctive | A bleeding rail with type over full-bleed media is a distinctive device, not a safe or modular one |
| — | `002` Premium / Editorial | Originated. No supplied reference occupied the publication-spread register |
| — | `004` Conversion-led | Originated. No supplied reference made the act of choosing a treatment the organising idea |

References were used as **structural and visual research**, not as pixel targets.

| Study | What was taken | What was deliberately not taken |
| --- | --- | --- |
| `001` ← Ref 2 | The even media-topped card grid, the name-plus-one-line card contract, the section-header-above-grid hierarchy | Its icon set — an invented iconography would be fabricated brand material, replaced here by a small category tag; its outcome copy ("improve skin texture, tone, and reduce imperfections", "lift, firm, and rejuvenate for younger-looking skin") |
| `003` ← Ref 1 | The mosaic of unequal interlocking panels, the mix of pure-media panels with content panels, the sage-and-cream register | Its entire content model. The image is a brand identity board — logo blocks, device mockups, an exterior shot. A treatments section is not a logo presentation, and no wordmark, mockup or brand artefact appears in the study |
| `005` ← Ref 3 | The edge-bleeding horizontal rail, the tall card proportion, the serif name over full-bleed media, the closing pill action | Its arrow and dot controls, which need a script to do anything — a control that does not work is worse than no control, so the rail is driven by native scroll-snap; its third-party help widget, which is site chrome; its outcome copy ("restore your skin's natural glow", "promote deep relaxation") |

**No study reproduces a supplied screenshot, embeds one, or loads one remotely.** Every image area
is a reserved, intentionally empty media slot.

**Section-shell check.** No global header, navigation, footer or announcement bar appears in any
study, verified by scan.

**Claims check.** All three references carry outcome and efficacy language, which is the expected
failure mode for this section role — real spa sites describe treatments by what they achieve. In
every case the composition was taken and the claim was left.

The technique used across the batch, and recorded as the section's copy rule in `./README.md`, is
**procedural description**: every treatment is described by what happens in the room, in order,
rather than by its result.

    Not: "Restores volume and softens fine lines."
    But: "Cleansing, steam and extraction, then a slow massage through the face and neck."

This keeps the copy genuinely useful to a visitor while making no claim that would need evidence.
No study contains an efficacy claim, percentage, price, duration, rating, practitioner name,
qualification, client or address.

**Boundary check.** Category names appear only as small tags on treatment cards, never as the item
being presented. The subject of every study is a named treatment. Category-level browsing is
`S03`'s role.

## Study Records

### WELL-S02-001 — Universal / Safe

- **Structural intent / archetype:** The dependable treatments grid any spa, salon or studio could
  ship. Easiest of the five to bind to an arbitrary number of treatments.
- **Layout model:** A two-part section header — heading left, supporting line and onward link
  right — closed by a hairline rule, above an even three-column, two-row card grid. Each card is
  media-topped at 4:3, then a category tag, the treatment name, one procedural line, and a
  rule-separated onward link pinned to the card foot.
- **Media relationship:** Six reserved areas at equal, generous scale — one per treatment. The
  role's honest minimum: a treatment list without one image per treatment is a price list.
- **Responsive strategy:** 3 → 2 → 1 columns; the card media steps 4:3 → 16:9 → 3:2 so a
  single-column card on a phone does not become a tall block of empty tone. The header splits to
  one column at 768px.
- **Visual-first check:** 149 visible words across six treatments — roughly 13 words of copy per
  treatment. The count is driven by carrying six items, not by longer copy per item.

### WELL-S02-002 — Premium / Editorial

- **Structural intent / archetype:** A publication feature spread. Three treatments instead of
  six, each given a full-width row, with the pacing and measure of a printed magazine.
- **Layout model:** A left-aligned header block, then three full-width rows separated by hairline
  rules. Each row is a 1.06fr / 0.94fr split of media and copy that **alternates side down the
  sequence**, so the eye crosses the page three times. Serif display throughout, with a small
  01/02/03 sequence marker above each name.
- **Media relationship:** Three reserved areas at 5:4, the largest per-item media in the batch.
- **Document-metaphor note:** The 01/02/03 markers are an editorial sequence device. They are not
  a schedule, a protocol, a course register or a session count, and carry no figure a visitor
  could read as a claim.
- **Responsive strategy:** The alternation is deliberately **dropped** at 768px rather than
  preserved — below that width there is no crossing to read, and forcing media-right on alternate
  rows would only produce an inconsistent reading order. Rows become media-then-copy throughout,
  and the media steps 5:4 → 16:10 → 4:3.
- **Visual-first check:** 141 visible words across three treatments. Higher per item than `001` by
  design — editorial measure — but the study's distinctiveness is the alternating row topology,
  not the copy.

### WELL-S02-003 — Structured / Visual Modular

- **Structural intent / archetype:** Capacity through visual structure. Seven panels at four sizes
  and two shapes, interlocking rather than repeating.
- **Layout model:** A twelve-column mosaic. A header panel set directly on the sage ground at
  columns 1–5; one tall media-topped treatment panel at 5–10 spanning two rows; a tall pure-media
  panel at 10–13 spanning two rows; three horizontal media-left treatment panels; and one short
  statement panel. Two panel shapes — media-topped and media-left — are what make it read as a
  mosaic rather than a grid.
- **Content-capacity justification:** The study holds four treatments, two standalone media areas
  and a statement in one composed field. Its difference from the others is the panel field itself;
  removing half the copy would not remove that difference. It carries **no price table, no
  treatment menu and no tariff**, which is the specific 003 trap named for this sector in
  `../WELLNESS-DESIGN-DIRECTION.md`.
- **Media relationship:** Five reserved areas at three scales — one large 16:11 field, one tall
  standalone panel, three narrow fixed-width strips inside the horizontal panels.
- **Responsive strategy:** 12 → 6 columns at 1024px with the header going full width and the lead
  and standalone media panels pairing 4 + 2; every panel goes full width at 768px in an authored
  order that keeps the lead treatment first and the statement last.
- **Visual-first check:** 117 visible words.

### WELL-S02-004 — Conversion-led

- **Structural intent / archetype:** The section where choosing is the composition. A master-detail
  picker: the treatment names are the interface, and the booking action lives inside the detail
  panel rather than under the section.
- **Layout model:** A 0.72fr / 1.28fr split. Left column is a vertical index of four treatment
  names on hairline rules, with the "not sure" escape route directly beneath it. Right column is a
  single large detail card — media, tag, name, procedural description, a filled booking action and
  an underlined "ask if it suits me" link.
- **Conversion behaviour, and how it stays sector-appropriate:** This is the trap named for `004`
  in `../WELLNESS-DESIGN-DIRECTION.md` — booking is this sector's native action, so the risk of
  the section collapsing into a form is highest here. It does not collapse: **nothing is
  collected.** The panel action opens a booking route; the section's content role — telling you
  what each treatment involves — stays primary and in fact gets more room per treatment than in
  any other study in the batch. The escape hatch sits beside the choices rather than after them,
  so a visitor who cannot choose is not left at a dead end.
- **Interaction:** Native radio inputs plus CSS sibling selectors — selecting a name swaps the
  panel, with **no JavaScript**. The group carries a visually-hidden `legend`, every option is a
  real `label` bound to its input, arrow keys move through it as a native radiogroup, and the
  focus ring is mirrored onto the visible option for each of the four inputs.
- **Media relationship:** Four reserved 16:9 areas, one per panel, of which one is visible at a
  time — the lowest simultaneous media density in the batch.
- **Responsive strategy:** The split tightens to 0.86fr / 1.14fr at 1024px and becomes a single
  column at 768px, where the index sits above the panel and the picker still works unchanged.
- **Visual-first check:** 99 visible words on screen. The file's markup totals 212 because all four
  panels are present; the three unselected panels account for 113 of those and are `display: none`.

### WELL-S02-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The most cinematic reading of the role. The treatments are
  presented as a sequence you move through rather than a set you scan.
- **Layout model:** A near-black ground, a serif header with a scroll cue opposite, then a
  horizontal rail of five tall 3:4 cards that **bleeds past the shell padding on both sides** via
  negative inline margins, with `scroll-padding-left` holding the first card flush to the text
  column. Each card is a full-bleed reserved media field with a gradient scrim over its lower
  third and a serif name plus one procedural line set over it. A single pill action closes the
  section beneath a hairline rule.
- **Distinctiveness, and why it is not paperwork:** The differentiation is crop, scale, sequence
  and typographic register — the sector's own visual material. It reaches for none of the clinical
  or administrative devices in the sector anti-pattern list.
- **Media relationship:** Five reserved areas, each filling an entire card. The scrim is a CSS
  gradient, not an asset, and exists so the overlaid name stays legible once real photography is
  placed; the empty-state contrast was measured rather than assumed.
- **Responsive strategy:** Card width steps `clamp(238px, 25vw, 360px)` → `min(62vw, 300px)` →
  `78vw`, and the card proportion steps 3:4 → 4:5 → 3:4, so the number of cards visible at once
  falls from about four to just over one while the bleed is preserved at every width. The rail is
  native scroll-snap, so it works on touch and with a trackpad without any control.
- **Static-state note:** The reference is shown mid-scroll, with a partial card at the left edge.
  A static study cannot start mid-scroll without a script, so the first card is flush left and the
  bleed runs off the right. This is the honest initial state of the same rail.
- **Visual-first check:** 93 visible words, the lowest in the batch.

## Structural Diversity

| Study | Topology | Media | Copy position | Conversion behaviour |
| --- | --- | --- | --- | --- |
| 001 | Even 3 × 2 card grid under a split header | 6 equal, media-topped | Inside each card | Onward link per card |
| 002 | Three alternating full-width editorial rows | 3 large, side-alternating | Opposite the media, alternating | One text link per row |
| 003 | Twelve-column mosaic, 7 panels, 2 shapes | 5 at three scales | Inside panels of two shapes | Onward link per panel |
| 004 | Master-detail picker | 4, one visible at a time | Inside the detail panel | Booking action inside the panel |
| 005 | Edge-bleeding horizontal scroll-snap rail | 5, each filling a card | Overlaid on the media | One closing pill action |

Grounds also differ by study and follow each source register: warm sand, warm clay, deep sage,
deep forest green, near-black.

## Research Metadata

- **Sources:** three visual-research images supplied by the user; two directions originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 93–149 visible words per study, against 28–111 in the authored
  `AUTO-S02` batch, which is the same catalog position under the corrected standard. This batch
  sits above that band because the role carries named items with a description each, where
  `AUTO-S02` carries four one-word categories. Per-item copy is one line — roughly 13 words in
  `001`. No study derives its distinctiveness from copy volume.
- **Document-metaphor justification:** `NONE`. No study uses a technical, clinical, professional
  or administrative document metaphor. The `002` sequence markers are addressed in its study
  record.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `004` uses radio inputs with CSS sibling selectors and `005`
  uses native scroll-snap; neither needs a script. The other three studies are fully static. No
  `<script>` element appears in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Treatment media ×6 | `001` — one photograph per treatment card | Still image, 4:3 stepping to 3:2 at 480px | Empty tonal surface with a quiet label; the card's tag, name, line and link stand alone |
| Treatment media ×3 | `002` — the large editorial field beside each row | Still image, 5:4 stepping to 4:3 | Empty tonal surface; the serif name and procedural line carry the row |
| Facial treatment media | `003` — the mosaic's lead panel | Still image, 16:11 stepping to 3:2 | Empty tonal surface; the panel field's composition is independent of it |
| Studio detail | `003` — the tall standalone panel, the only area with no text of its own | Still image, tall | Empty tonal surface with a quiet label; reads as a deliberate tonal panel when empty |
| Media ×3 | `003` — the narrow strips inside the horizontal panels | Still image, fixed-width strip | Empty tonal surfaces at deliberately small scale |
| Treatment media ×4 | `004` — one per detail panel, one visible at a time | Still image, 16:9 stepping to 4:3 | Empty tonal surface; the panel body carries the treatment |
| Card media ×5 | `005` — each fills an entire rail card, under a CSS gradient scrim | Still image, 3:4 stepping to 4:5 | Empty tonal surface with a quiet label; the overlaid name is contrast-checked against the empty tone, not only against a hypothetical photograph |

Empty reserved media areas are intended output, not defects.

**Media-density note.** `../WELLNESS-DESIGN-DIRECTION.md` warns that a wall of small treatment
thumbnails reads as a catalogue rather than as a spa. No study here uses thumbnails: `001`'s six
areas are full-width cards in a three-column grid, `003`'s five are at three deliberately
different scales, `005`'s five each fill a whole card, and `004` shows one at a time. `002`
carries the fewest and largest.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Tag balance verified per file, and heading elements verified to sit in
  valid flow containers rather than inside phrasing wrappers.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, gives every interactive
  element a 44px-or-greater target, and marks decorative arrows `aria-hidden`. `004`'s picker is a
  native radiogroup with a visually-hidden legend, bound labels and a mirrored focus ring; `005`'s
  rail is a labelled list of links, reachable by keyboard without any control. Text contrast was
  measured against each study's own ground, including `005`'s overlaid names against the **empty**
  slot tone rather than against an assumed photograph.
- Responsive QA: **PASS.** Four authored breakpoints per study (1024 / 768 / 480 plus the
  reduced-motion query). Each study's narrow-width behaviour is authored rather than inherited and
  is recorded per study above, including `002`'s deliberate decision to drop its alternation and
  `005`'s decision to preserve its bleed.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** All authoring, reference and policy explanation is held in HTML
  comments and `<meta>` fields.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s02-00N` root, verified by scan. `004`'s `:checked` and
  `:focus-visible` sibling rules are ID-based but remain scoped as descendants of the study root.
- Claims check: **PASS.** Scanned for efficacy vocabulary, percentages, currency and durations, in
  visible copy only. Clean in all five.
- Render check: **PASS, after one correction.** All five studies were rendered in headless Chrome
  at 1440px and inspected. `004`'s picker was confirmed to actually work — the checked option is
  highlighted and its panel is the one shown. One composition problem was found and fixed: `004`'s
  left column ended after four short rows against a much taller detail panel, leaving a large void.
  The "not sure which to choose" route was moved out from under the section and placed directly
  beneath the index, which fills the column and puts the escape hatch beside the choices rather
  than after them.

## Notes

- This is the second authored batch in the `WELL` sector. The section's role and its boundary with
  `S03` were written into `./README.md` before authoring, because the two section names —
  *Treatments Services* and *Service Categories* — do not distinguish themselves and the two
  batches would otherwise converge.
- Reference 1 is the first supplied reference in this sector that is not a website. It was still
  usable, but only for its panel structure; the record above states exactly which part was
  extracted and which part was discarded.
- The review contact sheet at `review/index.html` does not yet include this batch, or the
  `WELL-S01` batch, or the `AUTO` batches. Regenerating it currently fails on this machine because
  `python3` resolves to a placeholder rather than an interpreter. Headless Chrome, which the
  generator uses for measurement, is present and working — it was used for the render check above.
