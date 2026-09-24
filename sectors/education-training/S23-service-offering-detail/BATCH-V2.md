# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S23` — Service Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the admissions-guidance service kept whole: context line, headline, intro, What you can discuss with its boundary that guidance does not replace a formal assessment or guarantee an offer, Who it is for and Service scope as placeholders, the three preparation steps with two placeholders, the closing invitation and one route to the same-variant S19; no media in any study — are kept exactly. The page title is set as the `<h1>` this detail page owns, as the register sets every detail page.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S23-001` | Universal / Safe | 001 Apricot | 1 — the introduction beside the preparation guide | loop behind the head | Split head with the intro; the discussion with its boundary under the struck-circle mark and the two labelled facts in the left column; the three steps as a bordered plate with word-numeral chips; the closing with the action on the lead rule | none · 4 | 164 |
| `EDU-S23-002` | Premium / Editorial | 002 Mulberry | 2 — the overview above a three-part row | rise above the head | Split head; three ruled columns on the lead rule — discussion, facts, preparation steps; the closing on the closing hairline | none · 4 | 164 |
| `EDU-S23-003` | Structured / Visual Modular | 003 Cobalt | 3 — the summary cell beside grouped modules | cross grid behind | A bordered plate with V1's summary as a cell on the band tone, where V1 set its blue field, beside the discussion, facts and steps as modules; the closing on the lead rule | none · 4 | 164 |
| `EDU-S23-004` | Conversion-led | 004 Iris | 4 — the service detail with a prominent enquiry rail | outline round *your next step.* | The reading column — intro, discussion, facts, steps — beside V1's closing as a band on the band tone with the action on the lead rule | none · 4 | 164 |
| `EDU-S23-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the oversized introduction above the preparation band | margin bar along the display column | Display column beside the discussion and facts; the three steps as a band on the band tone in three columns, where V1 set its lime band; the closing on the closing hairline | none · 4 | 164 |

## What changed from V1

V1's rounded preparation guide, the blue summary field, the purple enquiry rail and the lime band go; the detail is bare type on hairlines or ink seams — the context line as a tracked eyebrow with the layers mark, the headline with one accent phrase, the boundary line in graphite with the struck-circle mark, Who it is for and Service scope as tracked labels with marks, the steps as word-numeral chips, the closing as a tracked eyebrow, a statement, its line and the 1px action. The darkened surfaces are the 003 summary cell, the 004 rail and the 005 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S23 -AllowClaims 'guarantee' -Fields 'Student services|Admissions guidance|your next step|Admissions guidance helps you organise|What you can discuss|Bring the programme name|does not replace a formal assessment|Who it is for|Confirmed applicant groups|Service scope|Included support, exclusions|Prepare for the conversation|Gather your questions|Note your programme|Check how to connect|Confirmed delivery format|Confirm the next step|Follow-up process|Ask about admissions guidance|Start with your question|mention this service|Contact admissions'` — ALL CHECKS PASS; parity 110/110. `guarantee` is allowed only for V1's boundary *does not replace a formal assessment or guarantee an offer* — a negation kept verbatim. One `<h1>` per study (a detail page); no header/nav/footer; no form or booking control; one link per study to the same-variant `EDU-S19`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; four placeholders per study.
- Rendered and read at 1440. Correction: the closing eyebrow kept at the label size inside the 004 rail.
