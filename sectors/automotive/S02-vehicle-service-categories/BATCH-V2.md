# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S02` — Vehicle Service Categories · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- Original authoring record: [BATCH-V1.md](BATCH-V1.md). Only the **design layer** is re-authored.
- Batch Status: `RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## What was kept

V1's content spine: the eyebrow *Browse by category*; the heading *Start with the kind of vehicle you need*; the lead *Four ways into the range. Pick the one that matches how you drive.*; the four categories with V1's own descriptions — **SUV** *space and versatility for everyday routes* · **Sedan** *comfort and balance for the daily drive* · **Electric** *quieter driving, with charging built into the routine* · **Performance** *sharper handling and a more focused drive*; the per-category *Explore* link and the *All categories* index action.

V1 spread five different category sets across its five studies. The canonical set is V1-001's, and all five studies now carry it, which is what makes content parity measurable.

## What was added, and why

One block, the contract's required limit:

> **What is not on this page:** a price, a payment, a figure or a badge. A category tells you the shape of a journey, not the cost of one — and if none of these is yours, the team will say so rather than sell you the nearest.

## What changed

**V1's per-category media tiles are gone.** The contract allows three media subjects — the place the work happens, people named by role only, the thing the copy names — and forbids a vehicle presented as a specific vehicle. A photograph standing for "SUV" is exactly that. The categories are **hairline rows** instead: the name in ink, the line in the muted tone, one underlined link, separated by 1px rules rather than boxed as cards. Each study keeps **one** reserved area, of a place: the showroom floor, the forecourt, the road outside, the yard.

**V1-004 built its categories from scripted button elements** carrying `data-name`, `data-desc`, `data-cta` and `data-media`, with a radio role. The dependency list forbids the control and the register forbids the interaction; it is re-authored as the same four links.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S02-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — head straight, categories on the lead rule | the bay lines behind the head | 1 reserved · 0 | 113 |
| `AUTO-S02-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the categories as an editorial index | the plate edge at the head | 1 reserved · 0 | 116 |
| `AUTO-S02-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the categories as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 0 | 117 |
| `AUTO-S02-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — the choice, measured | the torque mark under *need* | none · 0 | 109 |
| `AUTO-S02-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — an offset band-tone list | the ramp frame | 1 reserved · 0 | 112 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: the conversion-led reading is the choice itself — four names, four lines, four links, nothing between the reader and the decision. **002 numbers the categories in words** (`One`…`Four`) in the bordered chip, which is this register's index device; no digit appears in visible copy anywhere.

## Verification

- `autocheck.ps1 -Sec S02 -Fields 'Browse by category|Start with the kind|Four ways into the range|SUV|Sedan|Electric|Performance|All categories|What is not on this page'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<input>`, `<button>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no manufacturer, model, badge, plate, price, payment, rate, figure, rating or urgency device; no digit in visible copy outside the field ratio labels. All links point at the same-variant S03.
- Rendered and read at 1440. Correction: the content note quoted the V1 control by its tag name, which the dependency check reads out of the comment as a real dependency; the note now names it in words.
