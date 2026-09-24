# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S14` — Locations & Departments · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section was half-built.** `HC-S14-001` and `HC-S14-002` existed as V1 studies; `003`, `004` and `005` did not exist at all. There is no `BATCH-V1.md`, so this record carries both the authoring and the design decisions. The two V1 studies keep their content spine word for word; the three new studies are authored directly in the register and take their spine from the two that existed, so all five carry the same six places, the same statements and the same practical lines. **No new claim, value or fact is introduced by the three new studies.**
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Origin | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S14-001` | V1 spine kept | Universal / Safe | 001 Linen & Sage | A | 1 — the building walked in six frames | column rules behind the head | 6 reserved · 2 | 278 |
| `HC-S14-002` | V1 spine kept | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the door, then the way in | open bracket at the head | 1 reserved · 2 | 260 |
| `HC-S14-003` | **new** | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the walk as a shared-line ledger | bordered cell grid, 1px lines shared | 1 reserved · 2 | 272 |
| `HC-S14-004` | **new** | Conversion-led | 004 Sand & Terracotta | B | 4 — nothing to find, said first | measure rule under the key phrase | 1 reserved · 2 | 287 |
| `HC-S14-005` | **new** | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the building read as a walk | corner frame at the head | none · 2 | 263 |

Shapes read A · B · B · B · C across the batch: never more than two consecutive `A`, and the batch carries a `C`, as the contract's page rhythm requires. The `C` records why it carries no media: the six names already say what a corridor photograph would.

## What was designed

The section refuses the sector's department directory outright — its headline says so — and the design keeps that refusal structural. There is **no table of departments, no floor plan drawn as a diagram, no map, and no address, street, telephone number or opening hour**; V1's own closing line sends those to the contact page. Every study walks the same six places in the order a visitor meets them.

Each place is a ruled row or a shared-line cell: the name in ink, what happens in the muted tone, and **the one practical thing set in the accent**, because that line is the only part of the section a worried visitor actually needs to carry in. The two demo values — whether the door is step-free, and how many consulting rooms there are — stay marked `data-placeholder="true"` and spelled as words. In 003 and 005 the six places are opened by word-numeral chips, ONE to SIX, never digits.

**No SVG, no icon, no badge, no pin.**

## Verification

- `hccheck.ps1 -Sec S14 -Fields 'The building|One building, described so you can find your way in it|…|Contact and directions'` — ALL CHECKS PASS; parity 90/90. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; two placeholders per study, declared in the `placeholder-data` meta. The contact link is held at `#` for S19; the 004 booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440. Corrections: the 003 ledger repeated its column labels on every row, which pushed the study to 290 words, so the labels were moved to one hidden header row as the sector's other ledgers do; its cells were then set to stretch so the band-tone column fills each row; in 005 the place-name selector was strengthened to `.item p.name`, having been overridden by the row's own paragraph rule and rendering at body size.

## A note on length

**All five studies run over the contract's 250-word ceiling** — 260 to 287. This is inherited, not introduced: V1's own two studies measure 289 and 266 words, and the detailing pass does not cut copy, because cutting copy is a content change and the spine is V1's. The three new studies were held to the leanest form that still carries the same six places with the same statements and practical lines, which is why they land between the two V1 figures rather than below them. If the section is to come inside the band, the six practical lines are the place to shorten, and that is an authoring decision rather than a design one.
