# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S26` — Person / Adviser Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the category prefix, the introduction, the section titles (How they work, Areas of focus, Works on, Background, At a glance, Get in touch), the fact labels (Team, Based at, Languages), the contact copy, the preparation line and the clearance statement kept as written, every value bracketed, no person, role, qualification, language, office, service or engagement invented, and no personal address or direct line offered — are kept exactly. V1's own reserved-area count per study is kept: a portrait in 001, 003, 004 and 005, none in 002. This is a detail page, so V1's name heading is promoted to the page's `<h1>`. The works-on `<nav>` is V1's own (`-AllowNav`).
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S26-001` | Universal / Safe | 001 Ivory & Olive | 1 — the identity row above a read profile | column rules behind the identity | A 4:5 portrait beside the name, role, focus, introduction and the three facts as bare labelled fields; four section rows on the lead rule beside the contact panel on the band tone | 1 reserved · 13 | 164 |
| `FIN-S26-002` | Premium / Editorial | 002 Rosewood | 2 — the profile read as one editorial column | open bracket at the head | A 52rem column — the bracketed head, four section rows on the lead rule, At a glance as bare labelled fields under the folder mark, then the contact block on the band tone | none · 12 | 156 |
| `FIN-S26-003` | Dense / Information-heavy | 003 Lagoon | 3 — the identity card beside a sectioned plate | registration grid behind | The portrait, name, role, focus and facts held in the rail; the four sections and the contact block as cells in a bordered plate on ink seams, How they work spanning the width | 1 reserved · 13 | 164 |
| `FIN-S26-004` | Conversion-led | 004 Iris | 4 — the identity above a standing contact band | span mark under the name | A 4:5 portrait beside the name with the span mark; V1's contact band on the band tone across the width; four section rows on the lead rule beside the facts and the clearance statement | 1 reserved · 13 | 164 |
| `FIN-S26-005` | Sector-native / Distinctive | 005 Ink & Apricot, inverted | 5 — the framed identity above an offset profile | corner frame around the identity | A 3:4 portrait framed beside the name, role, focus, V1's three focus areas and its introduction; how they work, the background, works on and At a glance offset inward beside the contact panel | 1 reserved · 13 | 164 |

## What changed from V1

V1's rounded profile cards, tinted role pills, avatar rings and boxed fact tables go. The name is the display `<h1>` with its second half in the accent; the verified role sits in ink beneath it and the area of focus in the muted tone. The profile sections are rows, each opened by its own mark — the compass for how they work, the tick for the areas of focus, the link for works on, the document for the background and the folder for At a glance — and the three facts are bare labelled fields on hairlines rather than a table. V1's clearance statement is carried in the graphite refusal tone behind the shield, so the consent note reads as the condition it is rather than as small print, and the contact panel keeps V1's routing through the firm with the preparation row on the information mark and no personal address anywhere. Each portrait is an empty flat labelled field with V1's bracketed caption beneath. The darkened surfaces are the 001, 002 and 005 contact panels, the 003 How they work cell and the 004 contact band.

## Verification

- `fincheck.ps1 -Sec S26 -AllowNav -Fields 'People|Team or office|Approved adviser name|…|All people'` — ALL CHECKS PASS; parity 125/125 on the slots common to all five. *Areas of focus* is checked separately because V1 carries it as a visible heading in 001–004 and as an `aria-label` only in 005, and the re-authored studies match that split exactly. One `<h1>` per study (detail page); no header/footer; the works-on nav is V1's (`-AllowNav`); no form; links only, all to existing same-variant studies (checked on disk); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term.
- Rendered and read at 1440. Corrections: in 003 the background cell was spanned across the plate so its seam runs the full width instead of stopping at the column break with an empty cell beside it; in 005 At a glance was put on its own rule, having read as a continuation of the works-on row above it.
