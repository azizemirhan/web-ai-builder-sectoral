# HEALTHCARE THEME CONTRACT

Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Written with `HC-S01` and governing all
twenty-seven sections.

This file is the sector's register, anti-patterns, media rules, claims limits and five themes. Every
`HC` study is authored against it, and every batch document records where it applies it.

---

## The Sector's Design Problem

Healthcare websites are built in one of two registers and both are wrong for the person visiting.

    The brochure: a stethoscope on a desk, a white-coat team laughing in a corridor,
    blue and white, "compassionate care", a wall of accreditation badges.

    The portal: a department directory, a form, a patient-record aesthetic,
    a heart-trace graphic, a dashboard of statistics.

The first is a picture of nothing in particular. The second is the hospital's own administration
shown to the public. Neither answers the question a visitor came with.

## The Governing Constraint — The Visitor Has A Symptom, Not A Shopping List

> **Nobody browses a clinic. They arrive with a symptom, a referral, a worry, or somebody else's care
> to organise.**

The sector designs for a comparison shopper. There is no such visitor. The real one is worried,
often in a hurry, and frequently on a phone, and they want three things answered before anything
else:

| The question | What the sector does | What it should do |
| --- | --- | --- |
| **Is this the right place for what I have?** | Lists departments | Say plainly what is seen here and what is not, and where to go instead |
| **How soon can I be seen?** | Says *"book online"* | Say how first appointments actually work and what the wait usually is |
| **What happens when I get there?** | Says *"compassionate care"* | Describe the first visit: who you see, what they do, what you leave with |

A design that answers those three has done the whole job. Everything else is secondary.

---

## The Three Honest Media Subjects

Every reserved area in this sector is one of three things. Nothing else earns a frame.

1. **The room the visit happens in** — the consulting room, the waiting area, the corridor, the
   treatment room — photographed from where the patient will be, in use, not staged empty.
2. **The people who will see you, named by role** — the doctor, the nurse, the receptionist — at
   work, not lined up. Never named; never a stock model.
3. **The equipment the text names** — a scanner, a monitor, a chair — only where the copy refers to
   it, and only as the thing itself.

**Never:** a stethoscope on a desk, a white-coat team laughing, a hand holding a pill or syringe, an
empty white corridor, a heart-trace or pulse line, a globe, a shield, a tick in a circle, a stock
doctor with folded arms.

## Anti-patterns

Not the sector's default styling device, and not a way to make a `005` distinctive:

- patient-record, chart and EHR aesthetics
- appointment-portal and admin dashboard imitation
- department directory tables and service matrices
- accreditation walls, badge rows and seal strips as the main device
- statistics panels with percentages, success rates or patient counts
- clinical protocol schedules, dosage tables, pathway flowcharts drawn as diagrams
- before/after evidence grids presented as proof
- intake and consent form imitation
- emergency-red alarm colour as a styling accent
- the blue-and-white hospital palette, and any cyan or aqua accent

## Claims, Evidence and Regulation

Medical communication is regulated in every market this catalog addresses. No `HC` study may
contain:

- an invented doctor, nurse or specialist name, qualification, registration, licence, board, award
  or professional body
- a success rate, percentage, patient count, survival figure, waiting-time guarantee or any
  outcome statistic
- the words *cure*, *guaranteed*, *painless*, *pain-free*, *permanent*, *risk-free*, *best*,
  *leading*, *world-class* or *award-winning* applied to care
- medical advice, a diagnosis, or a named condition presented with a treatment promise
- an invented price, fee, insurer, plan, or coverage statement presented as real
- an invented address, telephone number, opening hour or emergency line
- a fabricated testimonial, review, rating or before/after image

**Structure is authored; evidence is reserved.** A results role is composed as a comparison
structure with reserved areas and no outcome text. A stats role is composed without figures. A
testimonial role is a quotation structure with no attributed name. Condition and service names use
neutral category vocabulary — *skin*, *joints*, *heart*, *women's health*, *children* — never a
diagnosis with a promise attached.

Clinic-own countable facts that a real site would fill in — how many rooms, how many days a
first appointment usually takes, how many people are on the team — may appear as **demo values
marked `data-placeholder="true"`**, spelled as words, never as statistics about outcomes.

## Copy Direction

Visible copy is written as the clinic would actually speak to a worried person: plain, specific,
short sentences, no adjectives that cannot be checked. It says what happens, who does it and what
you leave with. It refuses *compassionate*, *dedicated*, *state-of-the-art*, *holistic*,
*patient-centred* and every other word a clinic writes when it has nothing to state.

Copy bands, by role: **hero, CTA and breadcrumb 40–90 words; standard sections 90–170; structured
and detail roles 170–230.** Absolute ceiling 250. Reserved fields count.

---

## Five Fixed Themes

Variant N keeps its theme across every section, so that variant N of all twenty-seven sections
assembles into one coherent site.

| Variant | Theme | Ground | Ink | Accent | Media ground | Soft text | Radius |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Linen & Sage | `#f7f5f0` | `#1f2a26` | `#3f6f5a` | `#e4e7dc` | `#5f6a64` | 20px |
| 002 | Porcelain & Plum | `#faf6f7` | `#33222c` | `#7a3b5c` | `#eedde4` | `#6f5c66` | 10px |
| 003 | Sky & Slate | `#f1f5f8` | `#172530` | `#2c5f8a` | `#d8e2ea` | `#526270` | 22px |
| 004 | Sand & Terracotta | `#fbf7f1` | `#2d241c` | `#b8562f` | `#efe1d1` | `#6d6157` | 28px |
| 005 | Night & Mint | `#14211f` | `#eef5f1` | `#9fd8c0` | `#223330` | `#a9bcb4` | 26px |

- Accent controls in 001–004 carry white or paper text; 005 carries dark ink on mint.
- 004's accent is for headings, labels and controls; small running text on the accent uses
  `#9a4525` for contrast.
- Focus rings use the accent and must contrast with the surface they sit on; inside an accent
  panel the ring switches to paper.
- Every study sets the host `body` background to its ground and declares its tokens on the study
  root. No cyan, no aqua, no alarm red.

## Page Rhythm

Every section is one of three shapes, and the shapes are read across the assembled page.

| Shape | Meaning |
| --- | --- |
| **A** | Item grid, media in every item, five to eight reserved areas |
| **B** | Anchored, one to three reserved areas |
| **C** | Type and colour, no reserved area |

1. Never more than two consecutive `A` sections at one variant.
2. Every assembled page needs at least one `C`.
3. A section is not entitled to media because it could have some.
4. A `C` records why it carries none.
5. Read the two sections above at the same variant before authoring.

A batch whose five shapes exactly repeat a previous batch's row is a flatness signal, not a rule
violation; break it when the content allows.

## Structure

Standalone HTML with the research `<meta>` block, a comment header carrying the study's reasoning,
scoped CSS under `.hc-sNN-VVV`, border-box descendants, a `1320px` frame with
`clamp(22px, 3.6vw, 58px)` insets, breakpoints at `1100`, `980`, `860` and `560`, a
`prefers-reduced-motion` block, visible focus, 44px targets. No framework, CDN, script, image,
iframe, SVG, form or remote resource. A hero carries an `<h1>`; every other section is labelled
by an `<h2>`. No global header, navigation or footer in any study.

**Never put a `border` and a `max-width` on the same element** — the rule belongs to the section
and the measure to the text. Where the bordered element is the paragraph, use `padding-right`.

Links to other sections are relative and at the same variant. Where the target section is not yet
authored, the control is a link to `#` and the batch record says so.

---

# Detailing Pass — the modern register applied to HC

Status: ACTIVE from 23 September 2026. Governs the V2 authoring of all one hundred and thirty-five
`HC` studies. Source: `../../standards/08-VISUAL-REFERENCE-STYLE.md`, read through this sector's own
constraint — *the visitor has a symptom, not a shopping list*. Everything above this line stays in
force: the three honest media subjects, the anti-patterns, the claims and regulation limits, the
placeholder rule, the page rhythm, the copy bands and the structural prohibitions. The pass rewrites
only the design layer. Where this section and the V1 language above disagree on surface treatment
(corner radius, decoration, disclosure behaviour), this section governs the V2 studies.

**S01–S14 carry a V1 content spine and it is kept whole.** S15–S27, and `HC-S14-003…005`, had no
studies at all; they are authored directly in this register, and their batch record carries both the
authoring and the design decisions in place of a `BATCH-V1.md`.

## The HC reading in one sentence

**A calm, modern clinic page: a confident sans display with one phrase in the accent, bare warm
fields of the room and the people at work, hairline structure, soft 6px corners, and one thin line
of structure drawn in CSS behind the composition — never an icon, never a badge, never a wall of
blue and white.**

Where the reference register's voice is a serif magazine, HC's is a clinic that has decided to speak
plainly. The serif is dropped and the sans carries the display. The softness the sector needs is
carried by a small corner radius on large fields, never by pills, shadows or the 20–28px blobs the
reference register explicitly rules out.

## The no-SVG rule stands, and it shapes the register

The structural prohibition above — *no framework, CDN, script, image, iframe, SVG, form or remote
resource* — is **not** relaxed by this pass. The reference register does not require vector marks;
§10 rules out icon rows outright. So HC carries no marks and no drawn ornament of any kind:

- Sections are opened by a **tracked uppercase eyebrow and a rule**, never by an icon beside a
  heading.
- The per-variant structure layer is drawn with **empty `<span aria-hidden="true">` elements
  carrying CSS borders only**. No gradient, no shadow, no background image, no pattern.
- Arrows in links and actions are the characters that follow the label, set through `content:`,
  which are type, not iconography.

## What HC translates

| Reference device | HC reading |
| --- | --- |
| Serif display with one italic word | **Sans display**, weight 550, `clamp(2.4rem, 4.6vw, 5rem)`, line-height 1.0, tracking −0.035em, sentence case, **one word or phrase in the accent** (`.ac`) — never italic, never bold inside bold |
| Statement line | Sans 400, `clamp(1.1rem, 1.8vw, 1.55rem)`, line-height 1.35, ink |
| Item title | Sans 650, 1.0–1.35rem, tracking −0.015em |
| Eyebrow / label | Sans 0.62rem, 700, 0.2em tracked, accent, uppercase — no mark beside it |
| Index numeral | **Word-numerals** — ONE to EIGHT, or an ordered list whose markers carry the count. No digit appears in visible copy outside a placeholder element or a field's ratio label |
| Hairlines plus one accent rule | Kept exactly: `--line` soft, ink strong, **one 3px accent lead rule per composition** |
| Tinted band | Paper darkened (`--band`), 6px radius, never a card stack |
| Bare media field | Flat `--media`, 6px radius, slate label bottom-left *inside* the field: `THE ROOM · 4:3`, `THE DESK · 3:2`, `IN USE · 21:9`, `THE NURSE · 4:5`, `THE SCANNER · 1:1` |
| Bordered rectangle action | 1px ink border, **2px radius**, uppercase 0.68rem tracked, trailing arrow character; a second action is an underlined text link |
| Refusal token | **`--no` is not red in this sector** — alarm red is banned above. The refusal token is a cool graphite, used as an edge, a chip border or the colour of a sentence that states a limit, never as a surface |

## The structure layer, by variant

One device per study, drawn once, in CSS only. It sits behind text (`z-index: 0`) or on the edge of
a phrase, never across a media field.

| Variant | Device | How it is built |
| --- | --- | --- |
| `001` | **Column rules** — three 1px vertical hairlines in the line tone, behind the head | three absolutely positioned spans with `border-left` |
| `002` | **Open bracket** — a 1px accent bracket at the top-left of the head | one span with `border-top` and `border-left` |
| `003` | **Bordered cell grid** — the composition's cells share 1px lines; no background layer at all | the grid itself, `border` on the container and one shared edge per cell |
| `004` | **Measure rule** — a 3px accent bar with two short end risers, under the key phrase | one span with `border-bottom` plus two riser spans with `border-left` |
| `005` | **Corner frame** — a 3px accent frame on two sides of the display column | one element with `border-left` and `border-top` |

## HC themes for the detailing pass

The five contract themes are kept by name and accent. The grounds are tuned to the register — warm,
never a clinical white floating on white — and each theme gains the `--line` and `--band` tones the
register's hairline-and-band structure needs. **`005` Night & Mint stays inverted**, as the contract
sets it, and is the sector's one dark ground.

| Variant | Theme | `--paper` | `--ink` | `--muted` | `--line` | `--media` | `--band` | `--accent` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `001` | Linen & Sage | `#f7f5f0` | `#1f2a26` | `#5f6a64` | `#dfddd4` | `#e4e7dc` | `#edeee5` | `#3f6f5a` sage |
| `002` | Porcelain & Plum | `#faf6f7` | `#33222c` | `#6f5c66` | `#e7dae0` | `#eedde4` | `#f4eaee` | `#7a3b5c` plum |
| `003` | Sky & Slate | `#f1f5f8` | `#172530` | `#526270` | `#d5dee6` | `#d8e2ea` | `#e6edf2` | `#2c5f8a` slate blue |
| `004` | Sand & Terracotta | `#fbf7f1` | `#2d241c` | `#6d6157` | `#e6dccd` | `#efe1d1` | `#f4ece1` | `#b8562f` terracotta |
| `005` | Night & Mint, inverted | `#14211f` | `#eef5f1` | `#a9bcb4` | `#2a3d39` | `#223330` | `#1c2b29` | `#9fd8c0` mint |

`--line-strong` is the ink. `--no` is `#5f6a72` on `001` to `004` and `#93a5a0` on `005`. The sans is
the system stack; no serif anywhere in HC; no web font. 004's small running text on the accent uses
`#9a4525`, as the contract sets.

**Radius supersedes the contract's per-theme column.** The V1 table's 10 to 28px is the blob the
reference register exists to avoid. In the V2 studies every large field, band and panel is **6px**
and every control, chip and small edge is **2px**. Nothing is round.

## Sector rules that remain in force

Unchanged and checked: the three honest media subjects and nothing else; no stethoscope, no laughing
white-coat team, no hand with a pill or syringe, no empty corridor, no heart-trace, no globe, no
shield, no tick in a circle; no patient-record or portal aesthetic, no department directory table,
no accreditation wall, no percentage or outcome statistic, no protocol flowchart, no intake-form
imitation, no alarm red, no cyan or aqua. No invented clinician name, qualification, registration or
body; no success rate, patient count or waiting-time guarantee; none of the words *cure*,
*guaranteed*, *painless*, *pain-free*, *permanent*, *risk-free*, *best*, *leading*, *world-class* or
*award-winning* applied to care; no medical advice or diagnosis with a treatment promise; no
invented price, insurer, address, telephone number or opening hour; no fabricated testimonial,
review or rating. Clinic-own countable facts stay demo values marked `data-placeholder="true"`,
spelled as words, and declared in a `placeholder-data` meta. Reserved areas stay empty. An `h1`
appears only on S01, S21 and the detail pages S23 to S27; every other section is labelled by an
`h2`. No global header, navigation or footer anywhere.

## The checker

`hccheck.ps1 -Dir <raw> -Sec SNN [-Fields '...'] [-AllowNav] [-AllowClaims '...']` verifies the
theme tokens, the `.hc-sNN-vvv` namespace, the batch token, structure and tag balance, **the absence
of any svg, script, form, iframe or remote reference**, the radius ceiling, the banned-decoration
list (gradient, shadow, dashed border, pill), the healthcare claims vocabulary, the digit rule, the
h1 rule and content parity across the five studies.

## Completion record — 24 September 2026

All **27 sections, 135 studies** are authored in the detailing pass and verified by measurement.

### What each section carries

Every section has a `BATCH-V2.md`. **S01–S13** had V1 studies and were re-authored from that
content spine. **S14–S27** had none: their content and design were authored together in one
pass, their records say so explicitly, and no fictional V1 stage was written for them.

| | Sections | Studies |
| --- | --- | ---: |
| Re-authored from a V1 spine | S01–S13 | 65 |
| Authored directly in the V2 register | S14–S27 | 70 |

### Verified, not asserted

- `hccheck.ps1` over all 27 sections — **27/27 ALL CHECKS PASS**.
- 135/135 studies carry the `V2-detailing` batch token.
- `<h1>` appears only in **S01, S21, S23, S24, S25, S26, S27** — the hero and the five detail
  pages, plus the subpage hero. Nowhere else.
- No `<script>`, `<svg>`, `<iframe>`, `<img>`, `<form>`, `<input>`, `<button>`, `<table>`,
  `<details>`, `<header>`, `<nav>` outside the S22 breadcrumb, or `<footer>` in any study.
- No remote reference of any kind: no `http://`, no `https://`, no `@import`, no `data:image`,
  no `tel:` and no `mailto:`. The only occurrence of the string `tel:` in the sector is inside
  an S27 header comment recording that there is no `tel:` link.
- No gradient, shadow, dashed border, pill or `background-image`; radius ceiling 6px on fields,
  bands and panels, 2px on controls and chips.
- No cyan, aqua or alarm red anywhere.
- No digit in visible copy outside the reserved-field ratio labels. Every numeral in prose is
  spelled as a word.

### Three legitimate checker allowances

Three sections trip the claims list because they **name the forbidden words in order to refuse
them**, which is the sector's own device. Each was read before being allowed:

| Section | Allowance | Why |
| --- | --- | --- |
| S06 Why Choose Clinic | `award` | *"What is not on this page: a figure, a rating, an award, or the word best. You could not check any of them."* |
| S11 Accreditations | `award` | the page lists what it will not carry — logos of bodies it is not a member of, awards |
| S17 About / Philosophy | `state-of-the-art\|compassionate\|patient-centred\|holistic` | the page refuses these four words by name |

S22 additionally needs `-AllowNav`, because the breadcrumb itself is the `nav` landmark.

**A trap worth recording:** `-AllowClaims` and `-AllowDigits` are `[string]` parameters taking a
pipe-separated allow list, not switches. Passing them bare, or as `$true`, sets the value to
`True`, matches nothing, and the section still fails — or, in a loop that does not read the
output, appears to pass. Pass the actual terms.

### One inherited defect, recorded rather than hidden

**S14** runs 260–287 words against the contract's 250 ceiling, because V1's own two studies are
289 and 266. Cutting the copy would be a content change, not a design change, so the spine was
kept and the overrun left documented in that section's record, with a note on where to shorten
it if that is ever wanted.

### Where the copy bands did not fit the role

**S21** (31–39 words) and **S22** (23–46 words) sit under the contract's 40–90 hero and
breadcrumb band. Both are template roles whose page-specific values are all reserved; the only
way to reach forty would be filler or an invented hierarchy. Each record states this.
