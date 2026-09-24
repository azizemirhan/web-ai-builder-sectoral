# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S09` — Certifications & Standards · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three credential groups kept as written, the description and evidence of each a bracketed placeholder, no certification, standard, qualification, issuing body, reference, date or status named, nothing presented as certified or accredited; no media in any study — are kept exactly. V1's numerals become word-numeral chips; V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S05 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S09-001` | Universal / Safe | 001 Sunlit | 1 — three open credential summaries | arc behind the head | Split head with the lead; three credential cells in a bordered grid with word-numeral chips, bracketed descriptions and opened evidence rows | none · 6 | 149 |
| `ENG-S09-002` | Premium / Editorial | 002 Terracotta | 2 — editorial credential rows beneath a split introduction | rise above the head | Three ruled rows on the lead rule with the chip column, the title at display size, the bracketed description and the opened evidence row | none · 6 | 149 |
| `ENG-S09-003` | Structured / Visual Modular | 003 Tidal | 3 — the featured certification beside two supporting groups | dot grid behind | A bordered plate: Certifications as a tall cell on the band tone with its row on the lead rule, the two other groups stacked beside | none · 6 | 149 |
| `ENG-S09-004` | Conversion-led | 004 Daybreak | 4 — the evidence-first stack beside a concise introduction | outline round *with clarity.* | Narrow head column with the lead beneath; three credential rows stacked beside on the lead rule, led by word numerals with marks, each evidence row on the band tone | none · 6 | 149 |
| `ENG-S09-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — asymmetric columns with a central emphasis | margin bar along the display column | Three credential columns of unequal width, Applicable standards wider on the band tone with its row on the lead rule | none · 6 | 149 |

## What changed from V1

V1's numbered credential summaries, editorial rows, featured panel, evidence stack, dark columns with lime emphasis and plus-marked disclosures go; each credential group is a word-numeral chip (or word numeral with its mark in 004), the title as type, the bracketed description in muted ink and the evidence disclosure opened as a row with the document mark and its bracketed placeholder. The darkened surfaces are the 003 certification cell, the 004 evidence rows and the 005 middle column. Copy is V1's throughout; nothing is presented as certified, accredited or verified.

## Verification

- `engcheck.ps1 -Sec S09 -Fields 'Look at the scope behind a credential|Certifications|Verified certification name|Certificate reference|Applicable standards|Confirmed standard and edition|Applicable requirements|Professional qualifications|Verified qualification or authorisation|Named holder or authorised entity|View evidence details'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term ("certified by" / "accredited by" absent — V1's placeholders name no issuer); six placeholders per study.
- Rendered and read at 1440. No correction needed.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
