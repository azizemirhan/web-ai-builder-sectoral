# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S03` — Capabilities · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — everybody claims the same six, so each capability is stated with the limit it stops at; the limits are policy commitments; no ordering claim; the media counts and shapes per study (C, A, B, A, A) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S03-001` | Universal / Safe | 001 Paper & Indigo | 3 with 4 — bordered grid with a band | ghost serif section sign behind the head | Head split with the pencil rule and the italic *keepable*; three bands by two cells sharing hairlines, the middle band on the tinted paper (V1's accent fill), each cell a serif title, its line and the limit red-edged (`--no`) with a struck-circle mark; ruled foot with the closing line and one action | none, by V1's reasoning | 144 |
| `CONS-S03-002` | Premium / Editorial | 002 Sable & Bronze | 2 — head split | pencil ellipse round *stop* | Serif display and the serif italic standfirst at the baseline; six horizontal items on two ruled columns, a 1:1 field a third wide, serif title, the limit in the accent's italic; underlined route | 6 × 1:1 | 110 |
| `CONS-S03-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — bordered grid with a field column | ruled margin behind the grid | A full-height field as the grid's first column; six cells with a stroke mark each (calculator / speech / person / balance / compass / two people) in place of any numbering, the limit red-edged; band-tone foot cell with V1's question and the action | 1 × column | 136 |
| `CONS-S03-004` | Conversion-led | 004 White & Signal | 4 with 5 — plate crossing the field edge | underline stroke under *red line* in the accent, and under every limit in `--no` | 21:9 field with a band-tone claim plate crossing its lower edge, the pencil rule and the one action HOLD US TO ONE; bordered 3×2 grid of items with small 1:1 fields; V1's red line literally drawn under each limit | 1 × 21:9 + 6 × 1:1 | 158 |
| `CONS-S03-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 as a set — type crossing the field edge | bracket grouping the head column | Six tall 3:4 fields on three columns, each with a paper plate on a hairline crossing its lower edge carrying the serif title and the limit in the accent's italic; the head in a narrow column with the italic *not* and the action. V1's near-black ground becomes chalk | 6 × 3:4 | 101 |

## What changed from V1

The limit — V1's whole argument — is now drawn the same way across the batch: a deep-red (`--no`) edge, mark or underline, never a chip. Cards, pills and the saturated 001 band become hairline cells and the band tone; the dark 005 ground is gone. Copy is V1's throughout, including the shorter limit wording V1 used in `003`; word counts equal V1's. Slates read `IN USE` — the capability being done by the people doing it — and `AT WORK · 21:9` on the wide field.

## Verification

- `cslcheck.ps1 -Sec S03 -Fields '<six capability names>|We do not set your prices'` — ALL CHECKS PASS; parity 35/35. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit; no claims vocabulary. The checker's claims list was word-bounded (`" rated "`) after "illustrated" in V1's slate tripped it.
- Rendered and read at 1440. Corrections: `001` ghost glyph selector specificity against the head's paragraph rule; `005` plate rule reduced from the accent to a hairline so the composition keeps one accent bar.
