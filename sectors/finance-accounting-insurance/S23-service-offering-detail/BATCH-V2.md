# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S23` — Service Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the five section headings (Overview, What it includes, What it does not include, How it runs, Who it is for), the three inclusion lines, the three stages, the enquiry copy and the related-offering labels kept as written, every value bracketed, no offering, inclusion, exclusion, stage, client type, fee or turnaround invented — are kept exactly. This is a detail page, so V1's section title is promoted to the page's `<h1>`. The related-offerings `<nav>` is V1's own (`-AllowNav`); every link goes to the same-variant study V1 routed it to.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S23-001` | Universal / Safe | 001 Ivory & Olive | 1 — the reading body with a standing aside | column rules behind the title | The five sections on hairlines left; the 4:3 field, the enquiry panel and related offerings stacked right | 1 reserved · 10 | 220 |
| `FIN-S23-002` | Premium / Editorial | 002 Rosewood | 2 — the bracketed head above a panoramic field | open bracket at the head | Title and introduction split across the head; a 3:1 field full width; the sections in a reading column with the aside beside | 1 reserved · 10 | 220 |
| `FIN-S23-003` | Structured / Visual Modular | 003 Lagoon | 3 — the five-cell plate with a closing band | registration grid behind | A bordered plate on ink seams — the overview, how it runs and who it is for spanning, includes and excludes paired; a closing band on the band tone with the 1:1 field, enquiry panel and related offerings | 1 reserved · 10 | 220 |
| `FIN-S23-004` | Conversion-led | 004 Iris | 4 — the sections beside a persistent ask | span mark under the title phrase | The reading body left; the enquiry panel, the 4:5 field and related offerings held together in the right rail | 1 reserved · 10 | 220 |
| `FIN-S23-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the framed title above an offset body | corner frame at the head | Title framed left with the introduction opposite; the sections on the band tone offset inward beside the tall field; the enquiry panel and related offerings as a closing pair | 1 reserved · 10 | 220 |

## What changed from V1

V1's rounded offering cards, tinted inclusion chips, shaded stage counters and boxed enquiry block go. The five sections are rows on hairlines, each opened by its own mark — information for the overview, the tick for inclusions, the prohibition for exclusions, the compass for how it runs, the person for who it is for — with the inclusions as a plain list and the stages as an ordered list whose names sit in ink and whose bracketed detail sits in the muted tone. The offering title is the display `<h1>` with its second half in the accent, above V1's category prefix; the reserved photograph is an empty flat labelled field with V1's bracketed caption beneath. The enquiry panel keeps V1's bordered action to S19 and its underlined link to S20, with the preparation note opened as a row on the information mark. Related offerings stay a bordered `<nav>` of underlined links. The darkened surfaces are the 003 overview cell and closing band, the 004 rail and the 005 body and panels.

## Verification

- `fincheck.ps1 -Sec S23 -AllowNav -Fields 'Services|Service category|Approved offering title|…|Resources and guides'` — ALL CHECKS PASS; parity 115/115. One `<h1>` per study (detail page); no header/footer; the related-offerings nav is V1's (`-AllowNav`); no form; links only, all to existing same-variant studies (checked on disk); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term; ten placeholders per study.
- Rendered and read at 1440. Corrections: in 003 the section rows were set `align-content: start` so the shorter exclusions cell no longer distributes its rows to the height of the inclusions cell beside it, and *How it runs* was spanned across the plate so its seam runs the full width instead of stopping at the column break.
