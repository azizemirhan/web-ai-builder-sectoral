# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S26`
- Section Name: `Leader / Project Expert Profile`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S26-001` | Universal / Safe | AUTHORED | `raw/CON-S26-001.html` |
| `CON-S26-002` | Premium / Editorial | AUTHORED | `raw/CON-S26-002.html` |
| `CON-S26-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S26-003.html` |
| `CON-S26-004` | Conversion-led | AUTHORED | `raw/CON-S26-004.html` |
| `CON-S26-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S26-005.html` |

Twenty-sixth batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — Will This Person Be On My Job

Every profile page in this industry makes the same promise and none of them state it. `S11` said so
at team scale; `S26` is one person at length, so it arrives at the hard version:

    A profile page is read by somebody asking one question. Will this person be on my
    job? The honest page answers how often, and then answers the harder half — what
    happens the week they are not.

**Both halves are in all five studies**, and the second one is the check:

| Half | What every study prints |
| --- | --- |
| How often | **Two mornings in a normal week.** Every morning in the fortnight either side of a date that cannot move. Inside the hour when the work has stopped |
| What happens when they are not there | Holiday. Illness. **And the one nobody prints — they get moved to a job that is in trouble** |

> A page that answers only the first half is the tender interview again, in a browser.

## The Second Device — What They Cannot Decide

The `S07` authority device and the `S11` decision table, narrowed to one person and then turned round:

| Settles standing on your site | Has to ring somebody about |
| --- | --- |
| The sequence inside the week | Anything with money on it |
| What gets ordered for tomorrow | Anything that moves the completion date |
| Stopping the work | Taking somebody off site for good |

    A page that lists only what somebody can decide is describing an owner, not an
    employee.

**The second column is the one a client needs**, because it is the column that tells them how long an
answer takes. It costs a firm nothing to print and it is missing from every profile page in the trade.

## The Third Device — What Is Only In Their Head

Absence costs something because a person carries a job in their head, so every study names what gets
written down so that it is not only in there:

1. **The outstanding items**, with who owes each one and the day it was asked for.
2. **The drawing revision the work is actually being built to**, which is not always the latest issued.
3. **The things the client has asked for that are not in the contract yet.**

The third line is the one that saves an argument in month four, and it is the honest reason a firm
writes anything down at all.

## Study Records

| Study | Ground | Model | Anchors |
| --- | --- | --- | --- |
| `001` | `#ede6d6` | Identity and the post, frequency, settles against rings, the weeks away, the routes | none |
| `002` | `#faf4e0` | **The handover note, published as the profile.** No portrait anywhere | none |
| `003` | `#dbe0e4` | **A week in the post, drawn as five banded days**, and the two fortnights that suspend it | none |
| `004` | `#141c18` | **The three things to have in front of you**, and routing that sends three callers in four elsewhere | the batch's only ones |
| `005` | `#c3bdb0` | **In their head against written down**, at display scale | none |

### `002`, the handover note

The document one manager leaves for whoever covers them. It is **the only thing in this trade written
to be read by somebody who is not the author, about a job the author is not on that week** — which is
exactly what a profile page is being asked to be.

Distinct from the colophon of `S16-002`, the standfirst of `S21-002`, the errata of `S24-002` and the
head-note of `S25-002`. **It also carries no portrait at all**, and is the batch's proof of the
scaffold rule that a profile must read completely with the portrait absent.

### `003`, the banded week

The sector direction names this variant's trap as *the specification table*; five criteria with ticks
would have turned a person into a product. So the module is **a week whose bands are unequal on
purpose, and the largest band on it is not your site.**

Two bands do the arguing. The blue one is your job, twice. **The red one is a half day somewhere in
the week that goes to something that has gone wrong** — a week drawn without it would be a week
nobody in this trade has ever had.

### `004`, the routing that sends you away

The conversion-led study is the one most tempted to answer yes to everything, so its largest block is
an ask that collects nothing — **have three things in front of you: where it is, what stage it is at,
and the date that matters and why** — and its second block sends three callers in four somewhere else:

> If it is on site and it is today, ring the site, not this person. At seven in the morning they are
> driving, and the answer you need is standing on the slab.

It also prints **what this person will tell you before you ring** — that the date is not achievable,
that the change costs a fortnight rather than a day, that the weather is not what put you behind.

### `005`, in their head against written down

One split held at display scale. The left column is **reserved on purpose and says so**: the shape of
everything a person carries about a job that has never been put on paper, drawn rather than written
**because that is exactly how much use it is to anybody else** in the week they are not here.

The right column is the answer, and it is short. **Writing things down is not a large undertaking in
this trade, only an unpopular one.** The portrait is the smallest thing on the page.

## The Scaffold's Responsive Rule, Made Structural

> Portrait and identity must stay paired at every width; a name must never end up beside or above the
> wrong portrait when the layout reflows.

Carried from `WELL-S26` and enforced by the checker: **the portrait and the name are one `<figure>`,
with the name in the `<figcaption>`.** No reflow can separate them because there is nothing to
separate. A portrait found outside such a figure fails the batch.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG or form control anywhere in the batch.
- **One-mechanism check: PASS.** Two anchors, both in `004`, both routing in-page.
- **Question check: PASS.** *Will this person be on my job* stated in all five.
- **Both-halves check: PASS.** Frequency and absence in all five, including *moved to a job that is
  in trouble* and *the reason nobody prints*.
- **Authority-pair check: PASS.** What they settle and what they must ring about in all five, with
  *describing an owner, not an employee* stated in all five.
- **Written-down check: PASS.** All three items in all five.
- **Figure-pairing check: PASS.** Exactly one reserved portrait in `001`, `003`, `004` and `005`,
  each inside a figure that also carries the name; **`002` carries none and declares `media-mode:
  none`.**
- **Credential check: PASS.** No qualification, registration, membership, chartership, training card
  or award claim, **and none as an empty field**; the omission is explained in visible copy in all
  five.
- **Quote check: PASS.** No quotation mark anywhere in the batch, and the reason is printed: a quote
  over a name that has not been filled in was written by nobody.
- **Adjective check: PASS.** No *expert*, *experienced*, *passionate*, *dedicated*, *visionary* or
  *industry leader*.
- **Handle check: PASS.** No social handle, no personal address, no *follow us*.
- **Density check: PASS.** Between ninety-one and one hundred and forty-three visible words per
  reserved field.
- **Placeholder check: PASS.** No em-dash placeholder; every reserved value labelled.
- **Drawing check: PASS.** Nothing drawn at an angle.
- **No-refusal-region check: PASS.** The architecture run carries none.
- **Digit check: PASS.** No digit in visible copy in any of the five, including the week diagram.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.**
- Section-shell check: **PASS.**
- Scoped-CSS check: **PASS.**
- Markdown-artefact check: **PASS.**
- Ground check: **PASS**, after two corrections. Five distinct grounds, none used by `S01`–`S25`.
- Render check: **PASS**, after two corrections.

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `004` | Carried the absence half but **not the frequency half**, and named what this person cannot decide without ever naming what they can | Both added. The conversion-led study was the one that had quietly dropped half the section's argument, which is exactly the study where that matters |
| `001`, `002` | `#f2f0ea` and `#fcfaf2` — the second sits **one step from `S16-002`'s ground** on a contact sheet | Regrounded to `#ede6d6` and `#faf4e0`. Non-duplication is the rule; being told apart is the point of the rule |
| `003` | The paired modules had `margin-bottom: 0` and the grid above them none, so **the module beneath collided with them** | A margin on the pair itself |
| `004` | `.away li b { display: block }` also caught the `<b>` inside the ordered list, so item one broke into two lines and **the second began with a comma** | Scoped to `.away ul li b` |

## Checker Note

**No content rule failed on its first run** — a first in this sector, and the reason is that the two
devices carried over from `S11` were written before the studies were.

The batch's own new check is the **figure-pairing check**: a portrait must sit inside a `<figure>`
that also contains the name field, or the study fails. It is the first check in this catalog derived
from a *responsive* rule rather than a content one — **the scaffold said a name must never end up
beside the wrong portrait, and the way to guarantee that is to make them one element** rather than
two elements a reviewer has to re-check at every width.

The second is the **credential check**, which bans the claim and its empty field together. The
studies must also say why the field is absent, so the refusal is visible to a reader rather than only
to the checker.

**Fourth occurrence in this sector of the descendant-selector defect** (`S13-005`, `S17-005`,
`S23-003`, now `S26-004`): a rule keyed to an element type inside a block captures the same element
type in a later block, and the result passes every check while looking deliberate. It is why every
study is rendered and looked at.

## Notes

- Twenty-sixth authored batch in the `CON` sector. `S01`–`S26` are complete.
- **The reusable outcome is the second column.** A firm can publish what each person settles on the
  spot and what they have to ring about, and a client reading it knows how long an answer takes
  before they need one. Nothing about it is a claim, so nothing about it can be disputed.
- The second is the absence half. **A profile that does not say what happens the week the person is
  away is describing an employee who never takes one**, and the third reason — being moved to a job
  in trouble — is the one that costs something to print and is worth the most.
- The third is `002`'s form. **A handover note is a profile that has already been tested**, because
  somebody who is not the author has had to work from it.
- `S27 Office / Regional Branch Detail` is next, and it closes the sector.
