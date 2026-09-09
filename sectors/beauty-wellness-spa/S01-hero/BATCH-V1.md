# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S01`
- Section Name: `Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S01-001` | Universal / Safe | AUTHORED | `raw/WELL-S01-001.html` |
| `WELL-S01-002` | Premium / Editorial | AUTHORED | `raw/WELL-S01-002.html` |
| `WELL-S01-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S01-003.html` |
| `WELL-S01-004` | Conversion-led | AUTHORED | `raw/WELL-S01-004.html` |
| `WELL-S01-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S01-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. These are the current direction names; the earlier
"Dense / Information-heavy" and "Sector-native / Distinctive" readings are not used anywhere in
this batch. Study IDs never change with a direction name.

## Authoring Direction

Five visual-research images were supplied with the authoring request, with a **locked
reference-to-study mapping** chosen by the user: reference 1 to `001`, reference 2 to `002`, and
so on. They were used as **structural and visual research**, not as pixel targets: composition,
hierarchy, media proportion, type scale, spatial relationships, action placement, layering and
crop strategy were taken; brand, wordmark, wording, photography, product identity, price and
every claim were not.

| Study | Reference | What was taken | What was deliberately not taken |
| --- | --- | --- | --- |
| `WELL-S01-001` | Reference 1 — sage ground, serene centred portrait, very short paragraph, strip of five small thumbnails along the bottom | The calm single-colour field, centred subject dominance, very low copy count, and the idea of a subordinate media rail beneath one dominant image | Its oversized display type layered behind the subject — that device belongs to the art-directed register; its "clinically proven ingredients" claim |
| `WELL-S01-002` | Reference 2 — dark ground with a coloured glow, uppercase kicker above a large two-line serif statement closed with a full stop, one soft pill action, dominant portrait right, hairline rule above a three-column labelled row | The dark editorial register, the serif display voice, the kicker-above-statement hierarchy, the asymmetric copy-and-portrait split, the hairline three-column closing row | Its jewellery content model, its brand, its wording, its material and sourcing claims |
| `WELL-S01-003` | Reference 3 — warm dark tonal frame, centred statement over a dominant face, one heading word carried in a soft rounded box, short lead, single pill action | The warm dark tonal field and the marked-word device inside the heading | Its centred full-bleed overlay topology — that belongs to `004` in this set; its "built on Proof" and "tested to perform" efficacy language, dropped entirely |
| `WELL-S01-004` | Reference 4 — dim stone interior with water as full-bleed ground, short paragraph top-left over the media, pill action opposite it top-right, oversized lowercase word running off the bottom edge | The full-bleed ambient ground, the copy-opposite-action placement over media, the bottom-cropped oversized type | Its site header and primary navigation; its wordmark, which is **not** replaced by an invented brand — the cropped word is a typographic device, not a name |
| `WELL-S01-005` | Reference 5 — saturated colour field, copy block held left, dominant portrait centre, small detail card floating over the portrait's edge with a price | The layering logic — saturated ground, dominant offset media plane, small card breaking across that plane's edge — and the confidence of its colour | Its site navigation; its product content model; its price, and any figure in the floating card |

**No study reproduces a supplied screenshot, embeds one, or loads one remotely.** Every image area
is a reserved, intentionally empty media slot.

**Section-shell check.** References 4 and 5 carry site headers and primary navigation, and
reference 1 carries top-edge brand chrome. None of that appears in any study: these are hero
components only, per the section-shell rule in `standards/01-AUTHORING-STANDARD.md` and its
sector reading in `../WELLNESS-DESIGN-DIRECTION.md`.

**Claims check.** Three of the five references carry content this sector's direction forbids —
reference 1 an ingredient efficacy claim, reference 3 outcome and testing language, reference 5 a
price. In each case the composition was taken and the claim was left. No study in this batch
contains an efficacy claim, percentage, price, duration, rating, practitioner name, qualification,
client or address.

## Study Records

### WELL-S01-001 — Universal / Safe

- **Structural intent / archetype:** The dependable, image-supported spa hero that any studio
  could ship. Reads as a wellness site immediately, with no experimental device, and is the
  easiest of the five to bind to arbitrary content.
- **Layout model:** Centred stacked hero on a light sage field inside a 1440px shell. A centred
  copy column — eyebrow, heading, one supporting sentence, a filled action beside an underlined
  link — sits above one dominant 21:9 media field, which is in turn closed by a subordinate rail
  of five small 4:3 tiles and a single hairline-separated closing line. It is the only study of
  the five whose media sits entirely below the copy.
- **Media relationship:** One dominant field carries the room; the five-tile rail acts as a
  supporting index at clearly subordinate scale. Six areas in total, deliberately hierarchical
  rather than a grid of equals — see *Media Slots* below for the density justification.
- **Responsive strategy:** The dominant field steps 21:9 → 16:9 → 3:2 → 4:3 so it never becomes a
  letterbox sliver on a phone. The five-tile rail becomes a scroll-snapped horizontal rail at
  768px rather than collapsing into a stack, which keeps its "index" reading at every width.
- **Visual-first check:** 51 visible words. The study is carried by the colour field, the centred
  proportion and the dominant-to-subordinate media step, not by copy.

### WELL-S01-002 — Premium / Editorial

- **Structural intent / archetype:** Publication pacing on a dark ground. The register a
  destination spa or a premium skin studio would use — restrained, confident, unhurried.
- **Layout model:** Asymmetric split at `0.92fr / 1.08fr` inside a 1440px shell with a
  `min-height` of `clamp(560px, 70vh, 740px)`. Left column runs an uppercase kicker, a two-line
  serif statement closed with a full stop, one short lead and a single high-contrast pill action.
  Right column is a dominant full-height media panel with a near-square corner radius. Beneath
  both, a hairline rule opens a three-column row of short labelled statements.
- **Media relationship:** One media area only, given the full height of the composition. The
  study's weight comes from the panel's scale against the dark field rather than from media count.
- **Responsive strategy:** Splits to a single column at 1024px with the panel resolving to 16:10,
  then 4:3 at 768px, then **3:4 portrait at 480px** — the panel deliberately becomes taller than
  it is wide on a phone, because a portrait role reads correctly there. The closing row steps
  3 → 2 → 1 columns.
- **Visual-first check:** 60 visible words, the highest in the batch, and all of it in short
  labelled fragments rather than paragraphs.

### WELL-S01-003 — Structured / Visual Modular

- **Structural intent / archetype:** Capacity through visual structure. A bento field of five
  modules at four different sizes, so the hero can hold a way-in for a visitor who does not yet
  know which treatment they want.
- **Layout model:** A twelve-column grid holding five cells — a copy module (span 5), a dominant
  media module (span 7), a small media module (span 3), a grouped category module (span 5) and a
  short statement module (span 4). The heading carries one word inside a soft tinted rounded box,
  the one device taken from reference 3.
- **Media relationship:** Two reserved areas at two clearly different scales — one dominant
  landscape field, one small portrait tile — so the module field reads as composed rather than as
  a uniform grid.
- **Content-capacity justification:** The category module carries **four category names and
  nothing else**: no prices, no durations, no descriptions. It is a grouping and routing device,
  not a treatment menu or a tariff. Removing half the copy from this study would not remove the
  reason it differs from the others — the difference is the module field itself. This satisfies
  the 003 test in `standards/01-AUTHORING-STANDARD.md` and the sector's explicit 003 trap in
  `../WELLNESS-DESIGN-DIRECTION.md`.
- **Responsive strategy:** 12 → 6 columns at 1024px with the copy and dominant media going full
  width and the small media and category modules pairing at 2 + 4; all modules go full width at
  768px. The dominant media steps to 16:9, then 4:3, then 1:1, so the field stays composed rather
  than becoming a column of equal blocks.
- **Visual-first check:** 42 visible words.

### WELL-S01-004 — Conversion-led

- **Structural intent / archetype:** The booking route shapes the composition without replacing
  it. The hero stays an atmospheric spa hero; the route is one integrated band, not a form.
- **Layout model:** A full-bleed ambient media stage with a `min-height` of
  `clamp(480px, 74vh, 720px)` and a 22px radius. Copy sits top-left over the media with an
  outlined pill action opposite it top-right; an oversized lowercase display word runs off the
  stage's bottom edge, cropped by `overflow: hidden`. A three-field availability band in cream
  overlaps the stage's bottom edge by a negative margin, followed by one short closing line.
- **Conversion behaviour, and how it stays sector-appropriate:** The band carries three fields —
  treatment, guests, preferred day — and one action. It is a route-opener, not a booking or
  intake form, and it belongs to this hero rather than being site-wide chrome. This is the
  specific trap named for `004` in `../WELLNESS-DESIGN-DIRECTION.md`: booking is this sector's
  native action, so the risk of the hero collapsing into a widget is higher here than elsewhere.
  A studio or location field was deliberately **omitted** rather than filled with invented
  branches.
- **Media relationship:** One reserved area, serving as the ground of the whole composition. Every
  overlaid element is set against a mid-dark stage tone so the study stays legible in the empty
  state, as required by `standards/05-RESPONSIVE-QA.md`.
- **Responsive strategy:** The band steps 3 fields + action → 2 + full-width action at 1024px →
  single column at 480px, where its overlap is reduced from 46px to 22px so it does not swallow
  the cropped word. The top row stacks at 768px and the action goes full width.
- **Interaction:** Native form controls only — two selects and a `type="date"` input. No
  JavaScript.
- **Visual-first check:** 50 visible words.

### WELL-S01-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The strongest composition in the set. Three explicit z-planes
  on a saturated field, arranged so the media crops into the type and the card breaks the media.
- **Layout model:** A twelve-column canvas over two rows in which three elements deliberately
  overlap: an oversized two-line type plane spanning all columns on row 1; a dominant 4:5 media
  plane at columns 6–12 spanning both rows and cropping into the type; a floating cream detail
  card at columns 4–8 on row 2, breaking across the media's lower-left edge; and a small copy
  block held bottom-left at columns 1–5.
- **Distinctiveness, and why it is not paperwork:** The differentiation is colour, scale,
  overlap and crop — the sector's own visual material. It reaches for none of the clinical or
  administrative devices listed as anti-patterns in `../WELLNESS-DESIGN-DIRECTION.md`. The
  display words are a typographic device, not a brand or a wordmark, and the floating card
  carries a treatment name, a reserved thumbnail and one neutral line — no figure of any kind,
  where the reference carried a price.
- **Media relationship:** One dominant portrait plane plus one small square thumbnail inside the
  card, at deliberately extreme scale difference.
- **Responsive strategy:** The layering is **kept rather than dropped**, as
  `standards/05-RESPONSIVE-QA.md` requires of a distinctive device. At 1024px the media moves to
  columns 3–13 and drops below the type by a top margin, the card re-anchors to columns 1–9 and
  keeps a negative bottom margin so it still breaks the media edge, and the copy moves to a third
  row beneath. At 768px and 480px the same three-plane relationship survives at narrower spans;
  the media steps 4:5 → 1:1 and the card goes full width while still overlapping.
- **Visual-first check:** 35 visible words, the lowest in the batch.

## Structural Diversity

The five studies differ in layout topology, not in styling:

| Study | Topology | Media relationship | Copy position | Conversion behaviour |
| --- | --- | --- | --- | --- |
| 001 | Centred stack, media below copy | 1 dominant + 5 subordinate tiles | Centred, above media | Action pair inside the copy block |
| 002 | Asymmetric split + hairline closing row | 1 dominant full-height panel | Left column | Single pill action |
| 003 | Modular bento field, 5 cells | 2 areas at 2 scales | Inside one module | Routing through a category group |
| 004 | Full-bleed stage with overlaid copy | 1 area as the ground | Overlaid top-left | Integrated three-field band |
| 005 | Layered z-planes with overlap and crop | 1 dominant plane + 1 card thumbnail | Held bottom-left | Single text link |

Colour fields also differ by study and follow each reference's own register: light sage, dark
olive-black, warm dark terracotta, dim stone, saturated teal.

## Research Metadata

- **Sources:** five visual-research images supplied by the user with the authoring request, with
  a locked reference-to-study mapping.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 35–60 visible words per study, against a sector-core comparison band of
  28–111 words in the `AUTO-S01` batch. No study in this batch derives its distinctiveness from
  copy volume.
- **Document-metaphor justification:** `NONE`. No study uses a technical, clinical, professional
  or administrative document metaphor.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE. `WELL-S01-004` uses native form controls — two `select` elements
  and one `input type="date"` — and needs no script. The other four studies are fully static.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Treatment room | `WELL-S01-001` — the dominant field; the room the visitor is being invited into | Still image, 21:9 at 1440px stepping to 4:3 at 480px | Empty tonal surface with a quiet label; the copy block above stands alone and the composition still reads |
| Rail tile ×5 | `WELL-S01-001` — a subordinate supporting index beneath the dominant field | Still image, 4:3 | Empty tonal surfaces with quiet labels; the rail reads as a deliberate strip when empty and scroll-snaps at narrow widths |
| Portrait | `WELL-S01-002` — a full-height portrait holding the right of the split | Still image, full-height panel stepping to 3:4 portrait at 480px | Empty tonal surface; the serif statement and the closing row carry the study on their own |
| Treatment in progress | `WELL-S01-003` — the dominant module of the bento field | Still image, landscape stepping to 1:1 at 480px | Empty tonal surface; the module field's composition is independent of it |
| Texture | `WELL-S01-003` — the small counterweight module | Still image, 3:4 stepping to 16:9 | Empty tonal surface at deliberately small scale |
| Treatment space | `WELL-S01-004` — the ambient ground of the whole composition | Still image or ambient video, full-bleed | Mid-dark tonal ground with a centred quiet label; all overlaid copy, the action and the band are contrast-checked against the empty state |
| Treatment portrait | `WELL-S01-005` — the dominant offset plane that crops into the type | Still image, 4:5 stepping to 1:1 | Empty tonal surface; the plane's silhouette is what crops the type, so the layering survives an empty slot |
| Detail | `WELL-S01-005` — the thumbnail inside the floating card | Still image, 1:1 | Empty tonal surface with a quiet label; the card's text stands alone |

Empty reserved media areas are intended output, not defects.

**Media-density justification for `WELL-S01-001`.** `../WELLNESS-DESIGN-DIRECTION.md` warns that a
wall of small tiles reads as a catalogue rather than as a spa. The six areas in this study are
deliberately hierarchical, not equal: one dominant 21:9 field plus five clearly subordinate 4:3
tiles at roughly a fifth of its width. The rail is a supporting index beneath a dominant image,
which is the relationship reference 1 uses, and no other study in the batch carries more than two
areas.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study.
- Accessibility QA: **PASS, after one correction.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, gives every interactive
  element a 44px-or-greater target, and marks decorative arrows `aria-hidden`. The `WELL-S01-004`
  band labels all three fields and carries an `aria-label` on the form.
  Text contrast was measured against each study's own ground rather than assumed. One failure was
  found and fixed: `WELL-S01-005`'s oversized type plane, which is also that study's `h1`, was
  first set in `#1c666d` on `#10555c` — **1.27:1**, far below the 3:1 large-text threshold and
  effectively invisible in render. It was raised to `#74afae` (**3.43:1**) and the media plane
  tightened from 3:4 to 4:5, which also made the intended crop-into-the-type layering legible for
  the first time. Every other foreground/ground pair in the batch measures between 4.06:1 and
  7.70:1.
- Responsive QA: **PASS.** Four authored breakpoints per study (1024 / 768 / 480 plus the
  reduced-motion query). Each study's narrow-width behaviour is authored rather than inherited and
  is recorded per study above; `WELL-S01-005` keeps its three-plane layering at every width rather
  than resolving to a stack.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script in
  any study.
- Section-shell check: **PASS.** No global header, navigation, footer or announcement bar in any
  study, verified by scan.
- Visible-copy check: **PASS.** All authoring, reference and policy explanation is held in HTML
  comments and `<meta>` fields. No study displays authoring notes.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s01-00N` root, verified by scan.
- Render check: **PASS.** All five studies were rendered in headless Chrome at 1440px and
  inspected. No overflow, no collapsed slot, no overlapping text, and no element lost against its
  ground. This check is what surfaced the `WELL-S01-005` contrast failure recorded above.
- Claims check: **PASS.** No efficacy claim, percentage, price, duration, rating, practitioner
  name, qualification, client or address appears in any visible composition, verified by scan.

## Notes

- This is the first authored batch in the `WELL` sector, and the first authored under
  `../WELLNESS-DESIGN-DIRECTION.md`, which was written before authoring began rather than after.
- The three claims dropped from references 1, 3 and 5 are recorded in *Authoring Direction* above
  so a reviewer can see what was deliberately not carried across.
- The review contact sheet at `review/index.html` does not yet include this batch. Regenerating it
  currently fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter; the batch is complete and the contact sheet is a separate workspace-level repair.
