# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S21`
- Section Name: `Subpage Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S21-001` | Universal / Safe | AUTHORED | `raw/CON-S21-001.html` |
| `CON-S21-002` | Premium / Editorial | AUTHORED | `raw/CON-S21-002.html` |
| `CON-S21-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S21-003.html` |
| `CON-S21-004` | Conversion-led | AUTHORED | `raw/CON-S21-004.html` |
| `CON-S21-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S21-005.html` |

Twenty-first batch in the `CON` sector, and the first of the subpage architecture sections. Role and
boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — It Must Fail As An S01

The extended set's standing test:

> A study that would work unchanged as `S01` has not answered this role.

And this sector has the sharpest available way to fail it:

    A homepage hero in this sector is built around a number. An interior hero has no
    number in it at all — because the visitor already believed enough to click, and
    what they need now is to know where they are.

The sector direction records that all five supplied `S01` references were built on a counter, and
that the counter is this sector's signature device. **Withholding the signature is the discipline**,
and it is checkable: no counter, no figure, no digit in visible copy anywhere in the batch.

| Discipline | Result |
| --- | --- |
| Height | No viewport-height unit in any study |
| Voice | No proposition about the firm. The vocabulary scan bans *leading*, *trusted*, *expert*, *years of experience*, *why choose*, *our mission* |
| Actions | **One in the whole batch**, and it points into its own page |
| Subject | The title names where you are |
| Counter | None |

## The Worked Example Is A Project Page

All five studies are the hero of a project detail page — the `S24` parent. It carries the most
metadata and is the interior page most likely to be turned back into a second homepage hero.

`003` additionally shows the same slots re-labelled for the other four parents.

## The Introduction Describes The Page, Not The Project

A project name may not be invented, and neither may what the job achieved. So the orienting line does
something better:

> *What was on the site before we started, what we chose, and **the decision this one got wrong**.
> The page runs in that order.*

`S13`'s three-part device used as a **page description** — real, authorable, and more use to a reader
than a claim about a building they have not seen.

## The Hard Problem — A Reserved Title At Display Scale

The title is the largest element in a subpage hero, and in this catalog the page title is a reserved
field. Five art-directed studies running — `S08-005`, `S09-005`, `S15-005`, `S16-005`, `S18-005` —
have recorded the same lesson: **a reserved em-dash at display scale reads as a redaction.** Every
one of them solved it by keeping the reserved thing small.

Here it cannot be kept small, because it is the design. So the batch carries a rule none of the
earlier ones needed:

    Every study reserves the title, and no study uses an em-dash to do it.

The title is drawn as a labelled fill — a caption naming the field and bars at the measure the
finished title would occupy. The rule is enforced twice: the `h2` must contain a drawn fill, and
**the em-dash placeholder appears nowhere in the batch at all** — the metadata values read *Reserved*
rather than carrying a dash.

### `005`, which exists for that problem

Three ruled measures, labelled: *a short name*, *a long one*, *where it wraps*. A reviewer sees the
constraint rather than a blank, which is the only useful thing a placeholder can be when it is the
largest object on the page. Everything else in the study is deliberately small.

## No Refusal Region In This Batch

The first section in this sector with none:

> **A hero that argues with itself is not a hero.**

Every other `CON` section declares a `data-refusal` block so the vocabulary scans can run on the page
with its own refusals removed. There is nothing to remove here, so the scans run on **the whole of
the visible copy** — a stricter test, and the checker verifies the absence of the region rather than
its presence.

## Study Records

| Study | Ground | Model | Action | Media |
| --- | --- | --- | --- | --- |
| `001` | `#f2eee6` | Title, description, four-field rail, interior media band | none | reserved band |
| `002` | `#fbf9f0` | **A standfirst** — the newspaper deck | none | none |
| `003` | `#d6dade` | **The component, not one instance** — the same slots on four other parents | none | reserved band |
| `004` | `#191d1f` | A deep header carrying one anchor into its own page | **the batch's only one** | none |
| `005` | `#b8bcbb` | **The reserved title at display scale, drawn as three measures** | none | none |

### `002`, the standfirst

The one editorial form built specifically to sit under a title and say what the piece contains, and
it had not been used elsewhere in this sector. It also fails as an `S01` structurally rather than by
rule: **a deck about one project is meaningless anywhere except above that project.**

### `003`, the component

The worked project instance, then the same four slots re-labelled for a service page, a person, an
office and a journal entry. The interesting question about an interior hero is whether it survives
the pages nobody designed it for, and no single instance answers that.

The sector direction names this variant's trap as *the specification table*. The strip avoids it by
being uneven: **two parents drop the media, and one drops the fourth slot rather than filling it** —
*there is no fourth fact worth carrying here* — which is exactly what a matrix would have hidden.

### `004`, the one action

> **The only honest call to action in an interior hero is one that goes deeper into the page.**

An enquiry button here asks for a decision the page has not earned; the reader arrived to read
something and has read nothing. So the single anchor jumps to what the job cost the firm to get
wrong, and the study says why in the copy beneath it. `S20` owns the ask.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG or form control anywhere in the batch.
- **Action check: PASS.** One anchor in the whole batch, in `004`, pointing into its own page.
- **Height check: PASS.** No viewport-height unit in any study.
- **Title check: PASS.** Every title reserved, labelled as a field, drawn as a fill — and **no
  em-dash placeholder anywhere in the batch.**
- **Scope check: PASS.** Parent label, page description and all four metadata labels present in all
  five; four reserved values per study, all labelled for a screen reader.
- **Media check: PASS.** Where media appears it is a reserved area captioned as one, at interior
  scale; three of the five carry none.
- **No-refusal check: PASS.** No `data-refusal` region in any study, so every vocabulary scan ran on
  the complete visible copy.
- **S01 check: PASS.** No counter, no *years of experience*, no *leading*, *trusted*, *expert*,
  *specialist*, *why choose*, *our mission*, *excellence*, *world-class* — and no *contact us*,
  *get a quote*, *download* or *book now*, which belong to other sections.
- **Digit check: PASS.** No digit in visible copy in any of the five.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no non-ASCII character in any stylesheet, no
  accidental 8-digit hex, no `clamp()` arity error.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Markdown-artefact check: PASS.**
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S20`, and the five separate on a
  contact sheet.
- Render check: **PASS**, after one correction.

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `005` | The three measure labels were pushed to the far right of the page by a two-column grid, so each label sat a long way from the bar it names | Laid out as flex, with the bar taking a flex basis and the label following it immediately. Fill contrast raised a step at the same time |

Small, but it mattered here more than usual: the entire study is a diagram of a reserved field, and a
label that does not sit beside the thing it labels is a diagram that does not work.

## Checker Note

No rule failed a study. Two of the batch's checks are new in shape:

- **An absence check.** The `data-refusal` region is verified *not* to be present, which is the first
  time this catalog has required the absence of its own mechanism. The reason is editorial rather
  than technical: a hero that carries a refusal block is a hero that has started arguing.
- **A placeholder-form check.** The em-dash placeholder — used in every section from `S01` to `S20` —
  is banned outright here, because at title scale it stops reading as a field. It is the first time
  the catalog's own reserved-field convention has had to be replaced rather than applied.

## Notes

- Twenty-first authored batch in the `CON` sector. `S01`–`S21` are complete; the subpage architecture
  run has begun.
- **The reusable outcome is that an interior hero should withhold the device that makes the homepage
  hero work.** In this sector that is the counter. In another it might be the photograph or the
  proposition — but naming it and removing it is a sharper test than any rule about height or button
  count, and it is checkable.
- The second outcome is the placeholder. **A reserved field that becomes the design has to be
  redrawn, not reused** — and drawn as a measure rather than a blank, so a reviewer sees how much
  room the real content has.
- The third is `003`'s: **a hero study should show the component, not an instance.** The uneven strip
  — two parents dropping the media, one dropping a slot — is the only part of the batch that answers
  whether the design survives the pages it was not drawn for.
- `S22 Breadcrumb / Context Navigation` is next.
