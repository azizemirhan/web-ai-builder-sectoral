# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S17` — Offers & Packages · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

Offers are where the contract's two hardest bans meet: no price or discount, and no urgency device of any kind. The page is written to both:

> **An offer with a clock on it is a *tactic*.** Whatever is running is written here in full, with what it covers and what it leaves out. It runs until it stops.

**For each one that is running** — four reserved fields: *what it is*, *what it covers*, **what it leaves out, in the same size type**, and *who can have it*.

> **What will not appear here.** No countdown, no ending soon, no last few left, no price struck through with a bigger one beside it. If something is about to change we will say so in a sentence, not in a colour.

> **Where the small print goes.** In the third row, in the same size as the rest. An exclusion set smaller than the offer is an exclusion designed not to be read.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S17-001` | Universal / Safe | 001 Chalk & Racing Green | C | 1 — the fields on the lead rule, refusal opposed | the bay lines behind the head | none · 4 | 157 |
| `AUTO-S17-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the refusal over a blank-total sheet | the plate edge at the head | 1 reserved · 4 | 163 |
| `AUTO-S17-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the offer as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 4 | 167 |
| `AUTO-S17-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *tactic*, measured | the torque mark under *tactic* | none · 4 | 157 |
| `AUTO-S17-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the fields framed against the sheet | the ramp frame | 1 reserved · 4 | 163 |

All five sit inside the contract's standard band of 90–170.

**Two studies are `C`, and each records why.** 001: an offer page without an offer on it has nothing to photograph, and a picture here would be the thing doing the persuading. 004: this is the conversion-led direction on the section most tempted to convert, and the whole point is that nothing pushes.

## What was designed

**The exclusions row is the design.** It is the third field, set in the same type size and the same ink as the offer itself, and it is the one row in the register that carries a 3px accent edge down its left side — so the thing a promotion normally shrinks is the thing this page marks. The section's second refusal says so out loud.

The only media allowed is **the itemised sheet with the total line left blank**, because an offer is a line on that sheet or it is not an offer. Nothing counts down, nothing animates, there is no timer and no struck-through figure.

## Verification

- `autocheck.ps1 -Sec S17 -Fields 'What is on at the moment|An offer with a clock on it|For each one that is running|What it is|What it covers|What it leaves out|Who can have it|What will not appear here|Where the small print goes'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; nothing counts down or animates; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no offer, price, discount, percentage, deadline, countdown, stock count or scarcity line**; no manufacturer, model, badge or plate; no rating or award; no digit in visible copy outside the field ratio labels; four placeholders per study. Both links point at same-variant S08 and S19 studies.
- Rendered and read at 1440.
