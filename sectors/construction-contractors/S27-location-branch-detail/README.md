# Section ID

CON-S27

# Section Name

Office / Regional Branch Detail

# Sector

Construction & Contractors

# Prefix

CON

# Planned Studies

CON-S27-001
CON-S27-002
CON-S27-003
CON-S27-004
CON-S27-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `CON-S27-001` | Universal / Safe |
| `CON-S27-002` | Premium / Editorial |
| `CON-S27-003` | Structured / Visual Modular |
| `CON-S27-004` | Conversion-led |
| `CON-S27-005` | Art-directed / Distinctive |

Read for this sector in `../CONSTRUCTION-DESIGN-DIRECTION.md`.

# Section Role

S27 — Location / Branch Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all twenty sectors; the
section name above is this sector's own term for it. The detail page for one physical place: where it
is, what happens there, and how to reach it.

# The Governing Constraint — Almost Nobody Reading This Is Coming Here

A location page assumes a visitor. In this industry that assumption is wrong, and it is wrong in a
way that decides the whole section:

    A contractor's office is not a shop. Almost nobody who reads this page is coming
    here, and the client least of all — their meetings happen on their own site.

So the page is not directions. It is an answer to the question a client actually has, which is
whether **this** office is the one whose mornings reach their job, and an answer to the three people
who genuinely do turn up.

# The Three People Who Actually Come

Every study names them, in this order, because it is the order of how many arrive:

| Who | What the page owes them |
| --- | --- |
| **A delivery** | Where the wagon goes, who signs for it, and the fact that the yard is emptiest by the time the sites start |
| **A supplier or subcontractor** | That turning up unannounced is not how anybody gets on a list, and what to send instead |
| **Somebody looking for work** | The honest route, kept short, and never *see our careers page* when the real answer is a person in the yard |

**A client is not on that list**, and every study says so plainly. It is the most useful sentence on
the page, because it sends them to the place where their answer actually is.

# What Is Here, And What Leaves

A yard is a place things leave from, so the section describes the place by its output:

| Leaves here | Means |
| --- | --- |
| **Plant off our own yard**, the same day | The reason a yard exists at all |
| **The fitter, in a van** | A breakdown is a drive rather than a hire-desk telephone call |
| **The manager, before the sites start** | The `S14` attendance rule, narrowed to one office |

And what does not: **plant hired locally when the site is further out**, which is the honest half and
belongs to `S14`'s outermost band.

# Access Is Answered By Conversation

Carried unchanged from `WELL-S16` and `WELL-S27`. A row of facility icons would be invented, and a
tick is a promise about a place nobody has measured. Worse here than in most sectors: **a yard is not
a level floor.**

> Tell us before you come and we will say honestly what the route from the gate is like, including
> when the answer is that it is not passable.

# The Arrival Rule

The one piece of real, sector-native arrival information a construction office can publish without
inventing anything:

    You cannot cross the yard in what you drove in. Boots and a hi-vis, or you will be
    met in the office instead — which is fine, and is what most people should do anyway.

# What Is Real, And What May Not Be Invented

| Element | Treatment |
| --- | --- |
| Address, telephone, the yard's own line | **Reserved fields** |
| Branch name, and the region this office runs jobs in | **Reserved fields** |
| A map | **Reserved area only** — never an embed, never drawn, never pinned |
| Media of the place | **Reserved areas**, and two studies carry none |
| Opening hours | **Omitted** — an empty hours table asserts a weekly schedule and prints figures. Stated as practice instead: the yard is emptiest by the time the sites start |
| Directions, travel time, nearest station | **Omitted** — the scaffold rules out invented directions |
| What is here and what leaves | **Real** |
| Who is based here | **Role tokens**, and the honest note that the site managers are not |
| The arrival rule, and access by conversation | **Real** |
| Reviews, ratings, claims about the place | **Forbidden** — the scaffold's own line |
| *Nationwide*, *national coverage* | **Forbidden** — the `S14` rule |

**Not present in any study:** an address, a postcode, a telephone number, a set of hours, a drawn map,
a pin, a travel time, a distance, or a digit in visible copy.

# The Scaffold's Responsive Rule, Made Structural

> Address and contact details are the content most likely to be needed on a phone and must be
> first-class at small widths, **not pushed below decorative media**.

As in `WELL-S27`, made impossible to break rather than promised: **in every study the contact block
comes before any media or map area in source order.** There is no width at which it can reflow below
one, because it never comes second. The checker compares the source position of the first contact
element with the first media area in each file.

# The Map Is Reserved, And Argued With

Where a study carries a map area it is a reserved rectangle with no remote dependency of any kind,
and the study says what it would be worth:

> A map tells you where this office is, which is the one fact on this page that will not help you.

**`002` carries no map and no media at all**, which is a legitimate answer rather than an omission.

# Boundary With S14, S10 And S19

| Section | What it owns |
| --- | --- |
| `S14` Service Areas | **Where we work**, and what attendance costs at each distance |
| `S10` Equipment Fleet | **The plant**, by the site condition it answers |
| `S19` Contact | **How to reach a person**, whichever office |
| `S27` Office / Regional Branch Detail | **This place** — what leaves it, and who actually comes |

    S14 says how far a morning reaches. S27 says which office the morning starts from.

The test against `S14`: this section may state **that a job further out is run from another office**;
the moment it lays out the bands and what is lost at each, it has written `S14` again.

# One Mechanism, In One Study

The batch's anchors belong to `004`, routing in-page. No other study carries one.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
