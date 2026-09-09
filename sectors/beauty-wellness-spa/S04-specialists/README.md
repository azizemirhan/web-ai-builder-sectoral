# Section ID

WELL-S04

# Section Name

Specialists

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S04-001
WELL-S04-002
WELL-S04-003
WELL-S04-004
WELL-S04-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S04-001` | Universal / Safe |
| `WELL-S04-002` | Premium / Editorial |
| `WELL-S04-003` | Structured / Visual Modular |
| `WELL-S04-004` | Conversion-led |
| `WELL-S04-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

The people. The section presents the practitioners who actually carry out the work — what each
one does, and how to reach or book them — as a set the visitor can take in at a glance.

It answers: *who will be in the room with me?*

# Boundary With S26

`S26-person-profile-detail/` owns one practitioner in full: their background, the work they are
attached to, and their own contact route. Its own README already states that a team index or grid
belongs to the sector core sections, which is this one.

    A set of practitioners seen at a glance is S04. One practitioner in full is S26.

A card here carries a role, a short line and a route. It stops being S04 the moment a single
person gets a biography, a body of work or a page-scale treatment.

# The Identity Problem, And How This Batch Solves It

This is the first `WELL` section whose content is people, which changes what a placeholder has to
mean. `../WELLNESS-DESIGN-DIRECTION.md` forbids an invented practitioner name, qualification,
licence, registration or professional body, and `03-MEDIA-POLICY.md` forbids inventing people at
all. A specialists section filled with realistic names and credentials would be fabrication, not
placeholder content.

The solution used across this batch, and the reason it also produces a better composition:

- **Role leads, identity is reserved.** The occupational role — *Facialist*, *Massage therapist*,
  *Nail technician*, *Brow & lash specialist* — is a real, generic, non-fabricated fact about a
  post, so it carries the card as the heading. The name sits beneath it as a reserved token
  (`Practitioner 01`), following the `Team member NN` convention established in `ARC-S08`.
- **Focus lines are procedural**, in line with the `S02` copy rule: what the person spends their
  time doing, never how good they are at it.
- **No credentials of any kind.** No qualification, licence, registration, membership, award,
  years of experience, rating, review or social handle appears in any study, in any form —
  including as an empty labelled field, which would still assert that the studio holds one.
- **Portraits are reserved media areas.** A filled portrait slot means a photograph of a real
  person who has consented to appear.

**The disclosure lives in the batch record, not on the page.** `ARC-S08` put a visible statement
in each study saying its roster was a placeholder. Under the *Visible Website Copy vs Research
Notes* rule added to `01-AUTHORING-STANDARD.md` after that section was authored, that explanation
now belongs in HTML comments, `<meta>` fields and this section's batch document instead. No study
in this batch displays a note about its own placeholder status.

# Out Of Scope

- A global site header, primary navigation or footer
- One practitioner in full, which belongs to S26
- Invented names, qualifications, registrations, memberships, awards or social links
- Ratings, review scores or testimonials attributed to a person
- Treatments presented as the subject, which belongs to S02
- Prices and durations, which belong to S11

# Authoring Questions

**1. What is the primary visual element of this role?**

The portrait, at a scale that reads as a person rather than an avatar. A specialists section is
the one place on a spa site where the visitor is looking for a face, and the layout has to reserve
space for four of them without turning into a contact sheet.

**2. What must a visitor understand immediately?**

That real, named people do this work; what each of them does; and that they can either choose one
or let the studio choose for them.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
