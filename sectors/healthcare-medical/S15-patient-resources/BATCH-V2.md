# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S15` — Patient Resources · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** It is authored directly in the V2 register, so this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`. The five things, their purposes, who writes each one and the refusal are shared across all five studies, so the batch reads as one section.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The sector's resources role is a downloads wall: leaflets, PDFs, a blog index, a symptom checker. None of that answers the three questions the contract says a visitor arrives with, and a symptom checker is medical advice by another name. The honest version is the small set of things a visitor **actually carries out of the building**, with what each is for and who writes it:

| | The thing | What it is for | Who writes it |
| --- | --- | --- | --- |
| One | The letter | What was found and what happens next, in plain words | The person who saw you, before you leave |
| Two | The plan | What to do at home, and for how long | Written with you in the room |
| Three | A note for someone else | A short version you can show whoever you will have to explain this to | Written only if you ask |
| Four | Where to read about the area | What is usual for skin, joints or the heart. Not about you | Chosen by the clinic and listed by name |
| Five | Who to ring, and when | One line, so it is never a search | On every letter, with its hours |

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S15-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the five things read down one measure | column rules behind the head | 1 reserved · 2 | 212 |
| `HC-S15-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the handover beside the list | open bracket at the head | 1 reserved · 2 | 214 |
| `HC-S15-003` | Structured / Visual Modular | 003 Sky & Slate | C | 3 — the five things as a shared-line ledger | bordered cell grid, 1px lines shared | none · 2 | 223 |
| `HC-S15-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the reason to come, beside what you take home | measure rule under the key phrase | 1 reserved · 2 | 244 |
| `HC-S15-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the five things read as an index | corner frame at the head | none · 2 | 214 |

Shapes read B · B · C · B · C: no `A` in this batch, and two `C`s, which the contract's page rhythm allows and which suits a section whose subject is documents rather than rooms.

## What was designed

Each thing is a ruled row: the name in ink, what it is for in ink beneath, and **who writes it in the muted tone**, so the authority behind each document is visibly a separate kind of statement from the document's purpose. In 003 that becomes the third column of a shared-line ledger on the band tone; in 005 the five names are set at statement size behind word-numeral chips, ONE to FIVE, never digits.

**Nothing here is advice and nothing is a download.** No diagnosis, dose, symptom checker, leaflet title, author or external source is named — the reading the clinic points to is a bordered edge in the graphite refusal token reading `RESERVED — THE READING THE CLINIC POINTS TO`. The refusal that says so is set in the refusal tone in all five. The 004 panel adds the one thing the list implies: none of these documents exists until somebody has seen you.

**No SVG, no icon, no badge, no file-type mark, no download control.**

## Verification

- `hccheck.ps1 -Sec S15 -Fields 'To take away|Nothing here replaces being seen|…|Ask at the desk'` — ALL CHECKS PASS; parity 80/80. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; two placeholders per study, declared in the `placeholder-data` meta. The ask is held at `#` for S19; the 004 booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440. Corrections: the 004 foot was given the same two-part shape as the other four, so the ask appears in all five rather than being dropped where the booking action sits; the letter's demo value was capitalised, having read as a lower-case fragment after a full stop.
