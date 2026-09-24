# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL`
- Section: `WELL-S02` — Treatments / Services · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in
  `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the
  design layer; the copy spine (six treatments described by what happens, the choose-for-me
  route) is retained.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S02-001` | Universal / Safe | 001 Linen & Olive | 1 — column + grid | Sticky intro column; three-by-two grid of 4:5 fields, serif title, family label, one line | 6 | 134 |
| `WELL-S02-002` | Premium / Editorial | 002 Bone & Clay | 2 + 3 — head split, bordered cells | "THE TREATMENTS" tracked uppercase; three cells sharing hairlines, 1.45:1 fields, circular arrows; foot link | 3 | 97 |
| `WELL-S02-003` | Structured / Visual Modular | 003 Mist & Moss | 8 — mosaic + labelled captions | Five-field mosaic (16:9 lead, 3:4, three 4:3) with WHAT HAPPENS / FAMILY labels; a ruled row for the sixth | 5 | ~141 |
| `WELL-S02-004` | Conversion-led | 004 Sand & Ochre | 4 — tinted band | Ruled six-row list beside the display; band with a 4:5 field, the choose-for-me statement and one bordered action | 1 | 162 |
| `WELL-S02-005` | Art-directed / Distinctive | 005 Ivory & Plum | edge-bleeding rail | "TREATMENTS" display; scroll-snap rail of five 4:5 fields with serif indices and ruled captions | 5 | 114 |

## What changed from V1

White cards, pill tags, "Read more" links and the bento/rail chrome are gone. The V1 device of
the bleeding rail survives in `005` because it is a composition, not a component; it is re-dressed
with bare fields, serif indices and hairline captions.

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on the shared spine (head line, lead, three shared
  treatments) 5/5.
- Rendered and read at 1440 and 390. Corrections: `003` had an empty cell in its second row —
  the fifth treatment moved into the mosaic; `004` band lost its inline inset (`padding` shorthand
  overrode the shell) and its list columns drifted per row (`auto` third column) — fixed with
  `padding-block` and a fixed 8rem family column.
- Cross-browser and assistive-technology testing not run. Design Lab ingestion not performed.
