# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S09`
- Section Name: `Technology Products`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S09-001` | Universal / Safe | AUTHORED | `raw/WELL-S09-001.html` |
| `WELL-S09-002` | Premium / Editorial | AUTHORED | `raw/WELL-S09-002.html` |
| `WELL-S09-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S09-003.html` |
| `WELL-S09-004` | Conversion-led | AUTHORED | `raw/WELL-S09-004.html` |
| `WELL-S09-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S09-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S02`, `S08` and `S11` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — And The Distinction That Resolves It

This role is about named things, and named things in this sector are **brands**. A real page here
carries device names, product ranges and partner marks. A placeholder carries none:
`03-MEDIA-POLICY.md` forbids inventing products, logos and brands outright, and
`../WELLNESS-DESIGN-DIRECTION.md` forbids the device-specification blocks and ingredient tables
this role most naturally reaches for.

| Layer | Example | Status |
| --- | --- | --- |
| **Brand** | A device name, product range, manufacturer, partner mark | **Reserved**, never invented |
| **Function** | "A steamer", "hand tools", "warm stones", "cleansers", "oils" | **Allowed** — generic objects and categories |
| **Policy** | "Sterilised between every guest", "chosen in the room", "any label can be read" | **Allowed, and it is the real content** |

**Function and policy lead; brand is reserved.** This is the same resolution as `S04`, where the
role led and the name was reserved, and it produces the better section for the same reason: a
visitor learns more from *sterilised between every guest* than from a logo they do not recognise.

**Marks are reserved, not omitted.** All five studies carry a row of empty partner-mark slots —
five, four, four, five and four respectively — so the structure a real page needs is demonstrated
without inventing the brands that would fill it. These are reserved media areas, exactly like the
portrait slots in `S04`.

**Not present in any study:** an invented device name, product name, range, manufacturer,
ingredient, patent or partner mark; a certification, approval or compliance mark; *medical grade*,
*clinically tested*, *professional only*, *latest technology*, *state of the art*, *advanced* or
*exclusive*; an efficacy claim about any device or product; a specification block, ingredient table
or datasheet; a price, percentage or award.

## The Equipment And Product Set

| Equipment | Stated as |
| --- | --- |
| The couch | Heated, and set to your height before anything starts |
| The steamer | Used before cleansing, at a temperature you agree to |
| Hand tools | Cleaned and sterilised between every guest, without exception |
| Warm stones | Heated in water and tested on our own wrist first |

| Products | Stated as |
| --- | --- |
| Cleansers · Oils · Masks · Exfoliants | Chosen in the room for the skin in front of us; any label can be read on request |

Every product line describes **how the thing is chosen**, never what it does to skin. That is the
`S02` procedural rule applied to objects rather than to actions.

## Study Records

### WELL-S09-001 — Universal / Safe

- **Structural intent / archetype:** The two halves of the role in their most legible arrangement.
- **Layout model:** A split header above a four-column grid of media-topped equipment cards, closed
  by a labelled row of five reserved mark slots and one line covering the products.
- **Media relationship:** Four object-scale areas plus five small mark slots — the highest media
  count in the batch, which is correct for the study whose job is to show both halves plainly.
- **Responsive strategy:** Cards 4 → 2 → 1; the mark row 5 → 3 → 2, so a mark slot never becomes a
  sliver.
- **Visual-first check:** 119 visible words.

### WELL-S09-002 — Premium / Editorial

- **Structural intent / archetype:** Still life. Three product categories at plate scale rather
  than every category at list scale.
- **Layout model:** A serif header and lead, a triptych of three tall 4:5 plates with serif names
  beneath, and a hairline closing row pairing the equipment line with a compact four-slot mark row.
- **The naming point:** the plate names are **product categories, not products**. A category is a
  generic noun; a product is a brand. This is the study where that line matters most, because the
  editorial register wants a named object under a beautiful photograph.
- **Direction-specific risk, recorded:** the editorial caption wants to describe what a product
  does to skin — exactly the claim the role may not make. The lines stay on how the thing is chosen.
- **Responsive strategy:** The triptych goes to one column at 768px with plates becoming 16:10, and
  the closing row unstacks to a single column.
- **Visual-first check:** 124 visible words.

### WELL-S09-003 — Structured / Visual Modular

- **Structural intent / archetype:** The role's three subjects held side by side.
- **Layout model:** Three labelled columns — *In the room*, *On your skin*, *Ranges we carry* —
  each with a **different item anatomy**: equipment items pair a thumbnail with a policy line
  inside a card, product items are plain ruled rows with no media, and the ranges are stacked
  reserved slots.
- **How it avoids the anti-pattern, recorded:** three columns of listed items is one step from a
  specification table, which the sector direction rules out. What keeps it modular is that the
  columns share **no row grid and no common item shape**, so nothing aligns across them — because
  nothing compares across them. The header says so in the visible copy, which is a design
  statement rather than an authoring note.
- **Content-capacity justification:** the capacity is the three-way split and the three anatomies,
  not longer sentences; the per-item lines here are shorter than in `001`.
- **Responsive strategy:** 3 → 2 columns at 1024px with the ranges column going full width and its
  slots turning into a four-across row; one column at 768px.
- **Visual-first check:** 161 visible words, the highest in the batch, and the direct result of
  carrying all three subjects at once.

### WELL-S09-004 — Conversion-led

- **Structural intent / archetype:** Permission to inspect.
- **Layout model:** A tall reserved object area of the trolley beside a cream panel carrying the
  inspection commitment, three short guarantees on hairlines and the action, closed by a full-width
  five-slot mark row.
- **Conversion device, and the claim it replaces:** a section about equipment and products invites
  *"the most advanced technology"* — a claim about things a placeholder cannot name and could not
  substantiate if it could. The offer here is instead that **anything in the room can be examined
  and any label read**: a commitment the studio controls and can keep, and a stronger one for a
  visitor deciding whether to let a stranger work on their skin. Nothing is collected; the action
  opens a consultation route.
- **Media relationship:** One tall object area plus five mark slots.
- **Responsive strategy:** The split becomes one column at 1024px with the media resolving to 16:8;
  the action goes full width at 768px.
- **Visual-first check:** 97 visible words.

### WELL-S09-005 — Art-directed / Distinctive

- **Structural intent / archetype:** A shelf.
- **Layout model:** Four reserved object areas of deliberately different widths *and* heights stand
  bottom-aligned on one continuous rule, the way objects stand on a real shelf, with their names
  below the line. Column widths run `0.82 / 1.24 / 0.68 / 1.12`; object heights run
  `62% / 100% / 44% / 78%` of the shelf height.
- **Why the inequality is the device:** equal tiles would be a grid, and a grid is not a shelf. The
  differing proportions are what make four tonal blocks read as four different objects before any
  photography arrives.
- **Empty-state check:** the objects are tonal blocks standing on a lit rule; the arrangement reads
  as a shelf of things in the empty state, which is the state a reviewer sees.
- **Responsive strategy:** the shelf is horizontal by nature. Below 1024px it becomes **two shelves
  of two objects, each with its own rule**, rather than a stack with the rule dropped — the
  object-standing-on-a-line relationship is the study's identity and survives at every width.
- **Visual-first check:** 79 visible words, the lowest in the batch.

## Structural Diversity

| Study | Topology | Object media | Mark slots | Ground |
| --- | --- | --- | --- | --- |
| 001 | Four-column media-topped card grid | 4 equal, 4:3 | 5, in a row | Pale cool white |
| 002 | Three-plate still-life triptych | 3 equal, 4:5 tall | 4, compact | Warm ivory |
| 003 | Three labelled columns, three anatomies | 4 small square thumbnails | 4, stacked | Soft slate blue |
| 004 | Tall object beside a commitment panel | 1 tall | 5, full-width row | Deep gold-olive |
| 005 | Four unequal objects on one shelf rule | 4 **unequal** in both axes | 4, in the closing row | Near-black warm |

Every study handles the reserved marks differently — a row, a compact pair-row, a stacked column, a
full-width band, and a closing row — so the one element they all share is not the element that
makes them look alike.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 79–161 visible words. `003` sits highest because it carries all three
  subjects at once; `005` lowest because the shelf does the work the copy would otherwise do.
- **Document-metaphor justification:** `NONE`. No datasheet, specification block, ingredient table,
  compliance list or device register is used. `003` is the study that came closest and its
  three-anatomy defence is recorded in its study record.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>` element appears
  in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Object ×4 | `001` — one per equipment card | Still image, 4:3 stepping to 16:9 | Empty tonal surface with a quiet label; the card's name and policy line stand alone |
| Category plate ×3 | `002` — still life per product category | Still image, 4:5 stepping to 4:3 | Empty tonal surface; the serif name and its line carry the plate |
| Thumbnail ×4 | `003` — small square beside each equipment row | Still image, 1:1 | Empty tonal surface; the row is complete without it |
| Trolley and shelf | `004` — one tall object area beside the panel | Still image, tall, becoming 16:8 at 1024px | Empty tonal surface; the panel carries the study |
| Object ×4 | `005` — four unequal areas standing on the shelf rule | Still image, four different proportions | Empty tonal blocks; the inequality is what makes them read as objects while empty |
| Partner mark ×4–5 | All five — where a real page carries range and partner marks | Logo or wordmark, 5:2 or 7:2 | **Reserved and intentionally empty. These must never be filled with an invented mark; a filled slot means a real range the studio actually carries.** |

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above —
  including `005`'s two-shelves transformation and the mark rows' step-downs, which keep a mark
  slot from ever becoming a sliver.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s09-00N` root, verified by scan.
- **Brand and certification check: PASS.** This batch's defining check. Visible text only, comments
  stripped, scanned for *medical grade*, *clinical*, *pharmaceutical*, *patent*, *FDA*, *CE*,
  *certified*, *approved*, *professional only*, *latest technology*, *state of the art*,
  *advanced*, *exclusive*, *premium*, *proven*, *best*, efficacy verbs, awards, percentages and
  currency. Clean in all five. Reserved mark slots counted per study: 5, 4, 4, 5, 4 — all empty.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `005`'s four objects stand correctly on one continuous rule at four different heights
  and widths; `003`'s three columns show three distinct item anatomies with nothing aligning
  across them. Third consecutive batch to need no render correction.

## Notes

- This is the ninth authored batch in the `WELL` sector and the seventh authored entirely without
  references.
- **The reserved-mark pattern is the reusable outcome.** Every sector has a section that would
  carry partner logos, client marks, accreditation badges or press logos, and every one of them is
  a fabrication risk. Reserving the row as empty media slots — rather than omitting it, which hides
  the structure, or filling it, which invents brands — is the answer to all of them.
- `S09` closes the group `S02`, `S08` and `S09` form: what is done, in what order, and with what.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
