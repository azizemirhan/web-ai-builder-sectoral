# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S27` — Location / Branch Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the bracketed location as the page's `<h1>`, address, phone, email and the four arrival chapters as bracketed placeholders, the map held empty with no location data, the access note, one primary action and two routes; the media counts per study (2, 1, 2, 0, 2) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S27-001` | Universal / Safe | 001 Chalk | 1 — the address first, then the entrance diptych | ring behind the h1 | FIND THIS CLINIC as placeholder chips with the action on the lead rule; the entrance and reception from the entrance as two 3:2 fields; the four chapters as a bordered grid; the access note on the plum edge; two links | 2 × 3:2 · 6 | 164 |
| `DN-S27-002` | Premium / Editorial | 002 Linen | 2 — the identity beside a tall entrance | arc above the h1 | The h1, lead, address chips, action and note on the plum edge beside the clinic entrance at 4:5; the four chapters as a ruled column with labels on the left; two links on the lead rule | 1 × 4:5 · 6 | 153 |
| `DN-S27-003` | Structured / Visual Modular | 003 Slate | 3 — the identity and address as one band, with a reserved map | dot grid behind | One bordered plate — the h1 and lead beside the address chips and action on the band tone; a bordered grid of four; the map as a 2:1 field labelled VERIFIED LOCATION PENDING in the plum beside the entrance at 3:2; the note on the plum edge; two links | map 2:1 + 3:2 · 7 | 168 |
| `DN-S27-004` | Conversion-led | 004 Daylight | 4 — the type-led location with the contact as a band | bar under the location | The h1 with the bar, lead and note beside a band holding the address chips and the action; the four chapters in V1's order as a ruled column; two links on the lead rule. No field | none · 6 | 145 |
| `DN-S27-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the heading above an address and entrance pairing | corner marks framing the h1 | The h1 framed at the largest measure; address chips and the action beside the entrance at 3:2; the four chapters ruled with reception from the entrance as a 3:1 field set between the third and the fourth; the note on the plum edge; two links on the lead rule | 3:2 + 3:1 · 6 | 164 |

## What changed from V1

The bracketed location prints in muted ink as the h1; the address, phone and email become bordered placeholder chips inside an `<address>`, never a real line; the access note carries the plum edge in every study and the empty map its plum label. V1's amber contact panel and arched entrance become the 004 band and a bare soft-cornered field. No map tile, pin or directions link. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S27 -Fields 'Clinic location|Building and street|clinic number|clinic email|Opening hours|Getting here|Getting inside|Care at this location|before setting out|Ask the clinic team|Explore clinic locations|Browse dental treatments'` — ALL CHECKS PASS; parity 60/60. One `<h1>` per study; no header/nav/footer; no form; no iframe; three links per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; six placeholders per study, seven in 003 with the map.
- Rendered and read at 1440. No corrections needed.
