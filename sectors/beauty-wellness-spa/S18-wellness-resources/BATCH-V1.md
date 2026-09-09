# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S18`
- Section Name: `Wellness Resources`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S18-001` | Universal / Safe | AUTHORED | `raw/WELL-S18-001.html` |
| `WELL-S18-002` | Premium / Editorial | AUTHORED | `raw/WELL-S18-002.html` |
| `WELL-S18-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S18-003.html` |
| `WELL-S18-004` | Conversion-led | AUTHORED | `raw/WELL-S18-004.html` |
| `WELL-S18-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S18-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its two simultaneous constraints and its
boundary with `S15` and `S25` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — Two Problems At Once

**1. An article title is invented content.** Writing *"Five ways to strengthen your skin barrier"*
invents a publication, and that particular title is also an efficacy claim.

| Element | Treatment |
| --- | --- |
| Article title | **Reserved area**, sized to the type scale it will occupy |
| Article summary | **Reserved area** where shown — no study shows one |
| Topic category | **Real** — generic sector vocabulary, as in `S03` |
| Kind of resource | **Real** — an aftercare note, a guide, a question answered |
| Publication date | **Reserved field** — a published piece has a date, so the empty field asserts nothing |
| Reading time | **Omitted** — a figure a placeholder cannot compute |
| Per-topic article count | **Omitted** — same reason |

**2. This is the section where the sector's claims rule is most likely to break.** A wellness
resources index is the natural home of *"boost"*, *"detox"*, *"reset your skin"*, *"the truth about
collagen"*. Because every title in this batch is reserved, **no study can carry such a claim even
accidentally.** That is the strongest argument for reserving a title rather than writing a
plausible-sounding placeholder, and it is the batch's defining result.

The `S11` field-versus-figure test decides the rest: *reserve the field when the empty field asserts
nothing; omit it when the empty field asserts a system.* A date is reserved. A reading time and an
article count are omitted — an empty *"— min read"* asserts that the studio measures reading time.

**Not present in any study:** an invented article title, summary, author name, publication date,
reading time, view count, share count or category count; an efficacy, outcome or ingredient claim;
a diagnostic statement; a "trending", "most read", "popular" or "featured" label; a newsletter
capture, email field or subscriber figure.

## What Is Real — Including What The Section Is Not

Three things, and the third is the most important:

1. **The topics and kinds.** Generic, and enough to show how an index sorts itself.
2. **Why the studio publishes.** *"These exist so you do not have to ring us about the same five
   things"* — an operating position, and the notes are handed over on paper anyway.
3. **What this is not.** **None of this is medical advice, and something changing, sore or worrying
   on your skin is a doctor's question, not a spa's.**

That third line appears in **all five studies**, verified by scan. It is the sector's clearest
liability point, and it is completely authorable because it is a statement about limits rather than
a claim. In `004` it is promoted from small print to the conversion device.

## Study Records

### WELL-S18-001 — Universal / Safe

- **Layout model:** Three index cards, each with a reserved 16:9 media area, the kind of resource,
  a reserved title area, the topic, a reserved date and a "Read it" link — closed by the limits
  line.
- **Why the card still carries media:** the reserved title leaves the card without its normal
  anchor, and an image area gives the dependable variant something to be built around. This is the
  only study in the batch that reserves media at all.
- **Responsive strategy:** 3 → 2 cards with the third spanning full width, then one per row.

### WELL-S18-002 — Premium / Editorial

- **Layout model:** A five-row ruled reading list — topic, kind and reserved date set small in the
  left margin, and a reserved title area at display scale filling the measure.
- **The editorial reading:** an index of this kind is carried by its headlines, so the study spends
  its whole composition on the title areas and **uses no media at all**. Where `001` gives the
  reserved title a supporting picture, `002` makes the reservation the subject.
- **Correction made, recorded:** at first authoring the reserved areas ran the full measure and read
  as empty plates rather than as missing headlines. They are now held to a headline measure
  (`36rem`) with two-line and one-line heights, so the reservation states the *shape* of the
  headline it is holding — which is the only useful thing an empty title area can say.
- **Responsive strategy:** the margin column folds above the title at 768px; the title area releases
  its measure.

### WELL-S18-003 — Structured / Visual Modular

- **Layout model:** Three topic modules, each holding two entries, plus a fourth full-width legend
  module on a dark ground.
- **The device — the fourth module is what earns the direction.** Sorting an index into topic groups
  is ordinary. Explaining **what an "aftercare note" is**, and how it differs from a guide and from
  a question answered, is the part a visitor actually needs, and it is entirely authorable because
  it describes the studio's publishing habits rather than the content of anything published.
- **Not a table:** the modules have their own internal shape; there is no matrix of rows and
  columns. See the `003` trap in `../WELLNESS-DESIGN-DIRECTION.md`.
- **Responsive strategy:** 3 → 2 → 1 modules; the legend goes 4 → 2 → 1 columns with its intro
  spanning.

### WELL-S18-004 — Conversion-led

- **Layout model:** A held panel — why any of this is written down, the limits statement in its own
  bordered block, one action, and a line saying nothing needs signing up to — beside a compact list
  of four entries.
- **Conversion device: the disclaimer is the conversion device.** A visitor deciding whether to read
  a wellness studio's writing about skin is deciding whether to trust it, and the fastest way to
  earn that is to say plainly where the writing stops. The sentence most sites bury in small print
  is given the panel, above the action.
- **What it avoids:** **no newsletter capture, no email field, no gated download.** A resources
  section is exactly where those belong on a real site, and every one of them would need an invented
  subscriber promise or figure. The action is to read, which is the only thing this section can
  honestly ask for; booking belongs to `S19` and `S20`.

### WELL-S18-005 — Art-directed / Distinctive

- **Layout model:** Four paper sheets fanned down the page and stepped to the right, each
  overlapping the one above it, on a warm oat ground.
- **The device:** the studio already prints these notes and hands them over. Drawing the index as
  **a spread-out pile of that paper** makes the section say what it is before a word is read — and
  it works *because* the titles are missing, since a stack of sheets is legible as a stack whether
  or not you can read the top one.
- **Deliberately not rotated:** no sheet is turned. `WELL-S17-005` is the sector's one rotated study
  and the effect stops being distinctive if a second study copies it, so the pile is built from
  offset and overlap alone.
- **Correction made, recorded:** the mobile reset of the rightward step was written as
  `.pile li .sheet { margin-left: 0 }` against a base rule of
  `.pile li:nth-child(4) .sheet { margin-left: 18% }`. The `:nth-child` adds a specificity point, so
  **the reset never applied** and the cascade kept stepping right below 768px. Caught in render, not
  in the compliance scan. Fixed by matching the override to the base selectors. Recorded because it
  is a general trap: *an override in a media query must match the specificity of the rule it is
  overriding, and `:nth-child` quietly raises it.*
- **Responsive strategy:** the rightward step reduces at 1024px and is removed at 768px; the
  vertical overlap is kept, so the pile reads as a squared-up stack rather than a fan.

## Structural Diversity

| Study | Topology | Reserved titles | Media | Ground |
| --- | --- | --- | --- | --- |
| 001 | Three index cards | 3, card scale | 3 reserved 16:9 areas | Pale eucalyptus `#edf2ef` |
| 002 | Five ruled list rows | 5, display scale | None, deliberate | Warm parchment `#eee7da` |
| 003 | Three topic modules + a legend | 6, small | None | Pale slate `#e5e8ec` |
| 004 | Trust panel beside a compact list | 4, medium | None | Deep forest-teal `#1f3835` |
| 005 | Four overlapping paper sheets | 4, sheet scale | None | Warm oat `#ddd3c2` |

Grounds do not repeat any used in `WELL-S01`–`S17`; verified by scan across all 90 studies.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is how
  much of the composition a reserved title is allowed to occupy — supported by media, given the
  whole measure, reduced to a small unit inside a sorted module, made compact beside an argument, or
  set on an object that is itself the image.
- **Document-metaphor justification:** `005` uses paper sheets. This is a **licensed** use of the
  document metaphor rather than a breach of the sector rule, because the studio genuinely hands
  these notes over on paper; the metaphor names a real physical artefact instead of dressing web
  content as a form or a certificate. No other study uses one.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>`, no `<iframe>`,
  no inline `style` attribute in any file.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Resource media ×3 | `001` — one per index card | Still image, 16:9 | Empty tonal surface with a quiet label |
| Article title ×22 | All five studies | **Text**, replaced by the real headline | Sized reserved area stating how many lines it holds |
| Publication date ×22 | All five studies | **Text**, replaced by the real date | Em dash with a visually hidden "Publication date" label |

Verified by scan: 22 reserved title areas and 22 reserved date slots across the batch, all 22 dates
carrying a visually hidden field label.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`, 44px-plus targets. Every reserved date slot carries a visually hidden
  field label.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above. `005`'s failed mobile
  reset was found in render and fixed. Verified at 1440px and at 720px, where the sub-768 branch of
  every study fits its measure with no horizontal overflow.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script, iframe
  or inline style.
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex and no `clamp()` with the
  wrong arity. The 8-digit check was added for this batch after an authoring slip produced
  `#62594691` — a valid but unintended RGBA colour that the `S16` hex check would have passed.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s18-00N` root.
- **Claims and metrics check: PASS — this batch's defining check.** Visible text only, comments and
  hidden field labels stripped, scanned for *min read*, *reading time*, *views*, *shares*,
  *trending*, *most read*, *popular*, *featured*, *subscribe*, *newsletter*, *boost*, *detox*,
  *toxins*, *collagen*, *reset your*, *cure*, *heal*, *anti-ageing*, *clinically*, *proven*,
  *scientific*, *dermatologist*, *diagnos-*, *prescrib-*, *treats*, *remedy*, *miracle*,
  percentages and **any digit**. **Zero matches in all five** — there is not one digit in visible
  copy anywhere in the batch.
- **Limits-statement check: PASS.** All five studies carry both halves of the sentence — *none of
  this is medical advice*, and *a question for a doctor rather than for a spa*.
- Render check: **PASS, after two corrections.** All five rendered in headless Chrome at 1440px and
  inspected: `002`'s title areas were re-proportioned to a headline measure, and `005`'s mobile
  cascade reset was fixed. Both are recorded in the study records above.

## Notes

- This is the eighteenth authored batch in the `WELL` sector and the sixteenth authored entirely
  without references.
- **The reusable outcome is that reserving a field can enforce a policy, not just avoid a lie.** In
  every earlier section a reserved slot was a way of not inventing something. Here the reserved
  title also makes it *structurally impossible* for the batch to carry a health claim — the riskiest
  copy in the sector cannot enter the section, because the place it would have been written is a
  labelled empty area. Where a catalog has a content rule that is easy to break by accident, put the
  reservation where the breach would be written.
- The section's most valuable content turned out to be its own limit. `S14` established that a
  belief is worth stating when it costs the business something; `S18` extends that to *what we will
  not tell you, and who you should ask instead*, which is both the honest position and the strongest
  trust device available to a section that cannot show a single real article.
- `S18` completes the reading group: `S15` answers a booking question, `S18` indexes what has been
  written, `S25` will hold one piece in full.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a Windows Store placeholder
  rather than an interpreter. Headless Chrome, which the generator uses for measurement, is present
  and working, so a Node port of `review/build-index.py` would restore it.
