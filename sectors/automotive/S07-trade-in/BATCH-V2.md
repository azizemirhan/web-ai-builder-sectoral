# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S07` — Trade In · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

Every trade-in section on the web offers an instant valuation. The contract forbids a part-exchange figure, a mileage and a registration, which happens to leave the truthful version:

> **What yours is worth is a number we have not *seen* yet.** A valuation is a person looking at a car. Anything before that is a range somebody typed.

**How a figure gets made** — one, you tell us what it is and what it has had done; two, somebody looks at it, in daylight, with the doors open; three, **it goes on the ramp**; four, you get the figure in writing, *with what moved it up and what moved it down*.

**What you end up with** — *the figure* and *how long it stands*, both reserved.

Then the limit, which names the trick rather than just declining it:

> **No instant valuation, and no range.** A number produced before anybody has seen the car is not a valuation. It is an appointment in disguise, and you can have the appointment without the number.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S07-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the four steps on the lead rule | the bay lines behind the head | 1 reserved · 2 | 156 |
| `AUTO-S07-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the ramp as the lead image | the plate edge at the head | 1 reserved · 2 | 156 |
| `AUTO-S07-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the process as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 2 | 160 |
| `AUTO-S07-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *seen*, measured | the torque mark under *seen* | none · 2 | 153 |
| `AUTO-S07-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the steps framed and offset | the ramp frame | 1 reserved · 2 | 158 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: the conversion-led reading is the four steps and the appointment at the end of them, and a photograph is one more thing between a visitor and the ramp.

## What was designed

Each study's media is chosen to be **the step an instant valuation skips**: the ramp with a car up on it at 21:9 in 002 — step three — the inspection sheet on the clipboard in 003, and in 005 the tread being measured on the bench, which is the one thing on a car that is measured rather than estimated. 001 and 003 open on the yard, the place a car sits between arriving and being looked at.

The four steps are word-numbered in the bordered chip. The reserved figure sits in the same bare labelled register as everywhere else in this sector, and in the narrow plate cells the label stacks above its value rather than squeezing it.

## Verification

- `autocheck.ps1 -Sec S07 -Fields 'Your car|What yours is worth|How a figure gets made|What you end up with|The figure|How long it stands|No instant valuation|Book it in to be looked at'` — ALL CHECKS PASS; parity 40/40. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<input>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no valuation tool and nothing that computes; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no valuation, range, mileage, age, registration or part-exchange figure**; no manufacturer, model, badge or plate; no rating, award or urgency device; no digit in visible copy outside the field ratio labels; two placeholders per study.
- Rendered and read at 1440. Correction, applied across the sector: the bare labelled register kept its `11rem` label column inside the narrow cells of the 003 plate, which wrapped the reserved values onto three lines; the shared stylesheet now stacks the label above its value whenever the register sits in a plate cell.
