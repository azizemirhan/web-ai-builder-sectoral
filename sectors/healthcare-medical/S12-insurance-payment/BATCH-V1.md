# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S12`
- Section Name: `Insurance Payment`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S12-001` | Universal / Safe | 001 Linen & Sage | B | Three cards for the three ways to pay, each with *you need* and *what happens* and a reserved pill; **a frame of the desk, the fee being written on the letter**, beside the never-charged list | 1 | 225 |
| `HC-S12-002` | Premium / Editorial | 002 Porcelain & Plum | **C** | The three ways as ruled serif columns; **the never-charged list set large across the width** | 0 | 211 |
| `HC-S12-003` | Structured / Visual Modular | 003 Sky & Slate | **C** | **A ledger of three routes with the same three fields — *you need*, *what happens*, *reserved***; the never-charged list and the cannot-pay line as two modules | 0 | 211 |
| `HC-S12-004` | Conversion-led | 004 Sand & Terracotta | B | **A terracotta panel — *ask the fee; you will get it in writing* — with the never-charged list inside it**, over a frame of the desk with the card reader; the three ways as a column | 1 | 227 |
| `HC-S12-005` | Art-directed / Distinctive | 005 Night & Mint | B | Dark ground; **the promise at display size in mint**; **a wide frame of the letter with the fee line blank** beside the never-charged list; three ways as columns | 1 | 227 |

Row `B C C B B`. Page two is owed a `C` after `B B B` across `S09`–`S11`; page three takes a
second `C` in a row (`C B C C` across `S09`–`S12`) and its next section returns to a frame. No
page has two consecutive `A`.

## The Governing Idea

> **The price of the first visit is told to you before you book, in writing, and nothing is
> added on the day without your yes.**

The sector's payment section is an insurer logo strip and the words *competitive fees*; in this
sector an invented price, insurer, plan or coverage statement is prohibited. A real visitor wants
one thing: to know what it will cost before they commit, and that it will not grow in the room.
This batch says how the fee is told, and the **three ways it can be paid for** — *yourself*,
*through an insurer*, *through a referral* — each with what you need and what happens. In every
study:

- **Never charged for:** being told this is not the place for it; a referral letter; asking a
  question, before or after.
- **If you cannot pay:** say so at the desk. There is a conversation to be had, not a form.

Every action links to the same-variant booking study.

## Reserved Fields

No fee, currency, insurer, plan or coverage is named. Each route carries a reserved field marked
`data-placeholder="true"` — *first-visit fee*, *the insurers we work with*, *referral
arrangements* — visibly empty. `005`'s frame is the letter with the fee line blank, for the same
reason. Fill before real use.

## Density

All five are declared **structured, 170–230**: three routes with two fields each, plus the
never-charged list and the cannot-pay line, is a list-shaped role. 211–227; `004` was trimmed
from 244 by shortening the panel line and the caption, not by dropping a field.

## Media

Three reserved areas: the desk with the fee being written on the letter (`001`); the desk with
the card reader, the letter and the receipt pad — equipment the text names (`004`); the letter
on the desk with the fee line blank (`005`). `002` and `003` are type by intent.

## Verification Record

- Word band structured `170–230`: **225 / 211 / 211 / 227 / 227.**
- Content parity: **20 shared fields across five studies, 100/100 slots present.**
- Reserved areas: **1 / 0 / 0 / 1 / 1.** Reserved fields: 3 per study.
- Claims scan clean; no price, fee, insurer, plan, coverage, currency, clinician name, outcome,
  figure, telephone, hour or digit.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width, relative hrefs only: all pass.
- Rendered and read at 1440 and 390; no layout corrections required.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
