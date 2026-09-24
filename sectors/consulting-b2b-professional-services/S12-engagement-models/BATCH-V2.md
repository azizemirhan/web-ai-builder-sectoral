# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S12` — Engagement Models · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — every fee model pays the firm to do something, so each is stated with what it pays them to do; outcome-based fees declined and said so; no price, currency, day rate, percentage, ROI multiple or tier; the retainer cap as a placeholder demo value; the media counts per study (1, 0, 0, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S12-001` | Universal / Safe | 001 Paper & Indigo | 3 with 7's labelled captions | ghost word-numeral *Four* behind the head | Four models as a bordered row with stroke marks (document / clock / calendar / chair), SUITS and PAYS US TO as labelled fields with the incentive on the accent edge; 3:2 field of the weekly meeting beside the declined model on a `--no` rule with a struck-seal mark; closing line with one action | 1 × 3:2 · 1 | 229 |
| `CONS-S12-002` | Premium / Editorial | 002 Sable & Bronze | 2 as an editorial run | pencil ellipse round *something* | Four models two to a row on hairlines with serif word-numerals, SUITS as a line and PAYS US TO closing each in the accent's italic; the declined model as a band with a red rule | none · 1 | 194 |
| `CONS-S12-003` | Structured / Visual Modular | 003 Field & Emerald | 3 as two declared blocks | ruled margin behind | WE CARRY THE TIMING RISK — one model on the band tone behind the accent edge — beside YOU CARRY IT — three models as cells sharing hairlines; V1's observation on a hairline with a pencil mark; the declined model as a foot cell on a red rule | none · 1 | 196 |
| `CONS-S12-004` | Conversion-led | 004 White & Signal | 4 with 3 — declined first | underline stroke under *will not sell you* | V1's filled declined panel as a band on the tinted paper behind a `--no` rule; four models in a bordered row; the weekly-meeting field beside V1's closing line and the one action DESCRIBE YOUR SITUATION | 1 × 3:2 · 1 | 192 |
| `CONS-S12-005` | Art-directed / Distinctive | 005 Chalk & Violet | the incentive as display type | bracket grouping the head | Four blocks on hairlines with *Finish early. / Take longer. / Still be here. / Be agreeable.* in the serif italic at display scale and the model as the small tracked label; the field beside the declined model on a red edge with V1's closing sentence. The near-black ground becomes chalk | 1 × 3:2 · 1 | 188 |

## What changed from V1

PAYS US TO is one device across the batch — the accent edge, or the accent's italic — and the declined model one refusal — the deep-red rule with the struck-seal mark. Numerals in `002` become word-numerals; cards, tier-like panels and the dark 005 ground go. Copy is V1's throughout; the retainer cap keeps its placeholder.

## Verification

- `cslcheck.ps1 -Sec S12 -Fields 'Fixed fee|Time and materials|Retainer|Secondment|Outcome-based fees|Pays us to'` — ALL CHECKS PASS; parity 30/30; one placeholder per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit, price, percentage or tier.
- Rendered and read at 1440. No corrections needed.
