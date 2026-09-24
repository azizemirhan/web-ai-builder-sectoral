# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S09` — Results / Before and After · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the four before-and-after pairs, the row labels in 003, the distance panel in 004, the your-own line and the not-shown-here refusal kept word for word — are kept exactly. **The comparison is the visitor's own**: the two reserved areas are their first-visit record and their follow-up record, left empty, and no other patient's photograph, outcome or figure appears anywhere. V1's own reserved-area count per study is kept: two in 001, 003, 004 and 005, none in 002.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S09-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the two columns, then the two records | column rules behind the head | Two hairline-split columns on the lead rule; the two reserved records at 4:3 with the your-own line | 2 reserved · 0 | 140 |
| `HC-S09-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the pairs read across one rule | open bracket at the head | Two tracked column labels; four pairs as ruled rows, before in the muted tone and after in ink | none · 0 | 133 |
| `HC-S09-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the comparison as a three-column ledger | bordered cell grid, 1px lines shared | Head with two 4:3 records; a four-row ledger with the after column on the band tone | 2 reserved · 0 | 151 |
| `HC-S09-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the distance named | measure rule under the key phrase | Two hairline-split columns beside the distance panel on the band tone and the two 4:3 records | 2 reserved · 0 | 158 |
| `HC-S09-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the comparison as a diptych | corner frame at the head | Two halves offset inward, each opening with its own 4:3 record, the after half on the band tone | 2 reserved · 0 | 140 |

## What changed from V1

This is the section the sector's anti-pattern list warns about most — *before/after evidence grids presented as proof* — and the re-authoring holds V1's answer to it. There is **no image pair, no slider, no outcome and no other patient**. The comparison is made in words, and the only two reserved areas are the visitor's own records, bare flat fields labelled `YOUR FIRST-VISIT RECORD · 4:3` and `YOUR FOLLOW-UP RECORD · 4:3`.

V1's rounded panels go. The headline is the display `<h2>` with `your own.` in the accent, and in 004 under the measure rule. The before column is set in the muted tone and the after column in ink — in 003 and 005 on the band tone — so the difference between the two states is carried by weight and surface rather than by a graphic device. V1's two hidden column labels and its hidden ledger header row are **kept hidden from assistive technology exactly as V1 set them**, because each row already reads as a pair. **V1's `tag` chip in 004** becomes the register's tracked uppercase label, and the not-shown-here refusal is set in the graphite refusal tone throughout.

**No SVG, no icon, no badge.**

## Verification

- `hccheck.ps1 -Sec S09 -Fields 'Before and after|The only before-and-after that is honest|…|Book a first appointment'` — ALL CHECKS PASS; parity 90/90. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; no placeholder in this section. Every booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440.
