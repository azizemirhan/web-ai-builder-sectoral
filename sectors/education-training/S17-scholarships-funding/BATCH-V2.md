# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S17` — Scholarships & Funding · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one funding opportunity whose name, purpose, coverage, eligibility, deadline, duration and application and condition lines are bracketed placeholders, funding details declared awaiting confirmation, V1's line that eligibility does not guarantee an award kept verbatim, no application control, one route to the same-variant programme list; the media counts per study (1, 1, 0, 0, 1) — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. The five compositions carry the S11/S14/S16 record devices.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S17-001` | Universal / Safe | 001 Apricot | 1 — the field beside an open overview | loop behind the head | Split head with the lead and a 3:2 field of the shared table beneath it; the opportunity as a bordered plate — name cell, four labelled cells with the tick, person, calendar and clock marks, the opened application and condition rows as the foot on the band tone; the action and the refusal as a graphite chip with its line on the lead rule | 3:2 · 9 | 144 |
| `EDU-S17-002` | Premium / Editorial | 002 Mulberry | 2 — the funding story with a field | rise above the head | Split head with the lead and the 3:2 field beside; the name at display size on the lead rule; four ruled labelled columns; the opened application and condition rows; the action and the refusal on the closing hairline | 3:2 · 9 | 144 |
| `EDU-S17-003` | Structured / Visual Modular | 003 Cobalt | 3 — the title cell beside coverage and eligibility | cross grid behind | A bordered plate with the opportunity as a cell on the band tone, where V1 set its blue coverage field, beside four labelled rows and the opened application and condition rows; the action and the refusal on the lead rule | none · 9 | 135 |
| `EDU-S17-004` | Conversion-led | 004 Iris | 4 — the introduction with prominent application details | outline round *See the possibilities.* | V1's introduction as a band holding the lead, the refusal and the action on the lead rule; the opportunity beside it as ruled rows | none · 9 | 135 |
| `EDU-S17-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the split story with a field and the terms | margin bar along the display column | Display column with the lead, the name at display size in the accent with its purpose and the 3:2 field; the labelled rows, the opened rows, the refusal where V1 set its lime terms, and the action in the wide column | 3:2 · 9 | 144 |

## What changed from V1

V1's opportunity cards, the curved photograph, the blue, purple and lime panels and the plus-marked disclosures go; the opportunity is bare type on hairlines or ink seams — the name in muted ink (or in the accent where V1 made it the display) as a placeholder, Coverage, Eligibility, Apply by and Duration as tracked labels with marks, How to apply and Funding conditions opened as rows. FUNDING DETAILS AWAITING CONFIRMATION is a graphite chip — the sector's `--no` — above V1's refusal line in semibold ink; the field is a bare 8px area labelled THE SHARED TABLE. The darkened surfaces are the 001 plate foot, the 003 name cell and the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S17 -AllowClaims 'guarantee|award' -Fields 'Understand the support that may be available|Funding opportunity|Scholarship or funding name|Provider, support type|Coverage|Eligibility|Apply by|Duration|Funding details awaiting confirmation|does not guarantee an award|How to apply|Required documents, selection process|Decision timeline|Funding conditions|Repayment obligations|Explore programmes'` — ALL CHECKS PASS; parity 80/80. `guarantee` and `award` are allowed only for V1's refusal *Eligibility does not guarantee an award* and its bracketed *[Award period and renewal conditions]* and *rules for combining awards* — negations and placeholders kept verbatim. No `<h1>`; no header/nav/footer; no form or application control; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; nine placeholders per study.
- Rendered and read at 1440. Correction: 002 head aligned to start so the headline sits level with the field.
