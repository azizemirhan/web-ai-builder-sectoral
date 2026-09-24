# Section ID

CONS-S27

# Section Name

Office Detail

# Section Role

S27 — Location / Branch Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Consulting & B2B Professional Services

# Prefix

CONS

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

CONS-S27-001
CONS-S27-002
CONS-S27-003
CONS-S27-004
CONS-S27-005

# Expected Structural Diversity

| Variant | Direction | Theme | Shape | Composition | Slots |
| --- | --- | --- | :---: | --- | ---: |
| `CONS-S27-001` | Universal / Safe | 001 Paper | B | Address first, how to get in as four steps beside the door, then a map slot | 2 |
| `CONS-S27-002` | Premium / Editorial | 002 Sable | B | One measure. The lead image is the door, not the building | 1 |
| `CONS-S27-003` | Dense / Information-heavy | 003 Field | B | The arrival sequence as joined modules; the address demoted to a rail | 1 |
| `CONS-S27-004` | Conversion-led | 004 Signal | C | The hour is in this room — the sector's single ask, finally given a place | 0 |
| `CONS-S27-005` | Sector-native / Distinctive | 005 Midnight | C | Written to somebody standing outside — the arrival lines are the display type | 0 |

# The Governing Idea

> **Every office page tells you where the building is. Nobody tells you how to get in.**

The address is the part a search engine already has. What is missing everywhere is the last hundred
metres: which door, which floor, what to press, who to ask for. **A visitor standing on the street
with the right postcode and the wrong door is the ordinary outcome of every location page in this
sector.** So *How to get in* is a first-class section in all five: the door beside the sandwich shop
and not the glass one on the corner, the bell marked `four`, the fob-locked lift, and the person by
name.

# The Place All Five Render

**London — the office.** `S17` printed four locations and said which was which; this is the one of the
four that is an office, and **the room of twelve is this room** — `S15`'s session and `S19`'s hour
happen in it. The other three are named at the foot of every study with what they actually are.

# Placeholders

Every address, phone and email is deliberately impossible to mistake for real — `00 Example Street`,
`EC0A 0AA`, `+44 (0)20 0000 0000`, an `example.com` address — all marked `data-placeholder="true"`.
Fabricating a plausible address is the failure mode this role invites.

# The Map Slot

**A map area is a slot, never a service.** Two studies reserve one and its label says so; three carry
none and each says why. No study contains a remote URL, an embedded map or any third-party script. The
address is above both reserved areas in source order in every study, which is what keeps it
first-class on a phone.

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

Nearest existing section in this sector: S17 Offices Locations (`S17-offices-locations/`).

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION. Design record in `./BATCH-V2.md`; original authoring record in `./BATCH-V1.md`.

# Raw Path

./raw/
