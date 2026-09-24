# Section ID

CON-S09

# Section Name

Company Stats

# Sector

Construction & Contractors

# Prefix

CON

# Planned Studies

CON-S09-001
CON-S09-002
CON-S09-003
CON-S09-004
CON-S09-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `CON-S09-001` | Universal / Safe |
| `CON-S09-002` | Premium / Editorial |
| `CON-S09-003` | Structured / Visual Modular |
| `CON-S09-004` | Conversion-led |
| `CON-S09-005` | Art-directed / Distinctive |

Read for this sector in `../CONSTRUCTION-DESIGN-DIRECTION.md`. **This is the section that document's
governing constraint was written for.**

# Section Role

The counter. Four figures about the firm, and nothing else pretending to be one.

# The Rule Is Already Settled

The sector direction fixed the treatment of every figure in this sector before any section was
authored, and this is where it applies literally:

| Figure | Treatment |
| --- | --- |
| Year founded | **Reserved field** — every firm has one |
| Projects completed | **Reserved field** — a countable fact the firm knows |
| People employed | **Reserved field** — same |
| Largest project by value | **Reserved field** — a fact, not a claim |
| Sectors and trades covered | **Real** — generic vocabulary, and not a figure |
| *Happy clients* | **Omitted** — asserts a survey nobody ran |
| *Satisfaction, on-time, on-budget percentages* | **Omitted** — assert a measurement system |
| *Awards won* | **Omitted** — invented bodies, invented judgements |
| *Safety record, incident rate, days without* | **Forbidden** — `S07` |
| Price per square metre, day rate | **Omitted** — `S15` owns money |

So the content is decided. **What is not decided, and what this batch is actually about, is the
shape.**

# The Governing Constraint — Four Different Quantities, Four Identical Boxes

Every contractor's stats band is a row of four equal cells with four numbers in them. That row is
the lie, and it is a design lie rather than a copy one:

    A date, a running total, a snapshot and a single extreme are not the same
    kind of number, and drawing them as one asserts that they are.

Look at what is actually in the row:

| Figure | What kind of quantity it is | What the identical box hides |
| --- | --- | --- |
| **Year founded** | A fixed point in the past | It is not a score. It does not grow because the firm is good |
| **Projects completed** | A cumulative running total | Meaningless without *since when* |
| **People employed** | A snapshot, true today and different next month | Presented as permanent when it is provisional |
| **Largest project by value** | A single extreme | Read as typical, which is exactly what it is not |

**Every study in this batch draws each figure according to what kind of quantity it is**, and no
study contains a row of four identical cells. That is the section's whole design argument, and it
survives the fact that all four values are reserved — because the shape is the part being authored.

# Every Figure Carries Its Basis

A number without a denominator is a shape rather than a fact, so each figure carries a **second
reserved field** stating what it is counted against:

| Figure | Its basis |
| --- | --- |
| Year founded | Under this name — firms change names, and a longer date is not always a longer history |
| Projects completed | Counted since a stated year, on a stated definition of *project* |
| People employed | As at a stated date, and split between our own books and long-term labour |
| Largest project by value | The one job, and the year it completed |

**Eight reserved fields minimum per study.** A reviewer sees not only the four numbers the finished
page will assert but the four qualifications that make them readable.

# The Sentence This Section Is Built Around

> **The largest project we have done is not the size of project we usually do.**

*Largest project by value* is the figure in this row most designed to be misread, and it is the one
a client uses to decide whether their own job is too small to matter. Every study prints the
correction next to the figure rather than in a footnote.

# The Refusal, And Why It Names What It Refuses

Each study carries a block naming the figures deliberately absent and why, in the client's interest
rather than the catalog's:

- **Happy clients** — nobody ran that survey. The number is the client list with a compliment
  attached.
- **Satisfaction and on-time percentages** — assert a measurement system, and the definition of *on
  time* is set by whoever reports it.
- **Awards** — an invented body making an invented judgement.
- **Safety figures** — forbidden, and `S07` explains why an incident rate rewards under-reporting.

Because the section's content requires naming these to reject them, **each study marks its refusal
region with `data-refusal`**, exactly as `S07` does, and the checker permits the vocabulary only
inside it.

# The Only Real Thing On The Page Is The Part That Is Not A Number

Sectors and trades covered are generic vocabulary and are therefore real. Every study carries them,
and every study says so:

> Everything on this page with a figure in it is reserved. The only thing here we can state outright
> is the list that has no number attached to it.

# What May Not Appear

| Element | Treatment |
| --- | --- |
| The four figures and their bases | **Reserved fields** |
| Sectors and trades covered | **Real** |
| The *not typical* correction | **Real, and required** |
| Any fifth figure | **Omitted** — if it is countable and not one of the four, it is a claim |
| Percentage of any kind | **Omitted** |
| A growth arrow, trend line or *up from last year* | **Omitted** — asserts a series nobody has |
| Client logos, awards, ratings, reviews | **Omitted** |
| Safety figures of any kind | **Forbidden** |
| Media | **None** — a counter has nothing to photograph |

# Boundary With S01, S05 And S08

| Section | What it owns |
| --- | --- |
| `S01` Hero | May carry a reserved counter as a device; this section is where it is explained |
| `S05` Capabilities | Depth as a **field, demoted** — explicitly so as not to become a stats band |
| `S08` Certifications | Reserved registrations, **enlarged** — identifiers, not quantities |
| `S09` Company Stats | **The counter itself**, and the argument about how it should be drawn |

`S05` demoted its numbers to avoid writing this section. `S08` enlarged its numbers because a
registration is an identifier rather than a quantity. `S09` is the only section where the number is
both large and a quantity, which is why it is the only one that has to explain itself.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/
