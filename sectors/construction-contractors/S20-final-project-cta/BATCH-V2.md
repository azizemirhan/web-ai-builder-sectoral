# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S20` — Final Project CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a close is a commitment, not a button; the five undertakings, how each would visibly break, and the question that tests each; what to have ready; no countdown, slot count, order-book line, free quote, price, response time or figure; the person who would come and the walk booking contact reserved; the batch's only anchor in `004` — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S20-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — undertaking sheets | setting-out grid behind the head | Five bordered sheets under the tape — word index and stroke icon (site / badge / stop octagon / calendar / phone), WE WILL in tracked uppercase with its paragraph, IF WE BROKE IT on the band tone behind a deep-red edge with a struck seal, ASK US at headline size behind an accent edge with a speech-line icon; tape-topped table band with square-bulleted list and the two reserved fields at counter scale; bordered refusal with tags | 2 slots | 713 |
| `CON-S20-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — the declaration as ruled chapters | levelling circle behind the head | Five ruled chapters with iconed eyebrows (THE FIRST … AND THE FIFTH), the undertaking in tracked uppercase and its paragraph, and a bordered broke / ask pair beside; the table chapter with a ruled list beside a tape-topped ledger of the reserved fields; closing chapter | 2 slots | 833 |
| `CON-S20-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — usual against undertaken | dimension line with ticks behind the head | Bordered two-column sheet with a column head and five rows — the usual sentence struck through in the muted tone behind a struck seal in the small half, the undertaking with WE WILL, IF WE BROKE IT (band tone, deep-red edge) and ASK US (accent edge) in the large half; bordered two-cell foot with the table list and reserved fields at counter scale; red-topped refusal | 2 slots | 749 |
| `CON-S20-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — one ask, and when not to make it | chevron run behind the ask band | Display with tape underline; hi-vis ask band with one bordered iconed action and the reserved fields at counter scale; HAVE THESE OUT ON THE TABLE as a bordered four-cell iconed row; DO NOT BOOK IT YET IF as three bordered cells behind a deep-red edge with a struck calendar and DO THIS INSTEAD on the band tone; the undertakings as a ruled iconed list with the question in the accent; ruled foot. The batch's only anchor, in-page | 2 slots | 698 |
| `CON-S20-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — five sentences at display size | cut-earth hatching down the left margin | Five ruled rows with the ordinal and icon in the margin, the undertaking at display size, and the same bordered broke / ask pair beneath each, drawn identically; the table as a ruled list beside AND WHO WOULD COME with the reserved fields at counter scale; ruled foot | 2 slots | 538 |

## What changed from V1

The five undertakings are drawn with one geometry across the batch — the undertaking in ink or the accent, the break on the band tone behind a deep red (`--no`) edge with a struck seal, the question behind the theme accent edge with a speech-line icon — and each carries a stroke icon (site, badge, stop octagon, calendar, phone); the table list uses filled square bullets; the reserved fields are bordered slots at counter scale. `003`'s "dashed half" is drawn as a struck half — the register carries no dashed rule — and the two sentences naming it say "struck" instead; every other line is V1's word for word, and word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S20 -Fields 'Name of the person who would run the job|Contact for booking the site visit' -AllowClaims 'limited slots'` — ALL CHECKS PASS; parity 10/10. The allowed string is "No limited slots" in `001`'s refusal tags, V1's words. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no deadline, count, price, response time or figure; the anchor in `004` only, in-page.
- Rendered and read at 1440. Corrections: `005` pair width moved to `width: min()` (checker rule) and its record heading unflexed.
