# Section ID

WELL-S25

# Section Name

Wellness Article / Guide Detail

# Section Role

S25 — Article / Insight Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Purpose

The detail page for one piece of editorial or resource content.

# Visitor Intent

The visitor came to read something specific, usually from a search result or a link, and wants to read it without obstruction.

# Content Responsibility

One article in full: its heading structure, its body, its attribution and its context.

# In Scope

- Article title, standfirst and body content
- Attribution and factual publication context
- Category or topic labels
- Optional lead media and in-body media
- Optional in-page contents for long pieces
- Related reading

# Out Of Scope

- An index or feed of all articles, which belongs to the sector core sections
- Marketing copy dressed as editorial
- Fabricated authors, publications, dates or citations
- Any advice a regulated sector may not publish without qualification

# The Governing Constraint — The Only Section Whose Content Is Entirely Unwritable

`S18` reserved the article title because writing one invents a publication and, in this sector,
would almost certainly also be an efficacy claim. `S21-003` and `S22-002` inherited that reservation
for the hero and the trail. **`S25` is where the consequence lands in full: the title is reserved,
the standfirst is reserved, and the body *is* the article.** There is no part of the content proper
that a placeholder may write.

    Reserve the article. Author the apparatus around it.

And that turns the section into a genuinely interesting design problem rather than an empty one:

    What does a reading page look like when the reading is not written yet?

**The reserved body is not a gap — it is the demonstration.** Reserved blocks set at real prose
rhythm, at the measure the finished article will occupy, let a reviewer judge line length, paragraph
cadence and heading hierarchy before a word exists. The scaffold says this role *"is judged on
reading comfort"*; a reserved body judged for reading comfort is exactly what these studies provide.

| Element | Treatment |
| --- | --- |
| Article title | **Reserved area** at title scale |
| Standfirst | **Reserved area** |
| Body paragraphs | **Reserved blocks** at prose rhythm, on the real measure |
| Sub-headings | **Reserved bars** at heading scale, so the hierarchy is visible |
| Pull quote | **Reserved area** where a study shows one |
| Author | **Reserved field** — `Practitioner 01` where a token is shown |
| Publication date | **Reserved field** |
| Topic, kind | **Real** — `S18` vocabulary |
| Reading time | **Omitted** — the `S18` decision holds |
| Citations, sources | **Omitted** — the scaffold rules out fabricated citations, and an empty citation asserts a research practice |

# What Is Authorable — The Apparatus

Everything that is not the article itself, and there is more of it than expected:

1. **The limits line.** None of this is medical advice; something changing on your skin is a doctor's
   question. `S18` established it; **every study in this batch carries it**, and on a page whose body
   is empty it is the only real prose on the screen.
2. **The editorial policy.** Who writes these, that they are updated when practice changes, that
   nothing here is sponsored, that there are no affiliate links and nothing is sold from a guide.
   This is the section's strongest authorable content and no wellness blog prints it.
3. **What this piece does not cover**, as a structural promise rather than a summary of the specific
   article.
4. **The treatment it concerns**, named from the real `S02`/`S03` vocabulary.
5. **Related reading**, as reserved titles on the `S18` pattern.

**Not present in any study:** an invented article title, standfirst, body sentence, sub-heading,
pull quote, author name, publication or date; a citation, source list or reference; a reading time,
view, share or comment count; an efficacy, outcome or ingredient-action claim; a named condition
presented as treatable; a newsletter capture, sponsored label, affiliate link or product sale.

# Boundary With S18 And S21

| Section | What it owns |
| --- | --- |
| `S18` Wellness Resources | **The index** of what has been published |
| `S21` Subpage Hero | The **page identity** at the top of this page |
| `S25` Article Detail | **The piece itself**, and the apparatus around it |

    S18 lists them. S21 names this one. S25 is the reading.

`S25` does not repeat the index and does not restate the page title as a hero; where a study shows
the title it is as the article's own opening, at body scale rather than at hero scale.

# Media Relationship

Optional lead media plus in-body media slots. Body media must not break the reading measure, and captions belong to the study, not to alt text alone.

Every media area in this batch carries a **visible caption**, not an alt attribute alone, exactly as
the scaffold requires. No in-body media area is wider than the reading measure it sits in.

# Interaction Notes

Usually none. In-page contents, footnotes or a progress indicator may be justified for long pieces and must degrade to plain markup.

`003` carries in-page contents as a plain anchor list — it is plain markup already, so there is
nothing to degrade to. No study uses a progress indicator, which cannot exist without script.

**A second `<nav>` exception, recorded.** `S22` established that the section-shell prohibition on
`<nav>` is aimed at **global site chrome**, not at the element: *a section whose role is navigation
uses navigation markup.* `S25-003` is the second case. Its in-page contents are listed in this
role's own In Scope, and a document's table of contents is a navigation region belonging to that
document — so it is marked up as `<nav aria-label="On this page">`. The prohibition still holds in
full for `001`, `002`, `004` and `005`, and for `<header>`, `<footer>`, a logo, a search field and a
primary menu everywhere.

# Responsive Considerations

This role is judged on reading comfort: a controlled measure, a stable line length, and heading hierarchy that survives at every width. Media inside the body must reflow without forcing the text column wider than it should be.

Each study states the measure it holds and keeps it at every width. The measure is set in `ch` on the
body element itself so it stays stable when the type scale changes.

# Related Sections

Sector terminology varies and the label should follow it. Not every sector calls this a blog, and professional sectors generally do not.

Nearest existing section in this sector: S18 Wellness Resources (`S18-wellness-resources/`).

This sector calls them **notes and guides**, never a blog — `S18` established the vocabulary:
an aftercare note, a guide, a question answered.

# Planned Studies

WELL-S25-001
WELL-S25-002
WELL-S25-003
WELL-S25-004
WELL-S25-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S25-001` | Universal / Safe |
| `WELL-S25-002` | Premium / Editorial |
| `WELL-S25-003` | Dense / Information-heavy |
| `WELL-S25-004` | Conversion-led |
| `WELL-S25-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer. Headings start
at `<h2>`, as in `S23` and `S24` — the page title belongs to `S21`.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
