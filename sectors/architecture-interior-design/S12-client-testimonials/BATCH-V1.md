# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S12`
- Section Name: `Client Testimonials`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S12-001` | Universal / Safe | AUTHORED | `raw/ARC-S12-001.html` |
| `ARC-S12-002` | Premium / Editorial | AUTHORED | `raw/ARC-S12-002.html` |
| `ARC-S12-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S12-003.html` |
| `ARC-S12-004` | Conversion-led | AUTHORED | `raw/ARC-S12-004.html` |
| `ARC-S12-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S12-005.html` |

## Authoring Direction

Five visual-direction reference images were supplied. Each study follows the topology of one,
retargeted from software, sport and wellness marketing to an architecture and interior practice.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S12-001` | Reference 5 | Centred pill and serif heading, a tall image card carrying an overlaid quote, and a two-by-two grid of quote cards beside it |
| `ARC-S12-002` | Reference 2 | Oversized display word set hard right, a bracketed label joined to it by a rule with a node, and a portrait beside one large quote panel with attribution bottom-left and controls bottom-right |
| `ARC-S12-003` | Reference 1 | Numbered pill above a centred heading, then a wall of quote cards at mixed heights with dark feature cards set among them |
| `ARC-S12-004` | Reference 4 | Eyebrow above a two-line heading, then a row of quote cards in which one is a dark image card, attributions set as signatures beneath each quote |
| `ARC-S12-005` | Reference 3 | A left column with a small image, a pill label, a large heading and a forward control, beside stacked cards carrying a quote and the name, organisation and address of the person who gave it |

### Section placement

The references were supplied against `S13 — Featured Project Case Study`. All five are
testimonial layouts, and this sector already has `S12 — Client Testimonials`, so the mismatch was
raised before authoring and the section was confirmed as `S12`. `S13` is untouched and remains
`NOT_STARTED`.

### The claim problem

This section's content **is** third-party evidence, which puts it in the same class as `ARC-S09`.
A testimonial section filled with realistic names, companies and figures is not a placeholder: it
is fabricated evidence, and it is the single most likely content type to be pasted into a live
site unchanged because it reads as finished. The approach was confirmed before authoring and is
applied throughout:

- **Quotes say what they are.** Every quote opens by naming itself a placeholder and then runs to
  the length a real quote would, so the layout is genuinely exercised without a sentence of it
  being usable as a claim.
- **Attributions are tokens.** `Client placeholder 01`, `Signatory placeholder 02`, plus a
  relationship and a project type. No person, company, organisation or project is named.
- **No ratings and no figures.** The references carry five-star rows, percentages, hours saved and
  ROI statements. None survives. A QA scan for star language, percentages, `N+` patterns, ROI,
  time-saved phrasing, company suffixes and four-digit years returns nothing across the batch,
  including the four quotes held inside the `002` script.
- **Permission is stated, not assumed.** `004` and `005` both say references are released with the
  client's permission, because that is the condition a real practice is under.

This is consistent with how the sector has handled the material elsewhere: `ARC-S05-004` replaced
a reference testimonial with an unattributed studio principle, and `ARC-S08` declined two
testimonial-pattern references and recorded that they belonged to this section.

## Study Records

### ARC-S12-001 — Universal / Safe

- **Structural intent / archetype:** One quote given weight over an image, with four more beside
  it. The most reusable arrangement in the section.
- **Layout model:** Centred pill and serif heading over a `0.82fr / 1.35fr` body — a tall featured
  card whose gradient band carries an overlaid quote and attribution, beside a two-by-two grid of
  quote cards.
- **Density:** Medium. Five quotes.
- **Media mode:** One tall empty media area behind the featured quote, plus five empty round
  attribution slots.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Body stacks at 1024px where the featured card re-proportions from a
  `min-height` to 16:10, then 4:3 at 768px; the grid goes single-column at 480px where the head
  also left-aligns, because a centred heading over a single column reads as a mistake.
- **Composer value:** The safest binding target — five records of `{quote, attribution, relationship}`
  with one flagged as featured, plus one media slot. Nothing depends on a rating or a figure.
- **Limitation / content ceiling:** Four grid quotes plus one featured. Quote lengths must stay
  within roughly a 20–45 word band or the two-by-two grid goes visibly uneven; the study
  deliberately ships with one short, one medium and one long quote so that limit is visible.

### ARC-S12-002 — Premium / Editorial

- **Structural intent / archetype:** One quote at a time, given the whole panel, with the section
  title treated as a display word rather than a label.
- **Layout model:** A three-track head — bracketed label, a rule with a centred node, and the
  display word set hard right — over a `0.46fr / 1.4fr` body pairing a tall portrait with a single
  quote panel whose attribution sits bottom-left and controls bottom-right.
- **Density:** Low. One quote visible; five held.
- **Media mode:** One tall empty portrait area.
- **Interaction:** Vanilla JavaScript, about fifty-five lines. **A stepper, not a tab set** — this
  is deliberately not the ARIA tab pattern already used by `ARC-S04-005` and `ARC-S08-007`, and
  not the scroll rail used by `ARC-S03-004`, `ARC-S08-008` and `ARC-S08-009`. Two controls move
  through five quotes, a monospace readout states the position (`02 / 05`), and each change is
  announced in a `role="status"` live region. Controls disable at each end and hand focus to the
  opposite control when the pressed one becomes disabled. The five quotes are held in script
  rather than as five hidden panels: only one is ever shown, so five copies in the DOM would be
  four extra things for a screen reader to walk past. With the script blocked, the first quote and
  its attribution remain fully readable.
- **Responsive strategy:** The head cannot hold a label and a display word on one line below 768px,
  so the rule is dropped and the word left-aligns rather than shrinking further; the portrait
  becomes 16:10 and then 4:3, and the panel foot stacks at 480px.
- **Composer value:** The premium register, and the only study here that shows one quote at a time
  — which suits a practice with a small number of strong references rather than a wall of them.
- **Limitation / content ceiling:** Five quotes is the tested count; the readout is two-digit so it
  scales to 99, but a set beyond about eight makes stepping tedious with no overview. Quotes run to
  roughly 60 words before the panel outgrows the portrait beside it.

### ARC-S12-003 — Dense / Information-heavy

- **Structural intent / archetype:** A wall. The argument is the volume and the unevenness — many
  clients, different lengths, different projects — with two project references set among them.
- **Layout model:** Centred numbered pill and heading over a three-column CSS multi-column flow.
  Six quote cards at natural heights and two dark feature cards, each feature card carrying a
  media area, a project tag and a project record heading.
- **Density:** High — eight cards, the largest set in the section.
- **Media mode:** Two empty media areas inside the feature cards, plus eight empty round
  attribution slots.
- **Interaction:** None. No `<script>` element. The wall is a `columns` flow rather than a grid, so
  cards keep their source order in the DOM regardless of how they pack visually.
- **Responsive strategy:** Three columns → two at 1024px → one at 480px, where the head also
  left-aligns. Feature cards swap their `min-height` for a 4:3 ratio at 768px.
- **Composer value:** The highest-capacity option, and the only one that mixes quotes with project
  references in a single flow — useful where the practice wants the section to carry both.
- **Limitation / content ceiling:** Eight cards is the tested shape. A wall needs at least two
  columns to read as a wall, so below 480px it is honestly just a stack. Quote lengths must vary or
  the columns resolve flat and the device is wasted; the study ships with one-paragraph and
  two-paragraph cards for that reason.
- **Policy note:** the reference's feature cards carry a play control and an outcome headline, and
  its quote cards carry figures. No play control, no outcome headline and no figure appears here.

### ARC-S12-004 — Conversion-led

- **Structural intent / archetype:** Three references and a way to ask for the rest. The conversion
  is the fourth cell of the same row, so it reads as part of the set rather than as a banner.
- **Layout model:** Eyebrow and two-line heading over a four-cell row: two light quote cards, one
  dark card carrying a media area with the quote over a gradient, and an inverted conversion cell
  with a count line, a heading, a filled action and a text link.
- **Density:** Medium.
- **Media mode:** One empty media area inside the dark quote card.
- **Interaction:** None. No `<script>` element. The reference's row bleeds off the page edge to
  imply more cards; here the row is a fixed four-cell grid whose last cell states how many
  references exist and links to them. The same signal, without a fourth scroll container in the
  sector.
- **Responsive strategy:** Four cells → two at 1024px → one at 480px; the dark card goes 4:5 at
  768px and 4:3 at 480px, and the secondary link stretches rather than staying centred.
- **Composer value:** The conversion register. The count line and the request action are a
  content-model pair — `{shown, total, request route}` — that most testimonial sections lack.
- **Limitation / content ceiling:** Three quotes and one conversion cell. Quotes run to about 30
  words before the row goes uneven. The conversion cell states no response time and no outcome, so
  a studio must add its own terms.

### ARC-S12-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The client reference, not the marketing quote. A practice asks
  a past client for a written statement and encloses it with a competition entry, a
  prequalification return or a new appointment. That document is attributable and expected to be
  followed up, which is what separates it from a line lifted out of an email.
- **Layout model:** A bordered sheet with a `0.62fr / 1.5fr` grid. The head column runs a small
  plate, an annex tag, a heading and two short notes. The record column is a stack of bordered
  reference records, each with a keyed header row (`[REF-01]`, project, an "On request" stamp), a
  relationship pair, the statement, and a signature foot with a dated token.
- **Density:** Medium-high. Three full records.
- **Media mode:** One small empty plate in the head column. The records carry no imagery — a
  written reference is a document, and a photograph beside it adds nothing checkable.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The grid stacks at 1024px with the plate capped at 320px; the record
  header drops its stamp to its own line at 768px rather than crushing the project reference; the
  relationship pair and signature foot both go single-column at 480px.
- **Composer value:** The identity option, and a ninth distinct sector-native register for the
  sector alongside the drawing sheet, specification clause, project programme, colophon, practice
  register, bibliography, schedule of services and build-up. Its content model —
  `{key, project, relationship, statement, signatory, role, date, release status}` — is the
  strongest in the section, because a reference that can be followed up is worth more than a quote
  that cannot.
- **Limitation / content ceiling:** Three records before the sheet outgrows a screen; statements run
  to about 60 words. The register reads as formal and will suit a practice that tenders more than
  one that sells. Every field is a token and every date reads `YYYY`.

## Research Metadata

- **Sources:** Five visual-direction reference images supplied with the authoring request.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five ways a practice shows
  client feedback — one featured quote with a supporting grid for the general case, a single
  stepped quote for the premium case, a wall for the dense case, three quotes and a request for the
  conversion case, and the written client reference for the discipline-native case.
- **Differentiation notes:** Five distinct geometries — featured card plus two-by-two grid, display
  word with a single stepped panel, a multi-column wall, a four-cell row with an inverted
  conversion cell, and a keyed record sheet. Quote counts differ (5 / 5 stepped / 6 / 3 / 3).
  Grounds differ: warm off-white, near-white, light grey, warm with dark cards, and paper. Only one
  uses script, and it uses a stepper rather than repeating the sector's tab or rail patterns.
- **Sector-interpretation note:** The references come from software, sport and wellness marketing,
  where testimonial sections lead with figures and ratings. None of that survives; what replaces it
  is labelled placeholder text and, in `005`, the document form the material actually takes in
  architecture.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, no inline
  SVG, and no inline `style` attribute in any of the five files.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: One of five. `ARC-S12-002` needs it to step through quotes and announce the
  change; the other four contain no `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Featured area | `ARC-S12-001` | One image behind the featured quote | Still image, tall (16:10 at 1024px, 4:3 at 768px) | Gradient band already present, so the overlaid quote keeps contrast over any replacement image. |
| Attribution slot ×5 | `ARC-S12-001` | Small round portrait beside each name | Square crop, 34px | Decorative and `aria-hidden`; the name beside it carries the identity, and the card reads with the slot empty. |
| Portrait | `ARC-S12-002` | One portrait beside the quote panel | Still image, tall (16:10 at 768px, 4:3 at 480px) | Labelled empty area; the panel is independent of it. |
| Feature area ×2 | `ARC-S12-003` | Project image behind each dark feature card | Still image, tall (4:3 at 768px) | Gradient band present; the project tag and heading are page text. |
| Attribution slot ×6 | `ARC-S12-003` | Small round portrait per quote card | Square crop, 34px | Decorative and `aria-hidden`. |
| Dark card area | `ARC-S12-004` | Image behind the quote on the dark card | Still image, tall (4:5 at 768px, 4:3 at 480px) | Gradient band present; quote and signature stay legible over any image. |
| Head plate | `ARC-S12-005` | One small plate in the sheet head column | Still image, 4:3 (16:10 at 480px) | Labelled empty area; the records carry no imagery by design. |

Filling any attribution or portrait slot means using an image of a real person who has consented
to appear, alongside a quote that person actually gave with permission to publish it.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S12-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting and unique-id
  checks pass on all five. All CSS is namespaced to the study root class; a scan for unscoped rules
  and for inline `style` attributes returns zero across the batch. One inline style used for the
  `002` live region was moved into the scoped stylesheet before sign-off.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps. Every quote
  is a real `<blockquote>` paired with an attribution element — verified by count, five files, one
  attribution per quote. In `002` both controls carry an `aria-label`, the position is stated in
  text as well as by control state, and each change is announced in a `role="status"` polite live
  region. Decorative attribution slots and quotation glyphs are `aria-hidden`. Visible
  `:focus-visible` styling in all five, with an amber ring inside dark cards, and a
  `prefers-reduced-motion` block in all five. Contrast measured on 32 pairs against each study's own
  ground: all text ≥ 4.5:1 (lowest 6.30:1) and all interactive borders ≥ 3:1 (lowest 3.53:1).
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder. Two layouts change behaviour rather than
  shrinking: `002` drops its head rule and left-aligns the display word at 768px instead of
  compressing a three-track head, and `005` moves the record stamp onto its own line rather than
  crushing the project reference. No horizontal scroll anywhere. Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs, `@import`,
  `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity` and `crossorigin`.
  Zero matches across all five files; the only `<script>` is the inline block in `002`.
- **Evidence-policy validation: PASS — the key check for this section.** Visible text scanned for
  star and rating language, percentages, `N+` patterns, ROI and time-saved phrasing, company
  suffixes (Ltd, LLC, Inc, GmbH, Co.), award and certification language, and any four-digit year.
  Zero matches. The four quotes held inside the `002` script were scanned separately and are also
  clean. A positive count confirms the opposite: 61 explicit "placeholder" mentions across the
  batch, with every quote self-labelled and every attribution a token.
- **Structural-diversity validation: PASS.** Five distinct geometries, checked against the sector's
  earlier studies by their recorded `layout-model` and `interaction` metadata. `002` specifically
  uses a stepper rather than reusing the tab set or the scroll rail already in the sector, and `004`
  uses a fixed row rather than becoming a fourth rail.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- The section placement decision is recorded under Authoring Direction: the references arrived
  against `S13`, all five are testimonial layouts, and `S12` was confirmed as the correct home.
  `S13 — Featured Project Case Study` remains `NOT_STARTED` and untouched.
- The evidence policy above should be read before any of these studies is filled. The three places
  it bites hardest: the attribution tokens, which must become a real named person only with their
  permission; the `004` count line, which states how many references exist and must match reality;
  and the `005` record fields, which are the ones a reader would expect to be able to follow up.
- `ARC-S12-005` adds a ninth sector-native register to the sector — the client reference record.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
