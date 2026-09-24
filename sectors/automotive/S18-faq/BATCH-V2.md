# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S18` — FAQ · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

> **Six questions, answered *before* you ask them.** The six that come up most, written out rather than folded away behind a plus sign.

- **Can you look at it today?** — Sometimes. Ring and ask; the answer is a yes or a no, not a maybe.
- **Will you tell me before you do the work?** — Always. Nothing is ordered or fitted until you have said yes to it in writing.
- **Can I keep the old parts?** — Yes. Say so when you book and they go in the boot.
- **Do you work on my make?** — That is the one list we keep current. Ask before you set off rather than after.
- **What if it turns out to be something else?** — You get rung, and the job stops until you have decided what happens next.
- **Can I wait while it is done?** — For some jobs. The waiting room has a kettle and a view of the bay, and nobody moves you out of it.

Then the one refusal that is about the component rather than the trade:

> **Nothing here is folded away.** A question worth answering is worth reading without opening it first, and an answer hidden behind a plus sign is usually an answer somebody hoped you would not find.

**Every answer is open on the page.** There is no disclosure element and no accordion in any of the five studies.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S18-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — six ruled questions on the lead rule | the bay lines behind the head | 1 reserved · 0 | 206 |
| `AUTO-S18-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the six set in two columns | the plate edge at the head | none · 0 | 202 |
| `AUTO-S18-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — question left, answer right, on a sheet | bordered plate, 1px lines shared | 2 reserved · 0 | 210 |
| `AUTO-S18-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *before*, measured | the torque mark under *before* | none · 0 | 202 |
| `AUTO-S18-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the six offset on the band tone | the ramp frame | 1 reserved · 0 | 206 |

All five sit inside the contract's structured band of 170–230.

**Two studies are `C`, and each records why.** 002: six questions and six answers are the page, and the editorial reading gives them two columns and no picture. 004: a photograph between question three and question four helps nobody.

## What was designed

The questions are a `<dl>`, which is what they are, and the five variants set the same list four ways — ruled full-width, two typographic columns, question-left-answer-right split, and offset on the band tone. None of them is a card and none of them opens.

The media answers the questions rather than illustrating them: **the service reception**, where these six are actually asked, and **the waiting room**, which is the sixth answer photographed.

## Verification

- `autocheck.ps1 -Sec S18 -Fields 'Asked at the desk|Six questions, answered|Can you look at it today|Will you tell me before|Can I keep the old parts|Do you work on my make|What if it turns out|Can I wait while it is done|Nothing here is folded away'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<details>`, `<summary>`, `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; nothing expands; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no price, rate, time, figure, rating, award or urgency device; no manufacturer, model, badge or plate; no digit in visible copy outside the field ratio labels; no placeholder in this section. Both links point at same-variant S08 and S19 studies.
- Rendered and read at 1440. Correction: the sixth answer read *nobody will hurry you out of it*, and `hurry` is on the automotive claims list as an urgency device; rather than take an allowance for a word used in the opposite sense, the line was reworded to *nobody moves you out of it* and the checker left clean.
