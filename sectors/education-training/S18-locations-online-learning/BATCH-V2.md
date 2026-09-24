# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S18` — Locations & Online Learning · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — two study modes whose campus name, online option, descriptions, four facts and two disclosure lines are bracketed placeholders, locations and delivery options declared awaiting confirmation, one reserved image of the campus environment, no map embed, the note that available modes vary, one route to the same-variant programme list; the media counts per study (1, 1, 1, 1, 1) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S18-001` | Universal / Safe | 001 Apricot | 1 — the paired options below an open introduction | loop behind the head | Split head with the lead and the graphite confirmation chip; the two modes as paired cells in a bordered grid, the campus cell with a 3:2 field; each with its chip, bracketed name and description, two labelled facts with marks and the opened disclosure row; the action and the note on the lead rule | 3:2 · 11 | 137 |
| `EDU-S18-002` | Premium / Editorial | 002 Mulberry | 2 — the campus feature above the online band | rise above the head | The campus mode as a wide row on the lead rule with a 3:2 field beside its lines; the online mode as a band on the band tone with its facts in columns; the action and the note on the closing hairline | 3:2 · 11 | 137 |
| `EDU-S18-003` | Structured / Visual Modular | 003 Cobalt | 3 — the side introduction beside connected modes | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; one bordered plate with the campus module — a 4:5 field beside its lines — over the online module | 4:5 · 11 | 137 |
| `EDU-S18-004` | Conversion-led | 004 Iris | 4 — the campus beside a prominent online panel | outline round *Choose how to learn.* | The campus mode with a 3:2 field over its lines beside the online mode as a band stretched to match, its participation row on the lead rule; the action and the note on the closing hairline | 3:2 · 11 | 137 |
| `EDU-S18-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the asymmetric field and the online rows | margin bar along the display column | Display column with the lead, the action and the chip, a 3:2 field dropped beneath; the two modes as ruled blocks in the wide column, the online block where V1 set its lime field; the note on the closing hairline | 3:2 · 11 | 137 |

## What changed from V1

V1's mode cards, the curved campus photograph, the lime and purple online panels and the plus-marked disclosures go; each mode is its chip in the accent, the bracketed name in muted ink, the description, two facts as tracked labels with the place, calendar, clock and screen marks on hairlines, and the disclosure opened as a row with the document mark. The campus image is a bare 8px field labelled THE ENTRANCE; no map is drawn. LOCATIONS AND DELIVERY OPTIONS AWAITING CONFIRMATION is a graphite chip — the sector's `--no`. The darkened surfaces are the 002 and 004 online bands. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S18 -Fields 'Explore where and how learning can happen|delivery options awaiting confirmation|On campus|Campus name|Learning environment and programmes|Location|City, address and building|Attendance|Required days, hours|Visiting|Transport, step-free access|Online learning|Online study option|Programmes available remotely|Session format|Live or self-paced|Joining setup|Platform, device|Participation|Platform accessibility, recordings|Available modes vary|Explore programmes'` — ALL CHECKS PASS; parity 110/110. No `<h1>`; no header/nav/footer; no form; no `<details>`; no map embed; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; eleven placeholders per study.
- Rendered and read at 1440. Correction: 004 campus field set to 3:2 and the online band stretched so the pair closes level.
