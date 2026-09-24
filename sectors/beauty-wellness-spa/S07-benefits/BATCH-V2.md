# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S07` — Benefits · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the six commitments about how the room is run are retained.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S07-001` | Universal / Safe | 001 Linen & Olive | 1 + ruled list | Intro column with a 4:5 field; six commitments as a two-column ruled list with accent dashes | 1 | 159 |
| `WELL-S07-002` | Premium / Editorial | 002 Bone & Clay | wide field + statements | A 21:8 field; three serif statements at publication size in one centred measure | 1 | 78 |
| `WELL-S07-003` | Structured / Visual Modular | 003 Mist & Moss | 3 + two-tier modules | Two cells sharing a hairline — in the room / around the visit — each with a 16:10 field and three ruled modules | 2 | 185 |
| `WELL-S07-004` | Conversion-led | 004 Sand & Ochre | 4 — tinted band | One commitment promoted in a band with a 4:5 field and one action; three ruled supporting commitments | 1 | 93 |
| `WELL-S07-005` | Art-directed / Distinctive | 005 Ivory & Plum | 3 — cells with large figures | Four cells sharing hairlines, display-size accent serif numerals, commitment at the base | 0 | 105 |

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on the three shared commitments 30/30.
- Rendered and read at 1440 and 390. Correction: `004` head and supporting row lost their inline inset (`padding` shorthand on a `.shell` element) — `padding-block` used instead. Noted as a recurring pitfall: never set `padding` shorthand on an element that also carries `.shell`.