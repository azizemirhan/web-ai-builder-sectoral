# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S04` — Workshop Services · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A workshop-services section usually becomes a price list. The contract forbids a price, a labour rate, a turnaround time and a service interval, which leaves the honest version: **what each job includes, and where it stops.**

> **Four jobs, and what each one *includes*.** The work the bay does most. Each one says what is in it, and what is not.

- **One · A service** — oil, filter, fluids, lights, tyres and brakes looked at. *You get the sheet with what was checked and what was found.*
- **Two · Brakes** — pads and discs **measured rather than guessed**. The parts that came off go back in the boot.
- **Three · Tyres** — tread measured across the width, pressures set, wheels balanced. *If one has life left in it, it stays on.*
- **Four · Diagnostics** — the reader tells us where to look. **It does not tell us what is wrong; somebody still has to find it.**

Then the limit:

> **What is not on this page:** a price, a time, or a promise that your car will be ready today. The bay quotes after it has looked, and says so before it starts.

Three of the four job lines contain their own refusal — *if one has life left in it, it stays on* is the line a tyre bay is least likely to print — which is the reading working at the level of the sentence, not only the section.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S04-001` | Universal / Safe | 001 Chalk & Racing Green | A | 1 — the jobs as a four-up item grid | the bay lines behind the head | 5 reserved · 0 | 169 |
| `AUTO-S04-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the jobs as a ruled editorial list | the plate edge at the head | 1 reserved · 0 | 153 |
| `AUTO-S04-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the jobs as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 0 | 157 |
| `AUTO-S04-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *includes*, measured | the torque mark under *includes* | none · 0 | 150 |
| `AUTO-S04-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | A | 5 — the jobs as a square grid, offset | the ramp frame | 5 reserved · 0 | 169 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: a visitor deciding whether to book wants the four lines, not four photographs of parts.

**Two studies are `A`** — the sector's first — and they are entitled to it, because each job field is **the thing the copy names**: the oil and filter, the disc and pad, the tyre, the reader. That is the one media subject an item grid can honestly carry here; a photograph standing for a *category* could not.

## What was designed

The word-numeral in its bordered chip sits on the baseline of each job name rather than above it, so the four read as an itemised list even when they are laid out four-up. 001 sets the objects at 4:3 in a four-column grid; 005 sets them at 1:1 in the same grid, offset onto the band tone inside the ramp frame; 002 and 003 drop the objects and rule the four as rows.

Media is a place or an object throughout: the bay, the ramp, the tools, the job sheet — and the four job objects. No vehicle, no badge, no plate.

## Verification

- `autocheck.ps1 -Sec S04 -Fields 'In the workshop|Four jobs, and what each one|A service|Brakes|Tyres|Diagnostics|What is not on this page|Book the bay'` — ALL CHECKS PASS; parity 40/40. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no price, rate, time, interval, part number, figure, rating or urgency device; no digit in visible copy outside the field ratio labels. The one link points at the same-variant S08.
- Rendered and read at 1440. Correction: 001 and 005 first measured 173 words, three over the standard band, because five slate labels count as visible copy; the brakes line was shortened by five words and both now sit at 169.
