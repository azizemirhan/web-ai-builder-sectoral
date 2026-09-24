# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S13` — Events & Webinars · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three sessions whose format, date, time, title, topic, venue and joining lines are bracketed placeholders, event details declared awaiting confirmation, no registration control, the note that dates and joining arrangements must be confirmed and that registration links appear once verified, one route to the same-variant programme list; no media in any study — are kept exactly. V1's `<details>` disclosures open as rows because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S13-001` | Universal / Safe | 001 Apricot | 1 — three equal sessions below an open introduction | loop behind the head | Split head with the lead and the graphite preview chip; three cells in a bordered grid on ink seams — the date and time line with the calendar mark, format chip, title, topic, venue with the place mark and the opened joining row; the action and the note on the lead rule | none · 25 | 166 |
| `EDU-S13-002` | Premium / Editorial | 002 Mulberry | 2 — stepped rows with generous type | rise above the head | Three ruled rows on the lead rule with the date, time and format chip in a left column and the title at display size, topic, venue and the opened joining row stepping in row by row; the action and the note on the closing hairline | none · 25 | 163 |
| `EDU-S13-003` | Structured / Visual Modular | 003 Cobalt | 3 — the introduction beside compact modules | cross grid behind | Narrow intro column with the chip, the action and the note on the lead rule; one bordered plate of three horizontal modules with the date line at the left of each | none · 25 | 163 |
| `EDU-S13-004` | Conversion-led | 004 Iris | 4 — the featured session with the joining disclosure made prominent | outline round *A shared moment.* | The first session as a band with the stacked date and time beside its title at display size and its joining row on the lead rule; the second and third as compact ruled rows; the action and the note on the closing hairline | none · 25 | 163 |
| `EDU-S13-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the staggered sessions | margin bar along the display column | Display column with the lead, the action and the chip; three sessions staggered — flush, dropped, half-dropped — with the same lines; the note on the closing hairline | none · 25 | 163 |

## What changed from V1

V1's event cards, its date tiles, the lime focal panel and the plus-marked disclosures go; each session is the bracketed date and time as a tracked line with the calendar mark, the format as an accent chip, the title in muted ink as a placeholder, the topic, the venue with the place mark and the joining details opened as a row with the document mark, all on hairlines or ink seams. PROGRAMME PREVIEW · EVENT DETAILS AWAITING CONFIRMATION is a graphite chip — the sector's `--no`. No registration control is drawn; V1's note that links appear once verified is kept. The only darkened surface is the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S13 -Fields 'Make room for a conversation|Event details awaiting confirmation|Event format|Day|Time zone|Session title 1|Session title 3|Topic, intended audience|Venue or online platform|Joining details|Host, duration, cost|Accessibility support|must be confirmed before attending|Explore programmes'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form, button or input; no `<details>`; one link per study to the same-variant `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; twenty-five placeholders per study.
- Rendered and read at 1440. Correction: 004 date and time stacked in their column so the featured band and the compact rows read as one grammar.
