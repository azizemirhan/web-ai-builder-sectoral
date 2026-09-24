# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S23` — Service / Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the page's `<h1>`, the two chapters, the three steps, before your visit, one primary action to the contact study and one secondary to the treatments study, no price, no outcome, no figure; the media counts per study (1, 1, 2, 0, 1) — are kept exactly. V1's `<details>` disclosures in 004 open as ruled rows, because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S23-001` | Universal / Safe | 001 Chalk | 1 — the room above an open three-part story | ring behind the h1 | The h1 with the lead and primary action beside; the consultation room as a 3:1 field; two ruled columns; the three steps as bordered cells with word-numeral chips; before your visit on the lead rule with the secondary link | 1 × 3:1 · 0 | 193 |
| `DN-S23-002` | Premium / Editorial | 002 Linen | 2 — the tall room beside the narrative | arc above the h1 | The consultation room as a 4:5 field captioned *A conversation. A considered next step.* on the lead rule; the h1 and the four chapters as one continuous ruled column with tracked labels; the two actions on the lead rule | 1 × 4:5 · 0 | 195 |
| `DN-S23-003` | Structured / Visual Modular | 003 Slate | 3 — joined chapters, each led by its field | dot grid behind | One bordered plate — the consultation room beside the first two chapters, the dentist in conversation beside the three steps, a full-width band row holding before your visit and the two actions | 2 × 3:2 · 0 | 200 |
| `DN-S23-004` | Conversion-led | 004 Daylight | 4 — the question-led introduction | bar under *your questions* | *Let's start with your questions.*; the two questions opened as ruled rows with the question as a tracked label; ONE STEP AT A TIME as a band with the primary action; three ruled steps; before your visit on the lead rule. No field | none · 0 | 219 |
| `DN-S23-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the asymmetric composition with the field as anchor | corner marks framing the h1 | The h1 framed with the introduction and *You bring the questions. We begin there.* offset; two ruled chapters with the primary action on the lead rule; the consultation room as a 4:3 field beside the three steps; before your visit with the secondary link | 1 × 4:3 · 0 | 196 |

## What changed from V1

The page title keeps its `<h1>` at the display measure; V1's arched anchor becomes a bare soft-cornered field; V1's amber rail becomes the 004 band; the disclosures open. The primary action is the 1px ink border with the speech mark, the secondary an underlined line with the arrow. Word-numeral chips and keys count the three steps. The darkened surfaces are the 003 last row and the 004 band. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S23 -Fields 'what matters to you|relevant dental history|discussed separately|return after time away|immediate concern|Share your concerns|Explore the next step|Take time to decide|written cost|have chosen a treatment|Ask about a consultation|Explore dental treatments'` — ALL CHECKS PASS; parity 60/60. One `<h1>` per study as the page title; no header/nav/footer; no form; no `<details>`; two links per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no price, outcome or claim term.
- Rendered and read at 1440. No corrections needed.
