# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S07` — Admissions & Enrolment · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three admission steps of which the second and third are bracketed placeholders, the guide declared illustrative with programme details to be confirmed, dates and fees held as placeholders under *Before you begin*, no form or application device, the note that requirements and timelines vary, one route to the same-variant programme list; the media counts per study (0, 1, 0, 0, 1) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S07-001` | Universal / Safe | 001 Apricot | 1 — three open steps above the preparation band | loop behind the head | Split head with the lead and the graphite guide chip; three step cells in a bordered grid on ink seams with word-numeral chips; *Before you begin* as a band with dates and fees opened as rows with the calendar and information marks; the action and the note on the lead rule | none · 5 | 119 |
| `EDU-S07-002` | Premium / Editorial | 002 Mulberry | 2 — the introduction with a field and the preparation column | rise above the head | Head, lead, chip and a 3:2 field of the entrance left; three ruled step rows, the preparation rows and the action and note on the lead rule right | 3:2 · 5 | 127 |
| `EDU-S07-003` | Structured / Visual Modular | 003 Cobalt | 3 — large step labels with compact information | cross grid behind | Split head; three step columns in a bordered plate with the word-numeral at display size in the accent; *Before you begin* as the plate's foot on the band tone; the action and the note on the lead rule | none · 5 | 119 |
| `EDU-S07-004` | Conversion-led | 004 Iris | 4 — the selection callout beside the preparation sequence | outline round *with a choice.* | Split head; V1's callout as a band holding the chip and the action on the lead rule, in V1's order before the steps; three ruled step rows, the preparation rows and the note beside it | none · 5 | 119 |
| `EDU-S07-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the offset sequence | margin bar along the display column | Display column with the lead, the action and the chip, a 4:3 field dropped beneath; three ruled step rows, the preparation rows and the note in the wide column | 4:3 · 5 | 127 |

## What changed from V1

V1's numbered step cards, the warm and purple panels, the curved photograph and the plus-marked disclosure controls go; each step is a word-numeral chip (or, in 003, the word-numeral at display size where V1 set its large labels), the title as type and V1's line or bracketed placeholder in muted ink. ILLUSTRATIVE ADMISSIONS GUIDE · PROGRAMME DETAILS TO BE CONFIRMED is a graphite chip — the sector's `--no`. Dates and fees open as rows with the calendar and information marks. The darkened surfaces are the 001 band, the 003 plate foot and the 004 callout band. Copy is V1's throughout; no requirement, date, fee or form is introduced.

## Verification

- `educheck.ps1 -Sec S07 -Fields 'Find a programme that fits|Illustrative admissions guide|Find your programme|Check what is needed|Follow the application route|Before you begin|Application window|Full fees, payment terms|Requirements and timelines vary'` — ALL CHECKS PASS; parity 45/45. No `<h1>`; no header/nav/footer; no form, button or input; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; five placeholders per study.
- Rendered and read at 1440. Correction: 005 field set to 4:3 so it closes level with the wide column.
