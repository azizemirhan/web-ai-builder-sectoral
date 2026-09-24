# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S07` — Medical Technology · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the leads, the six machines with what each answers and what each cannot do, the rule and the not-held-here line kept word for word; the trace length and the wait for results left as demo values spelled as words; **no accuracy figure, detection rate, diagnosis or outcome claimed for any machine** — are kept exactly. V1's own reserved-area count per study is kept: one in 001, 002 and 004, six in 003, none in 005.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S07-001` | Universal / Safe | 001 Linen & Sage | B | 1 — each machine with its limit under it | column rules behind the head | A 4:5 ultrasound room beside six ruled machine rows on the lead rule; a three-part foot | 1 reserved · 2 | 198 |
| `HC-S07-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the machines as an editorial column | open bracket at the head | Six ruled rows on the lead rule beside the 4:5 field of the trace being taken | 1 reserved · 2 | 199 |
| `HC-S07-003` | Structured / Visual Modular | 003 Sky & Slate | A | 3 — the six machines as shared cells | bordered cell grid, 1px lines shared | Six cells at 4:3 with Answers / Not for as bare labelled fields | 6 reserved · 2 | 223 |
| `HC-S07-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the rule raised to a standing panel | measure rule under the key phrase | The rule panel on the band tone with the booking action beside six ruled rows; a closing band with the 21:9 monitor being fitted | 1 reserved · 2 | 216 |
| `HC-S07-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the limit read before the machine | corner frame at the head | Six entries, limit first in the refusal tone and the machine beside it, on the lead rule and offset inward | none · 2 | 196 |

## What changed from V1

V1's rounded equipment cards go. The headline is the display `<h2>` with `when it is not used` — the sentence the whole section turns on — in the accent, and in 004 under the measure rule. **Every limit is set in the graphite refusal tone**, which is this section's real subject: what each machine cannot answer sits visibly apart from what it can. In 005 that becomes the composition, keeping V1's own device of reading the limit before the name. In 003 the Answers / Not for pair becomes bare labelled fields rather than a table. **V1's `tag` chip in 004 is dropped** for the register's tracked uppercase label.

**No SVG, no icon, no badge** — in particular no heart-trace line, which the sector's anti-pattern list names and which a section about a trace machine would be the obvious place to reach for.

## Verification

- `hccheck.ps1 -Sec S07 -Fields 'What we use|The machine is named|…|Book a first appointment'` — ALL CHECKS PASS; parity 95/95 on the slots common to all five. *The rule* as a heading is variant-specific — V1's 005 carries the rule as a paragraph with no label — and is not a shared slot. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; two placeholders per study, declared in the `placeholder-data` meta. Every booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440.
