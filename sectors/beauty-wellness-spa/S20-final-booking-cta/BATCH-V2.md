# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S20` — Final Booking CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the two rules — no mechanism (no form, field, select, date or time) and no pressure (no count, countdown, discount, price or rating) — and the five reassurances are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S20-001` | Universal / Safe | 001 Linen & Olive | 1 — tall field beside the ask | 4:5 field beside the ask with a bordered action and an underlined second route; ruled three-column reassurances | 1 | 100 |
| `WELL-S20-002` | Premium / Editorial | 002 Bone & Clay | mast + one sentence + one link | One serif sentence at display size; one underlined serif action on a rule; one quiet line — the fewest elements in the sector | 0 | 57 |
| `WELL-S20-003` | Structured / Visual Modular | 003 Mist & Moss | 3 — four cells two by two | The ask with its actions in the first cell; what happens next, what can still change, what you are not agreeing to in the other three | 0 | 225 |
| `WELL-S20-004` | Conversion-led | 004 Sand & Ochre | 3 — two cells + ruled row + statement | Two route cells with their own actions; ruled risk-removal row; the no-countdown statement in serif on the foot rule over a 21:8 field | 1 | 200 |
| `WELL-S20-005` | Art-directed / Distinctive | 005 Ivory & Plum | 5 — type crossing a field's edge | One serif sentence with the bordered action inline, its last line crossing the top of a 21:9 field; quiet line and second route beneath | 1 | 59 |

## What changed from V1

Filled pills, the dark first module of `003` and the bled ground of `005` are gone. Every action is the register's thin bordered rectangle or an underlined link; `005`'s inline action is a bordered rectangle at 0.34em of the display size rather than a pill, and the sentence now crosses the field's edge instead of sitting above it. The three conversion studies (`001`, `003`, `004`) all carry the second route as an underlined link so the visitor who is still deciding is kept.

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on "Book a time" and "When you are ready" 10/10. No `<form>`, field, select, date or time; no digit in visible copy beyond indices and ratio labels; urgency vocabulary appears only in the negative.
- Rendered and read at 1440. Correction before sign-off: `003` list carried border and max-width on one element — measure removed (the cell already bounds it).
