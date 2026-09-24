# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S22` — Breadcrumb / Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one `<nav aria-label="Breadcrumb">` with an ordered list, Home › Appointments › Your first visit, the current page not a link, the same-variant routes, no media, no script; the related and paired routes in 003 and 005 — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S22-001` | Universal / Safe | 001 Chalk | 1 — the path on two hairlines | 3px lead mark at the left end | One tracked breadcrumb line between two hairlines, accent arrow marks as separators, the current page in ink | none · 0 | 5 |
| `DN-S22-002` | Premium / Editorial | 002 Linen | 2 — the parent return first | — | *Back to Appointments* as a bordered action with the exit mark beside the compact breadcrumb, on one ink hairline | none · 0 | 8 |
| `DN-S22-003` | Structured / Visual Modular | 003 Slate | 3 — the path above related routes | — | The breadcrumb on a hairline; ALSO USEFUL on the lead rule beside three underlined routes with the arrow in a bordered row on ink seams | none · 0 | 14 |
| `DN-S22-004` | Conversion-led | 004 Daylight | 4 — the focusable rail | bar under *Your first visit* | The breadcrumb as a non-wrapping rail in a band, scrolling horizontally when narrow, the scroll cue shown below 560px | none · 0 | 10 |
| `DN-S22-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the path with its two neighbours | corner marks framing the breadcrumb | The breadcrumb framed; a bordered plate of two route cells on one seam — BACK TO THE OVERVIEW with the exit mark, EXPLORE NEXT with the arrow | none · 0 | 14 |

## What changed from V1

The breadcrumb takes the eyebrow register — 0.68rem, tracked, uppercase — with accent arrow marks as separators and underlined links in muted ink; V1's rounded band, dark band and back-pill become a hairline, a band tone and a bordered action. The 003 and 005 geometry layers are omitted where a dot grid or an arc would be noise on five words; the lead mark, the bar and the corner marks carry the variant. No script; the 004 rail scrolls natively. Routes are V1's, variant to variant.

## Verification

- `dncheck.ps1 -Sec S22 -AllowNav -Fields 'Home|Appointments|Your first visit'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; one breadcrumb `<nav>` per study, plus the related-pages `<nav>` in 003 and 005; no header/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy.
- Rendered and read at 1440. No corrections needed.
