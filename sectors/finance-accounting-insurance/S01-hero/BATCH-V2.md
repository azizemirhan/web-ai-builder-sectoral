# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass* (the quiet ledger). Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — eyebrow, headline, introduction and preparation line kept as written, the firm name and the contact/scope/eligibility information bracketed placeholders, no firm, service, fee, eligibility or contact route named; one consented conversation photograph (none in 004, as V1 set it) — are kept exactly. V1's `<h2>` is promoted to the page's `<h1>` because this is the hero; V1's `<details>` disclosure opens as a row because the register runs no script.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S01-001` | Universal / Safe | 001 Ivory & Olive | 1 — the split introduction beside a generous field | column rules behind the head | Brand, eyebrow and h1; the introduction and the opened preparation row on the lead rule; a 4:5 conversation field beside | 1 · 2 | 71 |
| `FIN-S01-002` | Premium / Editorial | 002 Rosewood | 2 — the editorial opening with the field set first | bracket above the headline | A 3:4 conversation field left, as V1 placed it; brand, eyebrow, h1, introduction and the opened preparation row on the lead rule right | 1 · 2 | 71 |
| `FIN-S01-003` | Structured / Visual Modular | 003 Lagoon | 3 — the wide title above a panoramic field | registration grid behind | The h1 at width with the introduction and the opened preparation row beside on the lead rule; a 3:1 conversation field beneath | 1 · 2 | 71 |
| `FIN-S01-004` | Conversion-led | 004 Iris | 4 — the typographic composition with a prominent preparation | span mark beneath *clearer next step.* | Type-only composition; the h1 at the large size with the introduction beside; the preparation row as a band on the band tone on the lead rule | none · 2 | 63 |
| `FIN-S01-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the oversized introduction with a tall field | corner frame along the display column | The h1 at the large size, the introduction and the opened preparation row; a tall 4:5 conversation field beside, set right | 1 · 2 | 71 |

## What changed from V1

V1's rounded cards, pill caption floating on the image, accent-filled hero panel and plus-marked disclosure go; the headline is the h1 with one accent phrase, the preparation line opens as a row with the speech mark, and the photograph is a labelled empty field (THE MEETING) with its caption beneath. Edges are 2px, surfaces are separated by hairlines and one 3px accent lead rule anchors each composition. The darkened surface is the 004 preparation band. Copy is V1's throughout; the firm name and contact information stay bracketed.

## Verification

- `fincheck.ps1 -Sec S01 -Fields 'Approved firm name|Finance|Accounting|Insurance|Make room for a|clearer next step|Bring your questions into focus|Plan your first conversation|Note your priorities and questions|Confirmed contact route'` — ALL CHECKS PASS; parity 50/50. One `<h1>` per study, as the hero set requires; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio label; no claim term; two placeholders per study.
- Rendered and read at 1440. No correction needed.
