# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S12` — Insurance & Payment · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the three ways to pay with what you need and what happens, the never-charged list, the before-booking panel in 004 and the if-you-cannot-pay line kept word for word — are kept exactly. **No price, fee, currency, insurer, plan or coverage is named**: the first-visit fee, the insurers worked with and the referral arrangements are reserved values marked `data-placeholder="true"`. V1's own reserved-area count per study is kept: one in 001, 004 and 005, none in 002 and 003.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S12-001` | Universal / Safe | 001 Linen & Sage | B | 1 — three ways, each fully answered | column rules behind the head | Three way-columns on the lead rule; a closing band with the 4:3 fee-being-written field, the never-charged list and the action | 1 reserved · 3 | 215 |
| `HC-S12-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the three routes as an editorial set | open bracket at the head | Three way-columns on the lead rule; the never-charged list as ruled lines keeping V1's emphasis | none · 3 | 211 |
| `HC-S12-003` | Structured / Visual Modular | 003 Sky & Slate | C | 3 — the three ways as a four-column ledger | bordered cell grid, 1px lines shared | Three rows of route, You need, What happens on the band tone and the reserved value; two closing modules | none · 3 | 211 |
| `HC-S12-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — ask the fee, said first | measure rule under the key phrase | The before-booking panel on the band tone with the never-charged list and the action, and a 4:3 desk field, beside three ruled way-rows | 1 reserved · 3 | 221 |
| `HC-S12-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the promise given the whole top of the page | none (the display line is the device) | The promise at display size in mint; a band with the 21:9 letter, fee line blank, beside the never-charged list; three way-columns on the lead rule | 1 reserved · 3 | 217 |

## What changed from V1

V1's rounded price cards and its pill-shaped reserved tags go. The headline is the display `<h2>` with `in writing` in the accent, and in 004 under the measure rule; in 005 the whole promise is the composition, set at display size on the dark ground as V1 intended. **Each reserved value is a bordered edge in the graphite refusal token** — a 1px rule and 2px corners, never a filled pill — reading `RESERVED — FIRST-VISIT FEE`. V1's *You need* and *What happens* become bare labelled fields; in 003 they become the columns of a shared-line ledger with What happens on the band tone. **The never-charged list is set in the refusal tone throughout**, because it is the part of the page a visitor most needs to be able to trust.

**No SVG, no icon, no badge, no insurer logo and no currency symbol.** There is no form anywhere: V1's own line says the way to raise not being able to pay is a conversation, not a form.

## Verification

- `hccheck.ps1 -Sec S12 -Fields 'Paying for it|The price of the first visit is told to you|…|Book a first appointment'` — ALL CHECKS PASS; parity 105/105. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; three placeholders per study, declared in the `placeholder-data` meta. Every booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440.
