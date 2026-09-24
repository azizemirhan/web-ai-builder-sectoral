# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the hero statement, lead, project-brief disclosure and three scope topics kept as written, no capacity, saving, client or site named, the reserved image a solar installation in its site context; the media counts per study (1, 1, 1, 0, 1) — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing. The hero statement is set as the `<h1>` the page owns.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S01-001` | Universal / Safe | 001 Sunlit | 1 — the split hero | arc behind the head | Eyebrow with the sun mark, the h1 with one accent phrase, the lead, the opened brief row on the lead rule and three scope chips left; a 4:5 field of the array right | 4:5 · 0 | 80 |
| `ENG-S01-002` | Premium / Editorial | 002 Terracotta | 2 — the statement above a panorama | rise above the head | Split statement with the lead; a shallow 3:1 field on the lead rule; the opened brief row beside the scope chips | 3:1 · 0 | 80 |
| `ENG-S01-003` | Structured / Visual Modular | 003 Tidal | 3 — the colour field beside the framed site | dot grid behind | A bordered plate with the statement as a cell on the band tone, where V1 set its teal field, beside a 4:3 field; the scope chips and the opened brief row as the plate's foot split by the lead rule | 4:3 · 0 | 80 |
| `ENG-S01-004` | Conversion-led | 004 Daybreak | 4 — the centred typographic hero | outline round *For your energy.* | Centred h1, the lead at a measured width, the scope chips and the opened brief row centred on the lead rule | none · 0 | 69 |
| `ENG-S01-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the oversized statement with an asymmetrical field | margin bar along the display column | Display column with the h1 at the largest size, the lead, the opened brief row and the scope chips; a 3:2 field dropped beside | 3:2 · 0 | 80 |

## What changed from V1

V1's tall rounded photograph, the 28–32px corners, the teal and blue colour fields, the dark Night Current ground and the plus-marked disclosure go; the hero is the sans display with one accent phrase, a bare 8px field labelled THE ARRAY, the project brief opened as a row with the document mark on the one lead rule, and the scope topics as accent chips. The only darkened surface is the 003 statement cell; Night Current is inverted onto pale sage paper with a moss accent. Copy is V1's throughout.

## Verification

- `engcheck.ps1 -Sec S01 -Fields 'Energy|Solar|Engineering|A brighter direction|For your energy|Explore solar energy and engineering possibilities|Prepare your project brief|Bring your site location|Solar possibilities|Site considerations|Long-term planning'` — ALL CHECKS PASS; parity 55/55. One `<h1>` per study (the hero); no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; no placeholder needed.
- Rendered and read at 1440. No corrections needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
