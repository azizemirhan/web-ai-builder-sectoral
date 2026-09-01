# Section ID

ARC-S25

# Section Name

Studio Journal / Article Detail

# Section Role

S25 — Article / Insight Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

The detail page for one piece of editorial content from the studio.

# Role Clarification

This page naturally carries more copy than any other Architecture role. It must still look like a
**contemporary editorial webpage**.

Favour an article hero and title, lead media, a readable measure, a pull quote, embedded media,
visual breaks, related articles, and author or profile context only where it is real.

"Detail page" is not permission for uncontrolled text density, and the body must stay readable and
web-native.

# Visitor Intent

The visitor came to read something specific, usually from a search result or a link, and wants to
read it without obstruction.

# Content Responsibility

One article in full: its heading structure, its body, its media, its attribution and its context.

# In Scope

- Article title, standfirst and body content
- Lead media and in-body media
- A pull quote and other visual breaks
- Attribution and factual publication context
- Category or topic labels
- Optional in-page contents for long pieces
- Related reading

# Out Of Scope

- **A global site header, primary navigation or footer.** Supplied references that include site
  chrome must be read selectively: take the article, leave the header
- An index or feed of all articles, which belongs to S16
- Uncontrolled text density and long undifferentiated prose
- Marketing copy dressed as editorial
- Fabricated authors, publications, dates or citations

# Planned Studies

ARC-S25-001
ARC-S25-002
ARC-S25-003
ARC-S25-004
ARC-S25-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S25-001` | Universal / Safe |
| `ARC-S25-002` | Premium / Editorial |
| `ARC-S25-003` | Structured / Visual Modular |
| `ARC-S25-004` | Conversion-led |
| `ARC-S25-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** structures a longer article visually — contents, sections, embedded media, pull quotes,
  captioned breaks — rather than simply running longer.
- **005** is an art-directed article page: display typography, lead media and pacing, still built
  around a readable measure.

**Recorded correction.** All five studies carry site headers taken from the supplied references,
and all five exceed 350 visible words. The chrome comes out and the copy comes down; the display
typography and media presence are the section's strength and stay.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Editorial in this sector means images breathing inside the text, not text filling the page. Lead
media, spaced visual breaks and a controlled measure.

# Section Shell

Page archetype: internal page content architecture is allowed. Global website chrome is not. The
region this page shares with S21 and S22 is marked `data-region="page-context"`.

# Media Relationship

Optional lead media plus in-body media slots. Body media must not break the reading measure, and
captions belong to the study, not to alt text alone.

# Interaction Notes

Usually none. In-page contents, footnotes or a progress indicator may be justified for long pieces
and must degrade to plain markup.

# Responsive Considerations

This role is judged on reading comfort: a controlled measure, a stable line length, and heading
hierarchy that survives at every width. Media inside the body must reflow without forcing the text
column wider than it should be.

# Authoring Questions

- **Primary visual element:** the lead media and the in-body images that break the text.
- **Immediate understanding:** what the article is about, and that it is readable.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S16 Press News (`../S16-press-news/`) is the index this page sits behind. Sector terminology
varies and the label should follow it; not every sector calls this a blog, and professional
sectors generally do not.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
