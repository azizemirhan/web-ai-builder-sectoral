# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S27` — Office / Location Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the category prefix, the introduction, the section and field titles (Address, Contact, Visiting hours, What happens here, Getting here, People based here), the preparation line and both map refusals kept as written, every value bracketed, no address, number, email, hour, timezone, transport, parking, access arrangement or adviser invented, and no third-party map embedded anywhere — are kept exactly. V1's own reserved-area count and address layout per study are kept as it set them: map and photograph in 001 and 003, map only in 004, neither in 002 and 005; four address lines in 001 and 003, two in 004, one in 002 and 005. This is a detail page, so V1's office name is promoted to the page's `<h1>`. The people `<nav>` is V1's own (`-AllowNav`).
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S27-001` | Universal / Safe | 001 Ivory & Olive | 1 — the address and map above three read columns | column rules behind the head | The address card on the band tone beside the 4:3 map area; the three sections as columns under one lead rule; the 3:1 office photograph beneath | 2 reserved · 16 | 170 |
| `FIN-S27-002` | Premium / Editorial | 002 Rosewood | 2 — the office read as one editorial column | open bracket at the head | A 52rem column — the single-line address, four bare labelled fields in pairs, the preparation row, the three sections on the lead rule and the map refusal | none · 15 | 162 |
| `FIN-S27-003` | Dense / Information-heavy | 003 Lagoon | 3 — the office set out as three banded rows | registration grid behind | Address, Contact and Visiting hours as three cells in a bordered plate on ink seams; the 3:2 map beside the arrival arrangements; the 4:3 photograph beside the closing pair | 2 reserved · 16 | 172 |
| `FIN-S27-004` | Conversion-led | 004 Iris | 4 — the address panel standing beside the map | span mark under the office name | The address panel on the band tone with the Plan a visit action beside the 4:3 map area; the three sections on the lead rule in a 52rem column, the introduction kept inside what happens here | 1 reserved · 15 | 158 |
| `FIN-S27-005` | Sector-native / Distinctive | 005 Ink & Apricot, inverted | 5 — the framed head above three offset columns | corner frame at the head | The address on the band tone with the four arrangements as one four-field strip; the three sections as columns under one lead rule, offset inward; the map refusal | none · 15 | 163 |

## What changed from V1

V1's rounded location cards, tinted map placeholders, boxed contact tables and pill-shaped hour chips go. The office name is the display `<h1>` with its second half in the accent, the staffing status sits in ink beneath it, and the address is set as plain ink lines rather than a table. Every arrangement — telephone, email, visiting hours, appointments, entrance, parking, access and arrival — is a bare labelled field on a hairline. The sections are opened by their own marks: the pin for the address, the telephone for contact, the clock for visiting hours, the layers for what happens here, the compass for getting here and the person for the people based here. V1's two map refusals are carried in the graphite refusal tone behind the prohibition mark — beneath the reserved map area where there is one, and standing alone in 002 and 005 where V1 refused both a map and a photograph — so the refusal reads as a stated position rather than as caption text. The reserved map and office areas are empty flat labelled fields and nothing is embedded. The darkened surfaces are the 001, 004 and 005 address panels and the 003 address cell.

## Verification

- `fincheck.ps1 -Sec S27 -AllowNav -Fields 'Our offices|Region|Approved office name|…|All offices'` — ALL CHECKS PASS; parity 160/160. One `<h1>` per study (detail page); no header/footer; the people nav is V1's (`-AllowNav`); no form; links only — Plan a visit to the same-variant S19, the two advisers to S04 and All offices back to S18 (all checked on disk); no embedded map or map service anywhere; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term.
- Rendered and read at 1440. Corrections: in 005 the four-column field strip was scoped to the address panel, having also been applied to the arrival arrangements in a one-third column, where the four fields were crushed to a few characters a line; in 003 the closing photograph column was narrowed from 0.9fr to 0.6fr so the 4:3 field does not tower over the short pair of sections beside it.
