# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S10` — Dealership Locations · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids an invented address, coordinate, telephone number, opening hour, direction or map. A locations section under those rules is **a page of reserved fields**, and the heading makes the reservation the argument rather than the apology:

> **An address we have not checked is worse than *none*.** Where to find us, and what this page does when a detail changes.

**Each site** is four bare labelled fields, all reserved: *the street*, *what is there*, *getting in* (access and parking), *when it is open*.

Then two refusals, which are the section's real content:

> **Why there is no map.** An embedded map hands your visit to a third party, and a drawn one is out of date the week a gate moves. The street is above, and a telephone will do the rest.

> **What gets printed.** Nothing until it has been checked this month. A wrong address costs somebody a journey in a car that is already not right.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S10-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the fields on the lead rule, refusals opposed | the bay lines behind the head | 1 reserved · 4 | 133 |
| `AUTO-S10-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the road as the lead image | the plate edge at the head | 1 reserved · 4 | 134 |
| `AUTO-S10-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the site as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 4 | 137 |
| `AUTO-S10-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *none*, measured | the torque mark under *none* | none · 4 | 130 |
| `AUTO-S10-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the fields framed against the door | the ramp frame | 1 reserved · 4 | 134 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: every value on the page is reserved, and a photograph of a forecourt whose street has not been written would be the only settled thing on it.

## What was designed

The media answers the question a map would: **the forecourt from the pavement** (what you see once you have the right street), **the road outside the workshop door** at 21:9 (the last thing before the turning), and **the workshop door from the yard** — the two doors a visitor might actually be looking for. No pin, no coordinates, no tile, no directions service.

The four reserved values sit in the same bare labelled register used across this sector, and the two refusals are set as a matched pair — the map one takes the 3px accent lead rule in 002 and 005, the *what gets printed* one closes the page.

## Verification

- `autocheck.ps1 -Sec S10 -Fields 'Where we are|An address we have not checked|Each site|The street|What is there|Getting in|When it is open|Why there is no map|What gets printed'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>`, map embed or remote reference**; no `tel:` or `mailto:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no invented address, coordinate, number, hour or direction**; no manufacturer, model, badge or plate; no price, figure, rating or urgency device; no digit in visible copy outside the field ratio labels; four placeholders per study.
- Rendered and read at 1440.
