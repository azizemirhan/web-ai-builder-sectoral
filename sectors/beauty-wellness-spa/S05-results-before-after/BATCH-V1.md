# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S05`
- Section Name: `Results Before After`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S05-001` | Universal / Safe | AUTHORED | `raw/WELL-S05-001.html` |
| `WELL-S05-002` | Premium / Editorial | AUTHORED | `raw/WELL-S05-002.html` |
| `WELL-S05-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S05-003.html` |
| `WELL-S05-004` | Conversion-led | AUTHORED | `raw/WELL-S05-004.html` |
| `WELL-S05-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S05-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role and its governing constraint are in
`./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint

This is the highest-risk section role in the sector, and the one `../WELLNESS-DESIGN-DIRECTION.md`
names first. Everything the section exists to show is evidence, and a placeholder study has none
and may invent none.

**Structure is authored; evidence is reserved.** The five studies compose the comparison
*structure* — how a real studio would present paired imagery — and leave every position that would
carry a claim empty.

**Not present in any study in this batch:**

- a fabricated before image, after image or comparison
- an outcome statement, result claim, improvement description or efficacy word
- a percentage, success rate, satisfaction figure or count of results
- a number of sessions, a course length, or any time-to-result
- an identifiable client, client name, age, testimonial or rating
- a treatment presented as producing a named effect

**Present, because structural and non-fabricated:**

- `Before` and `After` as slot labels. They name the two positions in a comparison; they assert
  nothing about what happened between them.
- The category and treatment name per case, from the same set used in `S02` and `S03`.
- Reserved media areas at the scale and pairing the real experience needs.

**Where copy was needed, it went to method rather than outcome.** Three studies carry a line about
how the pair is photographed — same room, same light, same distance, same lens. That is procedural,
verifiable and non-fabricated, and it is the one thing a studio can honestly say about a
before-and-after pair without describing a result. It also happens to be the thing that makes a
comparison trustworthy, so the constraint improved the copy rather than hollowing it out.

## Consent And Compliance — Handoff Note

In most markets, before-and-after imagery for beauty and aesthetic treatments is regulated: it
normally requires documented client consent, and attached claims are restricted. **A real
implementation of this section needs a consent line and a compliance review before any image is
placed in these slots.**

That line is deliberately absent from the visible compositions. A study with no images cannot
truthfully say images are shown with consent, and the *Visible Website Copy vs Research Notes* rule
keeps policy explanation off the page. Whoever fills these slots must add it. Every study reserves
room for it beneath its caption or in its closing row.

## Study Records

### WELL-S05-001 — Universal / Safe

- **Structural intent / archetype:** The dependable comparison grid. Three cases, each an
  unambiguous side-by-side pair.
- **Layout model:** A header closed by a hairline, above three case cards. Each card holds two
  equal frames separated by a 2px seam in the card colour, with `Before` and `After` chips at the
  top-left of each frame, closed by a caption naming the category and the treatment. A single
  closing line routes to a consultation.
- **Pairing device:** The 2px seam is what makes the two frames read as **one comparison** rather
  than two pictures. It is the smallest gap in the batch, deliberately.
- **Media relationship:** Six reserved areas in three pairs, every frame at identical scale and
  proportion.
- **Responsive strategy:** 3 → 2 → 1 cards; the frames step 3:4 → 4:5 → 1:1. The **pair never
  stacks** — two frames above one another stop reading as a comparison, so both frames narrow
  together at every width.
- **Visual-first check:** 69 visible words.

### WELL-S05-002 — Premium / Editorial

- **Structural intent / archetype:** One case at publication scale. The whole section is a single
  diptych.
- **Layout model:** A serif header, one large two-frame diptych with a small gap, then a caption
  row beneath a hairline — treatment name on the left, one procedural sentence and a text link on
  the right.
- **Direction-specific risk, recorded:** the editorial register invites a caption that *interprets*
  the image, which is exactly what this role may not do. The caption is held to method.
- **Media relationship:** Two reserved areas, the largest in the batch.
- **Responsive strategy:** The frames step 4:5 → 3:4; the caption row goes to one column at 768px.
  The pair never stacks, for the same reason as `001`.
- **Visual-first check:** 53 visible words.

### WELL-S05-003 — Structured / Visual Modular

- **Structural intent / archetype:** The comparison held in one footprint instead of two. Each case
  swaps state in place.
- **Layout model:** Three case modules in a row. Each has one frame footprint holding two stacked
  reserved areas, a segmented `Before` / `After` switch beneath it, and a caption. Selecting a
  state swaps which area occupies the frame.
- **Content-capacity justification:** Six reserved areas exist, three are visible at a time. The
  capacity is in the state swap, not in copy — and the swap is not decoration: showing both views
  at **exactly** the same size, crop and position is the strongest guarantee that they are
  comparable, which is precisely what this section role is for.
- **Interaction:** Native radio inputs plus CSS sibling selectors, one group per case, **no
  JavaScript**. Each group sits in a fieldset with a visually-hidden legend naming its treatment,
  every option is a real label bound to its input, arrow keys move through each group as a native
  radiogroup, and the focus ring is drawn on the visible switch.
- **Responsive strategy:** 3 → 2 → 1 modules; the frame steps 4:5 → 1:1 → 4:3. The switch keeps its
  two-column shape at every width, since it has only two states.
- **Visual-first check:** 85 visible words, the highest in the batch — which includes both state
  labels for all three cases.

### WELL-S05-004 — Conversion-led

- **Structural intent / archetype:** The comparison and the honest next step, side by side.
- **Layout model:** An asymmetric 1.18fr / 0.82fr split. Left: header, one pair, caption. Right: a
  cream consultation panel with a heading, one lead, three hairline-separated items describing what
  a consultation covers, and the action pinned to the panel foot.
- **Conversion behaviour, and the specific risk here:** this is the direction where a
  before-and-after section is most likely to make a promise, because the obvious conversion line is
  *get this result too*. The composition routes the other way. The panel's third item is **"What is
  and is not realistic to expect"** — which is the compliant answer, the honest one, and a better
  offer than a claim would be. Nothing is collected; the action opens a consultation route.
- **Media relationship:** Two reserved areas in one pair.
- **Responsive strategy:** The split becomes one column at 1024px with the frames going 1:1; the
  action goes full width at 768px. The pair never stacks.
- **Visual-first check:** 69 visible words.

### WELL-S05-005 — Art-directed / Distinctive

- **Structural intent / archetype:** Not two images beside each other, but one field cut once.
- **Layout model:** A full-bleed stage of two equal halves meeting at a hard vertical seam with no
  gap. `Before` and `After` marks sit at the outer top corners — pushed apart rather than paired,
  so the eye reads the whole width as one frame. A translucent band spans the full width at
  mid-height carrying the category and the treatment name in oversized type **across** the seam.
- **Distinctiveness, and why it is not paperwork:** the differentiation is a single cut and a
  crossing. It reaches for none of the clinical or administrative devices in the sector
  anti-pattern list.
- **Empty-state devices, recorded:** the two halves carry slightly different tones so the seam is
  visible before any photography arrives, and the band is a translucent backdrop rather than plain
  overlaid text, so the name stays legible over the empty tone now and over two different
  photographs later.
- **Separation from `WELL-S04-005`:** that is a four-column band of separate people; this is one
  field cut once, with the type crossing the cut rather than sitting inside a column.
- **Responsive strategy:** the field is **never stacked** — a split that becomes two rows stops
  being one comparison. Only the stage height reduces, across three steps, and the slot labels are
  dropped at 480px where the band occupies most of the field.
- **Visual-first check:** 41 visible words, the lowest in the sector so far.

## Structural Diversity

| Study | Comparison device | Media | Cases | Conversion behaviour |
| --- | --- | --- | --- | --- |
| 001 | Side-by-side pair, 2px seam, per card | 6 in 3 pairs | Three | One closing consultation link |
| 002 | Single large diptych | 2, largest scale | One | One text link in the caption row |
| 003 | In-place state swap in a shared footprint | 6 in 3 stacked pairs, 3 visible | Three | None — the section is the comparison |
| 004 | Side-by-side pair beside a panel | 2 | One | Consultation panel with three covered items |
| 005 | One field cut once, type across the seam | 2, full-bleed | One | One text link in the closing row |

Grounds: light cool grey, soft sage-cream, deep slate-green, deep olive, deep navy-slate. None
repeats a ground used in `WELL-S01`–`S04`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 41–85 visible words per study — the leanest batch in the sector, which
  follows from the constraint: with no claims available, there is very little for copy to do, and
  the studies are carried entirely by the pairing structure.
- **Document-metaphor justification:** `NONE`. No clinical chart, evidence grid, protocol table or
  case-record device is used anywhere. The `003` switch is a segmented control, not a data view.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `003` uses radio inputs with CSS sibling selectors; the other
  four are fully static. No `<script>` element appears in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Before / After ×3 pairs | `001` — two frames per case, split by a 2px seam | Still image, 3:4 stepping to 1:1; both frames of a pair identical | Empty tonal surfaces with chips; the pair still reads as a pair when empty, which is the point of the seam |
| Before / After ×1 pair | `002` — the editorial diptych | Still image, 4:5 stepping to 3:4, at the largest scale in the batch | Empty tonal surfaces with corner marks; the caption row carries the case |
| Before / After ×3 pairs | `003` — two areas sharing one footprint per case | Still image, 4:5 stepping to 4:3; both states identical in scale and crop | Empty tonal surfaces labelled by state; the switch works and is legible with both areas empty |
| Before / After ×1 pair | `004` — the pair beside the consultation panel | Still image, 4:5 stepping to 3:4 | Empty tonal surfaces; the panel carries the section without them |
| Before / After ×1 field | `005` — two halves of one full-bleed field | Still image, filling half a stage of fixed height | Slightly different tones keep the seam visible while empty; the band keeps the name legible over either state |

Empty reserved media areas are intended output, not defects. **A filled slot in this section
requires documented client consent and a compliance review** — see the handoff note above.

**Media-density note.** No study carries more than three pairs. Density was never the risk here;
the risk was content, and it is addressed above.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse with correctly balanced, correctly ordered elements.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, gives every interactive element
  a 44px-or-greater target, and marks decorative arrows `aria-hidden`. `003`'s three radio groups
  each sit in a fieldset with a visually-hidden legend naming the treatment, so the two options are
  never announced as a bare "Before / After" with no context.
- Responsive QA: **PASS.** Four authored breakpoints per study. The decision recorded across the
  whole batch: **the pair never stacks.** Two frames placed above one another stop reading as one
  comparison, so in every study both frames narrow together instead of reflowing into a column.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status, and the
  consent requirement is held here rather than on the page.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s05-00N` root, verified by scan.
- Claims check: **PASS.** Visible text only, comments stripped, scanned for percentages, currency,
  session and week counts, and for outcome vocabulary — *results, improve, reduce, proven,
  guarantee, younger, glow, rejuvenate, transform, visible, dramatic, review, rating*. Clean in all
  five.
- Render check: **PASS, after two corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `003`'s CSS-only state swap was confirmed working — the selected option is filled and
  the frame shows the matching reserved area. Two defects were found and fixed:
  - `005`'s slot labels were vertically centred in each half, which put them directly behind the
    mid-height band; they rendered as clipped fragments either side of the treatment name. The
    labels were moved low in each half, clear of the band.
  - `004`'s panel action carried `margin-top: auto` followed later in the same rule by
    `margin-top: clamp(...)`, so the second declaration won and the button sat directly under the
    list with a large void beneath it instead of being pinned to the panel foot. The duplicate was
    removed. **This is the same defect found in `WELL-S04-004`** — a duplicated `margin-top` in a
    flex-column card — and it is worth watching for in future batches.

## Notes

- This is the fifth authored batch in the `WELL` sector and the third authored entirely without
  references.
- The constraint shaped the work rather than limiting it. With no claim available, the studies had
  to earn their difference from the pairing structure alone, which produced the leanest and most
  structurally varied batch in the sector so far.
- The consent and compliance requirement recorded above should carry to `S24`, which the sector
  brief already scopes to anonymised programme context.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
