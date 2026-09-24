# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — *Your first visit.* as the page's `<h1>` in every study, the three topics named not linked, one question route in 004 only, no figure; the media counts per study (0, 1, 1, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S21-001` | Universal / Safe | 001 Chalk | 1 — the open page identity | ring behind the h1 | The h1 with the context lines beside; IN THIS GUIDE as three word-numeral chips on the lead rule with the audience line. No field | none · 0 | 55 |
| `DN-S21-002` | Premium / Editorial | 002 Linen | 2 — the editorial title over the strip | arc above the h1 | The h1 at display size with the introduction beside; the clinic reception as a contained 3:1 strip captioned *Patient information / First appointments* on the lead rule | 1 × 3:1 · 0 | 52 |
| `DN-S21-003` | Structured / Visual Modular | 003 Slate | 3 — page identity over one joined module | dot grid behind | The h1; one bordered plate on a single seam — the clinic reception as a 3:2 field beside the introduction, WHAT THIS PAGE COVERS as three chips on the lead rule, and the note | 1 × 3:2 · 0 | 63 |
| `DN-S21-004` | Conversion-led | 004 Daylight | 4 — the page context as a band | bar under *first visit* | The h1 in a band with the context lines beside; the question route on the lead rule with one bordered action carrying the speech mark to the contact study. No field | none · 0 | 45 |
| `DN-S21-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the asymmetric title with the field set low | corner marks framing the h1 | The h1 framed with the introduction offset right; the clinic reception as a low 3:1 field indented, FIRST APPOINTMENTS as its label and V1's line as its caption on the lead rule | 1 × 3:1 · 0 | 52 |

## What changed from V1

The page title keeps its `<h1>` and takes the display measure with one accent phrase; the topics become bordered word-numeral chips rather than a boxed topic line or tinted panel; V1's capsule image becomes a bare soft-cornered field. The only darkened surface is the 004 band. No breadcrumb, no header — that belongs to S22. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S21 -Fields 'first visit|appointment'` — ALL CHECKS PASS; parity 10/10. One `<h1>` per study as the page title; no header/nav/footer; no form; one link in 004 only; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. No corrections needed.
