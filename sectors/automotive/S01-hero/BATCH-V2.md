# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- Original authoring record: [BATCH-V1.md](BATCH-V1.md). Only the **design layer** is re-authored.
- Batch Status: `RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## What was kept

V1's content spine, word for word: the eyebrow *Vehicle range*; the heading *Every journey starts with the right car*; the lead *Browse the current range and find a vehicle that fits how you drive, where you drive, and who travels with you.*; the primary action *Explore the range*; the secondary *Arrange a test drive*; and the closing note *Speak to the team at your nearest showroom, or start online and continue the conversation in person.*

## What was added, and why

**One sentence.** The contract requires a stated limit on every page, and V1 had none:

> **What this page will not tell you:** a price, a payment or a figure. Those come from the car in front of you, not from a heading.

This is recorded as an addition rather than slipped in. A refusal removes a claim rather than making one, which is why it is the one line the pass allows itself to add to a V1 spine.

## What changed

V1's rounded media panel, filled primary action and card-assembled split go. The head is now a **serif display line** — Georgia at `clamp(2.3rem, 4.4vw, 4.2rem)`, weight 400, leading 1.02 — with **one italic word in the accent**, *right*, which is this register's emphasis device and appears once per composition. The primary action is a thin-bordered control at 2px radius, the secondary an underlined link; neither is filled.

**V1's media slot was "Vehicle media".** The contract allows three media subjects — the place the work happens, people named by role only, and the thing the copy names — and forbids a vehicle presented as a specific vehicle. The slot is therefore re-subjected to **the forecourt from the pavement**, which shows the range without naming a marque. 003 adds the showroom floor.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S01-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the head read straight | the bay lines behind the head | 1 reserved · 0 | 84 |
| `AUTO-S01-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the editorial reading, baseline-opposed | the plate edge at the head | 1 reserved · 0 | 84 |
| `AUTO-S01-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the head as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 0 | 88 |
| `AUTO-S01-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — the key word measured | the torque mark under *right* | none · 0 | 81 |
| `AUTO-S01-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the head framed | the ramp frame | 1 reserved · 0 | 85 |

All five sit inside the contract's hero band of 40–90.

**004 is the `C`**, and it records why: the conversion-led reading of a hero is the sentence and the action, and a photograph of a forecourt delays both. It is also the variant where *right* is measured by the torque mark instead of coloured, so the emphasis device is still used once.

## Verification

- `autocheck.ps1 -Sec S01 -Fields 'Vehicle range|Every journey starts|Browse the current range|Explore the range|Arrange a test drive|will not tell you'` — ALL CHECKS PASS; parity 30/30. `<h1>` present and single (hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no manufacturer, model, plate, price, payment, rate, figure, rating or urgency device; no digit in visible copy outside the field ratio labels. Both links point at same-variant S02 and S20 studies.
- Rendered and read at 1440.
