# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S06` — Project Delivery Process · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the gates are the content, every gate carries *fixed after this* and *what we need from you*, no duration or date anywhere (omitted, not reserved), no price, client, project name, certification or safety record — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S06-001` | Universal / Safe | 001 Site White & Safety Orange | 6 — ruled sheet with giant index | dimension line with running ticks behind the head | Seven stage rows (index 01–07, phase, name, text) each followed by a bordered tape-topped GATE strip — a vertical GATE tab, FIXED AFTER THIS with a padlock icon, WHAT WE NEED FROM YOU with a clipboard icon; two 3:2 fields inside the walk and on-site rows; no-durations foot line | 2 fields | 802 |
| `CON-S06-002` | Premium / Editorial | 002 Bone & Burnt Amber | 4 — tinted bands as interruptions | levelling circle behind the proposition | Display proposition and lead; 3:1 field; six stages in a 44rem reading column, each cut across by a full-width band-tone gate of two iconed cells under a tape edge; foot lines; closing 3:1 handover field | 2 fields | 787 |
| `CON-S06-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — bordered two-lane sheet | setting-out grid behind the head | 3:1 field; lane heads WHAT WE DO / WHAT YOU OWE BEFORE IT with icons; seven band-toned stage strips each over two lane cells and a tape-topped FIXED AFTER THIS strip spanning both; foot line | 1 field | 743 |
| `CON-S06-004` | Conversion-led | 004 White & Hi-Vis | 10 — dominant panel beside a field | chevron run behind the rail | Display with tape underline; the site walk as a bordered tape-topped panel with an open-padlock tab, text, WHAT WE NEED FROM YOU row and one bordered action, beside a 1:1 field; ruled rail of the five remaining stages with padlock icons and CLOSES lines; foot line | 1 field | 362 |
| `CON-S06-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — staggered chapters | cut-earth hatching down the left margin | Seven stage blocks stepping 3rem further in each time, name at display size, with full-width tape-topped band-tone gate strips between; three 3:2 fields inside the walk, on-site and handover stages; foot line | 3 fields | 688 |

## What changed from V1

The dark gate bars of `003`, the black slabs and sand ground of `005`, and the outlined rail of `004` are re-cut: every gate is now a 3px tape line with a tone change or a hairline frame, and both halves of the gate carry a stroke icon (padlock closed for what is fixed, open where nothing is; clipboard for what is owed). Copy is V1's throughout; word counts equal V1's — the section is long-form by its content rule.

## Verification

- `concheck.ps1 -Sec S06 -Fields 'How a job runs|The site walk'` — ALL CHECKS PASS; parity 10/10 (`004` says CLOSES rather than FIXED AFTER THIS, as V1 did). No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels and indices; no duration; no claim from the CON list.
- Rendered and read at 1440. Corrections: `001`/`005` the stage paragraph rule was overriding the giant index size (scoped to the text column); `002` fields 21:9 → 3:1 and stage padding tightened (the column ran past 4000px); `004` field 4:5 → 1:1 to sit level with the panel.
