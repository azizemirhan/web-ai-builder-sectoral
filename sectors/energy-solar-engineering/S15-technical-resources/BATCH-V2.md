# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S15` — Technical Resources · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three resource slots (planning guide, system reference, care handbook) kept as written, the title, summary and resource information of each a bracketed placeholder, no publisher, revision, format, size, source or destination named, no download offered; three reserved cover images, never a person — are kept exactly. V1's bracketed titles now carry `data-placeholder="true"`; V1's numerals become word-numeral chips; V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S12 grammar with 3:4 covers labelled THE COVER.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S15-001` | Universal / Safe | 001 Sunlit | 1 — three resource cards with generous cover reservations | arc behind the head | Split head with the lead; three resource cells in a bordered grid with 3:4 covers, word-numeral chips, bracketed titles and summaries and opened resource rows | 3 · 9 | 183 |
| `ENG-S15-002` | Premium / Editorial | 002 Terracotta | 2 — editorial resource rows pairing compact covers with open summaries | rise above the head | Three ruled rows on the lead rule with a compact 3:4 cover in a left column, the bracketed title at display size and the opened resource row | 3 · 9 | 183 |
| `ENG-S15-003` | Structured / Visual Modular | 003 Tidal | 3 — the featured resource beside two compact modules | dot grid behind | A bordered plate: the planning guide as a tall cell on the band tone with its 3:4 cover and its row on the lead rule, the two other resources stacked beside with compact covers | 3 · 9 | 183 |
| `ENG-S15-004` | Conversion-led | 004 Daybreak | 4 — the wide introduction above accented cover cards | outline round *Start with the right resource.* | Three ruled resource columns on the lead rule with 3:4 covers, each resource row on the band tone | 3 · 9 | 183 |
| `ENG-S15-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the collection with staggered covers and a central card | margin bar along the display column | Three staggered resource columns with 3:4 covers, the system reference dropped as a card on the band tone, the first on the lead rule | 3 · 9 | 183 |

## What changed from V1

V1's warm cards, editorial rows, teal feature, blue-accented cards, dark collection with the lime centre and the plus-marked disclosures go; each resource slot is a labelled empty cover field (THE COVER · 3:4), a word-numeral chip, the bracketed title and summary in muted ink and the resource disclosure opened as a row with the document mark and its bracketed placeholder. The darkened surfaces are the 003 featured cell, the 004 resource rows and the 005 central card. Copy is V1's throughout; no publisher, revision, format or destination appears anywhere and nothing is offered for download.

## Verification

- `engcheck.ps1 -Sec S15 -Fields 'Explore guidance for planning|Planning guide title|Approved guide summary|Verified publisher, revision date|System reference title|Approved reference summary|Verified manufacturer, model applicability|Care handbook title|Approved handbook summary|Verified publisher, covered equipment|View resource information|Planning guide|System reference|Care handbook'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term; three fields and nine placeholders per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): 004 head widened and its display size reduced so the outlined phrase stays inside its column.
