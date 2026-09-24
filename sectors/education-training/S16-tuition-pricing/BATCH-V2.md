# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S16` — Tuition & Fees · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one programme tuition whose name, amount, currency, basis, four cost facts and payment and cancellation lines are bracketed placeholders, fees declared awaiting institutional confirmation, no payment or enrolment control, V1's refusal line kept in full, one route to the same-variant programme list; no media in any study — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing. No figure or currency is introduced: the amount is V1's bracketed [Amount]. The five compositions carry the S11/S14 record devices.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S16-001` | Universal / Safe | 001 Apricot | 1 — the fee panel beside an introduction | loop behind the head | Split head with the lead; the tuition as a bordered plate — fee cell with the amount at display size in the accent, four labelled cells with the tick, plus, person and calendar marks, the opened payment and cancellation rows as the foot on the band tone; the action and the fee refusal as a graphite chip with its line on the lead rule | none · 11 | 137 |
| `EDU-S16-002` | Premium / Editorial | 002 Mulberry | 2 — the amount above an open breakdown | rise above the head | The fee at display size on the lead rule; four ruled labelled columns; the opened payment and cancellation rows; the action and the refusal on the closing hairline | none · 11 | 137 |
| `EDU-S16-003` | Structured / Visual Modular | 003 Cobalt | 3 — the fee cell beside grouped context | cross grid behind | A bordered plate with the tuition as a cell on the band tone beside four labelled rows and the opened payment and cancellation rows; the action and the refusal on the lead rule | none · 11 | 137 |
| `EDU-S16-004` | Conversion-led | 004 Iris | 4 — the spotlight joined to payment information | outline round *Understand the cost.* | V1's spotlight as a band holding the lead, the refusal and the action on the lead rule; the tuition beside it as ruled rows | none · 11 | 137 |
| `EDU-S16-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the oversized amount beside the terms | margin bar along the display column | Display column with the lead and the amount at the largest size in the accent, where V1 set its lime figure; the labelled rows, the opened payment and cancellation rows, the refusal and the action in the wide column | none · 11 | 137 |

## What changed from V1

V1's fee cards, the blue, purple and lime panels and the plus-marked disclosures go; the tuition is bare type on hairlines or ink seams — the programme name in muted ink as a placeholder, the bracketed amount and currency at display size in the accent, the basis muted, Included in tuition, Additional costs, Fee category and Valid for as tracked labels with marks, Payment details and Changes & cancellations opened as rows. FEES AWAITING INSTITUTIONAL CONFIRMATION is a graphite chip — the sector's `--no` — above V1's refusal line in semibold ink; no payment control is drawn. The darkened surfaces are the 001 plate foot, the 003 fee cell and the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S16 -Fields 'See the tuition in context|Programme tuition|Programme name|Amount|Currency|Per term, year or full programme|Included in tuition|Additional costs|Fee category|Valid for|Fees awaiting institutional confirmation|Confirm the full cost|Payment details|Deposit, payment dates|Accepted payment methods|cancellations|withdrawal, refund|Explore programmes'` — ALL CHECKS PASS; parity 90/90. No `<h1>`; no header/nav/footer; no form, button or payment control; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy — no figure anywhere; no claim term; eleven placeholders per study.
- Rendered and read at 1440. Correction: a hairline set between the two opened disclosure rows.
