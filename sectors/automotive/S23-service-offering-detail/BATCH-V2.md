# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S23` — Service / Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A detail page needs one real offering, and inventing a treatment or a package would invent content. So the page is the detail view of **a job this sector's own S04 already names** — *a service* — written out of that section's words.

> **A service, and everything that is *in* it.** One job, written out in full, so you can decide whether it is the one your car needs.

- **What is in it** — oil drained and replaced, filter with it; fluids topped and the levels written down; lights, wipers and tyres looked at and reported; brakes measured, and the reading put on the sheet.
- **What is not in it** — *anything found while looking. It gets quoted and it waits for your yes; **a service that quietly becomes three jobs is not a service**.*
- **How it runs** — one, you leave it or wait, either is fine; two, it goes on the ramp and somebody works through the list; three, you are told what was checked, what was found, **and what was left alone**.
- **Who it is for** — anybody whose car is due one, and anybody who is not sure whether it is. *If it is not due, the desk will say so.*

No price, labour rate, turnaround time, service interval or mileage appears anywhere.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S23-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the page read in order | the bay lines behind the head | 1 reserved · 1 | 180 |
| `AUTO-S23-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the editorial reading, baseline-opposed | the plate edge at the head | 2 reserved · 2 | 187 |
| `AUTO-S23-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the whole page as one plate | bordered plate, 1px lines shared | 1 reserved · 1 | 194 |
| `AUTO-S23-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *in*, measured | the torque mark under *in* | none · 0 | 172 |
| `AUTO-S23-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the page held in a frame | the ramp frame | 1 reserved · 1 | 180 |

All five sit inside the contract's detail band of 170–230.

**004 is the `C`**: the conversion-led reading of a detail page is the decision, and a photograph of a bench does not help anyone make it. It is the one study with no reserved area and therefore no caption, so its `placeholder-data` is declared as none.

## What was designed

**The refusal is a designed element, not a footnote.** *What is not in it* is set in the graphite `--no` tone with only the operative clause in ink, and it takes the one 3px accent lead rule the composition is allowed in 001, 002 and 005 — so the limit is the strongest horizontal on the page.

Media is a place or an object the copy names, never a vehicle: **the oil and filter**, which is the first line of the list; **the ramp** and **the workshop bay**; **the job sheet being written**, which is step three; and in 005 **the disc and pad** — the one item on the list that is measured rather than replaced by the calendar.

## Verification

- `autocheck.ps1 -Sec S23 -Fields 'What is in it|What is not in it|How it runs|Who it is for|Read next|Book the bay'` — ALL CHECKS PASS; parity 30/30. `<h1>` present and single (detail page); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no price, rate, time, interval, mileage or figure**; no manufacturer, model, badge or plate; no rating, award or urgency device; no digit in visible copy outside the field ratio labels. All links point at same-variant S09, S16 and S08 studies.
- Rendered and read at 1440.
