# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S11`
- Section Name: `Leadership Team`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S11-001` | Universal / Safe | AUTHORED | `raw/CON-S11-001.html` |
| `CON-S11-002` | Premium / Editorial | AUTHORED | `raw/CON-S11-002.html` |
| `CON-S11-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S11-003.html` |
| `CON-S11-004` | Conversion-led | AUTHORED | `raw/CON-S11-004.html` |
| `CON-S11-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S11-005.html` |

Eleventh batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Rules Were Set In Advance, And Left The Interesting Question Open

Anti-pattern thirteen forbids the wall of stock portraits; the sector direction sends this section to
the `WELL-S04` rule — **role leads, identity reserved**. So names and portraits are reserved fields,
and qualifications, memberships, years in the trade, biographies and personal detail are **omitted**
under the `WELL-S26` rule.

That settles what may appear. It leaves open what the section is *for*, and the answer is the batch:

    A team page shows you the people who win the work. You want the people who run it.

## The Governing Constraint — Ordered By Contact, Never By Seniority

The person at a tender interview is very often not the person who runs the job. It is the most common
complaint about contractors in this industry and almost no team page addresses it, because addressing
it means admitting it.

So every person in this batch carries **when you will actually deal with them** — *every day on your
site · every week · at each valuation · when the programme changes · at tender and at handover* — and
every study prints the last row:

> **The managing director decides nothing about your site day to day, and a firm where they do is a
> firm with a problem** — either the site manager has no authority or the director cannot leave it
> alone.

## The Second Half — What Each Can Decide Without Asking

The `S07` authority device, applied to people. A title tells a client nothing; an authority is
checkable by asking the person standing under it.

| Role | Decides without asking |
| --- | --- |
| Site manager | Stops the work. Orders what the day needs. Moves the sequence within the week |
| Foreman | Runs the gang. Stops the work. Calls the site manager rather than working round it |
| Contracts manager | Agrees a variation. Moves resource between sites. Is the escalation |
| Commercial manager | Agrees the valuation. Prices a change — and priced the job originally |
| Planner | Rewrites the programme. Nobody else does |
| Managing director | Changes the contract. Turns work down. **Nothing on your site** |

## Anti-Pattern Thirteen Is A Shape, Not Only A Content Rule

    No study lays the team out as a uniform grid of equal portraits.

The organising principle is contact or presence in every study, never seniority, and that produces
naturally unequal groupings. The portrait counts differ deliberately across the batch — **six, six,
two, one, six** — and the two low numbers are arguments rather than economies:

- `003` gives a face to **only the two people you will meet every day**, and says so: *"A gallery of
  six equal portraits would tell you less."*
- `004` carries **one**, because there is one person the study is about.

Portrait and reserved name sit inside a single `<figure>` in every study, carried from `WELL-S26`, so
no reflow at any width can separate a face from the name under it. The checker verifies it per
figure rather than per page.

## Study Records

| Study | Ground | Model | Faces | The move |
| --- | --- | --- | --- | --- |
| `001` | `#edeeec` | Four contact groups, most-seen first | 6 | The true order, which is the reverse of the convention |
| `002` | `#faf9f6` | Chronological prose, portraits floated into the text | 6 | **The people arrive in the order you meet them** |
| `003` | `#e2e0da` | Five stage modules — who is in the room, who has left | 2 | **Presence, stage by stage** |
| `004` | `#1a2224` | One ask, with what a straight answer sounds like | 1 | **Ask to meet the one who will run it** |
| `005` | `#141519` | Blocks scaled to contact frequency | 6 | **Size by contact, not by seniority** |

### `002`, the magazine setting proper

Floated figures with text wrapping around them — new to this catalog, whose editorial studies have so
far used a margin, a sidebar, a centred measure, a question set, an annotated margin and real
columns. It is the only one where the people are **inside** the argument rather than beside it, and
each portrait appears at the paragraph where that person enters the job.

The essay's hinge is the swap: *"Here is the swap, and it is the whole reason this page is written as
a sequence."*

### `003`, and the two faces

Five stage modules — tender, pre-start, on site, handover, defects — each marking who joins, who is
still here, and who has left. Two facts become unavoidable in a way no list makes them: **the
director leaves after tender**, and **the same site manager comes back for defects**, which is the
last module and carries one name.

The direction's trap here is the specification table, and a presence matrix is the obvious wrong
answer. Modules instead: the stages carry different numbers of people, the on-site one is twice the
size of the others, and *not in the room* is a dashed list rather than an empty cell.

### `004`, the ask that tests the page

> **Ask to meet the one who will run it.** Before you sign anything, and of every firm on your list
> including this one.

It costs the reader nothing and it is uncomfortable for any firm whose tender team and delivery team
are different people. The study also prints what a straight answer sounds like beside what a poor one
does — *"You'll be well looked after — we have a great team"* — and names its own limit:

> If your job starts far enough ahead that we do not yet know who will run it, **we will tell you
> that** rather than name somebody to win the tender and change them at pre-start.

### `005`, the inversion in pixels

Every leadership page in this industry is sized by seniority, which makes the biggest face the person
you will meet least. `005` scales the block, the portrait and the role type to **contact frequency**,
which makes the managing director the smallest block on the page — set against a wide empty column
that carries the explanation.

    That last block is the correct size, and the space around it is the point.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, remote reference, embedded image,
  inline SVG or form control anywhere in the batch.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder. `002`'s floats release
  and `005`'s scaling survives as type and portrait size after the columns collapse.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Figure check: PASS.** Twenty-one portraits across the batch, every one inside a `<figure>` with
  its reserved name in the `<figcaption>` of the same figure.
- **Reserved-field check: PASS.** Names and the site-manager count reserved; every field labelled for
  a screen reader.
- **Shape check: PASS.** No study lays its people out as a uniform three-, four- or six-across grid
  of equal portraits.
- **Device check: PASS.** Contact frequency stated in all five; the director gap admitted in all
  five; at least three named authorities per study.
- **Omission check: PASS**, on the page with its declared refusal removed. No qualification,
  membership, years-in-the-trade figure, biography, previous employer, personal detail, award or
  safety figure outside the block that names them in order to refuse them.
- **Markdown-artefact check: PASS.** Carried forward from `S09`.
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S10`.
- Render check: **PASS, no corrections.**

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `005` | A stray closing tag in the void block — caught by the nesting stack | Closed correctly |
| `004` | **No contact frequency on its one portrait.** The study argued the whole contact case in prose but never said, next to the face, why that person matters | *Every day, on your site* added to the figcaption |

And three checker faults, all of the same family:

- **The refusal was undeclared.** Every study closes by listing the credentials it omits — *no
  qualifications, no memberships, no years in the trade* — and the hard scan read that list as a
  credential claim in all five. Fixed with `data-refusal`, the pattern established in `S07` and
  reused in `S09`.
- **Two rules were keyed to phrasing.** The authority check looked for the literal label *Decides
  without asking*, which `003` states inside a figcaption and `004` states in prose; the director
  check looked for one wording of an admission `004` makes in another. Both re-keyed to the content:
  a list of the six named authorities, and five phrasings of the same admission.
- **One regex was simply wrong** — `orders what the day needs` where the prose reads *order*. It
  failed a study for a defect in the check, which is the most expensive kind of false negative
  because it looks exactly like a real finding.

## Notes

- Eleventh authored batch in the `CON` sector. `S01`–`S11` are complete.
- **The reusable outcome is that a people page should be ordered by contact, not by rank.** Every
  sector has this page and every sector builds it as an org chart with faces. Ordering by how often a
  reader will actually deal with somebody inverts it, answers the question they came with, and forces
  the one admission that makes the rest credible — that the person who sold the work is not the
  person who does it.
- The second outcome is `003`'s and `004`'s: **withholding portraits can be an argument.** Two faces
  instead of six, or one instead of six, says something a full gallery cannot — and it is the
  honest reading of anti-pattern thirteen rather than a workaround for it.
- The third is a checker discipline now proven three sections running: **a section that must name
  what it refuses needs its refusal region declared in the markup.** `S07` invented it, `S09` reused
  it, `S11` needed it in all five studies at once.
- `S12 Client Testimonials` is next, and it is the hardest section left in this sector: the direction
  forbids the satisfaction badge and every invented rating, and a testimonial is by construction a
  quotation from a client the catalog does not have.
