# Section ID

ARC-S04

# Section Name

Project Typologies

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Organise the practice's work by project typology so a visitor can move from the kind of building
or interior they have in mind to the relevant work.

# Visitor Intent

The visitor is looking for their own project type — a house, a workplace, a hotel, a cultural
building, an interior, a reuse project — and wants to see that the practice works in it.

# Content Responsibility

The typology set: each typology named, illustrated, and given a route into the matching work.

# In Scope

- Project and work typologies such as residential, workplace, hospitality, cultural, interiors and
  reuse
- A short descriptor per typology
- Project imagery representing each typology
- A route into the work for that typology

# Out Of Scope

- A global site header, primary navigation or footer
- **Audience or client personas mixed into the building typology set**, unless that mixing is an
  explicit part of the design concept — the taxonomy must stay semantically consistent
- Markets and sectors served, which belong to S15
- A taxonomy document, plate catalogue or atlas presented as the section itself

# Planned Studies

ARC-S04-001
ARC-S04-002
ARC-S04-003
ARC-S04-004
ARC-S04-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S04-001` | Universal / Safe |
| `ARC-S04-002` | Premium / Editorial |
| `ARC-S04-003` | Structured / Visual Modular |
| `ARC-S04-004` | Conversion-led |
| `ARC-S04-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** carries a larger typology set through visual grouping and modular blocks — not through
  scope field pairs attached to every typology.
- **005** may be visually distinctive in how typologies are composed, but must not default to an
  atlas, plate catalogue or technical taxonomy document.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

A typology reads through its imagery before its label. Prefer typographic and image-led
presentation, with a consistent naming register across the set.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Expected. Each typology should be able to carry representative project imagery.

# Interaction Notes

Optional. Tab or filter switching between typologies is justified; the full set must remain
reachable without script.

# Responsive Considerations

Typology names must stay attached to their imagery through every reflow, and a switcher must
degrade to a readable stacked set rather than a horizontal strip that runs off the viewport.

# Authoring Questions

- **Primary visual element:** representative project imagery per typology.
- **Immediate understanding:** which kinds of project the practice takes on.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S15 Sectors Markets (`../S15-sectors-markets/`) covers the markets and contexts served, which is a
different axis from building typology. S02 Selected Projects (`../S02-selected-projects/`) is the
work itself.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
