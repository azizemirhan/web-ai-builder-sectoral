# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S13` — Customer Reviews · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids a rating, a review count, a star, a testimonial attributed to a customer, and the review-card-with-portrait anti-pattern. That removes the whole conventional section and leaves the argument:

> **A review you cannot *trace* is an advertisement.** Anything quoted here comes with where it was left and when. Until it does, the space stays empty.

**Where to read them** — three reserved fields: *left where* (a platform this business does not control), *how many* (a count taken from that platform, not typed here), and **including the bad ones** — a route to the unfiltered list.

> **What you will not find here.** No star, no score, no quote with a first name and an initial under it. A rating we typed is a rating we chose. If a number appears on this page it will come from somewhere you can open yourself.

And the part that is true today:

> **What happens to a bad one.** Somebody reads it, rings the person, and fixes the thing if it can be fixed. None of that gets posted here either.

**Not one quotation appears in any of the five studies.**

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S13-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the fields on the lead rule, refusal opposed | the bay lines behind the head | 1 reserved · 3 | 147 |
| `AUTO-S13-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the refusal set as the page | the plate edge at the head | none · 3 | 143 |
| `AUTO-S13-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the fields as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 3 | 152 |
| `AUTO-S13-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *trace*, measured | the torque mark under *trace* | none · 3 | 143 |
| `AUTO-S13-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the fields framed against the key | the ramp frame | 1 reserved · 3 | 148 |

All five sit inside the contract's standard band of 90–170.

**Two studies are `C`, and each records why.** 002: the editorial reading puts the refusal at the top at full measure, and a photograph under it would be exactly the picture a testimonial card carries. 004: a page with no quotation on it has no face to put beside one.

## What was designed

The media is the moment a review is actually about, and it is a **place or an object, never a customer**: the handover desk at the end of a job, and the key being handed across the counter. There is no portrait, no quotation mark as ornament, no star glyph, no pager and no carousel.

The third reserved field, *including the bad ones*, is the longest label in the register and sits last, which puts the hardest promise at the bottom of the block where a rating would normally be.

## Verification

- `autocheck.ps1 -Sec S13 -Fields 'What people said|A review you cannot|Where to read them|Left where|How many|Including the bad ones|What you will not find here|What happens to a bad one'` — ALL CHECKS PASS; parity 40/40. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no quote, name, initial, star, score, rating or count**; no manufacturer, model, badge or plate; no price, figure, award or urgency device; no digit in visible copy outside the field ratio labels; three placeholders per study. Both links point at same-variant S08 and S19 studies.
- Rendered and read at 1440. Correction: the action helper was named `tell`, which collides with a Perl built-in and silently produced five broken files; it is now `tellus`, and the five were regenerated and re-checked.
