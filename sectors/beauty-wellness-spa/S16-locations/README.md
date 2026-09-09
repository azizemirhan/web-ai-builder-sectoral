# Section ID

WELL-S16

# Section Name

Locations

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S16-001
WELL-S16-002
WELL-S16-003
WELL-S16-004
WELL-S16-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S16-001` | Universal / Safe |
| `WELL-S16-002` | Premium / Editorial |
| `WELL-S16-003` | Structured / Visual Modular |
| `WELL-S16-004` | Conversion-led |
| `WELL-S16-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

Where the studio is. The section sets out the site or sites a guest can visit and gives them what
they need to choose one and find it.

It answers: *where do I go, and if there is more than one, which?*

# The Governing Constraint

Almost everything a locations section normally contains is a verifiable fact about a real building,
and none of it is authorable.

| Element | Treatment |
| --- | --- |
| Street address, postcode, city | **Reserved field** — every studio has one, so the empty field asserts nothing |
| Phone number | **Reserved field** |
| A map | **Reserved media area.** An embedded map is a remote dependency, which the workspace forbids outright — so a map here is a slot, never a frame |
| Exterior or entrance photograph | **Reserved media area** |
| Opening hours | **Omitted entirely** — this sector states no hours anywhere, on the same basis as durations |
| Travel directions, nearest station, parking, step-free access | **Reserved field where present, never written** — each is a specific claim about a specific building, and a wrong access claim is the one that actually harms someone |

**No description of the building.** This is the constraint that catches people out. Writing *"a
converted townhouse on a quiet street"* invents a property as surely as inventing an address does.
No study in this batch describes what a site looks like, what it is near, or what kind of building
it occupies. The compositions carry that weight instead, which is why every study reserves generous
space for an exterior or a map.

**What is real.** Two things, and neither is about a building:

1. **How many sites there are** is a structural fact the design must handle, not a claim — and it
   changes the section completely. A single-site studio and a three-site studio need different
   compositions, so this batch **demonstrates both** rather than assuming one.
2. **How the studio handles the questions around a place** — that access needs are asked about at
   booking rather than guessed from a web page, that the exact address is confirmed with the
   appointment. These are operating commitments in the same family as `S07` and `S11`.

**The access line is the one that matters.** Every study says access needs are settled by asking
rather than by reading a badge on a page. That is honest for a placeholder — it does not know what
the building is — and it is better practice than a step-free icon that turns out to be wrong.

**Not present in any study:** an invented address, street, postcode, city, region, phone number,
email, map coordinate, travel time, distance, transport line, parking claim, access claim or
opening hour; an embedded map or any remote frame.

# Boundary With S19 And S27

| Section | What it owns |
| --- | --- |
| `S16` Locations | **The places** — which sites exist, and choosing between them |
| `S19` Contact | **The channels** — how to reach the studio, whichever site |
| `S27` Location / Branch Detail | **One site in full**, on its own page |

    "We have three studios, here is where" is S16.
    "Here is the phone number and the form" is S19.
    "Everything about this one studio" is S27.

The same pattern as `S02` against `S23`, and `S04` against `S26`: the set here, one in depth there.

# Out Of Scope

- A global site header, primary navigation or footer
- Contact channels and forms, which belong to S19
- One location in depth, which belongs to S27
- Opening hours, in any study
- An embedded map, in any study

# Authoring Questions

**1. What is the primary visual element of this role?**

The map or the door. A locations section is the one place a visitor wants to see the outside of the
building rather than the inside, so the compositions reserve that space at real size — and because
the copy cannot describe the place, the reserved area is doing more work here than anywhere else in
the sector.

**2. What must a visitor understand immediately?**

How many places there are, and what to do next about getting to one.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
