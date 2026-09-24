# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S05` — Instructors & Faculty · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three instructors whose subject, name, role, introduction, teaching background and programmes are bracketed placeholders, the profiles declared to be confirmed, portraits reserved and labelled by role only, the note that teaching teams vary by programme, one route to the same-variant programme list; the media counts per study (3, 3, 3, 3, 3) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S05-001` | Universal / Safe | 001 Apricot | 1 — three equal profiles below an open introduction | loop behind the head | Split head with the lead and the graphite profiles chip; three cells in a bordered grid on ink seams with 4:5 portrait fields, subject chips, bracketed names, roles, introductions, the opened teaching-background row and the programmes line; the action and the note on the lead rule | 3 × 4:5 · 19 | 164 |
| `EDU-S05-002` | Premium / Editorial | 002 Mulberry | 2 — one featured profile, then two compact | rise above the head | The first profile as a wide row on the lead rule with a 3:4 field beside its lines; the second and third as ruled columns with 1:1 fields; the action and the note on the closing hairline | 3:4 + 2 × 1:1 · 19 | 164 |
| `EDU-S05-003` | Structured / Visual Modular | 003 Cobalt | 3 — the intro column beside three joined modules | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; one bordered plate of three horizontal modules, each a 4:5 field beside the profile lines | 3 × 4:5 · 19 | 164 |
| `EDU-S05-004` | Conversion-led | 004 Iris | 4 — open columns with the background made prominent | outline round *behind the learning.* | Split head; three ruled profile columns with 4:5 fields; the teaching-background row set on the band tone in each; the action and the note on the lead rule | 3 × 4:5 · 19 | 164 |
| `EDU-S05-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered gallery | margin bar along the display column | Display column with the lead, the action and the chip; three profiles staggered — flush, dropped, half-dropped — with 4:5 fields and the same lines; the note on the closing hairline | 3 × 4:5 · 19 | 164 |

## What changed from V1

V1's portrait cards, its circular and curved crops, the tinted background panels and the plus-marked disclosure controls go; each profile is a bare 8px portrait field labelled THE INSTRUCTOR, its subject an accent chip, its name in muted ink as a placeholder and its lines on hairlines. FACULTY PROFILES · DETAILS TO BE CONFIRMED is a graphite chip — the sector's `--no`. The teaching background opens as a row with the document mark in every study; 004 sets it on the band tone as V1 made the control prominent. Copy is V1's throughout; no name, qualification or pronoun is introduced.

## Verification

- `educheck.ps1 -Sec S05 -Fields 'Explore who teaches|Details to be confirmed|Instructor name 1|Instructor name 3|Teaching role|Teaching background|Verified experience|Associated programmes|Explore programmes|Teaching teams can vary'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; nineteen placeholders per study.
- Rendered and read at 1440. Correction: 002 featured row given its own text column and a 3:4 field so the lines sit beside the portrait rather than stretching to it.
