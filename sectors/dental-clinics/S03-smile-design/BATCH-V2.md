# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S03` — Smile Design · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the five stages with their state, the line rendered as a compositional event between three and four, *below this line, nothing comes off*, irreversibility stated as a material fact, no before/after gallery and the link to smile results, no outcome, price or guarantee; the media counts per study (1, 1, 2, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S03-001` | Universal / Safe | 001 Chalk | 3 — two bordered runs with the line between | ring behind the head | The plan on screen as a 3:1 field; three reversible stages as bordered cells with word-numeral and REVERSIBLE chips; the line as a 3px plum rule with a half-circle mark; two irreversible cells with IRREVERSIBLE chips in the plum; foot | 1 × 3:1 · 0 | 181 |
| `DN-S03-002` | Premium / Editorial | 002 Linen | 2 in one measure | arc at the head's corner | Five ruled lines with chips in the margin; the review appointment as a 3:1 field placed on the line, the line sentence beneath it on the plum rule; close | 1 × 3:1 · 0 | 179 |
| `DN-S03-003` | Structured / Visual Modular | 003 Slate | 3 — one joined row | dot grid behind | Seven bordered cells: the scanner, three reversible stages, the seam widened into a band-tone gap carrying the line sentence turned on its side, two irreversible stages, the plan on screen; foot | 2 cells · 0 | 184 |
| `DN-S03-004` | Conversion-led | 004 Daylight | 4 — the last free no | bar under *reversible* | The scanner as a 4:3 field beside the head; three bordered cells; THIS IS THE LAST POINT WHERE NO IS FREE as a band whose lower edge is the plum rule; two bordered cells; foot | 1 × 4:3 · 0 | 185 |
| `DN-S03-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the line is the page | corner marks framing the head | Three ruled lines on the paper; from the line down the page is the band tone and does not change back, holding the two irreversible stages and the foot. No field | none · 0 | 183 |

## What changed from V1

Stage numbers `01`–`05` become word-numeral chips; the state is a second chip — REVERSIBLE in the accent, IRREVERSIBLE in the refusal plum — and the line is the one 3px plum rule in every study, never a red. Cards and filled panels go; the darkened surfaces are the 003 gap, the 004 band and the 005 lower half, each carrying the argument. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S03 -Fields 'Photographs and a scan|The digital plan|The trial smile|Below this line, nothing comes off|Preparation|Enamel is removed|Fitting|smile results|Nobody is prepared on the day'` — ALL CHECKS PASS; parity 45/45. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no outcome, price, guarantee or comfort term; no tooth mark.
- Rendered and read at 1440. No corrections needed.
