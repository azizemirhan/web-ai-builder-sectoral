# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S11` — Team · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids invented names, qualifications, certifications and trade bodies. On a team page that is not only a compliance rule — it is the right rule, because the material belongs to somebody else:

> **Names go up when the *person* says yes.** Six people keep this place running. Their names are theirs to give, so the page holds the space.

**The roles are real and generic; the names are reserved.** Each row is a tracked role, a bracketed name, and one line that describes the *post* rather than the holder:

- **The technician** — does the work, and writes down what was found.
- **The service adviser** — takes the call, and *says no when the answer is no*.
- **The parts keeper** — knows what is on the shelf without looking.
- **The tester** — signs the sheet. **Cannot be leaned on.**
- **The valeter** — last person to touch it before you do.
- **The sales adviser** — *shows you the car, not the finance.*

Then the limit, which is the only one in this sector that protects somebody other than the reader:

> **No name, qualification, ticket or photograph goes up without the person agreeing to it.** A team page is the one page where the business is not the only one with something to lose.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S11-001` | Universal / Safe | 001 Chalk & Racing Green | A | 1 — a three-up portrait grid at 4:5 | the bay lines behind the head | 6 reserved · 6 | 170 |
| `AUTO-S11-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the six together, then a ruled roster | the plate edge at the head | 1 reserved · 6 | 152 |
| `AUTO-S11-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the roster as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 6 | 156 |
| `AUTO-S11-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *person*, measured | the torque mark under *person* | none · 6 | 149 |
| `AUTO-S11-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | A | 5 — a square grid at 1:1, offset | the ramp frame | 6 reserved · 6 | 170 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**, and the reason matters: six reserved names beside six portraits would put a face where a name is being withheld, which is the opposite of what the page says.

## What was designed

Every portrait field is **named by role only** in its own slate label — `THE TECHNICIAN · 4:5` — so the reservation is legible in the media as well as in the copy. 002 replaces six portraits with **one photograph of the six together**, which is the editorial answer to the same problem; 003 pairs the group shot with the **job board on the workshop wall**, because the board is how the work is actually shared out.

The row is three-part and always in the same order: the role tracked in the accent, the reserved name in ink at 1.1rem, the line in the muted tone. The reserved names therefore sit where a name would sit, at the size a name would be.

## Verification

- `autocheck.ps1 -Sec S11 -Fields 'Who does the work|Names go up when the|The technician|The service adviser|The parts keeper|The tester|The valeter|The sales adviser|Ask for somebody by role'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no name, qualification, ticket, certificate, trade body, years of service, award or rating**; no manufacturer, model, badge or plate; no digit in visible copy outside the field ratio labels; six placeholders per study. Both links point at same-variant S04 and S19 studies.
- Rendered and read at 1440. Corrections: the five first measured up to 173 words, over the standard band, and the lead was shortened; the portraits were rendering 507 pixels tall at 3:4 in a three-up grid and were retuned to 4:5 in 001 and 1:1 in 005, which also separates the two `A` variants.
