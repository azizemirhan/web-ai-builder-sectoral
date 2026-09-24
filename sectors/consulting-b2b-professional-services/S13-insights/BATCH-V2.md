# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S13` — Insights · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — each piece carries the claim it makes and whether the firm still believes it; three statuses; nothing taken down; media only ever the piece's own opening spread, never a bought photograph; titles as placeholder demo values; no author, byline, date, reading time, category, view count or share row; the media counts per study (0, 1, 5, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S13-001` | Universal / Safe | 001 Paper & Indigo | 1's ruled list | ghost serif pilcrow behind the head | Four pieces on two ruled columns — serif placeholder title, the claim, the status as a marked chip (tick in a circle / half mark); the withdrawn claim as a band on the tinted paper behind a `--no` rule with a struck-seal mark; V1's foot line on a hairline | none · 5 | 179 |
| `CONS-S13-002` | Premium / Editorial | 002 Sable & Bronze | 2 with one wide field | pencil ellipse round *wrong* | The lead piece as a 21:9 field of its own opening spread with title, claim and status; four ruled claims on two columns, the withdrawn status in `--no`; foot line | 1 × 21:9 · 5 | 196 |
| `CONS-S13-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with 8 — bordered grid, mixed ratios | ruled margin behind | V1's tally as a mast line between hairlines; five pieces in a bordered three-track grid — the lead across two with a 3:2 field, four with 4:3 — each its own opening spread, serif title, claim and status chip; band-tone foot cell | 1 × 3:2 + 4 × 4:3 · 5 | 194 |
| `CONS-S13-004` | Conversion-led | 004 White & Signal | 4 with 3 — scanning row | underline stroke under *wrong* | Five claims as one bordered row, the claim in the serif first and the placeholder title small beneath; the withdrawn cell on the band tone behind a red rule (V1's fill); band with V1's ask and the one action ARGUE WITH ONE | none · 5 | 179 |
| `CONS-S13-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5's inversion — the withdrawn piece largest | bracket grouping the head | The withdrawn piece with its 3:2 opening-spread field, WE WERE WRONG in `--no`, the title at display scale crossing the field's edge and the correction; four held pieces on hairlines; foot line. The near-black ground becomes chalk | 1 × 3:2 · 5 | 174 |

## What changed from V1

The three statuses are one system across the batch — tick in a circle (accent), half mark (muted), struck seal (`--no`) — as chips, labels or edges; the withdrawn piece carries the deep-red rule wherever it is given room. Cards, the stock-image slot and the dark 005 ground go; every field is the piece's own opening spread. Titles keep V1's placeholder marking. Copy is V1's throughout.

## Verification

- `cslcheck.ps1 -Sec S13 -Fields 'Still holds|Partly wrong|We were wrong|Nothing is taken down|Central delivery becomes a queue'` — ALL CHECKS PASS on every rule; parity 24/25, the one absence V1's own (`004` carries no foot line). Five placeholders per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit; no author, date or category.
- Rendered and read at 1440. No corrections needed.
