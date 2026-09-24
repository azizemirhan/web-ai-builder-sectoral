# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S24` — Fleet / Custom Build Case Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The section README carries a **Sector Semantic Limitation**: most depth in this sector sits in vehicle and inventory templates, which are out of S21–S27 scope, so this role *stays a record of completed work, not a vehicle page.*

The page is written **to** that limitation rather than around it, and says so in the heading:

> **A job written up, with no *vehicle* page behind it.** One piece of finished work, recorded the way the bay records it. The car it was done to is not the subject.

> **Why this is not a vehicle page.** Vehicle and inventory pages are a different thing, and this scaffold reserves them for later. What is here is the work: what came in, what was found, what was done, and what was left.

**All four stages of the record are reserved** — *what came in*, *what was found, including anything that was not expected*, *what was done*, and **what was left: work deliberately not done, and why** — because naming the work would name a customer, and the brief forbids fabricated clients.

What is *not* reserved is the standard the record is kept to:

> **What goes in a record.** The stage, the day, the part, and the name of whoever signed it. Four things, on one sheet, in the order they happened. A record written any other way is a story.

> **What this cannot show you.** A client, a figure, a before and after, or a quote from somebody who paid for it. None of those can be shown without showing the customer.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S24-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the limitation first, the record after | the bay lines behind the head | 1 reserved · 5 | 211 |
| `AUTO-S24-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the limitation set as the page | the plate edge at the head | none · 4 | 204 |
| `AUTO-S24-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the record as one plate, with the metadata | bordered plate, 1px lines shared | 1 reserved · 6 | 221 |
| `AUTO-S24-004` | Conversion-led | 004 Bone & Aubergine | B | 4 — *vehicle*, measured | the torque mark under *vehicle* | 1 reserved · 5 | 211 |
| `AUTO-S24-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | C | 5 — the page framed and emptied | the ramp frame | none · 4 | 204 |

All five sit inside the contract's detail band of 170–230.

**Two studies are `C`, and each records why.** 002: a page whose argument is that the vehicle is not the subject cannot open with a photograph of one. 005: the distinctive reading takes the page at its word — if the vehicle is not the subject and every stage is reserved, nothing stands in for either.

**003 is the only variant carrying the metadata** the brief allows — *Discipline: Workshop* and a reserved *Where* — which is why it has six placeholders against four and five.

## What was designed

Every reserved area is **a document or a part, never a vehicle**: the job sheet on the desk, the job sheet being written, and in 004 **the part that came off, on the bench beside the new one** — which is what *what was done* looks like when nobody is photographing a car.

The four stages are a three-part row — the word-numeral in its bordered chip, the stage name in ink, the reserved value in the muted tone — with the numeral column fixed at `5rem` so the stage names share one left edge. The limitation takes the one 3px accent lead rule in every variant.

## Verification

- `autocheck.ps1 -Sec S24 -Fields 'Why this is not a vehicle page|The record|What came in|What was found|What was done|What was left|What goes in a record|What this cannot show you'` — ALL CHECKS PASS; parity 40/40. `<h1>` present and single (detail page); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no client, fleet, company, figure, outcome, before-and-after or quotation**; no manufacturer, model, badge, plate, registration, mileage or price; no digit in visible copy outside the field ratio labels. All links point at same-variant S23, S11 and S08 studies.
- Rendered and read at 1440.
