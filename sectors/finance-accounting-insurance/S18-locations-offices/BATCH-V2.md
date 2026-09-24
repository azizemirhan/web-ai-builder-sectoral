# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S18` — Locations & Offices · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — eyebrow, headline, introduction and arrival title kept as written, the photograph caption, office name, address, visiting arrangements, local contact line and arrival information bracketed placeholders, no address, hours, timezone, contact detail, transport or accessibility arrangement named and no map drawn or embedded; one verified office photograph — are kept exactly. V1's `<details>` disclosure opens as a row.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S18-001` | Universal / Safe | 001 Ivory & Olive | 1 — the office field beside an open visitor introduction | column rules behind the head | A 4:5 office field with its bracketed caption beside the office details on the lead rule | 1 · 6 | 132 |
| `FIN-S18-002` | Premium / Editorial | 002 Rosewood | 2 — the panoramic office above an editorial address layout | bracket above the headline | A 3:1 office panorama on the lead rule; the office details inset beneath | 1 · 6 | 132 |
| `FIN-S18-003` | Structured / Visual Modular | 003 Lagoon | 3 — the office information below its introduction beside a tall field | registration grid behind | A bordered plate with the details cell on the band tone, its arrival row on the lead rule, beside a 4:3 office field | 1 · 6 | 132 |
| `FIN-S18-004` | Conversion-led | 004 Iris | 4 — the visitor information beside an office field | span mark beneath *your next conversation.* | The office details with its arrival row as a band on the band tone, beside a 4:5 office field | 1 · 6 | 132 |
| `FIN-S18-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the office panorama followed by a visitor panel | corner frame along the display column | A 4:5 office field beside the display column; the office details as an offset band on the band tone | 1 · 6 | 132 |

## What changed from V1

V1's rounded office photograph, editorial address layout, teal and violet panels and apricot visitor panel and the plus-marked disclosure go; the photograph is a labelled empty field (THE ENTRANCE) with V1's bracketed caption beneath, and the details are the OFFICE DETAILS label with the building mark, the bracketed office name as type in muted ink, the bracketed address and visiting arrangements, the bracketed contact line and the arrival disclosure opened as a row with the compass mark. The darkened surfaces are the 003 details cell, the 004 arrival band and the 005 details band. Copy is V1's throughout; no address, hours or contact detail appears anywhere and no map is drawn.

## Verification

- `fincheck.ps1 -Sec S18 -Fields 'Our offices|Plan your visit|Find a place for|your next conversation|Explore the office details before planning|Verified office photograph caption|Office details|Approved office name|Verified street address|Confirmed visiting hours|Verified local contact details|Arrival and accessibility|Verified entrance, public transport'` — ALL CHECKS PASS; parity 65/65. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio label; no claim term; one field and six placeholders per study.
- Rendered and read at 1440. No correction needed.
