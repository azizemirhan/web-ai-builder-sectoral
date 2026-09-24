# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S25` — Ownership Guide / News Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids a diagnosis, a price, a part number and every performance figure, which rules out most of what an automotive "guide" normally is. What is left is the genuinely useful thing a workshop can publish: **an article about the appointment, not about the fault.**

> **How to describe a noise you cannot *point* at.** A short guide to the first thing you will be asked at the desk, written so you can answer it.

Four headings, each a real `<h2>`:

- **Start with when** — cold start, first corner, over bumps, only above a certain speed. *When beats what, every time.*
- **Say what it sounds like, not what it is** — grinding, ticking, whining, knocking, a rumble that rises with the wheels. Nobody expects the right word.
- **Say what changes it** — braking, steering, the clutch, the heater on. **If something makes it stop, that is the most useful sentence you have.**
- **Say what you have done** — anything replaced, topped up, or looked at elsewhere. It saves an hour of looking.

> **What this is not.** It does not say what the noise is, what it will cost, or whether it is safe to keep driving. It says how to be understood by somebody who can find out.

**The attribution is real structure with reserved values** — *Author* (by role) and *Last checked*, both bracketed — because a fabricated author or date is forbidden, and leaving the apparatus out would have been easier and less honest.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S25-001` | Universal / Safe | 001 Chalk & Racing Green | C | 1 — the article with its apparatus beside it | the bay lines behind the head | none · 2 | 185 |
| `AUTO-S25-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the editorial reading, offset column | the plate edge at the head | 1 reserved · 3 | 191 |
| `AUTO-S25-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the article as one plate, with contents | bordered plate, 1px lines shared | 1 reserved · 3 | 229 |
| `AUTO-S25-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *point*, measured | the torque mark under *point* | none · 2 | 185 |
| `AUTO-S25-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the article framed, body on the band tone | the ramp frame | 1 reserved · 3 | 194 |

All five sit inside the contract's detail band of 170–230.

**Two studies are `C`, and each records why.** 001: somebody who arrived to read four paragraphs is not helped by a photograph above them. 004: the conversion-led reading is getting somebody ready to speak at the desk, and a photograph delays that.

**003 is the only variant carrying the in-page contents** — four anchors to the article's own headings, verbatim, in the band-tone cell beside the reading column.

## What was designed

The article is a **reading column with its apparatus kept out of it**: what it is not, the attribution and the adjacent reading never interrupt the four sections. The accent falls on the last word of the title — *point* — which is the word the whole article is about; 004 measures it with the torque mark instead.

Media is a place or a document, never a car with a fault: **the ramp**, where a noise is finally found — which is not where it is described — the service reception, and **the job sheet being written**, because the article ends where the writing starts.

## Verification

- `autocheck.ps1 -Sec S25 -Fields 'Start with when|Say what it sounds like|Say what changes it|Say what you have done|What this is not|Written and checked by|Read next'` — ALL CHECKS PASS; parity 35/35. `<h1>` present and single, with four `<h2>` section headings beneath it; no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no diagnosis, part number, price, figure, mileage or performance claim**; no manufacturer, model, badge or plate; no digit in visible copy outside the field ratio labels; two placeholders per study, three where there is a caption; 003's four anchors resolve to its own heading ids.
- Rendered and read at 1440. Correction: 003 first measured 235 words because the contents duplicate the headings; two headings were tightened — *Start with when it happens* to *Start with when*, *Say what you have already done* to *Say what you have done* — bringing every study into band.
