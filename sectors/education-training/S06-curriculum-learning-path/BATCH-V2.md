# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S06` — Curriculum & Learning Path · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — four stages whose titles, summaries and detail lines are bracketed placeholders, the programme name bracketed and the sequence declared illustrative, the duration and study format bracketed, the note that sequence, pace and assessment depend on the programme, one route to the same-variant programme list; the media counts per study (0, 1, 0, 0, 1) — are kept exactly. V1's `<details>` stage disclosures open as detail lines because the register runs no script and folds nothing; V1's lead, including *Open each stage for its learning content*, is kept as written.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S06-001` | Universal / Safe | 001 Apricot | 1 — the introduction beside a vertical sequence | loop behind the intro head | Intro column with the lead, the graphite sequence chip, the duration line with the clock mark, the action on the lead rule and the note; four stages as ruled rows with word-numeral chips | none · 14 | 134 |
| `EDU-S06-002` | Premium / Editorial | 002 Mulberry | 2 — the sequence beside a tall field | rise above the head | Split head; four ruled stage rows beside a 3:4 field; the duration, the action and the note on the lead rule | 3:4 · 14 | 143 |
| `EDU-S06-003` | Structured / Visual Modular | 003 Cobalt | 3 — the horizontal path | cross grid behind | Split head; four stage columns in a bordered plate on ink seams with the word-numeral at display size in the accent; the duration, the action and the note on the lead rule | none · 14 | 134 |
| `EDU-S06-004` | Conversion-led | 004 Iris | 4 — the programme context beside spacious stages | outline round *unfolds.* | Split head; V1's context panel as a band holding the chip, the duration, the note and the action on the lead rule; four spacious ruled stage rows beside it | none · 14 | 134 |
| `EDU-S06-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the asymmetric path | margin bar along the display column | Display column with the lead, the chip, the duration on a hairline, the note and the action; four ruled stage rows in the wide column with a 3:2 field dropped beneath at the right | 3:2 · 14 | 143 |

## What changed from V1

V1's numbered timeline nodes, its connecting spine, the curved photograph and the purple context panel go; each stage is a word-numeral chip (or, in 003, the word-numeral at display size where V1 set its oversized digits), the bracketed title in muted ink, the summary and the detail line on hairlines. The programme line is a graphite chip — the sector's `--no`; the duration line carries the clock mark. The only darkened surface is the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S06 -Fields 'Explore the shape of a programme|Illustrative learning sequence|Duration and study format|Explore the foundations|Review and take forward|Modules, learning activities|Explore programmes|sequence, pace and assessment'` — ALL CHECKS PASS; parity 40/40. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; fourteen placeholders per study.
- Rendered and read at 1440. No corrections needed.
