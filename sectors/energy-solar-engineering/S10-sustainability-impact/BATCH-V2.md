# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S10` — Sustainability & Impact · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — kicker, title and two paragraphs kept as written, the impact evidence a bracketed placeholder, no impact figure, emission reduction, baseline, saving or environmental claim named; two reserved photographs of the site and of lifecycle activity, never a person — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S04 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S10-001` | Universal / Safe | 001 Sunlit | 1 — the wide site field above the impact story | arc behind the head | Split head with the lead; a 3:1 site field on the lead rule; the story beside a 4:3 lifecycle field | 2 · 1 | 126 |
| `ENG-S10-002` | Premium / Editorial | 002 Terracotta | 2 — the portrait site context beside an editorial narrative | rise above the head | A 4:5 site field beside the narrow story on the lead rule with its title at display size and a 1:1 lifecycle field beneath | 2 · 1 | 126 |
| `ENG-S10-003` | Structured / Visual Modular | 003 Tidal | 3 — the evidence narrative beside a paired composition | dot grid behind | A bordered plate: the story as a cell on the band tone with its evidence row on the lead rule, beside the site and lifecycle fields stacked at 3:2 | 2 · 1 | 126 |
| `ENG-S10-004` | Conversion-led | 004 Daybreak | 4 — the panoramic context above the evidence invitation | outline round *Look at the whole picture.* | A 3:1 site field; the story beside a compact 4:3 lifecycle field; the evidence row as a band on the band tone on the lead rule | 2 · 1 | 126 |
| `ENG-S10-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the tall landscape beside an offset statement | margin bar along the display column | A 4:5 site field beside the display column; the story as an offset band on the band tone with a 4:3 lifecycle field inset beside | 2 · 1 | 126 |

## What changed from V1

V1's wide-photo stage, portrait narrative, teal panel, blue invitation, curved landscape and lime statement and the plus-marked disclosure go; the story is V1's kicker as a tracked label with the layers mark, the title as type, the two paragraphs and the evidence disclosure opened as a row with the document mark and its bracketed placeholder in muted ink; the two photographs are labelled empty fields (THE SITE, THE EQUIPMENT). The darkened surfaces are the 003 story cell, the 004 evidence panel and the 005 story band. Copy is V1's throughout; no figure, reduction or saving appears anywhere.

## Verification

- `engcheck.ps1 -Sec S10 -Fields 'Explore sustainability through the decisions|Context|Choices|Evidence|Make the impact clear|Start with the project boundaries|Look for a clear baseline|Explore the evidence|Verified impact statement|Site context|Equipment lifecycle'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term; two fields and one placeholder per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
- Correction (22 September 2026): 004 head widened and its display size reduced so the outlined phrase stays inside its column.
