# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S09` — Parts & Accessories · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A parts section is normally a catalogue with prices and part numbers, all of which the contract forbids. What is left is what a good counter actually does — and what it declines to do:

> **Parts we keep, and parts we will *not* sell you.** What is on the shelf, and what the counter says when you do not need it.

Six things, each with its condition attached rather than its price:

- **Tyres** — measured off your car, not a screen.
- **Brakes** — pads and discs. *The old ones come back with you.*
- **Batteries** — tested before it is sold. **If yours holds charge, it stays in.**
- **Wiper blades** — fitted at the counter while you wait.
- **Bulbs** — the right one, fitted, not a box you fail with later.
- **Oil and filters** — what the book says for your engine, *not what is nearest the till*.

Then the limit, which is the section's whole argument:

> **What the counter will not do:** sell you a part that is not worn out, order something it cannot fit, or read a code off your car and turn it into a shopping list.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S09-001` | Universal / Safe | 001 Chalk & Racing Green | A | 1 — a three-up item grid of objects | the bay lines behind the head | 7 reserved · 0 | 169 |
| `AUTO-S09-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the six as ruled editorial rows | the plate edge at the head | 1 reserved · 0 | 146 |
| `AUTO-S09-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the six in two ruled columns on a sheet | bordered plate, 1px lines shared | 2 reserved · 0 | 150 |
| `AUTO-S09-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *not*, measured | the torque mark under *not* | none · 0 | 142 |
| `AUTO-S09-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | A | 5 — the six as a square grid, offset | the ramp frame | 6 reserved · 0 | 165 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: the conversion-led reading is the six lines and the condition on each, and six photographs of consumables would slow the only decision on the page.

**Two studies are `A`.** Every item field is **the thing the copy names** — the tyre, the disc and pad, the battery, the wiper blade, the bulbs, the oil and filter — which is the one way an item grid can be honest in this sector. 001 sets them at 4:3 three-up, 005 at 1:1 in the same grid, offset onto the band tone inside the ramp frame.

## Verification

- `autocheck.ps1 -Sec S09 -Fields 'Over the counter|Parts we keep|Tyres|Brakes|Batteries|Wiper blades|Bulbs|Oil and filters|What the counter will not do'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<input>`, `<button>`, `<iframe>`, `<img>`, `<table>` or remote reference**; nothing that prices and no basket; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no price, part number, stock count, brand, fitment code or manufacturer**; no rating, award or urgency device; no digit in visible copy outside the field ratio labels; no placeholder in this section. Both links point at same-variant S08 and S19 studies.
- Rendered and read at 1440. Correction: 001 measured 171 words, one over the standard band, because seven slate labels count; two item lines were tightened by a word each.
