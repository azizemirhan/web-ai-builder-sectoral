# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S03` — Projects · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the picture is the point; sector, scope + marker, status and constraint real; project and client names reserved; no value, area, duration, date, award or rating — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S03-001` | Universal / Safe | 001 Site White & Safety Orange | 1 — column and grid | north point behind the head | Head split; six 3:2 fields under a tape rule, each with a status chip (open square completed, filled square on site) and a ruled record — sector, marker icon, constraint, PROJECT reserved slot; no-values line on the foot rule with a tape-measure icon | 6 fields, 6 slots | 136 |
| `CON-S03-002` | Premium / Editorial | 002 Bone & Burnt Amber | 2 + 10 — head split, offset record tab | dimension line with running ticks under the lead | 21:9 lead field with tape; its record (sector, delivery, reserved name) as a bordered tab hanging from the field's bottom rule beside the constraint paragraph; ruled three-up of 4:3 fields with one-line records and slots | 4 fields, 4 slots | 97 |
| `CON-S03-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 6 — ruled sheet, sector at display size in the margin | cut-earth hatching down the left margin | Four ruled sector rows (first under tape): sector at display size + one-line constraint in the margin, two 16:10 fields across with status chips and ruled records (marker icon, scope, slot) | 8 fields, 8 slots | 152 |
| `CON-S03-004` | Conversion-led | 004 White & Hi-Vis | 5 — panel crossing the media edge | chevron run behind the foot | Display with hi-vis tape underline; 21:9 field with tape and a bordered constraint panel over its lower-right corner carrying sector, marker, constraint, slot and one action; ruled four-up of 3:2 sector fields with underlined ↗ routes; no-values line | 5 fields, 1 slot | 102 |
| `CON-S03-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 5 ×4 — staggered plates, sector crossing the edge | cutting-plane line with section arrows down the centre | Four stagger rows alternating 21:9 and 1:1 plates left and right, the sector at display size on a paper plate crossing each field's edge, a ruled note beside each with index, status chip, constraint and slot; closing line on the foot rule | 4 fields, 4 slots | 210 |

## What changed from V1

The charcoal ground of `005`, the floating white card of `004` and the marginal-label rows are re-cut in the register: paper, hairlines, one tape bar, tracked uppercase, bare fields with tracked labels, the status as a square chip on a paper plate, and the marker as a stroke icon. Copy is V1's throughout; `002` gains a one-line lead so its head split has a right-hand column.

## Verification

- `concheck.ps1 -Sec S03 -Fields 'The work|Healthcare|Project name'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels and indices; no claim from the CON list.
- Rendered and read at 1440. Corrections: `003` "Health&shy;care" broke parity (removed); `005` tall plates 4:5 → 1:1 at 30rem (the stack ran to 2900px).
