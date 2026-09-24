# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S06`
- Section Name: `Why Choose Clinic`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S06-001` | Universal / Safe | 001 Linen & Sage | **A** | Five reason cards, three and two, **each with a frame of where the reason can be checked**; the reason bold, the check beneath; not-claimed foot | 5 | 229 |
| `HC-S06-002` | Premium / Editorial | 002 Porcelain & Plum | B | Ruled head; **a tall frame of the doctor writing at the desk** on the left, the five reasons as a ruled serif column on the right | 1 | 209 |
| `HC-S06-003` | Structured / Visual Modular | 003 Sky & Slate | B | Head beside **the examination room**; then **a ledger of five rows with the same two fields — *we do* / *you check*** | 1 | 220 |
| `HC-S06-004` | Conversion-led | 004 Sand & Terracotta | **C** | **The five reasons as a checklist to take to the first visit**; a terracotta panel with one action — *come and check* — linking to the booking study | 0 | 230 |
| `HC-S06-005` | Art-directed / Distinctive | 005 Night & Mint | B | Dark ground; **a wide short strip of the nurse in the treatment room**, then **the five reasons as five numbered columns in one row** | 1 | 209 |

Row `A B B C B`. Page one takes its first `A` since `S03` (it carried `B B` across `S04`–`S05`).
Page four takes a `C` (it carried `C B` across `S04`–`S05` — two `C`s in three sections, which
page four can afford after `B B B` across `S01`–`S03`). No page has two consecutive `A`.

## The Governing Idea

> **Reasons you can check on the first visit, not reasons we would like you to believe.**

The sector's "why choose us" is a wall of badges, a row of statistics and a list of adjectives —
*compassionate, patient-centred, state-of-the-art* — none of which a visitor can verify. This
batch lists **five practices, each ending in a check** the visitor can perform on the day:

1. *You are told who you will see before you book* — check: ask when you book.
2. *The first visit is an examination and a conversation* — check: you leave with a plan, not a
   bill for treatment.
3. *What was found goes to you in writing* — check: it is in your hand before you leave.
4. *A scan or a test only if it changes what we do* — check: ask what the result would change.
5. *If this is not the place, you are told, and referred* — check: ask on the day.

**What is not on this page** is said, not just omitted: *a figure, a rating, an award, or the
word best — you could not check any of them.* The registrations live elsewhere, by link (`#`
until `S11` is authored).

`004` turns the section's action from *choose us* into *come and check*, and is the first study
in the sector to link to an authored destination: `../../S05-appointment-booking/raw/HC-S05-004.html`.
The `S01`–`S04` actions still point to `#`; they were authored before `S05` existed and are not
retouched in this batch.

## Density

All five are declared **structured, 170–230**, and the batch records why: five reasons, each
carrying its own check, is a list-shaped role. Cutting the checks to reach the standard band would
remove the thing that makes the section honest. First drafts ran 220–247; trimmed to 209–230 by
shortening explanations, never by dropping a check.

## Media

Nine reserved areas across four studies: `001` carries five (reception at the desk, the
examination room, the doctor writing, the scanner room, the doctor on the phone — each the place
where its reason can be seen); `002` the writing desk alone, because the letter is what makes the
other four verifiable; `003` the examination room; `005` the nurse taking a reading. `004` is type
because a checklist is the composition and page four can hold it.

## Verification Record

- Word band structured `170–230`: **229 / 209 / 220 / 230 / 209.**
- Content parity: **15 shared fields across five studies, 75/75 slots present.**
- Reserved areas: **5 / 1 / 1 / 0 / 1.**
- Claims scan clean; no badge, statistic, testimonial, award, credential, clinician name, price,
  telephone, hour or digit. The word *best* appears only inside the sentence that refuses it.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width: all pass.
- Rendered and read at 1440 and 390. Correction made: `001` second-row frames set to 21:9 at
  desktop (16:10 at half width stood taller than the row above).
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
