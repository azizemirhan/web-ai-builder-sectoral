# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S09`
- Section Name: `Company Stats`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S09-001` | Universal / Safe | AUTHORED | `raw/CON-S09-001.html` |
| `CON-S09-002` | Premium / Editorial | AUTHORED | `raw/CON-S09-002.html` |
| `CON-S09-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S09-003.html` |
| `CON-S09-004` | Conversion-led | AUTHORED | `raw/CON-S09-004.html` |
| `CON-S09-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S09-005.html` |

Ninth batch in the `CON` sector, and **the section the sector direction's governing constraint was
written for.** Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Content Was Already Decided. The Shape Was Not.

The sector direction fixed every figure in this sector before any section was authored: year
founded, projects completed, people employed and largest project by value are **reserved fields**;
happy clients, satisfaction, on-time and awards are **omitted**; safety figures are **forbidden**.

So this batch had no content decisions left to make, which turned out to be the useful constraint.
What it had instead was the one design question nobody in the industry asks:

    A date, a running total, a snapshot and a single extreme are not the same kind
    of number, and drawing them as one asserts that they are.

## The Governing Constraint — Four Different Quantities, Four Identical Boxes

Every contractor's stats band is a row of four equal cells. **That row is the lie, and it is a design
lie rather than a copy one.** Look at what is actually in it:

| Figure | What kind of quantity | What the identical box hides |
| --- | --- | --- |
| **Year founded** | A fixed point in the past | It is not a score. It does not grow because the firm is good |
| **Projects completed** | A cumulative running total | Meaningless without *since when*, and without a definition of *project* |
| **People employed** | A snapshot, true today | Presented as permanent when it is provisional |
| **Largest project by value** | A single extreme | Read as typical, which is exactly what it is not |

**No study in this batch contains a row of four identical cells**, and the checker tests for it. Each
figure is drawn as the kind of quantity it is:

- a **point on a rule** for the date, with the dot marking it,
- an **accumulating stack** for the running total,
- a **dashed frame** for the snapshot, because it is provisional,
- **one spike against ordinary bars** for the extreme.

Each kind also carries its own marker *shape* as well as its own tone — circle, square, diamond,
triangle — so the distinction survives without colour.

## Every Figure Carries Its Basis

A number without a denominator is a shape rather than a fact, so each figure carries a **second
reserved field**: *under this name since*, *counted since* and *a project means*, *as at* and *on our
own books*, *that one job, completed*. **Ten reserved fields in every study.**

A reviewer sees not only the four numbers the finished page will assert but the qualifications that
make them readable — which is the difference between a reserved counter that works and one that is
merely blank.

## The Sentence This Section Is Built Around

> **The largest project we have done is not the size of project we usually do.**

It is the figure most designed to be misread, and the misreading runs in the direction that costs
the reader something: it is what makes somebody with an ordinary job decide they are too small to
ask. Every study prints the correction beside the figure rather than in a footnote, and the checker
requires it.

## Study Records

| Study | Ground | Model | The move |
| --- | --- | --- | --- |
| `001` | `#eef1ef` | Four figures, each drawn by kind, over the trades list and refusal | The four geometries, stated plainly |
| `002` | `#fbf9f5` | Annotated text — prose wide, figures small in the margin | **The number is smaller than the sentence about it** |
| `003` | `#e8e6e0` | A deliberately unequal grid under a legend of the four kinds | **The grid is unequal on purpose** |
| `004` | `#f5f3ef` | Compact figures over a dark action panel | **The useful number is the one nearest yours** |
| `005` | `#12161f` | Four full-width bands, different internal geometry, poster scale | Same size, four different shapes |

### `002`, the inversion that only an editorial study could make

Every stats band sets the figure at display scale and the label at caption scale. `002` reverses the
proportion: the reserved figures sit small and precise in the margin, and the prose that explains
them takes the width. **The number is the part nobody can evaluate; the sentence is the part that
makes it readable**, so the sentence gets the room.

It is also the only study in the batch where the margin entries are *aligned to the paragraphs that
discuss them*, so neither column reads on its own.

### `003`, the trap as the subject

This direction's usual answer to four figures is four equal cells — which is precisely what the
section exists to argue against. So the grid is unequal by construction: the date is a wide shallow
band across the full width, and the other three sit at five, four and three columns. A legend of the
four kinds sits above it, because a reader who takes nothing else should take the distinction — it
transfers to every other contractor's stats band they will look at today.

### `004`, converting by giving the number away

The largest-project figure exists to attract larger projects. `004` converts by offering the
opposite:

> **Tell us the size of yours and we will send the three most like it.** Not the three largest.

And says why it is giving that away: *"If your own job is ordinary, the honest thing we can offer is
the ordinary ones — and those are the jobs a client can actually check on."* A firm that leads with
its largest project is fishing for larger ones; a firm that offers the comparable is answering the
question the reader actually has.

## The Only Real Thing On The Page Is The Part That Is Not A Number

Sectors and trades are generic vocabulary and are therefore real. Every study carries them and every
study says so:

> Everything on this page with a figure in it is reserved. The only thing we can state outright is
> the list with no number attached to it.

## The Refusal

Each study names the absent figures and explains them in the client's interest: *happy clients* is a
client list with a compliment attached and nobody ran the survey; a satisfaction or on-time
percentage asserts a measurement system, and the definition of *on time* belongs to whoever reports
it; an award is a body the firm chose making a judgement it paid to enter. Safety figures are absent
for the harder reason set out in `S07`.

    If a figure is countable and it is not one of the four, it is a claim rather than a count.

Because the content requires naming these to reject them, each study marks its refusal with
`data-refusal` and the checker permits the vocabulary only inside it — the pattern established in
`S07`, reused without modification.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, remote reference, embedded image,
  inline SVG or form control anywhere in the batch.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Kind check: PASS.** All four kinds of quantity distinguished in all five studies.
- **Basis check: PASS.** Ten reserved fields per study, every one labelled for a screen reader.
- **No-equal-row check: PASS.** No study lays its figures out as four identical cells.
- **Correction check: PASS.** The largest-project caveat present in all five.
- **Real-content check: PASS.** The non-numeric trades list present and identified as such in all five.
- **Refusal check: PASS.** Region declared in all five; the explanation, not merely the omission,
  present in all five.
- **Fabricated-proof check: PASS**, on the page with its declared refusal removed. No digit in
  visible copy, no percentage, no trend or growth claim, no award, rating, safety figure or urgency
  device.
- **Markdown-artefact check: PASS.** Added after one slipped through — see below.
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S08`.
- Render check: **PASS, one correction.**

## Corrections

| Study | Was | Now |
| --- | --- | --- |
| `001` | A backtick-quoted section reference had leaked from the authoring notes into visible copy, where it would have rendered literally | Rewritten as plain prose; a markdown-artefact check added to the batch checker |
| `005` | The reserved dash at poster scale read as a redaction mark rather than as a value waiting to be entered | A fill rule under each value, exactly the fix `S08-005` required |

The second is the same fault `S08` recorded, arriving in the next section and fixed from the note
rather than rediscovered: **when a reserved field is enlarged to carry the design, the placeholder
has to be redrawn as well.**

The first is new and worth a check of its own. The authoring notes in these files use backticks for
section references, and one crossed into the body. It is invisible to every content rule in the
checker — it is not a digit, not a forbidden word, not a fabricated figure — and it would have
shipped as a literal backtick on a finished page.

## Notes

- Ninth authored batch in the `CON` sector. `S01`–`S09` are complete.
- **The reusable outcome is that a stats band's dishonesty is in its layout, not its numbers.** Four
  equal cells assert that four different kinds of quantity are commensurable. Every sector with a
  counter row — agencies, SaaS, clinics, universities, charities — has the same latent problem, and
  the fix costs nothing: draw each figure as the kind of quantity it is, and print what it is counted
  against.
- The second outcome is that **this batch had no content decisions available and was better for it.**
  With all four values reserved and the omissions fixed by the sector direction, the only thing left
  to author was the shape — which is where the section's real argument turned out to live.
- The third is `004`'s: **the honest conversion is to give away the number's advantage.** The largest
  project exists to attract larger ones; offering the comparable instead answers the question the
  reader actually has and can be checked by phoning somebody.
- The `S05`/`S06`/`S07`/`S08`/`S09` run now shows the field-versus-figure test resolved five
  different ways in five consecutive sections — demote, omit, omit for another reason, reserve and
  enlarge, reserve and qualify. That sequence is the clearest demonstration in the catalog that the
  test is a method rather than a rule of thumb.
- `S10 Equipment Fleet` is next, and `S05` has already fenced it: plant appeared there as one of
  three families with a line each, and `S10` is the plant itself at length.
