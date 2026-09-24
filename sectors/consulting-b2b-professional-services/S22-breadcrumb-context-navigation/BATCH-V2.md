# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S22` — Breadcrumb / Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — every level carries the count of what is up there and one legend says so; the current page is `<span aria-current="page">`, never a link; the trail is a `<nav>` with an ordered list, the sibling pages a second `<nav>`; no primary navigation, sitemap, page title or hero; no media; level counts and sibling page names as placeholder demo values; the no-invented-folder commitment closes every study — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S22-001` | Universal / Safe | 001 Paper & Indigo | 1 as a strip | ghost `/` behind the row | The trail as one ruled row of hairline-separated levels, counts as bordered chips inside the links, the current page in the serif with a pin mark; legend; THE OTHER TWO IN OPERATIONS as a second nav on the pencil rule; foot line. No pills | none · 4 | 55 |
| `CONS-S22-002` | Premium / Editorial | 002 Sable & Bronze | 2 as a descending stack | pencil ellipse round the current page | One level per ruled line, each stepping in by an indent with a return-arrow mark so the hierarchy is drawn; counts as tracked lines; the across-nav beside on the pencil rule; legend; foot line | none · 4 | 53 |
| `CONS-S22-003` | Structured / Visual Modular | 003 Field & Emerald | 3 on one seam | ruled margin behind | Four level modules and the across-module joined on one bordered seam; the current module on the band tone with the pencil rule, a pin mark and THIS PAGE as its line; legend and commitment as one foot | none · 4 | 54 |
| `CONS-S22-004` | Conversion-led | 004 White & Signal | 4 — the way up promoted | underline stroke under *Operations* | The full trail small along the top with chips; BACK UP TO OPERATIONS as one bordered link in the serif at the largest size with an up-arrow mark; the placeholder count and the other two pages as inline links beneath; foot line on the pencil rule | none · 5 | 48 |
| `CONS-S22-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — display numerals | bracket grouping the row | How many pages are inside each level as serif italic numerals at display size, ALL for Home, the current page's *1* in the ink with its name never a link; legend; across-nav on the pencil rule; foot line | none · 5 | 53 |

## What changed from V1

The count per level is one device — a bordered chip inside the link, a tracked line, or the display numeral — and the current page carries the pin mark in every study and is never a link. Pills, joined-pill rows and filled panels go; the one darkened surface is 003's current module. Copy is V1's throughout; counts and sibling names keep their placeholder marking, and the digits sit only inside placeholder elements.

## Verification

- `cslcheck.ps1 -Sec S22 -AllowNav -Fields 'You are here|Home|Services|Operations|Operating model redesign|Cost structure|Post-merger integration|somebody maintains'` — ALL CHECKS PASS; parity 40/40 on copy fields (an attribute-level field was excluded from the text check and confirmed by grep: one `aria-current="page"` per study). Four or five placeholders per study, declared. No `<h1>`; no header or footer; `<nav>` allowed by the role; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder.
- Rendered and read at 1440. Corrections: 003 rebuilt without `display: contents` on the nav so its landmark survives; the 002 ellipse widened round the current page.
