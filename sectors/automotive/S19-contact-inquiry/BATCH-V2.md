# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S19` — Contact & Inquiry · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

No form is allowed, and no number, address, email or opening hour may be invented. What a contact section can honestly say is **who is at the other end**:

> **Four ways in, and who *answers* each one.** Where a message lands, who picks it up, and how long it sits before somebody does.

- **One · At the desk** — somebody is on it whenever the door is open.
- **Two · By telephone** — reserved: the number, and the hours it is answered.
- **Three · In writing** — reserved: the route, and how long a reply takes.
- **Four · Not by message** — **if the car is not safe to drive, ring.** A message sits until somebody opens it.

**What to put in it** — what the car is doing; whether it is drivable; a way to reach you that you will actually answer.

> **There is no form here, no chat window and no automatic reply pretending to be a person.** Every route ends at somebody who can say no.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S19-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the four on the lead rule, brief opposed | the bay lines behind the head | 1 reserved · 2 | 148 |
| `AUTO-S19-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the diary as the lead image | the plate edge at the head | 1 reserved · 2 | 148 |
| `AUTO-S19-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the routes as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 2 | 152 |
| `AUTO-S19-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *answers*, measured | the torque mark under *answers* | none · 2 | 144 |
| `AUTO-S19-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the routes framed against the key cabinet | the ramp frame | 1 reserved · 2 | 148 |

All five sit inside the contract's standard band of 90–170.

**004 is the `C`**: two of the four routes are reserved values, the page's promise is that a person is at the end of each, and a photograph adds nothing to that promise.

## What was designed

This section and S08 share the four-route shape deliberately — a visitor who has read one recognises the other — but the content is the opposite way round: S08 is about booking, this is about **who answers**, and the fourth route here is a refusal of the channel rather than of the emergency.

The media is the place a message lands: the service reception, the **booking diary open on the desk**, and the key cabinet behind it. No `tel:` link, no chat widget, no auto-reply.

## Verification

- `autocheck.ps1 -Sec S19 -Fields 'Getting hold of us|Four ways in, and who|The four routes|At the desk|By telephone|In writing|Not by message|What to put in it|There is no form here'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<form>`, `<input>`, `<button>`, `<svg>`, `<script>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no `tel:` or `mailto:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no invented number, address, email or opening hour; no price, rate, response-time promise, figure, rating, award or urgency device; no digit in visible copy outside the field ratio labels; two placeholders per study. Both links point at same-variant S08 and S10 studies.
- Rendered and read at 1440.
