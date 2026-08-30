# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S09`
- Section Name: `Awards & Publications`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S09-001` | Universal / Safe | AUTHORED | `raw/ARC-S09-001.html` |
| `ARC-S09-002` | Premium / Editorial | AUTHORED | `raw/ARC-S09-002.html` |
| `ARC-S09-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S09-003.html` |
| `ARC-S09-004` | Conversion-led | AUTHORED | `raw/ARC-S09-004.html` |
| `ARC-S09-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S09-005.html` |

## Authoring Direction

**No reference images were supplied.** The five topologies were designed to brief and checked
against each other and against the forty-two studies already authored in `ARC-S01`–`ARC-S08`, so
no device is reused across sections.

### The problem this section poses

Every other section can be placeheld with neutral copy. This one cannot, because its subject *is*
evidence. An awards section filled with plausible-looking entries — "Design Prize, Residential
Category" — is indistinguishable from a real record, and a studio pasting its own content over the
top would be correcting a fabrication rather than filling a blank. Two rules follow, and they
shape every study here:

- **Template tokens, not sample records.** Fields read `YYYY`, `NN`, `Award record 01`,
  `Category placeholder`, `Awarding body placeholder`. A token is visibly a slot; a plausible
  value is not. No concrete year appears anywhere in the batch — a QA scan for any four-digit year
  returns nothing.
- **No institution, real or invented.** No awarding body, publication, publisher, jury or prize is
  named, and no plausible-sounding fictional one is created either. Inventing a body is the same
  failure as naming a real one: the reader cannot tell.

Every study also carries a visible note saying the entries are tokens and that nothing asserts an
award was given or an article printed.

### Why four of five studies carry no image

The natural imagery for this section is award marks, jury seals and publication mastheads. Those
cannot be placeheld honestly — a rectangle labelled "award badge" invites a real badge, and any
drawn badge shape reads as an endorsement. So `001`, `003`, `004` and `005` offer no image slot at
all, and `002` offers one slot described specifically as a **tear sheet — a page spread**, which is
a photograph of published work rather than a mark of endorsement. This is a deliberate constraint,
not an omission, and it is what pushed the section toward typographic and tabular solutions.

## Study Records

### ARC-S09-001 — Universal / Safe

- **Structural intent / archetype:** The two records a studio actually keeps, side by side: what has
  been recognised, and what has been written about. The plainest useful form.
- **Layout model:** A split head (heading against an explanatory paragraph) over two parallel
  columns, each a hairline list. Each row places the record title and its category on the left with
  the year token right-aligned on the first line, so the two lists scan as one ledger.
- **Density:** Medium. Eight entries across two lists.
- **Media mode:** None, by policy.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Head stacks at 1024px; the two lists become one column at 768px, keeping
  their headings so the grouping survives; at 480px the year drops below the title rather than
  squeezing the record name.
- **Composer value:** The safest binding target — two repeatable collections of title, category and
  year, with nothing that depends on an image, a link or a count.
- **Limitation / content ceiling:** Four entries per list before the section gets long; category is
  one short line. There is no per-entry link and no outcome field, so it records what exists rather
  than routing anywhere.

### ARC-S09-002 — Premium / Editorial

- **Structural intent / archetype:** One piece of coverage given the weight of a spread, with the
  rest of the record set as a display-scale index beside it.
- **Layout model:** A serif heading over a `0.78fr / 1.35fr` body. The left column is a single
  tear-sheet area at 4:5 with a monospace caption. The right column is an index whose rows set the
  record at heading size with the kind beneath and monospace metadata right-aligned on the first
  line, separated by hairlines.
- **Density:** Low-medium.
- **Media mode:** One empty tear-sheet area — explicitly a page spread, not a mark or masthead.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Body stacks at 1024px with the tear sheet capped at 420px so it does not
  dominate; the sheet re-proportions to 16:10 at 768px; index metadata drops below the record at
  480px.
- **Composer value:** The premium register, and the only study here that mixes awards and
  publications in one chronological index rather than separating them — useful where the studio
  wants one "recognition" narrative.
- **Limitation / content ceiling:** Five index entries at display scale before the section outruns
  the tear sheet. Record titles must be short; at `1.5rem` a long title wraps to three lines and
  breaks the row rhythm. Depends on having one strong spread to feature.

### ARC-S09-003 — Dense / Information-heavy

- **Structural intent / archetype:** The complete record as a working table — the form a studio
  keeps internally, exposed rather than curated.
- **Layout model:** A head row over a four-cell summary rail, then a bordered card holding a real
  `<table>` with sticky column headers: year, record, project, kind chip, and a "field to fill"
  column. Eight rows covering awards, press and book contributions in one sequence.
- **Density:** High — the largest content set in the section.
- **Media mode:** None, by policy.
- **Interaction:** None. No `<script>` element. Below 900px the table becomes a labelled,
  keyboard-focusable scroll region with a 720px minimum, so no column is dropped.
- **Responsive strategy:** Summary rail steps 4 → 2 → 1 columns; the table enters its scroll region
  at 900px and tightens its minimum at 480px. Sticky headers keep the column names visible while
  the body scrolls.
- **Composer value:** The highest-capacity option, and the only one that models awards and
  publications as one table with a `kind` field — which is how most content models would actually
  store them.
- **Limitation / content ceiling:** Five columns is the practical maximum before the scroll region
  becomes the primary reading mode. Horizontal scrolling on phones is a deliberate trade. The
  summary rail counts rows in this table, and its labels say so explicitly — it must never be
  repurposed to count achievements.

### ARC-S09-004 — Conversion-led

- **Structural intent / archetype:** This section's real audience is often a journalist or an awards
  jury looking for material, so the conversion is a press enquiry rather than a client enquiry.
- **Layout model:** A `0.86fr / 1.2fr` grid. The left column is a sticky dark press-office panel
  with a heading, a short line, a full-width primary action and three secondary links. The right
  column is a coverage list where each row pairs the record and its monospace metadata with its own
  pill "Read" link.
- **Density:** Medium.
- **Media mode:** None, by policy — the panel offers a press kit instead of showing marks.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The panel un-sticks and the grid stacks at 1024px; at 480px each coverage
  row goes single-column and its read link goes full width, so the touch target never depends on
  the row width.
- **Composer value:** The conversion register, and the only study in the sector aimed at press
  rather than clients. The three secondary links (media enquiries, image use and credits, awards
  submissions) are the routes a practice is actually asked for.
- **Limitation / content ceiling:** Five coverage rows before the list outruns the sticky panel.
  The panel promises no contents and no response time — deliberately, since neither can be true of
  a placeholder — so a studio filling it must add both.

### ARC-S09-005 — Sector-native / Distinctive

- **Structural intent / archetype:** Monograph back matter. A practice lists awards and published
  work as citations that can be checked, not as badges — in the back of a monograph, in a CV, in a
  competition submission. That convention is the sector-native device.
- **Layout model:** A ruled head over two grouped bibliographies. Each group is set in a two-column
  flow using CSS `columns` with `break-inside: avoid`, and each entry is a true hanging indent
  (`padding-left` with a negative `text-indent`) opening on a bracketed monospace citation key
  (`[A-01]`, `[P-03]`). Entries run as citation text: italic body or title, record, project, issue
  and page tokens, year.
- **Density:** Medium-high. Ten citations across two groups.
- **Media mode:** None. Back matter is set text; an image would break the convention the study is
  built on.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The multi-column flow drops to one column at 768px, because a hanging
  indent only reads when the measure is wide enough; at 480px the hanging indent is abandoned
  entirely and the citation key moves onto its own line, rather than leaving a 4.6em indent on a
  narrow measure.
- **Composer value:** The identity option, and a sixth distinct sector-native register for the
  sector alongside the drawing sheet, the specification clause, the project programme, the
  monograph colophon and the practice register. It is also the most honest structure available for
  this section: a citation is checkable in a way a badge is not.
- **Limitation / content ceiling:** Roughly six citations per group before the two-column flow
  becomes uneven. Citation format is fixed by the markup, so a studio using a different convention
  would need the entries rewritten. The register reads as scholarly and will suit a practice that
  publishes rather than one that advertises.

## Research Metadata

- **Sources:** None. This section was authored to brief with no reference images.
- **Research date:** 2026-08-30
- **Structural territory rationale:** Territories were mapped onto the five ways a practice presents
  this material — two plain parallel ledgers for the general case, one featured spread with an index
  for the premium case, the full internal table for the dense case, a press office for the case
  where the visitor is media rather than a client, and monograph back matter for the
  discipline-native case.
- **Differentiation notes:** Five distinct geometries — parallel hairline lists, a tear sheet beside
  a display index, a summary rail over a scrollable table, a sticky dark panel beside a linked list,
  and a two-column citation flow. Only one has an image; only one is tabular; only one is dark; only
  one uses CSS `columns`; only one carries links. Grounds differ: white, warm off-white, cool grey,
  near-white with a dark panel, and paper. No study uses JavaScript.
- **Sector-interpretation note:** The section's whole content class is evidence, so the substantive
  design decision here was what *not* to draw. See "The problem this section poses" above.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, no inline
  SVG. All type uses system font stacks.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Tear sheet | `ARC-S09-002` | One featured spread from published work | Still image of a page spread, 4:5 (16:10 at 768px) | Labelled empty area with a monospace caption. **Not a logo or badge slot** — filling it with an award mark or a masthead would turn a placeholder into an endorsement. |
| — | `ARC-S09-001` | **No media slot by design** | — | Award marks and mastheads cannot be placeheld honestly; see Authoring Direction. |
| — | `ARC-S09-003` | **No media slot by design** | — | As above. |
| — | `ARC-S09-004` | **No media slot by design** | — | As above. |
| — | `ARC-S09-005` | **No media slot by design** | — | As above; back matter is set text. |

No study contains a logo, a badge, a seal, a masthead, or any fabricated evidence. Licensing and
provenance metadata is not applicable because no third-party asset is referenced — and for this
section specifically, filling the one slot means using an image of a real published spread, which
carries the publisher's rights.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S09-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps — `001` and
  `004` run three levels because their entries sit under group headings. Sequences use `<ol>` so
  order is structural. The `003` table has a `<caption>` and `scope`-qualified headers, and its
  scroll region is labelled and keyboard focusable. Every `<a>` carries an `href`, and the repeated
  "Read" links in `004` each carry an `aria-label` naming their record rather than relying on
  "Read" alone. Visible `:focus-visible` styling in all five, with an amber ring inside the dark
  panel, and a `prefers-reduced-motion` block in all five. Contrast measured on 21 text and UI
  colour pairs against each study's own ground: all text ≥ 4.5:1 (lowest 6.73:1) and all
  interactive borders ≥ 3:1 (lowest 3.55:1).
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder; `003` adds a 900px rule where
  its table enters a scroll region. Two layouts change behaviour rather than shrinking: `003`
  scrolls its table instead of dropping columns, and `005` abandons its hanging indent at 480px
  instead of leaving a 4.6em indent on a narrow measure. Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Fabrication validation: PASS.** This section's key check. Visible text scanned for named
  awarding bodies and publications (real ones by name), for "winner of" / "awarded by" /
  "featured in" phrasing, and for **any four-digit year**. Zero matches across all five files. A
  positive count confirms the opposite: 66 template tokens (`YYYY`, `NN`) across the batch, 12 / 8 /
  12 / 8 / 26 per study.
- **Structural-diversity validation: PASS.** Five distinct geometries, five distinct grounds, and
  five distinct data treatments. Checked against `ARC-S01`–`ARC-S08` so no device is reused; in
  particular `005` uses CSS `columns`, which nothing else in the sector does, and `003`'s data table
  is a different structure from `ARC-S06-005`'s two-dimensional programme.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- The fabrication constraint is the substantive story of this batch and should be read before any
  of these studies is filled. In particular: the `002` tear-sheet slot is for a page spread, and
  the `003` summary rail counts rows in its own table. Both are easy to repurpose into claims.
- `ARC-S09-005` adds a sixth sector-native register to the sector — bibliographic citation —
  alongside the drawing sheet, the specification clause, the project programme, the monograph
  colophon and the practice register.
- Four of five studies deliberately carry no media slot. That is recorded in the Media Slots table
  as "no media slot by design" so the absence is not read as unfinished work.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
