# Section ID

WELL-S20

# Section Name

Final Booking CTA

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S20-001
WELL-S20-002
WELL-S20-003
WELL-S20-004
WELL-S20-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S20-001` | Universal / Safe |
| `WELL-S20-002` | Premium / Editorial |
| `WELL-S20-003` | Structured / Visual Modular |
| `WELL-S20-004` | Conversion-led |
| `WELL-S20-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

The closing ask. The last thing on the page, for a visitor who has read everything above and is
deciding whether to act now.

It answers: *is this the moment, and what am I actually agreeing to if I press it?*

# The Governing Constraint — Two Rules, And The Second Is The Sector's Dignity

**1. No mechanism.** `S06` is the booking moment and carries the machinery — the flow, the fields,
what happens at a consultation. A final CTA that contains a booking form is **`S06` in the wrong
place**, and a catalog that allows it stops being able to tell the two sections apart.

| Section | What it owns |
| --- | --- |
| `S01` Hero | The **opening** proposition, at the top of the page |
| `S06` Consultation Booking | The booking moment and **the means to start it** |
| `S19` Contact | The ways in for someone with a **question** rather than a booking |
| `S20` Final Booking CTA | The **closing ask** — a decision, not a form |

    S06 gives you the means. S20 gives you the moment.

**So no study in this batch contains a form field, a select, a date or a time.** The actions are
links. What fills the space instead is the answer to *what am I agreeing to*.

**2. No pressure.** This is the section where a wellness site most often loses its register.
*"Only two slots left this week"*, a countdown, *"book by Friday"*, *"join 4,000 clients"* — every
one of those is an invented figure, and even with real numbers behind them they read as a business
that needs the money. The sector direction rules out the whole family:

| Device | Treatment |
| --- | --- |
| Scarcity count | **Forbidden** — an invented figure and a manufactured pressure |
| Countdown or deadline | **Forbidden** |
| Client / booking counts | **Forbidden** — the `S10` rule; a count asserts real data |
| Discount, offer, saving | **Forbidden** — the `S12` rule, a relationship between two figures |
| Price of anything | **Omitted** — `S11` owns money |
| Star rating or review score | **Forbidden** — the `S10` rule |

**Not present in any study:** an invented figure of any kind; a countdown, deadline, scarcity or
availability count; a discount, offer, saving or price; a client, booking or review count; a star
rating; a testimonial; an invented telephone number, email address or address; a form field, select,
date or time input.

# What Is Real — The Reassurance, Not The Push

What actually moves somebody at the foot of a wellness page is not urgency. It is knowing that the
step is small and reversible. All of this is operating policy, so all of it is authorable:

1. **What happens immediately after.** One step — somebody gets in touch, or a time is held. Not a
   schedule, on the `S08` rule.
2. **What it does not commit you to.** You can move it. You can change your mind at the end of the
   consultation and nothing has been spent. Asking costs nothing.
3. **The second route.** For anyone not ready to book, a way to ask instead — which belongs to
   `S19`, so it appears here as one line and a link, never as a second form.
4. **That we do not push.** Saying plainly that this section will not tell you two slots are left
   is itself the strongest thing it can say, and it is only sayable because the batch has given up
   the device.

# Out Of Scope

- A global site header, primary navigation or footer
- A booking form, appointment picker, treatment selector or any field, which belong to S06
- Contact details as a block, which belong to S19
- Prices, packages and memberships, which belong to S11 and S12
- Testimonials, ratings and counts, which belong to S10

# Authoring Questions

**1. What is the primary visual element of this role?**

The action itself, and the space around it. With the mechanism gone and the pressure devices
forbidden, each study has to decide how much page a single button deserves and what one sentence
earns the space beside it.

**2. What must a visitor understand immediately?**

What pressing it starts, and how little it commits them to.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
