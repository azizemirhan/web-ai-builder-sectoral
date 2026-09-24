# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S12` — Emergency Dental Care · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three lists hardest first with the hospital list before us, the two facts, no phone number printed, no countdown, the ring line and the closing line in every study, the daily slot count as a placeholder demo value; the media counts per study (0, 1, 1, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S12-001` | Universal / Safe | 001 Chalk | 1 — three lists in one row | ring behind the head | *Three lists, and the first one is not us* with *not us* in the plum; HOSPITAL, NOT US on the plum rule, TODAY, AND RING FIRST on the lead rule, IT CAN WAIT UNTIL MORNING on the ink rule, as bordered cells with symptoms as ruled lines and the instruction at the foot; two ruled facts; ring line; foot on the lead rule. No field | none · 1 | 208 |
| `DN-S12-002` | Premium / Editorial | 002 Linen | 2 — the third list takes the measure | arc above the display line | The first two lists as ruled columns; the surgery edge to edge at 21:9 captioned *The only list that arrives in this room is the second one.*; *It can wait until morning.* at display size with its list as one run; two ruled facts; ring line; foot on the lead rule | 1 × 21:9 · 1 | 224 |
| `DN-S12-003` | Structured / Visual Modular | 003 Slate | 3 — the instruction at the bottom of each one | dot grid behind | The surgery as a 3:1 field above one bordered plate of three joined modules on subgrid rows, each ending in its own instruction on its own ground — band tone with the plum rule, band tone with the lead rule, paper with the ink rule; two ruled facts; ring line; foot | 1 × 3:1 · 1 | 225 |
| `DN-S12-004` | Conversion-led | 004 Daylight | 4 — the hours and the slots first | bar under *every working day* | The two facts as a band at display size, the shut hours on the plum edge in the plum; three lists as a ruled row, the hospital list on the plum edge; the surgery as a 3:1 field; ring line on the lead rule; foot | 1 × 3:1 · 1 | 212 |
| `DN-S12-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — one column, reading-out-loud size | corner marks framing the head | Five ruled blocks with tracked labels in the left column and the symptoms as sentences at statement size, the hospital block on the plum edge and the today block on the lead rule; *If you are not sure which list you are on, ring.* at display size; foot on the lead rule. No field | none · 1 | 203 |

## What changed from V1

The hospital list carries the refusal token in every study — plum rule, plum edge or plum label — and the today list carries the lead rule; nothing is red and nothing counts down. Symptoms are ruled lines or sentences, never icons; the darkened surfaces are the 003 instruction feet and the 004 band. Fields are bare and labelled *The room*. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S12 -Fields 'Three things cannot|Bleeding that will not stop|A blow to the head|not dental appointments|knocked out or knocked loose|the first hour matters most|A lost filling|none of it is worse at nine|not open at night or on Sunday|who do this all night|appointments free every working day|they are for that day|Guessing from a list is not your job|not to come tonight'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no pain or guarantee term.
- Rendered and read at 1440. Two corrections: the 004 ring line used `max-width` with its rule and tripped the boxed-callout check — set to `width: min(100%, 44rem)`; the 003 module feet sat at different heights — the plate now runs subgrid rows so the three instructions align.
