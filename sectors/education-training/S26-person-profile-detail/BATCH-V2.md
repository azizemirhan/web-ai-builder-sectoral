# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S26` — Person Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the instructor profile as bracketed placeholders throughout, each carrying V1's instruction to use the person's approved words and confirmed facts, the portrait reserved with consent and labelled by role only, the note routing course questions to admissions, two routes to the same-variant S02 and S19; the media counts per study (1, 1, 0, 0, 1) — are kept exactly. No identity, qualification, affiliation or pronoun is introduced. The bracketed name is set as the `<h1>` this detail page owns.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S26-001` | Universal / Safe | 001 Apricot | 1 — the identity and portrait beside a continuous biography | loop behind the identity | Identity column with the bracketed name, role, summary and a 4:5 portrait field; the biography beside as three ruled sections with the catalogue link and the action to admissions on the lead rule | 4:5 · 7 | 158 |
| `EDU-S26-002` | Premium / Editorial | 002 Mulberry | 2 — the identity and portrait above a three-column profile | rise above the name | Identity with a compact 1:1 portrait field beside; background, teaching and contact as three ruled columns on the lead rule | 1:1 · 7 | 158 |
| `EDU-S26-003` | Structured / Visual Modular | 003 Cobalt | 3 — the identity cell with grouped modules | cross grid behind | A bordered plate with the identity as a cell on the band tone, where V1 set its blue field, beside the three modules stacked | none · 7 | 150 |
| `EDU-S26-004` | Conversion-led | 004 Iris | 4 — the open biography with a contact panel | outline round the name | The reading column with background and teaching beside V1's Get in touch as a band on the band tone with the action on the lead rule | none · 7 | 150 |
| `EDU-S26-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the oversized identity with the portrait and a teaching band | margin bar along the identity column | Identity at the largest size in the accent with a 3:4 portrait field dropped beside; background as a ruled section; teaching as a band where V1 set its lime panel; the contact on the closing hairline | 3:4 · 7 | 158 |

## What changed from V1

V1's portrait frames and curved crop, the blue identity field, the purple contact panel and the lime teaching panel go; the profile is bare type on hairlines or ink seams — the context line as a tracked eyebrow with the person mark, the bracketed name as the h1 in muted ink (or in the accent where V1 made it the display), the role as a tracked line, the sections with the document, layers and speech marks, the catalogue route as an underlined link and the admissions route as the 1px action. The portrait is a bare 8px field labelled THE INSTRUCTOR. The darkened surfaces are the 003 identity cell, the 004 contact panel and the 005 teaching band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S26 -Fields 'People|Instructor profile|Instructor name|Verified teaching role|subject focus and current teaching responsibilities|Background|Describe the professional experience|Explain their approach to teaching|Teaching|Name the confirmed programmes|Browse programme catalogue|Get in touch|A question about their teaching|Approved professional contact route|admissions can help you find|Contact admissions'` — ALL CHECKS PASS; parity 80/80. One `<h1>` per study (a detail page); no header/nav/footer; no form or direct contact control; two links per study to the same-variant `EDU-S02` and `EDU-S19`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; seven placeholders per study.
- Rendered and read at 1440. No corrections needed.
