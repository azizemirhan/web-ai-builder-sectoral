# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S18` — Emergency / Quick Contact · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

This is the most dangerous role in the sector to get wrong. The sector default is a red banner with a number in it. The contract **bans alarm red** and **bans invented numbers**, so neither is available — and neither should be, because a page cannot know which of three situations a reader is in.

The honest version sorts the reader into three routes, in the order to try them, and says plainly that it is not doing the sorting:

| | The route | Where to go |
| --- | --- | --- |
| One | Now — chest pain, severe bleeding, difficulty breathing, someone who will not wake | The emergency service. Do not ring us first: ringing us costs you minutes |
| Two | Today, but not the emergency service | The out-of-hours or urgent-care service for where you are *(reserved)* |
| Three | It can wait until we are open | Ring the desk |

Then: **Have this ready** — where you are, what happened and when it started, and anything already taken, in that order. And: **We do not triage on this page.**

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S18-001` | Universal / Safe | 001 Linen & Sage | B | 1 — three routes in order, the first weighted | column rules behind the head | 1 reserved · 1 | 212 |
| `HC-S18-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the first route given the page | open bracket at the head | none · 1 | 209 |
| `HC-S18-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the three routes sorted in a ledger | bordered cell grid, 1px lines shared | 1 reserved · 1 | 223 |
| `HC-S18-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — have this ready, raised | measure rule under the key phrase | 1 reserved · 1 | 213 |
| `HC-S18-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — three routes as one descending scale | corner frame at the head | none · 1 | 209 |

## What was designed

**Urgency is carried by surface, scale and rule — never by colour.** The first route sits on the band tone with a 3px accent edge in every study; in 002 it is given the page at statement size; in 005 the three routes descend in scale so the eye reaches the first one before it reads anything. No alarm red appears anywhere, and the checker enforces that.

**Nothing on the page dials, submits or triages.** No telephone link, no form, no checker, no script. The emergency service is named only as *the emergency service*; the out-of-hours service is a bordered edge in the graphite refusal token reading `RESERVED — THE OUT-OF-HOURS SERVICE FOR THIS AREA`. The no-triage refusal is set in the refusal tone and closes every study.

**The conversion-led variant carries no booking action.** For the first route the only right action is to leave the page, and a Book-a-first-appointment control beside *chest pain* would be the worst thing this batch could contain. 004 raises the have-this-ready line instead.

## Verification

- `hccheck.ps1 -Sec S18 -Fields 'If it cannot wait|this is not the page|…|Contact and directions'` — ALL CHECKS PASS; parity 75/75. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no `tel:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; **no cyan, aqua or alarm red**; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; one placeholder per study, declared in the `placeholder-data` meta. The one link is held at `#` for S19.
- Rendered and read at 1440.
