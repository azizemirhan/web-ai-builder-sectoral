# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S09` — Client Testimonials · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a quote you cannot check is an advertisement, so every quote carries its situation, its stage and what the reader may do about it; the three check states; quote sentences and the reference-call count as placeholder demo values, marked and declared; nothing identifying attached to any quote; the media counts per study (1, 0, 0, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S09-001` | Universal / Safe | 001 Paper & Indigo | 7 — the quotation panel | ghost serif opening quote behind the head | One feature quote in the serif italic on the band tone with the pencil rule and a giant quote mark; four compact quotes in a bordered row; check states as marked chips (telephone / person / speech line, the last in `--no`); 4:3 field of the reference room beside the count and the one action | 1 × 4:3 · 6 | 221 |
| `CONS-S09-002` | Premium / Editorial | 002 Sable & Bronze | 2 with the quotes as the composition | pencil ellipse round *check* | Five quotes at display size in the serif italic on hairlines, alternating full and half measure; situation, stage and check-state chips; the reference statement as a band with the pencil rule | none · 6 | 191 |
| `CONS-S09-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a key | ruled margin behind | A bordered key row of the three states with marks; five modules on a six-track bordered grid, each edged in its state's colour (accent / ink / `--no`) — V1's colour system as edges and marks, never fills; band-tone foot cell with the count and the action | none · 6 | 223 |
| `CONS-S09-004` | Conversion-led | 004 White & Signal | 4 as three stacked bands | underline stroke under *ring them* | Three bands by state, deepest first — the call band on the tinted paper with the pencil rule, the count and the one action; the named band between hairlines; the words-only band red-edged; V1's closing sentence as the foot | none · 6 | 226 |
| `CONS-S09-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 with 7 — the display quote crossing the field edge | bracket grouping the head | A tall 4:5 field with the first quote at display scale beginning over its edge; four ruled quotes graded in size by permission — the words-only quote smallest and muted; ruled foot with the count and V1's closing sentence. The near-black ground becomes chalk | 1 × 4:5 · 6 | 202 |

## What changed from V1

The three check states are one system across the batch — telephone (accent), person (ink), speech line (`--no`) — as chips, edges or labels; quotes stay unattributed placeholder sentences inside `<blockquote data-placeholder>`, and the count is a placeholder span. "Stage 02" and the like are written "stage two" (no-digit rule) in every study, including inside the placeholder quote "stop at stage 03". Cards and the dark 005 ground go. No other copy changed.

## Verification

- `cslcheck.ps1 -Sec S09 -Fields 'The first four weeks felt slow|We did not renew|Named privately|Words only|clients have agreed'` — ALL CHECKS PASS; parity 25/25; six placeholders per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element; no attribution of any kind.
- Rendered and read at 1440. No corrections needed.
