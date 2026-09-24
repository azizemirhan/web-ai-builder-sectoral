# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S10` — Testimonials · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; V1's governing rule — the quotation structure is authored, the quotation is reserved — is kept exactly, as are the gathering policy, the `Guest NN` tokens, the short / medium / long sizing and the omission of every rating, score, count and platform.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S10-001` | Universal / Safe | 001 Linen & Olive | 3 — bordered cells | Head split; three cells sharing hairlines, each a reserved area at its own height (short / long / medium) with a portrait field and token | 3 + 3 | 52 |
| `WELL-S10-002` | Premium / Editorial | 002 Bone & Clay | 7 — quotation panel with pager | Portrait field beside a tinted panel holding one area at display proportion, pager `01 / 03` with circular arrows as in-page links; rows 02 and 03 beneath | 3 + 3 | 66 |
| `WELL-S10-003` | Structured / Visual Modular | 003 Mist & Moss | 3 — cells with group headings | Three category columns sharing hairlines, each two areas of unequal height with portrait tokens; policy on the foot rule | 6 + 6 | 81 |
| `WELL-S10-004` | Conversion-led | 004 Sand & Ochre | 4 — tinted band | Band with the three collection rules as ruled rows, one bordered action and the second route as an underlined link, beside a ruled stack of three areas | 3 + 3 | 95 |
| `WELL-S10-005` | Art-directed / Distinctive | 005 Ivory & Plum | 3 + 5 — brick grid, type crossing an edge | Twelve-column wall of six hairlined cells at spans 5/4/3/4/3/5, each with a sized area; one display-size accent quotation mark crossing the wall's top rule; no portraits | 6 | 65 |

## What changed from V1

Cards, round portrait slots, the deep aubergine and near-black grounds and the watermark glyph are gone. Portrait slots are small square fields. `002` renders the ARC quotation-panel device without script: the pager's arrows are in-page links to the ruled rows beneath, and the disabled arrow is a bordered ring in the hairline colour. `005` keeps the wall's unequal spans but shows the three lengths as sized tinted areas inside hairlined cells, with the oversized glyph moved from watermark to accent type crossing the top rule.

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on `Guest 01`, "written" and "exchange" 15/15. Reserved quotation areas per study: 3, 3, 6, 3, 6 — all empty. No curly-quoted run of visible text anywhere; the only quotation marks are decorative glyphs marked `aria-hidden`.
- Rendered and read at 1440. Corrections before sign-off: `005` glyph sat above the rule rather than across it — margin pulled to `-0.75em`; `005` cells first carried only labels, so the three lengths were invisible at row height — tinted areas at 4.5 / 6.5 / 9rem added inside each cell.
