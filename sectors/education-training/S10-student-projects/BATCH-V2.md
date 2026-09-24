# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S10` — Student Projects · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three projects whose programme line, title, description, credit and process lines are bracketed placeholders, work and credits declared awaiting confirmation, images reserved as the work only, no student or team named, the note that projects reflect individual work within a programme, one route to the same-variant programme list; the media counts per study (3, 3, 3, 3, 3) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions carry the S05 devices — the same item grammar with the work in place of the portrait.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S10-001` | Universal / Safe | 001 Apricot | 1 — three equal projects below an open introduction | loop behind the head | Split head with the lead and the graphite showcase chip; three cells in a bordered grid on ink seams with 3:2 fields of the work, bracketed programme chips, titles, descriptions, credit lines and the opened process row; the action and the note on the lead rule | 3 × 3:2 · 19 | 195 |
| `EDU-S10-002` | Premium / Editorial | 002 Mulberry | 2 — one featured project, then two compact | rise above the head | The first project as a wide row on the lead rule with a 3:4 field beside its lines; the second and third as ruled columns with 1:1 fields; the action and the note on the closing hairline | 3:4 + 2 × 1:1 · 19 | 195 |
| `EDU-S10-003` | Structured / Visual Modular | 003 Cobalt | 3 — the intro column beside three joined modules | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; one bordered plate of three horizontal modules, each a 4:5 field beside the project lines | 3 × 4:5 · 19 | 195 |
| `EDU-S10-004` | Conversion-led | 004 Iris | 4 — open columns with the process made prominent | outline round *Learning, made visible.* | Split head; three ruled project columns with 4:5 fields; the process row set on the band tone in each, as V1 coloured its control; the action and the note on the lead rule | 3 × 4:5 · 19 | 195 |
| `EDU-S10-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered gallery | margin bar along the display column | Display column with the lead, the action and the chip; three projects staggered — flush, dropped, half-dropped — with 4:5 fields and the same lines; the note on the closing hairline | 3 × 4:5 · 19 | 195 |

## What changed from V1

V1's project cards, its varied rounded crops, the coloured process control and the plus-marked disclosures go; each project is a bare 8px field labelled THE WORK, its programme and type as an accent chip, its title in muted ink as a placeholder and its description, credit and process lines on hairlines. PROJECT SHOWCASE · WORK AND CREDITS AWAITING CONFIRMATION is a graphite chip — the sector's `--no`. *Explore the process* opens as a row with the document mark; 004 sets it on the band tone. Copy is V1's throughout; no student, team or project is introduced.

## Verification

- `educheck.ps1 -Sec S10 -Fields 'Explore how students approach a brief|Work and credits awaiting confirmation|Project title 1|Project title 3|Project type|question explored|Student or team|Explore the process|Project brief, methods|Learning reflection|Projects reflect individual work|Explore programmes'` — ALL CHECKS PASS; parity 60/60. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; nineteen placeholders per study.
- Rendered and read at 1440. No corrections needed.
