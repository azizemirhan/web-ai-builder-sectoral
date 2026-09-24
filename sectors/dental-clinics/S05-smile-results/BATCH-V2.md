# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S05` — Smile Results · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the four cases with the second-photograph timing on every one; the four rules printed in full, the selection admitted; no face in any pair, one case each, never a typical result; no outcome promise, price or retouching; the case count, year total and timings as placeholder demo values; the media counts per study (4, 1, 4, 2, 4) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S05-001` | Universal / Safe | 001 Chalk | 1 — the rules first | ring behind the head | The four rules as a marked row on the lead rule; four cases as paired fields two across — one bare area split by a 1px seam, BEFORE and AFTER as slates — with word-numeral chip, case, what was done and the timing as a tracked line; the no-face line | 4 pairs · 6 | 197 |
| `DN-S05-002` | Premium / Editorial | 002 Linen | 2 in one measure | arc at the head's corner | One case shown properly as a paired field at full measure; the four rules as ruled lines on the lead rule; THE OTHER THREE, IN A LINE EACH with their timings; close | 1 pair · 6 | 180 |
| `DN-S05-003` | Structured / Visual Modular | 003 Slate | 3 — four joined modules | dot grid behind | Four bordered cells in one row, each with its 1:1 paired field, chip, case, timing and its own band-tone rule strip *one case, not a typical result*; the three shared rules as a row on the lead rule | 4 pairs · 6 | 216 |
| `DN-S05-004` | Conversion-led | 004 Daylight | 4 — the selection ratio first | bar under *sixty-one* | FOUR SHOWN OUT OF SIXTY-ONE THAT YEAR as a band at display size with the best-of-a-year line; two paired fields; two ruled lines; three rules on the lead rule | 2 pairs · 6 | 176 |
| `DN-S05-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — captioned twice | corner marks framing the head | Four 1:1 paired fields in one row, each with a second caption DOES NOT SHOW on the plum edge; the last-ten-minutes line on the lead rule; four rules as a row | 4 pairs · 6 | 222 |

## What changed from V1

The before-and-after area is one device across the batch — a single bare field split by a 1px seam, BEFORE and AFTER as slates, never a mouth in the label; the timing is a tracked line with the placeholder in the accent; the rules carry the same four marks everywhere. Cards and filled panels go; the darkened surfaces are the 003 rule strips and the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S05 -AllowClaims ' best' -Fields 'Two chipped front teeth|Discoloured after a root canal|Crowding, upper front|A missing premolar|Same camera, same light|Not retouched|sixty-one|Not a typical result|No face appears|the same day|eleven months later'` — ALL CHECKS PASS; parity 55/55. The one allowed term is V1's own admission in 004 (*the best of a year, not the average of one*), a disclosure and not a superiority claim. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no outcome promise.
- Rendered and read at 1440. No corrections needed.
