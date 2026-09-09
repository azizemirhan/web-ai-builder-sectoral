# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S13`
- Section Name: `Gallery`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S13-001` | Universal / Safe | AUTHORED | `raw/WELL-S13-001.html` |
| `WELL-S13-002` | Premium / Editorial | AUTHORED | `raw/WELL-S13-002.html` |
| `WELL-S13-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S13-003.html` |
| `WELL-S13-004` | Conversion-led | AUTHORED | `raw/WELL-S13-004.html` |
| `WELL-S13-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S13-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its density constraint and its boundary with
`S05` and `S09` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — Density, Not Claims

This is the first `WELL` section in some time whose difficulty is **not** a claims problem. Nothing
here needs reserving beyond the imagery, and imagery is already reserved everywhere. The difficulty
is the opposite one: a gallery fails by putting too much in.

`../WELLNESS-DESIGN-DIRECTION.md`:

> *Prefer fewer, larger, better-proportioned areas over many small thumbnails — a wall of treatment
> thumbnails reads as a catalogue, not as a spa.*

There is also **a specific instruction on record from the user**, given about the architecture
sector's gallery: *too many images, and it should be 3 × 3.* That is a stated preference about
galleries in general rather than a one-off correction, and this batch carries it across.

| Study | Areas | Why that many |
| --- | --- | --- |
| `001` | **9** | The stated 3 × 3, exactly |
| `002` | 3 | Editorial pacing — few, large, captioned |
| `003` | 6 | Two per group across three groups |
| `004` | 4 | One dominant plus three supporting |
| `005` | 4 | A sequence, each wider than the last |

**The count is not the point; the reading is.** Nine identical small squares would satisfy the
number and still fail the rule. At 1440px each cell in `001` is roughly 415px wide — a photograph,
not a thumbnail — and every other study differentiates its areas by scale, proportion or grouping.
Confirmed in render.

**No script.** No study uses a lightbox, carousel or slideshow. A gallery that needs JavaScript to
be looked at is not a raw study, and the sequence in `005` is in the layout rather than in a scroll
effect. Verified by scan: no `<script>` element in any file.

## What The Gallery Is Of

The rooms, the surfaces, the light and the details of the place. **Not results, and not products.**

| Section | What its imagery is |
| --- | --- |
| `S05` Results Before After | Paired outcome evidence, bound by the consent and claims rule |
| `S09` Technology Products | Objects — equipment and product categories |
| `S13` Gallery | The place — rooms, materials, light, hands at work |

A gallery that fills with before-and-afters has taken `S05`'s role and escaped `S05`'s constraint.
No study carries a paired comparison, an outcome caption or a treatment result — and three studies
say so in visible copy, which is why a scan for *result* and *before and after* matches: every
match is the section disclaiming them.

`003` needed that disclaimer most, because it puts two pictures side by side in each group. Its
closing line states plainly that two pictures in a group are two views of one subject, **not a
before and after**.

## Consent

The rule from `S04` and `S05` applies unchanged: **a filled slot showing a person means a real
person who has consented to appear.** `001` labels two person-bearing areas — *Hands at work* and
*Guest at rest* — so the requirement is visible where it applies, and every study closes on a line
stating that anyone appearing has agreed to.

## Study Records

### WELL-S13-001 — Universal / Safe

- **Structural intent / archetype:** The grid the user asked for, done at a size that works.
- **Layout model:** A split header above nine equal 4:3 areas in three columns, with gaps of
  12–22px.
- **Why equal cells are right here:** 3 × 3 means equal cells. What keeps it from being a thumbnail
  wall is scale, not variety — roughly 415px per cell at desktop.
- **Responsive strategy:** 3 → 2 → 1 columns, with the cell stepping to 3:2 at phone width so a
  single-column image does not become a tall block.
- **Areas:** 9. Two of the labels name person-bearing views.

### WELL-S13-002 — Premium / Editorial

- **Structural intent / archetype:** The argument that a gallery is improved by removing images.
- **Layout model:** One 21:9 plate across the top and two 3:4 plates beneath, each with a serif
  caption and a smaller sub-line.
- **The pairing with `001`:** where `001` carries nine, this carries three at roughly four times
  the area each. Both satisfy the direction's "fewer, larger" preference at different points on it,
  so a reviewer chooses rather than being given one reading.
- **The captions are about the photograph, not the treatment** — *photographed empty, in the
  afternoon, with nothing moved* — which is what keeps an editorial caption from drifting into a
  claim.
- **Responsive strategy:** the wide plate steps 21:9 → 16:7 → 16:10 → 4:3; the pair unstacks at
  768px.
- **Areas:** 3.

### WELL-S13-003 — Structured / Visual Modular

- **Structural intent / archetype:** Structure found in the imagery, because there is no copy to
  structure with.
- **Layout model:** Three labelled groups of two, where **each group has its own aspect ratio** —
  the rooms 16:10, the surfaces 1:1, the light 3:4 — and the surfaces and light groups are held to
  narrower measures so the three blocks differ in width as well as proportion.
- **The device:** a visitor can see there are three kinds of picture before reading a label. It is
  the `WELL-S09-003` move — a different anatomy per group — applied to a section made only of media.
- **Responsive strategy:** the proportions are the structure, so they are kept at every width; only
  the measures unlock and the rooms group goes single-column at 768px.
- **Areas:** 6.

### WELL-S13-004 — Conversion-led

- **Structural intent / archetype:** Make someone want to be in the room, then let them come to it.
- **Layout model:** One dominant 16:10 view of the room a visitor would actually be in, with the
  copy and action beside it, over a row of three 3:2 supporting views.
- **Conversion device:** the action is **a look round, not a booking**. It is a lower-commitment
  ask, it is the thing the section has just made the visitor want, and the studio can honour it
  without a diary claim. A secondary route goes to booking for anyone already past that point.
- **What it avoids:** no opening hours, no availability, no urgency. A look round is offered as a
  standing invitation rather than as a slot a placeholder cannot know about.
- **Responsive strategy:** the lead row unstacks at 1024px; the supporting row steps 3 → 2 → 1.
- **Areas:** 4.

### WELL-S13-005 — Art-directed / Distinctive

- **Structural intent / archetype:** A route through the building rather than a set of views of it.
- **Layout model:** Four photographs down the page at widths of 46% / 60% / 76% / 92% of the
  measure, with indents running alongside, so the frame opens as you descend — the door, the
  corridor, the room, the couch.
- **Why the progression is the composition:** it says *you arrive here and end up there* without a
  numbered step list, which is `WELL-S08`'s role. The captions are locations, not stages.
- **Responsive strategy:** the widths compress at each breakpoint but the progression never
  flattens — the first frame is always the narrowest and the last always the widest, because the
  opening-out is the study.
- **Areas:** 4.

## Structural Diversity

| Study | Topology | Areas | Proportions | Ground |
| --- | --- | --- | --- | --- |
| 001 | 3 × 3 equal grid | 9 | One (4:3) | Pale greige |
| 002 | One wide plate above two portraits | 3 | Two (21:9, 3:4) | Warm ivory |
| 003 | Three groups, each at its own ratio | 6 | Three (16:10, 1:1, 3:4) | Soft clay |
| 004 | Dominant view with action, over three | 4 | Two (16:10, 3:2) | Deep spa green |
| 005 | Four frames of increasing width | 4 | One ratio, four widths | Warm off-black |

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 69–106 visible words. A gallery has almost no copy by nature; the
  differentiator across the batch is entirely proportion, count and interval, which is the correct
  outcome for this role.
- **Document-metaphor justification:** `NONE`. No contact sheet, index plate, catalogue grid or
  archive sheet device is used — `001` is a nine-image grid at photograph scale, which the
  *Governing Constraint* section addresses directly.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** No `<script>` element and no inline `style` attribute in any file.
  No lightbox, carousel or slideshow anywhere in the batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Room and space views | `001` ×5, `002` ×1, `003` ×2, `004` ×4, `005` ×4 | Still image, at the study's proportion | Empty tonal surface with a quiet label naming what the view is of |
| Surface and material views | `001` ×2, `002` ×1, `003` ×2 | Still image, square or portrait | Empty tonal surface with a quiet label |
| Light views | `002` ×1, `003` ×2 | Still image, portrait | Empty tonal surface with a quiet label |
| Person-bearing views | `001` ×2 — *Hands at work*, *Guest at rest* | Still image | **A filled slot means a real person who has consented to appear.** Labelled as person-bearing so the requirement is visible at the point it applies |

Twenty-six reserved areas across the batch — nine, three, six, four and four. None is a thumbnail.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly. Captioned areas use `<figure>` / `<figcaption>`.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above — including `003`'s
  decision to keep its three proportions at every width, since they are the structure, and `005`'s
  decision that the progression must never flatten.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script or
  inline style.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status. Slot
  labels name the subject of the view, which is field naming rather than commentary.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s13-00N` root, verified by scan.
- **Density check: PASS.** Reserved-area counts verified by scan: 9 /
  3 / 6 / 4 / 4. No study exceeds nine, the shape the user asked for, and only one reaches it.
- **Role-boundary check: PASS.** Visible text scanned for outcome vocabulary, *before and after*,
  currency, durations and percentages. The only matches are the three studies **disclaiming** those
  things — *nothing here is a result*, *not a before and after*, *nothing here is a treatment
  result* — each confirmed in context.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `001`'s nine cells measure roughly 415px wide and read as photographs rather than
  thumbnails; `005`'s four frames open out correctly down the page. Sixth batch in seven to need no
  render correction.

## Notes

- This is the thirteenth authored batch in the `WELL` sector and the eleventh authored entirely
  without references.
- **The user's 3 × 3 instruction is now carried in two places** — this section's README and this
  record — so it survives into any future gallery in any sector rather than living only in
  `sectors/architecture-interior-design/sorunlar.txt`.
- The reusable outcome here is smaller than in the claims-constrained sections but real: **in a
  section made only of media, the structural direction has to find its modules in proportion.**
  `003` is the demonstration.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working —
  it rendered every study in this batch.
