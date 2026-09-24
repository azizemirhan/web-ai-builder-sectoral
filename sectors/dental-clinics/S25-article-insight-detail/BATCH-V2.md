# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S25` — Article / Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the page's `<h1>`, the standfirst, author and date as bracketed placeholders marked editorial draft, three chapters, the pull line, two related-reading links, no figure, no claim; the media counts per study (1, 1, 2, 0, 2) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S25-001` | Universal / Safe | 001 Chalk | 1 — the reading column with a rail | ring behind the h1 | Byline chips on a hairline; three chapters as a narrow reading column with word-numeral labels, the first on the lead rule; a rail with the dentist in conversation at 4:5, the pull line and KEEP READING | 1 × 4:5 · 1 | 173 |
| `DN-S25-002` | Premium / Editorial | 002 Linen | 2 — the title beside the lead image, then a centred article | arc above the h1 | The h1, standfirst and byline beside the consultation room at 4:3; a centred reading column with the pull line on the lead rule between chapters one and two; two related links | 1 × 4:3 · 1 | 170 |
| `DN-S25-003` | Structured / Visual Modular | 003 Slate | 3 — the broad title and strip over open chapters | dot grid behind | The two fields as a seamed 3:1 strip in one bordered plate; the three chapters as a bordered row of three cells; the pull line full width on the lead rule beside KEEP READING | 2 × 3:1 · 1 | 181 |
| `DN-S25-004` | Conversion-led | 004 Daylight | 4 — the typography-led guide with the opening line as a band | bar under *your questions* | The pull line at display size in a band with V1's three short sentences on the lead rule; a single reading column; KEEP READING on the lead rule. No field | none · 1 | 173 |
| `DN-S25-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the centred article with an opening field and a closing pair | corner marks framing the h1 | The h1 centred and framed with the byline; the dentist in conversation at 3:1; the pull line on the lead rule; a centred reading column; the consultation room at 3:2 beside KEEP READING | 3:1 + 3:2 · 1 | 181 |

## What changed from V1

The byline becomes two bordered placeholder chips with EDITORIAL DRAFT in the plum — the one refusal in an article that promises nothing. V1's amber quotation and curved image become the 004 band and a bare soft-cornered field; the pull line takes the lead rule in every study. Word-numerals count the chapters; the related reading is underlined with the arrow. No date, no reading time, no share row. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S25 -AllowNav -Fields 'name pending|date pending|Editorial draft|Start with one thing|perfectly organised list|Use your own words|Everyday language is enough|Before you leave|questions you would like to revisit|worth asking|A first dental consultation|Browse patient resources'` — ALL CHECKS PASS; parity 60/60. One `<h1>` per study; the related-reading `<nav aria-label="Keep reading">` is the only nav; no header/footer; no form; two links per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. No corrections needed.
