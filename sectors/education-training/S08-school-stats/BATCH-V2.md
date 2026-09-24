# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S08` — School Stats · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — four institutional measures whose every value is the pending `[—]` with an aria-label and whose every definition is a bracketed placeholder, the figures declared pending with a bracketed reporting period, the source and scope lines held under *About these figures*, V1's scope note that the measures do not indicate outcomes, completion rates or employment prospects, one route to the same-variant programme list; the media counts per study (0, 1, 0, 0, 1) — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing. No number is introduced anywhere.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S08-001` | Universal / Safe | 001 Apricot | 1 — four figures in an open strip | loop behind the head | Split head with the lead and the graphite pending chip; four measure cells in a bordered strip on ink seams, the pending value at display size in the accent; the opened source row; the action and the scope note on the lead rule | none · 11 | 109 |
| `EDU-S08-002` | Premium / Editorial | 002 Mulberry | 2 — the field paired with two-by-two figures | rise above the head | Head, lead, chip and a 3:2 field left; four measures two-by-two on hairlines, the opened source row, the action and the scope note on the lead rule right | 3:2 · 11 | 118 |
| `EDU-S08-003` | Structured / Visual Modular | 003 Cobalt | 3 — the featured figure beside three compact measures | cross grid behind | Split head; a bordered plate with the learner measure at the largest size beside the three others stacked; the opened source row as the plate's foot on the band tone; the action and the scope note on the lead rule | none · 11 | 109 |
| `EDU-S08-004` | Conversion-led | 004 Iris | 4 — the context beside the statistical band | outline round *A clearer picture.* | Split head; the context column with the chip, the opened source row, the scope note and the action on the lead rule; V1's statistical field as a band with the four measures two-by-two | none · 11 | 109 |
| `EDU-S08-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the asymmetric figures around a field | margin bar along the display column | Display column with the lead, the chip, the opened source row, the scope note and the action; four measures two-by-two on hairlines with a 4:3 field dropped beneath at the right | 4:3 · 11 | 118 |

## What changed from V1

V1's statistical tiles, the curved photograph and the purple statistical panel go; each measure is V1's pending `[—]` at display size in the accent, the measure name as type and the bracketed definition in muted ink, on hairlines or ink seams. FIGURES PENDING CONFIRMATION · [REPORTING PERIOD] is a graphite chip — the sector's `--no`. *About these figures* opens as a row with the document mark. V1's scope note is set in semibold ink in every study so its refusal of outcome claims reads first. The darkened surfaces are the 003 plate foot and the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S08 -Fields 'Explore the scale of the learning community|Figures pending confirmation|Learners|Programmes|Teaching team|Learning locations|About these figures|Source record|describe institutional scale|Explore programmes'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy — every value is the pending dash; no claim term; eleven placeholders per study.
- Rendered and read at 1440. Correction: 002 columns rebalanced so the field sits shorter beside the measures.
