# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S05` — Capabilities · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three capability areas kept as written, each expertise line a bracketed placeholder, 004's own lead-ins kept, no method, discipline, qualification or deliverable named; no media in any study — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions carry the S02 devices.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S05-001` | Universal / Safe | 001 Sunlit | 1 — open columns with large typographic anchors | arc behind the head | Split head with the lead; three cells in a bordered grid with word-numeral chips, titles, lines and the opened capability row | none · 3 | 149 |
| `ENG-S05-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial index beside a compact introduction | rise above the head | Three ruled rows on the lead rule with the chip column, the title at display size and the opened capability row | none · 3 | 149 |
| `ENG-S05-003` | Structured / Visual Modular | 003 Tidal | 3 — three connected bands with the middle emphasised | dot grid behind | A bordered plate of three stacked bands, System coordination on the band tone with its row on the lead rule | none · 3 | 149 |
| `ENG-S05-004` | Conversion-led | 004 Daybreak | 4 — capability choices with prominent scope | outline round *Connected expertise.* | Three ruled columns led by V1's own lead-ins as tracked labels with marks; each capability row on the band tone | none · 3 | 155 |
| `ENG-S05-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the asymmetric field with an oversized first statement | margin bar along the display column | Site understanding as a band with its title at display size; the two other capabilities as ruled columns | none · 3 | 149 |

## What changed from V1

V1's capability columns with giant numerals, the contrasting middle band, the dark field and the plus-marked disclosures go; each capability is a word-numeral chip (or V1's lead-in in 004), the title as type, the line and the capability opened as a row with the document mark and its bracketed placeholder in muted ink. The darkened surfaces are the 003 middle band, the 004 capability rows and the 005 band. Copy is V1's throughout.

## Verification

- `engcheck.ps1 -Sec S05 -Fields 'Capabilities|Bringing it together|Clear thinking|Connected expertise|Explore the capabilities an energy project|Site understanding|Bring the place into focus|System coordination|Consider how the parts|Delivery planning|Make the route towards delivery|Explore capability|Verified assessment methods|Confirmed design disciplines|Verified planning support'` — ALL CHECKS PASS; parity 75/75. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; three placeholders per study.
- Rendered and read at 1440. Correction: 003 chip column narrowed and top-aligned.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
