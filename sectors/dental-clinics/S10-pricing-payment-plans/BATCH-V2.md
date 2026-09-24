# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S10` — Pricing & Payment Plans · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — no figure of any kind, the two kinds of price, the commitment in writing, the closed list of three movers, the two paying lines, the closing line in every study; the media counts per study (1, 1, 1, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S10-001` | Universal / Safe | 001 Chalk | 1 — the two kinds of price side by side | ring behind the head | ONE PRICE and CANNOT BE QUOTED as two bordered panels on one seam, the second on the plum rule; the commitment as a band; the room as a 3:1 field; WHAT CAN MOVE IT as a bordered row of three, *Nothing else* on the plum rule; two ruled paying lines; foot | 1 × 3:1 · 0 | 232 |
| `DN-S10-002` | Premium / Editorial | 002 Linen | 2 — the commitment as the head | arc above the head | V1's commitment at display size with *in writing* in the accent; the room edge to edge at 21:9; two ruled columns; three ruled mover lines, the third on the plum edge; two paying lines; foot on the lead rule | 1 × 21:9 · 0 | 221 |
| `DN-S10-003` | Structured / Visual Modular | 003 Slate | 3 — shaped like the document | dot grid behind | The room as a 3:1 field above one bordered plate of five ruled bands — WHEN, FIXED, NOT YET on the plum edge, WHAT MOVES IT, PAYING — each labelled in the left column; foot | 1 × 3:1 · 0 | 225 |
| `DN-S10-004` | Conversion-led | 004 Daylight | 4 — the movers first | bar under *in advance* | *Three things can move your quote. Here they are, in advance.* as a band at display size holding the three as bordered cells with word-numeral labels, the third on the plum rule; two ruled columns; the commitment on the lead rule; two paying lines; foot. No field | none · 0 | 216 |
| `DN-S10-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — three moments of knowing | corner marks framing the head | RIGHT NOW, THEN, AFTER THAT as three columns on one rule, the middle one seamed and carrying the commitment in the accent and the room as a 4:3 field — the only column with a picture, as the only moment with a number; two paying lines; foot on the lead rule | 1 × 4:3 · 0 | 243 |

## What changed from V1

The refusal token carries every "cannot" and every "nothing else": the plum rule under CANNOT BE QUOTED, the plum edge on NOT YET, the plum rule or edge under *Nothing else*. Tick, struck, half-circle and exit marks replace any icon row; the only darkened surfaces are the 001 band and the 004 band. Fields are bare and labelled *The room*. Copy is V1's throughout; no figure appears in any study.

## Verification

- `dncheck.ps1 -Sec S10 -Fields 'no prices on this page|does not change|A filling, a crown, an implant, aligners|Nobody can know that from a website|in writing, before anything starts|including doing nothing|under an old filling|after seeing both|Nothing else|instalments|what was done and nothing more|after someone has looked'` — ALL CHECKS PASS; parity 60/60. No `<h1>`; no header/nav/footer; no form; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no price, no guarantee term.
- Rendered and read at 1440. One correction: the 005 middle field was 4:5 and left the outer columns hanging — set to 4:3.
