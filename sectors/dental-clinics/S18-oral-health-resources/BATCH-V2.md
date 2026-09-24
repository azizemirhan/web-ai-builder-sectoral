# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S18` — Oral Health Resources · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the six that work, the three refused, nothing to download and no email to leave, no article card, no date, no author, no brand, the closing line; the media counts per study (2, 0, 6, 1, 3) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S18-001` | Universal / Safe | 001 Chalk | 1 — the six that work as a grid | ring behind the head | WHAT WORKS as a bordered grid of six with word-numeral chips, *Do not smoke* on the lead rule as the largest item; the brush sizes and the brush heads as two 3:2 fields; WHAT WE WILL NOT PUBLISH as a ruled row on the plum rule with struck marks; the ask line; foot | 2 × 3:2 · 0 | 243 |
| `DN-S18-002` | Premium / Editorial | 002 Linen | 2 — one paragraph, set large | arc above the head | The whole of it as one paragraph at large size with the six imperatives in the accent and *That is all of it.* in ink; three notes as a ruled row, WHAT IS MISSING on the plum edge; foot on the lead rule. No field | none · 0 | 140 |
| `DN-S18-003` | Structured / Visual Modular | 003 Slate | 3 — the cupboard, specified | dot grid behind | Six objects as a bordered grid of cells, each a 1:1 field with what it is for and WHO DOES NOT NEED IT as a tracked line — the two for everybody on the lead rule, mouthwash on the plum rule; THREE THAT ARE NOT IN THE CUPBOARD as a ruled row; the ask line; foot | 6 × 1:1 · 0 | 211 |
| `DN-S18-004` | Conversion-led | 004 Daylight | 4 — the refusal first | bar under *to download* | THE GUIDE, THE NEWSLETTER, THE SIGNUP as a band at display size with the explanation on the plum edge; the contents of the guide we did not write as a ruled grid of six with tick marks; the written summary as a 3:1 field; the no-whitening line on the plum edge; foot on the lead rule | 1 × 3:1 · 0 | 215 |
| `DN-S18-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — a bench, actual size | corner marks framing the head | Three fields of different proportion — 3:1, 1:1, 3:2 — standing on one ink baseline, each labelled ACTUAL SIZE with V1's caption beneath; THE PART THAT DOES NOT PHOTOGRAPH as a ruled row; the twenty-years line with the refusals in the plum; foot on the lead rule | 3:1 + 1:1 + 3:2 · 0 | 194 |

## What changed from V1

The three refusals — whitening, the products, anything monthly — carry the refusal token in every study: plum rule, plum edge, plum sentence or the plum WHO DOES NOT NEED IT line. No article card, thumbnail, date, byline, read-more or email field anywhere; the 003 cupboard and the 005 bench are object fields, never a mouth. The only darkened surface is the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S18 -Fields 'twenty years|fluoride|Spit, do not rinse|between the teeth|how often, not how much|smok|bleed|hitening|download|email|in writing|monthly'` — ALL CHECKS PASS; parity 60/60. No `<h1>`; no header/nav/footer; no form; no link; no input; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no brand or claim term.
- Rendered and read at 1440. One correction: the 002 paragraph and the 004 no-whitening line paired `max-width` with a rule and tripped the boxed-callout check — both set to `width: min(100%, …)`.
