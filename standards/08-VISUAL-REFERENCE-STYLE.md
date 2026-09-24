# Visual Reference Style — derived from the Architecture KEEP set

Status: ACTIVE. Applies to every sector's detailing pass, starting with `WELL`.
Source of truth: the 72 `ARC` studies marked **KEEP** in
`../sectors/architecture-interior-design/ARCHITECTURE-REWORK-EXECUTION-PLAN.md` (user-confirmed
`S02-001…005`, and the KEEP rows of S03–S27). The studies marked REWORK / REBUILD there are the
counter-examples: technical-document metaphors, text walls, dark rounded panels.

This document records *how* those studies achieve "detailed, modern, sector-specific" so the same
craft can be translated — not copied — into other sectors. It is additive to
`01-AUTHORING-STANDARD.md` and `03-MEDIA-POLICY.md`; where they conflict, the global standard
governs.

---

## 1. The register in one sentence

**A premium editorial publication: large bare image fields, a serif display voice, hairline
rules, one earth accent, and almost no boxes.** The page is composed like a magazine spread,
not assembled from UI components.

Reference studies to open first: `ARC-S02-001` (asymmetric mosaic), `ARC-S03-002` (narrow
editorial column + card row + tinted band), `ARC-S07-002` (display type overlapping media),
`ARC-S11-001` (six samples with two-field captions), `ARC-S12-002` (quotation panel with
pager), `ARC-S18-001` (figures in a ruled grid), `ARC-S20-002` (ruled sheet with a giant index
numeral), `ARC-S24-002` (long-form detail page paced by chapters).

## 2. Media fields

- **Bare, flat, large.** A media area is a single flat tone (paper darkened by ~6–10%), no
  dashed border, no inner icon, no "Image area" centred in a badge. Corner radius 0–3px in the
  editorial register; a sector may allow a soft radius (see §9) but never a pill or a 24px+
  blob on a small tile.
- **Label pinned to a corner.** One tiny uppercase tracked label (0.55–0.65rem, 0.14–0.2em)
  sits bottom-left *inside* the field: `IMAGE AREA`, `PORTRAIT AREA`, `SAMPLE AREA`,
  `IMAGE AREA · 3:4`. It reads as a photographer's slate, not a form placeholder.
- **Deliberate ratios, mixed for rhythm.** 4:5 portrait for people and samples; 4:3 and 16:10
  for rooms; 21:9 for a long view; 1:1 for detail. A mosaic mixes a lead field spanning two rows
  with smaller ones (`S02-001`, `S14-001`). Ratios change per breakpoint.
- **Media carries meaning.** Where a caption could be a paragraph, it is a title plus a tiny
  meta line under the field. The field *is* the content; the words are the slate.
- **The field may be overlapped by type** (`S07-002`: a display word sits across the top edge
  of the image) — once per page, as the art-directed device.

## 3. Typography

| Role | Face | Size | Weight | Leading / tracking |
| --- | --- | --- | --- | --- |
| Display (h1/h2 of the section) | Serif (Georgia stack) | `clamp(2.6rem, 5vw, 6rem)` | 400 | 0.85–1.0 / −0.045 to −0.02em |
| Display, alternative | Sans, uppercase | `clamp(3rem, 6vw, 6.5rem)` | 500 | 0.83 / −0.065em |
| Statement (a philosophy line) | Serif | `clamp(1.4rem, 2.4vw, 2.2rem)` | 400 | 1.2 |
| Item title | Serif or sans | 1.0–1.45rem | 400 / 600 | tight |
| Eyebrow / label | Sans | 0.58–0.7rem | 700 | uppercase, 0.13–0.2em |
| Body | Sans | 0.8–0.95rem | 400 | 1.55–1.65, measure 28–34rem, muted colour |
| Index numeral | Serif, accent colour | `clamp(4rem, 10vw, 10rem)` | 400 | 0.7 |

- **One italic word** inside a serif heading is the emphasis device (`space.`, `specific`),
  never bold inside a heading.
- **Display copy is short**: a heading of two to five words, a lead of one or two sentences.
  Nothing else in the head.
- The sans is the system stack; the serif is Georgia / Times / Iowan Old Style. No web fonts.

## 4. Layout

- **Asymmetric editorial grid.** The default is a narrow intro column (`0.55–0.7fr`, max ~18rem
  of copy) and a wide media grid (`2–2.4fr`). The head can also split: heading left, lead
  right-aligned at the baseline (`S02-002`, `S18-001`).
- **Rules do the structuring.** 1px lines in ink (strong) or `--line` (soft): a top rule on the
  shell, a rule under the head, rules between rows and list items, a bordered grid where the
  cells share lines (`S02-002`, `S18-001`, `S20-002`). Lines replace card backgrounds.
- **Bands, not cards.** A second beat of the section is a full-width band with a tinted paper
  (`--band`, ~5% darker/warmer) holding a statement, an image and a short ruled list
  (`S03-002`). Never a stack of white cards with shadows.
- **Wide frame, deep insets.** `max-width` 1360–1600px (`min(100%, 92–100rem)`), section
  padding `clamp(2rem, 5–6vw, 6rem)`, inline padding `clamp(1rem, 4–5vw, 5rem)`.
- **Whitespace is a material.** Space between the head and the grid, and around a statement,
  is at least one display-line height. A study that fills its frame edge to edge with content
  has failed the register.
- **One page = one composition.** A section is one or two beats, not four. If a third beat is
  needed the section is probably two sections.

## 5. Colour

- **Paper**: warm off-whites — `#f3efe8`, `#f5f5f2`, `#fdfdfc`, `#ece8df`. One per study.
- **Ink**: near-black with a warm or green cast — `#20201d`, `#111310`, `#1b1a17`. Never pure
  `#000` on paper; never a pure white surface floating on paper.
- **Muted**: `#5f5c54`–`#6d6a63` for body and meta.
- **Line**: `#c7bfb2`–`#ddd8ce`; strong line = ink.
- **Media tone**: paper darkened — `#dedbd3`, `#e0dcd4`, `#e1e2dd`.
- **One accent, used small**: terracotta `#9a5c3d` / `#94422f`, forest `#1f4d3a`, olive.
  It appears on eyebrows, the index numeral, arrows, hover states and one italic word — **never
  as a filled panel, never on a large button**. A dark filled panel is the sector-free
  "SaaS" look this register exists to avoid.

## 6. Actions and links

- Primary action: **thin-bordered rectangle** (1px ink), uppercase 0.65–0.72rem tracked,
  `min-height: 44–52px`, hover inverts to ink fill. Or an **underlined text link** with a
  trailing `↗` / `→` in accent. Or a **circular bordered arrow** (2.8rem) at the end of a
  caption.
- Never: pill buttons with heavy fills, gradient buttons, two competing filled buttons, "Read
  more" under every card.
- One action per composition; a second is a text link.

## 7. Density

- Head: heading + lead ≤ 40 words.
- Per item: title + one meta line (≤ 8 words) or one sentence (≤ 20 words).
- A section's visible copy should sit in the **low band (60–120 words)** for grids and galleries,
  **standard (90–170)** for statements and lists, and only detail pages (S23–S27) go higher —
  paced by chapters, pull-quotes and media, never by continuous prose.
- Labelled two-field captions (`USED FOR` / `WHAT WE ASK OF IT`, `S11-001`) are how the
  structured direction carries information: visible micro-labels, not paragraphs.

## 8. Rhythm devices (the vocabulary)

1. Narrow intro column + wide grid (`S02-001`, `S03-001`, `S03-002`).
2. Head split with right-aligned lead at baseline (`S02-002`, `S18-001`).
3. Bordered cell grid — cells share 1px lines (`S02-002`, `S18-001`).
4. Tinted band with statement + image + ruled list (`S03-002`).
5. Display word overlapping the image edge (`S07-002`).
6. Ruled sheet: top and bottom ink rules, a mast line of tiny labels, a giant accent index
   numeral (`S20-002`).
7. Quotation panel: portrait left, quote in a pale panel, pager `01 / 05` with arrow buttons
   (`S12-002`).
8. Gallery of mixed ratios with slate captions (`S14-001`).
9. Chapter pacing on a long page: eyebrow `CHAPTER 01 · INHERIT`, serif chapter title,
   pull-sentence with one accent phrase, image pair (`S24-002`).
10. Portrait with a colour tab behind it, offset (`S08-001`).

## 9. Per-sector translation rules

The register is shared; the *subject* and the *temperature* are the sector's own:

- Keep: §2–§8 as written.
- Change per sector: paper temperature, the one accent, the serif's role (display vs. statement),
  corner radius (0–3px architecture; a sector may allow up to ~8px on large fields where softness
  is its language), media subjects (rooms, people at work, materials/tools the text names), and
  the vocabulary of labels.
- Never import: architecture words, plan/section motifs, the terracotta itself as a "house" colour.
- Every sector keeps its own claims and evidence rules; the register does not license new
  claims.

## 10. What the register is not

- Not dark rounded panels with white text; not white cards with 20–28px radii and shadows.
- Not pill tags on every card; not icon rows; not stat tiles in coloured boxes.
- Not dashed "reserved" boxes with explanatory sentences inside them.
- Not three bold weights in one caption; not "Read more →" as a component.
- Not a technical document (sheet, register, matrix, protocol, dossier) — see the ARC
  anti-pattern list.
- Not text-dependent: if removing half the copy breaks the study, it is not in the register.

## 11. Checklist for a re-authored study

1. One paper, one ink, one muted, one line, one accent — accent used on ≤ 3 small elements.
2. Media fields flat, bare, slate label bottom-left, ratios deliberate, mixed for rhythm.
3. Display type serif at ≥ 2.6rem with tight leading, or tracked uppercase sans; one italic word.
4. Structure by rules and bands, not by cards.
5. Copy inside the sector's low/standard band; head ≤ 40 words.
6. One action, thin-bordered or underlined; no heavy fills.
7. Responsive ladder 1280 / 1024 / 768 / 480 / 360; ratios and columns step down; nothing
   overflows at 320.
8. No global header, nav or footer; hero only for S01.
9. Sector claims rules intact; reserved areas remain empty.
10. Rendered at 1440 and 390 and read before it is recorded.
