# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S24` — Project / Case Study Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the anonymised cohort case kept whole: context line, bracketed title, intro, three labelled facts, the starting point, two documented stages with bracketed narratives, the note that a single project is context and not a prediction of individual results, one route to the same-variant S02; three reserved images of the work, the process and the delivered detail in every study, never a person — are kept exactly. The bracketed case title is set as the `<h1>` this detail page owns.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S24-001` | Universal / Safe | 001 Apricot | 1 — the case introduction beside the work, then paired stages | loop behind the head | Split head with the intro and a 3:2 field of the completed work; the three facts on a hairline row; the starting point; the two stages as paired columns with 4:3 fields, word-numeral chips and bracketed narratives; the closing with the note and the action on the lead rule | 3:2 + 2 × 4:3 · 7 | 185 |
| `EDU-S24-002` | Premium / Editorial | 002 Mulberry | 2 — the panorama with an open narrative and a two-image sequence | rise above the title | Split head; a shallow 3:1 field of the completed work; the facts beside the starting point on the lead rule; the two stages as ruled rows with 4:3 fields; the closing on the closing hairline | 3:1 + 2 × 4:3 · 7 | 185 |
| `EDU-S24-003` | Structured / Visual Modular | 003 Cobalt | 3 — the context module with a staggered evidence grid | cross grid behind | A bordered plate with the facts as a cell on the band tone, where V1 set its blue module, beside the 3:2 field and the starting point; the two stages staggered with 3:2 and 4:3 fields; the closing on the lead rule | 2 × 3:2 + 4:3 · 7 | 185 |
| `EDU-S24-004` | Conversion-led | 004 Iris | 4 — the narrative with an integrated exploration panel | outline round the case title | The reading column — 3:2 field, facts, starting point, two stage rows with 4:3 fields — beside V1's closing as a band on the band tone with the action on the lead rule | 3:2 + 2 × 4:3 · 7 | 185 |
| `EDU-S24-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the oversized introduction with asymmetrical evidence | margin bar along the display column | Display column with the title at the largest size, the intro and the facts, a 4:5 field dropped beside; the starting point; the two stages staggered with 3:2 and 4:3 fields; the closing as a band where V1 set its lime reflection | 4:5 + 3:2 + 4:3 · 7 | 185 |

## What changed from V1

V1's rounded image frames, the blue context module, the purple exploration panel and the lime reflection go; the case is bare type on hairlines or ink seams with three bare 8px fields labelled THE WORK and THE WORKSHOP — the context line as a tracked eyebrow with the camera mark, the bracketed title as the h1 in muted ink, the facts as tracked labels with the layers, calendar and people marks, the stages as word-numeral chips with V1's stage labels, the closing as a statement with its note and the 1px action. The darkened surfaces are the 003 facts cell, the 004 panel and the 005 closing band. Copy is V1's throughout; no cohort, student or outcome is named.

## Verification

- `educheck.ps1 -Sec S24 -Fields 'Student work|anonymised cohort case|Project or cohort case title|Follow one learning project|Learning context|Programme, discipline|Cohort|Anonymised group|Contributors|Consented roles|The starting point|Describe the original brief|develop|The decisions along the way|Explain the approach|reflect|What the work shows|Describe the delivered artefact|Explore the learning behind it|not a prediction of individual results|Explore programmes'` — ALL CHECKS PASS; parity 105/105. One `<h1>` per study (a detail page); no header/nav/footer; no form; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; seven placeholders per study.
- Rendered and read at 1440. Correction: 003 and 005 stage fields set to 3:2 and 4:3 so the stagger stays shallow.
