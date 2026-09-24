# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S16` — Insurance & Financing · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — two relationships and we are only in one, no panel, no logo wall, no provider, no rate, the refused-claim line, the ring line and the closing line in every study; the media counts per study (1, 0, 2, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S16-001` | Universal / Safe | 001 Chalk | 1 — two runs, we are only in one | ring behind the head | BETWEEN YOU AND YOUR INSURER as ruled lines on the plum rule with struck marks beside BETWEEN YOU AND US on the lead rule with tick marks, the person who does the paperwork as a 4:5 field labelled by role at the foot of our run; ring line; foot | 1 × 4:5 · 0 | 208 |
| `DN-S16-002` | Premium / Editorial | 002 Linen | 2 — the sentence that replaces the logo wall | arc above the head | *We are not on anyone's panel.* at display size with its line beside; the two sides as ruled columns, the insurer side in the plum; ring line; foot on the lead rule. No field | none · 0 | 186 |
| `DN-S16-003` | Structured / Visual Modular | 003 Slate | 3 — one rule, nothing crosses it | dot grid behind | Two columns on a single full-height 3px plum rule; the insurer side ends in *There is no photograph on this side. None of it happens here.* in the plum; our side ends in the desk at 3:2 and the person at 4:5; ring line; foot | 3:2 + 4:5 · 0 | 231 |
| `DN-S16-004` | Conversion-led | 004 Daylight | 4 — the refusal risk first | bar under *the same amount* | IF THE CLAIM IS REFUSED as a band at display size with *The risk is real. The surprise is not.* on the plum edge; two ruled columns; the desk as a 3:1 field; ring line on the lead rule; foot | 1 × 3:1 · 0 | 207 |
| `DN-S16-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — one line with a sentence on it | corner marks framing the head | The insurer's three items as a plum ruled row above; a full-width 3px plum rule with *We are not part of anything above this line.* sitting on it; our three items as a ruled row on the lead rule below; ring line; foot on the lead rule. No field | none · 0 | 202 |

## What changed from V1

The insurer's side carries the refusal token in every study — plum rule, plum column, plum edge or the plum line itself — and our side carries the lead rule and the tick mark. No insurer logo, card, badge or rate appears; the person who does the paperwork is a field labelled by role, never a portrait with a name. The only darkened surface is the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S16 -Fields 'does not change if they say no|not on anyone|claim it back yourself|usually will not cover|the excess|If the claim is refused|the same amount|itemised receipt|do not arrange credit|nobody|need to spread it|stops when you stop|before the first appointment rather than after it|which claims fail'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no provider, rate or guarantee term.
- Rendered and read at 1440. No corrections needed.
