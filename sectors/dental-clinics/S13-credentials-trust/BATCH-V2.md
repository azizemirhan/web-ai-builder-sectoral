# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S13` — Credentials & Trust · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the two halves marked, four by law and four chosen, no badge, no grade, no number, no registration, no letters after any name, the letters line and the closing line in every study; the media counts per study (1, 1, 2, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S13-001` | Universal / Safe | 001 Chalk | 1 — the two halves side by side | ring behind the head | REQUIRED BY LAW as a ruled list on the ink rule with an ink THE LAW chip on every line, beside NOT REQUIRED. WE DO IT ANYWAY on the lead rule with an accent CHOSEN chip; the sterilisation room as a 3:1 field; the letters line on the plum edge with the struck-person mark; foot | 1 × 3:1 · 0 | 196 |
| `DN-S13-002` | Premium / Editorial | 002 Linen | 2 — the one nobody prints | arc above the head | *If a treatment is the first of its kind for the person doing it, you are told before you agree.* as the head at display size; the room edge to edge at 21:9; the chosen half first at subhead weight, the law half second in muted; the letters line on the plum edge; foot | 1 × 21:9 · 0 | 175 |
| `DN-S13-003` | Structured / Visual Modular | 003 Slate | 3 — a notice and a claim | dot grid behind | The room as a 3:1 field; REQUIRED BY LAW as a bordered notice on the band tone in small ruled print, beside NOT REQUIRED as an open column on the lead rule with tick marks, ending in the instrument tray as a 2:1 field; the letters line on the plum edge; foot | 3:1 + 2:1 · 0 | 196 |
| `DN-S13-004` | Conversion-led | 004 Daylight | 4 — the loudest element demotes the credentials | bar under *It is the law.* | REQUIRED BY LAW as a band at display size — *This is the part a competitor would put badges on. It is the law.* — with the four lines chipped in ink inside it; the chosen four as a ruled row on the lead rule; the letters line on the plum edge; foot. No field | none · 0 | 188 |
| `DN-S13-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the compulsory half as small print | corner marks framing the head | *Four sentences somebody chose to write* with the four as ruled lines at statement size with word-numeral keys and tick marks; the room as a 3:1 field; REQUIRED BY LAW as one run of small print on the ink rule; the letters line on the plum edge; foot | 1 × 3:1 · 0 | 185 |

## What changed from V1

The law half never takes the accent: its chip, its rule and its label are ink, and in 002, 003 and 005 it drops to muted or small print. The chosen half carries the lead rule and the tick mark. The letters line carries the plum edge and the struck-person mark — the one refusal in the section. No badge, seal, star or shield anywhere; the darkened surfaces are the 003 notice and the 004 band. Fields are bare and labelled. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S13 -Fields 'not an achievement|on the public register|criminal offence|national standard and the log is kept|indemnity insurance|it is on the wall|what changed after each one|whether it reads well or not|first of its kind|read the sterilisation log|No letters appear after any name|the only place they mean anything|with badges around it'` — ALL CHECKS PASS; parity 65/65. No `<h1>`; no header/nav/footer; no form; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no credential, number or award term.
- Rendered and read at 1440. One correction: the 003 tray field was 3:2 and left a void beside the notice — set to 2:1.
