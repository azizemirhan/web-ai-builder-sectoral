# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S23` — Service Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the edge is the content; the building envelope as the worked service; in / not in and who does it instead; the seams and who owns each joint; the three failure modes and the hose on the first bay; the four holding markers; no turnkey claim, product, system, standard, guarantee, badge or before-and-after; the retained specialist reserved; anchors in `004` only — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S23-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — seam sheets | setting-out grid behind the head | IN / NOT IN as two bordered cells with iconed square-bulleted lists, the exclusions naming the trade in the accent; four bordered seam sheets with the two sides as iconed chips either end and THE JOINT as the wide accent-edged centre cell with WHO OWNS THE JOINT on the band tone; three bordered failure cells with icons (pen / scaffold / drop) and WHAT WE DO on the band tone; four-marker holding row with the reserved specialist; refusal beside a 3:1 reserved junction photograph | 1 field, 1 slot | 696 |
| `CON-S23-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — a walk up one elevation | levelling staff (vertical datum with ticks) down the left margin with a square node at each stop | Four ruled chapters bottom to top with a height eyebrow and icon, the prose in the centre and WHO OWNS THIS JOINT as an accent-edged bordered cell in the margin; the hose and the refusal on a tape-topped band; NOT OURS as a four-cell ledger with red-edged chips | 1 slot | 647 |
| `CON-S23-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — the joint as a thing | dimension line behind the head and over the sheet at the column widths | Bordered three-column sheet with a column head, the joint as the widest accent-edged centre column and the sides as iconed chips with holding markers (filled / accent / red square), the unowned row on the band tone with its cell red-edged; three bordered failure cells with icons, the refusal and the reserved specialist inline | 1 slot | 564 |
| `CON-S23-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — send the junctions | chevron run behind the ask band | Display with tape underline; hi-vis band with THREE DRAWINGS as a bordered iconed three-cell row, one bordered action and its note; three bordered stage rows with the answer at headline size and one action each; four-cell joint ledger with icons and the reserved specialist; ruled exclusions and refusal foot | 1 slot | 540 |
| `CON-S23-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the rules loud, the parts quiet | cut-earth hatching down the left margin | The elevation as a section of five part bands (paper for ours, band tone for not ours, each with an icon and holding marker) separated by four 3px accent rules carrying the junction at headline size and the owner on a bordered paper plate sitting on the line, the usually-broken rule in deep red; the hose and the refusal as two bordered foot cells | 1 slot | 575 |

## What changed from V1

The joint is drawn with one geometry across the batch — the 3px accent rule or edge, the owner named on it or beside it, the unowned joint in deep red — and each side carries a stroke icon (roof, brick wall, window panes, ground strata, hard hat, penetration) with the `S05` holding markers as filled / open / accent / red squares; the failure modes carry pen, scaffold and water-drop icons; the reserved specialist is a bordered slot reading *Reserved*. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S23 -Fields 'Name of the retained roofing specialist'` — ALL CHECKS PASS; parity 5/5. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit, product, system, standard, guarantee, period or badge; the anchors in `004` only, in-page; no em-dash placeholder.
- Rendered and read at 1440. No corrections needed.
