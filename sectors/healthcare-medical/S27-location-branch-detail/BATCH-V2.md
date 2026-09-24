# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S27` — Clinic / Department Location Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The brief forbids fabricated addresses, coordinates, telephone numbers, opening hours, maps and directions, and the sector contract forbids the same. A location page under those rules is **a page of reserved fields**, and the design makes the reservation deliberate rather than apologetic.

Nine reserved values: the location name (as the label and again as the `<h1>`), the street, the step-free access note, the parking note, the public-transport note, the telephone with the hours it is answered, the written route, and the opening context.

What is written is what stays true of the building **whatever its address turns out to be**:

- **When you arrive** — one: the door is on the street named above. two: the desk is the first thing inside it. three: say the name you booked under. Nothing else is needed.
- **When it is open** — the value is reserved, and under it: *An hour that has not been checked this month is not printed.*
- **Why there is no map** — *An embedded map is a third party watching you plan a visit, and a drawn one goes out of date the week a door moves. The street is written above.* This is the one page in the sector where the refusal has to be explained rather than stated, because the absence of a map is the thing a visitor will notice.
- **What happens here** — the first appointment, the look, and the letter, with the areas index named. **Who is based here** — the people and the area. And last: *If it cannot wait, do not come here first.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S27-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the page read as a journey | column rules behind the head | 2 reserved · 11 | 220 |
| `HC-S27-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the door as a panorama, the fields at full measure | open bracket at the head | 1 reserved · 10 | 214 |
| `HC-S27-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the location as one plate | bordered plate, 1px lines shared | 2 reserved · 11 | 220 |
| `HC-S27-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the reserved name, measured | measure rule under the name's second half | 1 reserved · 10 | 214 |
| `HC-S27-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the location framed and left empty | corner frame at the head | none · 9 | 208 |

All five sit inside the contract's detail band of 170–230.

**005 is the `C`**, and it records why: every value that locates this place is reserved, so a photograph of a door would be the only certain thing on the page and would carry more weight than it has earned.

## What was designed

This is the one page in S21–S27 where reserved media is genuinely earned, and there are only two honest subjects for it: **the street door from the pavement** and **the reception desk in use** — the two things a visitor actually has to find. 001 and 003 carry both, 002 runs the door alone at 21:9, 004 sets it at 4:3 beside the fields, 005 carries neither.

The reserved fields are designed as a **register, not a contact card**: bare labelled rows on hairlines with a fixed `10rem` label column, no icons, no `tel:` link, no pin, no coordinates, nothing that could be dialled or opened. In 003 the label sits above its value in the narrow plate cells rather than beside it, which is the same field rendered for a narrower measure.

*Getting here* takes the one 3px accent lead rule in 001 and 002 — the street is the reason the page exists — while 005 gives it to the map refusal and 003 and 004 to the foot. The graphite `--no` tone carries three sentences on every study: the unchecked hour, the missing map, and *do not come here first*.

No SVG, no icon, no badge, no map of any kind, no embedded service, no global header or footer.

## Verification

- `hccheck.ps1 -Sec S27 -Fields 'Getting here|Reaching it|When it is open|When you arrive|Why there is no map|What happens here|Who is based here'` — ALL CHECKS PASS; parity 35/35. `<h1>` present and single (detail page); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image, map embed or remote reference**; no `tel:` or `mailto:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no claim term; no digit in visible copy outside the field ratio labels; nine to eleven placeholders per study, declared in the `placeholder-data` meta. All links point at same-variant S02, S03, S23, S18 and S05 studies and resolve on disk.
- Rendered and read at 1440.
