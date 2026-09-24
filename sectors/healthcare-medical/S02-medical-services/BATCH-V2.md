# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S02` — Medical Services · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the six area names and their lines, the first-visit lines in 003, the emergency refusal and the ask kept word for word; the area names left as neutral category vocabulary with no diagnosis and no treatment promise attached — are kept exactly. V1's own reserved-area count per study is kept: one in 001 and 004, none in 002 and 005, six in 003.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S02-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the six areas read down one measure | column rules behind the head | Head split; six ruled area rows on the lead rule beside the 4:5 consulting room; the refusal and the ask as the foot | 1 reserved · 0 | 148 |
| `HC-S02-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the six areas as an editorial index | open bracket at the head | Bracketed head; six areas in three ruled columns on the lead rule; the refusal and the ask as the foot | none · 0 | 145 |
| `HC-S02-003` | Structured / Visual Modular | 003 Sky & Slate | A | 3 — the six areas as shared cells | bordered cell grid, 1px lines shared | Six cells at 4:3 — the couch, the physiotherapy room, the monitor, the room, the children's corner, the nurse's room — each with V1's first-visit line; a closing band on the band tone | 6 reserved · 0 | 211 |
| `HC-S02-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the ask standing beside the list | measure rule under the key phrase | The ask panel on the band tone beside six ruled area rows; a 21:9 reception field with the refusal beneath | 1 reserved · 0 | 147 |
| `HC-S02-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the six areas as a framed index | corner frame at the head | Framed head with the lead opposite; the index opened by word-numeral chips ONE to SIX on the lead rule, offset inward | none · 0 | 151 |

## What changed from V1

V1's rounded service cards and its plain stacked list go. The headline is the display `<h2>` with `what is wrong` — the thing the section is actually organised around — in the accent, and in 004 under the measure rule. The six areas are structured by one 3px accent lead rule and hairlines: ruled name-and-line rows in 001 and 004, three ruled columns in 002, shared cells in 003, a word-numeralled index in 005. **V1's emergency refusal is set in the graphite refusal tone** rather than as ordinary body copy, so the sentence that says what the clinic will not do reads as the limit it is. Each reserved area is a bare flat field with its slate label inside the bottom-left corner, at 6px.

**No SVG, no icon, no badge.** The 005 index is numbered with word-numeral chips, never a digit; the 003 device is the bordered cell grid itself; the 004 measure rule is the key phrase's own border with two CSS risers.

## Verification

- `hccheck.ps1 -Sec S02 -Fields 'What we see|Start from what is wrong|…|Tell us what is wrong'` — ALL CHECKS PASS; parity 90/90. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; no placeholder in this section, so no `placeholder-data` meta; the single ask held at `#`, as V1 left it.
- Rendered and read at 1440. Correction: in 005 the index rows were given a fixed 4.6rem chip column — with an `auto` column the differing chip widths (ONE against THREE) pushed the area names and their lines to six different left edges.
