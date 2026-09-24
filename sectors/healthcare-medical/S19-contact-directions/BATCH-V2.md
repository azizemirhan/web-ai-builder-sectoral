# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S19` — Contact & Directions · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids an invented address, telephone number or opening hour, and forbids an embedded map. A contact role under those rules is **a page of reserved fields**, so the design makes the reservation deliberate rather than apologetic and says what each blank will hold.

Four routes, each with what it is for and what comes back: *the desk in person · the telephone (reserved) · in writing (reserved) · none of these — the emergency service.* Then **Getting here** as four bare labelled fields, every value reserved: the street, step-free access, parking, public transport. Then the refusal: *a map, a floor plan, or an address we have not checked this month. A wrong address costs somebody a journey they were already dreading.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S19-001` | Universal / Safe | 001 Linen & Sage | B | 1 — four routes, then the way in | column rules behind the head | 1 reserved · 6 | 229 |
| `HC-S19-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the four routes as an editorial index | open bracket at the head | none · 6 | 230 |
| `HC-S19-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the routes sorted in a ledger | bordered cell grid, 1px lines shared | 1 reserved · 6 | 242 |
| `HC-S19-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the desk raised above the rest | measure rule under the key phrase | 1 reserved · 6 | 229 |
| `HC-S19-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the reserved page, admitted | corner frame at the head | none · 6 | 226 |

## What was designed

Six reserved values per study, each a **bordered edge in the graphite refusal token** — `RESERVED — THE NUMBER, AND THE HOURS IT IS ANSWERED`, `RESERVED — THE STREET, THE BUILDING AND WHAT IS EITHER SIDE OF THE DOOR` — so a blank reads as a decision rather than an omission. Each route carries what it is for in ink and what comes back in the muted tone; in 003 what-comes-back becomes the band-tone column of a shared-line ledger.

**Nothing on the page can be submitted or dialled**: no form, no `tel:` link, no embedded map, no pin, no script. The fourth route exists so the page has somewhere to send anything that cannot wait, and links to the same-variant S18.

## Verification

- `hccheck.ps1 -Sec S19 -Fields 'Finding us, reaching us|…|Book a first appointment'` — ALL CHECKS PASS; parity 80/80. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; six placeholders per study, declared in the `placeholder-data` meta. Both links point at the same-variant S18 and S05 and resolve on disk.
- Rendered and read at 1440. Correction: the what-comes-back line was using a `back` class, which the shared module already styles as the return link — it rendered as four underlined links with leading arrows. Renamed to `reply`.
