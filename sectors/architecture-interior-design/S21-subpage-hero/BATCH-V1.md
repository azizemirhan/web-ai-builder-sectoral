# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S21`
- Section Name: `Subpage Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S21-001` | Universal / Safe | AUTHORED | `raw/ARC-S21-001.html` |
| `ARC-S21-002` | Premium / Editorial | AUTHORED | `raw/ARC-S21-002.html` |
| `ARC-S21-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S21-003.html` |
| `ARC-S21-004` | Conversion-led | AUTHORED | `raw/ARC-S21-004.html` |
| `ARC-S21-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S21-005.html` |

## Authoring Direction

**No reference images were supplied.** This is the first of the extended site architecture roles
(S21–S27) to be authored, and unlike the sector core sections it arrived with a written
specification: the section README produced during the catalog extension already set the purpose,
visitor intent, in and out of scope, media relationship, interaction limit and responsive rules.
The batch was authored **against that specification** rather than to a blank brief, and each study
records where it answers it.

### The test the README sets

> *S01 is the homepage or primary sector hero. S21 is the internal page contextual hero. A study
> that would work unchanged as S01 has not answered this role.*

That test drove three decisions across the batch:

- **No full-bleed stages.** All five S01 studies in this sector are stages — full-bleed grounds,
  overlay type, corner cards. None of that appears here. Every S21 study is a *block* at the top of
  a page, not a stage that fills a viewport.
- **Media is never behind the title.** `002` is the only study with an image and it sits *beneath*
  the title, contained, at a strip proportion. An internal page hero that sets type over a picture
  is a homepage hero wearing a smaller hat.
- **Four of five carry no image at all.** The README asks for at least one variant that works
  without one; the honest reading of internal pages is that most have none, so the batch inverts
  the usual ratio.

### Where the boundary with S22 was drawn

`003` carries an in-page contents list, which could arguably belong to context navigation. It is
here because it describes the **inside of this page**, while S22 describes the page's **position in
the site**. The same reasoning put the key-plan locator in `ARC-S22-005` rather than in this
section. Both studies state the distinction in their own closing note.

## Study Records

### ARC-S21-001 — Universal / Safe

- **Structural intent / archetype:** Parent label, title, one line of framing, four facts. The
  smallest thing that can honestly be called a page header.
- **Layout model:** A ruled context block: monospace parent label, title at `clamp(1.75rem, 3.4vw,
  2.75rem)`, a framing intro capped at 60ch, and a wrapping four-field metadata row on a rule.
- **Density:** Low.
- **Media mode:** **NONE, by design** — this is the variant the README asks for.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The metadata row is a wrapping flex row that becomes a column at 480px:
  a wrapped label is readable, a clipped one is not, and the README forbids truncation.
- **Composer value:** The safest binding target in the section — `{parent, title, intro, four
  label/value pairs}` and nothing that assumes an image exists.
- **Limitation / content ceiling:** Four metadata fields and one intro sentence. No action and no
  media, which is the point: it is the default that works everywhere.

### ARC-S21-002 — Premium / Editorial

- **Structural intent / archetype:** A page opener with one contained image, set so the image
  supports the title rather than competing with it.
- **Layout model:** A three-track context line (parent, rule, page qualifier) above a serif title,
  a framing intro, and a 21:9 media strip **below** the title with a two-part monospace caption.
- **Density:** Low.
- **Media mode:** One contained strip. Deliberately never a background.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The context line loses its rule at 768px before it loses either label,
  and collapses to a single column at 480px; the strip relaxes 21:9 → 16:9 → 3:2.
- **Composer value:** The premium register, and the only S21 study with a media field. Removing the
  image leaves a complete header, which is the property that keeps it an internal page hero.
- **Limitation / content ceiling:** One image and two context labels. A second image would make it
  a gallery header, and a taller ratio would make it a stage.

### ARC-S21-003 — Dense / Information-heavy

- **Structural intent / archetype:** A contextual masthead carrying everything a deep page needs to
  declare: what it is, what it belongs to, eight fields of context, and what is inside it.
- **Layout model:** Parent label, then a `1.2fr / 1.35fr` masthead pairing title and intro with an
  eight-cell hairline metadata grid, closed by a four-column in-page contents list of eight anchors.
- **Density:** High — the most a page header can carry before it becomes the page.
- **Media mode:** **NONE.** At this density an image is the only thing that could not fit.
- **Interaction:** None. The contents list is plain in-page anchors, which the README permits for
  local navigation provided it degrades to links — here there is nothing to degrade from.
- **Responsive strategy:** Metadata steps 4 → 2 → 1 columns, contents 4 → 2 → 1, masthead stacks at
  1024px. Nothing is dropped at any width.
- **Composer value:** The highest-capacity option, and the only one that models a page's own
  contents as a field. Useful for long detail pages in `S23`–`S27`.
- **Limitation / content ceiling:** Eight metadata fields and eight contents entries. Past that the
  header is longer than the first screen of the page it introduces.

### ARC-S21-004 — Conversion-led

- **Structural intent / archetype:** A page header that also routes — but exactly once.
- **Layout model:** Parent label over a `1.5fr / 0.85fr` split: title and intro on the left, a
  bordered card on the right holding a qualifying sentence, one full-width action, and a monospace
  line stating what the action does.
- **Density:** Low-medium.
- **Media mode:** **NONE.** The action is already the second element competing for the same glance.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The action card drops **below** the title at 768px rather than beside it,
  capped at 460px, because the README requires the title to be the first thing read at every width.
- **Composer value:** The conversion register. Its content model is `{title, intro, one action, one
  qualifier}` — the qualifier being the field that keeps the action honest.
- **Limitation / content ceiling:** **One** action, deliberately. The README caps the role at a
  single contextual action and puts competing calls to action out of scope; secondary routes belong
  further down the page.

### ARC-S21-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The running head and folio — the page opener a printed document
  uses to tell a reader who has landed mid-way which part they are in.
- **Layout model:** A running head on a rule (part name, dotted leader, folio mark), then a page
  opener set low against `clamp(34px, 6vw, 96px)` of space: part reference, serif title, framing
  intro, closed by a monospace rule line.
- **Density:** Low-medium.
- **Media mode:** **NONE.** A folio page opens on type; that is what makes it an opener rather than
  a cover.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The dotted leader needs a run to read, so it is dropped at 768px and the
  running head becomes two stacked lines; the opener's top space compresses rather than the title.
- **Composer value:** The identity option, and a twelfth sector-native register for the sector. It
  is deliberately a **print** register rather than a drawing one: the drawing-sheet header is
  already carrying `ARC-S01-005` and `ARC-S03-005`, and a running head answers this role more
  exactly than a title block does.
- **Limitation / content ceiling:** One part reference and one folio mark. The generous opener space
  is the design, so this study is the tallest header in the batch and suits a document-like page
  rather than a dense one.

## Research Metadata

- **Sources:** None. Authored against the section README written during the catalog extension to
  S27.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five ways an internal page
  can open — plain facts, one contained image, a full context masthead, a single routed action, and
  a printed running head.
- **Differentiation notes:** Five distinct geometries; four carry no media at all, which is itself a
  differentiator from every other section in this sector. Grounds differ: near-white, warm off-white,
  cool grey, warm light, and warm paper. Type differs: neutral sans, serif, sans with a hairline
  metadata grid, sans with a filled action, and serif with a monospace running head. No study uses
  JavaScript.
- **Sector-interpretation note:** The main risk in this role is writing S01 again at a smaller size.
  Every study was checked against that test and the three decisions it forced are recorded above.

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
| Contained strip | `ARC-S21-002` | One supporting image for an internal page | Still image, 21:9 (16:9 at 768px, 3:2 at 480px) | Sits **below** the title, never behind it. The header is complete with the slot empty. |
| — | `ARC-S21-001` | **No media slot by design** | — | The README asks for a variant that works without an image; this is it. |
| — | `ARC-S21-003` | **No media slot by design** | — | At this density an image is the only thing that would not fit. |
| — | `ARC-S21-004` | **No media slot by design** | — | The action already occupies the second position in the block. |
| — | `ARC-S21-005` | **No media slot by design** | — | A folio page opens on type. |

## QA

- **ID validation: PASS.** Five IDs, each with matching `<meta name="study-id">`, `data-study-id`,
  scoped root class and filename; every element `id` namespaced.
- **Raw-format validation: PASS.** Tag balance, nesting and unique-id checks pass on all five;
  unscoped-CSS and inline-`style` scans both return zero.
- **Accessibility QA: PASS.** One `<h1>` per study, no heading jumps, every `aria-labelledby`
  resolving, every `<a>` carrying an `href`, visible `:focus-visible` in all five, and a
  `prefers-reduced-motion` block in all five. Contrast measured on 8 pairs: all text ≥ 4.5:1
  (lowest 6.77:1).
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder, and all five honour the README's rule that the
  title reads first at every width — most visibly in `004`, where the action card moves below the
  title rather than staying beside it.
- **Dependency validation: PASS.** Zero matches across all five files.
- **Claim-policy validation: PASS.** Copy frames the page rather than the sector; no positioning
  line, capability claim, client, date, cost, area or completed-project claim appears, and `004`
  states no response time, fee, availability or guarantee.
- **Role-compliance validation: PASS.** Each study was checked against the README's own test — none
  would work unchanged as `S01`.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- This section and `ARC-S22` were authored against specifications written during the S27 catalog
  extension rather than to a blank brief. That is a different authoring mode from the sector core
  sections and is worth preserving for the remaining extended roles.
- A documentation defect was found and fixed while authoring: the generated "Homepage hero for this
  sector" line in every S21 README had the section name and directory slug transposed. Corrected in
  all twenty sectors.
- `ARC-S21-005` adds a twelfth sector-native register, and the first drawn from print convention
  rather than drawing-office convention.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
