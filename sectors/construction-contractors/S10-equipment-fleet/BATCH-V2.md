# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S10` — Equipment & Fleet · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — organised by the site constraint, not the machine; who operates it, what happens when it fails, when it is the wrong answer; counts reserved; no make, model, weight, reach, tonnage, hours, value or rating; machines in use, never at rest — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S10-001` | Universal / Safe | 001 Site White & Safety Orange | 3 — bordered cells | setting-out grid behind the head | 3:1 plant field under a tape rule; six bordered THE SITE SAYS cells with constraint icons (gate, mats, clock, party wall, road, height), plant as bordered tags and ruled SO WE BRING / WHO IS IN IT / WHEN IT FAILS / WHEN WE SAY NO rows; 3:1 site field; four-cell held row with holding chips and reserved counts; bordered refusal note | 2 fields, 4 slots | 871 |
| `CON-S10-002` | Premium / Editorial | 002 Bone & Burnt Amber | 9 — broadsheet chapters | levelling circle behind the proposition | Display and lead; 21:9 plant field with tape; the argument as two columns of iconed ruled chapters with one tape-edged pull; HELD, AND HOW as a four-cell row under a tape rule; refusal foot line | 1 field, 4 slots | 740 |
| `CON-S10-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 4 — tier bands with drawn gates | dimension line with running ticks behind the head | 3:1 plant field; four alternating tier bands, each headed by an inline drawn gate whose gap widens tier by tier (no dimension on it) beside the tier at display size, with bordered machine cells carrying ANSWERS and reserved HELD counts, tier four's cells the not-ours answer with cone icons; bordered refusal note | 1 field, 10 slots | 550 |
| `CON-S10-004` | Conversion-led | 004 White & Hi-Vis | 6 + 4 — indexed rows, tinted band | chevron run behind the band | Display with tape underline; three ruled photograph rows with accent index, constraint icon and tape-edged WHAT IT ANSWERS; 3:1 plant field; YOU WILL GET A TIER BACK as a hi-vis band with one bordered action and WHAT A PHOTOGRAPH WILL NOT TELL US beside it; four-cell held row; bordered refusal note | 1 field, 4 slots | 554 |
| `CON-S10-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — photo-essay chapters | cut-earth hatching down the left margin | Four ruled chapters with a 3:2 field swapping sides and the site condition in tracked uppercase at display size, SO WE BRING on a tape edge, the note and the machines as caption-size bordered tags; four-cell held row with the not-held line; bordered refusal note | 4 fields, 4 slots | 558 |

## What changed from V1

The card grid, the drawn gates of V1's own colour language and the photo-essay's dark captions are re-cut in the register; the gate figure of `003` is now an inline construction drawing at `--line-strong` with no measurement on it, as the section's rule requires, and every constraint carries a stroke icon from the CON set. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S10 -Fields 'The plant|specification'` — ALL CHECKS PASS; parity 10/10 (`003` carries the ten per-machine counts rather than the four-family row, as V1 did). No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels and indices; no make, model or specification figure anywhere.
- Rendered and read at 1440. No correction needed.
