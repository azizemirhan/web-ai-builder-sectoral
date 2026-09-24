# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S06` — Technology & Systems · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three technologies kept as written, the system scope of each a bracketed placeholder, 004's own lead-ins kept, no product, capacity, interface or constraint named; three reserved photographs, never a person — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions carry the S03 devices with a field in every item.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S06-001` | Universal / Safe | 001 Sunlit | 1 — three technology stories below an open introduction | arc behind the head | Split head with the lead; three cells in a bordered grid with 3:2 fields, word-numeral chips, titles, lines and the opened system row | 3 · 3 | 165 |
| `ENG-S06-002` | Premium / Editorial | 002 Terracotta | 2 — alternating editorial rows with generous fields | rise above the head | Three ruled rows on the lead rule, the 4:3 field alternating side to side, the title at display size and the opened system row | 3 · 3 | 165 |
| `ENG-S06-003` | Structured / Visual Modular | 003 Tidal | 3 — the featured solar technology beside two compact modules | dot grid behind | A bordered plate: Solar generation as a tall cell on the band tone with a 4:3 field, Energy storage and Power conversion stacked beside with 1:1 fields | 3 · 3 | 165 |
| `ENG-S06-004` | Conversion-led | 004 Daybreak | 4 — comparison columns with prominent discussion | outline round *One considered system.* | Three ruled columns with 4:3 fields led by V1's own lead-ins as tracked labels with marks; each system row on the band tone | 3 · 3 | 168 |
| `ENG-S06-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the staggered gallery with a tall central field | margin bar along the display column | Three staggered technology columns, 4:3 · 4:5 · 4:3, the centre dropped below the outer two | 3 · 3 | 165 |

## What changed from V1

V1's broad photo stories, alternating editorial rows, comparison cards with image windows, the dark staggered gallery and the plus-marked disclosures go; each technology is a labelled empty field (THE ARRAY or THE EQUIPMENT), a word-numeral chip (or V1's lead-in in 004), the title as type, the line and the system disclosure opened as a row with the document mark and its bracketed placeholder in muted ink. The darkened surfaces are the 003 featured cell and the 004 system rows. Copy is V1's throughout; the fields carry V1's three subjects — solar installation, storage equipment, conversion equipment.

## Verification

- `engcheck.ps1 -Sec S06 -Fields 'Get to know the building blocks|Solar generation|Explore solar modules|Energy storage|Consider storage alongside|Power conversion|Understand the equipment that connects|Explore system|Confirmed solar technologies|Verified storage options|Confirmed conversion equipment|Solar installation|Storage equipment|Conversion equipment'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders and field ratio labels; no claim term; three fields and three placeholders per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
