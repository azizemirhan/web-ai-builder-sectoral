# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S23`
- Section Name: `Architecture / Interior Service Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S23-001` | Universal / Safe | AUTHORED | `raw/ARC-S23-001.html` |
| `ARC-S23-002` | Premium / Editorial | AUTHORED | `raw/ARC-S23-002.html` |
| `ARC-S23-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S23-003.html` |
| `ARC-S23-004` | Conversion-led | AUTHORED | `raw/ARC-S23-004.html` |
| `ARC-S23-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S23-005.html` |

## Authoring Direction

**No reference images were supplied.** Like `ARC-S21` and `ARC-S22`, this batch was authored against
the section README written during the catalog extension.

**These are the sector's first page studies rather than section studies.** Everything authored for
`ARC-S01`–`ARC-S14` was a band that a page is assembled from. `S23` is a page role: its README
describes a document a visitor lands on and reads to the end, and it names six pieces of content
that have to coexist on it — description, inclusions and exclusions, delivery, suitability, adjacent
offerings, and a route to enquire. Each study is therefore a complete page from breadcrumb to
closing note.

### The composition boundary, made explicit

Each study opens with a region marked `data-region="page-context"` carrying a breadcrumb and a page
header. **That region overlaps `ARC-S22` and `ARC-S21` and would be supplied by those sections in an
assembly, not duplicated here.** It is included so that each study reads as a real page rather than
as a body fragment beginning mid-air. Every study says so in its own closing note and in its file
header. The region is deliberately plain in all five: the studies differ *below* it, which is where
this section's actual content responsibility begins.

### What the README ruled out, and what that changed

The out-of-scope list names four things — **fabricated pricing, guarantees, turnaround times and
availability** — and those four are precisely what a service page reaches for when it wants to feel
concrete. They are absent from all five studies, and their absence was designed around rather than
worked around:

- `003` states its stages as **sequence and dependency** (`T1` … `T6`, "depends on: T1 signed off")
  where a scope document would normally state durations. The dependency column carries the
  information a duration would have carried, and none of it is invented.
- `004` is the study most exposed to this, because a conversion page without numbers has to persuade
  some other way. Its "what happens after you enquire" steps describe **order only** — no response
  time, no capacity, no scarcity. It converts by *disqualifying*: the self-selection pair sends the
  wrong reader to another service by name.
- `005` states obligations as **what is done**, never as how long it takes.

The fifth temptation, not in the README but adjacent to it, is the fake enquiry endpoint. `004`
carries a real labelled form; it is unwired, has no action, and says so in visible text next to its
own submit button rather than only in a comment.

## Study Records

### ARC-S23-001 — Universal / Safe

- **Structural intent / archetype:** The standard service detail page. Every one of the README's six
  content pieces present, in the order a visitor asks for them, with nothing clever between them.
- **Layout model:** A `1.6fr / 0.62fr` body — a measured main column carrying description,
  inclusions and exclusions as a two-up pair, a four-stage delivery list and a suitability section —
  beside a sticky "at a glance" facts rail. Related services as three cards, then a filled enquiry
  block.
- **Density:** Medium.
- **Media mode:** TWO supporting areas, paired, `4/3`. The page is complete with both empty: they
  sit in their own section near the foot and carry no argument.
- **Interaction:** None. Static.
- **Responsive strategy:** The README's rail rule is answered literally — **the rail releases to
  normal flow at 1024px**, before it starts competing with the body, and becomes a two-column
  definition list rather than a shrunken column. Inclusions and exclusions stay side by side to
  480px and then stack; the stage number moves above its stage at 480px.
- **Composer value:** The safest binding target for the whole section. Its content model is
  `{title, standfirst, description, included[], excluded[], stages[], suitability, facts{}, related[], enquiry}`
  — the full README contract with nothing optional.
- **Limitation / content ceiling:** Six inclusions against four exclusions is the balanced shape;
  a much longer inclusion list unbalances the two-up pair before 1024px. Four stages fit the rail's
  height; more and the rail runs out before the body does.

### ARC-S23-002 — Premium / Editorial

- **Structural intent / archetype:** The offering as an argument, read start to finish. The premium
  move here is **refusal**: no rail, no cards, no chrome — one column, in order.
- **Layout model:** A centred `34rem` measure the whole way down, a `21/9` plate above it, a margin
  note that sits in the outer column above 1080px, a pull statement that breaks the measure to
  `44rem`, and a closing colophon carrying the facts once.
- **Density:** Low — the lowest in the batch.
- **Media mode:** ONE wide plate. The page reads intact when it is empty; it illustrates rather than
  carries, which is exactly the README's phrasing.
- **Interaction:** None. Static.
- **Responsive strategy:** The measure is the layout, so responsiveness is measure management:
  `34rem` → `33rem` at 1280 → `36rem` at 1024 → unconstrained at 768. The margin note leaves the
  outer column and folds into flow below 1080px. The drop cap becomes ordinary text at 480px, where
  a three-line initial eats a phone measure. The plate goes `21/9` → `16/9` → `4/3`.
- **Composer value:** The editorial register, and the only study whose facts are **not** presented
  as a lookup surface. Its content model is deliberately smaller than `001`'s: prose, one plate, one
  pull statement, four colophon fields.
- **Limitation / content ceiling:** It will not hold a long inclusion list or a deep stage set — the
  run-lists are sized for five or six items. A service with a lot of specifics belongs in `003`.

### ARC-S23-003 — Dense / Information-heavy

- **Structural intent / archetype:** The scope document. Where `001` describes an offering, this one
  **defines** it: numbered clauses, a deliverables table, assumptions against conditions, and the
  questions that actually get asked.
- **Layout model:** A document head with a six-field metadata block, a three-column contents grid of
  in-page anchors, then six numbered clauses on a `4.6em` number spine. Clause 3 carries a real
  `<table>` with a caption and row headers; clause 6 is a `<dl>` question register.
- **Density:** High — the highest in the batch.
- **Media mode:** NONE. A scope document carries no imagery, and the README makes media optional.
- **Interaction:** None. Static, and pointedly so: **nothing is hidden behind a control.** The
  README permits disclosure or tabs where an offering has stages, but requires the full content to
  remain reachable without script — the simplest way to satisfy that is not to hide anything, and a
  reader comparing two clauses should not have to open them.
- **Responsive strategy:** Contents grid `3` → `2` → `1` columns; the clause number leaves its spine
  and sits above its clause at 768px; the two-up bodies stack at 768px. The table gets its own
  `overflow-x: auto` container with a `min-width`, so it scrolls inside itself and the page body
  never scrolls sideways.
- **Composer value:** The highest-capacity option in the section, and the only one modelling
  deliverables as tabular data with an issue purpose and a dependency. Its content model is
  `{clauses[], included[], excluded[], deliverables[{stage, deliverable, purpose, depends}], assumptions[], conditions[], interfaces[], questions[]}`.
- **Limitation / content ceiling:** Six clauses and six table rows is the tested shape. Past about
  eight clauses the contents grid stops being a glance and becomes a second document.

### ARC-S23-004 — Conversion-led

- **Structural intent / archetype:** The page ordered by the reader's decision rather than by the
  anatomy of the service. It answers "is this for me" before "what is it", and it ends in a form
  rather than a link.
- **Layout model:** A decision header pairing the title with a bordered action box (two actions plus
  four quick facts), then a two-card self-selection pair, a three-column scope list, a three-step
  "what happens after you enquire", and a filled enquiry block holding a `0.85fr / 1.15fr` form.
- **Density:** Medium.
- **Media mode:** NONE. The page is a decision surface; nothing on it needs illustrating.
- **Interaction:** None. The form is markup only — no `action`, no script — and the page says so in
  visible text beside the submit button, not just in a comment. Four fields, four `<label for>`, two
  hints wired with `aria-describedby`, one `<fieldset>` with a `<legend>`.
- **Responsive strategy:** The decision header collapses at 1024px with the action box moving below
  the title, so the action is never a shrunken column beside the heading. The self-selection pair
  stacks at 768px, the form fields at 480px, and both buttons go full width at 480px.
- **Composer value:** The conversion register for a detail page, and the only study carrying an
  enquiry form rather than a link. Its content model adds
  `{fit_yes[], fit_no[], alternatives[], next_steps[], form_fields[]}` to the section contract.
- **Limitation / content ceiling:** Four fit reasons against three, three steps, four form fields.
  A longer form belongs to `S19 Project Inquiry`, which is a section role of its own — this form is
  the *service-specific* route the README asks for, not a general contact form.

### ARC-S23-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The **division-of-responsibility schedule** from an
  architectural appointment document — the register a client actually reads to find out what they
  are agreeing to do themselves. It answers the README's "how it is delivered" by splitting delivery
  in two, which none of the other four do.
- **Layout model:** A ledger of five stages. Each stage row is a
  `1fr / clamp(30px,4.4vw,72px) / 1fr` grid: a full-width stage head naming the stage and the item
  that closes it, then the studio's obligations on the left and the client's on the right, either
  side of a drawn spine. Column captions appear once, above the ledger. Below: a four-frame record
  strip, an "outside this appointment" list against a suitability note, related services, and the
  enquiry close.
- **Density:** Medium-high.
- **Media mode:** ONE record strip of four `3/2` frames. The ledger is complete without it, and the
  captions are sequence words rather than claims about a real building.
- **Interaction:** None. Static.
- **Responsive strategy:** The spine is a wide-width device, so at 768px it is removed and the two
  sides stack — **each keeping its own visible heading**, so the split survives without the
  geometry. The stage head's "closes with" line takes its own full-width line at the same
  breakpoint. Record strip `4` → `2` → `1`.
- **Composer value:** The identity option, and a **fourteenth sector-native register** for the
  sector. Its content model is genuinely different from the rest of the section:
  `{stages[{name, closes_with, studio_duties[], client_duties[]}]}` — a two-sided obligation list
  that no generic service-page component carries.
- **Limitation / content ceiling:** Five stages with three duties per side is the tested shape.
  Unequal sides read as an imbalance rather than as information, so the register wants roughly
  symmetric content; a service where the client does almost nothing should use `001`.

## Research Metadata

- **Sources:** None. Authored against the section README written during the catalog extension.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five ways one offering can be
  set out at depth — described plainly, argued as an essay, defined as a scope document, ordered
  around the decision to enquire, and split into who does what.
- **Differentiation notes:** Five distinct page geometries: measured column plus sticky rail; single
  centred measure with no rail at all; numbered clause spine with tabular data; decision-ordered
  blocks closing on a form; and a two-sided ledger across a spine. Grounds differ — near-white,
  warm paper, cool grey, warm off-white, and paper. Typography differs — three system-font studies,
  one serif editorial study, one mono-led document. Media differs — two frames, one plate, none,
  none, four frames. **No study uses JavaScript.**
- **Sector-interpretation note:** The sector's nearest section is `S03 Services`, which is the
  *index*. Nothing from `S03` is repeated here: this page is what one of its entries opens into, and
  none of the five studies lists more than one offering.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `@import`, `url()`, webfont, inline SVG, or inline
  `style` attribute in any of the five files.
- Network calls: NONE. Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static.
- Form endpoints: NONE. `004`'s form has an empty `action` and is labelled a placeholder on the page.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| `media-1`, `media-2` | `ARC-S23-001` | Two supporting frames near the foot, captioned "interior view" and "joinery detail" | Photograph, `4/3` | Sit in their own section; removing both leaves every README content piece intact. Captions are neutral and describe the kind of view, not a project. |
| `plate` | `ARC-S23-002` | One wide plate between the title and the essay | Photograph, `21/9` → `16/9` → `4/3` | The essay is self-contained; the plate illustrates the register rather than the argument. |
| — | `ARC-S23-003` | **No media slot, by design** | — | A scope document carries no imagery. |
| — | `ARC-S23-004` | **No media slot, by design** | — | A decision surface; nothing on it needs illustrating. |
| `record-1` … `record-4` | `ARC-S23-005` | Four-frame record strip below the ledger | Photograph, `3/2` | Captions are sequence words — as found, opened up, new work, complete — not claims about a real building. The ledger is complete with all four empty. |

No slot in any study carries a client logo, an award mark, a certification badge, a signature, or a
named person. No slot implies a completed project.

## QA

- **ID validation: PASS.** Five IDs, each with matching `<meta name="study-id">`, `data-study-id`,
  scoped root class and filename; every element `id` namespaced with the study ID and unique.
- **Raw-format validation: PASS.** Tag balance, nesting and unique-id checks pass on all five;
  unscoped-CSS and inline-`style` scans both return zero. The only unscoped rules are the two
  standalone-host baselines (`html { -webkit-text-size-adjust }`, `body { margin; background }`).
- **Accessibility QA: PASS.** One `<h1>` per study; no heading jumps — `005` runs `h1 → h2 → h3 → h4`
  because each ledger stage carries two duty columns, each with its own heading. Every
  `aria-labelledby` and `aria-describedby` resolves. Every `<a>` carries an `href`; every breadcrumb
  is a named `<nav>` landmark with the current page as a `<span aria-current="page">`, never a link.
  Visible `:focus-visible` in all five, with a light-on-dark focus colour inside the dark panels of
  `001` and `004`. `prefers-reduced-motion` block in all five. Inclusion and exclusion are marked
  with **words** (`Yes`/`No`, `Incl`/`Excl`, `Fits`/`Other`), never a glyph or a colour alone; in
  `005` the left/right split is reinforced by a visible heading on each side, so removing the spine
  removes nothing.
- **Form QA (`004`): PASS.** Four controls, four `<label for>` resolving, `<fieldset>` with
  `<legend>`, both hints wired with `aria-describedby`, `autocomplete` on name and email, a real
  `<button type="submit">`, 48px minimum control height, and a visible statement that the form is
  unwired.
- **Contrast QA: PASS.** Measured on 46 pairs across the batch: all text ≥ 4.5:1, all interactive
  and component borders ≥ 3:1. Two failures were found and fixed before sign-off — `004`'s form
  field border measured 1.93:1 against its panel, which fails the 3:1 component-boundary threshold
  that a field's only visible boundary has to meet, and was raised to 3.22:1 with its hover state at
  5.62:1; `005`'s em-dash list marker measured 3.56:1 and was given a dedicated `--marker` token at
  4.89:1, **held to the 4.5:1 text threshold rather than the 3:1 non-text one**, the same decision
  taken for the separator glyphs in `ARC-S22`.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder, and every grid track uses `minmax(0, …)`. The
  README's two responsive rules are answered directly: a controlled measure at wide widths exists in
  every study (`001` caps body copy at `68ch`, `002` at `34rem`, `003` at `76ch`, `004` at `54ch`,
  `005` at `72ch`), and **no study collapses into a single dense column on a phone** — each one
  changes structure instead. The rail rule is answered literally in `001`, the only study with a
  sticky element: it releases at 1024px and reforms as a two-column list.
- **Dependency validation: PASS.** Zero matches across all five files.
- **Role-compliance validation: PASS.** No study carries an index or grid of every offering, or
  homepage positioning copy. A claim scan for price, fee, cost, guarantee, warranty, turnaround,
  availability, capacity, percentage, award, certification, rating and ranking vocabulary returns
  matches **only** inside this batch's own disclaimers, two excluded-scope list items ("fire
  engineering and specialist certification", "statutory applications and their fees" — both stated
  as *not* included), and one negation ("it is not a permission and it is not a price").
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- **This is the sector's first page-role batch.** The `data-region="page-context"` marker is the
  mechanism that keeps that honest: it names the part of each study that belongs to `ARC-S21` and
  `ARC-S22` rather than to this section, so an ingestion pass can strip or replace it without
  guessing. The same marker should be used for `S24`–`S27`.
- `ARC-S23-005` adds a fourteenth sector-native register — the division-of-responsibility ledger.
  It was chosen against the registers already used in this sector: it is deliberately not the
  schedule of services with dot leaders (`ARC-S10-005`), the project programme table
  (`ARC-S06-005`), or the numbered-clause and hanging-indent registers (`ARC-S05-005`,
  `ARC-S09-005`). The organising idea — the split across the spine — is the part none of those have.
- The unwired form in `004` is the one piece of this batch that a reviewer should look at twice. It
  is markup for a route to enquire, which the README requires; it is not a working endpoint, and the
  page says so where a visitor will read it.
- The `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` roll-up counters still read
  `NOT_STARTED` for this sector. They are catalog-wide bookkeeping and need a separate
  workspace-level pass; they are deliberately not touched at section close-out.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
