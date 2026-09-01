# Section ID

ARC-S23

# Section Name

Architecture / Interior Service Detail

# Section Role

S23 — Service / Offering Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

The detail page for one single offering, presented in enough depth that a visitor can decide
whether it is the right one for them.

# Role Clarification

**This is a full internal service detail page archetype**, and in Architecture it must balance
information with visual storytelling.

A useful baseline content capacity — guidance, not a mandatory template:

- subpage hero / service title area
- concise service introduction
- large image or video slot
- three to four key service aspects
- an image-and-text story
- a simple process
- a relevant project or case example
- a concise FAQ
- a call to action

The five studies must still differ structurally, and all five must leave enough room to actually
explain the service.

# Visitor Intent

The visitor has chosen one offering from an index and now wants specifics: what it covers, how it
runs, what it involves and what happens next.

# Content Responsibility

One offering in full: what it is, what it involves, how it is delivered, who it suits, the work it
has produced, and the route to enquire about it.

# In Scope

- A description of the single offering the page is about
- What the offering includes and, where useful, what it excludes
- How it is delivered, staged or sequenced, at page scale rather than as full process
  documentation
- Who it is for, and the conditions under which it applies
- Project or case examples of the offering
- Related or adjacent offerings
- A route to enquire about this specific offering

# Out Of Scope

- **A global site header, primary navigation or footer**
- An index or grid of every offering, which belongs to S03
- **Responsibility ledgers, contract-style included/not-included walls, specification-document
  layouts and process documentation that crowds out the service explanation**
- Extremely long prose
- Homepage positioning copy
- Fabricated pricing, guarantees, turnaround times or availability
- Any regulated claim the sector does not permit

# Planned Studies

ARC-S23-001
ARC-S23-002
ARC-S23-003
ARC-S23-004
ARC-S23-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S23-001` | Universal / Safe |
| `ARC-S23-002` | Premium / Editorial |
| `ARC-S23-003` | Structured / Visual Modular |
| `ARC-S23-004` | Conversion-led |
| `ARC-S23-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** uses visual modularity to support the page's richer content — modules, panels, grouped
  media, disclosure — rather than carrying it in longer prose or in field lists.
- **005** is a more art-directed service page, not a professional document.

**Recorded correction.** All five studies were reviewed as too textual and too technical, with
insufficient visual storytelling: 485–819 visible words with little or no media, and two are
outright documents. The correction here is the content balance, not the page geometry.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

A service is explained by the work it produces. Give the page a large media field early, break the
explanation into visual sections, and keep each block short enough to scan.

# Section Shell

Page archetype: internal page content architecture is allowed. Global website chrome is not. The
region this page shares with S21 and S22 is marked `data-region="page-context"`.

# Media Relationship

Required in practice. At least one large image or video area plus supporting media through the
page. A service detail page with little or no media has not answered this role in this sector.

# Interaction Notes

Optional. Where an offering has stages or options, disclosure, accordion or tab patterns are
justified, and the full content must remain reachable without script.

# Responsive Considerations

Body copy needs a controlled measure at wide widths and must not collapse into a single dense
column on small screens. Any supporting rail or sticky element should release to normal flow
before it starts competing with the body.

# Authoring Questions

- **Primary visual element:** the large service media field, and the image-and-text story blocks.
- **Immediate understanding:** which service this is and what engaging it involves.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

This is the depth page behind one entry in S03 Services (`../S03-services/`). S06 Design Process
(`../S06-design-process/`) holds the full process; this page carries only a simple version of it.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
