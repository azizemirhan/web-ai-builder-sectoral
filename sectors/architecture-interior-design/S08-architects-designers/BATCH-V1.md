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
| `ARC-S08-006` | Extended — Featured member with thumbnail strip | AUTHORED | `raw/ARC-S08-006.html` |
| `ARC-S08-007` | Extended — Expanding filmstrip | AUTHORED | `raw/ARC-S08-007.html` |
| `ARC-S08-008` | Extended — Edge-bleeding card row | AUTHORED | `raw/ARC-S08-008.html` |
| `ARC-S08-009` | Extended — Lead card with buttoned rail | AUTHORED | `raw/ARC-S08-009.html` |

## Authoring Direction

Nine visual-direction reference images were supplied. **All nine are realised**: five as the
default territories `001`–`005`, and four as extension variants `006`–`009`.

The first pass authored only five and set four aside on the grounds that two were testimonial
patterns, one needed script for an effect the section did not require, and one would repeat the
scroll-rail device already carrying `ARC-S03-004`. That was a scoping decision, and it was
overruled: the direction is that every supplied reference is realised. The four were then authored
as `006`–`009`.

`standards/01-AUTHORING-STANDARD.md` permits variants 006–010 only where a structural territory is
genuinely missing, so each extension is recorded against that test in its own study record below.
All four clear it — each is a topology absent from `001`–`005`. Two of them do reuse an interaction
pattern from elsewhere in the sector, and that is stated rather than hidden: `007` uses the ARIA tab
set already used by `ARC-S04-005`, and `009` uses the buttoned scroll rail already used by
`ARC-S03-004`. In both cases the reference's identity *is* that interaction, so realising the
reference means realising the pattern. `008` deliberately does **not** add buttons to its rail —
native scrolling already does the job there — which keeps `008` and `009` structurally apart
rather than making them two coats of paint on one idea.

The section now holds nine studies against a default target of five. Whether all nine survive is a
Design Lab review decision and is not taken in this workspace.

| Study | Reference | Topology taken from the reference |
| --- | --- | --- |
| `ARC-S08-001` | Reference 3 | Centred bold heading over four equal cards, each with a coloured shape behind the portrait and the name and role banded at the card foot, closed by a centred paragraph |
| `ARC-S08-002` | Reference 2 | Dark pill badge above a large two-line heading, then four portraits on tinted panels rounded at the top, each followed by a role label, a name and a descriptor line |
| `ARC-S08-003` | Reference 9 | Three-by-two grid of captioned portrait tiles beside a two-column directory pairing a round avatar with a name, a description and two small actions |
| `ARC-S08-004` | Reference 1 | Label and heading left with a paragraph opposite, over four dark portrait cards carrying a role and name, each with its own pill action beneath |
| `ARC-S08-005` | Reference 8 | A ruled header row of names above roles sitting directly on a continuous band of portraits with no gaps between them |
| `ARC-S08-006` | Reference 4 | Centred two-line bold heading, a large portrait with a statement, a rule, and a name and role beside it, over a strip of smaller portraits |
| `ARC-S08-007` | Reference 5 | Heading and paragraph with previous / next controls, above a filmstrip where the selected person occupies a wide panel and the rest compress to slivers |
| `ARC-S08-008` | Reference 6 | Pill label, large heading, paragraph and action opposite, round controls, and a row of tall cards bleeding off both edges with text set over each image |
| `ARC-S08-009` | Reference 7 | Uppercase tag above a two-line heading with round controls opposite, then a row opening on a filled colour card with contact links, followed by portrait cards captioned over the image |

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

### ARC-S08-006 — Extended / Featured member with thumbnail strip

- **Extension test:** the only study in the section that singles one person out at large scale and
  reduces the rest to a strip. `001`–`005` all treat every person equally.
- **Structural intent / archetype:** One person given the weight of a statement, with the rest of
  the roster present but secondary — the arrangement for a studio where a named principal is the
  first point of contact.
- **Layout model:** A centred bold heading over a `0.72fr / 1fr` featured block — a 4:5 portrait
  beside a label, a statement, a short rule and the name and role. A four-item thumbnail strip
  follows under its own label.
- **Density:** Medium. Five people.
- **Media mode:** One large empty portrait plus four empty thumbnails.
- **Interaction:** None. The reference implies a selector — clicking a thumbnail swaps the featured
  person — but here the thumbnails are links to individual pages, so nothing depends on script.
- **Responsive strategy:** Featured block stacks at 1024px with the portrait capped at 380px; the
  portrait widens to 16:10 at 768px where the strip halves to two columns; single column at 480px.
- **Composer value:** The only layout here with a `featured` flag and a long-form statement field.
  Useful where one post carries the relationship and the others are supporting.
- **Limitation / content ceiling:** One featured person and four in the strip. The statement runs to
  about thirty-five words. Because the featured slot is fixed in markup, rotating who is featured is
  a content edit, not a setting.
- **Policy note:** the reference sets a five-star rating above its quote. Ratings are third-party
  evidence, so no rating appears and the statement describes what the post covers.

### ARC-S08-007 — Extended / Expanding filmstrip

- **Extension test:** the only study where selection changes the layout itself — one person expands
  in place while the others compress. Nothing in `001`–`005` has a selected state at all.
- **Structural intent / archetype:** A roster that fits in one band regardless of size, opened one
  person at a time.
- **Layout model:** A white card holding a heading, a lede, right-aligned controls, and a flex
  filmstrip bounded by two heavy rules. Each person is a tab: `clamp(52px, 7vw, 96px)` when
  collapsed, `clamp(200px, 34vw, 420px)` when selected, with the role and name revealed inside the
  expanded panel.
- **Density:** Low-medium on screen, six people in the markup.
- **Media mode:** Six empty portrait cells; one expanded, five slivers.
- **Interaction:** Vanilla JavaScript, about sixty lines — a horizontally laid out ARIA tab set with
  roving `tabindex`, Arrow / Home / End keys, and previous / next controls that step the same
  selection, disable at each end, and hand focus to the opposite control. **Every sliver keeps its
  name and post in a visually hidden span**, so the roster reads in full to assistive technology and
  to search whether or not a panel is expanded — the failure mode this layout invites. The width
  transition is switched off under `prefers-reduced-motion`.
- **Responsive strategy:** The strip becomes horizontally scrollable at 768px and the collapsed and
  expanded widths step down at 768, 480 and 360px, so the expanded panel always keeps a readable
  measure rather than the strip forcing everything narrower.
- **Composer value:** The only layout that scales to a large roster without getting taller. Suits a
  studio with more people than a grid can show at once.
- **Limitation / content ceiling:** Six to eight people before the slivers stop being distinguishable.
  Only role and name fit in the expanded panel — there is no room for a description. Requires
  JavaScript for the expansion, though not for the content.

### ARC-S08-008 — Extended / Edge-bleeding card row

- **Extension test:** the only study whose row runs past both page edges, and the only one where the
  caption sits *over* the portrait rather than beside or beneath it.
- **Structural intent / archetype:** A roster presented as a moving band — the section reads as
  wider than the page, which signals there are more people than are shown.
- **Layout model:** A contained heading block (pill, heading, paragraph, action) above a full-bleed
  flex row with scroll-snap. Each card is a 3:4 portrait with a gradient band carrying a line about
  the post, then a ruled row pairing name and role.
- **Density:** Medium. Six people.
- **Media mode:** Six empty portrait cards with overlaid caption bands.
- **Interaction:** None. The row is a native scroll container with `scroll-snap`, an accessible name
  and its own tab stop, so it works by keyboard, trackpad and touch with no script. The reference's
  round controls are deliberately **not** reproduced — buttons that only duplicate native scrolling
  would add script for nothing, and `009` already carries the buttoned variant.
- **Responsive strategy:** Card width steps from `clamp(230px, 26vw, 330px)` to 62% at 768px and 80%
  at 480px, so a card is always partly cut off at the right edge — which is what tells the reader the
  row scrolls. `scroll-padding-left` keeps snapped cards aligned to the text column, not the viewport.
- **Composer value:** The only layout that puts a sentence about each person over their portrait,
  which suits a roster where what someone works on matters more than their title.
- **Limitation / content ceiling:** The overlaid line runs to about eighteen words before the gradient
  band covers too much of the face. The bleeding row requires the section to control the full page
  width, so it cannot sit inside a narrower container.
- **Policy note:** the reference heads this layout with a client count and sets a testimonial and a
  company logo over each card. Counts, testimonials and third-party marks are all evidence this
  workspace does not author: the heading states no figure, and the overlaid line describes the post.

### ARC-S08-009 — Extended / Lead card with buttoned rail

- **Extension test:** the only study that opens its row with a filled contact card instead of a
  portrait, and the only one whose rail is driven by buttons.
- **Structural intent / archetype:** A roster with an explicit front door — the first cell is not a
  person to look at but a route to reach, and the portraits follow behind it.
- **Layout model:** A tagged heading with round controls opposite, over a scroll-snapping rail. The
  first item is an imageless indigo card carrying name, role, a short line and two contact links;
  the rest are 3:4 portrait cards captioned over a gradient at the foot.
- **Density:** Medium-high. Six people.
- **Media mode:** Five empty portrait cards. The lead card carries **no image by design** — it is a
  contact card, not a portrait.
- **Interaction:** Vanilla JavaScript, about forty lines. Previous / next buttons scroll the rail by
  one card, disable at each end, and hand focus to the opposite control when the pressed one becomes
  disabled. The rail is a labelled scroll region with its own tab stop, so the buttons are an
  enhancement and never the only path. Scrolling honours `prefers-reduced-motion`.
- **Responsive strategy:** Card width steps 24vw → 58% → 78% → 86%; the lead card drops its 3:4 ratio
  for a `min-height` at 480px so its text is never clipped by an aspect ratio it has outgrown.
- **Composer value:** The only layout with a dedicated lead-contact record separate from the roster —
  which is how many studios actually want the section to behave.
- **Limitation / content ceiling:** One lead card and five portraits. The lead card holds about
  twenty-five words plus two links. The indigo fill is a brand assumption and would need retinting.
- **Policy note:** the reference's lead card carries social platform icons. Platform identities are
  accounts this workspace cannot invent, so the links read "Profile" and "Contact" and point nowhere.

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
  Confirmed across all nine files.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: Two of nine. `ARC-S08-007` needs it for the filmstrip's expansion and
  `ARC-S08-009` for its rail controls; in both cases the roster content is fully readable without
  it. The other seven contain no `<script>` element.

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

- **ID validation: PASS.** All five planned IDs exist, plus the four extension variants
  `ARC-S08-006`–`009`, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S08-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Nine standalone `.html` files. Tag balance, nesting, and
  unique-id checks pass on all nine. All CSS is namespaced to the study root class; the only
  unscoped rules are a documented two-line standalone host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study and no heading-level jumps — `003` runs
  h1 / h2 for the roster tiles / h3 for the directory entries, which is the only three-level study
  in the sector. Every `aria-labelledby` reference resolves; every `<a>` carries an `href`; each
  per-person action in `004` carries an `aria-label` naming the post rather than relying on
  "Talk with 01" alone; decorative avatars in `003` are `aria-hidden`. Visible `:focus-visible`
  styling in all nine, with an amber ring inside the dark cards, and a `prefers-reduced-motion`
  block in all nine. Contrast measured on 44 text and UI colour pairs against each study's own
  ground: all text ≥ 4.5:1 and all interactive borders ≥ 3:1 (lowest 3.43:1). Three tones were
  corrected before sign-off: the `002` portrait slot label measured 4.21:1 on its panel and the
  panel was darkened to 4.67:1; the `007` role label measured 3.85:1 on the expanded cell and the
  accent was darkened to 4.61:1; the `009` lead-card body text measured 4.39:1 and was lightened to
  4.77:1.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All nine
  studies define the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder. Grid children use
  `minmax(0, …)`, type and spacing use `clamp()`. The `005` register is the notable case: rather
  than compressing six ruled columns onto a phone, each entry reverts to a self-contained card, so
  a caption can never be separated from its own portrait — the failure mode that a two-band layout
  invites. The two rails in `008` and `009` scroll horizontally by design, are labelled, and carry their own
  tab stop; there is no unintended horizontal scroll. Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`. Zero matches across all nine files; the only `<script>` elements are the two inline
  blocks in `007` and `009`.
- **Copy-policy validation: PASS.** Visible text scanned for awards, certifications,
  accreditations, named professional bodies, chartered or registered status, licences, degrees,
  years of experience, ratings, testimonial language, and social handles or profile URLs. Zero
  matches — including across the four extension variants, whose references carry a star rating, a
  client count, testimonials and named company and platform marks. A separate count confirms every
  person reference in the batch is a numbered placeholder: 4 / 4 / 12 / 4 / 6 / 5 / 12 / 6 / 6, 59
  in total across the nine studies.
- **Structural-diversity validation: PASS.** Nine distinct geometries. Two interaction patterns are
  knowingly reused from elsewhere in the sector — the ARIA tab set in `007` and the buttoned rail in
  `009` — because the references they realise are defined by those interactions; both reuses are
  recorded under Authoring Direction rather than presented as new. `008` and `009` were specifically
  checked against each other: same card row, different heading relationship, different first cell,
  and different scroll mechanism.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- Studies `006`–`009` were added in a second pass so that all nine supplied references are
  realised; the first pass had authored five and set four aside.
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
