# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S12` — Products & Systems · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three product slots (solar module, storage system, inverter) kept as written, the name, description and product details of each a bracketed placeholder, no manufacturer, model, specification, rating, capacity, warranty or price named; three reserved product photographs, never a person — are kept exactly. V1's bracketed names now carry `data-placeholder="true"` like the other placeholders; V1's numerals become word-numeral chips; V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S06 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S12-001` | Universal / Safe | 001 Sunlit | 1 — three product cards with contained image stages | arc behind the head | Split head with the lead; three product cells in a bordered grid with 4:3 fields, word-numeral chips, bracketed names and descriptions and opened product rows | 3 · 9 | 174 |
| `ENG-S12-002` | Premium / Editorial | 002 Terracotta | 2 — the collection with broad image columns and open summaries | rise above the head | Three ruled rows on the lead rule with 4:3 fields alternating side to side, the bracketed name at display size and the opened product row | 3 · 9 | 174 |
| `ENG-S12-003` | Structured / Visual Modular | 003 Tidal | 3 — horizontal modules pairing image, identity and details | dot grid behind | A bordered plate of three horizontal modules — 1:1 field, chip with name and description, opened product row in a right column — the middle on the band tone with its row on the lead rule | 3 · 9 | 174 |
| `ENG-S12-004` | Conversion-led | 004 Daybreak | 4 — the prominent featured product beside two compact cards | outline round *Start with the details.* | A bordered plate: the solar module slot as a tall cell on the band tone with a 4:3 field and its row on the lead rule, the two other slots stacked beside with 1:1 fields | 3 · 9 | 174 |
| `ENG-S12-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the collection with broad stages and a featured card | margin bar along the display column | Three ruled product columns with 4:5 fields, the solar module as a card on the band tone with its row on the lead rule | 3 · 9 | 174 |

## What changed from V1

V1's product cards with image stages, broad image columns, horizontal modules, featured card, dark collection with the lime card and the plus-marked disclosures go; each product slot is a labelled empty field (THE EQUIPMENT), a word-numeral chip, the bracketed name and description in muted ink and the product disclosure opened as a row with the document mark and its bracketed placeholder. The darkened surfaces are the 003 middle module, the 004 featured cell and the 005 first card. Copy is V1's throughout; no product, manufacturer or figure appears anywhere.

## Verification

- `engcheck.ps1 -Sec S12 -Fields 'Explore products in the context|Solar module name|Approved solar module description|Verified specifications, model reference|Storage system name|Approved storage system description|Verified usable capacity|Inverter name|Approved inverter description|Verified electrical ratings|View product details|Solar module|Storage system|Inverter'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term; three fields and nine placeholders per study.
- Rendered and read at 1440. Correction: 003 module rows given a trailing free row so the identity column no longer spreads to the field height.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
