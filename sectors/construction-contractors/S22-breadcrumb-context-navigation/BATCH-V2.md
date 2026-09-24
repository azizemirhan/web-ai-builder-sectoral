# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S22` — Breadcrumb / Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a trail shows one path and names the ones it hides; the axis stated; next with its ordering declared; every crumb a page or plainly not a link; no self-link, count or position; every anchor in-page; no button or form; the reserved value reads as the word *Reserved* — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S22-001` | Universal / Safe | 001 Site White & Safety Orange | crumb run + two cells | setting-out grid behind the head | The trail as bordered crumb rectangles at radius 0 joined by hairline connectors, the current page a band-tone chip with a filled square marker and no link; the axis note beside; ALSO IN as a bordered ledger of iconed rows (crane / calendar / office) with underlined arrow links; NEXT, BY THE SAME SECTOR as a tape-topped cell | 6 slots | 188 |
| `CON-S22-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — note beside a margin ledger | small levelling circle behind the head | Tape-topped crumb run; A NOTE ON THE ARRANGEMENT as a reading column beside a bordered margin ledger of the three memberships with icons and arrow links, ending in the next page on the band tone with the ordering declared | 6 slots | 219 |
| `CON-S22-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — three trails as bordered rows | dimension line with three ticks above the sheet | Three bordered rows with a status chip (IN USE filled / AVAILABLE open / INCOMPLETE deep-red) and the axis, the crumb run, and a note; the year level drawn as a plain muted label with a NO PAGE BEHIND IT chip and no border, visibly not a link; the incomplete row's note red-edged on the band tone; tape-topped next foot | 7 slots | 284 |
| `CON-S22-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — next by what | — (tape edge above the trail) | Tape-topped crumb run with the axis note; NEXT BY WHAT? at headline size with the tape underline; three bordered ordering cells — THE DEFAULT on the band tone with a filled chip, ALSO AVAILABLE with an open chip, the judgement with a deep-red chip — each with an icon and an underlined arrow link to the reserved next page; ruled no-button foot | 5 slots | 327 |
| `CON-S22-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the trail as a sentence | cut-earth hatching down the left margin | One sentence at headline size in tracked uppercase, every reserved membership an underlined arrow link and the page being read a band-tone marked chip; WHY THERE IS NO TRAIL and THE ORDERING, STATED as two bordered cells, the second tape-topped | 6 slots | 248 |

## What changed from V1

Crumbs are the register's bordered rectangles at radius 0 joined by hairline connectors, the current page a band-tone chip with a filled square marker, and every cross-link an underlined link carrying the arrow; the memberships carry a stroke icon each (crane, calendar, office, pin, arrow); statuses and orderings are bordered square chips (filled / open / deep red); a level with no page behind it is a plain label with a red chip. The trail sits in a `<nav>` with an `aria-label` and the current page carries `aria-current`. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S22 -Fields 'Project name|Sector this project sits in|Name of the next project' -AllowNav` — ALL CHECKS PASS; parity 15/15. The allowed element is the trail's own `<nav>`, which is this section's content, not global chrome. No `<h1>`; no header/footer; no button or form; every anchor in-page; no count, position or digit; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`.
- Rendered and read at 1440. Corrections: `005` sentence width moved to `width: min()` (checker rule).
