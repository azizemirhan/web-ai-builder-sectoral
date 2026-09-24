# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S05` — Brands & Manufacturers · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

This role is normally a **logo wall**, which is the single thing the contract most clearly forbids: no manufacturer, wordmark, badge, shield or approval claim. Rather than delete the role, the page is written to the prohibition and becomes the sector's plainest refusal:

> **We will not print a badge we have no right to *use*.** Which makes the bay works on is a list somebody has to keep current. It is kept, and it is reserved here until it has been checked.

**Not one manufacturer is named in any of the five studies.** The two lists are bracketed placeholders — *equipped for* and *not taken, and where those go instead* — and the second list is the one a dealership never publishes.

Then the explanation, which is the reason the refusal is not just caution:

> **What a badge on a website means.** Nothing, unless the maker put it there. A manufacturer mark on a dealer page can mean a franchise, a training certificate, or a designer with a folder of logos. You cannot tell which from looking.

And the positive claim the page *can* make: the bay has the tools and the data for the makes on the first list, **and puts that in writing when you book**.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S05-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the lists on the lead rule | the bay lines behind the head | 1 reserved · 2 | 166 |
| `AUTO-S05-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the refusal set as the page | the plate edge at the head | none · 2 | 162 |
| `AUTO-S05-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the lists as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 2 | 169 |
| `AUTO-S05-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *use*, measured | the torque mark under *use* | none · 2 | 162 |
| `AUTO-S05-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the lists framed against a blank plate | the ramp frame | 1 reserved · 2 | 166 |

All five sit inside the contract's standard band of 90–170.

**Two studies are `C`, and each records why.** 002: a page whose argument is that you cannot tell what a mark means by looking at it does not open with a photograph. 004: the conversion-led reading is the question a visitor actually has — *will you work on mine* — and a picture does not answer it.

## What was designed

The media is chosen to say what "equipped for" means without a badge: **the parts store with its shelves in order** (001, 003), **the diagnostic reader** (003) — tools and data — and, in 005, **the blank plate on the bench with no registration on it**, which is the one object on the whole site that is deliberately unmarked.

The two reserved lists are a bare labelled register with a fixed `11rem` label column, not a card. The badge refusal carries the one 3px accent lead rule in 002 and 005 and is given the full measure at 1.08rem in 002, where it is the page.

## Verification

- `autocheck.ps1 -Sec S05 -Fields 'Makes we work on|We will not print a badge|The two lists|Equipped for|Not taken|What a badge on a website means|What we can say|Ask before you book'` — ALL CHECKS PASS; parity 40/40. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no manufacturer name, wordmark, badge or approval claim**; no price, rate, figure, rating, award or urgency device; no digit in visible copy outside the field ratio labels; two placeholders per study, declared in the `placeholder-data` meta. Both links point at same-variant S04 and S08 studies.
- Rendered and read at 1440. Corrections: 003 measured 172 words, two over the standard band, and the badge line was shortened by three; in 004 and 005 the *what we can say* label and its paragraph were landing as two separate cells of the two-column foot, and were wrapped.
