# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S24` — Case / Care-Pathway Context Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The section README carries a **Sector Semantic Limitation**: clinical case material is regulated and often patient-identifiable, so this role is scoped to *anonymised care-pathway context, never a named patient case*.

The page is written **to** that limitation rather than around it. The subject is the route a skin referral takes, and the first thing the page says is why there is no case on it:

> **Why this page has no case** — Clinical case material identifies people. A date, a town, an age and a photograph are enough between them. So this page documents the route and leaves the person out.

Then **the route** in four stages, indexed in words: the first appointment (what changed, and when, written down as you said it) · the look (in daylight, with a second opinion in the room if you want one) · the decision (what it looks like, **what it is not**, and what is still being ruled out) · the letter (all of the above, in writing, to you and to whoever asked).

Then the two halves of the record: **what is recorded** — the stage, the day it happened, the decision, and who made it, by role — against **what is not**: no name, no photograph, no age, no town, nothing that would let this page be read backwards to a person. And last, the sentence that a case-study role in this sector has to carry: **what this cannot show you** — an outcome, a figure, a before and after, or a quote from somebody who went through it.

The title is the argument: *The skin pathway, followed through, with **nobody in it**.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S24-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the refusal first, the route after it | column rules behind the head | 1 reserved · 1 | 220 |
| `HC-S24-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the refusal set as the page | open bracket at the head | none · 0 | 212 |
| `HC-S24-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the pathway as one plate, with the metadata | bordered plate, 1px lines shared | 1 reserved · 2 | 228 |
| `HC-S24-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — *nobody in it*, measured | measure rule under the title's last clause | 1 reserved · 1 | 219 |
| `HC-S24-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the page framed and emptied | corner frame at the head | none · 0 | 212 |

All five sit inside the contract's detail band of 170–230.

**Two studies are `C`, and each records why.** 002: a page whose whole argument is that it will not show the person cannot open with a photograph of the room they were in. 005: the distinctive reading takes the page at its word — if the person is not on the page, nothing stands in for them.

**003 is the only variant carrying the metadata** the brief allows — *Area: Skin* and a reserved *Department* — as bare labelled fields in the record row. It is also the only one with two placeholders, the second being that reserved department.

## What was designed

Every reserved area on this page is a **document, not a person**: the plan being written in the consulting room (001), the letter being handed over at the desk (003), the doctor writing at the desk after a visit (004). The one figure that appears is at work and named by role; nobody stands in for a patient.

The refusal is the page's strongest horizontal. *Why this page has no case* gets the one 3px accent lead rule each composition is allowed — across the width in 001, at full measure in 002, offset inside the frame in 005 — and is set in the graphite `--no` tone throughout. In 003 the lead rule goes under the plate, where the ask sits; in 004 it opens the band-tone block.

The four stages are a **three-part row**: the word-numeral in its bordered chip, the stage name in ink, the line beneath it in the muted tone — with the numeral column fixed at `4.6rem` so the stage names and their descriptions share one left edge rather than stepping with the chip widths. 002 pulls the description out into a third column, which is the editorial reading of the same row.

No SVG, no icon, no badge; no global header or footer; nothing opens, expands or submits.

## Verification

- `hccheck.ps1 -Sec S24 -Fields 'Why this page has no case|The route|What is recorded|What is not|What this cannot show you|Read next'` — ALL CHECKS PASS; parity 30/30. `<h1>` present and single (detail page); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no claim term; no digit in visible copy outside the field ratio labels. All links point at same-variant S23, S03 and S05 studies and resolve on disk.
- Rendered and read at 1440. Corrections: 003 first ran to 240 words, outside the detail band, because the metadata and a second field label pushed it — the second reserved area was dropped and the metadata trimmed to two rows, bringing it to 228; the stage rows were stepping their left edge with each chip's width and were given a fixed numeral column; 004's 16:9 field was rendering 1140 by 640 and dominating the page, and was capped at 62% of the measure; the record block in 004's band was missing the label spacing rule and its two labels were colliding.
