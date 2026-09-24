# Section ID

WELL-S27

# Section Name

Spa / Studio Location Detail

# Section Role

S27 — Location / Branch Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

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

# The Governing Constraint — The Page Cannot Describe The Place

The scaffold's Out Of Scope list is unusually specific, and it removes almost everything a location
page normally contains:

> Fabricated addresses, coordinates, phone numbers or opening hours · Fabricated maps, embedded
> third-party map services, or **invented directions** · Reviews, ratings or claims attributed to
> the location

`S16` had already settled the sector's version of this for the set of locations: the map is a
reserved area and never an embed, there is no description of the building, and access is answered by
conversation rather than by a badge. `S27` inherits all of it for one branch in full.

So the thesis of this batch, in the same shape as `S23`'s and `S24`'s:

    The page cannot describe the place. So it describes the arrival.

Where the building is, what it looks like and how long it takes to get there are all either reserved
or unknowable. **What happens when you walk in is entirely authorable**, because it is the studio's
own practice — and it is what a visitor is actually anxious about before a first visit.

| Element | Treatment |
| --- | --- |
| Address | **Reserved field** |
| Telephone | **Reserved field** |
| Map | **Reserved area, never an embed** — `S16`'s rule, and the scaffold's |
| Media of the place | **Reserved areas** |
| Directions, travel time, nearest stop | **Omitted** — the scaffold rules out invented directions, and an empty *"— minutes from the station"* asserts a distance |
| Opening hours | **Omitted** — the `S19` decision holds: an empty hours table asserts a weekly schedule and prints figures |
| Parking, step-free access, facilities | **Omitted as a list**, answered as a policy — see below |
| Reviews, ratings, claims about the place | **Forbidden** — the scaffold's own out-of-scope line |
| What is available here | **Real** — `S03` category vocabulary |
| Who is based here | **Role tokens** — the `S04` rule |

# Access: A Policy, Not A Row Of Icons

A facilities list — a step, a lift, a toilet, a parking space, each with a tick or a cross — is the
conventional answer, and every item in it would be invented here. Worse, a tick is a promise about a
building nobody has measured.

**The sector's answer, established in `S16` and carried here: access is answered by conversation.**
The page says what the studio will tell you and how to ask, and commits to answering honestly
including when the answer is no. That is authorable, it is more useful than a row of icons, and it
does not put a symbol where a measurement should be.

# The Scaffold's Responsive Rule, Made Structural

> Address and contact details are the content most likely to be needed on a phone and must be
> first-class at small widths, **not pushed below decorative media**.

As in `S26`, this is made impossible to break rather than promised: **in every study the contact
block comes before any media area in source order.** No reflow can bury it, because there is no
width at which it comes second. The checker verifies the source position of the first contact
element against the first media element in each file.

# Boundary With S16 And S19

| Section | What it owns |
| --- | --- |
| `S16` Locations | **The set** — which studios exist |
| `S19` Contact | **How to reach a person**, whichever studio |
| `S27` Location Detail | **One place in full** — its details, and what arriving is like |

    S16 is which building. S19 is which channel. S27 is this building, and walking into it.

# Media Relationship, Read For This Sector

The scaffold: *"A map area is a reserved slot, not an embedded service."* Every map in this batch is
a reserved area with no remote dependency of any kind. `002` and `005` carry **no map and no
media at all**, which the batch treats as a legitimate answer rather than an omission: a page whose
address is a reserved field and whose directions cannot be written is not improved by an empty
rectangle where a map will go.

# Planned Studies

WELL-S27-001
WELL-S27-002
WELL-S27-003
WELL-S27-004
WELL-S27-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S27-001` | Universal / Safe |
| `WELL-S27-002` | Premium / Editorial |
| `WELL-S27-003` | Dense / Information-heavy |
| `WELL-S27-004` | Conversion-led |
| `WELL-S27-005` | Sector-native / Distinctive |

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

Nearest existing section in this sector: S16 Locations (`S16-locations/`).

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
