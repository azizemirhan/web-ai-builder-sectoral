# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S17` — Locations · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one address, the parts that fail named, no map embed, no directions link, no address line, the two walking times as placeholder demo values, the ring line in every study; the media counts per study (2, 6, 2, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S17-001` | Universal / Safe | 001 Chalk | 1 — getting in and getting here | ring behind the head | GETTING IN as four ruled lines on the lead rule, the toilet and hearing on the plum edge with struck marks; the door and the corridor as two 3:2 fields; GETTING HERE as three ruled lines, parking on the plum edge; ring line; foot | 2 × 3:2 · 2 | 213 |
| `DN-S17-002` | Premium / Editorial | 002 Linen | 2 — the walk itself, downward | arc above the head | Six ruled rows in the order met, each a word-numeral chip, a name, a line and a 3:2 field, THE STAIRS on the plum edge; NOT ON THE WALK as a ruled row of three; foot on the lead rule | 6 × 3:2 · 2 | 245 |
| `DN-S17-003` | Structured / Visual Modular | 003 Slate | 3 — the building as a specification | dot grid behind | One bordered plate of three blocks with verdicts — GROUND FLOOR on the lead rule, FIRST FLOOR on the plum rule and band tone, NOT A FLOOR PROBLEM on the ink rule; the hallway and the stairs as two 3:2 fields at seated height with V1's line; a ruled row of three; foot | 2 × 3:2 · 2 | 236 |
| `DN-S17-004` | Conversion-led | 004 Daylight | 4 — the reasons people arrive late, first | bar under *is traffic* | WHY PEOPLE ARRIVE LATE as a band at display size with three ruled reasons on the plum edge; GETTING IN as a ruled row of four; the door from across the street as a 3:1 field with the transport lines in its caption; ring line on the lead rule; foot | 1 × 3:1 · 2 | 223 |
| `DN-S17-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — marginalia | corner marks framing the head | Five failures at display size in the plum on a plum top rule, each with what we do instead as a small marginal note on a leading accent rule; THE PARTS THAT DO WORK on the lead rule; the ring line. No field | none · 2 | 198 |

## What changed from V1

Every part that fails carries the refusal token — plum edge, plum rule, plum chip or the plum sentence itself — and every part that works the tick mark or the lead rule; V1's numbered frames in 002 become word-numeral chips. No map tile, pin, compass or directions button anywhere; the fields are the street, the door and the corridor. The only darkened surfaces are the 003 first-floor block and the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S17 -Fields 'the bell is on the left|wheelchair|no lift|not accessible|loop|write things down|permit-only|five minutes|ten minutes|Look for the number, not a sign|ring before you book'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no link; no iframe; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the placeholder elements; no claim term.
- Rendered and read at 1440. One correction: the 002 walk rows had their chip, name and line spread across three grid rows against the field — the text is now one cell, centred against the field.
