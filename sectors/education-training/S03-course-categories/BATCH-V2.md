# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S03` — Course Categories · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — six subject areas whose names and scope lines are bracketed placeholders, the structure declared an example to be confirmed, one route to the same-variant programme list, the note that a subject area is a starting point; the media counts per study (0, 2, 6, 0, 2) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S03-001` | Universal / Safe | 001 Apricot | 1 — the subject list beside a concise introduction | loop behind the intro head | Narrow intro column with the lead, the graphite EXAMPLE CATEGORY STRUCTURE chip, the action on the lead rule and the note; six subject areas as a bordered two-column grid on ink seams with word-numeral chips | none · 13 | 152 |
| `EDU-S03-002` | Premium / Editorial | 002 Mulberry | 2 — the ruled list beside a staggered pair | rise above the head | Split head with the lead and the chip; six ruled subject lines with word-numeral keys beside a 4:5 and a 1:1 field staggered; the action and the note on the lead rule | 4:5 + 1:1 · 13 | 169 |
| `EDU-S03-003` | Structured / Visual Modular | 003 Cobalt | 3 — six field-led subjects in a compact mosaic | cross grid behind | Split head with the lead, the action and the chip; six cells in a bordered grid of three, each a 3:2 field of a learning space, chip, bracketed name, line and scope; the note on the lead rule | 6 × 3:2 · 13 | 204 |
| `EDU-S03-004` | Conversion-led | 004 Iris | 4 — the decision-led list with the begin panel as a band | outline round *interests you.* | Split head; six subject areas as ruled rows across four columns; V1's *Not sure where to begin?* as a band on the band tone split by the lead rule, holding the note, the action and the chip | none · 13 | 157 |
| `EDU-S03-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered pair beside the display column | margin bar along the display column | The display column with the lead, the action and the chip; a 3:2 field flush and a 1:1 field dropped; six subject areas as two ruled columns; the note | 3:2 + 1:1 · 13 | 169 |

## What changed from V1

V1's tinted subject cards, its icon tiles, the curved image pair and the filled purple exploration panel go; each subject area is a word-numeral chip, its name in muted ink as a placeholder and its scope as a muted placeholder line on a hairline. EXAMPLE CATEGORY STRUCTURE · CATEGORIES TO BE CONFIRMED is a graphite chip — the sector's `--no` — kept beside the action in every study. The only darkened surface is the 004 band. Copy is V1's throughout; the 004 band carries V1's note in place of a new line.

## Verification

- `educheck.ps1 -Sec S03 -Fields 'Start with a subject area|Categories to be confirmed|Creative subjects|Specialist subjects|Confirmed scope|Browse all programmes|starting point'` — ALL CHECKS PASS; parity 35/35. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; thirteen placeholders per study.
- Rendered and read at 1440. No corrections needed after the 004 band was set to carry V1's note.
