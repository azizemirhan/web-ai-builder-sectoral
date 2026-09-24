# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S11` — Leadership Team · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — role leads, name and portrait reserved inside one `<figure>`, the contact-frequency marker on everybody with the director's "at tender and at handover, and nowhere in between" printed, what each can decide without asking, the site-manager count reserved, no qualification, membership, years or biography — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S11-001` | Universal / Safe | 001 Site White & Safety Orange | 10 inside 3 — figures in bordered cells | setting-out grid behind the head | Four ruled contact groups with iconed marker chips (hard hat, calendar, clipboard, badge); each a row of bordered figure cells — 4:5 portrait field with the reserved name as an offset tab, role, tape-edged DECIDES WITHOUT ASKING, note, ANSWERS TO — single-person groups laid portrait-beside-text; count row; refusal foot | 6 portraits, 7 slots | 680 |
| `CON-S11-002` | Premium / Editorial | 002 Bone & Burnt Amber | 9 — chapters in meeting order | levelling circle behind the head | Display and lead; six ruled chapters each with an iconed moment eyebrow, a 1:1 portrait figure with name tab and the DECIDES line in the margin, the prose beside — the foreman's figure floated into the site-manager chapter; count row; refusal foot | 6 portraits, 7 slots | 795 |
| `CON-S11-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — stage sheet | dimension line with running ticks behind the head | Three-square status legend (filled joins, open still here, struck not in the room); five bordered stage modules with the people as ruled rows carrying status chips and reserved names where they first appear; the ON SITE module on the band tone with the only two portraits; count row; refusal foot | 2 portraits, 7 slots | 612 |
| `CON-S11-004` | Conversion-led | 004 White & Hi-Vis | 10 — one figure beside the ask | chevron run behind the band | Display with tape underline; one 4:5 portrait figure with name tab beside the ask — marker chip, role, the text and one bordered action; A STRAIGHT ANSWER / A POOR ONE as two bordered cells with closed and open padlocks; WHAT WE CAN AND CANNOT PROMISE as a hi-vis band with the reserved count; refusal foot | 1 portrait, 2 slots | 471 |
| `CON-S11-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 8 — gallery scaled by contact | cut-earth hatching down the left margin | Twelve-column gallery under a tape rule: site manager and foreman at six columns with 4:5 figures, contracts, commercial and planner at four with 1:1, the director at three with a small 1:1 beside a nine-column hairline frame holding the note about the room they are not in; every figure with name tab, iconed contact chip and DECIDES line; count row; refusal foot | 6 portraits, 7 slots | 439 |

## What changed from V1

The deep ground of `004` and the contact-scaled blocks of `005` are re-cut on paper; every portrait is the register's bare field with the reserved name as an offset tab on its edge (device 10), every contact marker a stroke-icon chip, and every decision line a tape edge. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S11 -Fields 'The people|Site manager|Name of the site manager'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels; no name, qualification or biography anywhere — each name is a reserved slot inside the same `<figure>` as its portrait.
- Rendered and read at 1440. Corrections: `001` single-person groups laid portrait-beside-text (the stacked cell ran the study past 3200px); `002` the DECIDES paragraph's max-width moved to its column (checker rule); `005` a `.fig p` rule was catching the field label (scoped to direct children) and the portraits capped at 24 / 15 / 9rem so the scale reads without the study running past 2800px.
