# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S23` — Service / Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the same page S21 and S22 render, with the plain `data-region="page-context"` block (trail and the one `<h1>`) kept as the assembly stand-in; *What it costs you* at the weight of the stages or above; the four stages, the two limits, the fee model, the two adjacent pages and one route out; no fabricated pricing, guarantee, turnaround or availability; the interview range, the ninety days and the adjacent page names as placeholder demo values; the media counts per study (1, 0, 1, 0, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S23-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered rows | ghost `&` behind the description | Description at full measure; HOW IT RUNS as a bordered row of four with word-numerals; WHAT IT COSTS YOU as a band with the pencil rule; two limit fields, the second on `--no`; foot with the ask as an underlined link, the fee and adjacent pages beside the 3:2 portrait field | 1 × 3:2 · 5 | 218 |
| `CONS-S23-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one measure | pencil ellipse round *room* | Description at display size; four ruled stage lines, the stage as one sentence; three ruled cost lines at the same weight; two limit lines; the close with fee, adjacent pages and the ask | none · 5 | 212 |
| `CONS-S23-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — body and rail | ruled margin behind | Body column: description, 21:9 field, four bordered stage cells with V1's timing lines as tracked captions, the ask; supporting rail on the band tone with the pencil rule — costs, limits with the fee, NEARBY | 1 × 21:9 · 5 | 233 |
| `CONS-S23-004` | Conversion-led | 004 White & Signal | 4 — the bill before the brochure | underline stroke under *what it costs you* | Description beside the title; the costs as the first band with the pencil rule; stages as a bordered row with STAGE ONE… chips; two limits; the close with the fee, adjacent pages and the ask as a bordered rectangle with a clock mark | none · 5 | 212 |
| `CONS-S23-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — the page written twice | bracket grouping *what you do* | WHAT WE DO as compact dim ruled lines; WHAT YOU DO bracketed, the three costs as the largest type on the page under the pencil rule; limits as a ruled row; close | none · 5 | 208 |

## What changed from V1

The stage numbers `01`–`04` become the serif word-numerals *One*–*Four* (or STAGE ONE… chips in 004), so no digit sits outside a placeholder; the costs carry the same labelled-field form in every study; *When it will not work* is on the `--no` edge throughout; fields are bare and labelled. Filled panels and cards go; the darkened surfaces are the 001 and 004 bands and the 003 rail. Copy is V1's throughout; the five placeholders keep their marking. The page-context region is unchanged in content and kept deliberately plain.

## Verification

- `cslcheck.ps1 -Sec S23 -Fields 'Operating model redesign|Decision map|Where it breaks|Redesign|days|Your COO|interviews|One decision you have already made|Not included|When it will not work|Fixed fee|Cost structure|Post-merger integration|Ask for the hour'` — ALL CHECKS PASS; parity 70/70. Five placeholders per study, declared. One `<h1>` per study inside the page-context region, as V1 and the section's page role require (the checker's detail-page list extended to S23–S27 for this); no header, nav or footer element; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no pricing, guarantee or turnaround.
- Rendered and read at 1440. One correction: 005's compact stage lines rebuilt with the heading beside the sentence in a wrapper, not inside the paragraph.
