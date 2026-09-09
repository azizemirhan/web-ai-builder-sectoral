# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S26`
- Section Name: `Practitioner / Specialist Profile`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S26-001` | Universal / Safe | AUTHORED | `raw/WELL-S26-001.html` |
| `WELL-S26-002` | Premium / Editorial | AUTHORED | `raw/WELL-S26-002.html` |
| `WELL-S26-003` | Dense / Information-heavy | AUTHORED | `raw/WELL-S26-003.html` |
| `WELL-S26-004` | Conversion-led | AUTHORED | `raw/WELL-S26-004.html` |
| `WELL-S26-005` | Sector-native / Distinctive | AUTHORED | `raw/WELL-S26-005.html` |

Sixth batch in the extended architecture set. The sector's reading of the scaffold is merged into
`./README.md`, in the same pattern as every other section.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — A Profile Whose Subject Cannot Be Named

`S04` established the sector's rule for people: **role leads, identity is reserved.** `S26` is a page
whose entire subject is one person, so the rule arrives at its hardest case — and the scaffold's own
Out Of Scope list settles most of it before the batch starts: *no fabricated qualifications,
registrations, memberships, awards or credentials; no invented social handles; no testimonials or
ratings attributed to a person.*

| Element | Treatment |
| --- | --- |
| Name | **Reserved area** — the subject of the page, as the title is in `S25` |
| Portrait | **Reserved slot**, optional; a filled slot means a real person who consented |
| Role and focus | **Real** — `S03` vocabulary |
| Qualifications, registrations, memberships, awards | **Omitted entirely, not reserved** |
| Years of experience, treatment counts | **Omitted** |
| Social handles, personal email | **Omitted** |
| Testimonials, ratings | **Omitted** |
| Contact route | **Real** — *ask for them by name when you book* |

**Why credentials are omitted rather than reserved.** An empty *"Qualifications: —"* asserts that
the studio lists credentials and that this person's are pending. In a sector adjacent to medicine a
credential list is the clearest route into the clinical register the sector direction rules out. It
is the `S10` empty-star failure and the `S17` empty-expiry failure, and `S04` decided it already.

**What is left is enough, and the batch's whole thesis is one line:**

    A visitor is not choosing a biography. They are choosing how somebody works.

## The Scaffold's Responsive Rule, Made Structural

> Portrait and identity must stay paired at every width; a name must never end up beside or above
> the wrong portrait when the layout reflows.

Most catalogs would satisfy this with a promise in a note. **Here it is made impossible to break:**
every study that carries a portrait wraps the portrait and the reserved name in a single `<figure>`,
with the name in the `<figcaption>`. They are one element, so no reflow can separate them. The
checker verifies it — a portrait outside a figure that also contains the name area fails the batch.
**Four portraits, four paired, verified.**

## Study Records

### WELL-S26-001 — Universal / Safe

- **Layout model:** The paired identity figure at the left; how they work, what they will say no to,
  and the contact route beside it.
- **The dependable shape**, and the one that establishes the batch's two content blocks: *how they
  work* is manner, not credentials; *what they will say no to* is the `S23` steer-away applied to a
  person.
- **Responsive strategy:** the portrait becomes 3:2 and the identity leads at 860px; nothing can
  separate name from portrait because they are one figure.

### WELL-S26-002 — Premium / Editorial

- **Layout model:** One 62ch column, no picture. Reserved name, the category, three written
  passages, the contact line.
- **The variant the scaffold requires:** *"a profile must read completely with the portrait
  absent."* This is the proof, and it is also the honest default — **a portrait is a picture of a
  real person who has agreed to appear**, and plenty of practitioners would rather not.
- **A profile with no photograph is a harder test of the writing**, because there is nothing else to
  look at. What replaces the picture is three passages that could not be written about anybody
  else: what they ask before anything is decided, what they do when the plan is wrong, what they
  turn down.

### WELL-S26-003 — Dense / Information-heavy

- **Layout model:** Paired identity above three record panels and a full-width omissions panel.
- **The device — the omissions panel.** The scaffold's Out Of Scope list is printed as visible
  content, with a reason for each absence: qualifications (*"a list of certificates is how a
  treatment room starts pretending to be a clinic"*), time served (*"some of the best hands in the
  building belong to the newest person in it"*), ratings (*"being averaged by strangers changes how
  somebody works, and not in the direction you would want"*).
- **Why that is the right dense content:** in a sector adjacent to medicine, a page that explains
  why it is *not* showing you a wall of certificates is more informative than the wall, and it is
  entirely authorable because it describes the studio's position rather than the person's history.

### WELL-S26-004 — Conversion-led

- **Layout model:** Paired identity beside one panel: ask for them by name, what that gets you, and
  when somebody else would be better.
- **The action is not a booking, it is a name.** `S20` owns the closing ask and `S06` the flow. What
  this page converts is **a preference** — the visitor deciding they want *this* person rather than
  whoever is free — so the ask is *ask for them by name*, and the panel says exactly what asking
  gets you and what happens when it cannot be honoured.
- **The steer away:** *"Somebody else here might suit you better… you will be told and pointed at
  whoever it is, before the booking."* A profile that cannot say that is a sales page.
- **What it avoids:** no rating, review count, testimonial attributed to a person, availability
  indicator, *"books up fast"*, social handle or personal email.

### WELL-S26-005 — Sector-native / Distinctive

- **Layout model:** The introduction you would get in the room, written in the second person as a
  five-step sequence, with the paired identity held small at the head.
- **Why this is sector-native:** in most sectors a profile answers *is this person qualified*. In
  this one the visitor is deciding **who is going to be touching them**, and the deciding factor is
  manner. So the page is written as the introduction a receptionist would give, ending at the point
  where you are lying down and it has gone quiet.
- **The portrait is deliberately small** — at profile scale a large portrait invites the visitor to
  judge a face, which is not what they are choosing. It is the only circular portrait in the sector.
- **What it refuses:** the professional-biography register entirely — where they trained, what they
  are certified in, how long they have done it. All out of scope, all would be invented, and none of
  it answers the question being asked.

## Structural Diversity

| Study | Shape | Portrait | What carries the page | Ground |
| --- | --- | --- | --- | --- |
| 001 | Identity left, practice right | 4:5, paired | Two lists: how they work, what they decline | Pale blue-grey `#d0d7de` |
| 002 | One 62ch column | **None** | Three written passages | Warm ivory `#f0eae0` |
| 003 | Identity above four panels | 1:1, paired | The omissions panel | Pale lilac `#e9e4ef` |
| 004 | Identity beside one panel | 4:5, paired | Ask by name, and the steer away | Warm dark `#3b3630` |
| 005 | Small identity above a sequence | 1:1 circular, paired | A second-person introduction | Mid blue-stone `#9fa8ac` |

Grounds do not repeat any of the 125 already in use. Nearest-neighbour channel distances: `005` is
26 away, `001` 18, `004` 12, `003` 7, `002` 5 — the light end of the space is now genuinely crowded,
and that is worth recording as the sector approaches its last section.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is what
  a profile becomes when the person cannot be named — two lists, three passages, a record with an
  omissions panel, a single named ask, or an introduction.
- **Document-metaphor justification:** `NONE`. No certificate, badge, credential card or CV device
  is used, which matters here because those are precisely the shapes this role invites.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** No `<script>`, `<iframe>`, form element or inline `style`.

## Media Slots

| Slot | Study | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Portrait | `001` | Still image, 4:5 | Reserved area labelled *a real person who has agreed to appear*; paired with the name in one `<figure>` |
| Portrait | `003` | Still image, 1:1 | As above, at record scale |
| Portrait | `004` | Still image, 4:5 | As above |
| Portrait | `005` | Still image, 1:1, circular | As above, small by decision |
| Name | all five | **Text** | Reserved area inside the identity figure |

`002` reserves no media at all. **Every portrait slot states in its own label that a filled slot
means a real person who consented** — the scaffold's requirement, made visible rather than assumed.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- Territory validation: **PASS.**
- Heading-level check: **PASS.** No `<h1>`; each labelled by an `<h2>`.
- **Identity-pairing check: PASS — this batch's defining check.** Four portraits, four inside a
  `<figure>` that also contains the reserved name. The scaffold's responsive rule cannot be broken
  by any reflow because the two are one element.
- **Portrait-optional check: PASS.** `002` carries none and reads complete.
- Accessibility QA: **PASS.** `aria-labelledby`, `prefers-reduced-motion`, 48px-plus targets,
  reserved areas labelled.
- Responsive QA: **PASS.** Identity leads and stays whole at every width in all five.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer.
- Scoped-CSS check: **PASS.**
- **Credential and proof check: PASS.** Twenty-nine assertive patterns — *certified in*, *qualified
  in*, *member of*, *registered with*, *trained at*, *diploma in*, *licensed*, *accredited*,
  *award-winning*, *specialist in*, *expert in*, *years of experience*, *rated*, *testimonial*,
  *five-star*, `@`, social platforms, money, percentages, durations, availability pressure. **Zero
  matches.** No digit appears in visible copy anywhere in the batch.
- **Soft check, five occurrences, all in `003`'s omissions panel**, verified in context — the study
  has to name *qualifications*, *certificates* and *ratings* in order to say it is not showing them.
  Sixth batch in a row to need the soft tier for exactly that reason.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. Second batch in a row to need none.

## Notes

- Twenty-sixth authored batch in the `WELL` sector, twenty-fourth without references, sixth of the
  seven extended architecture roles. **One section remains: `S27`.**
- **The reusable outcome is that a responsive rule can be made structural instead of promised.** The
  scaffold asked that a name never be separated from the wrong portrait; wrapping both in one
  `<figure>` makes the failure impossible rather than unlikely, and it is checkable in one line.
  Any catalog rule of the form *"X must stay with Y at every width"* should be answered this way.
- The second outcome is `003`'s omissions panel: **in a sector where the conventional proof is
  forbidden, printing the list of proofs you are not showing — with a reason for each — is better
  content than the proofs would have been.** It is the same family as `S20`'s *"you will not find a
  countdown on this page"*, `S24`'s record of what is not recorded, and `S25`'s refusal list. Four
  sections have now arrived at it independently; it is the sector's signature move.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch,
  because `python3` on this machine resolves to a Windows Store placeholder rather than an
  interpreter. With 130 studies now authored and one section left, porting the generator to Node is
  the single highest-value remaining task after `S27`.
