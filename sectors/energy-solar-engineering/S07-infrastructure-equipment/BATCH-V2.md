# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S07` — Infrastructure & Equipment · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — kicker, title and two paragraphs kept as written, the readiness detail a bracketed placeholder, no equipment, availability, access arrangement or maintenance responsibility named; two reserved photographs of infrastructure and equipment, never a person — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S04 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S07-001` | Universal / Safe | 001 Sunlit | 1 — the large infrastructure view beside the readiness story | arc behind the head | Split head with the lead; a 4:3 infrastructure field on the lead rule beside the story, with a 1:1 equipment crop beneath the story | 2 · 1 | 116 |
| `ENG-S07-002` | Premium / Editorial | 002 Terracotta | 2 — the panoramic field with a caption-level narrative | rise above the head | A 3:1 infrastructure field on the lead rule; a three-column editorial row — display title, narrative with the readiness row, 1:1 equipment crop | 2 · 1 | 116 |
| `ENG-S07-003` | Structured / Visual Modular | 003 Tidal | 3 — the asymmetric diptych above the readiness plate | dot grid behind | A bordered plate: 3:2 and 1:1 fields as a diptych above the story as a full-width cell on the band tone, its readiness row on the lead rule | 2 · 1 | 116 |
| `ENG-S07-004` | Conversion-led | 004 Daybreak | 4 — the readiness-led narrative beside two offset fields | outline round *Room to work well.* | The story with its readiness row as a band on the lead rule, beside the infrastructure and equipment fields offset at 4:3 | 2 · 1 | 116 |
| `ENG-S07-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the wide field above an offset story | margin bar along the display column | A 3:1 infrastructure field across the width; the story as an offset band on the band tone with a 4:3 equipment field beside | 2 · 1 | 116 |

## What changed from V1

V1's large-view stage, panoramic caption narrative, diptych and readiness panel, blue narrative panel, sculpted image and lime story and the plus-marked disclosure go; the story is V1's kicker as a tracked label with the layers mark, the title as type, the two paragraphs and the readiness disclosure opened as a row with the document mark and its bracketed placeholder in muted ink; the two photographs are labelled empty fields (THE SITE, THE EQUIPMENT). The darkened surfaces are the 003 story cell, the 004 readiness panel and the 005 story band. Copy is V1's throughout.

## Verification

- `engcheck.ps1 -Sec S07 -Fields 'Look at the spaces and equipment|Space|Access|Equipment|The setting matters|Consider where equipment belongs|Review installation space|Explore equipment readiness|Verified infrastructure, equipment availability|Site infrastructure|Equipment context'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term; two fields and one placeholder per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
