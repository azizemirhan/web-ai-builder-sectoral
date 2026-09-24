# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S04` — Dentists & Specialists · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the status on every person including the principal, *not a dentist* on the hygienist, no letters after a name and the register as the place to check, portraits labelled by role and never by name, placeholder names in initial-and-surname form, no pronoun; the media counts per study (5, 1, 5, 2, 5) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S04-001` | Universal / Safe | 001 Chalk | 1 — five portraits in one row | ring behind the head | Five bare 4:5 fields labelled by role, each with the status chip — REGISTERED SPECIALIST in the accent, NOT A SPECIALIST in the ink, NOT A DENTIST in the plum — the name, the role as a tracked label and what they do; the register line and the referral line on the lead rule | 5 × 4:5 · 6 | 211 |
| `DN-S04-002` | Premium / Editorial | 002 Linen | 2 — the one you will see gets the portrait | arc at the head's corner | The principal as a 4:5 field beside their entry at subhead size; the other four as ruled lines with the status chip in the margin; close on the lead rule | 1 × 4:5 · 6 | 181 |
| `DN-S04-003` | Structured / Visual Modular | 003 Slate | 3 — an offset gallery | dot grid behind | Head and foot in a narrow column; five 1:1 fields on two columns, the right column dropped so no pair aligns, the status chip sitting on each field as a slate | 5 × 1:1 · 6 | 211 |
| `DN-S04-004` | Conversion-led | 004 Daylight | 4 — how to check every claim | bar under *how to check* | The two specialists as 4:5 fields beside their entries; the other three as a bordered row; DO NOT TAKE ANY OF THIS ON TRUST as a band with three bordered checks led by word-numeral chips, the register link in the first | 2 × 4:5 · 6 | 196 |
| `DN-S04-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — sized by how often you see them | corner marks framing the head | Five fields at five sizes on a fourteen-column grid — the hygienist largest, the specialists smallest at 1:1 — the placeholder frequency as a tracked line on each; foot on the lead rule | 5 (4:5, 4:5, 4:5, 1:1, 1:1) · 11 | 231 |

## What changed from V1

The status is one chip device across the batch, the three states in three colours, never a filled badge; portraits are bare labelled fields; the role sits under the name as a tracked label. Cards, pills and filled panels go; the one darkened surface is the 004 band of checks. Copy is V1's throughout; names, frequencies and the register link keep their placeholder marking.

## Verification

- `dncheck.ps1 -Sec S04 -Fields 'J. Okafor|A. Lindqvist|M. Rahim|T. Byrne|S. Achebe|Registered specialist|Not a specialist|Not a dentist|public register|Look us up|never swapped in'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no credential, letters or rating; no portrait label carries a name.
- Rendered and read at 1440. Corrections: the 005 grid set to fourteen columns so the five widths sum; the 003 gallery fields set to 1:1.
