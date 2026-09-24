# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S18` — RFQ & Site Assessment · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — headline, lead, form title, notes, four labelled fields and button label kept as written, no address, telephone, price, timescale or availability named, no submission destination; no media in any study — are kept exactly. V1's local-summary script, `<noscript>` note and result region go because the register runs no script: the form is static, the PREPARE ENQUIRY button is an inert `type="button"` and V1's own note beneath the title says nothing is sent or saved. The five compositions follow V1's own five arrangements in the S13 grammar with the form in the story's place.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S18-001` | Universal / Safe | 001 Sunlit | 1 — the open introduction beside the enquiry panel | arc behind the head | Head and lead in a left column; the form as a panel on the band tone beside, its action row on the lead rule | none · 0 | 97 |
| `ENG-S18-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial introduction above a wide two-column form | rise above the head | The form in two columns on the lead rule — title at display size with its note, then the fields, closing note and inert action | none · 0 | 97 |
| `ENG-S18-003` | Structured / Visual Modular | 003 Tidal | 3 — the enquiry panel paired with the introductory column | dot grid behind | A bordered plate: head and lead as an open cell beside the form cell on the band tone, its action row on the lead rule | none · 0 | 97 |
| `ENG-S18-004` | Conversion-led | 004 Daybreak | 4 — the wide enquiry band beneath a split introduction | outline round *Shape the next step.* | The form as a full-width band on the band tone — title and note in a left column, fields beside, closing note and action on the lead rule across | none · 0 | 97 |
| `ENG-S18-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the oversized invitation above an offset enquiry panel | margin bar along the display column | The form as an offset band on the band tone, its action row on the lead rule | none · 0 | 97 |

## What changed from V1

V1's warm, teal, blue and lime enquiry panels, its script-prepared local summary, disabled-until-script button, `<noscript>` fallback and live result region go; the form is V1's title and note as type, four labelled fields on 1px ink borders at 4px radius, V1's closing note and the inert PREPARE ENQUIRY action in the register's bordered button on the lead rule. The darkened surfaces are the 001, 003, 004 and 005 form panels. Copy is V1's throughout; no destination, price or timescale appears anywhere.

## Verification

- `engcheck.ps1 -Sec S18 -AllowForm -Fields 'Prepare the essentials for a project conversation|Your project, at a glance|Prepare a local enquiry summary|Your name|Email address|Site location|Project brief|Include only information needed|Prepare enquiry'` — ALL CHECKS PASS; parity 45/45. No `<h1>`; no header/nav/footer; static form only (`-AllowForm`); no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; no placeholder tokens (the form collects nothing and names no destination).
- Rendered and read at 1440. Correction: the action block dropped the row grid so the closing note sits flush; inputs set to regular weight so the field hints read as hints.
