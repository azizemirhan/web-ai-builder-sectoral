# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S22` — Breadcrumb & Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the trail (Home, Services, current page), the parent return and, in 003, the two related topics kept as written, the current page a bracketed placeholder, no page, service or route invented; no heading, no media — are kept exactly. The `<nav>` landmarks are V1's own (`-AllowNav`); every link goes to the same-variant study V1 routed it to.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S22-001` | Universal / Safe | 001 Ivory & Olive | 1 — the inline trail with the parent return at the opposite edge | column rules behind the trail | One strip on hairlines — the trail left, the parent return right | none · 1 | 8 |
| `FIN-S22-002` | Premium / Editorial | 002 Rosewood | 2 — the editorial trail above a separate return | bracket above the trail | The trail on the lead rule with the current page enlarged; the return on a hairline beneath | none · 1 | 8 |
| `FIN-S22-003` | Structured / Visual Modular | 003 Lagoon | 3 — the contextual trail with a related row | registration grid behind | A bordered plate: the trail and return on the band tone beside the related label and two underlined links | none · 1 | 15 |
| `FIN-S22-004` | Conversion-led | 004 Iris | 4 — the parent return beside a framed trail | none (no display phrase) | A band on the band tone on the lead rule — the return as the bordered action left, the trail right | none · 1 | 8 |
| `FIN-S22-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the breadcrumb ribbon with the current-location marker | corner frame along the trail | The trail on the band tone with the current page in the accent; the return offset beneath | none · 1 | 8 |

## What changed from V1

V1's rounded strips, editorial trail, related row, framed trail and apricot ribbon go; the trail is Home with the home mark, muted slashes and the bracketed current page in ink (in the accent on 005), the parent return is an underlined link with the arrow (the bordered action with the exit mark in 004) and the related topics are the tracked label with the layers mark and underlined links. The darkened surfaces are the 003 trail cell, the 004 band and the 005 ribbon. Copy is V1's throughout; every link goes where V1 sent it.

## Verification

- `fincheck.ps1 -Sec S22 -AllowNav -Fields 'Home|Services|Current service|Back to all services'` — ALL CHECKS PASS; parity 20/20. No `<h1>`; no header/footer; the nav landmarks are V1's (`-AllowNav`); no form; links only, all to existing same-variant studies (checked on disk); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit; no claim term; one placeholder per study.
- Rendered and read at 1440. Correction: the return arrow set as a spaced `::before` so it does not collide with the label.
