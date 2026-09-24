# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S20` — Final Consultation CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A closing CTA is where the sector puts its urgency devices: a countdown, limited availability, a waiting-time promise, a rating. The contract forbids every one of them. What is left is the honest version: **one step, what follows from it, and the line that sends an emergency somewhere else.**

*One step: tell us what is wrong. Everything else follows from that.* → Four questions, then a time, a person by role, and what the first visit involves, in writing, before you come. → **Book a first appointment.** → *Not sure this is the place?* → **If it cannot wait, this is not the step.**

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S20-001` | Universal / Safe | 001 Linen & Sage | B | 1 — one step, stated and then shown | column rules behind the head | 1 reserved · 0 | 66 |
| `HC-S20-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the step set as the whole page | open bracket at the head | none · 0 | 62 |
| `HC-S20-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the step in a bordered cell beside what it books | bordered two-cell plate, 1px line shared | 1 reserved · 0 | 66 |
| `HC-S20-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the count set as the word it is | measure rule under the key phrase | none · 0 | 63 |
| `HC-S20-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the step framed and alone | corner frame at the head | none · 0 | 62 |

All five sit inside the contract's CTA band of 40–90 words.

## What was designed

**No urgency device of any kind.** No countdown, no scarcity, no availability claim, no figure, no rating, no alarm red — and the section that would normally carry them, the conversion-led 004, carries the least: the word **ONE** at display size in the accent as this register's index numeral, spelled out because no digit belongs in visible copy, with the measure rule under the key phrase and one bordered action.

Every study ends on the same two things: the cannot-wait line in the graphite refusal token, linking to the same-variant S18, and the way out for a visitor who is not sure this is the right place, linking to the same-variant S02. A closing step that cannot admit either of those is not honest in this sector.

**No SVG, no icon, no badge; nothing here takes a booking**, and the page says what happens when the action is used rather than implying it happens on the page.

## Verification

- `hccheck.ps1 -Sec S20 -Fields 'The next thing|One step|…|Use the emergency service'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no placeholder in this section. All three links point at the same-variant S05, S02 and S18 and resolve on disk.
- Rendered and read at 1440.
