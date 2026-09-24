# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Finance, Accounting & Insurance` · Prefix: `FIN` · Section: `FIN-S14` — Compliance Calendar · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, FIN translation in `../FINANCE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — three obligation slots and the scope title kept as written, the dates, titles, descriptions, source lines and scope notes bracketed placeholders, no date, deadline, jurisdiction, entity, period, holiday adjustment or official reference named; no media in any study — are kept exactly. V1's bracketed obligation titles gain the `data-placeholder="true"` attribute their brackets imply (thirteen placeholders per study, from V1's ten); V1's numerals become word-numeral chips; V1's `<details>` disclosure opens as a row.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `FIN-S14-001` | Universal / Safe | 001 Ivory & Olive | 1 — the agenda with date markers and open event rows | column rules behind the head | Three event cells in a bordered grid with word-numeral chips, bracketed dates at display size, titles, descriptions and source lines | none · 13 | 164 |
| `FIN-S14-002` | Premium / Editorial | 002 Rosewood | 2 — the introduction beside an editorial calendar sequence | bracket above the headline | Three ruled event rows on the lead rule with the chip column and the bracketed date at display size | none · 13 | 164 |
| `FIN-S14-003` | Structured / Visual Modular | 003 Lagoon | 3 — the dates arranged as three generous calendar cards | registration grid behind | A bordered plate with one obligation as a tall cell on the band tone, its date in the accent, beside two stacked event cells | none · 13 | 164 |
| `FIN-S14-004` | Conversion-led | 004 Iris | 4 — the featured date above two complementary agenda entries | span mark beneath *the dates ahead.* | Three event rows stacked beside the head rail, each description and source line on the band tone | none · 13 | 164 |
| `FIN-S14-005` | Art-directed / Distinctive | 005 Ink & Apricot, inverted | 5 — the agenda with date capsules and spacious event narratives | corner frame along the display column | Three event columns, the middle raised as a panel on the band tone | none · 13 | 164 |

## What changed from V1

V1's rounded date markers, editorial sequence, calendar cards, violet featured date and apricot capsules and the plus-marked disclosure go; each entry is a word-numeral chip with its mark, the bracketed date at display size in ink, the bracketed obligation title as type in muted ink, the bracketed description and the bracketed source line, with V1's calendar-scope disclosure opened as a row with the information mark on a hairline. The darkened surfaces are the 003 first cell, the 004 descriptions and the 005 central panel. Copy is V1's throughout; no date, deadline or reference appears anywhere.

## Verification

- `fincheck.ps1 -Sec S14 -Fields 'Planning ahead|Compliance calendar|A little clarity for|the dates ahead|See upcoming obligations|Day|Month|Approved obligation title|Confirmed filing obligation|Confirmed payment obligation|Confirmed review or renewal|Official source|last verified date|Calendar scope and source notes|Confirmed calendar year'` — ALL CHECKS PASS; parity 75/75. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; thirteen placeholders per study.
- Rendered and read at 1440. Correction: in 002 every item child other than the chip is held in the content column, so the source line no longer falls under the chip.
