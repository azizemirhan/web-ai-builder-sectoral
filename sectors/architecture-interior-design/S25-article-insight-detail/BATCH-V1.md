# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S25`
- Section Name: `Studio Journal / Article Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File | Reference |
| --- | --- | --- | --- | --- |
| `ARC-S25-001` | Universal / Safe | AUTHORED | `raw/ARC-S25-001.html` | Reference 5 |
| `ARC-S25-002` | Premium / Editorial | AUTHORED | `raw/ARC-S25-002.html` | Reference 1 |
| `ARC-S25-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S25-003.html` | Reference 2 |
| `ARC-S25-004` | Conversion-led | AUTHORED | `raw/ARC-S25-004.html` | Reference 3 |
| `ARC-S25-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S25-005.html` | Reference 4 |

## Authoring Direction

**Five reference images were supplied, and the instruction was to follow them directly** — the same
instruction given for `ARC-S01`: reproduce the layout, leave the image areas empty, keep it
responsive. So each study takes one reference and rebuilds its regions in the same order and the
same proportions, rather than abstracting a pattern from it.

### Which reference became which study

Territories were assigned to the references by what each reference actually is, not the other way
round:

- **Reference 5** — agency journal article with a ruled meta column and an author rail — is the
  plainest and most transferable of the five, so it took **001, Universal / Safe**.
- **Reference 1** — magazine sheet on a grey ground, huge centred display headline, interview — is
  the clearest editorial register, so it took **002, Premium / Editorial**.
- **Reference 2** — article between two sidebars, with share row, author box, related posts and
  comments — carries by far the most regions, so it took **003, Dense / Information-heavy**.
- **Reference 3** — pinned meta rail, dark contact card inside the body, oversized related band, and
  a standing action in the bar — is the only reference built around a route out, so it took
  **004, Conversion-led**.
- **Reference 4** — cream arts-magazine page ending in a labelled credits block — held the one
  device that belongs to this sector specifically, so it took **005, Sector-native / Distinctive**.

The fit is honest but not perfect, and the loosest is `004`: the reference is a well-made editorial
page rather than a conversion page, so the territory was met by taking the three routes the
reference already has — the bar action, the card in the body, the related band — and making them one
repeated route rather than by adding sales copy the reference does not contain.

### What was deliberately not reproduced

The section README puts **fabricated authors, publications, dates and citations** out of scope, and
the references are full of exactly those. The substitutions are the same in every study and are
stated on each page in its own closing note:

- Named people become `Author 01`, `Author 02`, `Speaker 01`. No name is invented.
- Dates become `DD Month YYYY`; reading time becomes `NN min`; archive counts become `Month YYYY (NN)`.
- **Reference 1's share count (293) and comment count (17) are removed entirely.** Those are
  invented statistics, and a count is the one thing on an article page that cannot be placeheld
  honestly — a token in that position still reads as a number.
- Platform names and marks in the share rows of references 2, 3 and 5 become neutral routes —
  `Copy link`, `Email`, `Save`, `Share`, `Link`, `Mail`, `More` — so the page does not imply the
  studio holds accounts anywhere.
- Reference 1's play button becomes a **drawn, non-interactive, `aria-hidden` mark** inside the
  media slot. A play control that plays nothing is a fake control; a media-type mark is not.

## Study Records

### ARC-S25-001 — Universal / Safe (reference 5)

- **Structural intent / archetype:** The standard studio-journal article. Back chip, title beside a
  ruled meta column, wide lead image, body with an author-and-share rail, large related block.
- **Layout model:** Head at `1.62fr / 0.38fr` with the meta column behind a left border; body at
  `1fr / 0.3fr` with the rail behind a left border; related at three columns under an oversized
  uppercase heading with a `See all` chip pushed right.
- **Density:** Medium.
- **Media mode:** One `16/9` lead area and three `4/3` related-card areas, all empty.
- **Interaction:** None. Static.
- **Responsive strategy:** Both ruled columns release at 1024px — the meta column becomes a
  three-across definition list above the lead image, the author rail moves under the body behind a
  top rule. Related goes 3 → 2 → 1; the lead image goes `16/9` → `4/3` at 480px.
- **Composer value:** The section's safest binding target:
  `{title, standfirst, date, category, reading_time, lead_media, body[], author, share[], related[]}`.
- **Limitation / content ceiling:** Three related cards and a title of about seventeen characters
  per line at the widest. A longer title pushes the meta column down before 1024px.

### ARC-S25-002 — Premium / Editorial (reference 1)

- **Structural intent / archetype:** The magazine sheet. A white page floating on grey, one narrow
  measure, and a headline large enough to be the whole of the composition.
- **Layout model:** A `1020px` sheet on a grey ground, opening with an `18px` band; a bar at
  `1fr / 1.6fr / 1fr` carrying publication, article title and actions; a `3/2` film area with a
  drawn play mark; a centred display headline capped at `15ch`; a bold centred standfirst; then a
  `36rem` measure carrying dateline, body and the interview.
- **Density:** Low — the lowest in the batch.
- **Media mode:** One lead area. The play mark is CSS-drawn, non-interactive and `aria-hidden`.
- **Interaction:** None. Static.
- **Responsive strategy:** The measure narrows `36rem` → `34rem` → unconstrained. At 768px the
  centred article title leaves the bar, because it repeats the headline directly beneath it; the
  film area goes `3/2` → `4/3`.
- **Composer value:** The editorial register and the only study modelling an **interview**: each
  question is a real `<h2>`, so the piece is navigable by heading rather than by scanning for bold
  text. Content model `{questions[{q, speaker, a}]}` on top of the article contract.
- **Limitation / content ceiling:** Three exchanges and a headline of about fifteen characters per
  line. It holds no sidebar, no related block and no credits — anything of that kind belongs to
  `001`, `003` or `005`.

### ARC-S25-003 — Dense / Information-heavy (reference 2)

- **Structural intent / archetype:** The blog article between two sidebars, with everything a blog
  carries: about block, connect row, pull quote, share row, author box, related posts, comments.
- **Layout model:** Three columns at `0.24fr / 1fr / 0.26fr`. The centre stacks seven regions in the
  reference's order. Related cards carry their titles on a filled band under the image, as the
  reference does.
- **Density:** High — nine regions on one page.
- **Media mode:** One `3/2` lead, one `3/4` portrait, one circular avatar, two `4/3` related cards.
- **Interaction:** None. The comment form is markup only, has no `action`, and says so beside its
  own button.
- **Responsive strategy:** Both sidebars release at 1024px and the article is promoted with
  `order: -1`, so the reading column is never squeezed between two rails on a narrow screen; the
  left sidebar becomes two-up, then one-up at 768px. The circular avatar becomes a `3/2` rectangle
  at 480px, where a 72px circle is too small to be worth its row.
- **Composer value:** The highest-capacity option in the section, and the only one modelling
  sidebars, comments and an author box together.
- **Limitation / content ceiling:** Three recent posts, three archive rows, two related cards. More
  and the right rail outruns the article at 1280px.

### ARC-S25-004 — Conversion-led (reference 3)

- **Structural intent / archetype:** The article with a standing route out. A pinned meta rail, an
  uppercase headline, and a dark card set into the text column carrying the same enquiry as the bar.
- **Layout model:** `150px / 1fr` shell: meta rail with hairline-separated fields and three round
  share marks on the left; article on the right. The first body section is itself a
  `1fr / 0.3fr` grid so the card sits beside the paragraph exactly as in the reference. Related band
  at four columns under a `5.25rem` uppercase heading; a closing enquiry line beneath.
- **Density:** Medium.
- **Media mode:** One `16/9` lead, one avatar in the card, four `3/4` related cards.
- **Interaction:** None. Static.
- **Responsive strategy:** The rail becomes a three-across row above the article at 1024px rather
  than a column too narrow to hold its own values; the card drops below its paragraph at 768px;
  related goes 4 → 2 → 1 and the card images turn `3/4` → `4/3` at 480px.
- **Composer value:** The conversion register for an article page. Its content model adds
  `{standing_action, in_body_card{author, role, note, action}, closing_action}` — one route, three
  placements.
- **Limitation / content ceiling:** Three body sections and four related cards. **No response time,
  readership figure, ranking or outcome is stated anywhere**, which is the discipline this territory
  needs on an editorial page.

### ARC-S25-005 — Sector-native / Distinctive (reference 4)

- **Structural intent / archetype:** The arts-magazine feature, and with it the **credits register**
  an architecture journal runs under a piece about built work: project, photography, drawings,
  location, each a label against a value, set beside the body rather than under it.
- **Layout model:** Cream sheet at `1080px`. Pill category nav; a serif display title whose joining
  words drop to `0.42em` on the same line; a `16/9` plate; a dated intro at `0.22fr / 1fr`; a centred
  serif pull quote; a plate pair at `0.62fr / 1fr` with different aspect ratios; the credits block at
  `0.3fr / 1fr` against the closing body; a `21/9` closing plate.
- **Density:** Medium.
- **Media mode:** Four plate areas. The piece reads with all four empty.
- **Interaction:** None. Static.
- **Responsive strategy:** The date column and the credits column both move **above** the copy they
  belong to at 768px rather than shrinking beside it; the plate pair stacks and equalises to `4/3`
  at 480px; the credits rows go from `7.4em / 1fr` to stacked label-over-value at 480px.
- **Composer value:** The identity option, and a **fifteenth sector-native register** for the sector.
  Content model `{credits[{label, value}]}` alongside the article contract — attribution for the
  work shown, which no generic article component carries.
- **Limitation / content ceiling:** Four credit rows and four plates. The mixed-scale title needs a
  phrase with joining words in the middle; a title without them loses the device.

## Research Metadata

- **Sources:** Five reference images supplied by the user, followed directly.
- **Research date:** 2026-08-31
- **Structural territory rationale:** See "Which reference became which study" above — territories
  were mapped onto the references rather than the references onto the territories.
- **Differentiation notes:** Five distinct page geometries: ruled meta column with author rail;
  white sheet on grey with one centred measure; three columns with two sidebars; pinned rail with an
  in-body card; and a cream feature with a credits register. Grounds differ — warm off-white, grey
  with a white sheet, near-white, white, and cream. Typography differs — two sans studies, two serif
  studies, one mixed. Media differs — 4, 1, 5, 6 and 4 areas. **No study uses JavaScript.**
- **Sector-interpretation note:** The section README says the label should follow sector
  terminology and that professional sectors generally do not call this a blog. The sector README
  calls it the **Studio Journal**, and the studies use "Journal" in the bar rather than "Blog".

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `@import`, `url()`, webfont, inline SVG, or inline
  `style` attribute in any of the five files.
- Network calls: NONE. Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static.
- Form endpoints: NONE. `003`'s comment form has an empty `action` and is labelled a placeholder on
  the page.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| `lead`, `rel-1…3` | `ARC-S25-001` | Lead image and three related cards | Photograph, `16/9` and `4/3` | The article is complete with all four empty; the lead carries a caption of its own. |
| `lead` | `ARC-S25-002` | Film still for the piece | Film still, `3/2` → `4/3` | Slot label reads "Film area". The play mark is drawn, non-interactive and `aria-hidden`, so an empty slot never implies a working player. |
| `lead`, `portrait`, `avatar`, `rel-1…2` | `ARC-S25-003` | Lead image, sidebar portrait, author avatar, two related cards | Photograph, `3/2`, `3/4`, `1/1`, `4/3` | Both portrait areas are unnamed and carry no person. Related card titles sit on a filled band beneath the image, not over it, so they are readable with the slot empty. |
| `lead`, `avatar`, `rel-1…4` | `ARC-S25-004` | Lead image, card avatar, four related cards | Photograph, `16/9`, circular, `3/4` | The dark card reads with its avatar empty; the related band keeps its titles below the images. |
| `plate-1…4` | `ARC-S25-005` | Lead plate, unequal pair, closing plate | Photograph, `16/9`, `3/4` + `4/3`, `21/9` | Captions are neutral ("lead plate", "narrow plate"). The credits register beside the body carries only tokens, so no plate implies a real, credited project. |

No slot in any study carries a client logo, an award mark, a certification badge, a signature, or a
named person.

## QA

- **ID validation: PASS.** Five IDs, each with matching `<meta name="study-id">`, `data-study-id`,
  scoped root class and filename; every element `id` namespaced and unique.
- **Raw-format validation: PASS.** Tag balance, nesting and unique-id checks pass on all five;
  unscoped-CSS and inline-`style` scans both return zero.
- **Accessibility QA: PASS.** One `<h1>` per study and no heading jumps — `004` was corrected before
  sign-off, where the meta rail's headings preceded the `<h1>` in source order; they are now
  paragraphs referenced by `aria-labelledby`, which keeps the rail's accessible names without
  putting an `<h2>` above the article title. Every `aria-labelledby` and `aria-describedby`
  resolves; every `<a>` carries an `href`; icon-only controls (the menu marks in `002`, `003` and
  `005`, the `@` in `003`) carry visually-hidden text. Visible `:focus-visible` in all five, with a
  light focus colour inside the dark card of `004`. `prefers-reduced-motion` in all five.
- **Form QA (`003`): PASS.** Three controls, three `<label for>` resolving, `<fieldset>` with
  `<legend>`, `autocomplete` on name and email, a real `<button type="submit">`, 46px minimum
  control height, and a visible statement that the form is unwired.
- **Contrast QA: PASS.** Measured on 36 pairs: all text ≥ 4.5:1, all component boundaries ≥ 3:1.
  One failure was found and fixed — `004`'s underline beneath the card action measured 2.91:1
  against the dark card and was raised to 3.34:1. The display headline in `002` is grey in the
  reference and was set at 4.59:1 rather than at the 3:1 large-text allowance, so it holds the
  stricter threshold even at display size.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390 and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder and every grid track uses `minmax(0, …)`. The
  README's reading-comfort rule is answered in every study: `001` caps the body at `72ch`, `002`
  runs a `36rem` measure, `003` keeps its centre column between two releasing rails, `004` caps at
  `78ch`, `005` at `74ch`. Every side column in the batch — meta column, author rail, both sidebars,
  the pinned rail, the date column, the credits column — releases to normal flow at 1024px or 768px
  rather than shrinking beside the text.
- **Dependency validation: PASS.** Zero matches across all five files.
- **Role-compliance validation: PASS.** No study carries an index or feed of all articles, or
  marketing copy dressed as editorial. A claim scan for award, certification, ranking, readership,
  share-count, comment-count, percentage and guarantee vocabulary returns matches **only** inside
  this batch's own disclaimers and negations.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- **Reference fidelity is the point of this batch.** Where a study departs from its reference it is
  for a stated policy reason — counts, names, platform marks and the play control — and each
  departure is written in that study's own closing note so it is visible on the page rather than
  only in this document.
- `ARC-S25-005` adds a fifteenth sector-native register — the credits register. It is deliberately
  not the service colophon of `ARC-S23-002`, which summarises an offering at the foot of a page, and
  not the bibliographic citation of `ARC-S09-005`. This one is attribution for the work in the
  plates, set beside the body.
- Every study marks its top region `data-region="page-context"`, the same mechanism introduced in
  `ARC-S23`: that region belongs to `ARC-S21` and `ARC-S22` and would be supplied by them in an
  assembly.
- The `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` roll-up counters still read
  `NOT_STARTED` for this sector; they are catalog-wide bookkeeping needing a separate
  workspace-level pass.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
