# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S08` — Patient Journey · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the six steps with what happens, what is asked and what you can do at each, the nothing-to-prepare panel in 004 and the at-any-point line kept word for word; the length of the conversation and the wait for results left as demo values spelled as words — are kept exactly. V1's own reserved-area count per study is kept: one in 001, 004 and 005, six in 002, none in 003.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S08-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the six steps read down one measure | column rules behind the head | Six ruled step rows on the lead rule beside a 4:5 corridor field | 1 reserved · 2 | 204 |
| `HC-S08-002` | Premium / Editorial | 002 Porcelain & Plum | A | 2 — the visit told as six places | open bracket at the head | Six step cells at 4:3 on the lead rule, each opened by the step name as a tracked label | 6 reserved · 2 | 223 |
| `HC-S08-003` | Structured / Visual Modular | 003 Sky & Slate | C | 3 — the six steps as shared cells | bordered cell grid, 1px lines shared | Six word-numeralled cells with Happens / Asked / You can as bare labelled fields | none · 2 | 243 |
| `HC-S08-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — nothing to prepare, said first | measure rule under the key phrase | Head with a 4:3 two-seats field; the nothing-to-prepare panel on the band tone beside six ruled step rows | 1 reserved · 2 | 234 |
| `HC-S08-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the visit as a spine that ends at the door | corner frame at the head | Six ruled step rows offset inward; a 21:9 front-door field closing the sequence | 1 reserved · 2 | 205 |

## What changed from V1

V1's rounded step cards and its numbered circles go. The headline is the display `<h2>` with `in order` in the accent, and in 004 under the measure rule. Each step is a ruled row: what happens in ink and the muted tone, and **V1's you-can line set in the accent**, so the thing the visitor is allowed to do at each step is the one coloured element on the page — which is the section's argument. **V1's decorative numeral rail in 003 is dropped** and replaced by word-numeral chips on the cells: the rail rendered digits through `data-n`, and no digit belongs in visible copy here. **V1's `tag` chip in 004** becomes the register's tracked uppercase label. The at-any-point line is set in the graphite refusal tone throughout.

Nothing on the page is drawn as a pathway flowchart, a protocol schedule or a consent form — three things the sector's anti-pattern list names and which a patient-journey section is the obvious place to reach for. The order is written, not diagrammed.

**No SVG, no icon, no badge.**

## Verification

- `hccheck.ps1 -Sec S08 -Fields 'The first visit|What happens, in order|…|Book a first appointment'` — ALL CHECKS PASS; parity 95/95. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; two placeholders per study, declared in the `placeholder-data` meta. Every booking action points at the same-variant S05 and resolves on disk. The 003 study runs to 243 words against the structured band's 230 — V1 set it that way with its extra *Asked* field, and it is inside the contract's absolute ceiling of 250.
- Rendered and read at 1440.
