# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S26`
- Section Name: `Architect / Designer Profile`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S26-001` | Universal / Safe | AUTHORED | `raw/ARC-S26-001.html` |
| `ARC-S26-002` | Premium / Editorial | AUTHORED | `raw/ARC-S26-002.html` |
| `ARC-S26-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S26-003.html` |
| `ARC-S26-004` | Conversion-led | AUTHORED | `raw/ARC-S26-004.html` |
| `ARC-S26-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S26-005.html` |

## Authoring Direction

**No reference images were supplied.** Authored against the section README.

This section's README is unusually direct, and two of its lines governed every study:

> *"Nothing in this role may be invented. Credentials, registrations and memberships are verifiable
> facts about real people, and a placeholder study must leave them as reserved fields rather than
> fill them."*

> *"Portrait and identity must stay paired at every width; a name must never end up beside or above
> the wrong portrait when the layout reflows."*

### The reserved-field device

Those facts are not omitted from these studies — they are **present, labelled and empty**. A profile
that simply drops the credential rows hides the shape of the page; one that fills them invents facts
about a person. So every study carries a register whose values read `Reserved` or `Reserved field —
supplied by the studio`, and each says on the page why. The device carries the whole batch: 22
reserved values across the five studies, and not one filled credential, registration, membership,
award, publication or direct contact detail.

The same rule extends past the README's list: no invented social handle or profile link, no
testimonial, no rating, and — in `004`, where the temptation is strongest — **no availability,
response time or capacity**, which a profile cannot promise on a person's behalf.

### The pairing rule, implemented rather than asserted

In all five studies the portrait and the identity text are **children of one grid**, never siblings
in the page flow. Reflow moves that grid as a unit, so nothing can be inserted between a portrait
and the name that belongs to it:

- `001`, `002` — the pair stacks together at 768px, portrait then name, nothing between.
- `003`, `005` — the pair *keeps its row* at every width, shrinking the portrait to 72px and then
  60px rather than breaking the row.
- `004` — the pair is its own grid **inside** the decision header, so the action box beside it can
  never land between the portrait and the name when the header collapses at 1024px.

## Study Records

### ARC-S26-001 — Universal / Safe

- **Structural intent / archetype:** The plain profile. Portrait and identity, what the post covers,
  how they work, what they are attached to, the background register, and a contact route.
- **Layout model:** Identity at `0.36fr / 1fr` above a rule; body at `1.5fr / 0.7fr` with a sticky
  contact card and an "also in this discipline" list in the rail.
- **Density:** Medium. **Media:** one `3/4` portrait area. **Interaction:** none.
- **Responsive strategy:** Rail releases at 1024px; the identity pair stacks at 768px with the
  portrait becoming `4/3`; the background register goes label-over-value at 480px.
- **Composer value:** The section's safest binding target —
  `{name, role, based_at, works_on, post, method, attachments[], reserved[], contact}`.
- **Limitation / content ceiling:** Five reserved rows and four attachments before the rail runs
  shorter than the body.

### ARC-S26-002 — Premium / Editorial

- **Structural intent / archetype:** The profile as a page in a monograph: one tall plate, a written
  statement, and almost no furniture.
- **Layout model:** Identity at `0.82fr / 1fr`, aligned to the baseline of the plate; then a `34rem`
  measure carrying the statement, a pull line, the attachments as a dashed list, and the reserved
  fields as a two-column CSS `columns` register.
- **Density:** Low. **Media:** one `4/5` portrait plate. **Interaction:** none.
- **Responsive strategy:** Measure `34rem` → `33rem` → `36rem` → unconstrained; the reserved register
  drops to one column at 768px; the drop cap becomes ordinary text at 480px.
- **Composer value:** The editorial register, and the only study where the person is described in
  prose rather than in fields.
- **Limitation / content ceiling:** Three statement paragraphs and six reserved rows. It carries no
  table and no rail; a person with a lot of structured detail belongs in `003` or `005`.

### ARC-S26-003 — Dense / Information-heavy

- **Structural intent / archetype:** The personnel record. Everything a studio holds about a post,
  open on one page.
- **Layout model:** Identity band at `118px / 1fr / 0.5fr`; an eight-row field register in two
  columns; a six-row stage-involvement table; attached work in two columns; and a bordered reserved
  block set apart from the rest of the sheet.
- **Density:** High — the densest in the section. **Media:** one small portrait. **Interaction:**
  none, and pointedly: nothing is hidden behind a control, because a reader comparing two people
  should not have to open anything.
- **Responsive strategy:** The identity facts move to a full-width two-across list at 1024px; field
  register and attached work go single-column at 768px; the portrait row survives to 360px at 60px
  wide.
- **Composer value:** The highest-capacity option, and the only one modelling **involvement by work
  stage** — `{stage, involvement, output}` — which is how a practice actually describes a post.
- **Limitation / content ceiling:** Eight fields, six stages, nine reserved rows.

### ARC-S26-004 — Conversion-led

- **Structural intent / archetype:** The profile ordered around asking for this person, and honest
  enough to send the wrong enquiry to another post by name.
- **Layout model:** Decision header at `1.28fr / 1fr` — the portrait-and-identity pair on the left,
  a bordered action box on the right — then what they help with in two columns, a bordered "when to
  ask for someone else" card, three introduction steps, what to include, and a filled closing band.
- **Density:** Medium. **Media:** one portrait. **Interaction:** none; **no form**, because the route
  is an enquiry to the studio and the section carries no form anywhere.
- **Responsive strategy:** Header collapses at 1024px with the action box below the pair; help list
  and steps go single-column at 768px; the pair itself stacks only at 480px.
- **Composer value:** The conversion register for a person page. Adds
  `{helps_with[], ask_elsewhere[], steps[], what_to_include[]}`.
- **Limitation / content ceiling:** Six help rows, three alternatives, three steps. **No
  availability, response time or capacity is stated**, which is the discipline this territory needs
  here.

### ARC-S26-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The **bid curriculum sheet** — the one page per person a
  practice issues with a submission, ruled and referenced, saying what that person carries and on
  what kind of project.
- **Layout model:** A bordered sheet: an issue line of four fields; a post block at
  `132px / 1fr / 0.62fr`; a **coverage matrix** of project type against stage; a split of experience
  register and verification block divided by a rule; and a sheet foot.
- **Density:** Medium-high. **Media:** one portrait inside the sheet. **Interaction:** none.
- **Responsive strategy:** The split becomes stacked with the rule turning horizontal at 1024px; the
  post facts move full width and go two-across; the portrait row holds to 64px at 360px; the matrix
  scrolls inside its own container so the page never scrolls sideways.
- **Composer value:** The identity option and a **sixteenth sector-native register** for the sector.
  Content model `{coverage[{type, stage: involvement}], verification[]}` — a two-axis statement of
  what a person carries, which no generic profile component holds.
- **Limitation / content ceiling:** Four project types against four stages is the tested shape.

## Research Metadata

- **Sources:** None. Authored against the section README.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five ways one person can be
  described — plainly, in prose, as a record, as a decision, and as a submission sheet.
- **Differentiation notes:** Five distinct geometries: identity-plus-rail; plate-and-measure; record
  sheet; decision header; ruled bid sheet. Grounds differ — near-white, warm paper, cool grey, warm
  off-white, paper with a lighter sheet. Portrait ratios differ — `3/4`, `4/5`, small `3/4`, `3/4`,
  sheet-inset. **No study uses JavaScript and none carries a form.**
- **Sector-interpretation note:** `S08 Architects & Designers` is the team index; this is the depth
  page behind one of its entries. The `Team member NN` naming is carried over from `S08` deliberately,
  so both sections use one token vocabulary.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `@import`, `url()`, webfont, inline SVG or inline
  `style` attribute in any of the five files.
- Network calls: NONE. Browser storage: NONE. JavaScript necessity: NONE.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| `portrait` | `ARC-S26-001` | Identity portrait | Photograph, `3/4` → `4/3` | Empty by default. Every field on the page reads without it. |
| `portrait` | `ARC-S26-002` | Tall editorial plate | Photograph, `4/5` → `4/3` | Captioned as a placeholder; the statement is self-contained. |
| `portrait` | `ARC-S26-003` | Record-sheet portrait | Photograph, `3/4` | Small by design; the record is the content. |
| `portrait` | `ARC-S26-004` | Identity portrait | Photograph, `3/4` → `4/3` | Sits inside the pair grid, never beside the action box. |
| `portrait` | `ARC-S26-005` | Sheet portrait | Photograph, `3/4` | Inside the ruled sheet; the coverage matrix carries the page. |

**A filled portrait slot means an image of a real person who has consented to appear** — the section
README's phrasing. No slot in this batch carries a name, a signature, a credential mark or a logo.

## QA

- **ID validation: PASS.** Five IDs with matching `<meta name="study-id">`, `data-study-id`, scoped
  root class and filename; every element `id` namespaced and unique.
- **Raw-format validation: PASS.** Tag balance, nesting and unique-id checks pass; unscoped-CSS and
  inline-`style` scans return zero.
- **Person-policy QA: PASS — the key check for this section.** Measured across all five: 22 reserved
  values, zero filled credentials, registrations, memberships, awards or publications; zero personal
  contact details; zero social handles or profile links; zero testimonials or ratings; zero invented
  names — every person is `Team member NN`. A vocabulary scan for registration and award terms
  returns matches only inside this batch's own disclaimers.
- **Pairing QA: PASS.** In all five studies the portrait and the identity text are children of one
  grid element. Checked at 1440, 1280, 1024, 768, 480 and 360px: no width separates them, and no
  other content is ever placed between them.
- **Accessibility QA: PASS.** One `<h1>` per study, no heading jumps, every `aria-labelledby`
  resolving, every `<a>` with an `href`, `:focus-visible` in all five with a light focus colour
  inside dark panels, `prefers-reduced-motion` in all five. Stage involvement in `003` and coverage
  in `005` are stated **in words** in every cell, so nothing depends on a tick, a dot or a fill.
- **Contrast QA: PASS.** 36 pairs measured across this section: all text ≥ 4.5:1, all component
  boundaries ≥ 3:1. No failures.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390 and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder; every grid track uses `minmax(0, …)`; the sticky
  rail in `001` releases at 1024px; both tables scroll inside their own containers.
- **Role-compliance validation: PASS.** No study carries a team index or grid, which belongs to
  `S08`.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- The reserved-field register is the transferable idea in this batch and should survive normalisation
  as a **content type**, not as styling: a profile component needs a way to say "this field exists
  and is empty" that is different from "this field is absent".
- `ARC-S26-005` adds a sixteenth sector-native register — the bid curriculum sheet. It was checked
  against the drawing-sheet title block already used in `ARC-S01-005` and `ARC-S03-005`: that
  register describes a drawing and is organised by its corner block; this one describes a person and
  is organised by the coverage matrix, with the issue line reduced to a single row.
- Every study marks its top region `data-region="page-context"` — the mechanism introduced in
  `ARC-S23`.
- `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` roll-up counters are unchanged; they need a
  separate workspace-level pass.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
