# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S08`
- Section Name: `Architects & Designers`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S08-001` | Universal / Safe | AUTHORED | `raw/ARC-S08-001.html` |
| `ARC-S08-002` | Premium / Editorial | AUTHORED | `raw/ARC-S08-002.html` |
| `ARC-S08-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S08-003.html` |
| `ARC-S08-004` | Conversion-led | AUTHORED | `raw/ARC-S08-004.html` |
| `ARC-S08-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S08-005.html` |

## Authoring Direction

Nine visual-direction reference images were supplied for a five-study section, so the set was
reduced rather than followed wholesale. Five were selected for being structurally distinct from
each other; four were set aside:

- the testimonial carousel with large quote cards, which is `S12 — Client Testimonials`, not a
  team section;
- the featured-portrait-plus-thumbnail-strip layout, which is also a testimonial pattern;
- the filmstrip in which the active speaker expands and the others compress to slivers, which
  needs JavaScript for an effect the section does not require;
- the team carousel with previous / next controls, because a horizontally scrolled rail with
  paired controls is already carrying `ARC-S03-004` and reusing it here would repeat a device
  across sections.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S08-001` | Reference 3 | Centred bold heading over four equal cards, each with a coloured shape behind the portrait and the name and role banded at the card foot, closed by a centred paragraph |
| `ARC-S08-002` | Reference 2 | Dark pill badge above a large two-line heading, then four portraits on tinted panels rounded at the top, each followed by a role label, a name and a descriptor line |
| `ARC-S08-003` | Reference 9 | Three-by-two grid of captioned portrait tiles beside a two-column directory pairing a round avatar with a name, a description and two small actions |
| `ARC-S08-004` | Reference 1 | Label and heading left with a paragraph opposite, over four dark portrait cards carrying a role and name, each with its own pill action beneath |
| `ARC-S08-005` | Reference 8 | A ruled header row of names above roles sitting directly on a continuous band of portraits with no gaps between them |

### People policy

This is the first section whose content is people, which changes what "placeholder" has to mean.
Three rules were applied to every study:

- **No invented personal names.** Every reference fills its cards with realistic full names
  ("Olivia Smith", "Adam Peacock", "Carter Botosh"). A team section populated with realistic names
  reads as a real roster of real staff, which is exactly the deceptive-evidence case the media
  policy rules out. Names read `Team member NN` throughout.
- **Descriptions describe the post, not the person.** Every descriptor says what that role covers
  — "runs projects on site and answers the queries that come back from the builder" — so a studio
  filling the slots replaces a name and a portrait, not a fabricated biography.
- **No credentials, registrations or social identities.** No professional body, no chartered or
  registered status, no years of experience, no handles or profile URLs. The action links in `003`
  read "Profile" and "Contact" and point nowhere.

Every study also carries a visible statement that the roster is a placeholder — as a closing note
in `001`, as the badge itself in `002`, in the head count line in `003` and `005`, and through the
numbered names everywhere.

## Study Records

### ARC-S08-001 — Universal / Safe

- **Structural intent / archetype:** The standard team row: a centred heading, four equal people,
  name and role under each. The safest and most reusable arrangement in the section.
- **Layout model:** Centred eyebrow and heading over a four-column row. Each card offsets a tint
  block up and to the left behind the portrait using a `::before`, so the portrait sits over
  colour without needing a second image or a cut-out. Name and role sit in a band below.
- **Density:** Medium.
- **Media mode:** Four empty portrait areas, each over an offset tint block.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Four columns → two at 1024px → one at 480px, where the portrait
  re-proportions to 4:3 and the tint block shrinks with it so the offset stays legible rather than
  swallowing the card. Closing note left-aligns at 480px.
- **Composer value:** The default binding target — four repeating items of portrait, name and role
  plus a heading and a closing note. Nothing in the layout depends on a bio, a link or a count.
- **Limitation / content ceiling:** Four people; the row is balanced for four and eight would need
  a second row the design does not describe. Role is one short line. There is no per-person action
  and no bio, so it cannot carry a directory.

### ARC-S08-002 — Premium / Editorial

- **Structural intent / archetype:** The team as an editorial line-up — a badge, a large heading,
  and four portraits presented on their own colour panels with a short descriptor each.
- **Layout model:** A dark pill badge above a display heading, then four cards whose tinted panel
  is rounded heavily at the top and squared at the foot, with an inner portrait area inset inside
  it. Captions run role label, name, descriptor. The ground carries a dot texture drawn with a
  `radial-gradient` — no external asset.
- **Density:** Low-medium.
- **Media mode:** Four empty portrait areas, each inset on its own tinted panel.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Four columns → two at 1024px → one at 480px, where the panel goes 4:3
  and both corner radii step down together so the panel and its inner slot stay concentric.
- **Composer value:** The premium register, and the only study here that gives each person a
  descriptor line as well as a role — useful where the team is the differentiator and each post
  needs a sentence.
- **Limitation / content ceiling:** Four people, one descriptor line each of about fifteen words.
  The panel colour is a strong brand commitment: it is the loudest surface in the section and would
  need retinting for most studio identities.

### ARC-S08-003 — Dense / Information-heavy

- **Structural intent / archetype:** The full team page compressed into one section — a visual
  roster on one side and a readable directory on the other, showing the same six people twice.
- **Layout model:** A ruled head over a `1fr / 1.02fr` body. The left column is a three-by-two grid
  of portrait tiles with name and role captions; the right column is a two-column directory where
  each entry runs a round avatar, a name, a description and two action links.
- **Density:** High — twelve person-entries across six people, the largest content set in the
  section.
- **Media mode:** Six empty portrait tiles plus six empty round avatar slots. The same six people
  appear in both columns, so a filled roster needs one image each used at two crops — recorded
  here because it is easy to mistake for twelve separate slots.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Body stacks at 1024px; portrait tiles square up at 768px; at 480px the
  tile grid goes three columns to two while the directory goes to one, so the roster stays scannable
  while the reading column widens.
- **Composer value:** The highest-capacity option, and the only one that models a person twice —
  once as a face in a roster and once as an entry with a description and contact routes. That maps
  onto how most studio content models actually store people.
- **Limitation / content ceiling:** Six people; a seventh breaks the three-by-two grid. Descriptions
  run to about twenty words. Two actions per entry — a third crowds the row at 1280px.

### ARC-S08-004 — Conversion-led

- **Structural intent / archetype:** A team section that converts per person rather than per
  section. Each card ends in its own action, so the visitor picks who to talk to instead of being
  handed one generic contact button.
- **Layout model:** A split head (heading left, paragraph right) over four dark portrait cards. Each
  card lays a gradient band over the portrait area to carry role and name, and each card is followed
  by its own full-width pill action. A closing foot bar offers a single routed alternative for
  visitors who do not know who to ask for.
- **Density:** Medium.
- **Media mode:** Four empty portrait areas on dark cards.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Head stacks and cards go four → two at 1024px, one at 480px where the
  card goes 4:3 and the foot bar stacks. Action pills are full-width at every size, so the touch
  target never depends on the card width.
- **Composer value:** The conversion register. Per-person actions plus one fallback route is a
  pattern most studio sites want and few team layouts provide; each action carries an `aria-label`
  naming the post, so a filled roster does not need the button text rewritten.
- **Limitation / content ceiling:** Four people. No bio field — the card carries role and name only,
  so the conversion depends on the role being self-explanatory. Cards are dark, which assumes the
  section is not placed on an already dark ground.

### ARC-S08-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The practice register — the ruled roster a studio keeps of who
  holds which post. Closer to a title-block roster than to a marketing team grid, and the only
  layout in the section that reads as a document rather than a display.
- **Layout model:** A monospace head over a six-column register. Each entry uses `display: contents`
  so its caption joins one ruled header band in row one and its portrait joins one uninterrupted
  portrait band in row two, with hairline verticals between captions and no gaps between portraits.
  Explicit `grid-column` assignments per entry keep the two bands in step rather than relying on
  auto-placement. A monospace foot rule closes it.
- **Density:** Medium-high.
- **Media mode:** Six empty portrait cells forming one continuous band.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The register form is deliberately abandoned below 1024px rather than
  compressed: each entry reverts to `display: block` and becomes a self-contained card with its
  caption beneath its own portrait, so a name can never end up above the wrong face. Columns then
  step 3 → 2 → 1.
- **Composer value:** The identity option, and a fifth distinct sector-native register for the
  sector alongside the drawing sheet, the specification clause, the project programme and the
  monograph colophon. Suits practices that publish a roster as a matter of record.
- **Limitation / content ceiling:** Six posts at desktop; the columns are already narrow at six and
  a seventh makes the captions unreadable. Role is one short line. The register look exists only at
  or above 1024px, which is a deliberate trade recorded here — below that it is a conventional card
  grid.

## Research Metadata

- **Sources:** Nine visual-direction reference images supplied with the authoring request; five
  used, four set aside for the reasons listed under Authoring Direction.
- **Research date:** 2026-08-30
- **Structural territory rationale:** Each selected reference was assigned to the territory its
  topology already served — the plain four-card row to Universal, the badge-and-panel line-up to
  Premium, the roster-plus-directory to Dense, the per-person action row to Conversion-led, and the
  ruled register band to Sector-native.
- **Differentiation notes:** Five distinct geometries — a tint-offset card row, tinted panels with
  captions, a tile grid beside a directory, dark cards with per-person actions, and a two-band ruled
  register. Person counts differ (4 / 4 / 6 / 4 / 6). Grounds differ: white, dotted light warm,
  near-white, warm light with dark cards, and paper. Only one study is dark-carded, only one has a
  textured ground, only one uses monospace, only one has per-person actions, and only one shows the
  same person twice. No study uses JavaScript.
- **Sector-interpretation note:** The references come from property, events, corporate and education
  marketing, and all of them lead with named individuals and personal credibility. That is the part
  that could not be carried across: see the people policy above.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, and no
  inline SVG anywhere in this batch. The `002` dot texture is a `radial-gradient`, not an image.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| Portrait ×4 | `ARC-S08-001` | One portrait per person, over an offset tint block | Still portrait, 3:4 (4:5 at 768px, 4:3 at 480px) | Labelled empty area; name and role sit outside the portrait so the card reads with no image. |
| Portrait ×4 | `ARC-S08-002` | One portrait per person, inset on a tinted panel | Still portrait, 3:4 (4:5 at 768px, 4:3 at 480px) | Slot label is white on the panel tone, measured at 4.67:1; captions sit below the panel. |
| Tile ×6 + avatar ×6 | `ARC-S08-003` | Six people shown twice — as roster tiles and as directory avatars | Still portrait, 3:4 for tiles; square crop for the 34px avatars | **Six people, not twelve**: one image each, used at two crops. Avatars are decorative and `aria-hidden`; the name beside them carries the identity. |
| Portrait ×4 | `ARC-S08-004` | One portrait per dark card, behind the name band | Still portrait, 3:4 (4:5 at 768px, 4:3 at 480px) | The band carries its own gradient, so role and name stay legible over any replacement portrait. |
| Portrait ×6 | `ARC-S08-005` | Six portraits forming one continuous band | Still portrait, 3:4 (4:3 at 480px) | Portraits are separated only by a hairline in the paper tone; a filled band needs consistent crops and tone to read as one register. |

No study contains a photograph of a person, a name of a real person, a logo, a client mark, or any
fabricated evidence. Licensing and provenance metadata is not applicable to this batch because no
third-party asset is referenced; it becomes required if these slots are filled — and for portraits
specifically, filling them means using images of people who have consented to appear.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S08-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps — `003` runs
  h1 / h2 for the roster tiles / h3 for the directory entries, which is the only three-level study
  in the sector. Every `aria-labelledby` reference resolves; every `<a>` carries an `href`; each
  per-person action in `004` carries an `aria-label` naming the post rather than relying on
  "Talk with 01" alone; decorative avatars in `003` are `aria-hidden`. Visible `:focus-visible`
  styling in all five, with an amber ring inside the dark cards, and a `prefers-reduced-motion`
  block in all five. Contrast measured on 22 text and UI colour pairs against each study's own
  ground: all text ≥ 4.5:1 and all interactive borders ≥ 3:1 (lowest 3.43:1). The `002` portrait
  slot label initially measured 4.21:1 on the panel tone and the panel was darkened to bring it to
  4.67:1 before sign-off.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** Every
  study defines the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder. Grid children use
  `minmax(0, …)`, type and spacing use `clamp()`. The `005` register is the notable case: rather
  than compressing six ruled columns onto a phone, each entry reverts to a self-contained card, so
  a caption can never be separated from its own portrait — the failure mode that a two-band layout
  invites. No horizontal scroll anywhere. Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Copy-policy validation: PASS.** Visible text scanned for awards, certifications,
  accreditations, named professional bodies, chartered or registered status, licences, degrees,
  years of experience, ratings, testimonial language, and social handles or profile URLs. Zero
  matches. A separate count confirms every person reference in the batch is a numbered placeholder:
  4 / 4 / 12 / 4 / 6 across the five studies.
- **Structural-diversity validation: PASS.** Five distinct geometries, five distinct grounds, and
  five distinct person counts and treatments. Checked against the sector's earlier sections so no
  device is reused; the scroll rail with paired controls was specifically declined for that reason.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- `ARC-S08-005` uses `display: contents` on each register entry so one list produces two aligned
  bands. Modern browsers expose list semantics correctly for this; and because the technique is
  switched off below 1024px, the small-screen rendering never depends on it.
- `ARC-S08-003` is the only study in the sector so far to use three heading levels, because its
  roster and its directory are two parallel lists of the same six people.
- The people policy above is the substantive difference between these studies and their references
  and should be read before any of these slots are filled. Filling a portrait slot means using an
  image of a person who has consented to appear in it.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
