# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S19` — Contact · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — telephone, email, address and hours as reserved tokens never real details, the three routes in every study, the sensitive-information line, a form that sends nothing and says so; the media counts per study (1, 1, 3, 1, 1) — are kept exactly. V1's `<details>` disclosures and its local review-and-copy script are replaced: the tokens are shown open as placeholder chips, and the review action is a plain button with the honesty line beneath, because the register runs no script.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S19-001` | Universal / Safe | 001 Chalk | 1 — the welcome beside the message | ring behind the head | *A little hello. A good start.*; the reception area as a 3:1 field; the three routes as ruled rows on the lead rule with token chips, beside a static three-field form with the review button and the honesty line on the plum edge | 1 × 3:1 · 4 | 143 |
| `DN-S19-002` | Premium / Editorial | 002 Linen | 2 — the editorial welcome | arc above the head | *Good care starts with a hello.* at display size; the clinic reception edge to edge at 21:9; *Come as you are.* at statement size; three ruled routes with token chips; the write-first note on the plum edge. No form | 1 × 21:9 · 3 | 114 |
| `DN-S19-003` | Structured / Visual Modular | 003 Slate | 3 — one team, three modules | dot grid behind | One bordered plate — VISITING THE CLINIC wide with a 3:2 field, CALL and EMAIL side by side each with a 2:1 field — every module with its line and token chips; the not-sure line on the lead rule. No form | 3:2 + 2 × 2:1 · 3 | 172 |
| `DN-S19-004` | Conversion-led | 004 Daylight | 4 — the question first | bar under *your question* | The form as a band — three bordered radio chips, two fields, the review button and the honesty line on the plum edge; beside it the reception area as a 4:5 field over three ruled routes with token chips | 1 × 4:5 · 4 | 138 |
| `DN-S19-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — conversation typography with the field set into it | corner marks framing the head | *Dental care starts here.* with *A little less on your mind.* as the lead; the reception team at work as a 3:2 field beside the statement; three ruled routes labelled FOR A CONVERSATION, FOR A QUIET FIRST STEP, PLAN YOUR VISIT with token chips; the first-email note on the plum edge. No form | 1 × 3:2 · 3 | 115 |

## What changed from V1

The disclosures open: every reserved token is printed as a bordered chip, so nothing needs a click to be seen and nothing pretends to dial. The form keeps V1's fields and labels, drops the script, and says *Nothing has been sent.* on the plum edge beneath a button that goes nowhere. No pill, no capsule, no filled panel; the only darkened surface is the 004 band that holds the form. Device, document and building marks name the routes. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S19 -AllowForm -Fields 'Clinic telephone|Opening days and hours|Clinic email|Clinic address|Town / postcode|sensitive health information'` — ALL CHECKS PASS; parity 30/30. No `<h1>`; no header/nav/footer; forms only in 001 and 004, no `action`, no submit; no link; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. No corrections needed.
