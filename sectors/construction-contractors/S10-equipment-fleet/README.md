# Section ID

CON-S10

# Section Name

Equipment Fleet

# Sector

Construction & Contractors

# Prefix

CON

# Planned Studies

CON-S10-001
CON-S10-002
CON-S10-003
CON-S10-004
CON-S10-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `CON-S10-001` | Universal / Safe |
| `CON-S10-002` | Premium / Editorial |
| `CON-S10-003` | Structured / Visual Modular |
| `CON-S10-004` | Conversion-led |
| `CON-S10-005` | Art-directed / Distinctive |

Read for this sector in `../CONSTRUCTION-DESIGN-DIRECTION.md`.

# Section Role

The plant, at length. `S05` carried it as one of three families with a line each; this is where it
gets a page.

# The Governing Constraint — The Specification You Need Is The Site's, Not The Machine's

The sector direction names this section's trap while describing a different variant: *becoming a car
advert; the subject is the work, not the plant.* On an equipment page that warning applies to all
five studies, because a fleet list **is** a car advert by default — a row of machines, photographed
clean, with their weights and reaches printed underneath.

    A fleet list is a car advert with the prices removed. A specification tells you what a
    machine can do somewhere. It does not tell you whether it can get onto your site.

So the section is not organised by machine. It is organised by **the site constraint each machine
answers**, and every entry says which one:

| On every entry | Why |
| --- | --- |
| **The site constraint it answers** | The client's actual question, and the only one a machine list never addresses |
| **Who operates it** | A machine is as good as the person in it, and that is not a specification |
| **What happens when it fails** | The `S05` ownership marker, carried through and deepened |
| **When it is the wrong answer** | The steer-away — some jobs need a specialist and a road closure |

# What Is Real, And What May Not Be Invented

| Element | Treatment |
| --- | --- |
| Kind of plant | **Real** — generic vocabulary: excavator, dumper, telehandler, roller, breaker |
| The site constraint it answers | **Real, and the content** |
| Operator and fitter arrangements | **Real** — practice, not specification |
| How it is held | **Real** — owned, long-term hire, retained, carried from `S05` |
| Machines held, ticketed operators, fitters | **Reserved fields** — countable facts the firm knows |
| Make, manufacturer or model | **Forbidden** — a third party's name, and the car advert in one word |
| Weight, power, reach, capacity, tonnage, bucket size | **Omitted** — this is the specification sheet, and it is the trap |
| Year, hours run, fleet value, utilisation | **Omitted** |
| Emissions or environmental rating | **Omitted** — `S17` owns practices, and a rating here is a badge |
| Plant media | **Reserved areas** — machinery **in use**, never at rest |

# The Media Rule Is Stricter Here Than Anywhere Else

The sector media direction allows *plant media — machinery in use*. On this page that stops being a
preference and becomes the rule that keeps the section out of the trap:

    No reserved area may be captioned for a machine at rest.

A photograph of clean plant on a forecourt is a car advert; a photograph of the same machine with an
operator in it, working, in mud, is evidence. `CON-S05-002` carried one at-rest yard area as a single
supporting image and that was defensible. Here plant is the whole subject, so at-rest is forbidden
and **every caption in this batch names the work, the operator, or the site.** The checker tests
for it.

# The Four Access Tiers

The organising fact a client needs first, and the one no fleet list gives them: **what can physically
get in.**

| Tier | Means |
| --- | --- |
| **Through a domestic gate** | Reaches a back garden, a side return, an occupied terrace |
| **Through a site gate** | Ordinary access, a hardstanding, a compound |
| **Needs a low-loader and a hardstanding** | Delivered rather than driven, and it has to have somewhere to stand |
| **Needs a road closure or a crane** | **Not us.** A specialist, a permit and somebody else's programme |

`003` is built entirely on this ladder. The fourth tier is the steer-away, and it is kept.

# The Refusal

Every study ends by naming what is deliberately absent, and this section's refusal is unusually
concrete:

> **There are no makes, models or tonnages on this page.** A specification tells you what a machine
> can do somewhere. Whether it can get down your access, stand on your ground and work in your hours
> is a different question, and it is the only one worth answering here.

Because the content requires naming the omitted specification vocabulary in order to reject it, each
study marks its refusal region with `data-refusal`, as `S07` and `S09` do, and the checker permits
that vocabulary only inside it.

# Boundary With S05, S06, S07 And S17

| Section | What it owns |
| --- | --- |
| `S05` Capabilities | **What we hold**, across three families, with a line each |
| `S06` Project Delivery Process | **What happens to you**, and where each door closes |
| `S07` Safety Program | **How the site is run** — authority, briefing, the chain |
| `S10` Equipment Fleet | **The plant**, organised by the site constraint it answers |
| `S17` Sustainability | **Practices** — never a rating, and never an emissions badge |

    S05 says we own our excavators. S10 says which of your problems that solves.

The test against `S05`: an entry that only states how a machine is held has written `S05` again. Each
one must name a site condition. The test against `S07`: plant may be described as operated and
maintained; the moment a study describes who stops the job, it has written `S07`.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/
