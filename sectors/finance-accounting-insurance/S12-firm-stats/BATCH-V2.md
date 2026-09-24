# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S12` — Firm Stats · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three metric titles and the definitions title kept as written, the values, definitions, source lines and source notes bracketed placeholders, no year, count, office number, source or review date named and nothing implying service quality or financial performance; no media in any study — are kept exactly. Each value stands as V1's bracketed `[Value]` at display size, never as a counter; V1's numerals become word-numeral chips; V1's `<details>` disclosure opens as a row.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S12-001` | Universal / Safe | 001 Ivory & Olive | 1 — three open firm figures separated by quiet rules | column rules behind the head | Three figure cells in a bordered grid with word-numeral chips, bracketed values at display size, titles, definitions and source lines | none · 10 | 157 |
| `FIN-S12-002` | Premium / Editorial | 002 Rosewood | 2 — the editorial figures aligned with their definitions | bracket above the headline | Three ruled figure rows on the lead rule with the chip column and the bracketed value at display size | none · 10 | 157 |
| `FIN-S12-003` | Structured / Visual Modular | 003 Lagoon | 3 — the firm facts in an asymmetric composition | registration grid behind | A bordered plate with one figure as a tall cell on the band tone, its value in the accent, beside two stacked figure cells | none · 10 | 157 |
| `FIN-S12-004` | Conversion-led | 004 Iris | 4 — the introduction beside a clear vertical fact sequence | span mark beneath *the people behind the work.* | Three figure rows stacked beside the head rail, each definition and source line on the band tone | none · 10 | 157 |
| `FIN-S12-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the typographic figures with a raised central fact | corner frame along the display column | Three figure columns, the middle raised as a panel on the band tone | none · 10 | 157 |

## What changed from V1

V1's olive rules, editorial alignment, asymmetric composition, violet sequence and apricot central fact and the plus-marked disclosure go; each figure is a word-numeral chip with its mark, the bracketed value at display size in ink, the title as type, the bracketed definition in muted ink and the bracketed source line beneath, with V1's definitions disclosure opened as a row with the information mark on a hairline. The darkened surfaces are the 003 first cell, the 004 definitions and the 005 central panel. Copy is V1's throughout; no year, count or figure appears anywhere and no counter runs.

## Verification

- `fincheck.ps1 -Sec S12 -Fields 'The firm|Facts with context|A clearer picture of|the people behind the work|Explore a few facts about the firm|Value|Firm history|Verified establishment year|People in the team|Verified team count|Office presence|Verified office count|Source and reference date|Definitions and source notes|Approved source references'` — ALL CHECKS PASS; parity 75/75. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; ten placeholders per study.
- Rendered and read at 1440. Correction: in 002 every item child other than the chip is held in the content column, so the source line no longer falls under the chip.
