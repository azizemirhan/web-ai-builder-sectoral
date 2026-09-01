# Section ID

ARC-S16

# Section Name

Press News

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Present press coverage and studio news as an editorial set a visitor can scan.

# Visitor Intent

The visitor wants to see that the practice is active and covered — recent work, recent mentions.

# Content Responsibility

Coverage and news entries: headline, category, imagery, a concise summary and the route onward.

# In Scope

- Editorial cards
- Publication and article imagery
- Headline and category
- A date, where the data is real
- A concise summary per entry

# Out Of Scope

- A global site header, primary navigation or footer
- **Dense press registers, archive tables and citation indexes** as the section's primary device
- The article in full, which belongs to S25
- Awards and publication recognition, which belong to S09
- Fabricated publications, journalists, headlines or dates

# Planned Studies

ARC-S16-001
ARC-S16-002
ARC-S16-003
ARC-S16-004
ARC-S16-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S16-001` | Universal / Safe |
| `ARC-S16-002` | Premium / Editorial |
| `ARC-S16-003` | Structured / Visual Modular |
| `ARC-S16-004` | Conversion-led |
| `ARC-S16-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** holds a longer feed through card modules, grouping and disclosure — not through a
  tabular archive index.
- **005** is an art-directed press-room composition, not a register.

**Recorded correction.** `ARC-S16-003` is a tabular archive index with no media and is a later
rework.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

A press entry is an editorial object: image, headline, one line of context. `ARC-S16-002` and
`ARC-S16-005` already give the section two distinct editorial identities worth keeping.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Expected. Publication or article imagery per entry.

# Interaction Notes

Optional. Filtering by category or year is justified; every entry must remain reachable without
script.

# Responsive Considerations

Cards must reflow to full-width entries keeping image, headline and summary together, and a filter
row must not become a clipped horizontal strip.

# Authoring Questions

- **Primary visual element:** article and publication imagery.
- **Immediate understanding:** that the practice is active, and what has been said about it.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S09 Awards & Publications (`../S09-awards-publications/`) is recognition; S25 Studio Journal /
Article Detail (`../S25-article-insight-detail/`) is the full article page.

# Status

READY_FOR_INGESTION

# Raw Path

./raw/

# Batch

./BATCH-V1.md
