# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S19` — Contact · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — ordered by urgency, the enquiry last; the six routes and what the answerer can settle; the out-of-hours answer; the site-visit refusal; every number, mailbox and name reserved; the hoarding as a reserved area; no form, response time, map or opening hours — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S19-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — route rows | setting-out grid behind the head | 21:9 hoarding field with slate; OUT OF HOURS as a tape-topped band with a phone icon and the reserved duty number at display scale; six bordered route rows in urgency order — word index, stroke icon (hard hat / house / wrench / exchange / badge / clipboard), the route in tracked uppercase, the one sentence, the reserved slot — the first on the band tone; bordered refusal with a stop octagon | 1 field, 7 slots | 202 |
| `CON-S19-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — ruled route chapters beside a sticky field | levelling circle behind the head | Sticky 4:5 hoarding field in the left column; six ruled chapters with the word index at counter scale, an iconed route heading and the reserved slot in the margin; OUT OF HOURS and NOT ON THE SITE as two bordered closing cells, the first tape-topped | 1 field, 6 slots | 186 |
| `CON-S19-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — one bay per problem | dimension line with ticks behind the head | 4:1 hoarding field; three-by-two bordered bay sheet with the word index at counter scale, an icon, the route and the reserved slot pinned to each cell foot, the first bay on the band tone under the tape; two-cell foot with OUT OF HOURS and the reserved duty number at display scale beside the refusal | 1 field, 7 slots | 201 |
| `CON-S19-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — the urgent route as the largest thing | chevron run behind the urgent band | Display with tape underline; the urgent route as a hi-vis band with the route at display size and the reserved site-and-duty number at display scale, beside a 3:1 hoarding field; the other five as a bordered five-cell ledger with word indices, icons and reserved slots, the enquiry last on the band tone; ruled refusal foot. No form, no anchor | 1 field, 6 slots | 200 |
| `CON-S19-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the hoarding at night | cut-earth hatching down the left margin | 21:9 hoarding field in a night tone with the slate at its head and an OUT OF HOURS paper plate crossing its lower edge carrying the reserved duty number at display scale; six broadside ruled rows with the route at headline size, icon and word index in the left margin and the reserved slot as a right-margin footnote; the refusal at display size under the tape rule | 1 field, 7 slots | 200 |

## What changed from V1

The urgency order is drawn as one geometry across the batch — the first route on the band tone or at the largest size, the enquiry last and demoted — with a stroke icon per route (hard hat, house, wrench, exchange arrows, badge, clipboard), a phone icon on the out-of-hours answer and a stop octagon on the site-visit refusal; V1's numerals are replaced by word indices (ONE to SIX) so no digit appears in copy; the hoarding is a bare flat field with a slate label; every reserved number is a bordered slot, the duty number at display scale. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S19 -Fields 'Same number, reserved|Estimating mailbox|Site hoarding media area'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no response time, map or opening hours; every number, mailbox and name a reserved slot with a visually-hidden label.
- Rendered and read at 1440. Corrections: word-index rules given the specificity to beat the row paragraph rule (`p.ix`) and set to ink.
