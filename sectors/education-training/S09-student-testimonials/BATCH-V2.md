# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S09` — Student Testimonials · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three reflections whose text, student name, programme line and story context are bracketed placeholders, the testimonials declared awaiting confirmation, V1's three themes kept as the only authored headings, portraits reserved and labelled by role only, no rating, star or outcome device, the note that each story reflects an individual experience, one route to the same-variant programme list; the media counts per study (3, 3, 3, 3, 3) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S09-001` | Universal / Safe | 001 Apricot | 1 — three equal stories below an open introduction | loop behind the head | Split head with the lead and the graphite stories chip; three cells in a bordered grid on ink seams with compact 1:1 portrait fields, V1's theme, the reflection at statement size, name and programme line and the opened story-context row; the action and the note on the lead rule | 3 × 1:1 · 13 | 164 |
| `EDU-S09-002` | Premium / Editorial | 002 Mulberry | 2 — one featured story above two supporting voices | rise above the head | The first story as a wide row on the lead rule with a 4:5 field and the reflection at display size; the second and third as ruled columns with compact 1:1 fields; the action and the note on the closing hairline | 4:5 + 2 × 1:1 · 13 | 165 |
| `EDU-S09-003` | Structured / Visual Modular | 003 Cobalt | 3 — the intro column beside three joined stories | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; one bordered plate of three horizontal modules, each a 1:1 field beside the story lines | 3 × 1:1 · 13 | 161 |
| `EDU-S09-004` | Conversion-led | 004 Iris | 4 — the featured story beside two open perspectives | outline round *through their eyes.* | Split head; V1's featured quotation as a band stretched to the side column, its story-context row on the lead rule; the second and third as ruled rows beside it; the action and the note on the closing hairline | 3 × 1:1 · 13 | 164 |
| `EDU-S09-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered stories | margin bar along the display column | Display column with the lead, the action and the chip; three stories staggered — flush, dropped, half-dropped — with 4:5 fields and the same lines; the note on the closing hairline | 3 × 4:5 · 13 | 167 |

## What changed from V1

V1's quotation cards, its circular portrait crops, the quotation-mark ornaments, the purple quotation panel and the plus-marked disclosure controls go; each story is a bare 8px portrait field labelled THE STUDENT, V1's theme as a tracked accent heading, the bracketed reflection in muted ink at statement size, the name and programme line as placeholders and the story context opened as a row with the document mark. STUDENT STORIES · TESTIMONIALS AWAITING CONFIRMATION is a graphite chip — the sector's `--no`. The only darkened surface is the 004 band. Copy is V1's throughout; no student, quote, rating or outcome is introduced.

## Verification

- `educheck.ps1 -Sec S09 -Fields 'A personal perspective can help|Testimonials awaiting confirmation|Choosing a programme|The learning experience|Making time to learn|Student name 1|Student name 3|Story context|learning context and date|Each story reflects|Explore programmes'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term — no star, rating or outcome device; thirteen placeholders per study.
- Rendered and read at 1440. Correction: 004 band stretched to the side column with its lines spaced between.
