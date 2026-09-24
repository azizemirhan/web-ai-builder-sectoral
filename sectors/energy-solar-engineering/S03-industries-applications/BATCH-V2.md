# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S03` — Industries & Applications · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three settings kept as written, each discussion-point line a bracketed placeholder, 004's own question labels kept, the images approved site photographs of the workplace, production and rural settings and never a person; the media counts per study (3, 3, 3, 3, 3) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions carry the S02 devices with a field in every item.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S03-001` | Universal / Safe | 001 Sunlit | 1 — three equal settings below an open introduction | arc behind the head | Split head with the lead; three cells in a bordered grid with 3:2 fields, word-numeral chips, titles, lines and the opened discussion row | 3 × 3:2 · 3 | 167 |
| `ENG-S03-002` | Premium / Editorial | 002 Terracotta | 2 — editorial rows pairing the site and its context | rise above the head | Three ruled rows on the lead rule with a 4:3 field in a left column, the title at display size and the opened discussion row | 3 × 4:3 · 3 | 167 |
| `ENG-S03-003` | Structured / Visual Modular | 003 Tidal | 3 — the featured application beside two compact modules | dot grid behind | A bordered plate with Business & workplaces as a cell on the band tone with a 4:3 field beside the two other settings stacked with 1:1 fields | 4:3 + 2 × 1:1 · 3 | 167 |
| `ENG-S03-004` | Conversion-led | 004 Daybreak | 4 — horizontal choices with focused discussion controls | outline round *Different energy questions.* | Three ruled columns with 4:3 fields led by V1's own questions as tracked labels; each discussion row on the band tone | 3 × 4:3 · 3 | 173 |
| `ENG-S03-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the staggered grid with varied fields | margin bar along the display column | Business & workplaces as a band with a 3:2 field beside its lines; the two other settings as ruled columns with 4:3 fields | 3:2 + 2 × 4:3 · 3 | 167 |

## What changed from V1

V1's application cards, the rounded photographs, the dark ground and the plus-marked disclosures go; each setting is a bare 8px field labelled THE SITE, THE WORKSHOP or THE FIELD, a word-numeral chip with V1's EXPLORE label (or V1's question in 004), the title as type, the line and the discussion points opened as a row with the document mark and its bracketed placeholder. The darkened surfaces are the 003 featured cell, the 004 discussion rows and the 005 band. Copy is V1's throughout.

## Verification

- `engcheck.ps1 -Sec S03 -Fields 'Explore energy considerations across three settings|Business|workplaces|For offices, shops|Production|logistics|For workshops, warehouses|Land|agriculture|For farms and rural properties|Discussion points|Confirmed commercial applications|Verified industrial applications|Confirmed rural applications|Workplace setting|Production setting|Rural setting'` — ALL CHECKS PASS; parity 85/85. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; three placeholders per study.
- Rendered and read at 1440. Correction: field ratios set per item in 003 and 005 so each label matches its field.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
