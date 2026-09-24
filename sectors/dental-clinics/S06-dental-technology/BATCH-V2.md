# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S06` — Dental Technology · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — every machine listed only for what it replaced, what it does not do printed under each, the radiation rule in full including the rule, no acronym, brand or model, the closing demotion in all five, the scan duration as a placeholder demo value; the media counts per study (2, 0, 3, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S06-001` | Universal / Safe | 001 Chalk | 1 — the two you can point at, paired | ring behind the head | The scanner and the milling unit as two 4:3 fields; four swaps as bordered cells with device, cube, mill and screen marks, the does-not line on the plum edge; the demotion on the lead rule | 2 × 4:3 · 1 | 183 |
| `DN-S06-002` | Premium / Editorial | 002 Linen | 2 — no photograph of any of it | arc at the head's corner | The four swaps as ruled lines at display size inside one band — the absence in the ink, the machine as a tracked label, the does-not line on the plum edge; the demotion. No field | none · 1 | 170 |
| `DN-S06-003` | Structured / Visual Modular | 003 Slate | 3 — two tiers | dot grid behind | Three machines as bordered cells with 4:3 fields; the thing that is not a machine as a band-tone cell below the seam with a NOT A MACHINE chip in the plum; the demotion | 3 × 4:3 · 1 | 199 |
| `DN-S06-004` | Conversion-led | 004 Daylight | 4 — the disclosure is not a footnote | bar under *a warning* | Four ruled lines with word-numeral chips and the does-not line beside; the second broken out into a band carrying the radiation rule with the X-ray unit as a 3:1 field beneath the admission it belongs to; the demotion | 1 × 3:1 · 1 | 179 |
| `DN-S06-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the page lists what is gone | corner marks framing the head | Four absences at display size with struck-circle marks, the machine as a tracked label; the surgery as a 3:1 field; the demotion | 1 × 3:1 · 1 | 175 |

## What changed from V1

*What it does not do* is one device across the batch — a 2px plum edge — and the machines carry the same four marks; fields are bare and labelled by the equipment the copy names. Cards, acronym tiles and filled panels go; the darkened surfaces are the 002 band, the 003 lower cell and the 004 warning band. Copy is V1's throughout; the one digit in visible copy is V1's name for the 3D X-ray, allowed as a token.

## Verification

- `dncheck.ps1 -Sec S06 -AllowDigits '3D' -Fields 'The scanner|3D X-ray|The milling unit|The screen at the chair|under the gum|more radiation|does not suit every crown|not a diagnosis|hands that place it|four minutes'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no acronym, brand or model; no digit outside a placeholder except the allowed `3D`.
- Rendered and read at 1440. One correction: the 004 band's radiation line and field kept in the band's own column.
