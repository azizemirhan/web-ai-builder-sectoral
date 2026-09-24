# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S25` — Article & Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — eyebrow, headline, standfirst, byline labels, three section titles and their copy and the action label kept as written, the author, date and publication notes bracketed placeholders, no author, date, source or licence named, one link to the same-variant S15; one reserved editorial photograph, never a person — are kept exactly. V1's `<h2>` is promoted to the page's `<h1>` because this is a detail page; V1's `<details>` disclosure opens as a row.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S25-001` | Universal / Safe | 001 Sunlit | 1 — the reading column beside a tall field | arc behind the head | Headline, standfirst and marked byline above three section rows on the lead rule, the publication-notes row and the action; a tall 4:5 field beside | 1 · 3 | 187 |
| `ENG-S25-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial opening above a quiet reading column | rise above the head | A 3:1 field on the lead rule; three section rows in two columns; the publication-notes row and the action beneath | 1 · 3 | 187 |
| `ENG-S25-003` | Structured / Visual Modular | 003 Tidal | 3 — the attribution rail beside the article with an inline field | dot grid behind | A bordered plate: the article cell on the band tone with its publication-notes row on the lead rule, beside a compact 4:3 field | 1 · 3 | 187 |
| `ENG-S25-004` | Conversion-led | 004 Daybreak | 4 — the editorial opening above the reading column and resource pathway | outline round *your solar project* | Three section columns on the lead rule; the publication-notes row beside the action inside a band on the band tone; a 3:1 field beneath | 1 · 3 | 187 |
| `ENG-S25-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the photo-led opening with an offset article | margin bar along the display column | A 4:5 field beside the display column; the section rows, publication-notes row and action as an offset band on the band tone | 1 · 3 | 187 |

## What changed from V1

V1's centred reading column, split opening, teal attribution rail, blue opening and lime closing thought and the plus-marked disclosure go; the headline is the h1 with the accent phrase, the byline is a marked list with bracketed values, the three sections are rows with their marks (speech, pin, information), the publication notes open as a row with the information mark and the resource action is the register's bordered button. The darkened surfaces are the 003 article cell, the 004 notes band and the 005 article band. Copy is V1's throughout; no author, date or licence appears anywhere.

## Verification

- `engcheck.ps1 -Sec S25 -Fields 'Planning perspectives|Article|A clearer brief for|A useful project brief makes room|Written by|Approved author|Published|Verified date|Start with the question|Describe the decision the project|Describe the site|Bring together the location|Keep unknowns visible|A brief can evolve|Publication notes|Editorial approval|Browse further resources|Site perspective'` — ALL CHECKS PASS; parity 90/90. One `<h1>` per study; no header/nav/footer; no form; one link (same-variant S15, as V1 routed it); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio label; no claim term; three placeholders per study.
- Rendered and read at 1440. No correction needed.
