# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S15` — Technology Integrations · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three connection categories and the availability title kept as written, the platform names, connection descriptions, supported editions and availability notes bracketed placeholders, no platform, vendor, edition, subscription, charge or documentation destination named; no media in any study — are kept exactly. V1's bracketed platform names gain the `data-placeholder="true"` attribute their brackets imply (ten placeholders per study, from V1's seven); V1's `<details>` disclosure opens as a row.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S15-001` | Universal / Safe | 001 Ivory & Olive | 1 — the integration introductions in three open columns | column rules behind the head | Three connection cells in a bordered grid with category labels, bracketed platform names, descriptions and edition lines | none · 10 | 169 |
| `FIN-S15-002` | Premium / Editorial | 002 Rosewood | 2 — the editorial rows pairing a platform with its everyday purpose | bracket above the headline | Three ruled connection rows on the lead rule with the chip column and the bracketed platform name at display size | none · 10 | 169 |
| `FIN-S15-003` | Structured / Visual Modular | 003 Lagoon | 3 — the introduction beside a stacked set of integration panels | registration grid behind | A bordered plate with one connection as a tall cell on the band tone beside two stacked connection cells | none · 10 | 169 |
| `FIN-S15-004` | Conversion-led | 004 Iris | 4 — the featured integration beside two supporting connections | span mark beneath *to work together.* | Three connection rows stacked beside the head rail, each description and edition line on the band tone | none · 10 | 169 |
| `FIN-S15-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the integration collection with a raised centre | corner frame along the display column | Three connection columns, the middle raised as a panel on the band tone | none · 10 | 169 |

## What changed from V1

V1's rounded integration cards, editorial rows, stacked panels, violet feature and apricot centre and the plus-marked disclosure go; each connection is V1's category as a tracked accent label, the bracketed platform name as type in muted ink, the bracketed description and the bracketed edition line, with V1's availability disclosure opened as a row with the link mark on a hairline. The darkened surfaces are the 003 first cell, the 004 descriptions and the 005 central panel. Copy is V1's throughout; no platform, vendor or destination appears anywhere and no documentation is linked.

## Verification

- `fincheck.ps1 -Sec S15 -Fields 'Working together|Your digital tools|A more connected way|to work together|Explore how your everyday tools|Accounting workspace|Approved platform name|Verified accounting connection|Document exchange|Verified document-sharing connection|Business reporting|Verified reporting connection|Supported edition|Availability and setup|Confirmed availability, setup'` — ALL CHECKS PASS; parity 75/75. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; ten placeholders per study.
- Rendered and read at 1440. Correction: in 002 every item child other than the chip is held in the content column, so the edition line no longer falls under the chip.
