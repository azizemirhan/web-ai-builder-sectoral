# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S22`
- Section Name: `Breadcrumb / Context Navigation`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S22-001` | Universal / Safe | AUTHORED | `raw/ARC-S22-001.html` |
| `ARC-S22-002` | Premium / Editorial | AUTHORED | `raw/ARC-S22-002.html` |
| `ARC-S22-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S22-003.html` |
| `ARC-S22-004` | Conversion-led | AUTHORED | `raw/ARC-S22-004.html` |
| `ARC-S22-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S22-005.html` |

## Authoring Direction

**No reference images were supplied.** Like `ARC-S21`, this batch was authored against the section
README written during the catalog extension rather than to a blank brief.

This is the only section in the catalog whose subject is **semantics**. Its README says so
directly — *"this role is semantic navigation, not decoration"* — and lists three requirements that
shaped every study: a real navigation landmark with an accessible name, the current page marked
programmatically rather than by styling alone, and a trail that stays keyboard reachable in a
sensible order. A fourth rule governs the responsive work: *"A trail must never be silently
truncated on small screens without a way to reach the hidden levels."*

### What that produced

- **No media in any study.** The README puts it plainly: navigation, not presentation. This is the
  only section in the sector where every single study carries no slot at all.
- **The current page is never a link, in any study.** It is a `<span>` carrying
  `aria-current="page"`. A QA scan confirms zero `<a aria-current>` across the batch.
- **Separators are generated in CSS**, so they never enter an accessible name or a copied selection,
  and they are `aria-hidden` by construction rather than by attribute.
- **Every state is marked at least twice.** The current sibling in `003` is filled *and* weighted
  *and* `aria-current`; the current cell in `005` is filled *and* glyphed *and* `aria-current`. A
  locator that communicates position by fill alone locates nothing for a visitor who cannot see it.
- **Nothing is ever hidden to fit.** `001`, `002` and `004` wrap; `003` converts its five-level
  trail into a labelled scroll region with its own tab stop; `005` moves the key plan below the
  trail. No study truncates, ellipsises or drops a level.

### The boundary with S21

A page's in-page contents list lives in `ARC-S21-003`, because it describes the inside of the page.
Position within the site lives here. `ARC-S21-005` states the page's position in *words*;
`ARC-S22-005` *shows* it. Both studies say so in their own closing note.

## Study Records

### ARC-S22-001 — Universal / Safe

- **Structural intent / archetype:** The plain trail. Four levels, wrapping, on a rule.
- **Layout model:** A small "You are here" heading, then a `<nav>` labelled by it containing an
  `<ol>` of four items; separators drawn with a CSS `content: "/"`.
- **Density:** Low.
- **Media mode:** NONE.
- **Interaction:** Links only.
- **Responsive strategy:** Wrapping is the entire strategy. Separator padding tightens at 768px and
  360px; link targets relax from 44px to 40px at 480px. No level is ever removed.
- **Composer value:** The safest binding target — an ordered `{label, href}` collection with the
  last item flagged current. Nothing else.
- **Limitation / content ceiling:** Four to five levels before wrapping produces three lines on a
  phone; `003` carries the pattern for deeper trails.

### ARC-S22-002 — Premium / Editorial

- **Structural intent / archetype:** The ancestry set small and quiet, with the way back out as the
  one weighted element on the row.
- **Layout model:** A `1fr / auto` row: a monospace uppercase trail with em-dash separators on the
  left, and a separate single-link navigation returning to the parent on the right.
- **Density:** Low.
- **Media mode:** NONE.
- **Interaction:** Links only.
- **Responsive strategy:** At 768px the parent return moves **above** the trail via `order: -1` —
  the way out is what a lost visitor reaches for first, so it should not be the last thing on the
  row.
- **Composer value:** The premium register, and the only study that separates position from action
  into two landmarks. A screen-reader user can skip one without losing the other.
- **Limitation / content ceiling:** The uppercase monospace trail is slow to read past four levels;
  it is a register choice, not a general-purpose trail.

### ARC-S22-003 — Dense / Information-heavy

- **Structural intent / archetype:** The full context bar: where you are, what else is at this
  level, and what is inside this page.
- **Layout model:** A five-level trail on a rule, then a `1.15fr / 1fr` local navigation pairing a
  wrapping sibling chip list with a two-column in-page contents list. Three landmarks, three
  accessible names.
- **Density:** High — the most a context bar can carry before it becomes the site's primary
  navigation, which the README puts out of scope.
- **Media mode:** NONE.
- **Interaction:** Links only.
- **Responsive strategy:** The notable decision: at 768px the trail stops wrapping and becomes a
  labelled `role="region"` with `tabindex="0"` and `flex-wrap: nowrap`, so a five-level trail
  scrolls horizontally instead of occupying four lines — the README's "scrolling with a visible
  affordance" option, with every level still keyboard reachable.
- **Composer value:** The highest-capacity option, and the only one modelling siblings and page
  contents together. Suits deep detail pages in `S23`–`S27`.
- **Limitation / content ceiling:** Five trail levels, six siblings, six contents entries. More
  siblings and the chip list becomes the page's main navigation.

### ARC-S22-004 — Conversion-led

- **Structural intent / archetype:** Conversion in a navigation section is **movement**, not a
  pitch. A pager keeps a visitor inside the work instead of sending them back to an index.
- **Layout model:** A three-level trail above a `1fr / auto / 1fr` pager: previous and next pages as
  bordered cards naming their destination in full, with a single filled contextual link between
  them.
- **Density:** Medium.
- **Media mode:** NONE.
- **Interaction:** Links only. The pager is two ordinary links, not a control — it moves between
  pages rather than changing state on this one.
- **Responsive strategy:** At 768px previous and next keep the row and the contextual link takes its
  own full-width line beneath, so the two directions stay side by side and readable as a pair; at
  480px they stack and the "next" card left-aligns.
- **Composer value:** The conversion register. Its content model is
  `{previous page, next page, one contextual link}`, which most breadcrumb components lack entirely.
- **Limitation / content ceiling:** One link per direction and one contextual link. **Each pager
  link names its destination in full** rather than saying only "previous" and "next" — that is the
  failure mode of every pager, and the direction word is marked up separately from the page name so
  each link is meaningful out of context.

### ARC-S22-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The key plan. Every drawing in a set carries a small diagram of
  the whole with the part this sheet covers picked out, so a reader who opens one sheet knows where
  it sits. That is exactly this section's job.
- **Layout model:** A bordered sheet with a `1fr / auto` grid: a monospace sheet-reference trail and
  a three-part reference line on the left, and a bordered key-plan block on the right holding a
  nine-cell grid of links with the current cell marked, plus a legend.
- **Density:** Medium.
- **Media mode:** NONE. The key plan is drawn from list items and borders, and it is navigation
  rather than illustration.
- **Interaction:** Links only.
- **Responsive strategy:** At 768px the key plan moves below the trail rather than shrinking — a
  locator that cannot be read locates nothing — and every cell keeps a 44px target at every width;
  at 480px the grid becomes `repeat(auto-fill, minmax(44px, 1fr))` so it fills the measure without
  going below the target.
- **Composer value:** The identity option, and a thirteenth sector-native register for the sector.
  Its content model is `{set, sheet position, total sheets, sibling links}`, which is a real
  navigational structure rather than a decorative one.
- **Limitation / content ceiling:** Nine cells at three columns is the tested shape; a set past
  about sixteen sheets stops being legible as a diagram. The register suits document-like sections
  and will read as technical elsewhere.

## Research Metadata

- **Sources:** None. Authored against the section README written during the catalog extension.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five things a context bar can
  do — state position plainly, offer a quiet way back, carry the full local context, move between
  siblings, and locate the page within its set.
- **Differentiation notes:** Five distinct geometries and, unusually, five distinct *separator and
  state treatments*: slash, em dash, chevron with filled chips, named pager cards, and a filled key
  cell. Grounds differ: near-white, warm off-white, cool grey, warm light, and paper. No study uses
  JavaScript and none carries media.
- **Sector-interpretation note:** This section is judged on semantics rather than composition, so
  the QA below carries a navigation-semantics check that the other sections do not need.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `@import`, `url()`, webfont, inline SVG, or inline
  `style` attribute in any of the five files.
- Network calls: NONE. Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| — | all five | **No media slot in any study, by design** | — | The section README states the role is navigation, not presentation. This is the only section in the sector with no media slot anywhere. |

## QA

- **ID validation: PASS.** Five IDs, each with matching `<meta name="study-id">`, `data-study-id`,
  scoped root class and filename; every element `id` namespaced.
- **Raw-format validation: PASS.** Tag balance, nesting and unique-id checks pass on all five;
  unscoped-CSS and inline-`style` scans both return zero.
- **Navigation-semantics QA: PASS — the key check for this section.** Measured across all five:
  every trail is a `<nav>` landmark with an accessible name (2, 2, 3, 2 and 2 landmarks per study,
  each named); every trail is an `<ol>` because a trail has an order; `aria-current="page"` is
  present in every study; and **zero** current-page items are links. Separators are CSS-generated
  and never enter an accessible name. Every state is signalled at least twice — never by fill or
  weight alone.
- **Accessibility QA: PASS.** One `<h1>` per study — a visible "You are here" label, which is real
  orientation text rather than a hidden heading — no heading jumps, every `aria-labelledby`
  resolving, every `<a>` carrying an `href`, visible `:focus-visible` in all five with a small
  border radius so the ring follows inline links, and a `prefers-reduced-motion` block in all five.
  Contrast measured on 13 pairs: all text ≥ 4.5:1 and all interactive borders ≥ 3:1. **Separator
  glyphs were treated as text, not as decoration:** they initially measured 3.53:1 and 3.55:1 and
  all five were given a dedicated `--sep` token at 4.8–4.9:1 before sign-off, so the batch has no
  sub-4.5 visible character anywhere.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder. Three studies change behaviour rather than
  shrinking: `002` re-orders the parent return above the trail, `003` converts its trail into a
  labelled keyboard-scrollable region, and `005` moves the key plan below the trail. **No study
  truncates, ellipsises, collapses or hides a level at any width**, which is the README's explicit
  prohibition.
- **Dependency validation: PASS.** Zero matches across all five files.
- **Role-compliance validation: PASS.** No study carries a page title, an introduction, primary site
  navigation, footer navigation or a sitemap listing — all four are out of scope per the README.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- This is the only section in the catalog authored primarily against an accessibility contract
  rather than a visual one. The navigation-semantics check above should be re-run on any variant
  added later.
- The separator decision is worth keeping: a breadcrumb separator is visible text, so it was held to
  the 4.5:1 text threshold rather than the 3:1 non-text threshold, even though it is decorative and
  hidden from assistive technology.
- `ARC-S22-005` adds a thirteenth sector-native register — the key plan.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
