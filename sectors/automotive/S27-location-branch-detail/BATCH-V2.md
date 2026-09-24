# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S27` — Dealership / Service Centre Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids an invented address, coordinate, telephone number, opening hour, direction or map. A location detail page under those rules is **a page of reserved fields**, and the design makes the reservation deliberate.

Nine reserved values: the site name (as the label and again as the `<h1>`), the street, the gate, parking, public transport, the telephone with the hours it is answered, the written route, and the opening context.

What is written is what stays true **whatever the address turns out to be**:

- **When you arrive** — one, the gate is on the street named above; two, the service desk is the first thing inside it; three, say the name you booked under. *Nothing else is needed.*
- **When it is open** — reserved, and under it: *An hour that has not been checked this month is not printed.*
- **Why there is no map** — *An embedded map hands your visit to a third party, and a drawn one is out of date the week a gate moves. The street is above, and a telephone will do the rest.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S27-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the page read as a journey | the bay lines behind the head | 2 reserved · 11 | 212 |
| `AUTO-S27-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the door as a panorama, fields at full measure | the plate edge at the head | 1 reserved · 10 | 205 |
| `AUTO-S27-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the location as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 11 | 212 |
| `AUTO-S27-004` | Conversion-led | 004 Bone & Aubergine | B | 4 — the reserved name, measured | the torque mark under the name | 1 reserved · 10 | 205 |
| `AUTO-S27-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | C | 5 — the location framed and left empty | the ramp frame | none · 9 | 198 |

All five sit inside the contract's detail band of 170–230.

**005 is the `C`**, and it records why: every value that locates this place is reserved, so a photograph of a gate would be the only certain thing on the page and would carry more weight than it has earned.

## What was designed

This is the one page in S21–S27 where reserved media is genuinely earned, and there are only two honest subjects for it: **the workshop door from the yard** and **the service reception** — the two things a visitor actually has to find. 001 and 003 carry both, 002 runs the door alone at 21:9, 004 sets it at 4:3 beside the fields, 005 carries neither.

The reserved fields are designed as a **sheet, not a contact card**: bare labelled rows on hairlines, no icons, no `tel:` link, no pin, no coordinates, nothing that could be dialled or opened. In the narrow plate cells the label stacks above its value.

*Getting here* takes the one 3px accent lead rule in 001 and 002 — the street is the reason the page exists — while 005 gives it to the map refusal and 003 and 004 to the foot.

## Verification

- `autocheck.ps1 -Sec S27 -Fields 'Getting here|The street|The gate|Reaching it|When it is open|When you arrive|Why there is no map|What happens here|Who is here'` — ALL CHECKS PASS; parity 45/45. `<h1>` present and single (detail page); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>`, map embed or remote reference**; no `tel:` or `mailto:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no invented address, coordinate, number, hour or direction**; no manufacturer, model, badge, plate, price or figure; no digit in visible copy outside the field ratio labels; nine to eleven placeholders per study.
- Rendered and read at 1440.
