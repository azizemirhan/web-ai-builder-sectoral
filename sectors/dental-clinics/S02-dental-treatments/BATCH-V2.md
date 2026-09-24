# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S02` — Dental Treatments · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the symptom is the title and the procedure the small label; the how-soon field on every entry, two of the three most expensive marked *when you are ready*; the sixth entry as S01's proposition; one link and no form; no price, guarantee or comfort claim; the six waits in 005 as placeholder demo values; the media counts per study (1, 1, 2, 0, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S02-001` | Universal / Safe | 001 Chalk | 3 — bordered cells under an anchor | ring behind the head | Head split with *the thing that is wrong* in the accent; reception as a 3:1 field; the six as bordered cells three across — how-soon chip (NOW in the accent), symptom title, procedure as tracked label, first visit; the link on the lead rule | 1 × 3:1 · 0 | 201 |
| `DN-S02-002` | Premium / Editorial | 002 Linen | 2 in one measure | arc at the head's corner | The six as ruled lines in the order they need looking at, chips in the margin; the hygiene room as a 3:1 field inside the list with *Below this line, nothing is urgent* as its caption on the lead rule; the link | 1 × 3:1 · 0 | 213 |
| `DN-S02-003` | Structured / Visual Modular | 003 Slate | 3 — a bento on one seam | dot grid behind | Eight cells four across sharing lines — six symptom modules and two fields as cells: the surgery in use and the scanner the aligner copy names; the link on the lead rule | 2 cells · 0 | 206 |
| `DN-S02-004` | Conversion-led | 004 Daylight | 4 — sorted by urgency | bar under *how soon* | The urgent one alone as a band at the largest size; THESE CAN WAIT A WEEK OR TWO as three bordered cells; THESE TWO COST THE MOST, AND NEITHER IS URGENT as two wider cells; the link. No field | none · 0 | 193 |
| `DN-S02-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — ordered by how long people wait | corner marks framing the wait column | The placeholder waits at display size in the accent down the left; chip, symptom, label and first visit to the right; V1's embarrassment line on the lead rule with the link. No field | none · 6 | 222 |

## What changed from V1

The how-soon field becomes one chip device across the batch — NOW bordered in the accent, the rest in the ink — and the procedure name one tracked label; fields are bare 6px areas labelled by what they are (RECEPTION, THE ROOM, THE SCANNER); cards, pills and filled surfaces go, the one darkened surface being the 004 band that holds the urgent entry. Copy is V1's throughout; the six waits keep their placeholder marking and are the only digits on the page.

## Verification

- `dncheck.ps1 -Sec S02 -Fields 'keeping you awake|Root canal or extraction|filling has come out|gums bleed|One is missing|crooked|where to start|Examination|Book the examination|composite bonding'` — ALL CHECKS PASS; parity 50/50. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no price, guarantee or comfort term; no tooth mark.
- Rendered and read at 1440. One correction: the 002 field set to 3:1 so the one-measure list stays under two screens.
