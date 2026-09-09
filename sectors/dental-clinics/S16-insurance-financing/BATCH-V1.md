# BATCH V1

## Batch Identity

- Sector: `Dental Clinics`
- Prefix: `DN`
- Section ID: `DN-S16`
- Section Name: `Insurance and Financing`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

Sixteenth batch in the `DN` sector, authored against `../DENTAL-THEME-CONTRACT.md`. The sector stands
at **80 studies**.

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `DN-S16-001` | Universal / Safe | 001 Chalk | **B** | Two runs, two parties, then the person who does the paperwork | 1 | 205 |
| `DN-S16-002` | Premium / Editorial | 002 Linen | **C** | **The sentence that replaces the logo wall** | **0** | 186 |
| `DN-S16-003` | Structured / Visual Modular | 003 Slate | **B** | **One rule down the middle, and nothing crosses it** | 2 | 221 |
| `DN-S16-004` | Conversion-led | 004 Daylight | **B** | **The refusal risk first**, in a filled band | 1 | 204 |
| `DN-S16-005` | Art-directed / Distinctive | 005 Dusk | **C** | **One line across the page with a sentence set into it** | **0** | 202 |

## The Most Reserved Section In The Sector

Every conventional element of an insurance and financing page is already reserved by an earlier batch:

- **`S13` reserved named bodies and brands.** An insurer is one; so is a plan.
- **`S10` reserved the figures.** No rate, no percentage, no monthly amount, no excess, no currency.
- **`S13` also reserved the badge**, in image or vector form, which is what a logo wall is made of.

That removes the logo row, the plan comparison, the finance calculator and the *from £x a month*
strip — the entire conventional content. **Sixth section running where the conventional material
cannot be produced**, and the deepest one yet.

What remains is the part the logos exist to obscure.

## The Governing Idea

> **Your policy is between you and your insurer. We are not part of it, and what you owe us does not
> change if they say no.**

A small practice is not on anybody's panel. The patient is treated, the patient pays, the patient
claims it back. **Almost nobody knows that until the claim comes back short**, and the row of
recognisable marks is precisely what stops them finding out earlier.

## The Two Sides

Shared across all five studies.

| Between you and your insurer | Between you and us |
| --- | --- |
| **We are not on anyone's panel.** You are treated here, you pay here, and you claim it back yourself | **The paperwork you need.** An itemised receipt with the treatment codes on it, on the day, without asking |
| **What policies usually will not cover.** Cosmetic work, anything started before the policy began, and the excess | **We do not arrange credit.** No third party, no commission to us, and nobody's application to fill in |
| **If the claim is refused.** You owe us the same amount, and we will have told you that amount before you agreed to anything | **If you need to spread it.** We do it ourselves. Same total, and it stops when you stop |

**`We do not arrange credit` is the refusal that costs something.** Arranging finance is a revenue
line for a great many practices, and it puts pressure on a treatment plan in exactly the way
commission on treatment does. `S01` refused the second; this refuses the first, and the two together
are the same argument about who the plan is for.

**`If the claim is refused` is the fact the logo wall exists to keep out of view.** It is the single
thing that decides whether a patient can afford to say yes. The pairing is what makes it usable rather
than merely honest — *and we will have told you that amount before you agreed to anything.* **The risk
is real and the surprise is not.**

## The Five Compositions

- **`001`** — the safe reading: two runs, two parties, labelled, with the accent on our side.
- **`002`** — **one sentence instead of a wall of marks.** *We are not on anyone's panel* is worth more
  than every logo it replaces, because it tells the reader the structural fact that decides what
  happens at the desk. No image: replacing a logo wall with a photograph would be the same move in a
  different medium — a recognisable thing standing where a fact should be.
- **`003`** — **one rule running the full height, and nothing crosses it.** Three facts each side, no
  row and no shared container joining them. **Both photographs are on our side, and the left column
  says so**: *there is no photograph on this side, none of it happens here.* The media asymmetry is
  the asymmetry the rule draws.
- **`004`** — the conversion-led reading puts the worst case in the loudest place. The band carries
  *you owe us the same amount*, which is what the logo wall's association is built to imply away. The
  trade is exact: **this section has no logo wall**, and the logo wall is the highest-recognition
  asset a clinic site has.
- **`005`** — **the whole section is one line**, with the sentence set into it: *we are not part of
  anything above this line.*

`005` is the sector-native reading, and it is the counterpart to `003` rather than a repeat of it.
`003` divides the material with a vertical rule and invites a reading across — two columns,
comparable. **`005` refuses the comparison.** A horizontal boundary is not a pair of columns; it is a
floor. And the rule carries type because **a rule with nothing on it is a divider a reader passes
over, while a rule with a sentence set into it has to be read to get past** — the correct behaviour
for the one fact this section exists to deliver.

## Page Rhythm

Rule 1: `S15` carries no `A`, `S14` carried three, so `A` was available. None taken — insurance has
two honest subjects, not five to eight.

Rule 2 is satisfied at every variant. **Two `C` studies**, both because their arguments are made out
of type and a photograph would start a second one.

## Placeholder Data

**None.** Sixth batch running with an empty placeholder set.

## Verification Record

- Word band `170–230` (structured): **205 / 186 / 221 / 204 / 202.** All five in band.
- Content parity: **19 shared fields checked across all five studies, zero missing.**
- Reserved areas: **1 / 0 / 2 / 1 / 0.**
- **Fabrication scan, written for this section: clean.** No insurer, plan or finance provider named;
  no figure, rate, percentage, `APR`, *interest-free* or currency; no *we work with*, *approved
  provider*, *preferred partner* or *in network*; no coverage promise.
- **No `<svg>` in any study.** A logo is a logo whether it is an image or a vector — the rule from
  `S13`, and it matters more here than it did there.
- Tag balance: **0 unbalanced elements** across all five. No `<script>`, `<img>`, `<iframe>`,
  `<table>`, `<form>`, `<input>` or `<button>`; no absolute URL, no `@import`, no `<link>`; every rule
  scoped to its study namespace; no non-`<li>` child directly inside a list.
- Theme conformance: **5/5** match the contract's grounds, inks and accents. Frame `1320px` and the
  `prefers-reduced-motion` block present in all five.
- Composition collisions: **no exact match, no near matches** across the sector's eighty studies.
- Rendered at 1440px and read: all five correct.

### A tooling failure worth recording

The parity diff reported `ring first` missing from `001`. **The content was there.** The checker
replaces every tag with a space when it strips markup, so a sentence broken across an `<em>` boundary
came out with a double space and stopped matching a single-space pattern.

The fix — collapsing runs of whitespace — then **broke the checker completely**, reporting sixteen of
nineteen fields missing across all five studies. The cause is the one recorded in the `S05` batch and
not yet fully absorbed: **the Bash tool collapses `\\` to `\` in embedded scripts**, so
`.replace(/\s+/g,' ')` was written to disk as `.replace(/s+/g,' ')` — a regex that deletes the letter
`s` from the text being matched.

Rewritten without any backslash at all —
`.split(String.fromCharCode(10)).join(' ').replace(/  +/g,' ')` — and the diff came back clean at
19/19. **The standing rule from `S05` needs its stronger form: do not write a backslash into a script
through the Bash tool.** Regex literals survive because they are typed once; anything constructed or
edited through a shell string does not.

## What This Batch Fixes For The Rest Of The Sector

- **Name the parties before describing the services.** Where a third party is involved, say which
  arrangement the practice is actually in.
- **A recognisable mark is not evidence.** Replacing a logo wall with a photograph is the same move in
  another medium, and `002` refuses both.
- **A boundary can be drawn horizontally or vertically, and they say different things.** A vertical
  rule invites comparison; a horizontal one refuses it.
- **A rule that must be noticed carries type.** An empty divider gets passed over.
- **Never write a backslash into a script through the Bash tool.** Second occurrence, now with a
  concrete failure attached.
