# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S20` — Consultation & Quote CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — eyebrow, headline, introduction, action label and preparation title kept as written, the consultation terms and preparation outline bracketed placeholders, no availability, initial fee, quote process, eligibility condition or follow-up arrangement named, one link to the same-variant S19; no media in any study — are kept exactly. V1's `<details>` disclosure opens as a row.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S20-001` | Universal / Safe | 001 Ivory & Olive | 1 — the closing invitation beside the next-step panel | column rules behind the head | Head and lead in a left column; the next step as a panel on the band tone beside, its preparation row on the lead rule | none · 2 | 114 |
| `FIN-S20-002` | Premium / Editorial | 002 Rosewood | 2 — the editorial invitation with a wide action row | bracket above the headline | The next step as a wide row on the lead rule — the action left, the terms and opened preparation row right | none · 2 | 114 |
| `FIN-S20-003` | Structured / Visual Modular | 003 Lagoon | 3 — the centred invitation in a generous field | registration grid behind | A bordered plate with the centred head above the next step on the band tone | none · 2 | 114 |
| `FIN-S20-004` | Conversion-led | 004 Iris | 4 — the split invitation with an oversized heading panel | span mark beneath *what matters to you.* | The head in a band on the band tone with the lead beside; the next step beneath, its preparation row on the lead rule | none · 2 | 114 |
| `FIN-S20-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the closing invitation on the dark ground | corner frame along the display column | The next step as an offset band on the band tone, its preparation row on the lead rule | none · 2 | 114 |

## What changed from V1

V1's rounded next-step panel, wide action row, teal field, violet heading panel and apricot invitation and the plus-marked disclosure go; the action is the register's bordered button with the arrow mark, V1's terms sit beneath in muted ink and the quote-preparation disclosure opens as a row with the document mark on the lead rule. The darkened surfaces are the 001, 003, 004 and 005 next-step panels. Copy is V1's throughout; no availability, fee or condition appears anywhere.

## Verification

- `fincheck.ps1 -Sec S20 -Fields 'Your next step|A conversation with purpose|Let us start with|what matters to you|Bring your questions, priorities|Explore contact options|Confirmed consultation availability|Preparing for a quote|Approved outline of the needs'` — ALL CHECKS PASS; parity 45/45. No `<h1>`; no header/nav/footer; no form; one link (same-variant S19, as V1 routed it); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; two placeholders per study.
- Rendered and read at 1440. No correction needed.
