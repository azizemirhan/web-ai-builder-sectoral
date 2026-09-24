# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S11` — Case Studies · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three case slots, their photograph captions and the context title kept as written, the case titles, anonymised descriptions, engagement contexts and editorial note bracketed placeholders, no client, business, period, permission, outcome or coverage named and no result compared; three non-identifying context photographs, never a client — are kept exactly. V1's `<details>` disclosures open as rows.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S11-001` | Universal / Safe | 001 Ivory & Olive | 1 — three open case introductions below landscape context fields | column rules behind the head | Three case cells in a bordered grid with 3:2 context fields, word-numeral chips and opened context rows; the editorial note beneath | 3 · 10 | 203 |
| `FIN-S11-002` | Premium / Editorial | 002 Rosewood | 2 — editorial case rows pairing fields with narrative | bracket above the headline | Three ruled rows on the lead rule with the 3:2 field in a left column and the bracketed title at display size | 3 · 10 | 203 |
| `FIN-S11-003` | Structured / Visual Modular | 003 Lagoon | 3 — the featured case above two complementary engagement stories | registration grid behind | A bordered plate: the first case as a wide cell on the band tone with a 3:2 field beside its title, above two cells with 4:5 fields | 3 · 10 | 203 |
| `FIN-S11-004` | Conversion-led | 004 Iris | 4 — the case narratives anchored by portrait context fields | span mark beneath *a different question.* | Three case rows stacked beside the head rail with 3:2 fields, each context row on the band tone | 3 · 10 | 203 |
| `FIN-S11-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the case sequence with a raised centre story | corner frame along the display column | Three case columns with 4:5 fields, the middle case raised as a panel on the band tone | 3 · 10 | 203 |

## What changed from V1

V1's rounded case cards, editorial rows, featured case, violet narratives and apricot centre and the plus-marked disclosures go; each case is a labelled empty field (THE CONTEXT) with V1's own caption, a word-numeral chip, the bracketed title as type in muted ink, the bracketed anonymised description and the engagement-context disclosure opened as a row with the information mark, with V1's editorial note on a hairline beneath. The darkened surfaces are the 003 first cell, the 004 context rows and the 005 centre panel. Copy is V1's throughout; no client, period or outcome appears anywhere.

## Verification

- `fincheck.ps1 -Sec S11 -AllowClaims 'guarantee' -Fields 'Selected work|The context behind it|Every engagement starts with|a different question|Explore the circumstances and scope|Approved case title A|Anonymised accounting engagement|Approved case title B|Anonymised advisory engagement|Approved case title C|Anonymised insurance engagement|Engagement context|Verified engagement period|Approved editorial note|business context|working context|planning context'` — ALL CHECKS PASS; parity 85/85. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; the only claim-vocabulary hit is *guarantee*, which appears solely inside V1's placeholder as the thing the account must not imply (`-AllowClaims 'guarantee'`); three fields and ten placeholders per study.
- Rendered and read at 1440. No correction needed.
