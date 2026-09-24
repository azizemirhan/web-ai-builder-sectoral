# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S04` — Sectors Served · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the constraint, not the category; media secondary (three studies carry none); the wrong-firm line; no client, logo, framework, count, share, certification or award — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S04-001` | Universal / Safe | 001 Site White & Safety Orange | 4 — tinted panels | setting-out grid behind everything | Head split; six band-toned panels in a 3 × 2 grid with hairline gutters under a tape rule, each with a sector stroke icon at 2rem, THE CONSTRAINT and a SO line on a 3px tape edge; WHERE WE ARE THE WRONG FIRM as a bordered paper note across the foot | none | 347 |
| `CON-S04-002` | Premium / Editorial | 002 Bone & Burnt Amber | 9 — chapter pacing | levelling circle behind the proposition | Proposition at display size; four ruled passages with icon + sector standing in the margin, the constraint set large and WHAT THAT CHANGES indented on a tape edge; one 21:9 field on a tape rule | 1 field | 246 |
| `CON-S04-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — bordered cells | dimension line with end ticks behind the head | Head split; 3 × 2 bordered sheet, each cell with icon, name and three ruled question rows, USUALLY NEEDS as bordered service tags with the S02 marker icon; no-counts line on the foot rule | none | 328 |
| `CON-S04-004` | Conversion-led | 004 White & Hi-Vis | 10 — opened panel beside a field | cut-earth hatching down the right margin | Display with tape underline; one opened sector as a bordered tape-topped panel with icon at 3rem, two ruled questions, one bordered action and the wrong-firm line, beside a 1:1 field; five ruled sector rows with icons and underlined OPEN ↗ routes | 1 field | 141 |
| `CON-S04-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 6 — ruled rows at display scale | brick coursing down the right margin | Head split; six ruled rows with the constraint in tracked uppercase at display size, the sector as a small bordered iconed tag in the margin, the SO line muted; wrong-firm line on the foot rule | none | 280 |

## What changed from V1

The colour halves, coloured rules, colour spines and tall colour columns of V1 are gone; the sector is carried by a stroke-icon set (cross, mortar board, factory, shop front, portico, house) at the register's small accent, and structure by hairlines, bordered cells and one tape bar. Copy is V1's word for word; the word counts above equal V1's (`001`, `003` and `005` were already over the 250 ceiling in V1 and the spine is kept rather than cut).

## Verification

- `concheck.ps1 -Sec S04 -Fields 'Who we build for|Healthcare|Civic'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels; no claim from the CON list.
- Rendered and read at 1440. Corrections: `001` foot note given a paper background so the grid does not run through it; `002` max-width moved off the tape-edged paragraph onto its wrapper (checker rule); `004` field 4:5 → 1:1 to sit level with the panel.
