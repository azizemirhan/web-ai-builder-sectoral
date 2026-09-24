# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S10`
- Section Name: `Patient Testimonials`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S10-001` | Universal / Safe | 001 Linen & Sage | **C** | **Three reserved quotation structures as cards in a row** — mark, empty body, empty attribution; the three things asked as a ruled row; not-read foot | 0 | 156 |
| `HC-S10-002` | Premium / Editorial | 002 Porcelain & Plum | B | **One large reserved quotation with two smaller beneath**, and **a tall frame of two chairs in the consulting room**; the three things asked as a ruled serif row | 1 | 167 |
| `HC-S10-003` | Structured / Visual Modular | 003 Sky & Slate | **C** | The three things asked as check-square modules; **a ledger of three reserved rows, each with the same three fields — *said*, *described as*, *printed since*** | 0 | 178 |
| `HC-S10-004` | Conversion-led | 004 Sand & Terracotta | B | Three reserved quotation cards; **a terracotta panel inviting a visitor who was seen here to add their words, with the three rules as its terms**, over a frame of the desk | 1 | 169 |
| `HC-S10-005` | Art-directed / Distinctive | 005 Night & Mint | B | Dark ground; **one enormous reserved quotation — a display-size mint mark and an empty stage**; two smaller slots and **the waiting room, late afternoon** | 1 | 160 |

Row `C B C B B`. Page one takes its `C` after `B B B B` across `S06`–`S09`; page three takes a
second `C` after `A C B`. No page has two consecutive `A`.

## The Governing Idea

> **Nothing here is written by us. Until a visitor says yes, the space stays empty.**

The contract is explicit: *a testimonial role is a quotation structure with no attributed name*,
and a fabricated testimonial is prohibited. An honest one cannot be authored in advance. So the
batch authors the **structure** — quotation slots with the marks, the body and the attribution
all reserved — and the **rules**, the three things asked before anything is printed:

1. **It is from a real visit here.** Not a form, not a survey, not a review site.
2. **It is in the person's own words.** Cut only for length, never for tone.
3. **They said yes, and can say no later.** Then it comes down, the same day.

**What you will not read here:** a star rating, a number of reviews, or a quotation we could not
show you the origin of. **Read them knowing:** one person's visit is not a prediction of yours.

`004`'s one action is aimed at someone already seen — *tell the desk; it goes up only with your
yes* — and links to `#` until `S19` is authored. No other study carries an action: a testimonial
section does not sell.

## Density

Standard band throughout except `003`, declared structured because its ledger carries three
fields per row; reserved labels count as words, and were shortened in second and third slots so
the band held without dropping a rule.

## Media

Three reserved image areas, all empty rooms — two chairs in the consulting room (`002`), the desk
(`004`), the waiting room late afternoon (`005`) — where the words would have been said, never
the person who said them. Every study also carries reserved *text* areas: the quotation slots,
which are not media and are counted separately.

## Verification Record

- Word bands: **156 / 167 / 178 / 169 / 160** (standard except `003` structured).
- Content parity: **14 shared fields across five studies, 70/70 slots present.**
- Reserved image areas: **0 / 1 / 0 / 1 / 1.** Reserved quotation slots: 3 / 3 / 3 / 3 / 3.
- Claims scan clean; no quotation text, name, initial, date, star, rating, review count,
  clinician name, price, telephone, hour or digit.
- Dependencies none. Attribution lines are `<p class="cite">`, not `<footer>`, which the checker
  treats as a page-shell element. Tag balance, namespace, frame, reduced-motion, `<h2>`
  labelling, no solid-border-plus-max-width: all pass.
- Rendered and read at 1440 and 390. Correction made: `002` rules moved out of the right column
  into a full-width ruled row, and the quotation slots deepened, so the left column meets the
  frame's height.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
