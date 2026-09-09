# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S21`
- Section Name: `Subpage Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S21-001` | Universal / Safe | AUTHORED | `raw/WELL-S21-001.html` |
| `WELL-S21-002` | Premium / Editorial | AUTHORED | `raw/WELL-S21-002.html` |
| `WELL-S21-003` | Dense / Information-heavy | AUTHORED | `raw/WELL-S21-003.html` |
| `WELL-S21-004` | Conversion-led | AUTHORED | `raw/WELL-S21-004.html` |
| `WELL-S21-005` | Sector-native / Distinctive | AUTHORED | `raw/WELL-S21-005.html` |

**This is the first batch in the extended architecture set (`S21`–`S27`), and its directions differ
from `S01`–`S20`:** *Dense / Information-heavy* replaces Structured / Visual Modular, and
*Sector-native / Distinctive* replaces Art-directed / Distinctive. The territory `<meta>` of every
study is checked against that set rather than the core one.

The section's role, its governing constraint and its boundary with `S01` and `S22` are in
`./README.md`, which now carries the sector's reading alongside the canonical scaffold text.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — It Must Fail As An S01

The section scaffold states the test, and it is the sharpest one in the extended set:

> A study that would work unchanged as `S01` has not answered this role.

Every study is authored to fail as a homepage hero, in ways that can be checked rather than
asserted:

| Discipline | How it is enforced | How it is verified |
| --- | --- | --- |
| Height | An interior hero that fills the screen buries the content the visitor came for | **No viewport-height unit in any file**, scanned |
| Voice | It orients rather than persuades | Scan for *welcome to*, *leading*, *award*, *best in*, *years of* — zero |
| Actions | At most one, tied to this page | **Link count ≤ 1 per study**, scanned; only `004` has one |
| Subject | The title names where you are | Titles are page names: `Facials`, `How we work`, `Deep cleansing facial`, `Hands & feet` |

**No breadcrumb anywhere.** `S21` names the page; `S22` shows the path to it. A parent **label**
appears as a word, never a link — naming the category a page belongs to is page identity, while
linking up the hierarchy is the next section's job. Scanned for *home*, *back to*, `›`, `»` and
*you are here*: zero matches.

## What Is Real, And What The Sector Filters Out

The canonical scope for this role allows *"category, date, reading time, discipline or reference"*.
Read through this sector's own rules:

| Metadata | Treatment | Rule it comes from |
| --- | --- | --- |
| Category / parent label | **Real** | `S03` vocabulary |
| Page title | **Real** where it is a page type or category | — |
| Article title and standfirst | **Reserved areas** | `S18` |
| Publication date | **Reserved field** | `S18` |
| Author | **Reserved field** | `S04` |
| Reading time | **Omitted** | `S18`, and this sector prints no durations |
| Item counts, prices, ratings | **Omitted** | `S11`, `S10` |

**Not present in any study:** an invented item count, price, duration, reading time, rating, review
count, practitioner name, telephone number or address; a breadcrumb, trail, parent link or *back to*
link; a form field; a second action; a viewport-height unit. Verified by scan — **no digit appears
in visible copy anywhere in the batch.**

## Study Records

### WELL-S21-001 — Universal / Safe

- **Layout model:** Parent label, page title and one framing line held left, above a wide reserved
  media band, closed by a line saying what is further down the page.
- **The band is short on purpose**, and held to a fixed height at desktop widths rather than an
  aspect ratio, so the whole section stays around six hundred pixels at 1440.
- **Correction made, recorded:** the band was first authored at 16:5, which rendered 380px tall and
  pushed the section close to a full viewport — the exact failure the batch is meant to avoid.
  Capping it with `max-height` shrank its width too (an `aspect-ratio` box obeys both), so the band
  stopped aligning with the section margin. A fixed `height` at desktop with aspect ratios only at
  the narrow breakpoints fixed both. **Worth recording: `aspect-ratio` plus `max-height` silently
  narrows a block.**
- **Responsive strategy:** the band relaxes to 16:7 at 768px and 3:2 at 480px — it changes shape
  before the title changes anything.

### WELL-S21-002 — Premium / Editorial

- **Layout model:** Parent label, serif title, one standfirst, a hairline. Nothing else.
- **The variant the scaffold asks for:** *"the study set should include at least one variant that
  works without an image"*. This is it, and on a page whose body is mostly reading, a picture in the
  hero would be decoration standing in front of the content.
- **The editorial reading — an interior hero is a chapter heading, not a cover.** Set as one, it
  takes the least page that still reads as an opening and hands over immediately. Shallowest study
  in the batch.

### WELL-S21-003 — Dense / Information-heavy

- **Layout model:** An article page hero — parent label, a reserved title area, a reserved standfirst
  area, and a four-item metadata rail.
- **The batch's most interesting result: the densest study is the one whose largest element is
  empty.** This is the hero of an `S25` article page, and an article title is invented content on
  the `S18` rule — so density had to come from the metadata rather than from the headline. The
  result is honest rather than awkward, and it shows exactly how much room a real headline will get.
- **The metadata is the canonical list, filtered:** topic and kind real, date and author reserved
  fields, **reading time omitted entirely**.
- **Correction made, recorded:** the metadata rail first ran the full 1136px while the reserved
  areas above were held to 30–42rem, which left the four items floating far apart. Capped at 62rem
  so the rail sits under the block it belongs to.
- **Responsive strategy:** the rail wraps 4 → 2 → 1 rather than truncating, as the scaffold requires.

### WELL-S21-004 — Conversion-led

- **Layout model:** A treatment page hero on a dark ground with the page identity left and a single
  action right, bottom-aligned to the text.
- **Exactly one action.** The scaffold rules out *multiple competing calls to action*, and the
  discipline matters most here, where two buttons are the obvious move. The action books **this
  page's treatment**, not the studio.
- **The honest line:** *"The same button is at the foot of the page. This one is for anyone who
  arrived already knowing."* An interior hero that pretends its button is the only one is arguing
  with its own page; saying what the duplicate is for costs a line and settles it.
- **Responsive strategy:** the action moves below the title at 860px and goes full width — the title
  stays the first thing read at every width.

### WELL-S21-005 — Sector-native / Distinctive

- **Layout model:** A soft mauve field with the page identity at the left and a short reserved media
  band offset to the right, pulled up so it **rises alongside the title** rather than sitting under
  it.
- **Why this is sector-native rather than art-directed:** the extended set asks for a variant
  distinctive to *this sector*. In beauty and wellness an interior page is usually reached from a
  busy index, and the job of its opening is to **lower the temperature** — so the study is wide, low,
  soft in tone, and interlocks type with image instead of stacking them.
- **Correction made, recorded — and it is the batch's most transferable lesson.** The first build
  tried to run the **title** over the panel. A page name is two or three words, so it never reached
  the panel and left a dead gap where the overlap should have been. Rebuilt as a **vertical**
  interlock — the band offset right and pulled up — which works whatever the title happens to say.
  *An overlap that depends on the length of unwritten content is not a layout, it is a hope.*
- **Deliberately not rotated:** `S17-005` remains the sector's only rotated study.
- **Responsive strategy:** the interlock unwinds at 860px into a plain stack — the composition gives
  way before the content does.

## Structural Diversity

| Study | Page type it opens | Title | Media | Actions | Ground |
| --- | --- | --- | --- | --- | --- |
| 001 | A category page | Real | Wide short band | 0 | Pale ice `#eef1f3` |
| 002 | A studio page | Real, serif | None | 0 | Warm parchment `#f7f2ec` |
| 003 | An article page | **Reserved** | None | 0 | Pale sage `#e9ece6` |
| 004 | A treatment page | Real | None | **1** | Deep slate `#1d2a33` |
| 005 | A category page | Real | Short interlocked band | 0 | Soft mauve `#d8cdd2` |

Five different interior page types, so the set answers the role rather than restyling one page.
Grounds do not repeat any used in `WELL-S01`–`S20`; verified by scan across all 105 studies.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is how
  an opening behaves when it must not behave like a homepage — band beneath, type alone, metadata
  rail, single action, or type and image interlocked.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>`, no `<iframe>`,
  no form element, no inline `style` attribute.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| A treatment room | `001` — wide band beneath the identity | Still image, shallow band | Empty tonal surface with a quiet label |
| Hands at rest | `005` — short band interlocked beside the title | Still image, 16:7 | As above |
| Article title | `003` — reserved area at title scale | **Text** | Sized area stating how many lines it holds |
| Standfirst | `003` — reserved area | **Text** | As above |
| Publication date, author | `003` — reserved fields | **Text** | Em dash with a visually hidden field label |

Two of five studies carry media, and both hold it to a band. **No study reserves a full-bleed area** —
that shape belongs to `S01`.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- **Territory validation: PASS.** Each study's `territory` matches the extended-architecture set,
  not the `S01`–`S20` set. New check, added for this batch.
- Accessibility QA: **PASS.** Exactly one `<h1>` per study — in `003` it is visually hidden, because
  the visible title is a reserved area and a page still needs a heading. `aria-labelledby`,
  `prefers-reduced-motion`, and 52px on the one action.
- Responsive QA: **PASS.** Verified at 1440px and 720px. In every study the media or the composition
  gives way before the title does, as the scaffold requires.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` with the
  wrong arity.
- Section-shell check: **PASS.**
- Visible-copy check: **PASS.**
- Scoped-CSS check: **PASS.**
- **The S01 test, as three scans: PASS.** No viewport-height unit in any file; no study has more
  than one link; no homepage-hero vocabulary.
- **No-breadcrumb check: PASS.** No *home*, *back to*, `›`, `»` or *you are here* in any study.
- **Figure and duration check: PASS.** No digit in visible copy; no *minutes*, *hours*, *read*,
  price, percentage, rating or count.
- Render check: **PASS, after three corrections.** All five rendered in headless Chrome and
  inspected: `001`'s band was flattened and its sizing method changed, `003`'s metadata rail was
  capped, and `005`'s overlap was rebuilt from horizontal to vertical. All recorded above.

## Notes

- This is the twenty-first authored batch in the `WELL` sector, the nineteenth authored entirely
  without references, and **the first of the seven extended architecture roles.**
- **The reusable outcome is that an interior hero is defined by restraint in three dimensions at
  once — height, voice and action count — and all three can be checked mechanically.** No viewport
  units, at most one link, no homepage vocabulary. Any sector can take those three scans unchanged;
  they are what stops `S21` from quietly becoming a second `S01`.
- The second outcome is narrower but sharper: **a composition that depends on the length of
  unwritten content is not a layout.** `005` failed the first time because a page title is short.
  Interlocking on the axis that does not depend on the content is what made it work, and the same
  reasoning applies to any overlap, cut-out or wrap in a placeholder catalog.
- `S22` is next, and this batch has already fixed its boundary: everything trail-shaped was kept out
  of `S21` deliberately, so `S22` inherits a clean role rather than a contested one.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a Windows Store placeholder
  rather than an interpreter.
