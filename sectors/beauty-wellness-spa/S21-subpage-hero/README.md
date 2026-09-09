# Section ID

WELL-S21

# Section Name

Subpage Hero

# Section Role

S21 — Subpage Hero

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Purpose

Top-of-page contextual hero for an internal page. It states where the visitor has landed and what the page is for, then hands off to the page body.

# Visitor Intent

The visitor has already arrived from somewhere specific. They are checking that this is the page they wanted and orienting themselves before reading.

# Content Responsibility

Page identity: title, a short contextual introduction, optional contextual metadata, optional media, and at most one contextual action.

# In Scope

- Page title and, where useful, a parent or category label
- A short introduction that frames the page rather than the sector
- Contextual metadata such as category, date, reading time, discipline or reference
- An optional single contextual action tied to this page
- An optional media area sized for an internal page rather than a landing stage

# Out Of Scope

- A restatement of the homepage hero from S01
- Primary sector positioning or brand manifesto copy
- Full navigation, which belongs to the site chrome and to S22
- Body content that belongs to S23 to S27
- Multiple competing calls to action

# The Governing Constraint — It Must Fail As An S01

This section's own scaffold states the test, and it is the sharpest one in the extended set:

> A study that would work unchanged as `S01` has not answered this role.

So every study here is authored to **fail** as a homepage hero, deliberately and in a way that can
be checked:

| Discipline | How it is enforced |
| --- | --- |
| Height | No study uses a viewport-height unit. An interior hero that fills the screen buries the content the visitor came for — and they arrived wanting that content, not an entrance |
| Voice | It **orients**, it does not persuade. No proposition about the business, no manifesto, no reason-to-choose-us copy — all of that is `S01` and `S14` |
| Actions | **At most one**, and it is tied to this page rather than to the business |
| Subject | The title names **where you are**, not what the studio is |

**Two failures to avoid in particular.** The first is the interior hero that is really a second
homepage hero — big claim, big picture, two buttons. The second is subtler: an interior hero so
decorative that a visitor has to scroll to find out whether they are on the right page. Both are
solved the same way, by treating the title as the only thing that must survive at every width.

# What Is Real, And What The Sector Filters Out

The canonical scope above allows *"category, date, reading time, discipline or reference"*. Read
through this sector's claims rule:

| Metadata | Treatment |
| --- | --- |
| Category / parent label | **Real** — generic sector vocabulary, as in `S03` |
| Page title | **Real** where it is a page type or a category; a named article title stays reserved, on the `S18` rule |
| Publication date | **Reserved field** — the `S18` treatment |
| Author | **Reserved token** — `Practitioner 01`, on the `S04` rule |
| Reading time | **Omitted** — the `S18` decision holds; a placeholder cannot compute it and the sector prints no durations |
| Item counts | **Omitted** — *"eleven treatments"* is an invented figure |
| Price, rating, review count | **Omitted** — `S11` and `S10` own those and they do not belong in a hero |

# Boundary With S01 And S22

| Section | What it owns |
| --- | --- |
| `S01` Hero | The **homepage** opening — the proposition of the whole studio |
| `S21` Subpage Hero | The **interior** opening — which page this is and what it holds |
| `S22` Breadcrumb / Context Navigation | The **trail** — where this page sits in the hierarchy, and the way back up |

    S21 names the page. S22 shows the path to it.

**No study in this batch contains a breadcrumb**, a trail, a parent link, a *back to* link or a
separator chain. A parent **label** appears — as a word, not a link — because naming the category a
page belongs to is page identity, while linking up the hierarchy is `S22`.

# Media Relationship

Optional. An internal page hero often carries no image at all, and the study set should include at least one variant that works without one. Where media is present it is usually smaller and more contained than the S01 stage.

`002` carries no media at all. Where media appears it is a **band or a panel, never a stage**: wide
and short in `001`, short and overlapped in `005`. No study reserves a full-bleed area.

# Interaction Notes

Normally none. Any interaction should be limited to a single contextual action.

Only `004` carries an action, and it carries exactly one.

# Responsive Considerations

The title must remain the first thing read at every width. Contextual metadata should wrap rather than truncate, and any media area should be allowed to reduce or disappear before the title does.

# Related Sections

S01 is the homepage or primary sector hero. S21 is the internal page contextual hero. A study that would work unchanged as S01 has not answered this role.

Homepage hero for this sector: S01 Hero (`S01-hero/`).

# Planned Studies

WELL-S21-001
WELL-S21-002
WELL-S21-003
WELL-S21-004
WELL-S21-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S21-001` | Universal / Safe |
| `WELL-S21-002` | Premium / Editorial |
| `WELL-S21-003` | Dense / Information-heavy |
| `WELL-S21-004` | Conversion-led |
| `WELL-S21-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

Note that this set differs from the `S01`–`S20` directions: the extended architecture roles use
**Dense / Information-heavy** in place of Structured / Visual Modular, and **Sector-native /
Distinctive** in place of Art-directed / Distinctive.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
