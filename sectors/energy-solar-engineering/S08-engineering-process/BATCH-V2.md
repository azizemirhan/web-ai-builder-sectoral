# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S08` — Engineering Process · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three stages kept as written in V1's order as an ordered list, the detail of each a bracketed placeholder, no deliverable, timescale, responsibility or approval named; no media in any study — are kept exactly. V1's numerals become word-numeral chips; V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S05 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S08-001` | Universal / Safe | 001 Sunlit | 1 — the open three-stage sequence | arc behind the head | Split head with the lead; three stage cells in a bordered grid with word-numeral chips and opened stage rows | none · 3 | 163 |
| `ENG-S08-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial sequence beneath a split introduction | rise above the head | Three ruled stage rows on the lead rule with the chip column, the title at display size and the opened stage row | none · 3 | 163 |
| `ENG-S08-003` | Structured / Visual Modular | 003 Tidal | 3 — stepped bands with a progressive inset | dot grid behind | A bordered plate of three stacked stage bands stepping in from the left, Prepare the handover on the band tone with its row on the lead rule | none · 3 | 163 |
| `ENG-S08-004` | Conversion-led | 004 Daybreak | 4 — the preparation-led first stage beside two compact later stages | outline round *At every stage.* | Frame the brief as a tall cell on the band tone with its title at display size and its row on the lead rule; two compact ruled cells stacked beside, led by STAGE labels with marks | none · 3 | 166 |
| `ENG-S08-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the triptych with descending stage positions | margin bar along the display column | Three ruled stage columns stepping down across the page, the first on the lead rule | none · 3 | 163 |

## What changed from V1

V1's circled numerals, editorial sequence, inset bands, preparation-led panel, dark triptych and plus-marked disclosures go; each stage is a word-numeral chip (or a STAGE label with its mark in 004), the title as type, the line and the stage opened as a row with the document mark and its bracketed placeholder in muted ink. The darkened surfaces are the 003 last band and the 004 first-stage cell. Copy is V1's throughout; the list stays ordered.

## Verification

- `engcheck.ps1 -Sec S08 -Fields 'Explore a possible path|Frame the brief|Start with the place|Shape the approach|Use the brief to discuss|Prepare the handover|Agree what completion|Explore this stage|Confirmed discovery inputs|Verified design stages|Confirmed commissioning scope'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; three placeholders per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
