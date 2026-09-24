# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S06` — Why Choose This Clinic · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the leads, the five checkable reasons with their check lines, the come-and-check panel in 004 and the what-is-not-on-this-page refusal kept word for word; every reason something a visitor can test on the day — are kept exactly. V1's own reserved-area count per study is kept: five in 001, one in 002, 003 and 005, none in 004.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S06-001` | Universal / Safe | 001 Linen & Sage | A | 1 — each reason with the place you can check it | column rules behind the head | Head split; five reason cells at 4:3 on the lead rule; the refusal and the link as the foot | 5 reserved · 0 | 219 |
| `HC-S06-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the five reasons numbered down one measure | open bracket at the head | The 3:4 field of the doctor writing beside five word-numeralled reasons on the lead rule | 1 reserved · 0 | 207 |
| `HC-S06-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — what we do set against what you check | bordered cell grid, 1px lines shared | Head with a 4:3 examination room; five WE DO / YOU CHECK rows, the check column on the band tone | 1 reserved · 0 | 217 |
| `HC-S06-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the list you take with you | measure rule under the key phrase | Five ruled reason rows beside the come-and-check panel on the band tone and the refusal | none · 0 | 230 |
| `HC-S06-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the reasons read under one wide strip | corner frame at the head | Framed head; a 21:9 strip of the nurse taking a reading; five ruled rows on the lead rule, offset inward | 1 reserved · 0 | 204 |

## What changed from V1

V1's rounded reason cards go. The headline is the display `<h2>` with `you can check` — the whole argument of the section — in the accent, and in 004 under the measure rule. Each reason is a claim in ink with its detail in the muted tone and V1's `Check:` clause marked by the accent, so the testable half is visibly separate from the assertion. In 003 that separation becomes the layout: WE DO against YOU CHECK as two columns of a shared-line grid with the check column on the band tone. In 002 the ordered list is opened by word-numeral chips, never digits. **V1's `tag` chip in 004 is dropped** for the register's tracked uppercase label, and **the what-is-not-on-this-page refusal is set in the graphite refusal tone** throughout.

**No SVG, no icon, no badge** — which is the section's own argument: a clinic that refuses to publish a rating does not get a badge row either.

## Verification

- `hccheck.ps1 -Sec S06 -AllowClaims ' best |award' -Fields 'Why here|Reasons you can check on the first visit|…|Registrations and accreditations'` — ALL CHECKS PASS; parity 55/55. **The allowance is V1's own refusal**: the foot names the words it will not use — *a figure, a rating, an award, or the word best* — so *best* and *award* appear on the page only as things being declined. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no placeholder in this section. The 004 action points at the same-variant S05, which is authored, and resolves on disk; the accreditation link is held at `#` for S11, as V1 left it.
- Rendered and read at 1440.
