# Section ID

WELL-S26

# Section Name

Practitioner / Specialist Profile

# Section Role

S26 — Person / Profile Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Purpose

The detail page for one person: who they are, what they work on, and how to reach them.

# Visitor Intent

The visitor is deciding whether this is the right person to work with, or has been sent to this page by name.

# Content Responsibility

One person in full: role, focus, the work they are attached to, and a contact route.

# In Scope

- Name, role and area of focus
- A description of what the post covers and how they work
- Links to the work and offerings they are attached to
- Factual professional background the person has supplied
- A contact route appropriate to the sector
- Optional portrait media

# Out Of Scope

- A team index or grid, which belongs to the sector core sections
- Fabricated qualifications, registrations, memberships, awards or credentials
- Invented social handles or profile links
- Testimonials or ratings attributed to a person

# The Governing Constraint — A Profile Whose Subject Cannot Be Named

`S04` established the sector's rule for people: **role leads, identity is reserved.** No invented
names, no invented credentials, and credentials not even as empty labelled fields. `S26` is a page
whose entire subject is one person, so the rule arrives at its hardest case.

The scaffold's Out Of Scope list settles most of it before the batch starts:

> Fabricated qualifications, registrations, memberships, awards or credentials · Invented social
> handles or profile links · Testimonials or ratings attributed to a person

| Element | Treatment |
| --- | --- |
| Name | **Reserved area** — it is the subject of the page, like the article title in `S25` |
| Portrait | **Reserved slot**, optional; a filled slot means a real person who has consented |
| Role and focus | **Real** — generic sector vocabulary from `S03` |
| Qualifications, registrations, memberships, awards | **Omitted entirely, not reserved** |
| Years of experience, treatment counts | **Omitted** — invented figures |
| Social handles, personal email | **Omitted** |
| Testimonials, ratings | **Omitted** — the `S10` rule, and the scaffold's own |
| A contact route | **Real** — *ask for them by name when you book* |

**Why credentials are omitted rather than reserved.** An empty *"Qualifications: —"* asserts that
the studio lists qualifications and that this person's are pending. In a sector adjacent to
medicine, a credential list is the clearest way into the clinical register the sector direction
rules out. It is the `S10` empty-star failure and the `S17` empty-expiry failure, and it is also
what `S04` decided for the team index — `S26` inherits it unchanged.

# What Is Left, And Why It Is Enough

    A visitor is not choosing a biography. They are choosing how somebody works.

That is entirely authorable, and it is what the page is made of:

1. **What they work on.** Real category vocabulary, not a specialism claim.
2. **How they work in the room.** What they ask before starting, whether they talk, how firm they
   are, what they write down.
3. **What they will say no to.** The strongest content on the page, on the `S23` steer-away pattern:
   *"will not do a first appointment the day before an event"*, *"will send you to a doctor rather
   than work over something changing."*
4. **How continuity works.** That you can ask for the same person, and what happens if they are away.
5. **The contact route.** Ask for them by name when you book — the only route that is sector-true
   and needs no invented address.

**Not present in any study:** an invented name, portrait, qualification, registration, membership,
award, social handle, personal email, testimonial, rating, count of years or treatments, price or
duration.

# The Scaffold's Responsive Rule, Made Structural

> Portrait and identity must stay paired at every width; a name must never end up beside or above
> the wrong portrait when the layout reflows.

**Every study that carries a portrait wraps it and the name in a single `<figure>`, with the name in
the `<figcaption>`.** They cannot be separated by any reflow because they are one element. The
checker verifies it: a portrait slot outside a `<figure>` that also contains the name area fails.

# Boundary With S04 And S23

| Section | What it owns |
| --- | --- |
| `S04` Specialists | **The set** — everyone, role-led, identities reserved |
| `S23` Treatment Detail | **One treatment**, whoever does it |
| `S26` Practitioner Profile | **One person in full** — how they work, and how to ask for them |

    S04 is the team. S26 is one of them, at length.

# Media Relationship, Read For This Sector

The scaffold: *"A profile must read completely with the portrait absent."* `002` carries **no
portrait at all** and is the proof; the other four reserve exactly one.

# Planned Studies

WELL-S26-001
WELL-S26-002
WELL-S26-003
WELL-S26-004
WELL-S26-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S26-001` | Universal / Safe |
| `WELL-S26-002` | Premium / Editorial |
| `WELL-S26-003` | Dense / Information-heavy |
| `WELL-S26-004` | Conversion-led |
| `WELL-S26-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Media Relationship

One portrait slot, optional. A profile must read completely with the portrait absent, and a filled portrait slot means an image of a real person who has consented to appear.

# Interaction Notes

Normally none.

# Responsive Considerations

Portrait and identity must stay paired at every width; a name must never end up beside or above the wrong portrait when the layout reflows.

# Related Sections

Nothing in this role may be invented. Credentials, registrations and memberships are verifiable facts about real people, and a placeholder study must leave them as reserved fields rather than fill them.

Nearest existing section in this sector: S04 Specialists (`S04-specialists/`).

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
