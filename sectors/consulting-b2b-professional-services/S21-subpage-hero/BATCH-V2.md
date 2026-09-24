# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the page title as the one `<h1>`; the three checkable facts; nothing that is a claim about the firm; one permitted action and it is the way out, never *book a call*; media contained at internal-page scale, never a stage; engagement length, the ninety days and the sibling page name as placeholder demo values; the media counts per study (1, 0, 1, 0, 0) — are kept exactly. The README test still holds: none of the five would work as S01.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S21-001` | Universal / Safe | 001 Paper & Indigo | 1 at internal-page scale | ghost `§` behind the title | Title as h1 with the brief, three labelled facts on a ruled list with the pencil rule over the first; the partner as a contained 4:5 field on the right; foot line with the way out as an underlined link | 1 × 4:5 · 3 | 86 |
| `CONS-S21-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one column | pencil ellipse round *redesign* | Title at display size with the brief beside; the three facts as plain ruled lines, tracked label and serif fact; closing line with the way out. No field | none · 3 | 68 |
| `CONS-S21-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a strip | ruled margin behind | Title left with two facts as bordered cells beside; the two people at work as a contained 3:1 strip beneath the title on the pencil rule, the placeholder length as a bordered chip on its top edge; foot line with the way out | 1 × 3:1 · 3 | 81 |
| `CONS-S21-004` | Conversion-led | 004 White & Signal | 4 — identity and the way out at the same level | underline stroke under *Wrong page?* | Title and brief left; the way out as a band with the pencil rule on the right, the one link as a bordered rectangle with an arrow mark; three facts as a bordered row | none · 3 | 73 |
| `CONS-S21-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — two display lines | bracket grouping the pair | The page as h1 and the disqualifier in the accent italic at the same size, bracketed; brief; ruled row of three facts; closing line under the pencil rule with the way out | none · 3 | 77 |

## What changed from V1

The way out is one device across the batch — a `--no` mark, then the sibling page as an underlined link with the ↗ glyph, or in 004 as the bordered rectangle — and the three facts read as the same tracked label plus fact everywhere. Fields are contained and labelled at page scale; nothing sits behind the title. Cards and filled bands go. Copy is V1's throughout; the three placeholders keep their marking.

## Verification

- `cslcheck.ps1 -Sec S21 -Fields 'Operating model redesign|why it has not happened|COO|weeks, named in the first hour|Not the rest|Strategy under uncertainty|Wrong page'` — ALL CHECKS PASS on every rule; parity 34/35, the one absence V1's own (`003` carries the length as a chip without *named in the first hour*). One `<h1>` per study, as the section requires; three placeholders each, declared. No header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no book-a-call.
- Rendered and read at 1440. One correction: the 003 strip changed from a height-capped 21:9 to a full-width 3:1 so the field spans the column; the chip moved outside the `role="img"` field so its placeholder text is not hidden from assistive technology.
