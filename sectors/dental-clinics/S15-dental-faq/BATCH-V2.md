# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S15` — Dental FAQ · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — six questions in the order asked with money first, every answer visible with no accordion, the three we cannot answer, the closing line; the media counts per study (1, 0, 1, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S15-001` | Universal / Safe | 001 Chalk | 1 — six in the order asked | ring behind the head | Six ruled question lines in two columns with word-numeral keys, the first on the lead rule; the desk as a 3:1 field; THREE WE CANNOT ANSWER as a ruled row on the plum rule with struck marks; foot | 1 × 3:1 · 0 | 229 |
| `DN-S15-002` | Premium / Editorial | 002 Linen | 2 — the first question at display size | arc above the head | *How much is it going to be?* as the head with its answer beside; AND THE OTHER FIVE as ruled lines in two columns; the three on the plum edge; foot on the lead rule. No field | none · 0 | 206 |
| `DN-S15-003` | Structured / Visual Modular | 003 Slate | 3 — one plate, the ground alternates | dot grid behind | The desk as a 3:1 field above one bordered plate of twelve rows — ASKED on paper, ANSWERED on the band tone, alternating — with the three as a last row on the plum rule; foot | 1 × 3:1 · 0 | 233 |
| `DN-S15-004` | Conversion-led | 004 Daylight | 4 — the three we cannot answer, first | bar under *what will happen to you* | THREE WE CANNOT ANSWER as a band at display size with struck plum marks; THE SIX WE ARE ASKED as a ruled grid of three columns; the desk as a 3:1 field at the foot; foot on the lead rule | 1 × 3:1 · 0 | 219 |
| `DN-S15-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the answer first, the question as attribution | corner marks framing the head | Six ruled blocks in two columns, each the answer at statement size with the question small beneath in the accent with a leading rule mark, ASKED MOST and ASKED SECOND kept; the three as a spanning last block on the plum edge; foot on the lead rule. No field | none · 0 | 214 |

## What changed from V1

Nothing folds: every answer is printed, and no chevron, plus or `<details>` appears. The three we cannot answer carry the refusal token in every study — plum rule, plum edge or struck plum marks — and the most-asked question carries the lead rule where a first is marked. The darkened surfaces are the 003 answer rows and the 004 band. Fields are bare and labelled *The desk*. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S15 -Fields 'because it always is|How much is it going to be|before someone looks|Will it hurt|anyone who promises is guessing|Do I actually need this|Can I stop part way|How long will I be here|about forty minutes|Will I see the same dentist|swap the person|How long a filling will last|Whether the pain comes back|what will happen to you|question marks in it'` — ALL CHECKS PASS; parity 75/75. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no pain-free or guarantee term.
- Rendered and read at 1440. One correction: the 005 blocks ran in one column and left the right half empty — set in two columns with the refusal block spanning.
