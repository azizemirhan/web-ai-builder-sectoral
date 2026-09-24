# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S11` — Appointment Booking · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three routes with the phone preferred and the form named slowest, the two terms in every study, one link and no form, no number printed, the closing line; the media counts per study (1, 0, 2, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S11-001` | Universal / Safe | 001 Chalk | 1 — three routes as a row | ring behind the head | THE PHONE, THE ONLINE FORM, WALKING IN as a bordered row with chips — ONE · FASTEST in the accent, TWO · SLOWEST in the plum, THREE in ink — the phone on the lead rule, the form on the plum rule; the desk as a 3:1 field; two ruled terms; action with the calendar mark; foot on the lead rule | 1 × 3:1 · 0 | 206 |
| `DN-S11-002` | Premium / Editorial | 002 Linen | 2 — the counterintuitive sentence | arc above the head | *The form is slower than the phone, and we are the ones telling you.* at display size; three ruled route lines with word-numeral keys, the phone on the lead rule and the form on the plum edge; two ruled terms; action; foot. No field | none · 0 | 197 |
| `DN-S11-003` | Structured / Visual Modular | 003 Slate | 3 — three modules over one terms band | dot grid behind | The desk and the waiting room as two 3:2 fields; one bordered plate — three route cells with tracked labels over the two terms on the band tone; action; foot | 2 × 3:2 · 0 | 217 |
| `DN-S11-004` | Conversion-led | 004 Daylight | 4 — the cancellation term first | bar under *the day before* | *If you cannot come, tell us the day before.* as a band at display size; three routes as a ruled row, the form on the plum edge; the desk as a 3:1 field; the commitment on the lead rule; action; foot | 1 × 3:1 · 0 | 192 |
| `DN-S11-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the gaps drawn | corner marks framing the head | Three route blocks in one column, the desk attached to the phone as a 3:1 field; UNTIL THE MORNING and AND THEN YOU WAIT as plum tracked lines on the plum rule between them; two ruled terms; action; foot on the lead rule | 1 × 3:1 · 0 | 206 |

## What changed from V1

The slow route carries the refusal token in every study — the plum chip, the plum rule or the plum edge — and the two gaps in 005 are drawn in the plum rather than as arrows or steps. The action is the 1px ink border with the calendar mark and the secondary line beside it; no filled button. Device, screen and building marks name the routes; the darkened surfaces are the 003 terms band and the 004 band. Fields are bare and labelled. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S11 -Fields 'The phone is the fastest|Answered by someone in the building|ring back the same day|nobody opens it until the morning|We will not turn you away|rather than rush you|about forty minutes|Nothing else is agreed|the day before|never on a later bill|Book online|The number is on the contact page|costs us the most to answer'` — ALL CHECKS PASS; parity 65/65. No `<h1>`; no header/nav/footer; no form; one link per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. No corrections needed.
