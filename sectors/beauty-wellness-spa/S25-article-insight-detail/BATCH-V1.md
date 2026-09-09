# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S25`
- Section Name: `Wellness Article / Guide Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S25-001` | Universal / Safe | AUTHORED | `raw/WELL-S25-001.html` |
| `WELL-S25-002` | Premium / Editorial | AUTHORED | `raw/WELL-S25-002.html` |
| `WELL-S25-003` | Dense / Information-heavy | AUTHORED | `raw/WELL-S25-003.html` |
| `WELL-S25-004` | Conversion-led | AUTHORED | `raw/WELL-S25-004.html` |
| `WELL-S25-005` | Sector-native / Distinctive | AUTHORED | `raw/WELL-S25-005.html` |

Fifth batch in the extended architecture set. Role, constraint and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — The Only Section Whose Content Is Entirely Unwritable

`S18` reserved the article title. `S21-003` and `S22-002` inherited that reservation for the hero
and the trail. **`S25` is where the consequence lands in full: the title is reserved, the standfirst
is reserved, and the body *is* the article.** No part of the content proper can be written.

    Reserve the article. Author the apparatus around it.

Which turns the section into a real design problem rather than an empty one:

    What does a reading page look like when the reading is not written yet?

**The reserved body is not a gap — it is the demonstration.** Blocks set at real prose cadence on
the real measure let a reviewer judge line length, paragraph rhythm and heading hierarchy before a
word exists. The scaffold says this role *"is judged on reading comfort"*; these studies can be
judged on exactly that while carrying no prose at all. Every study declares its measure in `ch` on
the body element, and the checker verifies each sits between 50ch and 75ch:

| Study | Measure |
| --- | --- |
| 001 | 66ch |
| 002 | 58ch |
| 003 | 64ch |
| 004 | 64ch |
| 005 | 62ch |

**Blocks vary in height on purpose.** Uniform blocks look like a wireframe and tell a reviewer
nothing; long, short, long, short reads as prose does.

## What Is Authorable — The Apparatus

Everything that is not the article, and there is more of it than expected:

1. **The limits line** — present in all five, and on a page whose body is empty it is the only real
   prose on the screen.
2. **The editorial policy** — who writes these, when they are corrected, what is not covered, and
   that nothing is sponsored. `003` gives it a panel; `002` compresses it to two sentences.
3. **The refusal list** — `004`'s device, below.
4. **The treatment the piece concerns**, from the real `S02` vocabulary.
5. **Related reading**, as reserved titles on the `S18` pattern.

**Not present in any study:** an invented title, standfirst, body sentence, sub-heading, pull quote,
author name, publication or date; a citation or source list; a reading time, view, share or comment
count; an efficacy or ingredient-action claim; a named condition; a newsletter field, sponsored
label, affiliate link or product. **No digit appears in visible copy anywhere in the batch.**

**Citations are omitted, not reserved.** The scaffold rules out fabricated citations, and an empty
citation slot asserts a research practice the studio may not have — the `S10` empty-star failure
again.

## The Second `<nav>` Exception, Recorded

`S22` established that the section-shell prohibition on `<nav>` targets **global site chrome**, not
the element. `S25-003` is the second case: in-page contents are in this role's own In Scope, and a
document's table of contents is a navigation region belonging to that document, so it is
`<nav aria-label="On this page">`. The checker permits `<nav>` **only in `003`** and only with an
accessible name; `001`, `002`, `004` and `005` are checked for zero.

## Study Records

### WELL-S25-001 — Universal / Safe

- **Layout model:** Reserved title and standfirst, a metadata kicker, the reserved body with two
  reserved sub-heads and one captioned in-body media area, then the limits and related reading.
- **The scaffold's two media rules, both honoured visibly:** the media area is held to the reading
  measure rather than breaking out of it, and it carries a `<figcaption>` written for the reader
  rather than an alt attribute alone. The checker verifies every `<figure>` has a `<figcaption>`.
- **Related reading uses reserved title lines**, on the `S18` pattern — the kind is real, the title
  is not.

### WELL-S25-002 — Premium / Editorial

- **Layout model:** One 58ch column and nothing beside it. Reserved title at display scale, a
  reserved pull-quote area, and the limits and policy as the only real prose.
- **The measure is the subject.** With the article unwritten, the only thing this page can be judged
  on is how it will read, so the study spends everything on the column, the outer margin and the
  cadence. Narrowest measure in the batch, and the only one with no media at all.
- **The pull quote is a reserved area, not a written line** — a pulled quotation is still the
  article's own words.

### WELL-S25-003 — Dense / Information-heavy

- **Layout model:** In-page contents in a rail beside the reading column, four reserved sections, a
  footnote area, and the editorial policy in full at the foot.
- **The device — the editorial policy is the dense content.** With the article unwritable, what
  fills a dense variant is everything a reader of a wellness guide should be told and never is: who
  wrote it, when it is corrected, what is not covered, and that nothing is sponsored. **The
  correction date is shown beside the publication date rather than hidden**, which is the detail
  that makes the rest credible.
- **The rail is not sticky, by decision.** A sticky rail on a reading page competes with the text it
  is meant to serve; the scaffold rules against exactly that for this role. It moves **above** the
  reading column at 900px rather than narrowing the measure. Checked: no `position: sticky` in any
  study.
- **Footnotes are reserved lines inside a real `<ol>`**, so the numbering is the browser's rather
  than invented content.

### WELL-S25-004 — Conversion-led

- **Layout model:** The reading column, then one held panel: the treatment this guide is about, one
  action, and the list of things this page will not do.
- **What an article page converts to, honestly.** Not a booking — `S20` owns the closing ask, and a
  guide that ends in a booking button is *marketing copy dressed as editorial*, which this role's
  scaffold rules out by name. It converts to the thing the reader is already thinking about: the
  treatment the guide describes, or a question answered directly.
- **The refusal list is the device.** Every wellness article page in the world ends in a newsletter
  capture, a products rail, an affiliate link or a sponsorship disclosure buried at the foot. This
  one prints that list and says it does none of them: *"Ask for your email. Sell you a product.
  Follow you around. Pretend to be advice for you."* It costs nothing, it is entirely authorable,
  and on a page whose article is unwritten it is the most persuasive content available.

### WELL-S25-005 — Sector-native / Distinctive

- **Layout model:** The piece shown as **the printed sheet it already is** — one pale sheet on a
  stone ground, ruled at head and foot like the aftercare paper the studio hands over.
- **Why this is sector-native:** `S18` established the fact this rests on — these pieces exist on
  paper first, are handed to you at the end of an appointment, and mostly end up in a bag. The web
  version is the same sheet, kept somewhere findable. **No other sector's article page would be
  designed from a piece of paper somebody was given.**
- **The form carries the honesty position by itself.** A sheet you were handed in a room has no
  newsletter box on it, carries no advertising, and does not pretend to know your face — and neither
  does this. `004` has to *say* it; `005` simply *is* it.
- **"Given out since" is a reserved date field**, which is the right metadata for a sheet that is
  reprinted rather than published once.

## Structural Diversity

| Study | Shape | Body treatment | Media | Ground |
| --- | --- | --- | --- | --- |
| 001 | Sheet, single measure | Reserved prose + 2 sub-heads | 1 in-body, captioned | Pale sage `#d5dbd0` |
| 002 | One narrow column | Reserved prose + pull quote | **None** | Warm sand `#e8e0ce` |
| 003 | Contents rail + column | Reserved prose + 4 sections + notes | **None** | Pale blue-grey `#c2ccd2` |
| 004 | Column + refusal panel | Reserved prose + 1 sub-head | 1 lead, captioned | Deep slate `#2b2f3d` |
| 005 | A printed sheet | Reserved prose + 2 sub-heads | **None** | Mid stone `#b6ada0` |

Grounds do not repeat any of the 120 already in use; selected by measuring channel distance against
every existing ground.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy — which is unusually
  literal here, since none of them has any article copy at all. The differentiator is how a reading
  page is composed around an absent article.
- **Document-metaphor justification:** `005` uses a printed sheet. **Licensed**, on the same grounds
  as `S18-005`: the studio genuinely prints and hands over these notes, so the metaphor names a real
  artefact rather than dressing web content as paper.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `003`'s contents are plain anchor links — already plain markup, so
  the scaffold's degradation requirement is met by construction. No progress indicator anywhere,
  since one cannot exist without script.

## Media Slots

| Slot | Study | Expected Type | Caption |
| --- | --- | --- | --- |
| In-body image | `001` | Still image, 16:9, held to the 66ch measure | Visible `<figcaption>`, written for the reader |
| Lead image | `004` | Still image, 21:9 (3:2 below 560px) | Visible `<figcaption>` |
| Article title | all five | **Text** | Reserved area at title scale |
| Standfirst | all five | **Text** | Reserved area |
| Body paragraphs | all five | **Text** | Reserved blocks at prose cadence |
| Sub-headings | 001, 002, 003, 004, 005 | **Text** | Reserved bars at heading scale |
| Pull quote | `002` | **Text** | Reserved area with a rule |
| Footnotes | `003` | **Text** | Reserved lines in a real `<ol>` |
| Author, publication, correction date | 001, 003 | **Text** | Reserved fields with visually hidden labels |

Two image areas in the whole batch, both captioned. Three studies carry no image at all.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- Territory validation: **PASS.**
- Heading-level check: **PASS.** No `<h1>`; each labelled by an `<h2>`, as in `S23` and `S24`.
- **`<nav>` check: PASS.** Present only in `003`, exactly once, with an accessible name; zero in the
  other four.
- **Reading-measure check: PASS — this batch's defining check.** Every study declares a measure in
  `ch` between 50 and 75, on the body element rather than on a wrapper, so it stays stable when the
  type scale changes.
- **Caption check: PASS.** Every `<figure>` has a `<figcaption>`; no media area relies on alt text
  alone, which the scaffold requires by name.
- **No-sticky check: PASS.** No `position: sticky` anywhere — a reading page's rail must not compete
  with the text.
- Accessibility QA: **PASS.** `aria-labelledby`, `prefers-reduced-motion`, 46px-plus targets,
  reserved fields with visually hidden labels.
- Responsive QA: **PASS.** The measure is held at every width in all five; `003`'s rail moves above
  the column rather than narrowing it.
- Dependency validation: **PASS.** No form, field or select anywhere — which is also the hard check
  against a newsletter capture.
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No `<header>` or `<footer>` anywhere.
- Scoped-CSS check: **PASS.**
- **Metric, citation and claim check: PASS.** No digit in visible copy; no reading time, view, share
  or comment count; no citation, source or reference; no efficacy vocabulary; no named condition.
- **Limits-statement check: PASS.** All five carry both halves of the sentence.
- **Soft check, twelve occurrences, all verified in context:** every *advice*, *sold*, *paid*,
  *advertised*, *subscribe* and *sponsored* sits inside a refusal or inside the medical-limits line.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. First batch in the extended set to need no render correction at all.

## Notes

- Twenty-fifth authored batch in the `WELL` sector, twenty-third without references, fifth of the
  seven extended architecture roles.
- **The reusable outcome is that a reserved body can be judged.** A placeholder article page is
  normally either fake prose or a grey wireframe, and neither can be assessed. Blocks set at true
  prose cadence on a declared measure can be — line length, rhythm and hierarchy are all visible.
  Any sector whose detail pages carry unwritable copy can use this directly, and the check that
  makes it real is trivial: **the measure must be declared in `ch`, on the text element, between 50
  and 75.**
- The second outcome is `004` and `005` answering the same question two ways. `004` **states** the
  refusals; `005` **embodies** them by taking the form of a sheet somebody was handed, which cannot
  have a newsletter box on it. Stating a position and choosing a form that makes the position
  structural are both valid, and having both in one batch is what makes the pair worth keeping.
- One checker refinement, now a standing rule: **check the mechanism hard, the vocabulary soft.**
  `subscribe`, `sponsored` and `affiliate` moved to the soft tier because the refusal list is this
  batch's device and a study must be able to name what it refuses; the hard check is the absence of
  any `<form>`, `<input>`, `<textarea>` or `<select>`, which is what an actual capture would need.
  That is a better test than the word ban was.
- `S26` is next: Practitioner / Specialist Profile — where the `S04` rule (role leads, identity
  reserved) meets a page whose entire subject is one person.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch,
  because `python3` on this machine resolves to a Windows Store placeholder rather than an
  interpreter.
