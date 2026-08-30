# Section ID

LOG-S27

# Section Name

Terminal / Warehouse Location Detail

# Section Role

S27 — Location / Branch Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Logistics & Transportation

# Prefix

LOG

# Purpose

The detail page for one physical place: where it is, what happens there, and how to reach it.

# Visitor Intent

The visitor is planning to go there, to contact it, or to check that it is the right place for what they need.

# Content Responsibility

One location in full: address and contact details, what the location does, how to reach it, and who is based there.

# In Scope

- Address and contact details for this one location
- Opening or operating context where applicable
- What is available at this location specifically
- Directions, access and arrival information
- Optional map area, optional media of the place
- People or services attached to this location

# Out Of Scope

- A list of all locations, which belongs to the sector core sections
- Fabricated addresses, coordinates, phone numbers or opening hours
- Fabricated maps, embedded third-party map services, or invented directions
- Reviews, ratings or claims attributed to the location

# Planned Studies

LOG-S27-001
LOG-S27-002
LOG-S27-003
LOG-S27-004
LOG-S27-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `LOG-S27-001` | Universal / Safe |
| `LOG-S27-002` | Premium / Editorial |
| `LOG-S27-003` | Dense / Information-heavy |
| `LOG-S27-004` | Conversion-led |
| `LOG-S27-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Media Relationship

Optional media of the place, plus an optional map area. A map area is a reserved slot, not an embedded service: studies carry no third-party map, and no remote dependency of any kind.

# Interaction Notes

Normally none. Any location switcher must remain a set of plain links.

# Responsive Considerations

Address and contact details are the content most likely to be needed on a phone and must be first-class at small widths, not pushed below decorative media.

# Related Sections

Every address, coordinate, hour and contact route in a study must be an obvious placeholder. Fabricating a plausible address is the failure mode this role invites.

Nearest existing section in this sector: S06 Terminals Locations (`S06-terminals-locations/`).

# Status

NOT_STARTED

# Raw Path

./raw/
