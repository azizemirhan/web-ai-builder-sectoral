# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S25` — Article / Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the category prefix, the byline labels (Written by, Reviewed, Applies to), the general information note, the Key point, In this piece, About this piece and Related reading titles kept as written, every value bracketed, no topic, title, author, date, jurisdiction, heading, copy or related piece invented — are kept exactly. V1's own reserved-area count per study is kept as it set it: one in 001, two in 002, none in 003, one in 004, one in 005. This is a detail page, so V1's section title is promoted to the page's `<h1>`. The related-reading and contents `<nav>` landmarks are V1's own (`-AllowNav`).
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S25-001` | Universal / Safe | 001 Ivory & Olive | 1 — the piece read straight down one measure | column rules behind the head | A 50rem measure — head, the byline as three bare labelled fields, the 3:2 lead field, the three sections on the lead rule, the note, the related reading and the foot | 1 reserved · 15 | 156 |
| `FIN-S25-002` | Premium / Editorial | 002 Rosewood | 2 — the panoramic opening above a held measure | open bracket at the head | The 3:1 lead across the width; a 48rem measure with the three sections on the lead rule, the key point on the band tone after the first and the 3:2 in-body figure after the second, where V1 placed them | 2 reserved · 17 | 182 |
| `FIN-S25-003` | Dense / Information-heavy | 003 Lagoon | 3 — the piece worked as a navigable document | registration grid behind | The contents as a numbered list of underlined anchors and About this piece as bare labelled fields in the rail; the three sections as cells in a bordered plate on ink seams | none · 15 | 158 |
| `FIN-S25-004` | Conversion-led | 004 Iris | 4 — the piece beside a standing invitation | span mark under the title phrase | The three sections on the lead rule in a 46rem body column; the 4:5 lead field, the related reading and the invitation panel on the band tone held together in the rail | 1 reserved · 15 | 176 |
| `FIN-S25-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the framed opening above an offset measure | corner frame at the head | Title framed left with the standfirst opposite; the 4:1 lead strip; the byline standing in the left rail beside the three sections on the lead rule, offset inward | 1 reserved · 15 | 156 |

## What changed from V1

V1's rounded article cards, tinted byline pills, shaded key-point boxes and boxed contents panels go. The piece is a reading measure: the bracketed article title is the display `<h1>` with its second half in the accent, the byline is three bare labelled fields on hairlines, and the three sections are rows whose bracketed headings sit in ink above their bracketed copy. V1's general information note is carried in the graphite refusal tone behind the prohibition mark, so the refusal reads as a refusal rather than as a footnote. The key point keeps the information mark on the band tone, the contents keep the layers mark with underlined anchors to the section ids, About this piece keeps the person mark and Related reading the book mark. Each reserved photograph is an empty flat labelled field with V1's bracketed caption beneath. The darkened surfaces are the 002 key point and the 004 invitation panel.

## Verification

- `fincheck.ps1 -Sec S25 -AllowNav -Fields 'Resources|Topic|Approved article title|Approved standfirst|Written by|…|Bring this to a conversation'` — ALL CHECKS PASS; parity 95/95. One `<h1>` per study (detail page); no header/footer; the related-reading and contents navs are V1's (`-AllowNav`); no form; links only — the two related pieces and All resources to the same-variant S13, the conversation action to S19, and in 003 the three contents links to the section anchors on the page (all checked on disk); no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside the field ratio labels; no claim term.
- Rendered and read at 1440. Corrections: in 002 the accent lead rule was addressed by `.recb + .parts` rather than `:first-of-type`, which matched nothing because the byline block is the first `div` in the measure and the composition was left with no lead rule at all; in 005 a 4:1 ratio was added to the shared field helper so V1's *shallow lead strip* is actually shallow, which took the study from 1618px to 1510px.
