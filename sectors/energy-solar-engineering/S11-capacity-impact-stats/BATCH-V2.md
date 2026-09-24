# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S11` — Capacity & Impact Stats · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three metrics kept as written, the value, description and source of each a bracketed placeholder, no capacity, generation total, emissions result, unit, period, baseline or source named; no media in any study — are kept exactly. The value stands as V1's bracketed `[Value]` at display size in muted ink, never as a counter; V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S09 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S11-001` | Universal / Safe | 001 Sunlit | 1 — open metric columns with oversized values | arc behind the head | Split head with the lead; three metric cells in a bordered grid with word-numeral chips, bracketed values at display size, bracketed descriptions and opened source rows | none · 9 | 151 |
| `ENG-S11-002` | Premium / Editorial | 002 Terracotta | 2 — editorial metric rows pairing a value with its scope | rise above the head | Three ruled rows on the lead rule with the chip column, the bracketed value at display size, the title, the bracketed description and the opened source row | none · 9 | 151 |
| `ENG-S11-003` | Structured / Visual Modular | 003 Tidal | 3 — the featured capacity figure beside two supporting metrics | dot grid behind | A bordered plate: Installed capacity as a tall cell on the band tone with its value at the large size and its row on the lead rule, the two other metrics stacked beside | none · 9 | 151 |
| `ENG-S11-004` | Conversion-led | 004 Daybreak | 4 — the source-focused stack beside the interpretation guide | outline round *So does their context.* | Narrow head column with the lead beneath; three metric rows stacked beside on the lead rule, led by word numerals with marks, each source row on the band tone | none · 9 | 151 |
| `ENG-S11-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the descending composition ending in the impact figure | margin bar along the display column | Three metric columns stepping down across the page, Emissions impact wider on the band tone with its value in the accent and its row on the lead rule | none · 9 | 151 |

## What changed from V1

V1's oversized numerals, editorial metric rows, featured panel, source stack, dark descending composition with the lime figure and the plus-marked disclosures go; each metric is a word-numeral chip (or word numeral with its mark in 004), the bracketed value at display size in muted ink, the title as type, the bracketed description and the source-and-scope disclosure opened as a row with the document mark and its bracketed placeholder. The darkened surfaces are the 003 capacity cell, the 004 source rows and the 005 impact cell. Copy is V1's throughout; no figure, unit, total or reduction appears anywhere — every value is V1's bracketed placeholder.

## Verification

- `engcheck.ps1 -Sec S11 -Fields 'Read capacity and impact together|Installed capacity|Verified capacity and unit|Source, system boundary|Energy generated|Verified energy total|Metering or calculation source|Emissions impact|Verified emissions result|Methodology, baseline|View source|Value'` — ALL CHECKS PASS; parity 60/60. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; nine placeholders per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
