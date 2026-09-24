# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S19` — Consultation & Proposal · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the contents page printed before the proposal exists; the six sections in V1's words; the hour is not called free, no *no obligation*, no turnaround promise, no form, wizard or booking widget; the page count and the decline ratio as placeholder demo values; the media counts per study (1, 0, 1, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S19-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered grid | ghost pilcrow behind the head | 21:9 field of the proposal with the placeholder page count as its caption; the six sections as bordered cells on three columns, word-numerals in the accent italic; WHAT THE CONVERSATION COSTS as a band of three fields, the third on a `--no` edge | 1 × 21:9 · 2 | 225 |
| `CONS-S19-002` | Premium / Editorial | 002 Sable & Bronze | 2 as a contents page | pencil ellipse round *contents* | The page count in the voice line; six ruled contents lines on two columns in DOM order (column flow), the word-numeral leading each; band of the three costs. No field, by V1's argument | none · 2 | 199 |
| `CONS-S19-003` | Structured / Visual Modular | 003 Field & Emerald | 3 sorted by rarity | ruled margin behind | Mast line; sections Five and Six as a wide bordered pair on the band tone with the pencil rule and a RARE chip; the four usual ones as a bordered row; 21:9 field beside the page count; ruled foot of the three costs | 1 × 21:9 · 2 | 221 |
| `CONS-S19-004` | Conversion-led | 004 White & Signal | 4 — the terms before the pitch | underline stroke under *before the pitch* | The costs as a band with the pencil rule beside the field of the proposal stretched to its height; WHAT IS IN IT, IN ORDER as a ruled contents list on three columns with the page count in its mast; one closing line and the bordered action ASK FOR THE HOUR with a clock mark | 1 · 2 | 188 |
| `CONS-S19-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — one uniform set | bracket grouping the head | Six section names as ruled lines at display size, numerals in the muted tone; only the last breaks the set — the pencil rule above it, numeral and name in the accent italic, V1's THIS IS THE ONE as a chip; the three costs as a ruled foot | none · 2 | 198 |

## What changed from V1

The section numbers `01`–`06` become the serif word-numerals *One*–*Six* in the accent italic in every study, so the batch carries no digit outside a placeholder. The document, where it is shown, is a bare wide field labelled THE PROPOSAL; the third cost is on the `--no` edge everywhere because it can end in a no. Cards and filled strips go; the pair in 003 and the band in 004 are the paper darkened. Copy is V1's throughout; the page count and decline ratio keep their placeholder marking.

## Verification

- `cslcheck.ps1 -Sec S19 -Fields 'The decision|The stages|The people|The fee model|What we would not do|What would make us wrong|One hour of yours|Nothing else|It can end in a no from us|pages'` — ALL CHECKS PASS; parity 50/50. Two placeholders per study, declared. No `<h1>`; no header/nav/footer; no form, input, wizard or calendar; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no *free*, *no obligation* or turnaround line.
- Rendered and read at 1440. Corrections: the proposal fields in 001 and 003 widened from 16:9 to 21:9 so the plate does not outrun its caption column; the ghost pilcrow lowered clear of the top edge.
