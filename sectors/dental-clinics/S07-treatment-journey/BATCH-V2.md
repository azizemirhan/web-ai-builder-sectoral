# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S07` — Treatment Journey · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — every stage in two halves with the patient's half printed; *Nothing.* as our half of healing; the arithmetic that adds up; no lecture, no should-have; the durations and the two totals as placeholder demo values; the media counts per study (0, 1, 2, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S07-001` | Universal / Safe | 001 Chalk | 3 — two lanes on one bordered grid | ring behind the head | The arithmetic on the lead rule; five columns sharing lines — our lane, the stage with a word-numeral chip and its duration on the band tone, your lane — US, STAGE and YOU as turned labels; foot. No field | none · 7 | 190 |
| `DN-S07-002` | Premium / Editorial | 002 Linen | 2 — the step with no appointment gets the most page | arc at the head's corner | The room as a 3:1 field with the arithmetic as its caption on the lead rule; four compact ruled lines with US and YOU labels; healing as a band at display size; foot | 1 × 3:1 · 7 | 197 |
| `DN-S07-003` | Structured / Visual Modular | 003 Slate | 3 — one seam, and it moves once | dot grid behind | Five paired rows on a bordered grid with the stage in a band-tone seam column; the consulting room and the surgery as 3:1 fields inside our lane; *Nothing.* alone in our healing cell; foot | 2 × 3:1 · 7 | 195 |
| `DN-S07-004` | Conversion-led | 004 Daylight | 4 — what booking commits you to | bar under *forty minutes* | BOOKING COMMITS YOU TO FORTY MINUTES as a band at display size with V1's three sentences; the consulting room as a 3:1 field with the arithmetic caption; five ruled rows; foot | 1 × 3:1 · 8 | 217 |
| `DN-S07-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the lanes inverted | corner marks framing the head | Your half at display size on five ruled lines, ours beneath as a small tracked line; the chair as a 3:1 field; foot | 1 × 3:1 · 7 | 191 |

## What changed from V1

US and YOU are one device across the batch — tracked labels, the accent for ours and the ink for yours — and *Nothing.* is set in the accent everywhere; the stage duration is a tracked placeholder line. Cards, numbered circles and icons go; the darkened surfaces are the stage lane in 001, the seam column in 003 and the bands in 002 and 004. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S07 -Fields 'The first appointment|The written plan|The work|Healing|The check|Nothing.|raise your hand|Nine weeks|Three hours|even if it feels fine|we do nothing'` — ALL CHECKS PASS; parity 55/55. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no should-have, ought-to, neglect or failed-to.
- Rendered and read at 1440. No corrections needed.
