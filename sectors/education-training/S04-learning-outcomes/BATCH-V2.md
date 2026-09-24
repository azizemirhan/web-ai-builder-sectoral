# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S04` — Learning Outcomes · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — four outcome verbs whose lines are bracketed placeholders, the programme name bracketed and the structure declared an example, the assessment disclosure as a placeholder, the note that outcomes vary by programme, one route to the same-variant programme list; the media counts per study (1, 1, 0, 0, 1) — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S04-001` | Universal / Safe | 001 Apricot | 1 — the split with the field under the head | loop behind the head | Head, intro, graphite programme chip and 3:2 field left; four ruled outcome rows with word-numeral chips, the opened assessment row with the document mark, the action and the note on the lead rule right | 3:2 · 6 | 121 |
| `EDU-S04-002` | Premium / Editorial | 002 Mulberry | 2 — outcome pairs around a tall field | rise above the head | Split head; Understand and Apply as ruled rows left, a 3:4 field centre, Communicate and Reflect right, rows stretched to the field's height; the assessment row, the action and the note on the lead rule | 3:4 · 6 | 121 |
| `EDU-S04-003` | Structured / Visual Modular | 003 Cobalt | 3 — the verbs as a typographic sequence | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; the four verbs at display size in the accent as a bordered plate of rows; the assessment row as the plate's foot on the band tone | none · 6 | 113 |
| `EDU-S04-004` | Conversion-led | 004 Iris | 4 — the statement with the capability stack | outline round *what comes next.* | Split head; V1's assessment, note and action in V1's order as a band split by the lead rule; four ruled outcome columns beneath | none · 6 | 113 |
| `EDU-S04-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the asymmetric split | margin bar along the display column | Display column with the intro, the action and the chip; a 4:3 field dropped beside; four outcomes as two ruled columns; the assessment row on the closing hairline; the note | 4:3 · 6 | 121 |

## What changed from V1

V1's numbered outcome cards, the curved and arched photograph shapes and the darkened summary panel go; each outcome is a word-numeral chip, the verb as type and the bracketed line in muted ink on a hairline. The programme line is a graphite chip — the sector's `--no`. The assessment disclosure is an opened row with the document mark in every study. The darkened surfaces are the 003 plate foot and the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S04 -Fields 'Look beyond the subject title|Example outcome structure|Understand|Reflect|How learning is demonstrated|Confirmed assessment task|Explore programmes|vary by programme'` — ALL CHECKS PASS; parity 40/40. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; six placeholders per study.
- Rendered and read at 1440. Corrections: 002 field narrowed to 3:4 with the outcome rows stretched to its height; 003 verb and line stacked so *Communicate* clears its outcome.
