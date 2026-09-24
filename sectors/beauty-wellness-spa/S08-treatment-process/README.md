# Section ID

WELL-S08

# Section Name

Treatment Process

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S08-001
WELL-S08-002
WELL-S08-003
WELL-S08-004
WELL-S08-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S08-001` | Universal / Safe |
| `WELL-S08-002` | Premium / Editorial |
| `WELL-S08-003` | Structured / Visual Modular |
| `WELL-S08-004` | Conversion-led |
| `WELL-S08-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

The shape of a visit. The section walks through what happens from arriving to leaving, in order,
so a visitor knows what they are agreeing to before they book.

It answers: *what actually happens when I come in?*

# Boundary With S06, S07 And S02

| Section | What it owns |
| --- | --- |
| `S06` Consultation Booking | The **request** — the form and the route into an appointment |
| `S07` Benefits | The **commitments** — what holds true on every visit, in no order |
| `S08` Treatment Process | The **sequence** — what happens first, then next, once you are here |
| `S02` Treatments | The **individual treatments** on offer |

    A form you fill in is S06. "One guest at a time" is S07.
    "First you sit down, then we talk, then the treatment" is S08.

`S08` describes the shape a visit takes **whatever treatment was booked**. A step that only applies
to one treatment belongs in that treatment's detail page, not here.

The first step of this sequence deliberately begins at **arrival**, not at booking. Starting at
"send us a request" would make this section a second, weaker version of `S06`.

# The Governing Constraint

Two rules govern this role, one carried forward and one specific to it.

**1. Steps describe the action, never the effect.** The procedural-description rule established for
`S02` applies at full force here, because a process section is where efficacy language enters most
naturally: *"Step 3: extraction — clears congestion and refines pores."* Every step in this batch
says what is done, not what it is meant to achieve. No study contains an efficacy claim, outcome
description, percentage, rating, review, client, award, certification or invented statistic.

**2. No durations, and no schedule register.** A visit has no stated length, no per-step timing and
no session count anywhere in this batch. That rules out the obvious device: a step table with a
timing column is a **treatment protocol**, which `../WELLNESS-DESIGN-DIRECTION.md` lists among the
sector's anti-patterns. A numbered sequence is not a schedule — it is a sequence, which is what
this role genuinely is — but the moment it acquires a time column, a dosage, or a course length it
has become clinical paperwork and fails the direction.

    Allowed: "Then you lie down and the work begins."
    Not allowed: "Step 3 · 20 min · Extraction · reduces congestion".

# The Sequence

Five steps, used consistently across the batch so the five studies read as one section. They are
written to hold for any treatment in `S02`.

| Step | What happens |
| --- | --- |
| 1 · Arriving | You come in, leave your things, and sit down. Nothing starts until you are ready. |
| 2 · A short conversation | We ask what you want from the session and what your skin has been doing. No clipboard. |
| 3 · The treatment | You lie down and the work begins. Pressure, warmth and products are adjusted as we go. |
| 4 · Coming back up | Time to sit, have something to drink, and come round before you stand. |
| 5 · Afterwards | If something would suit you at home we say so now — after, not during. |

Step 5 is deliberately the operational other half of the `S07` commitment *nothing sold in the
room*. The two sections should agree; they must not repeat each other's framing.

# Out Of Scope

- A global site header, primary navigation or footer
- The booking request itself, which belongs to S06
- The commitments, which belong to S07
- Individual treatments, which belong to S02
- Devices, machines and product ranges, which belong to S09
- Prices, durations, session counts and packages, which belong to S11 and S12

# Authoring Questions

**1. What is the primary visual element of this role?**

Sequence made visible — a spine, a descent, a band, a numbered rhythm. The composition's job is to
make five steps read as one continuous visit rather than five separate facts, and to do it without
becoming a schedule.

**2. What must a visitor understand immediately?**

That it is short, that nothing surprising happens in it, and where they get a say.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
