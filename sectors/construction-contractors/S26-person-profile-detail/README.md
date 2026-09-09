# Section ID

CON-S26

# Section Name

Leader / Project Expert Profile

# Sector

Construction & Contractors

# Prefix

CON

# Planned Studies

CON-S26-001
CON-S26-002
CON-S26-003
CON-S26-004
CON-S26-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `CON-S26-001` | Universal / Safe |
| `CON-S26-002` | Premium / Editorial |
| `CON-S26-003` | Structured / Visual Modular |
| `CON-S26-004` | Conversion-led |
| `CON-S26-005` | Art-directed / Distinctive |

Read for this sector in `../CONSTRUCTION-DESIGN-DIRECTION.md`.

# Section Role

S26 — Person / Profile Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all twenty sectors; the
section name above is this sector's own term for it. The detail page for one person: who they are,
what they work on, and how to reach them.

# The Governing Constraint — Will This Person Be On My Job

Every profile page in this industry makes the same promise and none of them state it: **that the
person on the page will be on your job.** It is the promise a tender interview makes and the one
most often broken, and `S11` has already said so at team scale.

    A profile page is read by somebody asking one question. Will this person be on my
    job? The honest page answers how often, and then answers the harder half — what
    happens the week they are not.

So every study in this batch carries **both halves**:

| Half | What it says |
| --- | --- |
| **How often you will see them** | Two mornings a week on your site, and every morning in the fortnight either side of the dates that cannot move |
| **What happens when they are not there** | Holiday, illness, and the third one nobody prints: **they get moved to another job** |

**The second half is the check.** A page that answers only the first is the tender interview again,
in a browser.

# The Second Device — What They Cannot Decide

The `S07` authority device and the `S11` decision table, narrowed to one person and then turned
round. Every study prints what this person settles standing on your site **and what they have to
ring somebody about**:

| Settles on the spot | Has to ring somebody |
| --- | --- |
| The sequence inside the week | Anything with money on it |
| What gets ordered for the next day | Anything that moves the completion date |
| Stopping the work | Taking somebody off site for good |

> **A page that lists only what somebody can decide is describing an owner, not an employee.** The
> second column is the one a client needs, because it tells them how long an answer takes.

# The Third Device — What Is Only In Their Head

The reason absence costs anything is that a person carries the job in their head, so every study
names **what gets written down so that it is not only in there**:

    The outstanding items. The drawing revision the work is actually being built to. And
    the three things the client has asked for that are not in the contract yet.

That last line is the one that saves an argument in month four, and it is the honest reason a firm
writes anything down at all.

# What This Section Will Not Do

- **No invented credential.** No qualification, registration, membership, chartership, award or
  training card, and none of them as an empty labelled field either — the `WELL-S26` rule, and at
  the scale of one person a credential list is anti-pattern two, the certification wall.
- **No years-in-the-trade figure**, no project count, no headcount. The counter rule.
- **No invented name, portrait, social handle or personal email address.**
- **No personal quote.** A sentence in quotation marks attributed to a reserved name is a fabricated
  statement by a person who does not exist.
- **No biography, career history or previous employer.**
- **No hard hat and folded arms.** Anti-patterns one, five and thirteen arrive together on a profile
  page and they arrive as a single photograph.

# What Is Real, And What May Not Be Invented

| Element | Treatment |
| --- | --- |
| Name | **Reserved field** — it is the subject of the page |
| Portrait | **Reserved area**, optional; a filled slot means a real person who has consented |
| Role and what the post covers | **Real** — generic vocabulary, as in `S11` |
| How often they are on your site | **Real** — a pattern, not a promise |
| What they settle, and what they must ring about | **Real** |
| What happens when they are away | **Real** |
| Qualifications, memberships, awards, years | **Omitted entirely, not reserved** |
| Number of jobs they run at once | **Reserved field** — a countable fact the firm knows |

# The Scaffold's Responsive Rule, Made Structural

> Portrait and identity must stay paired at every width; a name must never end up beside or above
> the wrong portrait when the layout reflows.

Carried unchanged from `WELL-S26`: **every study with a portrait wraps the portrait and the name in
a single `<figure>`, with the name in the `<figcaption>`.** They cannot be separated by any reflow
because they are one element, and the checker fails a portrait that sits outside one.

# The Portrait Is Optional, And One Study Proves It

The scaffold: *a profile must read completely with the portrait absent.* **`002` carries no portrait
at all** and is the proof.

# Boundary With S11, S23 And S24

| Section | What it owns |
| --- | --- |
| `S11` Leadership Team | **The set** — who you deal with, and what each can decide |
| `S23` Construction Service Detail | **One offering**, whoever runs it |
| `S24` Project Detail | **One job**, and what changed on it |
| `S26` Leader / Project Expert Profile | **One person in full** — how often, and what happens without them |

    S11 says which of them you will see. S26 is one of them, at length, including the
    weeks you will not.

The test against `S11`: the frequency marker may be **stated**; the moment a study lays out the
other roles beside it, it has written `S11` again.

# One Mechanism, In One Study

The batch's anchors belong to `004`, routing in-page. No other study carries one.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
