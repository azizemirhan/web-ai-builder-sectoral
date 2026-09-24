# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S09` — Patient Reviews · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — no review on the page, no quotation, no star, no rating, no named patient; the can/cannot lists and the four policies in every study; the closing line; the listing name as a placeholder demo value; the media counts per study (1, 1, 1, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S09-001` | Universal / Safe | 001 Chalk | 1 — the two lists side by side | ring behind the head | A REVIEW CAN TELL YOU as a ruled list with tick marks on the lead rule beside IT CANNOT TELL YOU with struck marks on the plum rule; the desk and waiting room as a 3:1 field; the four policies as a bordered row; foot | 1 × 3:1 · 1 | 202 |
| `DN-S09-002` | Premium / Editorial | 002 Linen | 2 — the sentence not in any of them | arc above the display line | *Whether the filling was placed well is not in any of them.* at display size; the desk and waiting room edge to edge at 21:9 captioned *The half a review can reach.*; two ruled lists; ruled row of four; foot on the lead rule | 1 × 21:9 · 1 | 220 |
| `DN-S09-003` | Structured / Visual Modular | 003 Slate | 3 — the grid keeps going, the cards do not | dot grid behind | Bordered grid of eight cells — four policy cards with marks over four card-shaped holes on the light rule carrying only a struck plum mark and what a review cannot tell you; the can-list as a ruled row on the lead rule; 3:1 field; foot | 1 × 3:1 · 1 | 232 |
| `DN-S09-004` | Conversion-led | 004 Daylight | 4 — one policy given the measure | bar under *chair* | *We do not ask at the chair.* as a band at display size with V1's extra sentence on the plum edge; the other three policies as a ruled row; two ruled lists; 3:1 field at the foot; foot on the lead rule | 1 × 3:1 · 1 | 220 |
| `DN-S09-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the whole argument as prose | corner marks framing the head | Running prose in one column at statement size, the can-sentences in the accent and the cannot-sentences in the plum; the four policies as a ruled column beside; foot on the lead rule. No field | none · 2 | 258 |

## What changed from V1

The refusal token carries every "cannot": the plum 3px rule under IT CANNOT TELL YOU, the plum struck circle in the holes, the plum edge beside the band, the plum sentence in the prose. No quotation mark, no star, no rating, no card that looks like a review card; the 003 holes are deliberately empty of anything a review would hold. Fields are bare and labelled; the only darkened surface is the 004 band. Copy is V1's throughout — 005 carries it as prose and repeats the four policies as a column, which is why its placeholder count is two.

## Verification

- `dncheck.ps1 -Sec S09 -Fields 'no reviews on this page|How long you waited|Whether the bill matched the plan|Whether the filling was placed well|needed at all|the public listing|We do not ask at the chair|The wrong ones stay up|under our own name|half you are paying for'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no link; no blockquote; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. No corrections needed.
