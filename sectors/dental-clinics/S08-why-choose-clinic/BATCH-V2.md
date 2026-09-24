# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S08` — Why Choose Clinic · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — four checkable reasons, three refusals in every study, the load-bearing fourth reason, the closing line, no superiority claim, the surgery count, headcount and referral names as placeholder demo values; the media counts per study (2, 1, 0, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S08-001` | Universal / Safe | 001 Chalk | 3 — reasons, surgeries, refusals | ring behind the head | Four reasons as bordered cells with tick marks; the two surgeries as paired 3:2 fields; GO SOMEWHERE ELSE IF as a row of three on the plum rule with struck marks; foot | 2 × 3:2 · 3 | 204 |
| `DN-S08-002` | Premium / Editorial | 002 Linen | 2 — one reason given the measure | arc at the display line | *We write down what we did not do* at display size with V1's explanation; a surgery as a 3:1 field; three more as ruled lines on the lead rule; three refusals as ruled lines on the plum rule; foot | 1 × 3:1 · 3 | 218 |
| `DN-S08-003` | Structured / Visual Modular | 003 Slate | 3 — one object, both sides drawn | dot grid behind | COME HERE IF and GO SOMEWHERE ELSE IF as two bordered panels on one seam, the refusals on the band tone with the plum rule; foot. No field | none · 3 | 190 |
| `DN-S08-004` | Conversion-led | 004 Daylight | 4 — the refusals first | bar under *first* | READ THIS PART FIRST as a band holding the three refusals as bordered cells; four reasons as a ruled row; a surgery as a 3:1 field; foot on the lead rule | 1 × 3:1 · 3 | 189 |
| `DN-S08-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — seven conditionals | corner marks framing the head | Seven ruled lines each opening *If* in the accent (or the plum), the last three on the plum edge; a surgery as a 3:1 field; foot on the lead rule | 1 × 3:1 · 3 | 214 |

## What changed from V1

Reasons carry the tick-circle mark in the accent and refusals the struck circle in the plum in every study, with the plum 3px rule or 2px edge as the refusal token, never a red; fields are bare and labelled. Icon rows, cards and filled panels go; the darkened surfaces are the 003 refusal panel and the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S08 -Fields 'same dentist|something can wait|four of us|what we did not do|sedation|cheapest price|two in the morning|who it is wrong for'` — ALL CHECKS PASS; parity 40/40. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no superiority term.
- Rendered and read at 1440. No corrections needed.
