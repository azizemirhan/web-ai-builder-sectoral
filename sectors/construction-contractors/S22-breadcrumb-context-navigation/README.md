# Section ID

CON-S22

# Section Name

Breadcrumb / Context Navigation

# Sector

Construction & Contractors

# Prefix

CON

# Planned Studies

CON-S22-001
CON-S22-002
CON-S22-003
CON-S22-004
CON-S22-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `CON-S22-001` | Universal / Safe |
| `CON-S22-002` | Premium / Editorial |
| `CON-S22-003` | Structured / Visual Modular |
| `CON-S22-004` | Conversion-led |
| `CON-S22-005` | Art-directed / Distinctive |

Read for this sector in `../CONSTRUCTION-DESIGN-DIRECTION.md`.

# Section Role

Where this page sits, what else it belongs to, and what the next one is ordered by.

# The Governing Constraint — A Trail Shows One Path And Hides The Others

    A breadcrumb shows one path. A project belongs to at least three, and the two it
    does not show are the ones a reader is most likely to want.

A project page sits under a sector, under a service, and under the year it finished. The chrome picks
one and the reader never learns the other two exist. **So this section shows the trail, says which
axis it runs on, and names the memberships the trail is hiding.**

# The Three Parts

| Part | What it does |
| --- | --- |
| **The trail** | One path, with the axis it runs on stated in words |
| **Also in** | The other memberships this page has, named and reachable |
| **Next** | A sibling, **with the ordering declared** — *next by the same sector*, not *next project* |

# Next By What?

    Every site in this trade has a next arrow, and none of them says what it is next
    by. It is almost always the order the pages were published in, which is an order
    nobody reading has any interest in.

Declaring the ordering costs a line and turns a decorative arrow into navigation. Where more than one
ordering is useful, `004` offers the choice and says which is the default and why.

# Every Crumb Is A Page, Or Plainly Not A Link

The commonest lie in this component is the invented intermediate level:

> Home / Our Work / **Commercial** / **Retail** / Project

where neither *Commercial* nor *Retail* is a page anybody can visit. So:

    A crumb that cannot be visited is not drawn as a link. It is drawn as a label, and
    it is visibly not a link.

`003` demonstrates it: one of the three axes has no index page behind it, and it is shown as a label
rather than quietly styled to look like the others.

# What This Section Will Not Do

- **No invented level.** If it is not a page, it is not a link.
- **No self-link.** The current page is the end of the trail, not a link to itself.
- **No position count.** *Project four of twenty-seven* is a figure, and it tells a reader nothing
  they can use.
- **No back-to-top dressed as navigation.**
- **No arrow diagram of the site.** That is decoration standing where a path should be.

# The Placeholder Convention For The Architecture Run

Carried from `S21`:

    The em-dash placeholder is not used in the architecture sections. A reserved value
    reads as the word *Reserved*, and a reserved title is drawn as a measure.

In the main-page run a slot sits inside a sentence and a dash reads as a field. In the architecture
run the slots sit inside navigation, where a dash reads as a broken link.

# What Is Real, And What May Not Be Invented

| Element | Treatment |
| --- | --- |
| The crumb labels for real levels (*Projects*, *Sectors*) | **Real** — generic vocabulary |
| The statement of which axis the trail runs on | **Real** |
| The declared ordering of the next page | **Real** |
| The project name, the sector value, the service, the year, the office | **Reserved fields** |
| Sibling page names | **Reserved fields** |
| Any count, position or figure | **Forbidden** |
| An intermediate level with no page behind it, drawn as a link | **Forbidden** |

# Boundary With S21 And S24

| Section | What it owns |
| --- | --- |
| `S21` Subpage Hero | **Which page this is**, and what is on it |
| `S24` Project Detail | **The body of the page** |
| `S22` Breadcrumb / Context Navigation | **Where it sits, what else it belongs to, and what next is ordered by** |

    S21 says which page. S22 says where that page is, and what it is next to.

# Links Rather Than One Mechanism

This is the one section in the sector where links are the content, so the usual
*one-mechanism-in-one-study* rule does not apply. Instead:

- **Every anchor in the batch routes in-page**, as everywhere else in this catalog.
- **No study carries a button or a form.** A breadcrumb with a call to action in it is a breadcrumb
  that has stopped being one.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/
