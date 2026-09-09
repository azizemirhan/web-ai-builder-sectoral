# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S12`
- Section Name: `Client Testimonials`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S12-001` | Universal / Safe | AUTHORED | `raw/CON-S12-001.html` |
| `CON-S12-002` | Premium / Editorial | AUTHORED | `raw/CON-S12-002.html` |
| `CON-S12-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S12-003.html` |
| `CON-S12-004` | Conversion-led | AUTHORED | `raw/CON-S12-004.html` |
| `CON-S12-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S12-005.html` |

Twelfth batch in the `CON` sector, and the hardest section in it. Role and boundaries in
`./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Section Has No Writable Content At All

Harder than anything else in this sector, and structurally rather than by restriction. A testimonial
is **a quotation from a named person**, and neither half is available:

- **The words** are somebody's actual sentence. Writing one is fabricating a person's speech — the
  most serious invention available on a website and the one a reader is least equipped to detect.
- **The name** is a client's, forbidden sector-wide.
- **A rating** is anti-pattern eight, and asserts a survey nobody ran.

This is the `WELL-S25` position, and it takes the same answer:

    Reserve the quotation. Author the apparatus.

## The Governing Constraint — A Testimonial Is Worth What You Can Check

    A quotation you cannot verify is a sentence the firm wrote about itself.

So the quote is a reserved block and everything around it is the content. **The apparatus is the only
part a firm can be honest or dishonest about, which makes it the only part worth designing.** Every
quotation in the batch carries:

| Field | Treatment |
| --- | --- |
| The quotation | **Reserved block at prose cadence** |
| Name, role, organisation | **Reserved fields** |
| Will they take your call | **Real** — and the answer varies |
| Was it edited | **Real** — for length only, or not at all |
| Were they given anything | **Real** — nothing, every time |

**Thirty-nine reserved fields across the batch. Seventeen reserved quotations. Not one invented word
of client speech**, verified by reading the contents of every `<blockquote>` and requiring it to be
empty of text.

## The Reserved Quotation Is Drawn As A Quotation

Carried from `WELL-S25`: three or four bars of varying length rather than a dash. A dash says *a
value goes here*; lines say *a paragraph of somebody's speech goes here*, which tells a reviewer how
much of the finished page is not the firm's own writing. Every one is announced to a screen reader as
*Reserved area: the client's quotation, about four lines of speech*.

`005` sets them at broadside scale, which turns the honest shape of an unfilled testimonials page
into the design itself.

## The Three Groups

Clients differ in what they can agree to, and flattening that difference is the first small
dishonesty of a testimonials page:

| Group | Means |
| --- | --- |
| **Will take your call** | Named, number on request. *We do not choose which of them you ring* |
| **Quoted, not contactable** | Named, but will not field calls. A busy person, not a reluctant one |
| **Anonymous at their request** | Public bodies mid-procurement, clients under an agreement |

`003` is built entirely on this and sizes its columns to match: **the most checkable column is the
widest.** A page where the narrow column is the full one is telling you something, and that layout
would show it rather than hide it.

## The Admission, And The Offer

> **These are the clients who agreed to be quoted. The ones who did not are not here, and we are not
> going to pretend the difference is random.**

Every study carries it. `005` sets it **larger than any quotation on the page**, which is the reverse
of every testimonials section in the sector — praise is cheap to display and impossible to check; a
caveat is the reverse.

And the offer that follows, which `004` converts on:

> **Ask for the ones who are not on this page.** We will give you a reference from a job that went
> badly, and the number of the client it went badly for.

`004` breaks it into three, and the third is the one that makes it a test rather than a gesture:
**our account of what went wrong, in writing, before you ring them** — so the two versions can be
compared. It also states what it will not do: *"We will not send you somebody we have primed, and we
will not pick the least bad of the bad ones and call it candour."*

## Study Records

| Study | Ground | Model | Quotes | The move |
| --- | --- | --- | --- | --- |
| `001` | `#eceeed` | Four cards, apparatus under each | 4 | The apparatus as the readable half |
| `002` | `#fbf8f2` | One specimen at full width, then the policy in prose | 1 | **The specimen and the policy** |
| `003` | `#dee1e0` | Three unequal columns, widest most checkable | 6 | **Sorted by how far you can check it** |
| `004` | `#131a1f` | The offer as the subject, quotations demoted to a strip | 3 | **Ask for the ones who are missing** |
| `005` | `#f4f1e8` | Broadside-scale reserved quotes, footnote apparatus | 3 | The admission set larger than the praise |

### `002`, one quotation on purpose

A testimonials page wants to be a wall of praise. **A single specimen with a long explanation
underneath cannot be read as a wall**, so the form refuses the section's default before any of the
copy has to — the same move `CON-S10-002` made with columns against a product grid.

It also prints the collection process, which is real content nobody publishes: asked **at handover
rather than during**, because a client mid-job has a reason to be generous and everybody knows it;
asked **in writing**, so nobody is put on the spot in a room; and the cut sent back before it goes
up. Three sentences a firm can only write if it does them.

### `004`, the inversion

The quotations are demoted to a strip at the foot, under a heading that says what they are: *the
supporting material rather than the argument*. On this page the admission is the subject and the
praise is the footnote, which is the reverse of every other testimonials section in the sector.

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
- **Invention check: PASS.** Every `<blockquote>` in the batch contains no text — seventeen reserved
  quotations, zero invented words of client speech.
- **Cadence check: PASS.** Every reserved quotation is drawn as lines rather than a dash, and every
  one is announced to a screen reader.
- **Apparatus check: PASS.** Contact policy, editing policy and inducement policy stated in all five.
- **Attribution check: PASS.** Names, roles and organisations reserved; every field labelled.
- **Star check: PASS.** No star glyph anywhere in the batch, tested on the character rather than the
  word.
- **Admission check: PASS.** The selected-sample admission, the *not random* clause and the offer,
  all present in all five.
- **Rating check: PASS**, on the page with its declared refusal removed. No rating, score, review
  count, aggregate, average, satisfaction figure, client logo wall or review platform outside the
  blocks that name them in order to refuse them.
- **Markdown-artefact check: PASS.** Carried forward from `S09`.
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S11`.
- Render check: **PASS, no corrections.**

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `003` | **The *not random* clause was missing.** The study admitted the sample was selected but dropped the half-sentence that makes the admission mean anything | Restored |
| `002` | Its passage explaining why there is no rating was not declared as a refusal, so the hard scan read *rating* and *average* as claims | Wrapped in `data-refusal` |
| `004` | The refusal was marked on a `<p>`, which the div-depth stripper could not see | Wrapped in a `<div>` |

And one checker fault, the recurring one: **the quotation floor was set at three**, which failed
`002` — a specimen-and-policy study where showing one quotation at full size is not less honest than
showing four. Re-keyed to one, and the batch-level invention test moved off the count and onto the
thing it was actually meant to test.

## Notes

- Twelfth authored batch in the `CON` sector. `S01`–`S12` are complete.
- **The reusable outcome is that when the content of a section cannot be written, the apparatus
  around it can — and is usually the better half.** `WELL-S25` found this for an article; `S12`
  finds it for a quotation, and the result is a stronger page than an invented testimonial would
  have produced even if inventing one were allowed. Any sector whose social proof is unverifiable —
  legal, medical, recruitment, consulting — has the same page available.
- The second outcome is `003`'s: **evidence of different strengths should not be drawn at the same
  size.** A named contactable reference and an anonymous line are different objects, and a grid that
  gives them equal cells asserts they are equivalent. Sizing by verifiability makes the page
  self-reporting.
- The third is `004`'s offer, which is the most exposed sentence written for this sector: it is
  checkable in one phone call, it costs nothing to print if it is true, and it is unprintable if it
  is not. That is the only test of a testimonials page worth applying, and it is available to any
  firm confident enough to use it.
- `S13 Case Studies` is next, and `WELL-S24` has already ruled on it: **a case study is an outcome
  claim by construction**, so the answer is to document a method rather than a result.
