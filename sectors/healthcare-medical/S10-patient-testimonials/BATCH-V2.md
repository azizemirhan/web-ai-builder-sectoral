# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S10` — Patient Testimonials · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the three printing conditions, the ledger labels in 003, the were-you-seen-here panel in 004 and both closing lines kept word for word — are kept exactly. **Every quotation is reserved and empty**: no testimonial, name, initial, attribution, star rating, review count or outcome appears, and the reserved attributions say how the person asked to be described, never who they are. V1's own reserved-area count per study is kept: none in 001 and 003, one in 002, 004 and 005.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S10-001` | Universal / Safe | 001 Linen & Sage | C | 1 — three empty quotations, side by side | column rules behind the head | Three reserved quotation blocks on the band tone; three printing conditions on the lead rule | none · 0 | 156 |
| `HC-S10-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — one quotation given the measure, two beneath | open bracket at the head | A wide reserved quotation with two smaller ones paired beneath, beside a 4:5 field of two chairs | 1 reserved · 0 | 160 |
| `HC-S10-003` | Structured / Visual Modular | 003 Sky & Slate | C | 3 — the three empty places as a ledger | bordered cell grid, 1px lines shared | Three printing conditions on the lead rule; a three-row ledger of Said / Described as / Printed since, every value reserved | none · 0 | 178 |
| `HC-S10-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the invitation beside the empty places | measure rule under the key phrase | Three stacked reserved quotations beside the were-you-seen-here panel on the band tone and a 4:3 desk field | 1 reserved · 0 | 167 |
| `HC-S10-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — one quotation staged | corner frame at the head | A staged reserved quotation at statement size, offset inward; a row of two smaller ones with the empty waiting room at 4:3 | 1 reserved · 0 | 155 |

## What changed from V1

The whole section is an argument for an empty space, and the re-authoring makes the emptiness deliberate rather than unfinished. Each reserved quotation is a block on the band tone opened by a quotation mark set at display size in the accent — **type, not an icon** — with V1's reserved line in the muted tone and the reserved attribution as a tracked uppercase label on a hairline. In 005 the first quotation is staged at statement size against the empty waiting room, so the empty chairs and the empty quotations make the same point.

V1's rounded testimonial cards go. The headline is the display `<h2>` with `stays empty.` in the accent, and in 004 under the measure rule. The three printing conditions are ruled rows on the lead rule; in 003 the three places become a shared-line ledger whose Said / Described as / Printed since are bare labelled fields. **V1's `tag` chip in 004** becomes the register's tracked uppercase label, and the what-you-will-not-read-here refusal is set in the graphite refusal tone.

**No SVG, no icon, no badge, no star, no rating control and no review widget.**

## Verification

- `hccheck.ps1 -Sec S10 -Fields 'In their words|Nothing here is written by us|…|not a prediction of yours'` — ALL CHECKS PASS; parity 75/75. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary — *a star rating* and *a number of reviews* appear only inside V1's refusal, as things the page will not carry; no placeholder in this section. The one action, in 004, is held at `#` for S19, as V1 left it.
- Rendered and read at 1440.
