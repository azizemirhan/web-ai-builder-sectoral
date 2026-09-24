# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S27` — Location Branch Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — eyebrow, lead, four contact labels and four section titles kept as written, the location name, address, telephone, email, hours and four sections bracketed placeholders and never real contact details, no place, team, route or arrangement named, no link and no map; one reserved location photograph, never a person — are kept exactly. V1's `<h2>` is promoted to the page's `<h1>` because this is a detail page.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S27-001` | Universal / Safe | 001 Sunlit | 1 — the contact rail beside the location field | arc behind the head | Name, lead and four marked contact fields above four visit rows on the lead rule in a left column; a tall 4:5 field beside | 1 · 9 | 157 |
| `ENG-S27-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial contact row above a panoramic field | rise above the head | The lead and contact fields beside the name; a 3:1 field on the lead rule; four visit rows in two columns beneath | 1 · 9 | 157 |
| `ENG-S27-003` | Structured / Visual Modular | 003 Tidal | 3 — the contacts and a supporting field beside the visit narrative | dot grid behind | A bordered plate: the visit cell on the band tone beside a compact 4:3 field | 1 · 9 | 157 |
| `ENG-S27-004` | Conversion-led | 004 Daybreak | 4 — the contact panel above the visit narrative and field | outline round *location name]* | Four visit columns on the lead rule inside a band on the band tone; a 3:1 field beneath | 1 · 9 | 157 |
| `ENG-S27-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the location identity with a contact ribbon and offset narrative | margin bar along the display column | A 4:5 field beside the display column; four visit rows as an offset band on the band tone | 1 · 9 | 157 |

## What changed from V1

V1's contact rail, editorial contact row, teal contacts, blue panel and lime ribbon go; the bracketed location name is the h1 in muted ink with its second half in the accent, the four contact fields are a marked list (pin, phone, mail, clock) with bracketed values, and the four visit sections are rows with their marks (building, people, compass, calendar). The darkened surfaces are the 003 visit cell, the 004 visit band and the 005 visit band. Copy is V1's throughout; no address, number, email or map appears anywhere.

## Verification

- `engcheck.ps1 -Sec S27 -Fields 'Our places|Location detail|Approved location name|Check the location details before planning|Address|Verified full address|Phone|Local contact number|Email|Location email address|Opening hours|Confirmed local hours|What happens here|Confirmed activities and services|The local team|Verified teams or people|Getting here|Verified arrival instructions|Before your visit|Confirmed booking requirements|Location entrance'` — ALL CHECKS PASS; parity 105/105. One `<h1>` per study; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio label; no claim term; nine placeholders per study.
- Rendered and read at 1440. Correction: the 004 visit block set on the band tone so it reads as the panel V1 gave it.
