# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S22`
- Section Name: `Breadcrumb / Context Navigation`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S22-001` | Universal / Safe | AUTHORED | `raw/CON-S22-001.html` |
| `CON-S22-002` | Premium / Editorial | AUTHORED | `raw/CON-S22-002.html` |
| `CON-S22-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S22-003.html` |
| `CON-S22-004` | Conversion-led | AUTHORED | `raw/CON-S22-004.html` |
| `CON-S22-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S22-005.html` |

Twenty-second batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — A Trail Shows One Path And Hides The Others

    A breadcrumb shows one path. A project belongs to at least three, and the two it
    does not show are the ones a reader is most likely to want.

A project page sits under a sector, under a service, under the year it finished and under the office
that ran it. The chrome picks one and the reader never learns the rest exist. So every study shows
the trail, **says which axis it runs on**, and names the memberships the trail is hiding.

## Next By What?

    Every site in this trade has a next arrow, and none of them says what it is next
    by. It is almost always the order the pages were published in, which is an order
    nobody reading has any interest in.

Declaring the ordering costs a line and turns a decorative arrow into navigation. All five studies
declare it; all five name the publication ordering and refuse it.

## Two Refusals That Are Really Design Rules

| Refusal | What it prevents |
| --- | --- |
| **A crumb that cannot be visited is not drawn as a link** | The invented intermediate level — *Home / Our Work / Commercial / Retail / Project*, where two of those are not pages |
| **The last step is not a link to the page you are already reading** | The self-link, which is in almost every implementation of this component |

`003` demonstrates the first rather than asserting it: its third trail has no index page behind the
middle level, and that level is drawn as a dashed label rather than styled to look like the two above
it. **The commonest lie in the component, told honestly.**

## Study Records

| Study | Ground | Model | Links |
| --- | --- | --- | --- |
| `001` | `#e9edea` | Trail, axis stated, *also in*, next with declared ordering | 7 |
| `002` | `#fdfbef` | **A note on the arrangement** | 7 |
| `003` | `#ccd4da` | **Three trails, one page** — in use, available, and one incomplete | 9 |
| `004` | `#101418` | **Next by what?** — three orderings, the default declared | 9 |
| `005` | `#c2bcb2` | **The whole component as one sentence** | 8 |

### `002`, the note on the arrangement

The short paragraph an index or a catalogue carries to say how it has been ordered and what that
ordering costs. It is a real book form, it had not been used in this sector, and it is the only
editorial register that fits a navigation component — **because the honest problem with a breadcrumb
is an arrangement problem, and this is the form invented to describe one.**

### `004`, the three orderings

The default is *by the same sector*, because it is the ordering the trail already implies. The third
is *by the same problem* — occupied while we worked, a structure nobody had opened, a start nobody
could move — and it is offered with the caveat that **it is a judgement rather than a field:
somebody decided these two jobs were alike, and that somebody can be wrong.** That is why it is not
the default.

The conversion claim is stated honestly too: the only thing this component can ask for is that a
reader reads another page, and the way to earn it is to say what the next page has to do with this
one.

### `005`, prose navigation

No trail at all. The whole component is one sentence at reading scale, with the links inside the
prose and **the one phrase that is not a link being the page you are already reading** — marked with
a dotted rule rather than left to be discovered by pressing it.

A row of chevrons can only draw a line, and this page belongs to four places at once. The sentence
holds all four, names the axis the site is arranged on, and states what the next page is ordered by —
which is more than the convention it replaces manages. It still answers the three questions a
breadcrumb has to answer, which is the only test that matters for replacing a convention.

## The Architecture Run's Placeholder Convention

Carried from `S21` and now confirmed as a run-wide rule:

    The em-dash placeholder is not used in the architecture sections. In navigation a
    dash reads as a broken link.

Reserved values read as the word *Reserved*. The checker verifies the em-dash placeholder is absent
from every study, and that every reserved value is immediately preceded by its screen-reader label.

## Links Rather Than One Mechanism

This is the one section in the sector where links are the content, so the usual
*one-mechanism-in-one-study* rule does not apply. Instead every anchor in the batch routes in-page —
between seven and nine per study — and **no study carries a button or a form**, because a breadcrumb
with a call to action in it has stopped being one.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG, form or button anywhere in the batch.
- **Link check: PASS.** Every anchor in every study routes in-page; no `tel:` or `mailto:` scheme.
- **Three-questions check: PASS.** Where am I, what else is this under, and what is next and by what
  — answered in all five.
- **Ordering check: PASS.** *By the same sector* declared in all five; the publication ordering named
  and refused in all five.
- **Self-link check: PASS.** Stated in all five.
- **Invented-level check: PASS.** Stated in all five, and drawn in `003`.
- **Placeholder check: PASS.** No em-dash placeholder in the batch; every reserved value labelled.
- **No-refusal check: PASS.** No `data-refusal` region, so every vocabulary scan ran on the complete
  visible copy.
- **Vocabulary check: PASS.** No position count, no *back to top*, no *you are here*, no sitemap
  diagram, no *view all*, and none of the other sections' devices.
- **Digit check: PASS.** No digit in visible copy in any of the five.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no non-ASCII character in any stylesheet, no
  accidental 8-digit hex, no `clamp()` arity error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Markdown-artefact check: PASS.**
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S21`, and the five separate on a
  contact sheet.
- Render check: **PASS**, after one correction.

## Corrections Before Render

Two content gaps caught by the checker, and one thing found by looking.

| What | Fix |
| --- | --- |
| `001` and `004` did not state the self-link refusal, which `002`, `003` and `005` did | Added to both, and the rule tightened from batch-level to per-study |
| `005` carried only two reserved values — its prose named the categories and hid the values behind the links | The sector value brought into the sentence. A reader of the other four studies can see which sector the page is in; a reader of `005` could not |
| **A reserved chip inside a link looked identical to the reserved chip that is the current page** | Every study given a rule underlining reserved values that are links. In a navigation component that distinction is the whole point, and it was invisible |

The last one is the interesting one, and no rule would have caught it. **The checker verified that
the current page is not a link and that every value is a labelled field — both true, and the render
still showed two chips a reader could not tell apart.** It took looking at the picture.

## Checker Note

One rule was written too narrowly and then tightened rather than loosened, which is the opposite of
this catalog's usual correction. The self-link refusal was set at batch level expecting some studies
to omit it; two did, and on inspection **there was no good reason for either to** — it is a rule
about the component, not a flourish some variants can skip. So the studies were changed and the rule
was raised to per-study.

## Notes

- Twenty-second authored batch in the `CON` sector. `S01`–`S22` are complete.
- **The reusable outcome is that a breadcrumb should say what it is ordered on.** Both halves of it:
  the trail names its axis, and the next link names its ordering. Neither costs more than a line, and
  between them they turn the least-read component on a site into the only one that admits it made a
  choice.
- The second outcome is `003`'s: **draw the broken level rather than hiding it.** Every site has a
  category with no page behind it; styling it like a link is the commonest lie in this component, and
  a dashed label is both more honest and more useful.
- The third is `005`'s: **a convention is not a requirement.** A row of chevrons can only draw a
  line. A sentence can hold a hierarchy, three cross-memberships and an ordering, and say what each
  one is — and it still answers the three questions, which is the only test that licenses replacing
  a convention.
- `S23 Construction Service Detail` is next, and the detail-page run begins.
