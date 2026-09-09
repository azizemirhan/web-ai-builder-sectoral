# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S17`
- Section Name: `Gift Cards`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S17-001` | Universal / Safe | AUTHORED | `raw/WELL-S17-001.html` |
| `WELL-S17-002` | Premium / Editorial | AUTHORED | `raw/WELL-S17-002.html` |
| `WELL-S17-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S17-003.html` |
| `WELL-S17-004` | Conversion-led | AUTHORED | `raw/WELL-S17-004.html` |
| `WELL-S17-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S17-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S11` and `S12` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint

The `S11` field-versus-figure test applies unchanged, plus one term it does not cover.

| Element | Treatment |
| --- | --- |
| Gift amount | **Reserved field** — a gift card has an amount by definition |
| Card artwork | **Reserved media area** |
| Denomination tiers | **Omitted** — a set of fixed amounts is a set of invented figures |
| An expiry period | **Omitted entirely** |
| Delivery time | **Omitted entirely** |

**Why an expiry period is omitted rather than reserved.** A reserved *"valid for —"* asserts that
the card expires at all, which is a commercial policy many studios deliberately do not have — the
same failure as `S10`'s empty star row and `S12`'s empty saving. The batch takes the opposite
position and states it: **the card does not expire.**

**Not present in any study:** an invented amount, denomination, currency symbol, figure, expiry
date or period, delivery time, postage cost, booking fee, discount or bonus-credit offer; a
popularity or value tier; an urgency device. Verified by scan — the only digits in visible copy are
`003`'s decorative step numbers.

## What Is Real — The Awkward Bits

A gift card section normally sells warmth. What a buyer is anxious about is narrower and entirely
answerable with operating commitments:

| The worry | The commitment |
| --- | --- |
| They will see what I spent | **The amount is not printed on the card** |
| There will be an awkward balance left | Whatever is left stays on it |
| It will expire before they use it | It does not expire |
| They will feel stuck with my choice | It can go on anything, or toward something dearer |
| It will feel impersonal | The message is reproduced exactly as written |

**The first is the section's strongest content and the one most sites get wrong.** Printing the
value on a gift card turns a present into a receipt. Saying plainly that it is not printed is
differentiating, costs the studio nothing, and is exactly the kind of thing a placeholder can state
honestly. It appears in all five studies and is the headline of `004`.

## The Forms

| Choice | Options |
| --- | --- |
| How it arrives | A printed card, handed over — or a digital one, sent by email |
| What it is for | An amount to spend on anything — or a named treatment from `S02` |
| What comes with it | A message written by the buyer |

## Study Records

### WELL-S17-001 — Universal / Safe

- **Layout model:** The two forms side by side, each with a reserved 8:5 card artwork, a reserved
  amount field on a hairline, and its own action — above three shared commitments in a row.
- **Why the commitments sit below rather than inside the cards:** they apply to both forms
  identically, and repeating them per card would imply a difference that does not exist.
- **Responsive strategy:** forms unstack at 768px with the action going full width; the commitment
  row steps 3 → 2 → 1.

### WELL-S17-002 — Premium / Editorial

- **Layout model:** One reserved card plate given the left half at object scale, with a short serif
  proposition, the reserved amount and one action beside it, and every commitment compressed into a
  single closing line.
- **The editorial reading:** the card is a **designed artefact, not a product thumbnail**. The copy
  is cut back to what a buyer needs to decide, which turns out to be very little once the object is
  doing the work. Lowest word count in the batch.
- **Responsive strategy:** the split unstacks at 768px; the action goes full width.

### WELL-S17-003 — Structured / Visual Modular

- **Layout model:** The three decisions a buyer actually makes, as three numbered modules — how it
  arrives, what it is for, what goes with it.
- **The device:** each module carries **its own option shape** — two artwork cards, two text
  choices with the reserved amount beneath, and one reserved message area — so the three read as
  three different kinds of decision rather than as three columns of one table. Same principle as
  `S09-003` and `S12-003`.
- **Interaction, deliberately absent:** the options are shown, not selected. Selection belongs to a
  real checkout, and a study that mocked one would be inventing a flow rather than authoring a
  section.
- **Responsive strategy:** 3 → 2 modules with the third spanning full width, then one per row.

### WELL-S17-004 — Conversion-led

- **Layout model:** Five buyer worries answered in order in a panel with the action, beside a
  reserved card artwork and the reserved amount.
- **Conversion device:** the section stops selling warmth and answers the five practical anxieties
  instead. Every answer is an operating commitment rather than a claim, so the panel is authorable
  in full — which is unusual for a conversion study in this sector, where most have had to work
  around a reserved figure.
- **What it avoids:** **no urgency device.** A gift section is exactly where *"order by Friday"*
  would normally sit, and that is an invented deadline.

### WELL-S17-005 — Art-directed / Distinctive

- **Layout model:** Two reserved card plates overlapping on a saturated berry ground, the back one
  turned three degrees, under an oversized line, with the reserved amount held small beneath.
- **The device:** this is **the only study in the WELL sector that rotates anything.** A gift card
  is a physical object that gets handed over, and a pair of them lying overlapped and slightly
  askew reads as objects on a table rather than as assets in a grid. The angle is small on purpose
  — the point is that they are real things, not that the page is tilted.
- **Responsive decision, recorded:** the rotation is removed below 768px. Two overlapping rotated
  plates at phone width either clip or force a horizontal scroll, and neither is worth the effect;
  the plates stack square with an offset, so the "two objects" reading survives without the tilt.
  The rotation is also removed under `prefers-reduced-motion`.

## Structural Diversity

| Study | Topology | Card areas | Amount treatment | Ground |
| --- | --- | --- | --- | --- |
| 001 | Two form cards + shared commitments | 2, equal | One per form | Pale lilac-grey |
| 002 | Object at half-width beside a proposition | 1, large | One, beside the action | Soft moss |
| 003 | Three numbered decision modules | 2, small | One, in module two | Pale peach-grey |
| 004 | Worry panel with the action beside the card | 1 | One, under the card | Deep plum |
| 005 | Two overlapping plates, one turned | 2, overlapping | One, small at the foot | Deep berry |

Grounds do not repeat any used in `WELL-S01`–`S16`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is how
  the card is treated as an object — equal pair, single artefact, small option swatches, supporting
  image, or overlapping physical things.
- **Document-metaphor justification:** `NONE`. No voucher, coupon, certificate or redemption-slip
  device is used — which matters here, because a gift card is the one element in this sector that
  could plausibly have been drawn as a coupon.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>`, no `<iframe>`,
  no inline `style` attribute in any file.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Card artwork ×2 | `001` — one per form | Still image or artwork, 8:5 | Empty tonal surface with a quiet label naming the form |
| Card artwork ×1 | `002` — at object scale, half the composition | Still image or artwork, 8:5 | As above; the proposition beside it stands alone |
| Card artwork ×2 | `003` — small option swatches inside module one | Still image or artwork, 8:5 | As above, at swatch scale |
| Card artwork ×1 | `004` — beside the worry panel | Still image or artwork, 8:5 | As above |
| Card artwork ×2 | `005` — overlapping, one rotated | Still image or artwork, 8:5 | As above; the overlap and tilt read with the fills alone |
| Gift amount ×6 | All five studies | **Text**, replaced by the real figure and its currency | Em dash with a visually hidden "Gift amount" label |
| Message | `003` — the buyer's own message | **Text**, reproduced as written | Sized, labelled region |

Verified by scan: six reserved amount slots across the batch, six labelled.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`, 44px-plus targets. Every reserved slot carries a visually hidden field
  label. `005`'s rotation is dropped under `prefers-reduced-motion` as well as at narrow widths.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above — including `005`'s
  explicit decision about when the tilt stops being worth its cost.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script, iframe
  or inline style.
- CSS-validity scan: **PASS.** No malformed hex or invalid custom property in any file. This check
  was added in `S16` after it caught a real defect there, and is now run on every batch.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s17-00N` root.
- **Amount, expiry and offer check: PASS.** Visible text only, comments and hidden field labels
  stripped, scanned for every currency symbol, *valid for*, *expires on/in*, months, years,
  *within N*, *next day*, *delivery*, *postage*, *p&p*, *most popular*, *best value*, *bonus*,
  *free X when*, *order by*, *limited*, *hurry*, percentages and any digit. **Zero matches in all
  five.** The only digits anywhere are `003`'s decorative `aria-hidden` step numbers.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `005`'s overlapping rotated plates read as two objects on a table with no clipping and
  no horizontal overflow. Ninth batch in eleven to need no render correction.

## Notes

- This is the seventeenth authored batch in the `WELL` sector and the fifteenth authored entirely
  without references.
- **The reusable outcome is the worry list.** For any section whose subject is a transaction on
  someone else's behalf — a gift, a referral, a booking made for a partner or a parent — the
  persuasive content is not the warmth, it is the small list of things that could make it
  embarrassing. Each of those is answerable with an operating commitment, which means it is
  authorable in a placeholder catalog where the warmth largely is not.
- `S17` completes the money group: `S11` for one treatment, `S12` for more than one, `S17` for
  someone else.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
