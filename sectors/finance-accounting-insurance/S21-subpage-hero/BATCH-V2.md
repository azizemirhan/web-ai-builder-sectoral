# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the category prefix kept as written, the service title, category, introduction, audience and jurisdiction line and image caption bracketed placeholders, no service, category, audience, jurisdiction or caption named; one reserved service-context photograph (none in 004, as V1 set it) — are kept exactly. V1's `<h2>` is promoted to the page's `<h1>` because this is the subpage hero.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S21-001` | Universal / Safe | 001 Ivory & Olive | 1 — the page title beside a contained landscape field | column rules behind the head | The bracketed title as h1, the category, the introduction and the audience line on a hairline; a 4:5 service field beside with its bracketed caption | 1 · 4 | 52 |
| `FIN-S21-002` | Premium / Editorial | 002 Rosewood | 2 — the typographic page title above a split context row | bracket above the headline | A 3:4 service field left; the title, category, introduction and audience line right | 1 · 4 | 52 |
| `FIN-S21-003` | Structured / Visual Modular | 003 Lagoon | 3 — the page introduction and context beside a compact field | registration grid behind | The title and category at width with the introduction and audience line beside on the lead rule; a 3:1 service panorama beneath | 1 · 4 | 52 |
| `FIN-S21-004` | Conversion-led | 004 Iris | 4 — the text-only contextual page banner | span mark beneath *service title]* | Type-only composition, as V1 set it; the title at the large size with the category, introduction and audience line | none · 3 | 41 |
| `FIN-S21-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the internal title above a context field | corner frame along the display column | The title at the large size with category, introduction and audience line; a tall 4:5 service field beside, set right | 1 · 4 | 52 |

## What changed from V1

V1's rounded photograph, split context row, compact square, violet banner and dark panorama go; the page title is the h1 in muted ink with its second half in the accent, V1's category is a tracked accent line, the audience and jurisdiction line sits on a hairline and the photograph is a labelled empty field (THE WORKSPACE) with V1's bracketed caption beneath. Copy is V1's throughout; every page-specific value stays bracketed.

## Verification

- `fincheck.ps1 -Sec S21 -Fields 'Approved service title|Service category|Approved introduction to this specific service|Applicable audience and jurisdiction'` — ALL CHECKS PASS; parity 20/20. One `<h1>` per study, as the hero set requires; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio label; no claim term; four placeholders per study (three in 004, which carries no field).
- Rendered and read at 1440. Correction: the field and its caption wrapped together so the caption stays with the image area.
