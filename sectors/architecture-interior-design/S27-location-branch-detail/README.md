# Section ID

ARC-S27

# Section Name

Studio / Location Detail

# Section Role

S27 — Location / Branch Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

The detail page for one studio: where it is, what happens there, and how to reach it.

# Role Clarification

A place-led studio page. Favour a location hero or studio image, the address, concise studio
context, contact details, opening or visit context where applicable, a reserved map area, the
people and projects based there, and a simple call to action.

It must not default to arrival diagrams, coordinate sheets, technical location registers or
letter-keyed plan systems.

# Visitor Intent

The visitor is planning to go there, to contact it, or to check that it is the right studio for
what they need.

# Content Responsibility

One location in full: address and contact details, what the studio does, how to reach it, and who
is based there.

# In Scope

- Studio and location imagery
- Address and contact details for this one location
- Concise studio context
- Opening or visiting context where applicable
- Access and arrival information, in plain language
- An optional reserved map area
- People and projects attached to this location
- A simple call to action

# Out Of Scope

- **A global site header, primary navigation or footer**
- A list of all locations, which belongs to S17
- **Arrival diagrams, coordinate sheets, technical location registers and letter-keyed plan
  systems**
- Embedded third-party map services or any remote dependency
- Fabricated addresses, coordinates, phone numbers or opening hours
- Reviews, ratings or claims attributed to the location

# Planned Studies

ARC-S27-001
ARC-S27-002
ARC-S27-003
ARC-S27-004
ARC-S27-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S27-001` | Universal / Safe |
| `ARC-S27-002` | Premium / Editorial |
| `ARC-S27-003` | Structured / Visual Modular |
| `ARC-S27-004` | Conversion-led |
| `ARC-S27-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** organises the practical information visually — grouped contact, access and people
  modules — rather than as a record sheet.
- **005** is a more art-directed location page that stays useful: the address, the contact route
  and the way in must remain easy to find.

**Recorded correction.** `ARC-S27-003` and `ARC-S27-005` are record sheets and keyed plans, and
only one study carries real photography. `ARC-S27-002` shows the section can be place-led and
premium; the reserved map slot is an honest device and stays.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

A studio is a space, and this is a page about a space. Lead with photography of the place, then the
address, then the people and work based there.

# Section Shell

Page archetype: internal page content architecture is allowed. Global website chrome is not. The
region this page shares with S21 and S22 is marked `data-region="page-context"`.

# Media Relationship

Expected: imagery of the place, plus an optional map area. A map area is a reserved slot, not an
embedded service: studies carry no third-party map and no remote dependency of any kind.

# Interaction Notes

Normally none. Any location switcher must remain a set of plain links.

# Responsive Considerations

Address and contact details are the content most likely to be needed on a phone and must be
first-class at small widths, not pushed below decorative media.

# Authoring Questions

- **Primary visual element:** photography of the studio and its place.
- **Immediate understanding:** where this studio is and how to reach it.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

Every address, coordinate, hour and contact route in a study must be an obvious placeholder.
Fabricating a plausible address is the failure mode this role invites.

Location index for this sector: S17 Studio Locations (`../S17-studio-locations/`).

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
