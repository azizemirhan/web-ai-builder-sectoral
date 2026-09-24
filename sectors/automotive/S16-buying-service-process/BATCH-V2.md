# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S16` — Buying & Service Process · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A process section usually promises speed. The contract forbids a turnaround time, so the page promises the opposite thing — the exit:

> **Five steps, and the one where you can *stop*.** What happens from the first call to the keys, and where you can walk away owing nothing.

- **One · The first call** — you say what you want, or what is wrong.
- **Two · The look** — somebody looks. A car, or your car.
- **Three · In writing** — what it is, what it needs, and what it will cost.
- **Four · You decide** — **nothing has been ordered and nothing has been done. Stopping here costs you nothing.**
- **Five · The work** — it happens, or the car changes hands, and you get the sheet.

> **No step here has a time on it.** A promise of a day is a promise about a part somebody else has to send, and we do not make it.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S16-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the five on the lead rule, the fourth lifted | the bay lines behind the head | 1 reserved · 0 | 145 |
| `AUTO-S16-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the handover desk after the five | the plate edge at the head | 1 reserved · 0 | 143 |
| `AUTO-S16-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the five as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 0 | 148 |
| `AUTO-S16-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *stop*, measured | the torque mark under *stop* | none · 0 | 139 |
| `AUTO-S16-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the five offset, the key at the end | the ramp frame | 1 reserved · 0 | 144 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: the conversion-led reading is the five steps and the promise inside the fourth, and a photograph between the reader and that promise earns nothing.

## What was designed

**Step four is lifted onto the band tone** in every variant — a 6px band behind one row of an otherwise hairline list, with its description in ink rather than the muted tone. It is the only place in the sector where a single list row gets its own surface, and it is spent on the sentence that says stopping is free. In 005, where the whole list already sits on the band tone, the fourth row is lifted the other way, onto the paper.

The media follows the steps rather than decorating them: **the job sheet being written** is step three, **the handover desk** and **the key on the counter** are step five, and **the key being handed across the counter** closes 005.

## Verification

- `autocheck.ps1 -Sec S16 -Fields 'How it goes|Five steps, and the one|The five steps|The first call|The look|In writing|You decide|The work|No step here has a time'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no turnaround time, deadline, same-day promise, price or figure**; no manufacturer, model, badge or plate; no rating, award or urgency device; no digit in visible copy outside the field ratio labels; no placeholder in this section. Both links point at same-variant S04 and S08 studies.
- Rendered and read at 1440.
