# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S10`
- Section Name: `Capabilities`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S10-001` | Universal / Safe | AUTHORED | `raw/ARC-S10-001.html` |
| `ARC-S10-002` | Premium / Editorial | AUTHORED | `raw/ARC-S10-002.html` |
| `ARC-S10-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S10-003.html` |
| `ARC-S10-004` | Conversion-led | AUTHORED | `raw/ARC-S10-004.html` |
| `ARC-S10-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S10-005.html` |

## Authoring Direction

**No reference images were supplied.** The direction was to work in the language the sector has
already established across `ARC-S01`–`ARC-S09` rather than to invent a new one, so before
authoring, all 51 existing studies were read back for their `layout-model` and `interaction`
metadata. Two things came out of that survey and both shaped this batch.

**What was inherited — the sector's house style:**
system font stacks with a monospace face reserved for technical labels and a Georgia serif for
editorial registers; warm paper grounds (`#f0efea`, `#f7f6f2`) and cool greys (`#f5f6f7`);
`clamp()` for every type and spacing ramp; `minmax(0, …)` on every grid track; the
1280 / 1024 / 768 / 480 / 360 breakpoint ladder; slot and field labels at 0.5–0.5625rem with
0.14–0.2em tracking; section title as the document `<h1>` with sub-headings at `<h2>`; and a
visible "placeholder … structure demonstration only" note closing each study.

**What was avoided — devices already carrying other sections:** the drawing-sheet plate index
(`S01-005`, `S04-005`), specification clauses (`S05-005`), the programme table (`S06-005`), the
monograph colophon (`S07-005`), the practice register (`S08-005`), bibliographic citation
(`S09-005`), the bento field (`S03-007`, `S04-003`), the buttoned scroll rail (`S03-004`,
`S08-009`), the ARIA tab set (`S04-005`, `S08-007`), the centre-spine timeline (`S06-002`), and
the sticky-panel-beside-a-list pairing (`S06-004`, `S09-004`).

Two genuinely new mechanisms enter the sector here: **native `<details>` disclosure** in `003` —
the first use of the element anywhere in the catalogue — and **CSS dot leaders** in `005`.

## Study Records

### ARC-S10-001 — Universal / Safe

- **Structural intent / archetype:** Three groups of work, each a short list, with the delivery
  mode stated per line. The plainest honest form for a capability section.
- **Layout model:** A split head over a three-column grid of bordered text-only cards. Each card
  runs a monospace group number, a title, a one-line description, and a ruled list where the
  capability sits left and its delivery mode right.
- **Density:** Medium. Twelve capability lines across three groups.
- **Media mode:** None. A capability is a list of what a studio does; a photograph beside it
  illustrates nothing the words do not already carry.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Three columns → two at 1024px with the third spanning both → one at
  768px. At 480px each line stacks its mode under its name rather than compressing the name.
- **Composer value:** The safest binding target — three repeatable groups, each with a repeatable
  list of `{name, mode}`. The mode field is the part most capability content models omit and most
  clients want.
- **Limitation / content ceiling:** Four lines per group before the cards go uneven; three groups
  before the row breaks. One line of description per group.

### ARC-S10-002 — Premium / Editorial

- **Structural intent / archetype:** Not everything the studio can do, but the four capacities it
  is organised around — the ones that decide which commissions it takes.
- **Layout model:** A serif head over a two-by-two field divided by full cross rules. Each
  quadrant pairs an oversized serif numeral with a title, a paragraph and a short dashed list.
- **Density:** Low-medium. Four capacities.
- **Media mode:** None. The quadrant field is the composition; an image inside it would break the
  cross that holds the layout together.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** The cross is abandoned rather than compressed: at 768px the field
  becomes a single ruled stack with the vertical rule and side padding removed, because a
  two-by-two divided field on a phone is four cramped boxes rather than a spread.
- **Composer value:** The premium register. Four records of `{numeral, title, paragraph, list}`
  and nothing else — the smallest field set in the section, and the one that reads as a position
  rather than an inventory.
- **Limitation / content ceiling:** Exactly four quadrants; the cross is the design. Three list
  items each. A studio with a genuinely broad offer will find this too narrow, which is the point.

### ARC-S10-003 — Dense / Information-heavy

- **Structural intent / archetype:** The full capability list, kept short on screen until someone
  wants it. Twenty-four lines that occupy the height of six.
- **Layout model:** A ruled head over a stack of native `<details>` panels. Each summary carries a
  monospace number, a title and an item count; each open panel holds a description and a
  two-column list of `{item, mode}` pairs.
- **Density:** High — the largest content set in the section, and the only study here that can grow
  without getting taller.
- **Media mode:** None.
- **Interaction:** **Native HTML disclosure only.** `<details>` / `<summary>` bring their own
  keyboard handling, focus behaviour and expanded state, so a section carrying far more than fits
  on screen needs no script at all. First use of the element in the sector. The open/closed state
  is also written out in words next to the count, so it is never carried by the marker triangle
  alone.
- **Responsive strategy:** Item lists go two columns → one at 768px; at 480px the summary drops to
  two tracks with the count moving to its own line, and each item stacks its mode beneath it.
- **Composer value:** The highest-capacity option, and the one whose content model is closest to
  how a practice actually keeps this list — grouped, with an in-house/consultant flag per line.
- **Limitation / content ceiling:** Six groups of four is the tested shape; the pattern scales but
  a summary row with a two-line title breaks the count alignment. Because the first panel is open
  by default, the section is never entirely collapsed.

### ARC-S10-004 — Conversion-led

- **Structural intent / archetype:** Most commissions arrive part-way through. Rather than pitching
  the full capability set, the section asks where the project already is and names the first piece
  of work for each answer.
- **Layout model:** A head over three routing cards, each with a monospace route tag, a situation
  title, a paragraph, a ruled "first piece of work" definition pair, and its own action, which is
  stretched over the whole card. A dark foot bar catches everyone the three routes miss.
- **Density:** Medium.
- **Media mode:** None.
- **Interaction:** None. No `<script>` element. The conversion is a routing decision, not a pitch.
- **Responsive strategy:** Three cards → two at 1024px with the third spanning → one at 768px. The
  foot bar stacks at 480px where the action goes full width.
- **Composer value:** The conversion register, and structurally the only "which of these are you"
  pattern in the sector. Each card is `{tag, situation, description, first-step, action}`, which
  maps onto a routing table rather than a service list.
- **Limitation / content ceiling:** Three routes; a fourth breaks both the row and the premise that
  the choice is easy. Each card names one first step — it cannot carry a scope. No fee, response
  time or guarantee is stated, deliberately, so a studio must add its own.

### ARC-S10-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The schedule of services — the annex a practice attaches to an
  appointment setting out what is included, what is available on request, and what it does not do.
  Written as scope, so a client can see the edges of the engagement before agreeing to it.
- **Layout model:** A bordered sheet with a monospace head and preamble, then four groups of ruled
  service lines. Each line runs a clause reference, the service name, a **dot leader**, and a
  right-hand inclusion stamp. A three-part legend and a sheet foot close it.
- **Density:** Medium-high. Fifteen service lines across four groups.
- **Media mode:** None. A schedule of services is a document issued with a fee proposal.
- **Interaction:** None. No `<script>` element.
- **Responsive strategy:** Dot leaders need a wide measure to read, so at 768px the leader is
  dropped and the stamp moves beneath the service name on its own rule — the line stays legible
  instead of the leader shrinking to a few pixels. At 480px the clause reference stacks too.
- **Composer value:** The identity option, and a seventh distinct sector-native register for the
  sector. Its content model is a scope table — `{ref, service, position}` — which is exactly what a
  practice already maintains for its appointments.
- **Limitation / content ceiling:** Four or five lines per group; longer service names collide with
  the stamp before the leader has room to read. Three stamp states only.
- **Distinctness from `ARC-S06-005`:** that study is a two-dimensional programme whose spanning
  cells read as bars across phase columns. This is a one-dimensional document of ruled service
  lines, each terminating in a stamp. Different document, different geometry, different data shape.

## Research Metadata

- **Sources:** None. Authored to brief, informed by a metadata survey of the 51 studies already in
  the sector.
- **Research date:** 2026-08-30
- **Structural territory rationale:** Territories were mapped onto the five ways a practice answers
  "what can you do" — a grouped list with delivery modes for the general case, four organising
  capacities for the premium case, the complete list held behind disclosure for the dense case, a
  routing question for the conversion case, and the issued schedule of services for the
  discipline-native case.
- **Differentiation notes:** Five distinct geometries — a three-card group grid, a cross-divided
  quadrant field, a disclosure stack, three routing cards over a bar, and a dot-leader document.
  Grounds differ: near-white, warm off-white, cool grey, warm light with a dark bar, and paper.
  Only one uses disclosure; only one uses leaders; only one has actions. No study uses JavaScript.
- **Sector-interpretation note:** Capability sections invite two claims this batch refuses. The
  first is tooling — naming software would be an unverifiable claim about a placeholder studio, so
  no product, vendor or file format appears anywhere. The second is capacity — no team size, volume,
  turnaround or certification is stated. What is stated instead is **delivery mode**: whether a line
  is held in-house or appointed out. That is the honest, checkable version of a capability claim,
  and it is the field the batch is built around.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, no `<img>`, no `@import`, no `url()`, no webfont, no inline
  SVG. The `005` dot leaders are a repeating `radial-gradient`, not an image.
- Network calls: NONE — no `fetch`, no `XMLHttpRequest`, no form.
- Browser storage: NONE.
- JavaScript necessity: NONE. All five studies are static; none contains a `<script>` element.
  `003` is interactive without script because it uses a native HTML element for the job.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| — | `ARC-S10-001` | **No media slot by design** | — | A capability is a list; an image beside it carries nothing the words do not. |
| — | `ARC-S10-002` | **No media slot by design** | — | The quadrant cross is the composition; an image inside it breaks the rules that hold it. |
| — | `ARC-S10-003` | **No media slot by design** | — | Disclosure panels are text records. |
| — | `ARC-S10-004` | **No media slot by design** | — | Routing cards are read, not looked at. |
| — | `ARC-S10-005` | **No media slot by design** | — | A schedule of services is a document issued with an appointment. |

This is the second section in the sector with no media slot in any study, after `ARC-S09` came
close with one. It is a consequence of the subject rather than an oversight, and is recorded here
so the absence is not read as unfinished work.

## QA

- **ID validation: PASS.** All five planned IDs exist, each with a matching
  `<meta name="study-id">`, a `data-study-id` attribute, a scoped root class, and a filename in the
  `ARC-S10-NNN.html` form. Every element `id` is namespaced with its study ID.
- **Raw-format validation: PASS.** Five standalone `.html` files. Tag balance, nesting and
  unique-id checks pass on all five. All CSS is namespaced to the study root class; a scan for
  unscoped rules returns zero across the batch, excluding the documented two-line host baseline.
- **Accessibility QA: PASS.** Exactly one `<h1>` per study, no heading-level jumps, every
  `aria-labelledby` reference resolving, every `<a>` carrying an `href`, visible `:focus-visible`
  styling in all five with an amber ring inside the dark bar, and a `prefers-reduced-motion` block
  in all five. In `003` the disclosure state is written in words beside the item count, so it is
  never signalled by the marker alone. Contrast measured on 15 pairs against each study's own
  ground: all text ≥ 4.5:1 (lowest 6.80:1) and all interactive borders ≥ 3:1 (lowest 3.55:1).
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390, and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder. Two layouts change behaviour rather than
  shrinking: `002` abandons its cross-divided field for a ruled stack at 768px, and `005` drops its
  dot leaders and re-places the stamp beneath the service name at the same width. No horizontal
  scroll anywhere. Interactive controls are ≥ 44px.
- **Dependency validation: PASS.** Scanned for `http:`, `https:`, protocol-relative URLs,
  `@import`, `src=`, `<link>`, `<iframe>`, `url(`, `fetch(`, `XMLHttpRequest`, `integrity`,
  `crossorigin`, and `<script`. Zero matches across all five files.
- **Claim-policy validation: PASS.** Visible text scanned for certification schemes and standards,
  accreditation and rating language, percentages and measured figures, and named software vendors
  and file formats. Zero matches across all five files.
- **Structural-diversity validation: PASS.** Five distinct geometries, checked against the 51
  earlier studies by their recorded `layout-model` and `interaction` metadata; the avoided devices
  are listed under Authoring Direction.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing, and
  reduced-motion behaviour under a real user preference. Those belong to Design Lab capture and QA.

## Notes

- `ARC-S10-003` is the first study in the sector to use `<details>` / `<summary>`. It is worth
  noting for ingestion that its interactivity is native: there is no script to preserve, and the
  panels are open-able in a captured screenshot only if the capture opens them.
- `ARC-S10-005` adds a seventh sector-native register — the schedule of services — alongside the
  drawing sheet, specification clause, project programme, monograph colophon, practice register and
  bibliography.
- The delivery-mode field (`in-house` / `consultant`) appears in three of five studies and is the
  batch's substantive editorial decision. It is what makes a capability list checkable instead of
  aspirational.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
  Territory labels are the authoring targets from `standards/01-AUTHORING-STANDARD.md`.
- Workspace roll-up counters in `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` still read
  `NOT_STARTED` for this sector and need a separate workspace-level pass.
