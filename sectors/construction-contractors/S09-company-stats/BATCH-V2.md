# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S09` — Company Stats · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — four figures only (founded, projects completed, people employed, largest project), every one a reserved field with its qualifying fields reserved too, four kinds of quantity never drawn as one, sectors and trades real, the omitted figures named and refused — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S09-001` | Universal / Safe | 001 Site White & Safety Orange | 3 — bordered cells at unequal widths | dimension line with running ticks behind the head | Four cells at 5/3/2/2 columns under a tape rule, each with a kind glyph (point on a line, stacked bars, bracketed band, spike), the figure as a bordered slot at counter scale — the snapshot's on the band tone, the extreme's tallest — a ruled record of secondary fields and V1's note; iconed sector tags and trade tags; bordered THE NUMBERS THAT ARE NOT HERE note | 10 slots | 525 |
| `CON-S09-002` | Premium / Editorial | 002 Bone & Burnt Amber | 9 — chapter pacing | levelling circle behind the head | Display and lead; four ruled chapters with the figure and its fields in the margin (smaller than the sentence, as V1 says) and the annotation in the wide column under a run-in line in tracked uppercase; ruled tags; refusal on the foot rule | 10 slots | 658 |
| `CON-S09-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — unequal modular grid | setting-out grid behind the head | Four-cell legend of the kinds under the tape rule; modules sized by kind — the fixed point 12 columns with the slot on a drawn datum line, the running total 7 with stacked ruled fields, the snapshot 5 on the band tone (the tint standing in for V1's dashed rule), the extreme 4 with a drawn spike beside the tallest slot, the tags in the remaining 8; bordered refusal strip | 10 slots | 441 |
| `CON-S09-004` | Conversion-led | 004 White & Hi-Vis | 4 — tinted band | chevron run behind the band | Display with tape underline; four-cell ruled figure row with kind glyphs and slots; TELL US THE SIZE OF YOURS as a hi-vis tape band with one bordered action and WHY WE ARE GIVING THAT AWAY beside it; ruled tags; ruled refusal foot | 10 slots | 414 |
| `CON-S09-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 4 ×4 — alternating bands | cut-earth hatching down the left margin | Four full-width alternating bands under a tape rule, the figure as a 5.2rem poster-scale slot in each with its own drawn geometry beside it — a datum point, stacked bars, a bracketed band, a spike against five short bars — and a tracked caption; ruled tags; ruled refusal foot | 10 slots | 488 |

## What changed from V1

The dark action panel of `004`, the dashed provisional rule of `003` and the coloured shape treatments of V1 are re-cut: the four kinds are told apart by cell width, tint, slot height and a small drawn construction figure, all in hairlines and one accent, with the reserved figure at counter or poster scale as the register prescribes. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S09 -Fields 'The firm, in figures|Year founded|Largest project' -AllowClaims 'incident rate'` — ALL CHECKS PASS; parity 15/15. The allowed string appears once, in `001`'s refusal explaining why no safety figure is printed, as V1 wrote it. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy at all — every quantity is a reserved slot with a visually-hidden label.
- Rendered and read at 1440. Corrections: `002` slot and record max-widths moved to `width: min()` (checker rule).
