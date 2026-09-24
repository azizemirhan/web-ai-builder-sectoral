# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S20` — Final Apply / Enrol CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the closing statement, lead and note kept as written, two routes to the same-variant S07 and S02, no form or application control, no deadline, fee or requirement introduced; the media counts per study (0, 1, 0, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S20-001` | Universal / Safe | 001 Apricot | 1 — the closing statement with the actions beside it | loop behind the head | Split statement with the lead; the action with the arrow mark, the underlined link and the note on the lead rule | none · 0 | 52 |
| `EDU-S20-002` | Premium / Editorial | 002 Mulberry | 2 — the invitation beside a field | rise above the head | The invitation with the lead, the action, the link and the note on the lead rule; a 4:5 field of a learning environment beside | 4:5 · 0 | 59 |
| `EDU-S20-003` | Structured / Visual Modular | 003 Cobalt | 3 — the invitation above an action band | cross grid behind | Split head; V1's action band as a band on the band tone split by the lead rule with the action, the link and the note | none · 0 | 52 |
| `EDU-S20-004` | Conversion-led | 004 Iris | 4 — the centred invitation with the prominent next step | outline round *what comes next.* | Centred statement, lead at a measured width, the action, the link and the note centred on the lead rule | none · 0 | 52 |
| `EDU-S20-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the oversized invitation beside a field | margin bar along the display column | Display column with the lead, the action, the link and the note; a 3:2 field dropped beside | 3:2 · 0 | 59 |

## What changed from V1

V1's rounded closing banner, the filled purple and blue panels and the curved photograph go; the close is the statement with one accent phrase, the primary route as the 1px action with the arrow mark and the secondary as the underlined link, the note in muted ink. The only darkened surface is the 003 band; the fields are bare 8px areas labelled THE ROOM. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S20 -Fields 'Turn your interest into a next step|Review application steps|Find a programme|Requirements, fees and dates vary'` — ALL CHECKS PASS; parity 20/20. No `<h1>`; no header/nav/footer; no form or application control; two links per study to the same-variant `EDU-S07` and `EDU-S02`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; no placeholder needed.
- Rendered and read at 1440. No corrections needed.
