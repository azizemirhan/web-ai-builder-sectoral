# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S25` — Article / Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the article kept as written: context line, title, intro, the byline as two placeholders, three passages, the continue-reading close and one route to the same-variant S14; the media counts per study (1, 1, 0, 0, 1), the image a quiet learning space and never a person — are kept exactly. The article title is set as the `<h1>` this detail page owns.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S25-001` | Universal / Safe | 001 Apricot | 1 — the reading column beside the quiet space | loop behind the head | Head with the intro and the bracketed byline; three ruled passages with word-numeral chips beside a 4:5 field of the quiet desk; the close with the action on the lead rule | 4:5 · 2 | 199 |
| `EDU-S25-002` | Premium / Editorial | 002 Mulberry | 2 — the title and shallow panorama above a centred column | rise above the title | Split head; a shallow 3:1 field on the lead rule; the three passages in a centred measured column; the close on the closing hairline | 3:1 · 2 | 199 |
| `EDU-S25-003` | Structured / Visual Modular | 003 Cobalt | 3 — the article introduction beside grouped passages | cross grid behind | A bordered plate with the introduction as a cell on the band tone, where V1 set its blue field, beside the three passages as rows; the close on the lead rule | none · 2 | 190 |
| `EDU-S25-004` | Conversion-led | 004 Iris | 4 — the open article with a further-reading rail | outline round *your next course.* | The reading column beside V1's continue-reading close as a band on the band tone with the action on the lead rule | none · 2 | 190 |
| `EDU-S25-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the oversized title with the accented opening | margin bar along the display column | Display column with the title at the largest size, the intro and the byline, a 4:5 field dropped beside; three ruled passages with the first heading in the accent; the close on the closing hairline | 4:5 · 2 | 199 |

## What changed from V1

V1's rounded and curved images, the blue introduction field and the purple further-reading rail go; the article is bare type at a reading measure — the context line as a tracked eyebrow with the book mark, the title with one accent phrase, the byline as tracked labels with the person and calendar marks, the passages as word-numeral chips over their headings on hairlines, the close as a tracked eyebrow, a statement and the 1px action. The fields are bare 8px areas labelled THE QUIET DESK. The darkened surfaces are the 003 introduction cell and the 004 rail. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S25 -Fields 'Learning notes|Choosing a course|your next course|A course can begin with curiosity|Written by|Verified author|Published|Verified publication date|Start with a question|What would you like to explore|Picture an ordinary week|Think about when and where|Read beyond the title|Look at the topics|Continue reading|More room to explore|Browse learning resources'` — ALL CHECKS PASS; parity 85/85. One `<h1>` per study (a detail page); no header/nav/footer; no form; one link per study to the same-variant `EDU-S14`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; two placeholders per study.
- Rendered and read at 1440. No corrections needed.
