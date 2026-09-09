# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S10`
- Section Name: `Testimonials`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S10-001` | Universal / Safe | AUTHORED | `raw/WELL-S10-001.html` |
| `WELL-S10-002` | Premium / Editorial | AUTHORED | `raw/WELL-S10-002.html` |
| `WELL-S10-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S10-003.html` |
| `WELL-S10-004` | Conversion-led | AUTHORED | `raw/WELL-S10-004.html` |
| `WELL-S10-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S10-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S05` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — Why This Section Has No Reframing

Every other constrained section in this sector had a reframing available. `S07` traded treatment
outcomes for operating commitments; `S09` traded brands for function and policy. **This one has
none.** A testimonials section is made of attributed quotations, and there is no version of a
fabricated quote that is acceptable, because the entire value of a quote is that a real person
said it.

> **The quotation structure is authored. The quotation is reserved.**

A **reserved quotation area** is a sized, labelled region where a real quote will go — the text
equivalent of the portrait slots in `S04` and the partner-mark slots in `S09`. Its size communicates
the expected length, so measure, rhythm, card balance and the behaviour of a layout under quotes of
different lengths are all demonstrable without a single invented word being put in a guest's mouth.

| Element | Treatment |
| --- | --- |
| The quotation | **Reserved area**, sized short / medium / long |
| The attribution | **Reserved token** — `Guest 01`, following `Practitioner NN` from `S04` |
| A guest portrait | **Reserved media slot** (`001`–`004`; omitted in `005`) |
| A star rating or score | **Omitted entirely** |
| How quotes are gathered | **Real content** — the only unreserved text in the batch |

**Why ratings are omitted rather than reserved.** A reserved quote area says "a quote goes here",
which is true of any business with testimonials. An empty star row says something stronger: that
this studio runs a rating system and has scores in it. That is the failure already recorded in
`S04`, where an empty credentials field would still have asserted the studio holds credentials. A
figure cannot be meaningfully reserved, so no study contains a star row, score, average, review
count or "500+ happy guests" figure — and none names a review platform, which would be an invented
brand under the `S09` rule.

**What is real here.** The gathering policy — asked for after the visit, printed as written, nothing
given in exchange — is a fact about the studio, exactly like the `S07` commitments. It is the
editorial frame of the section and appears in all five studies.

**Not present in any study:** an invented quotation, guest name, initial, age, location, photograph,
treatment attribution or occupation; a star rating, score, average or review count; a review
platform name or logo; an award, certification or press quote; an efficacy claim in any form.

## Study Records

### WELL-S10-001 — Universal / Safe

- **Structural intent / archetype:** The dependable three-up. Three quotations, plainly set.
- **Layout model:** A split header carrying the gathering policy, above three equal cards. Each
  card holds a reserved quotation area over an attribution row with a small reserved portrait.
- **The one decision that matters:** the three areas are **short, long and medium** rather than
  identical, so the study shows what a three-card row does when real quotes are not the same
  length. That is the first thing this layout will face in production.
- **Responsive strategy:** 3 → 2 columns with the third card spanning full width, then one column;
  the long area is reduced at 1024px so a full-width card does not become a tall empty box.
- **Visual-first check:** 46 visible words — the lowest band in the sector, because the content is
  reserved by design.

### WELL-S10-002 — Premium / Editorial

- **Structural intent / archetype:** One quotation, given the whole section.
- **Layout model:** A centred 50rem measure holding a small serif heading, a single large reserved
  area, a portrait and attribution beneath, and the gathering policy on a hairline at the foot.
- **The editorial decision the study records:** the area is proportioned for a **short quote at
  display size**, not a long one at reading size. That ratio is the whole point of the direction
  here, and it stays legible with the words absent.
- **Responsive strategy:** the centred measure becomes left-aligned at 480px, because centred text
  at phone width reads worse than it looks in a desktop mock.
- **Visual-first check:** 45 visible words, the lowest in the batch.

### WELL-S10-003 — Structured / Visual Modular

- **Structural intent / archetype:** Quotations sorted by what the guest came in for.
- **Layout model:** Three labelled category groups — the sector's own `Facials`,
  `Body & massage`, `Hands & feet` — with two reserved areas in each, at deliberately unequal
  lengths.
- **Content-capacity justification, and the real point:** the capacity is the grouping, and the
  **unequal heights are deliberate**. A grouped testimonial layout has to survive quotes of
  different lengths; reserving all six at one uniform size would have hidden the only structural
  problem this direction exists to solve.
- **Boundary note:** the category is an organising device for quotations. It is not attributed to
  any individual guest, which would be a fabricated treatment attribution.
- **Responsive strategy:** 3 → 2 groups with the third spanning full width and its two cards
  pairing, then one group per row.
- **Visual-first check:** 68 visible words.

### WELL-S10-004 — Conversion-led

- **Structural intent / archetype:** The method is the argument.
- **Layout model:** A cream panel carrying the gathering policy, the action, and a second route for
  guests who have already been, beside a stacked column of three reserved quotations on the dark
  ground.
- **Conversion device:** in a testimonials section the persuasive element is **how the quotes were
  collected, not what they say**. A visitor who does not trust the collection does not believe any
  of them, so the panel that carries the action carries the three collection rules with it. There
  is no score, no count and no "join 500 happy guests" — those are figures, and figures cannot be
  reserved.
- **The second route:** *Been in before? Leave one of your own.* A testimonials section has two
  audiences, and the returning guest is the one who can actually add to it.
- **Responsive strategy:** the split unstacks at 1024px with the three quotes becoming a row of
  three at equalised heights, then a single column at 768px where the three lengths return.
- **Visual-first check:** 87 visible words, the highest in the batch — all of it the gathering
  policy, which is the study's subject.

### WELL-S10-005 — Art-directed / Distinctive

- **Structural intent / archetype:** A wall of voices.
- **Layout model:** Six reserved areas of six different widths (5/4/3/4/3/5 of twelve columns) and
  three different heights, packed over an oversized decorative quotation mark.
- **Why the inequality is the device:** a wall of identically sized quotes is a grid, and real
  quotations are never the same length. The brick sizes are the study.
- **No portraits, deliberately:** at six items a portrait per brick would turn a wall of voices
  into a wall of faces, which is `S04`'s role.
- **Contrast decision:** the quotation mark sits at **1.55:1** against the ground as a watermark.
  It is decorative and `aria-hidden`, carrying no information the heading does not already carry —
  the same permission recorded in `WELL-S07-005`, and the opposite case to `WELL-S01-005` where
  low-contrast display type was the study's `h1` and had to be raised.
- **Responsive strategy:** 12 → 6 columns keeping unequal spans, then two equal columns at 768px,
  then one. The glyph is dropped only at 480px, where there is no uncovered ground for it.
- **Visual-first check:** 59 visible words.

## Structural Diversity

| Study | Topology | Reserved quotes | Lengths | Portraits |
| --- | --- | --- | --- | --- |
| 001 | Three equal cards | 3 | short / long / medium | 3 small round |
| 002 | Single centred measure | 1 | short at display size | 1 |
| 003 | Three labelled category groups | 6 | mixed, unequal within groups | 6 small |
| 004 | Policy panel beside a stacked column | 3 | medium / short / long | 3 small |
| 005 | Six unequal bricks over a watermark | 6 | three heights, six widths | none |

Grounds: pale cool sage, warm greige, pale peach, deep aubergine-brown, near-black. None repeats a
ground used in `WELL-S01`–`S09`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 45–87 visible words, the lowest band in the sector. That is a direct
  consequence of the constraint: with the quotations reserved, the only unreserved text is the
  gathering policy, and the studies differ entirely by composition.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>` element appears
  in any file in this batch, and no inline `style` attribute either — verified by scan after one
  was found and removed during authoring.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Reserved quotation ×3 | `001` — one per card, at three lengths | **Text**, replaced by a `<blockquote>` in a real implementation | Sized, labelled region; the card and its attribution row read complete while empty |
| Reserved quotation ×1 | `002` — one, at display proportion | Text | As above, at the scale the direction records |
| Reserved quotation ×6 | `003` — two per category group, unequal | Text | As above; the unequal sizes are the study's subject |
| Reserved quotation ×3 | `004` — stacked beside the panel | Text | As above |
| Reserved quotation ×6 | `005` — six unequal bricks | Text | As above |
| Guest portrait ×1–6 | `001`–`004` — small round slot in the attribution row | Still image, 1:1 | Empty tonal circle; **a filled slot means a real guest who has consented to appear** |

Reserved areas are intended output, not defects. The quotation areas are the first **text** slots
in the sector; every previous reserved area has been media.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly. Quotations use `<figure>` / `<figcaption>`, which is the right
  element pair for a quotation with an attribution.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target. The one low-contrast element in the batch is `005`'s decorative
  glyph, whose permission is recorded above.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script or
  inline style.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status. The
  reserved-area labels are field names, not commentary.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s10-00N` root, verified by scan. One inline `style="margin:0"`
  was written during authoring and replaced with a scoped class before the scan.
- **Fabricated-evidence check: PASS.** This batch's defining check. Visible text only, comments
  stripped, scanned for star ratings, `/5` scores, averages, the words *review*, *rating*, *score*,
  *verified*, review-platform names, `N+` counts, "happy clients/guests", percentages, currency —
  and for any curly-quoted run of 25 characters or more, which would indicate a fabricated
  quotation had crept into the visible copy. Clean in all five. Reserved quotation areas counted
  per study: 3, 1, 6, 3, 6 — all empty.
- Render check: **PASS, after one correction.** All five rendered in headless Chrome at 1440px and
  inspected. One defect was found and fixed in `005`: its oversized quotation mark — the study's
  stated art-direction device — **did not appear at all**. It was positioned with a negative `top`
  inside an `overflow: hidden` wall, so the glyph's ink, which sits near the top of its em box, was
  clipped away entirely; what remained was then covered by the brick backgrounds. The give-away was
  that re-rendering after a colour change produced a byte-identical PNG. Fixed by giving the wall a
  top padding band for the glyph to occupy and moving it to `top: 0`, and by raising the watermark
  tone from 1.18:1 to 1.55:1 so it reads as deliberate. The mark now appears above the bricks with
  its tails running behind them, which is the intended effect.

## Notes

- This is the tenth authored batch in the `WELL` sector and the eighth authored entirely without
  references. It completes `S01`–`S10`.
- **The reserved-text pattern is the reusable outcome.** Every sector has a testimonials or
  reviews section, and every one is a fabrication risk with no reframing available. Reserving the
  quotation as a *sized* area — rather than omitting the section, which hides the structure, or
  filling it, which invents words a real person never said — is the answer, and the sizing is what
  makes it useful rather than merely honest.
- The three evidence-shaped sections in this sector now share one rule: `S05` reserves images,
  `S09` reserves marks, `S10` reserves words. None supplies the evidence it exists to present.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
