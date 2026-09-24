# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S02` — Solutions & Services · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three solution areas kept as written, each service scope a bracketed placeholder, 004's own question labels kept, no service, deliverable or eligibility named; no media in any study — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S02-001` | Universal / Safe | 001 Sunlit | 1 — three equal solutions below an open introduction | arc behind the head | Split head with the lead; three cells in a bordered grid on ink seams with word-numeral chips, titles, lines and the opened scope row | none · 3 | 143 |
| `ENG-S02-002` | Premium / Editorial | 002 Terracotta | 2 — editorial rows with large titles | rise above the head | Split head; three ruled rows on the lead rule with the chip column, the title at display size and the opened scope row | none · 3 | 143 |
| `ENG-S02-003` | Structured / Visual Modular | 003 Tidal | 3 — the featured module beside two stacked | dot grid behind | A bordered plate with Solar planning as a cell on the band tone beside Energy storage and Engineering support stacked | none · 3 | 143 |
| `ENG-S02-004` | Conversion-led | 004 Daybreak | 4 — question-led choices with prominent scope | outline round *Explore the possibilities.* | Three ruled columns led by V1's own questions as tracked labels with marks; each scope row on the band tone | none · 3 | 145 |
| `ENG-S02-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the asymmetrical grid with the solar cell on the band | margin bar along the display column | Display column with the lead; Solar planning as a band where V1 set its lime card; the two other areas as ruled columns | none · 3 | 143 |

## What changed from V1

V1's solution cards, its 28–32px corners, the curved lime card, the dark ground and the plus-marked disclosures go; each area is a word-numeral chip with V1's EXPLORE label (or V1's question in 004), the title as type, the line and the service scope opened as a row with the document mark and its bracketed placeholder in muted ink. The darkened surfaces are the 003 featured cell, the 004 scope rows and the 005 band. Copy is V1's throughout.

## Verification

- `engcheck.ps1 -Sec S02 -Fields 'Find a starting point for your energy project|Solar planning|Consider how solar could fit|Energy storage|Explore the role storage|Engineering support|Understand the support a project|View service scope|Confirmed solar services|Verified storage support|Confirmed disciplines'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; three placeholders per study.
- Rendered and read at 1440. Correction: 005 band scope row aligned to start so it sits level with the title.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
