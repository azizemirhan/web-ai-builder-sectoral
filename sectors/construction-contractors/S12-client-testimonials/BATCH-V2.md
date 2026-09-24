# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S12` — Client Testimonials · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — reserve the quotation, author the apparatus; name, role and organisation reserved; will they take your call / was it edited / were they given anything real; the three groups; the selected-sample admission; the bad-reference offer; no star, score, count or logo — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S12-001` | Universal / Safe | 001 Site White & Safety Orange | 7 inside 3 — quotation panels as bordered cells | setting-out grid behind the head | 2 × 2 bordered cells under a tape rule, each a reserved quotation block (four hairlines at prose cadence on the band tone behind a giant accent quote mark), sector eyebrow, attribution record and three iconed apparatus lines (phone / badge / cone; clipboard; padlock); WHO IS NOT ON THIS PAGE as a bordered note with muted tags | 4 quotations, 10 slots | 447 |
| `CON-S12-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — one specimen at full width | levelling circle behind the head | One reserved quotation block at full width under the tape rule with a 12rem quote mark; four-cell reserved attribution row; iconed apparatus row; the statement of practice as two columns of iconed ruled chapters, the admission chapter in the display voice under its own tape rule | 1 quotation, 4 slots | 540 |
| `CON-S12-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — bordered columns at 6 / 4 / 2 | dimension line with running ticks behind the head | Three bordered columns sorted by verifiability, each with an iconed head and ruled entries of reserved block, attribution fields and edited / given lines, the widest the most checkable; WHAT THE WIDTHS ARE TELLING YOU as a bordered note with muted tags | 6 quotations, 16 slots | 418 |
| `CON-S12-004` | Conversion-led | 004 White & Hi-Vis | 3 + 4 — offer cells, tinted band | chevron run behind the band | Display with tape underline; YOU GET as three bordered iconed cells; the ask as a hi-vis band with one bordered action and WHAT WE WILL NOT DO beside it; the quotations demoted to a ruled three-cell foot strip with small reserved blocks and one-line apparatus; foot line | 3 quotations, 5 slots | 487 |
| `CON-S12-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 7 — broadside blocks with margin footnotes | cut-earth hatching down the left margin | Three ruled rows with a broadside reserved block behind a 10rem quote mark and the attribution and apparatus as margin footnotes; THESE ARE THE CLIENTS WHO AGREED at display size under a tape rule, larger than any quotation; ruled foot with muted tags and the offer | 3 quotations, 7 slots | 362 |

## What changed from V1

The reserved quotation is now drawn as the register's ruled block — hairlines at prose cadence on the band tone behind an accent quote mark — rather than a dash or an empty card; the apparatus is a stroke-icon set (phone, badge, cone, clipboard, padlock) on hairline rows; the refused devices are muted tags. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S12 -Fields 'What clients said|Given nothing|went badly' -AllowClaims 'stars|rated '` — ALL CHECKS PASS; parity 15/15. The allowed strings are "No stars" in every refusal list and "curated" in `004`'s band, both V1's words. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no quotation text, name or organisation anywhere — every quotation is a reserved block with a visually-hidden label and every attribution a reserved slot.
- Rendered and read at 1440. Corrections: `001` slot width moved to `width: min()` (checker rule).
