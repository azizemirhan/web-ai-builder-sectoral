# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S20` — Contact & Final CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — headline, lead, fact labels and closing note kept as written, the team name, enquiry route, email, telephone and availability bracketed placeholders and never real contact details, one link to the same-variant S18; no media in any study — are kept exactly. V1's bracketed name now carries `data-placeholder="true"`; V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements in the S13 grammar.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S20-001` | Universal / Safe | 001 Sunlit | 1 — the closing invitation beside the contact panel | arc behind the head | Head, the Prepare your enquiry action and lead in a left column; the contact as a panel on the band tone beside, its note row on the lead rule | none · 5 | 113 |
| `ENG-S20-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial closing headline above an open horizontal contact layout | rise above the head | The contact in two columns on the lead rule — bracketed name at display size, then the route, three marked facts and the opened note row | none · 5 | 113 |
| `ENG-S20-003` | Structured / Visual Modular | 003 Tidal | 3 — the contact panel paired with the compact closing statement | dot grid behind | A bordered plate: head, action and lead as an open cell beside the contact cell on the band tone, its note row on the lead rule | none · 5 | 113 |
| `ENG-S20-004` | Conversion-led | 004 Daybreak | 4 — the wide closing stage pairing contact information and the enquiry action | outline round *starts with a conversation.* | The contact as a full-width band on the band tone — name in a left column, the route and facts beside, the note row on the lead rule across | none · 5 | 113 |
| `ENG-S20-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the oversized closing statement above an offset contact panel | margin bar along the display column | The contact as an offset band on the band tone, its note row on the lead rule | none · 5 | 113 |

## What changed from V1

V1's rounded warm panel, horizontal layout, teal panel, blue stage, lime panel, arrow-marked text link and the plus-marked disclosure go; the action is the register's bordered button with the arrow mark beneath the headline, the contact is the CONTACT label with the mail mark, the bracketed name as type in muted ink, the bracketed route, V1's three facts as a marked list with bracketed values and the note disclosure opened as a row with the information mark. The darkened surfaces are the 001, 003, 004 and 005 contact panels. Copy is V1's throughout; no real contact detail appears anywhere.

## Verification

- `engcheck.ps1 -Sec S20 -Fields 'Bring your site, your goals|Prepare your enquiry|Contact team name|Confirmed project enquiries handled|Email|Verified enquiry email|Phone|Phone with country code|Availability|Days, hours and time zone|Before you get in touch|Have your site location, project goals'` — ALL CHECKS PASS; parity 60/60. No `<h1>`; no header/nav/footer; no form; one link (same-variant S18, as V1 routed it); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; five placeholders per study.
- Rendered and read at 1440. Correction: the bracketed team name set in muted ink like the other placeholders.
