# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S03` — Featured Vehicles · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A featured-vehicle section cannot name a vehicle without naming a manufacturer and a model, which the contract forbids. So the four vehicles are **bracketed placeholders**, and the page is about the only thing that is true whoever they turn out to be:

> **Featured means somebody *chose* it.** Four cars are out at the front this week. They were picked by the people who service them, not by what they cost.

Each row carries a reserved name, the **category it belongs to** — SUV, Sedan, Electric, Performance, taken from this sector's own S02, so no category is invented — a reserved reason it is out front, and one link that books it in. Then the turnover note, *the four change when the workshop says they should, not on a Monday*, and the limit:

> **What is not here:** a price, a payment, a badge, a mileage or a registration. A car that is right for you stops being right the moment a number is used to talk you into it.

Eight placeholders per study: four vehicles, four reasons.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S03-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — head straight, rows on the lead rule | the bay lines behind the head | 1 reserved · 8 | 142 |
| `AUTO-S03-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the reserved rows as an editorial index | the plate edge at the head | none · 8 | 143 |
| `AUTO-S03-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the page as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 8 | 145 |
| `AUTO-S03-004` | Conversion-led | 004 Bone & Aubergine | B | 4 — *chose*, measured | the torque mark under *chose* | 1 reserved · 8 | 142 |
| `AUTO-S03-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | C | 5 — the reserved list framed | the ramp frame | none · 8 | 139 |

All five sit inside the contract's standard band of 90–170.

**Two studies are `C`, and each records why.** 002: every car on the page is a reserved name, and a photograph beside four empty names would be the only specific thing on it. 005: the distinctive reading takes the page at its word — if the four are reserved, nothing stands in for them.

## What was designed

The reserved rows are the composition, not a defect in it. Each is a four-part grid — reserved name in ink at 1.1rem, category in tracked accent caps, reserved reason in the muted tone, one underlined link — separated by hairlines, never boxed. 002 numbers them in words in the bordered chip.

Media, where it exists, is a **place or an object, never a car**: the forecourt at 4:3 and 21:9, the key on the counter at 16:9 and 1:1. The key is the object the visit ends with, which is why the conversion-led 004 is the variant that keeps it.

## Verification

- `autocheck.ps1 -Sec S03 -Fields 'This week on the forecourt|Featured means somebody|On the forecourt this week|Book it in|What is not here|Arrange a test drive'` — ALL CHECKS PASS; parity 30/30. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no manufacturer, model, badge, plate, price, payment, rate, mileage, figure, rating or urgency device; no digit in visible copy outside the field ratio labels; eight placeholders per study, declared in the `placeholder-data` meta. All links point at same-variant S08 and S20 studies.
- Rendered and read at 1440.
