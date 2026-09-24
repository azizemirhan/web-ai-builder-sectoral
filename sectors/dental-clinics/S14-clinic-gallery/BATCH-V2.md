# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S14` — Clinic Gallery · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — six rooms in the order met, captions say what happens there, the sterilisation room as the one you will not be in, the two notes, no face, no treatment, no catalogue, the closing line; the media counts per study (6, 1, 6, 2, 5) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S14-001` | Universal / Safe | 001 Chalk | 1 — six rooms in order | ring behind the head | Six bare 4:3 fields in a grid of three, each captioned with a word-numeral chip, the sterilisation room on the plum edge with a plum chip; two ruled notes; foot on the lead rule | 6 × 4:3 · 0 | 198 |
| `DN-S14-002` | Premium / Editorial | 002 Linen | 2 — one room at full width | arc above the head | *For most of the appointment, this is the room.*; the ceiling above the chair edge to edge at 21:9; THE OTHER FIVE, A LINE EACH as ruled lines, the sterilisation room on the plum edge; two ruled notes; foot on the lead rule | 1 × 21:9 · 0 | 183 |
| `DN-S14-003` | Structured / Visual Modular | 003 Slate | 3 — five as one object, the sixth across a gap | dot grid behind | One plate of five 4:3 fields on 1px ink seams with their captions on the same seams; a gap labelled NOT ON THE ROUTE in the plum; the sterilisation room alone as a 3:1 field on the plum edge; two ruled notes; foot | 5 × 4:3 + 3:1 · 0 | 203 |
| `DN-S14-004` | Conversion-led | 004 Daylight | 4 — the invitation first | bar under *ask to see* | *You will be in five of these six. The sixth you can ask to see.* as a band at display size with V1's reason; the door and the ceiling as two 3:2 fields; THE OTHER FOUR, NAMED as a ruled row, the sterilisation room on the plum edge; two ruled notes; V1's alternative foot on the lead rule | 2 × 3:2 · 0 | 217 |
| `DN-S14-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — every frame from where you will be | corner marks framing the head | Five 4:3 fields whose own labels name the vantage in the accent; the sixth cell holds no field — a struck camera in the plum, NO VANTAGE, and V1's reason on the plum edge; two ruled notes; foot on the lead rule | 5 × 4:3 · 0 | 234 |

## What changed from V1

The sterilisation room carries the refusal token in every study — the plum chip, edge, label or struck camera — and WHAT IS NOT HERE carries the struck-person mark. Fields are bare, soft-cornered and labelled by room (or by vantage in 005); the 003 plate is the one hard-seamed object. No lightbox, no thumbnail strip, no hover. The only darkened surface is the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S14 -Fields 'what happens there rather than what it is|the bell is on the left|Somebody will tell you how late|ask to see the sterilisation log|the one on the ground floor|most of the appointment|The one room here you will not be in|nothing was moved|supplier|five of these six'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. No corrections needed.
