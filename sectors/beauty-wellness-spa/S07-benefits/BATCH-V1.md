# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S07`
- Section Name: `Benefits`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S07-001` | Universal / Safe | AUTHORED | `raw/WELL-S07-001.html` |
| `WELL-S07-002` | Premium / Editorial | AUTHORED | `raw/WELL-S07-002.html` |
| `WELL-S07-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S07-003.html` |
| `WELL-S07-004` | Conversion-led | AUTHORED | `raw/WELL-S07-004.html` |
| `WELL-S07-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S07-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S08` and `S14` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — And The Distinction That Resolves It

`Benefits` is the most claim-prone section name in this sector. The role exists to say what you get
out of it, and "what you get out of a treatment" is exactly the efficacy language the sector
direction forbids. The section could not be authored at all without a distinction:

| Kind of benefit | Example | Status |
| --- | --- | --- |
| **Treatment outcome** | "Clearer skin", "reduced tension", "a younger appearance" | **Forbidden.** An efficacy claim about a body. |
| **Experience and service** | "One guest at a time", "the same hands throughout", "nothing sold in the room" | **Allowed.** A fact about how the business chooses to operate. |

**This section is about the benefits of coming here, not the benefits of the treatment.** A studio
controls how it works; it does not control what a body does. Every benefit in this batch is an
operating commitment — something the studio decides and can keep — rather than a physiological
result it would have to prove.

This is the same move as the procedural-description rule established for `S02`, applied one level
up: `S02` describes what happens in the room, `S07` describes how the room is run. It is also the
stronger commercial position: every spa can claim relaxation; not every spa runs one guest at a
time.

**Not present in any study:** an efficacy claim, an outcome description, a percentage, a rating, a
review, a client, a superlative comparison to other studios, an award, a certification, a price, a
duration, an invented statistic, or an urgency device.

## The Benefit Set

Six operating commitments, used consistently across the batch so the five studies read as one
section. `001` and `003` carry all six, `002` carries three, `004` carries four and `005` carries
four — the count is part of each study's register, not an inconsistency.

| Commitment | What it means |
| --- | --- |
| One guest at a time | The room is yours for the whole appointment |
| The same hands throughout | Whoever you booked does the treatment start to finish |
| Nothing sold in the room | If a product would suit you, we say so afterwards |
| Unhurried appointments | Nothing is booked so tightly a treatment has to be cut short |
| Decided when we see you | What gets used is chosen in the room, not at the booking |
| Easy to move | Changing an appointment is a message, not a process |

## Study Records

### WELL-S07-001 — Universal / Safe

- **Structural intent / archetype:** The dependable version. All six commitments, plainly set.
- **Layout model:** A split header closed by a strong rule, above a two-column list where each item
  is separated by a hairline. **Rules rather than cards** — this is the deliberate move: six short
  statements in six boxes would read as six identical tiles, and the ruled list lets the statements
  differ in length without the layout looking ragged.
- **Media relationship:** None, deliberately. Recorded rather than left as an omission — see the
  *Media Slots* note below.
- **Responsive strategy:** The header stacks at 768px and the list goes to a single column at the
  same breakpoint, so a two-column list of short items never gets narrow enough to break awkwardly.
- **Visual-first check:** 155 visible words across six items plus a header — high for this sector,
  and addressed under *Research Metadata*.

### WELL-S07-002 — Premium / Editorial

- **Structural intent / archetype:** Fewer, larger, and slower. Three commitments at display scale
  instead of six at list scale.
- **Layout model:** A wide shallow media band (24:7) across the top, then a single centred 44rem
  measure carrying three commitments as large serif statements on hairlines, each with a small
  supporting line beneath.
- **The device that keeps it honest:** the small line under each statement exists specifically to
  stop the large type reading as a slogan. A display-scale "One guest at a time" alone is a claim
  shape; with the operational sentence under it, it is a commitment.
- **Media relationship:** One wide shallow band, placed above the measure rather than beside it so
  the column below stays a single unbroken reading line.
- **Responsive strategy:** The band steps 24:7 → 21:8 → 16:9 → 4:3; at 480px the centred measure
  becomes left-aligned, because centred text at phone width is harder to read than it looks in a
  desktop mock.
- **Visual-first check:** 75 visible words.

### WELL-S07-003 — Structured / Visual Modular

- **Structural intent / archetype:** The same six commitments, sorted and given a second tier.
- **Layout model:** Two labelled groups — *In the room* and *Around the visit* — each holding three
  two-tier modules. Each module carries the commitment above a hairline and what it means in
  practice below it.
- **Content-capacity justification:** The capacity is the sorting and the two-tier module, not
  longer copy. The same six statements appear in `001` as a flat list; here they gain a grouping
  axis and an internal division, which is what makes the study structurally rather than verbally
  denser.
- **Grouping note:** the two labels are an organising device for six statements. They are not a
  taxonomy, a register or a specification structure.
- **Media relationship:** None, deliberately.
- **Responsive strategy:** Groups stack at 768px, keeping their labels, so the sorting survives at
  every width rather than collapsing into one undifferentiated list.
- **Visual-first check:** 165 visible words, the highest in the batch and in the sector — addressed
  under *Research Metadata*.

### WELL-S07-004 — Conversion-led

- **Structural intent / archetype:** One reason made *the* reason.
- **Layout model:** A compact header, then one commitment promoted to a full panel — reserved media
  beside copy, carrying the booking action — over a row of three smaller supporting commitments on
  hairlines.
- **Conversion behaviour:** the device is **hierarchy**, not urgency. The promoted panel is the
  only place in the section with media, an action and display-scale type, so the ranking is done
  by scale rather than by pressure. There is deliberately **no urgency device** — no limited
  availability, no countdown, no "spaces going fast" — which would be both an invented diary state
  and the wrong register for this sector.
- **Media relationship:** One reserved area, inside the promoted panel only. The three supporting
  items carry none, so the scale difference does the ranking.
- **Responsive strategy:** The promoted panel goes to one column at 1024px with the media becoming
  a 16:7 band; the supporting row goes to one column at 768px.
- **Visual-first check:** 90 visible words.

### WELL-S07-005 — Art-directed / Distinctive

- **Structural intent / archetype:** Restraint made into a device. Four commitments on a deep calm
  ground, each behind an oversized tonal numeral.
- **Layout model:** Four plates in a 2 × 2 field, each with a hairline top edge and an oversized
  numeral at up to 12rem set only slightly off the ground colour, with the commitment and its line
  sitting over the numeral's lower half.
- **Contrast decision, recorded deliberately:** the numerals sit at **1.43:1** against the ground.
  **This is allowed here and was not allowed in `WELL-S01-005`**, where the same low-contrast
  treatment was applied to that study's `h1` and had to be raised to 3.43:1 after the render check
  caught it. The difference is that these numerals are genuinely decorative — they carry no
  information the list order does not already carry, and each is marked `aria-hidden`. Everything
  that conveys meaning in this study is at full contrast: the headings measure 12.44:1 and the
  supporting lines 6.66:1.
- **Media relationship:** None. The numerals are the visual event; a photograph per plate would
  compete with them and flatten the one device the study has.
- **Responsive strategy:** The watermark shrinks with the plate across three steps but never
  leaves — the device is the study's identity, so it survives at phone width rather than being
  dropped as decoration.
- **Visual-first check:** 97 visible words.

## Structural Diversity

| Study | Topology | Items | Type treatment | Media |
| --- | --- | --- | --- | --- |
| 001 | Two-column ruled list | 6 | Sans, list scale | None |
| 002 | Wide band above a centred measure | 3 | Serif, display scale | One wide band |
| 003 | Two labelled groups of two-tier modules | 6 | Sans, card scale, two tiers | None |
| 004 | Promoted panel above a supporting row | 4 | Sans, one at display scale | One, in the panel |
| 005 | 2 × 2 plates with tonal watermark numerals | 4 | Sans over oversized decorative numerals | None |

Grounds: warm apricot-white, mid sand, pale mauve, deep emerald, deep teal-black. None repeats a
ground used in `WELL-S01`–`S06`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check, stated honestly:** 75–165 visible words. `003` at 165 and `001` at 155 are
  the highest counts in the sector to date. **This is a property of the role, not padding.** A
  benefits section is a set of statements; there is no imagery that can replace the statement
  itself, and both studies carry all six commitments with one explanatory line each — roughly 24
  words per item including the heading. Neither derives its distinctiveness from copy: `001`'s
  difference is the ruled two-column list, `003`'s is the grouping and the two-tier module, and
  both would still differ from the others if every line were cut in half. The studies that carry
  fewer commitments — `002` at 75 words and `004` at 90 — show the same content at a third of the
  count, which is the honest demonstration that the copy is item count rather than verbosity.
- **Document-metaphor justification:** `NONE`. No specification sheet, charter, policy register or
  compliance list device is used. `005`'s numerals are an ordering device and are addressed in its
  study record.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>` element appears
  in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Studio interior | `002` — a wide shallow band above the measure | Still image, 24:7 stepping to 4:3 | Empty tonal surface with a quiet label; the measure below carries the study |
| Treatment room | `004` — inside the promoted panel, beside its copy | Still image, filling half the panel, becoming a 16:7 band at 1024px | Empty tonal surface; the panel's copy and action stand alone |

**Why three of five studies carry no media, recorded rather than left as an omission.**
`../WELLNESS-DESIGN-DIRECTION.md` warns that a visually oriented section must not quietly become
text-only. This role is not visually oriented: it is a small set of short commitments, and there is
no photograph of "nothing is sold in the room". One decorative image per statement would be filler
occupying space the policy reserves for something the role actually needs. `002` and `004` carry
media because their registers use it structurally — a band that sets the room before the reading
line, and a panel whose media is what promotes one commitment above the others. The other three
would not be improved by it.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly, with heading levels running h1 → h2 → h3 without skips.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target. Contrast was measured against each study's own ground; the one
  deliberately low-contrast element in the batch is `005`'s decorative numeral set, and the reason
  it is permissible there is recorded in its study record and in the file's own comment.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above —
  including `002`'s decision to abandon centred text at phone width and `005`'s decision to keep
  its watermark at every width.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s07-00N` root, verified by scan.
- **Outcome-claim check: PASS.** This batch's most important check. Visible text only, comments
  stripped, scanned for outcome and efficacy vocabulary — *results, improve, reduce, relax,
  relieve, heal, glow, younger, rejuvenate, restore, transform, proven, guarantee* — for
  superlatives — *best, leading, number one, finest* — and for awards, certifications,
  percentages, invented statistics, currency, durations, ratings, reviews and urgency words
  — *limited, hurry, only N*. Clean in all five.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `005`'s watermark reads as a deliberate device with the text sitting at full contrast
  over it; `004`'s hierarchy reads correctly, with the promoted panel clearly outranking the
  supporting row; `003`'s two groups and two-tier modules read as intended. This is the first batch
  in the sector to need no render correction.

## Notes

- This is the seventh authored batch in the `WELL` sector and the fifth authored entirely without
  references.
- The outcome-versus-operation distinction established here is the most reusable rule produced in
  this sector so far. It applies directly to `S14 About Philosophy`, and to the equivalent
  "why choose us" sections in every other sector — particularly `healthcare-medical` and
  `dental-clinics`, where the same claim risk exists in a stricter regulatory setting.
- The `S07` / `S08` / `S14` boundary written into `./README.md` matters because all three can be
  written as "how we work": `S07` states the commitment, `S08` gives the sequence, `S14` explains
  the thinking.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
