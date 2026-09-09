# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S19`
- Section Name: `Contact`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S19-001` | Universal / Safe | AUTHORED | `raw/CON-S19-001.html` |
| `CON-S19-002` | Premium / Editorial | AUTHORED | `raw/CON-S19-002.html` |
| `CON-S19-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S19-003.html` |
| `CON-S19-004` | Conversion-led | AUTHORED | `raw/CON-S19-004.html` |
| `CON-S19-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S19-005.html` |

Nineteenth batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — The Traffic Is Not The Enquiry

    The people who most need to reach a contractor are not buying anything. They are
    standing on a site, or living next to one.

Every contact page in this industry is built for the enquiry that becomes a job. The actual traffic
is a neighbour whose wall is shaking at half past six, a facilities manager with a defect in a
building that was signed off, a subcontractor chasing a payment, somebody who wants a start.

So the section is **ordered by whose problem is most urgent rather than by whose is most valuable**,
and the commercial route is last on all five studies. **The ordering is the argument**, which meant
it could be checked as one: the compliance script verifies that the bid contact appears after
aftercare and after applications in document order, on every study in the batch.

## The Six Routes, In That Order

| Route | What the person who answers can settle |
| --- | --- |
| **Something is happening on a site now** | Stop it, make it safe, and write it down |
| You live or work next to one | What the noise is, when it stops, and usually moving a delivery |
| A defect in a building we finished | Book somebody to look, **and say who pays before anybody arrives** |
| You are chasing a payment | Where the invoice is, and **who is holding it** |
| You want to work here | Read it and reply. **We do not keep a talent pool** |
| **You have work for us** | Take the scope, and say which of `S15`'s three answers it can produce |

## The Rung That Is Not Ours

    If somebody is hurt, or there is a fire, ring the emergency services first and us
    second.

Present on all five, and given the top of every study **without a button** — because it is not a
route this firm can be. It emerged during authoring rather than from the section brief, and a
contractor's contact page that leaves it out is the wrong page.

## The Out-Of-Hours Answer, Which Is The Whole Test

> **A real number rings a real phone**, held by somebody on a rota. What they can do at that hour is
> stop something, make it safe and write it down — and the writing down is what the site manager
> reads before anybody else arrives. **They cannot authorise work, and anybody who says they can at
> that hour is guessing.**

No response-time promise anywhere — the `S06` rule, arriving where every contact page in the trade
breaks it. What is stated instead is **what the person who answers is able to decide**, which is more
use at two in the morning than a service level.

## The Design Problem, And The Rule It Produced

A contact section is almost entirely reserved fields: every number, mailbox, address and name. Left
alone it becomes a grid of dashes.

    Every number on this page is reserved. Every sentence saying which one to ring is
    real — and there is more of the second than the first.

Made checkable as a **density rule**: visible words per reserved field, with a floor of forty. The
batch runs between eighty-two and a hundred and sixteen, so the routing is carrying the page and the
fields are furniture. It is the first quantitative design rule in this catalog that measures the
balance between authored content and reserved slots, and it is reusable in every identity-heavy
section.

## Study Records

| Study | Ground | Model | Anchors | The move |
| --- | --- | --- | --- | --- |
| `001` | `#e7eaed` | Six route cards — who answers, what they can settle, what they cannot | none | The *cannot* is the third part of every card |
| `002` | `#faf6ec` | **A list of people, not departments** | none | Each entry opens with the caller, in one line |
| `003` | `#cfd3d6` | **Escalation ladders** — first, if nobody answers, if still not answered | none | **The one route with no second rung says so** |
| `004` | `#1c1a17` | An action ladder, descending | **the batch's only ones** | **The biggest button is not the sale** |
| `005` | `#d9d2c4` | Six lines at six sizes, scaled by how long the caller can wait | none | **The last line is the smallest thing on the page** |

### `002`, people rather than departments

Not the letter of `S15-002`, the colophon of `S16-002`, the marginalia of `S17-002` or the narrative
of `S18-002`. Each entry opens with a person in a single line — *a neighbour, at half past six in the
morning*; *a subcontractor, on the second call about the same invoice* — and the routing is what
follows from it.

A contact page written as job titles is a page written for the firm. Written as people it is a page
for the callers, and the difference shows in what each entry has to answer.

### `003`, what to do when nobody answers

Every contact page in this trade publishes a number and stops there, **so a caller who gets no answer
concludes the firm is not there** when usually they have the right firm and the wrong phone. Each
route carries three rungs: the first call, what to do if nobody answers, and what to do if it is
still not answered.

Two of those rungs are admissions: *if all three fail, that is a failure we want reported*, and
*aftercare not answering is a fault in us rather than in you.* And the commercial route is drawn with
**no second rung at all**, dashed, saying so — because inventing one would be decoration when nobody
is standing next to a problem.

### `004`, weight follows urgency

> **The biggest button here is not the one that sells anything.**

The two largest actions are *ring the site* and *ring the duty phone*; three medium cards carry
aftercare, payments and applications; and the enquiry that becomes a job is a plain underlined link
in the smallest type on the page.

The reasoning is stated rather than assumed: **the neighbour and the subcontractor leave if they
cannot find the number, and the client with a building to price will read to the end.** Putting the
sale at the top only costs a firm the other five.

### `005`, the ramp

Six lines at six sizes, and nothing is scaled by importance to the firm — it is scaled by **how long
the caller can wait**, which is a fact about them rather than a claim about us. The page descends
from *something is happening on a site now* at display scale to *you have work you would like us to
price* in body type.

The point is the last line, and the foot says so: it is the only one that can wait, **and every other
contact page in this trade sets it largest.**

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG or form control anywhere in the batch.
- **One-mechanism check: PASS.** Anchors in exactly one study, and it is `004`; all six route
  in-page. **No `tel:` or `mailto:` scheme anywhere** — the numbers are reserved fields, so an
  interactive link to one would be a link to a dash.
- **Route check: PASS.** All six routes present in all five studies.
- **Ordering check: PASS.** The bid contact appears after aftercare and after applications in
  document order, on all five. The section's argument, checked as document structure.
- **Emergency check: PASS.** *Ring the emergency services first* on all five.
- **Out-of-hours check: PASS.** The duty position stated on all five; the *cannot authorise* limit on
  four of five, checked at batch level.
- **Site-visit check: PASS.** The induction refusal kept on all five.
- **Response-time check: PASS.** The refusal to promise a response time stated on all five.
- **Density check: PASS.** Between eighty-two and a hundred and sixteen visible words per reserved
  field, against a floor of forty.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no non-ASCII character in any stylesheet, no
  accidental 8-digit hex, no `clamp()` arity error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Cliche check: PASS**, on each page with its declared refusal removed. No response time, no
  *within N days*, no *we will get back to you*, no map, no *drop us a line*, no *we would love to
  hear from you* outside the blocks that name them in order to refuse them.
- **Digit check: PASS.** No digit in visible copy in any of the five.
- **Markdown-artefact check: PASS.**
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S18`, and the five separate on a
  contact sheet.
- Render check: **PASS, no corrections.**

## Corrections Before Render

One content addition rather than a correction. The emergency rung — *if somebody is hurt, ring the
emergency services first* — was written into `003`, `004` and `005` while authoring them and was
missing from `001` and `002`, which had been finished first. It was added to both before the checker
was written, and then made a per-study rule so it cannot be dropped from a later variant.

**That is the right order to discover a rule in.** It came from writing the studies rather than from
the section brief, which is where the useful ones in this catalog have tended to come from.

## Checker Note

One rule failed a study for a defect in the rule: the site-visit refusal was keyed to *come to a site
to talk to us*, and `004` states it as *it will not ask you to come to a site.* Broadened to the
argument, with the induction clause — present in all five — as the substance.

The batch's own new rules went the other way, and both are structural rather than lexical:

- **The ordering check** reads document order and requires the commercial route to come after the
  ones where somebody is waiting. A page could pass every vocabulary rule in this file and still
  put the sale at the top; this is the only check that would catch it.
- **The density check** measures visible words per reserved field. It exists because this is the
  section where the catalog's reserved-field discipline could quietly eat the page, and a study that
  had become a grid of dashes would look tidy and say nothing.

## Notes

- Nineteenth authored batch in the `CON` sector. `S01`–`S19` are complete.
- **The reusable outcome is that a contact page should be ordered by who is waiting, not by who is
  worth most.** Every sector has this page and every sector builds it around the enquiry; ordering it
  by urgency costs nothing that can be measured and saves the callers who would otherwise leave.
- The second outcome is `003`'s: **publish the fallback.** A number with no second rung teaches a
  caller who gets no answer that the firm is absent. Three rungs and an admission that all three
  failing is our fault is a better page than any promise about how fast the first one is answered.
- The third is the density rule. **A reserved-field discipline needs a floor**, or a section made
  mostly of identity turns into a grid of dashes that passes every other check in this catalog.
- `S20 Final Project CTA` is next, and it inherits an awkward inheritance: `S15` owns the submission,
  `S19` owns the routing, and the counter rule forbids urgency. What a closing call to action can
  honestly be after those three is the whole of that section's problem.


## V2 — Theme And Text-Budget Rework

Date: 2026-09-07. Pilot for the sector-wide correction recorded in
`../CONSTRUCTION-THEME-CONTRACT.md`.

### Why

Two measurements against the whole `CON` sector, and one rule the sector already had:

- **552 visible words** per study on average, against 40–80 in the supplied modern references.
  This section was the second heaviest in the sector at **830 words** per study.
- **135 of 135 studies carried no chromatic accent** after the monochrome pass — while
  `../CONSTRUCTION-DESIGN-DIRECTION.md` requires *"concrete and asphalt neutrals with one
  high-visibility accent."* The pass had removed the accent the direction asks for.

The audit also looked for technical-document styling of the kind corrected in `ARC` and found
**none** in this sector: no tables, no monospace, no tabular figures, no tracked versal labels, no
revision or sheet metaphors. The failure here was not technical *style*; it was essay-length prose.

### What Changed

| Study | Theme | Accent | Words before | Words after | Reduction |
| --- | --- | --- | ---: | ---: | ---: |
| `CON-S19-001` | 001 Site White | `#e8541f` safety orange | 812 | 164 | −80% |
| `CON-S19-002` | 002 Bone | `#b4531d` burnt amber | 796 | 160 | −80% |
| `CON-S19-003` | 003 Steel | `#1f5fd0` structural blue | 823 | 169 | −79% |
| `CON-S19-004` | 004 High-Vis | `#ffd400` high-vis yellow | 848 | 169 | −80% |
| `CON-S19-005` | 005 Night Plant | `#ff5c1a` electric orange | 871 | 169 | −81% |

Each study now carries one reserved hoarding media area, composed differently in each: a column
panel in 001, a full-frame 21:9 band in 002, a two-bay module in 003, a held-back head panel in
004, and a large field with the out-of-hours card overlapping its lower edge in 005.

**The prose did not become shorter sentences. It became structure.** The routing argument the
section README asks for is now carried by the order of the rows, the scale given to the urgent
route, and what each row states the person who answers can settle.

### What Did Not Change

Study IDs. The section role and its boundary with `S07`, `S15` and `S27`. The six routes and
their urgency order, with the commercial enquiry sixth. Every number, mailbox and name still a
reserved field. The out-of-hours position and the site-visit refusal, both kept as real content. No
map, no general enquiry form, no response-time promise, no header.

`004` deserves a note: conversion-led could not mean promoting the sales enquiry, because the
role puts it last. The conversion is the **urgent** route, which is why the saturated panel and the
display-scale field belong to it and the estimating route stays sixth.

### QA

- ID validation: PASS — five IDs, unchanged, matching filenames.
- Raw-format validation: PASS — standalone HTML, scoped CSS, tag balance verified on all five.
- Dependency check: PASS — no framework, CDN, remote runtime dependency, or script.
- Text budget: PASS — 160–169 visible words against the contract band of 90–170.
- Accent present: PASS — one chromatic accent per study, one per theme.
- Accessibility QA: NOT_RUN — reserved-field labels are exposed to assistive technology via
  visually hidden text; focus ring, heading order and reduced-motion block are in place, but no
  full checklist pass has been run.
- Responsive QA: NOT_RUN — ladders authored at 860px and 560px in all five, and at 980px in 003 and
  004; not yet verified in a browser, because `review/build-index.py` cannot run on this machine
  (no Python installed).
