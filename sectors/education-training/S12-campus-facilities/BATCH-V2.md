# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S12` — Campus & Facilities · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three learning spaces whose campus line, name, purpose, location and access lines are bracketed placeholders, facilities declared awaiting confirmation, images reserved as the room only, no campus, hour or address named, the note that facilities and access arrangements vary, one route to the same-variant programme list; the media counts per study (3, 3, 3, 3, 3) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S12-001` | Universal / Safe | 001 Apricot | 1 — three equal spaces below an open introduction | loop behind the head | Split head with the lead and the graphite spaces chip; three cells in a bordered grid on ink seams with 3:2 fields of the room, bracketed campus chips, names, purposes, locations and the opened access row; the action and the note on the lead rule | 3 × 3:2 · 19 | 193 |
| `EDU-S12-002` | Premium / Editorial | 002 Mulberry | 2 — alternating features | rise above the head | Three feature rows alternating the 3:2 field and the lines side to side, the first on the lead rule; the action and the note on the closing hairline | 3 × 3:2 · 19 | 193 |
| `EDU-S12-003` | Structured / Visual Modular | 003 Cobalt | 3 — the introduction beside a joined mosaic | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; one bordered plate of three horizontal modules, each a 4:5 field beside the space lines | 3 × 4:5 · 19 | 193 |
| `EDU-S12-004` | Conversion-led | 004 Iris | 4 — the featured space above two compact summaries | outline round *Room to explore.* | V1's featured panel as a band with a 3:2 field beside its lines and the access row on the lead rule; the second and third as compact ruled rows with 1:1 fields; the action and the note on the closing hairline | 3:2 + 2 × 1:1 · 19 | 193 |
| `EDU-S12-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered gallery | margin bar along the display column | Display column with the lead, the action and the chip; three spaces staggered — flush, dropped, half-dropped — with 4:5 fields and the same lines; the note on the closing hairline | 3 × 4:5 · 19 | 193 |

## What changed from V1

V1's space cards, its arched and curved crops, the purple featured panel and the plus-marked disclosures go; each space is a bare 8px field labelled THE ROOM, its campus and type as an accent chip, its name in muted ink as a placeholder and its purpose, location and access lines on hairlines. CAMPUS SPACES · FACILITIES AWAITING CONFIRMATION is a graphite chip — the sector's `--no`. *Access & facilities* opens as a row with the document mark, so step-free access and adjustments read in every study. The only darkened surface is the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S12 -Fields 'Explore the spaces that shape|Facilities awaiting confirmation|Facility type|Learning space 1|Learning space 3|Purpose of this space|Location within the campus|Access|Equipment, opening hours|Step-free access|access arrangements vary|Explore programmes'` — ALL CHECKS PASS; parity 60/60. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; nineteen placeholders per study.
- Rendered and read at 1440. Correction: 004 supporting spaces set as compact rows with 1:1 fields so they read as summaries beneath the featured band.
