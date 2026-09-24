# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S20` — Final Appointment CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one primary action to the booking study and one secondary to the contact study, no urgency, no countdown, no offer, no figure; the media counts per study (1, 1, 1, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S20-001` | Universal / Safe | 001 Chalk | 1 — the invitation beside the room | ring behind the head | *Let's take the next step.* with the lead and the two actions; the clinic reception as a 3:2 field captioned *A place to begin* on the lead rule | 1 × 3:2 · 0 | 62 |
| `DN-S20-002` | Premium / Editorial | 002 Linen | 2 — the room first, then the sentence | arc above the head | The clinic reception edge to edge at 21:9; *Make a little space for yourself* at display size with *A fresh beginning.* beside; the two actions on the lead rule | 1 × 21:9 · 0 | 50 |
| `DN-S20-003` | Structured / Visual Modular | 003 Slate | 3 — one plate, two cells | dot grid behind | *A visit. A conversation. A place to start.*; one bordered plate on a single seam — the reception team at work as a 3:2 field beside *Bring what's on your mind.* and the two actions on the lead rule | 1 × 3:2 · 0 | 73 |
| `DN-S20-004` | Conversion-led | 004 Daylight | 4 — the invitation as a band | bar under *is yours* | *The first step is yours.* at display size in a band with the lead and the two actions; V1's closing line on the lead rule. No field | none · 0 | 48 |
| `DN-S20-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the sentence around the field | corner marks framing the head | *A new visit. Your own pace.* framed, with the lead and the two actions on the lead rule; the clinic reception as a 4:3 field beside | 1 × 4:3 · 0 | 51 |

## What changed from V1

The primary action is the 1px ink border with the calendar mark in every study and the secondary is an underlined line with the arrow — no filled button, no capsule, no tile, no sun. V1's arrows become the register's mark and rule. The only darkened surface is the 004 band. Routes to S11 and S19 are V1's, variant to variant. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S20 -Fields 'appointment|visit|question'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no form; two links per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no urgency or claim term.
- Rendered and read at 1440. No corrections needed.
