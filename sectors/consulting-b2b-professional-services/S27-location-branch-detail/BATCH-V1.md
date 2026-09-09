# BATCH V1

## Batch Identity

- Sector: `Consulting & B2B Professional Services`
- Prefix: `CONS`
- Section ID: `CONS-S27`
- Section Name: `Office Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

**The last batch in the sector.** Seventh of the extended architecture roles, twenty-seventh overall.
`CONS` closes at **135 studies — S01 to S27, complete.**

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Slots | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `CONS-S27-001` | Universal / Safe | 001 Paper | **B** | Address first, **how to get in** as four steps beside the door, then a map slot | 2 | 189 |
| `CONS-S27-002` | Premium / Editorial | 002 Sable | **B** | One measure. **The lead image is the door, not the building** | 1 | 190 |
| `CONS-S27-003` | Dense / Information-heavy | 003 Field | **B** | The arrival sequence as joined modules; **the address demoted to a rail** | 1 | 175 |
| `CONS-S27-004` | Conversion-led | 004 Signal | **C** | **The hour is in this room** — the sector's single ask, finally given a place | **0** | 213 |
| `CONS-S27-005` | Sector-native / Distinctive | 005 Midnight | **C** | **Written to somebody standing outside** — the arrival lines are the display type | **0** | 204 |

## The Section Role

One physical place: where it is, what happens there, and how to reach it.

## The Trap

`S17` already disposed of three reflexes for this sector — the embedded map (a remote dependency the
catalog forbids), the drawn world map (four pins is not a network) and the skyline (a named
anti-pattern). What is left is the trap this role invites all by itself, and the README names it:
**fabricating a plausible address.**

## The Governing Idea

> **Every office page tells you where the building is. Nobody tells you how to get in.**

The address is the easy part and the part a search engine already has. What is missing everywhere is
the last hundred metres: which door, which floor, what to press, who to ask for. **A visitor standing
on the street with the right postcode and the wrong door is the ordinary outcome of every location
page in this sector.**

So *How to get in* is a first-class section in all five studies, and it names the thing that actually
catches people:

| | |
| --- | --- |
| **The door** | The one beside the sandwich shop, not the glass one on the corner |
| **The bell** | There is no reception. Ring the one marked `four` |
| **The lift** | It needs a fob, so somebody comes down for you |
| **Who to ask for** | The person you are meeting, by name. We have no front desk |

## The Place All Five Render

**London — the office.** `S17` printed four locations and said which of them was which; this is the
one of the four that is an office, and **the room of twelve is this room** — the room `S15`'s session
sits in and `S19`'s hour happens in. The other three are named at the foot of every study with what
they actually are, so a detail page cannot be read as implying four rooms like this one.

## Placeholders, Which This Role Is Strict About

The README: *every address, coordinate, hour and contact route in a study must be an obvious
placeholder. Fabricating a plausible address is the failure mode this role invites.*

Every one is deliberately impossible to mistake for real — `00 Example Street`, `EC0A 0AA`,
`+44 (0)20 0000 0000`, an `example.com` address — and all are marked `data-placeholder="true"`. A scan
confirms all three appear in all five studies in that form.

## The Map Slot

**A map area is a slot, never a service.** `001` and `003` reserve one and its label says what it is;
`002`, `004` and `005` carry none and each says why. No study contains a remote URL, an embedded map,
or any third-party script — a scan confirms zero `https://` in any body.

The README also requires address and contact details to be **first-class on a phone and never pushed
below decorative media**. In every study the address is above both reserved areas in source order.

## The Five Compositions

- **`001`** — the safe complete page: address on a rule, the four steps beside the door, the three
  facts across, the map slot, the other three at the foot.
- **`002`** — the lead image on a location page is the building shot from across the street, and it is
  useless twice over: the reader is not looking for the building from that angle, and every building
  in the district looks like it. **The one photograph that does any work is the door.** It runs at
  strip proportion immediately under the address, captioned *not the building*.
- **`003`** — the dense reading is not more facts but an inversion: **the arrival sequence promoted to
  the body and the address demoted to the rail** where a reader checks it rather than reads it. A
  location page's body is conventionally the address and a picture with directions in small type at
  the bottom, and that proportion is exactly backwards for the one visitor who is actually coming.
- **`004`** — every conversion path in this sector ends at the same sentence. `S19` offers the hour,
  `S20` makes it the only ask on the page, `S23` prices what it costs the buyer, `S26` names who it is
  with. **None of them says where it happens.** This page closes the loop: the hour is in this room,
  and the four steps above are what you need to walk into it. **A location page that tries to sell has
  misread why anyone opened it.**
- **`005`** — **the page is written to somebody already standing outside.** Second person, present
  tense, at display size: *the glass door on the corner is not us.* Every other study describes the
  arrival from a distance; this one addresses the single reader who is out of time, holding a phone,
  looking at two doors — the reader the page exists for and the only one it can still help. The
  address, which they have already used, is set small underneath.

`005` is the sector-native reading because the catalog has spent twenty-seven sections replacing
performance with things a reader can check — a count instead of an impression, a withheld line instead
of a claim, an error instead of an arc. **A door instruction is the smallest and most literal version
of that**, and a location page is the last place it can be made. `S17` refused to call a registered
address an office; this refuses to call a postcode directions.

## What This Section Will Not Do

- **No list of all locations.** That is `S17`.
- **No fabricated address, coordinate, phone number or opening hours.**
- **No embedded third-party map, no drawn world map with pins, no remote dependency of any kind.**
- **No review, rating or claim attributed to the location.**
- **No skyline, no glass tower.**
- **No form. No global header or navigation.**

## Verification Record

- Word band `150–230` (detail page): **189 / 190 / 175 / 213 / 204.** All five in band, headers synced.
- Tag balance: **0 unbalanced elements.** No `<script>`, `<iframe>`, `<img>`, `<svg>`, `<form>`,
  `<button>`, `<table>`, inline `style` or `position: sticky` anywhere.
- Field-parity scan across fourteen shared fields: **complete in all five.**
- Map-service scan, remote-URL scan, skyline scan, gendered-pronoun scan: **all clean.**
- Placeholder-address scan: **obvious in all five.**
- Theme conformance: **135/135 studies in the sector.**
- Composition collisions: **no exact match.** The sector's near-match count holds at 14; `S27` adds
  none.
- Structure check: the same **3 intentional FAILs** as before this batch — the rail helpers in
  `CONS-S02-002`, `CONS-S05-005` and `CONS-S11-003`, unchanged since `S11`.

### Found only by rendering

- `001` — the door slot was a fixed `3 / 4` beside a four-step list, leaving roughly **165px of void**
  under the steps. The row is now `align-items: stretch` and the slot has no ratio, so the photograph
  is exactly as tall as the instructions it belongs to. This is the fifth batch running where a fixed
  media ratio beside a shorter text column produced the same defect; **sizing a reserved area to its
  neighbour rather than to a ratio is the general fix.**
