# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S11` — Accreditations · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one accreditation record whose body name, title, scope, status, valid period and verification lines are bracketed placeholders, the information declared awaiting verification, no logo, crest or seal, V1's scope note that institutional recognition does not cover every course, one route to the same-variant programme list; no media in any study — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S11-001` | Universal / Safe | 001 Apricot | 1 — the introduction above an open record | loop behind the head | Split head with the lead and the graphite verification chip; the record as a bordered plate — organisation cell, three labelled cells with the layers, tick and calendar marks, the opened verification foot on the band tone; the action and the scope note on the lead rule | none · 8 | 108 |
| `EDU-S11-002` | Premium / Editorial | 002 Mulberry | 2 — the organisation title above a horizontal summary | rise above the head | The organisation at display size on the lead rule; three ruled labelled columns; the opened verification row; the action and the scope note on the closing hairline | none · 8 | 108 |
| `EDU-S11-003` | Structured / Visual Modular | 003 Cobalt | 3 — the organisation cell beside the details | cross grid behind | Split head; a bordered plate with the organisation as a cell on the band tone, where V1 set its blue field, beside three labelled rows and the opened verification row; the action and the scope note on the lead rule | none · 8 | 108 |
| `EDU-S11-004` | Conversion-led | 004 Iris | 4 — the contextual introduction beside a concise record | outline round *Know what it covers.* | V1's introduction as a band holding the lead, the chip, the scope note and the action on the lead rule; the record beside it as ruled rows | none · 8 | 108 |
| `EDU-S11-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the organisation at the largest size beside its context | margin bar along the display column | Display column with the lead, the chip and the organisation at display size in the accent, as V1's oversized typography; the labelled rows, the opened verification row, the scope note and the action in the wide column | none · 8 | 108 |

## What changed from V1

V1's record cards, its badge-like framing, the blue and purple panels and the plus-marked disclosure go; the record is bare type on hairlines or ink seams — the body name in muted ink (or in the accent where V1 made it oversized) as a placeholder, Scope, Status and Valid period as tracked labels with the layers, tick and calendar marks, the verification details opened as a row with the document mark. ACCREDITATION INFORMATION AWAITING VERIFICATION is a graphite chip — the sector's `--no`. V1's scope note is set in semibold ink in every study. The darkened surfaces are the 001 plate foot, the 003 organisation cell and the 004 band. No crest, seal or logo is drawn. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S11 -Fields 'Explore the organisation behind an accreditation|awaiting verification|Accrediting organisation|Accrediting body name|recognition title|Scope|Status|Valid period|Verification details|Official register reference|Date checked|Check the exact scope|Explore programmes'` — ALL CHECKS PASS; parity 65/65. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term — no *accredited by*; eight placeholders per study.
- Rendered and read at 1440. Correction: the organisation label excluded from the organisation paragraph rule so it keeps the tracked label size.
