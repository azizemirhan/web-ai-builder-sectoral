# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S04` — Industries & Markets · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — naming an industry is not knowing it, so each market is stated as what it constrains; generic vocabulary; the constraints are structural facts, not claims about any client; the media counts and shapes per study (B, C, B, C, B) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S04-001` | Universal / Safe | 001 Paper & Indigo | 1 — field left, ruled list right | ghost serif pilcrow behind the head | Head split with the pencil rule and the italic *knowing*; a tall 3:4 field held left and sticky, in a figure with a house-mark caption; six ruled rows with serif italic word-numerals, serif titles and the constraint phrase in ink; ruled foot with the question and one action | 1 × 3:4 | 151 |
| `CONS-S04-002` | Premium / Editorial | 002 Sable & Bronze | 2 with 6 — head split, pull plate | pencil ellipse round *knowing* | Serif display and italic standfirst at the baseline; six blocks on two columns with air, word-numerals; V1's saturated pull block as a band-tone plate with the pencil rule between the second and third block; underlined route | none | 137 |
| `CONS-S04-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — bordered bento | ruled margin behind the grid | Four-column bento of cells sharing hairlines: financial services 2×2 with a large field, energy 2×1 with a 4:1 strip, healthcare and retail 1×1, industrials and public 2×1; band-tone foot cell with the question and one action | 1 × large + 1 × 4:1 | 131 |
| `CONS-S04-004` | Conversion-led | 004 White & Signal | 4 with 3 — band, bordered grid | underline stroke under *headline* | V1's saturated challenge panel as a band on the tinted paper with the pencil rule and the one action CORRECT US; six cells sharing hairlines with the constraint as the serif headline and the sector as a bordered chip beneath, two cells on the band tone where V1 filled two | none | 115 |
| `CONS-S04-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 with 8 — type crossing the field edge | bracket grouping the set | Oversized serif line whose last word crosses the top edge of a full-width 12:5 field; six markets on two ruled rows of three with word-numerals; bordered action. V1's near-black ground becomes chalk | 1 × 12:5 | 137 |

## What changed from V1

Numerals `01–06` become serif italic word-numerals; saturated panels and tiles become the band tone and hairline cells; the 005 dark ground goes. The bento in `003` is drawn as one bordered grid rather than tiles with corners; its cell sizes are the design layer's (2×2, three 2×1, two 1×1 against V1's 2×2, two 2×1, three 1×1) and the six markets and their order are V1's. Copy is V1's throughout; word counts equal V1's. Slates read `AT WORK` — one market's people at work, never a skyline.

## Verification

- `cslcheck.ps1 -Sec S04 -Fields '<six market names>'` — ALL CHECKS PASS; parity 30/30. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit; no claims vocabulary.
- Rendered and read at 1440. Corrections: `003` foot cell released from the bento's row minimum; `005` word-numeral column widened for *Three*.
