# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S15` — Showroom Gallery · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

This is the one section in the sector whose subject is media, and the contract's first media subject — **the place the work happens** — fits it exactly. No vehicle has to be named for a gallery of a building to be worth looking at:

> **Six rooms, and *none* of them tidied for the camera.** Where the work happens, photographed on an ordinary day. Nothing has been moved.

- **The showroom floor** — where a car sits while you decide.
- **The service reception** — where the job sheet starts.
- **The workshop bay** — where most of the day goes.
- **The ramp** — *the only view of the underside you get before you are told about it.*
- **The parts store** — shelves in the order somebody keeps them in.
- **The waiting room** — kettle, chairs, and a view of the bay.

Then the page's own photography rule:

> **No wide lens, no empty forecourt at dawn, and no car we do not have.** If a photograph is not of this building, it does not go up.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S15-001` | Universal / Safe | 001 Chalk & Racing Green | A | 1 — a three-up grid of 4:3 places | the bay lines behind the head | 6 reserved · 0 | 148 |
| `AUTO-S15-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — two long views around a ruled index | the plate edge at the head | 2 reserved · 0 | 133 |
| `AUTO-S15-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the index as one itemised sheet | bordered plate, 1px lines shared | 3 reserved · 0 | 137 |
| `AUTO-S15-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *none*, measured | the torque mark under *none* | none · 0 | 126 |
| `AUTO-S15-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | A | 5 — a two-up grid of 16:9 places, offset | the ramp frame | 6 reserved · 0 | 148 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**, and it is the study that tests the captions: a gallery with no photographs has to be worth reading, and what is left is the six rooms named and explained.

## What was designed

Every field is **a place in this building** — the first of the three media subjects — so the section carries six reserved areas without naming a single vehicle. 001 sets them three-up at 4:3; 002 replaces the grid with **two long views**, the bay at 21:9 and the showroom at 16:9, around a ruled index; 003 puts the index in a plate and sets the photography rule *between* the bay and the waiting room; 005 runs them two-up at 16:9 on the band tone inside the ramp frame.

No lightbox, no carousel, no pager, no captions floating over the image: the slate label is inside the field, the name and the line sit under it.

## Verification

- `autocheck.ps1 -Sec S15 -Fields 'The place itself|Six rooms|The showroom floor|The service reception|The workshop bay|The ramp|The parts store|The waiting room|No wide lens'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no manufacturer, model, badge or plate; no price, figure, rating, award or urgency device; no digit in visible copy outside the field ratio labels; no placeholder in this section. Both links point at same-variant S08 and S10 studies.
- Rendered and read at 1440. Correction: 005 was first laid out as a mosaic with the showroom spanning two columns at 16:9, which left a two-hundred-pixel hole beside the reception; it is now a two-up grid at 16:9, which also separates it cleanly from 001's three-up at 4:3.
