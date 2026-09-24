# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S27` — Location / Branch Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — *How to get in* as a first-class section naming the door, the bell, the lift and who to ask for; every address, phone and email an obvious placeholder (`00 Example Street`, `EC0A 0AA`, `+44 (0)20 0000 0000`, `example.com`) marked and declared; a map area only ever a slot, never a service; no skyline, glass tower, world map, embedded map or opening hours; the other three named at the foot with what they are; the plain `data-region="page-context"` block with the one `<h1>`; the media counts per study (2, 1, 1, 0, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S27-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered rows | ghost `∴` behind the city | THE OFFICE as the eyebrow with a house mark, the city as h1; address row of obvious placeholders; HOW TO GET IN as a bordered row of four with word-numerals beside the door as a 3:2 field; three labelled fields, WHAT IS NOT HERE on `--no`; the map slot as a bare 6:1 field that says it is a slot; the other three on the pencil rule | 2 (3:2 door, 6:1 slot) · 13 | 196 |
| `CONS-S27-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one measure | pencil ellipse round *London* | The city at display size; the address as one line; the door as a 2:1 field — the lead image is the door, not the building — with V1's caption; four ruled step lines with word-numerals; three fact lines, the last on `--no`; the close on the pencil rule. No map slot | 1 × 2:1 · 13 | 193 |
| `CONS-S27-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — arrival sequence and rail | ruled margin behind | Four joined bordered step modules; two fields beneath; rail on the band tone with the pencil rule — ADDRESS, the map slot as a bare 4:3 field, WHO IS BASED HERE, NOT OFFICES with the other three as links and what they are. No door field, no sticky rail | 1 × 4:3 slot · 13 | 179 |
| `CONS-S27-004` | Conversion-led | 004 White & Signal | 4 — the hour is in this room | underline stroke under *this room* | Identity with the address as a ruled column; steps as a bordered row with STEP ONE… chips; three fields; THE HOUR IS IN THIS ROOM as a band with the pencil rule, a statement and not a booking; foot. No field, no slot | none · 13 | 213 |
| `CONS-S27-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — written to somebody outside | bracket grouping the arrival sequence | The four sentences as ruled lines at display size, word-numerals and the key phrase of each in the accent; YOU HAVE ALREADY USED THIS as the address row; ONCE YOU ARE UP as three lines, the last on `--no`; the other three on the pencil rule. No field, no slot | none · 13 | 205 |

## What changed from V1

The step numbers `01`–`04` become the serif word-numerals *One*–*Four* (STEP ONE… chips in 004), so the only digits on the page are the obvious placeholders; *What is not here* is on the `--no` edge everywhere; the map slot is a bare labelled field that names itself a slot; the door is a bare labelled field where it appears. Cards, filled panels and the badge go; the darkened surfaces are the 003 rail and the 004 band. Copy is V1's throughout; every placeholder keeps its marking.

## Verification

- `cslcheck.ps1 -Sec S27 -Fields 'The office|London|room of twelve|00 Example Street|EC0A 0AA|0000 0000|example.com|sandwich shop|marked|fob|by name|Farringdon|A. Whitfield|No parking|Manchester|Frankfurt|Singapore'` — ALL CHECKS PASS; parity 85/85. Thirteen placeholders per study, declared. One `<h1>` per study; no header, nav or footer element; no form; no script; no remote URL, embedded map or gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no opening hours, skyline or world map.
- Rendered and read at 1440. Corrections: the 001 ghost glyph enlarged to read at size and the map slot shortened to 6:1; the 002 door field set to 2:1 in its measure.
