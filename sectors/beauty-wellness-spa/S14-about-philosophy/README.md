# Section ID

WELL-S14

# Section Name

About Philosophy

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S14-001
WELL-S14-002
WELL-S14-003
WELL-S14-004
WELL-S14-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S14-001` | Universal / Safe |
| `WELL-S14-002` | Premium / Editorial |
| `WELL-S14-003` | Structured / Visual Modular |
| `WELL-S14-004` | Conversion-led |
| `WELL-S14-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

Why the studio works the way it does. The section sets out the thinking behind the way treatments
are run here — the positions the studio holds, and what those positions cost it.

It answers: *why is it like this, and did they choose it on purpose?*

# The Governing Constraint

An about section is the classic home of invented facts: a founding year, a founder's name, a
number of years, a city, a headcount, an origin anecdote. **None of that is authorable here.**

Applying the `S11` field-versus-figure test:

| Element | Test | Treatment |
| --- | --- | --- |
| Founding year | Every studio has one; the empty field asserts nothing | **Reserved slot**, where a study uses one |
| Founder portrait | As `S04` | **Reserved media slot** |
| A founder quotation | As `S10` — the value is that a real person said it | **Reserved quotation area** |
| Years of experience, headcount, number of guests | A figure that also carries a credential or scale claim | **Omitted entirely** |
| An origin story | Not a field at all — it is prose that would have to be invented outright | **Omitted entirely** |

**What is real here, and it is the whole point of the section.** Every other `WELL` section has an
operating policy line as its only unreserved content: `S07` commitments, `S08` sequence, `S09`
inspection, `S10` gathering, `S11` pricing, `S12` behaviour. **`S14` is where the reasoning behind
those lines lives.** An argument is not a fact — a studio can genuinely hold a position without a
placeholder inventing anything — so the beliefs, and the trade-offs they cost, are honest content.

    S07 says: one guest at a time.
    S14 says: because a room with someone else being shown in and out of it is not a quiet room,
    and we would rather earn less per day than sell that.

**The strongest device this section has is what the studio decided *not* to do.** Naming the
deliberate omissions — no selling in the room, no discount for buying a bundle, no double-booking —
is differentiating, verifiable against the rest of the site, and impossible to fake by accident,
because each one costs the business something.

**Not present in any study:** an invented founding year, founder name, personal history, origin
anecdote, city, address, headcount, years of experience, number of guests treated, award,
qualification, press mention or membership; a superlative comparison to other studios; an efficacy
claim in any form.

# Boundary With S07 And S04

| Section | What it owns |
| --- | --- |
| `S07` Benefits | **The commitments** — what holds true on every visit, stated flat |
| `S14` About Philosophy | **The reasoning** — why those commitments exist and what they cost |
| `S04` Specialists | **The people** — who does the work |

    "One guest at a time" is S07. Why we run it that way, and what we give up to, is S14.
    Who is in the room is S04.

`S14` must not restate `S07`'s list in longer sentences. Where a commitment appears here it appears
as the *conclusion* of an argument, not as an item.

# Out Of Scope

- A global site header, primary navigation or footer
- The commitments stated as a list, which belongs to S07
- The order of a visit, which belongs to S08
- Practitioner profiles, which belong to S04
- Any figure describing the business — age, size, volume

# Authoring Questions

**1. What is the primary visual element of this role?**

Words, unusually for this sector. This is the one section whose subject is an argument, so the
compositions are decisions about **how much prose is on screen at once** — from `005`, which is one
sentence at display scale, to `002`, which is a reading column. Media supports; it does not lead.

**2. What must a visitor understand immediately?**

That the way the place runs is deliberate, and that the studio can say why.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
