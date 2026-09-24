# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S06` — Experts & Leadership · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — who shows up, stage by stage, including where they are not; portrait slates name the role, never the person; the firm's own people as placeholder names (initial and surname), marked and declared; `002` carries no photograph by argument; the media counts per study (5, 0, 1, 5, 5) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S06-001` | Universal / Safe | 001 Paper & Indigo | 10 in a row — portraits with offset tabs | ghost serif asterisk behind the head | Five 4:5 portrait figures in one row (three-then-two below 1100px), each with a band-tone tab, the serif placeholder name, a role chip and IN THE ROOM FOR / ON YOUR ENGAGEMENT as labelled fields, the engagement line on the accent edge; ruled foot with the closing line and one action | 5 × 4:5 · 5 names | 195 |
| `CONS-S06-002` | Premium / Editorial | 002 Sable & Bronze | 2 with 4 — head split, argument band | pencil ellipse round *asked* | Serif display and italic standfirst; V1's saturated argument block as a band on the tinted paper with the pencil rule and a struck-portrait mark; five ruled rows with tracked roles, serif names and two labelled fields; underlined route | none · 5 | 183 |
| `CONS-S06-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with 10 — lead figure in a bordered grid | ruled margin behind | The lead figure as the grid's first column — the only 4:5 portrait, its slate naming the partner who runs the engagement, ON YOURS on the accent edge — beside four modules sharing hairlines with stroke marks (person / calculator / speech / compass); band-tone foot cell | 1 × 4:5 · 5 | 175 |
| `CONS-S06-004` | Conversion-led | 004 White & Signal | 4 with 3 — bordered grid, band | underline stroke under *gaps* | Five portrait figures in a bordered three-then-two grid; V1's five-block stage strip drawn as five bordered squares labelled I–V, filled in the accent where the person is on the stage; band with the pencil rule, V1's closing line and the one action ASK FOR THE NAMES | 5 × 4:5 · 5 | 194 |
| `CONS-S06-005` | Art-directed / Distinctive | 005 Chalk & Violet | 6 as a credits sequence | bracket grouping the head | Five credit rows on hairlines — a small 1:1 portrait, the tracked role, the name in the serif at display scale, the room line and the stages on the accent edge; bordered action. V1's circular portraits become square 1:1 (the register carries no round media); the near-black ground becomes chalk | 5 × 1:1 · 5 | 182 |

## What changed from V1

Portrait cards become bare fields inside `<figure>` with the name in the `<figcaption>`; the stage strip's `01 02 03 04 05` becomes I–V so the strip stays legible without a digit; every "Stages 01 and 04" in copy is written "stages one and four" (the no-digit rule), recorded here for all five studies; `001` sits in one row at 1440 rather than V1's three-then-two (design layer only; the five people and their order are V1's). Names keep V1's placeholder demo values. No other copy changed.

## Verification

- `cslcheck.ps1 -Sec S06 -Fields '<five names>|In the room for|the contract'` — ALL CHECKS PASS; parity 35/35; five placeholders per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element.
- Rendered and read at 1440. Corrections: `001` tab moved onto the field with `isolation: isolate` so it no longer runs behind the caption (same fix applied to `S01-001`), and the row re-templated (height 1954 → 1075); `004` grid cell selector scoped to direct children so the stage strip keeps five columns.
