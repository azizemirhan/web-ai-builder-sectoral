# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S24`
- Section Name: `Project Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S24-001` | Universal / Safe | AUTHORED | `raw/CON-S24-001.html` |
| `CON-S24-002` | Premium / Editorial | AUTHORED | `raw/CON-S24-002.html` |
| `CON-S24-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S24-003.html` |
| `CON-S24-004` | Conversion-led | AUTHORED | `raw/CON-S24-004.html` |
| `CON-S24-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S24-005.html` |

Twenty-fourth batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Boundary That Governed Everything

`S13 Case Studies` already owns named jobs and the device *what we found / what we chose / what it
cost us*, at one decision per case. **The risk in this section was writing `S13` again at greater
length**, and the whole batch was designed around not doing that.

    S13 is several jobs at one decision each. S24 is one job's register of change,
    and the difference is the register rather than the length.

`S21`'s hero already promises the reader *the decision this one got wrong*. **This is the section
where that promise is kept**, which is the first time in this sector that one section's copy has been
written to be redeemed by another.

## The Governing Constraint — The Record Worth Having Is The Difference

    Every project page shows what was built. The record worth having is the list of
    things that changed between the drawing and the building, and who decided each one.

Those things exist on every job, they are written down as they happen, and nobody publishes them.
They are the only content on a project page a reader with a similar building could not have guessed.

## The Four Classes, And Who Paid

| Class | Who decided | Who paid |
| --- | --- | --- |
| **Found on opening up** | Us and the designer, inside a day | The client — **and we said so before the work rather than after** |
| **The client changed their mind** | The client | The client. *What is worth recording is how fast it was priced, not that it happened* |
| **Could not be built as drawn** | The designer, on our proposal | **Nobody** — caught before anything was ordered |
| **We got it wrong** | **Us** | **Us** |

The second class is stated without complaint, which is itself the argument: *a building is designed
over a couple of years and lived in for forty, and a contractor who treats a late change as a failure
has forgotten what the building is for.*

The fourth is why the section exists.

## The Signature Refusal

> **Delivered on time and on budget** is not a claim about a project. It is a claim about a page.
>
> A job with no variations is a job nobody has looked at. Every project has a register like this one;
> the only question is whether the firm will show it to you.

Quoted rather than banned — the phrase appears in all five studies, always as the thing being
refused, which is why the vocabulary scan had to be written around it rather than against it.

## Study Records

| Study | Ground | Model | Anchors |
| --- | --- | --- | --- |
| `001` | `#eae7de` | The register as four cards, each with who decided and who paid | none |
| `002` | `#fbf7e9` | **An errata note** — for X, read Y, on whose authority | none |
| `003` | `#d2d9dd` | **Sorted by who paid**, four unequal columns ending on us | none |
| `004` | `#dce4e9` | **Ask every firm on your list for one of these** | the batch's only ones |
| `005` | `#241f1c` | **The page as a difference** — drawn against built | none |

### `002`, the errata note

The form a publisher uses to list what changed between one printing and the next. It is the exact
shape of this section's content, it is a real form with its own conventions — *for the drawings as
issued, read this* — and it had not been used in this sector.

The reason it fits is the register: **an erratum is written without embarrassment and without
boasting.** That is precisely the tone a change register needs and precisely the tone a project page
never has.

### `003`, sorted by who paid

Sorted by date a change register is a diary; sorted by trade it is an invoice; **sorted by who bore
the cost it is an account of how the job was run.** Four columns at four widths, ending on the
narrowest, which holds one entry and says *paid by us*.

The sector direction names this variant's trap as *the specification table*. Equal cells would have
invited a reader to count the entries; **these are not four comparable quantities, because one of
them is an admission**, and the study says so in its own foot.

### `004`, the ask that could fail

> **Ask every firm on your list for one of these.**

Not for our work — for a document, and one a reader can put to every contractor they are considering,
including us. The reply sorts a shortlist faster than anything else a client can request:

- **A firm that cannot produce one has not kept it**, which says how the job was administered.
- **A firm that produces one with nothing in the fourth column has edited it**, because every job has
  entries there.

Neither answer requires trusting anybody, and **the ask is deliberately one this firm could fail** —
which is the only kind of proof a page like this can honestly offer.

### `005`, the page as a difference

Two columns the whole way down — what was drawn, what was built — and **a row only where the two
disagree.** Everything that matched is absent, which is the correct amount of space to give it.

It also settles an old prohibition by replacing it. Anti-pattern ten forbids the before-and-after
pair because the two photographs are never of the same conditions. **Two columns of text are of the
same conditions**, and the study says so: that is the whole reason this comparison can be published
and that one cannot.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG or form control anywhere in the batch.
- **One-mechanism check: PASS.** One anchor, in `004`, routing in-page.
- **Class check: PASS.** All four classes of change present in all five studies.
- **Who-paid check: PASS.** Client, nobody and us all stated in all five.
- **Refusal check: PASS.** The on-time-and-on-budget phrase quoted and refused in all five, with the
  reason given.
- **Quotation check: PASS.** The client's words are a reserved space in every study. **No invented
  word of client speech anywhere in the batch** — the `S12` rule.
- **Density check: PASS.** Between fifty-one and seventy-one visible words per reserved field,
  against a floor of forty — the `S19` rule, carried into a page that could otherwise have become a
  grid of chips.
- **Placeholder check: PASS.** No em-dash placeholder; every reserved value labelled.
- **Media check: PASS.** One media area in the batch, single, and captioned *never a pair*.
- **Drawing check: PASS.** Nothing drawn at an angle.
- **No-refusal-region check: PASS.** The architecture run carries none.
- **Vocabulary check: PASS.** No *we delivered*, *ahead of schedule*, *under budget*, *zero defects*,
  *snag-free*, *flawless*, *seamless*, *before and after* or *turnkey* — and **no use of the term
  *case study***, which belongs to `S13`.
- **Digit check: PASS.** No digit in visible copy in any of the five.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.**
- Section-shell check: **PASS.**
- Scoped-CSS check: **PASS.**
- **Markdown-artefact check: PASS**, after one correction.
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S23`, and the five separate on a
  contact sheet.
- Render check: **PASS, no corrections.**

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `001` | A pair of asterisks used for emphasis in visible copy — a markdown artefact, and the sixth in this sector | Set with the catalog's own emphasis instead |
| `003` | The signature refusal named the phrase but never gave the reason | *It is not a claim about a project; it is a claim about a page* added |
| `005` | The second row described the change without naming its class, so a reader met three named classes and one unnamed | *The client changed their mind* added, in its own words |

## Checker Note

One rule was too narrow and was broadened: the *found on opening up* key, which `002` states as *the
building was not what the drawings said* — the same class in the register's own language. The other
two failures were genuine gaps in the studies and were fixed there.

The batch's own difficulty was the vocabulary scan. **The phrase this section refuses is a phrase it
also has to print**, five times, and there is no `data-refusal` region in the architecture run to
strip it. So the rule was written the other way round: the phrase must appear **and** be accompanied
by its refusal, while the claims around it — *ahead of schedule*, *under budget*, *zero defects* —
are banned outright. It is the first rule in this catalog that requires a banned phrase to be present.

## Notes

- Twenty-fourth authored batch in the `CON` sector. `S01`–`S24` are complete.
- **The reusable outcome is that a project page should publish its register of change.** What was
  built is visible in any photograph; what changed, who decided it and who paid is the only account
  of how a job was actually run, and it already exists on every job in a document nobody publishes.
- The second outcome is `004`'s: **hand the reader a test the firm could fail.** Asking a client to
  request the same document from every contractor on their list, including this one, is a stronger
  proof than any claim on the page, and it costs nothing but the willingness to be measured by it.
- The third is `005`'s: **a forbidden comparison can sometimes be replaced rather than dropped.**
  Anti-pattern ten bans the before-and-after pair because the two images are never of the same
  conditions; two columns of text are, and they carry the comparison the page actually wanted.
- `S25 Project Journal / Industry Update Detail` is next.
