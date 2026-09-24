# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S08` — Service Booking · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The dependency list forbids `<form>`, `<input>` and `<button>`, so a booking section cannot book. Rather than mime one, the page says so in the heading:

> **Four ways in, and *none* of them is a form.** Nothing here books anything. It says which route to use, and what comes back.

**The four routes** — *at the desk* (walk in and say what the car is doing) · *by telephone* (reserved: the number and the hours it is answered) · *in writing* (reserved: the route and how long a reply takes) · *none of these* — **if it is not safe to drive, do not drive it here.**

**What we need from you** — what it is doing and when it started; whether it is safe to drive; and whether you need it back the same day: *we will say yes or no, not that we will try.*

Then the limit, which describes what a booking actually is:

> **There is no form on this page and no booking system behind it.** A slot is somebody writing your name in a diary, and they tell you the day before you hang up.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S08-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the four routes on the lead rule | the bay lines behind the head | 1 reserved · 2 | 165 |
| `AUTO-S08-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the refusal set as the page | the plate edge at the head | none · 2 | 161 |
| `AUTO-S08-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the routes as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 2 | 169 |
| `AUTO-S08-004` | Conversion-led | 004 Bone & Aubergine | B | 4 — *none*, measured | the torque mark under *none* | 1 reserved · 2 | 165 |
| `AUTO-S08-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the routes framed and offset | the ramp frame | 1 reserved · 2 | 165 |

All five sit inside the contract's standard band of 90–170.

**002 is the `C`**: two of the four routes are reserved values, and the editorial reading sets the four as an index and lets the empty lines stand.

## What was designed

The media is the booking, literally: **the booking diary open on the desk** at 16:9 in 003 and 4:3 in 004, and **the key cabinet behind the desk** at 3:2 in 005 — where a booking ends up. 001 and 003 open on the service reception, because route one is the desk.

The four routes are a three-part row — word-numeral in the bordered chip, route name in ink, what it is or what is reserved in the muted tone — and the two reserved routes sit in exactly the same rhythm as the two written ones, so the blanks read as decisions.

## Verification

- `autocheck.ps1 -Sec S08 -Fields 'Booking the bay|Four ways in|The four routes|At the desk|By telephone|In writing|None of these|What we need from you|There is no form'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<form>`, `<input>`, `<button>`, `<svg>`, `<script>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no `tel:` or `mailto:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no invented number, address, email or opening hour; no price, rate, turnaround promise, figure, rating or urgency device; no digit in visible copy outside the field ratio labels; two placeholders per study. Both links point at same-variant S04 and S10 studies.
- Rendered and read at 1440. Correction: the five first measured 175–183 words, over the standard band, and the lead, the fourth route and the refusal were each shortened; all five now sit at 161–169.
