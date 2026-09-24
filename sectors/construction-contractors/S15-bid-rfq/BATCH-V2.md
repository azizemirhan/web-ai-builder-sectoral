# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S15` — Bid / RFQ · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a price is a function of information; three kinds of number and only the third is one; every question says why it is asked and what it costs not to answer; the budget asked and not priced to; no calculator, figure, response time or win rate; the form only in `004`, native and computing nothing; bid contact, address and deadline reserved — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S15-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — outcome cells, question ledger | setting-out grid behind the head | Three bordered outcome cells under the tape with send icons (speech line / compass / document set) and the outcome at headline size, the price cell on the band tone; eight-row bordered question ledger with a stroke icon per question, WHY WE ASK and IF YOU CANNOT ANSWER on the band tone, the budget row tape-topped; WHERE TO SEND IT as a tape-topped band with the reserved fields at counter scale and what happens next beside; refusal note with a struck calculator and muted tags | 3 slots | 867 |
| `CON-S15-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — reading column, sticky margin ledger | levelling circle behind the head | Ruled chapters with iconed eyebrows; the three objects as a bordered row inside the essay; the survey rule as a tape-topped chapter on the band tone; the budget and walk chapters; a sticky margin with WHERE TO SEND IT (reserved fields at counter scale) and WHAT IS NOT ON THIS PAGE with tags | 3 slots | 743 |
| `CON-S15-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — three depth columns | dimension line with three ticks above the columns | Three bordered columns sharing hairlines, headed by a send icon and the outcome, with ruled iconed entries growing in number to the right and the gap to the next depth drawn as a STILL MISSING cell on the band tone with tags; the price column tape-topped on the band tone; bordered three-cell foot — budget, reserved send-to fields, refusal note | 3 slots | 633 |
| `CON-S15-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — bordered field ledger, hi-vis submit band | chevron run behind the submit band | Display with tape underline; the form as a bordered ledger of native controls (textarea, selects) with iconed labels and WHY WE ASK on the band tone beside each, closing in a hi-vis band with one bordered submit and the no-number line; sticky margin of three bordered outcome cells and OR SEND IT THE OTHER WAY with the reserved fields; ruled refusal foot with a struck calculator | 3 slots | 673 |
| `CON-S15-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the three words at display scale | cut-earth hatching down the left margin | GUESS struck through in the accent, RANGE, and PRICE in the accent under the tape, each a ruled chapter with its send icon and bordered REQUIRES / GET / WORTH cells; six-row bordered question ledger with icons and the cost on the band tone; tape-edged budget band; reserved send-to slots at counter scale; ruled refusal foot | 3 slots | 806 |

## What changed from V1

The three kinds of number are always the tape-marked object — cell, row, column, margin cell or display word by variant — with a send-icon set (speech line, compass, document set); the questions carry a stroke icon each (brick, pin, house, layers, search, calendar, badge, balance) on bordered rows with the cost of not answering on the band tone; the reserved send-to fields are bordered slots at counter scale; the refusal carries a struck calculator. `004`'s controls are the register's 1px bordered rectangles at radius 0. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S15 -Fields 'Name of the bid contact|Submission address|Deadline for questions' -AllowForm` — ALL CHECKS PASS; parity 15/15. The form is in `004` only, native controls, no script, no computed output. No `<h1>`; no header/nav/footer; no remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit, price, rate, range figure, turnaround, win rate or count in copy.
- Rendered and read at 1440. Corrections: `005` display-word rule given the specificity to beat the chapter paragraph rule; budget heading aligned to the top of its band.
