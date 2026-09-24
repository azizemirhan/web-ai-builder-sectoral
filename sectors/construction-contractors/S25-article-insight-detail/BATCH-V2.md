# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S25` — Article / Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — give something away or it is an advertisement; written because somebody asked, by somebody who runs something, with what we get stated; the body as reserved prose drawn as measures, never filler; title, writer, date, reading time and category reserved; no counts, no newsletter form, no stock photograph, one portrait at most; anchors in `004` only — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S25-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — apparatus cells around reserved prose | setting-out grid behind the head | WHY and WHO as two bordered iconed cells with the reserved writer; the piece as reserved prose — ruled measures in the media tone with paragraph breaks — beside a 1:1 reserved portrait and a bordered five-slot ledger; WHAT YOU CAN DO WITHOUT US as a tape-topped band of three iconed cells (drop / pen / document); WHAT WE GET and WHAT IT DOES NOT COVER as two bordered cells, the second red-topped | 1 portrait, prose, 6 slots | 483 |
| `CON-S25-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — head-note, text, apparatus | levelling circle behind the head | HEAD-NOTE chapter in the reading voice with the reserved writer inline; THE TEXT as reserved prose at a reading measure beside a sticky bordered ledger of five slots; the can-do list as a tape-topped ruled iconed list with the test sentence; closing note on what it leaves out | prose, 6 slots | 456 |
| `CON-S25-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — four gates | dimension line with ticks behind the head | Four bordered gate rows sharing hairlines — ordinal with an open padlock, the gate as a question, its answer beside — the third gate THE FATAL ONE with a closed padlock behind a deep-red edge and its can-do list as a bordered iconed list on the band tone; the piece as reserved prose beside a bordered five-slot ledger | prose, 6 slots | 505 |
| `CON-S25-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — the giveaway where the newsletter box goes | chevron run behind the can-do band | Display with tape underline; the can-do block as the largest thing — a hi-vis band with a bordered iconed three-cell row and the test sentence; WHAT WE GET as a bordered cell; the piece as reserved prose beside a bordered five-slot ledger; AND ONE SMALL ASK, AFTERWARDS as a tape-topped cell with the batch's only action, in-page | prose, 5 slots | 525 |
| `CON-S25-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the body at display scale, redrawn | cut-earth hatching down the left margin; dimension lines under each measure | The article as three measures at display scale — AN OPENING, A LONG MIDDLE, AND A SHORT CLOSE — each a block of ruled lines with a dimension line and label beneath; the apparatus as a bordered five-cell iconed row with the leaves-out cell red-edged on the band tone; bordered metadata ledger row | prose, 5 slots | 336 |

## What changed from V1

Reserved prose is drawn as the register's bare flat measures — ruled lines in the media tone at the width the text would occupy, with paragraph breaks and, at display scale, dimension lines — never filler and never a dash; the apparatus carries a stroke-icon set (speech line, badge, hard hat, phone, struck seal; drop, pen and document for the three things a reader can do); the metadata is a bordered slot ledger reading *Reserved*. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S25 -Fields 'Title of the piece|Name of the writer|Reading time'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit, count or stock photograph; the anchor in `004` only, in-page; no em-dash placeholder.
- Rendered and read at 1440. Corrections: `005` section label margin given the specificity to beat the text paragraph rule.
