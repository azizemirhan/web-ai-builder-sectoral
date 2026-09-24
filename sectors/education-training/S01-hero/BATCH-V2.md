# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one `<h1>`, the shared lead, one primary route to the same-variant S02, no institution or outcome claim, reserved learning spaces only; the media counts per study (2, 1, 3, 0, 2) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S01-001` | Universal / Safe | 001 Apricot | 1 — the split headline beside an offset pair | loop behind the h1 | *Your next chapter starts here.* with the lead and the action on the lead rule; the shared table at 4:3 with the studio as an offset 1:1 and *Ideas begin with a question.* beneath | 4:3 + 1:1 · 0 | 70 |
| `EDU-S01-002` | Premium / Editorial | 002 Mulberry | 2 — the editorial headline beside a tall studio | rise in the corner above the h1 | *Stay curious. Go further.* at the largest measure; the studio at 4:5 captioned *An interest today. A possibility tomorrow.* | 1 × 4:5 · 0 | 56 |
| `EDU-S01-003` | Structured / Visual Modular | 003 Cobalt | 3 — the broad opening above unequal fields | cross grid behind | *Make space for what's next.* split with the lead; the action and its line on the lead rule; three learning spaces as one seamed plate — 3:2 wide, two 4:5 | 3:2 + 2 × 4:5 · 0 | 79 |
| `EDU-S01-004` | Conversion-led | 004 Iris | 4 — the question with the exploration field as a band | outline round *to learn?* | *What would you like to learn?*; a band with *Start with an interest. See where it could lead.*, the action and its line, and V1's three sentences as word-numeral chips. No field | none · 0 | 75 |
| `EDU-S01-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — oversized type above staggered windows | margin bar along the display column | *A little curiosity. A new direction.* at seven rem on the vertical lead rule; the lead and action offset right; the studio at 3:2 and the shared table at 4:3 staggered | 3:2 + 4:3 · 0 | 62 |

## What changed from V1

V1's 24–30px blobs, arched images, pill captions and filled accent buttons go: fields are bare, flat, 8px-cornered and labelled by what they are; the one action is a 1px ink rectangle with the arrow mark; the accent lands on one phrase of the headline and on the lead rule. Afterhours is inverted to a pale sage paper with the lime darkened to olive. No compass-rose crest, no mortarboard — the eyebrow mark is a plain compass stroke. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S01 -Fields 'Follow an interest|where you want it to take you|Explore programmes'` — ALL CHECKS PASS; parity 15/15. One `<h1>` per study; no header/nav/footer; no form; one link per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term.
- Rendered and read at 1440. One correction: the 002 rise was first drawn across the headline and read as a strike — it now sits in the corner above the h1, beside the eyebrow.
