# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S02` — Programmes & Courses · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three programmes whose every field is a bracketed placeholder, programme information pending, format and duration as labelled facts, entry, fees and next start kept together, the endnote; the media counts per study (3, 3, 3, 3, 3) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S02-001` | Universal / Safe | 001 Apricot | 1 — three equal programmes below an open introduction | loop behind the head | Three field-led cells in a bordered grid on ink seams, each a 3:2 field, subject chip, name, description, FORMAT / DURATION caption and opened information rows; endnote on the lead rule | 3 × 3:2 · 25 | 172 |
| `EDU-S02-002` | Premium / Editorial | 002 Mulberry | 2 — one featured programme, then two compact | rise above the head | The first programme as a wide row on the lead rule with a 3:2 field; the second and third as ruled columns with 4:3 fields; endnote | 3:2 + 2 × 4:3 · 25 | 172 |
| `EDU-S02-003` | Structured / Visual Modular | 003 Cobalt | 3 — the intro column beside three joined modules | cross grid behind | A narrow intro column with the endnote on the lead rule; one bordered plate of three modules with 4:3 fields, stacked labelled facts and the information rows on the band tone at the foot | 3 × 4:3 · 25 | 172 |
| `EDU-S02-004` | Conversion-led | 004 Iris | 4 — the decision-led introduction with the note as a band | outline round *next subject.* | V1's *An interesting subject. A commitment that fits.* as a band split by the lead rule; three ruled programme columns with 3:2 fields and the information rows on the lead rule; endnote | 3 × 3:2 · 25 | 179 |
| `EDU-S02-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered gallery | margin bar along the display column | Three programmes staggered — 4:5 flush, 3:2 dropped, 4:5 half-dropped — with the same fields; endnote on the lead rule | 2 × 4:5 + 3:2 · 25 | 172 |

## What changed from V1

White cards, 24–30px radii, arched image shapes and the filled purple summary pill go; each programme is a bare 8px field with its subject as an accent chip, its name in muted ink as a placeholder, and its facts as labelled lines on hairlines. PROGRAMME INFORMATION PENDING is a graphite chip — the sector's `--no`. The darkened surfaces are the 003 information feet and the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S02 -Fields 'Compare the focus|Programme information pending|Programme one|Programme three|Delivery mode|Study commitment|Entry:|Fees:|Next start:|specific to each course'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no `<details>`; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; twenty-five placeholders per study.
- Rendered and read at 1440. No corrections needed.
