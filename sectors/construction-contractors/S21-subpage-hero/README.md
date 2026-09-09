# Section ID

CON-S21

# Section Name

Subpage Hero

# Sector

Construction & Contractors

# Prefix

CON

# Planned Studies

CON-S21-001
CON-S21-002
CON-S21-003
CON-S21-004
CON-S21-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `CON-S21-001` | Universal / Safe |
| `CON-S21-002` | Premium / Editorial |
| `CON-S21-003` | Structured / Visual Modular |
| `CON-S21-004` | Conversion-led |
| `CON-S21-005` | Art-directed / Distinctive |

Read for this sector in `../CONSTRUCTION-DESIGN-DIRECTION.md`.

# Section Role

The top of an interior page: which page this is, what is on it, and nothing else.

# In Scope

- The page title, and a parent or category label
- A short introduction that frames **the page**, not the sector
- Contextual metadata: sector, status, form of contract, reference
- At most one contextual action, tied to this page
- An optional media area sized for an interior page rather than a landing stage

# Out Of Scope

- A restatement of `S01`
- Positioning, manifesto or reason-to-choose-us copy
- Navigation, which belongs to the chrome and to `S22`
- Body content, which belongs to `S23`–`S27`
- Competing calls to action

# The Governing Constraint — It Must Fail As An S01

The extended set's standing test:

> A study that would work unchanged as `S01` has not answered this role.

And this sector has the sharpest possible way to fail it:

    A homepage hero in this sector is built around a number. An interior hero has no
    number in it at all — because the visitor already believed enough to click, and
    what they need now is to know where they are.

The sector direction records that all five supplied `S01` references were built on a counter, and
that the counter is this sector's signature device. **Withholding it is how these studies fail as
homepage heroes**, and it is checkable: no counter, no reserved figure at display scale, no digit.

| Discipline | How it is enforced |
| --- | --- |
| Height | No viewport-height unit. An interior hero that fills the screen buries the thing the visitor came for |
| Voice | It orients, it does not persuade. No proposition about the firm |
| Actions | At most one, and it points **into this page** |
| Subject | The title names where you are |
| Counter | **None.** The device that makes `S01` work is the device this section must not have |

# The Worked Example Is A Project Page

All five studies are the hero of a project detail page — the `S24` parent. It is the interior page a
contractor's site is actually built around, it carries the most metadata, and it is the one most
likely to be turned back into a second homepage hero.

`003` additionally shows the same slots re-labelled for the other four parents, because a hero is a
component rather than a picture.

# The Introduction Describes The Page, Not The Project

A project name may not be invented, and neither may what the project achieved. So the orienting line
does something better:

    It says what is on the page, not what the job was worth.

> *What was on the site before we started, what we chose, and the decision this one got wrong.*

Which is `S13`'s three-part device used as a page description — real, authorable, and more use to a
reader than a claim about a building they have not seen yet.

# The Hard Problem — A Reserved Title At Display Scale

The page title is the largest thing in a subpage hero, and in this catalog **the page title is a
reserved field.** The recorded lesson from `S08-005`, `S09-005`, `S15-005`, `S16-005` and `S18-005`
is that a reserved em-dash at display scale reads as a redaction rather than as a field.

So this batch carries a rule none of the earlier ones needed:

    Every study reserves the title, and no study uses an em-dash to do it.

The title is drawn as a labelled fill — a caption naming the field, and bars at the measure the
finished title would occupy. A reviewer sees *this is where the project name goes and this is how
much room it has*, which is what a hero study is for.

# No Refusal Region In This Batch

The first section in this sector with none, and deliberately:

> **A hero that argues with itself is not a hero.**

Every other section in `CON` declares a `data-refusal` block so the vocabulary scans can run on the
page with its own refusals removed. There is nothing to remove here, so the scans run on the whole of
the visible copy — which is a stricter test, not a looser one.

# What Is Real, And What May Not Be Invented

| Element | Treatment |
| --- | --- |
| The parent label (*Projects*) | **Real** — generic vocabulary |
| The page description | **Real** — it describes the page |
| Metadata labels (sector, status, form of contract, reference) | **Real** |
| The project name | **Reserved**, as a labelled fill and never an em-dash |
| Sector value, status value, contract form, reference, dates | **Reserved fields** |
| Media | **Reserved area, at interior scale** — smaller and less central than `S01`'s |
| Any counter, figure, percentage or date | **Forbidden** |
| Any claim about the firm | **Forbidden** — that is `S01` |

# Boundary With S01, S22 And S24

| Section | What it owns |
| --- | --- |
| `S01` Hero | **The proposition**, and the counter |
| `S22` Breadcrumb / Context Navigation | **The path back**, and the siblings |
| `S24` Project Detail | **The body of the page** |
| `S21` Subpage Hero | **Which page this is, and what is on it** |

    S01 says why this firm. S21 says which page, and then gets out of the way.

# One Mechanism, In One Study

**`004` carries the batch's only action**, and it is an in-page anchor pointing further down the same
page. No study carries a form.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/
