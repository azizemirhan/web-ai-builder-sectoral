# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S26` — Person / Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the bracketed name as the page's `<h1>`, every profile field a bracketed placeholder marked `data-placeholder`, profile pending, the portrait labelled by role only, no invented name, no letters after a name, no pronoun, the enquiry and the three routes; the media counts per study (1, 1, 1, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S26-001` | Universal / Safe | 001 Chalk | 1 — the portrait-led identity split | ring behind the h1 | The clinician in conversation at 4:5 beside the name, the role chip, the plum pending chip, AT THE CLINIC and the enquiry action on the lead rule; AREAS OF FOCUS, HOW THEY WORK and PROFESSIONAL BACKGROUND as three ruled columns; two links on the lead rule | 1 × 4:5 · 9 | 160 |
| `DN-S26-002` | Premium / Editorial | 002 Linen | 2 — the centred name above a flanked portrait | arc above the h1 | The name centred with the chips; two ruled columns flanking the portrait at 4:5; the enquiry action and the two links on the lead rule | 1 × 4:5 · 9 | 160 |
| `DN-S26-003` | Structured / Visual Modular | 003 Slate | 3 — the portrait and identity as one object | dot grid behind | One bordered plate joining the 4:5 portrait and the identity; a bordered two-by-two of the narrative with the enquiry on the band tone; two links on the lead rule | 1 × 4:5 · 9 | 160 |
| `DN-S26-004` | Conversion-led | 004 Daylight | 4 — the type-led identity with the enquiry as a band | bar under the name | The name with the bar and chips beside the enquiry band with the action; the profile as a ruled essay column with labels on the left; two links on the lead rule. No field | none · 9 | 149 |
| `DN-S26-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the oversized identity with a staggered biography | corner marks framing the name | The name framed at the largest measure with the chips and the enquiry action beside the 4:5 portrait; four ruled rows staggered flush and indented in V1's order; two links on the lead rule | 1 × 4:5 · 9 | 160 |

## What changed from V1

The bracketed name prints in muted ink as the h1 so it reads as a placeholder; the role becomes an accent chip and PROFILE INFORMATION PENDING a plum chip — the refusal to publish an unverified person. V1's arched and capsule portraits become a bare soft-cornered 4:5 field labelled *The clinician · in conversation*, never a name on the field. The registration line stays a bracketed placeholder on a hairline; no letters, no number. The darkened surfaces are the 003 enquiry cell and the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S26 -AllowClaims 'award' -Fields 'Clinician name|Verified role within the clinic|Profile information pending|At the clinic|Areas of focus|How they work|Professional background|Registration|A question for the team|Ask about this clinician|Meet the wider team|Explore dental treatments'` — ALL CHECKS PASS; parity 60/60. `award` is allowed because V1's placeholder reads *awarding institutions* inside a bracketed field; no award claim appears. One `<h1>` per study; no header/nav/footer; no form; three links per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; nine placeholders per study.
- Rendered and read at 1440. No corrections needed.
