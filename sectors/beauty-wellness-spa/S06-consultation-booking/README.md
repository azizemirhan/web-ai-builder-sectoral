# Section ID

WELL-S06

# Section Name

Consultation Booking

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S06-001
WELL-S06-002
WELL-S06-003
WELL-S06-004
WELL-S06-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S06-001` | Universal / Safe |
| `WELL-S06-002` | Premium / Editorial |
| `WELL-S06-003` | Structured / Visual Modular |
| `WELL-S06-004` | Conversion-led |
| `WELL-S06-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

The booking moment. The section is where a visitor stops reading and asks for an appointment — it
sets out what happens next and gives them the means to start it.

It answers: *how do I actually get in?*

# Boundary With S19 And S20

Three sections in this sector touch on getting in touch, and they are not the same thing.

| Section | What it owns |
| --- | --- |
| `S06` Consultation Booking | The **booking interaction itself**, placed mid-page: fields, a route, and what happens after you send it |
| `S19` Contact | The studio's **contact facts** — how to reach it, where it is, when it is open |
| `S20` Final Booking CTA | The **closing invitation** at the end of the page: a statement and an action, not an interaction |

    A form you fill in is S06. A phone number and an address is S19. A closing band with one
    button is S20.

`S06` may name a phone route as an alternative, but the studio's contact details are `S19`'s
content and must not become the subject here.

# What "Conversion-led" Means In A Section That Is Already Conversion

Every study in this section carries a booking route, so `004` cannot be distinguished by having
one. The distinguishing move is **friction**: `004` is the shortest possible path — one field and
one action, with everything else explicitly deferred to the call — while `001` collects what a
studio would normally need up front and `003` makes the stages of the request visible. The five
differ in how much they ask and how they ask it, not in whether they ask.

# The Governing Constraint

The claims rule in `../WELLNESS-DESIGN-DIRECTION.md` applies, with three additions specific to a
booking role. No study in this batch contains:

- **Invented availability.** No named slot, no "next available", no waiting time, no opening hours,
  no diary state of any kind. A placeholder cannot know a real studio's calendar. Where a study
  needs the visitor to express timing, it offers **preference bands** — morning, afternoon, evening,
  no preference — which are the visitor's input rather than the studio's claim.
- **Invented prices or durations.** No treatment length, no consultation fee, no deposit.
- **A promise about the outcome of booking.** No response-time guarantee, no "confirmed instantly".
  Where a study says what happens next, it says it in the conditional voice the studio actually
  controls.

**The forms are structure, not collection.** Every form in this batch is composed of native
controls with real labels and no `action`, no endpoint and no script. Nothing is sent anywhere and
nothing is stored. A study demonstrates the shape of the request; wiring it is Design Lab's
problem, not this workspace's.

# Out Of Scope

- A global site header, primary navigation or footer
- Contact facts — phone, address, hours — which belong to S19
- The closing page-end invitation, which belongs to S20
- Treatments presented as the subject, which belongs to S02
- Practitioners presented as the subject, which belongs to S04
- Prices, packages and memberships, which belong to S11 and S12

# Authoring Questions

**1. What is the primary visual element of this role?**

The form itself, and the calm around it. This is the one section where an interface element is the
subject, so the composition's job is to make a request feel unhurried rather than transactional —
which for this sector means space, few fields, and no urgency devices.

**2. What must a visitor understand immediately?**

What they are being asked for, how little of it there is, and what happens after they send it.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
