# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S04` — Conditions Treated · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the six area names, every condition named, the first-visit lines, the not-treated-here refusal and the ask kept word for word; **conditions named and nothing more**, with no outcome, rate, cure or promise attached to any of them — are kept exactly. V1's own reserved-area count per study is kept: one in 001, 002 and 005, none in 003 and 004.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S04-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the six areas read down one measure | column rules behind the head | Head split; six three-column ruled rows on the lead rule; a closing band on the band tone with the 4:3 examination room, the refusal and the ask | 1 reserved · 0 | 188 |
| `HC-S04-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the list read beside one tall field | open bracket at the copy head | The 3:4 lamp field down the left beside a bracketed reading column of six ruled rows | 1 reserved · 0 | 187 |
| `HC-S04-003` | Structured / Visual Modular | 003 Sky & Slate | C | 3 — the six areas as shared cells | bordered cell grid, 1px lines shared | Six cells, conditions as hairline-ruled lists; the refusal spanning the closing row on the band tone | none · 0 | 184 |
| `HC-S04-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the ask standing beside the list | measure rule under the key phrase | The not-listed panel on the band tone and the refusal in a side column, beside six ruled rows | none · 0 | 189 |
| `HC-S04-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the areas read along the corridor | corner frame at the head | Framed head; the 4:5 corridor field beside six ruled rows on the lead rule, offset inward | 1 reserved · 0 | 187 |

## What changed from V1

V1's rounded condition cards go, and so does **V1's tag treatment in 003**: the register rules out pill tags outright, so the condition list is set as a hairline-ruled list — one condition per line, ink on paper, no chip, no border, no fill. The headline is the display `<h2>` with `the useful part.` in the accent, and in 004 under the measure rule. Each area is a ruled row carrying the condition line in ink and V1's first-visit line in the muted tone, so what is named and what actually happens are visibly different kinds of statement. **V1's not-treated-here refusal is set in the graphite refusal tone** in every study, which is the point of the section: what the clinic will not do, and where you go instead, reads as a limit rather than as small print.

**No SVG, no icon, no badge.**

## Verification

- `hccheck.ps1 -Sec S04 -Fields 'What we treat|Naming it is the easy part|…|Tell us what is wrong'` — ALL CHECKS PASS; parity 120/120. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; no placeholder in this section; the single ask held at `#`, as V1 left it.
- Rendered and read at 1440.
