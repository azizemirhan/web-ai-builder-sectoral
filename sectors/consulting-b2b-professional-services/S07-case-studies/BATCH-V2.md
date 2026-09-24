# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S07` — Case Studies · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — confidentiality: no client name, sector, logo, date or figure that identifies anyone; every case ends on WITHHELD; media only ever the firm's own artefact; outcomes as placeholder demo values, marked and declared; the media counts per study (1, 1, 4, 0, 4) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S07-001` | Universal / Safe | 001 Paper & Indigo | 3 under one wide field | ghost serif dagger behind the head | 21:9 artefact field; four cases in a bordered two-by-two grid — serif word-numeral CASE ONE … FOUR, the situation in the serif, WHAT WE DID / WHAT CHANGED as labelled fields (the outcome on the accent edge) and WITHHELD closing each cell on a deep-red edge with a struck-seal mark; ruled foot with V1's line and one action | 1 × 21:9 · 4 | 227 |
| `CONS-S07-002` | Premium / Editorial | 002 Sable & Bronze | 1 as a spread — sticky standing column | pencil ellipse round *say* | Narrow standing column held left and sticky with the display, the standfirst, the 4:5 artefact field and the underlined route; four ruled cases right with the withheld line in the accent's italic on a red edge | 1 × 4:5 · 4 | 205 |
| `CONS-S07-003` | Structured / Visual Modular | 003 Field & Emerald | 3 as a module system | ruled margin behind | One wide module across the grid with a 3:2 field beside its text, three compact modules with 4:3 fields above theirs, all sharing hairlines; band-tone foot cell with V1's line and the action | 1 × 3:2 + 3 × 4:3 · 4 | 229 |
| `CONS-S07-004` | Conversion-led | 004 White & Signal | 4 with 3 — argument band, inverted cells | underline stroke under *missing* | V1's near-black argument panel as a band on the tinted paper with the pencil rule and a struck-seal mark; four cases inverted in a bordered grid — WITHHELD first as the serif headline on a red edge, then the numeral, the situation and the labelled fields; ruled foot with one action | none · 4 | 221 |
| `CONS-S07-005` | Art-directed / Distinctive | 005 Chalk & Violet | 6 as rows — a banner with a giant index | bracket grouping the head, ghost *One* behind the banner | The first case as a banner with the ghost word-numeral behind its text and a 4:3 field; three rows on hairlines with 3:2 fields; the withheld line red-edged; bordered action. V1's near-black ground becomes chalk | 1 × 4:3 + 3 × 3:2 · 4 | 226 |

## What changed from V1

The withheld line — the section's argument — is drawn one way across the batch: a deep-red (`--no`) edge, in `001` and `004` with the struck-seal mark, in `004` first and largest. `Case 01–04` becomes *Case One … Four* (`005`, which used bare numerals, becomes *One … Four*). Cards, dark panels and the 005 dark ground go; the 005 row fields step from 4:3 to 3:2 after the banner. Outcomes keep V1's placeholder marking. No other copy changed.

## Verification

- `cslcheck.ps1 -Sec S07 -Fields 'What we did|What changed|Withheld|Redrew decision rights|Ask for a reference'` — ALL CHECKS PASS on every rule; parity 23/25, the two absences being V1's own (`002` and `003` do not carry the reference line). Four placeholders per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element.
- Rendered and read at 1440. Corrections: withheld blocks restructured so the mark sits outside the `<dl>` (valid markup); `005` ghost numeral moved behind the text column and the row fields reduced (height 1978 → 1709); `003` compact fields 1:1 → 4:3.
