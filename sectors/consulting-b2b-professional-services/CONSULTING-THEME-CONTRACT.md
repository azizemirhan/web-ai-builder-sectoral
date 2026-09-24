# Consulting & B2B Professional Services — Direction and Theme Contract

Prefix `CONS`. This document does two jobs: it sets the sector's visual register and anti-patterns,
and it fixes the five themes that make a variant number assemble into a website. It is the `CONS`
reading of `../../standards/01-AUTHORING-STANDARD.md` and follows the model established in
`../construction-contractors/CONSTRUCTION-THEME-CONTRACT.md`.

## The Register

    Wellness sells atmosphere. Construction sells the removal of risk.
    Consulting sells judgement — and judgement has no photograph.

The visitor is a senior buyer de-risking a decision they cannot make alone, or cannot be seen making
alone. Four questions sit behind every page:

1. **Do you understand my problem?** — this industry, this altitude, not consulting in general.
2. **Have you done this before?** — under confidentiality, which is the sector's hardest constraint.
3. **Who actually shows up?** — the partner in the pitch, or a team of juniors afterwards.
4. **What does working together actually look like?** — commitment, shape, and how it ends.

**The visual consequence:** this is the sector with the least honest photographic subject. Buildings,
sites, treatment rooms and products all exist; a strategy does not. So `CONS` is carried by
**typography, composition, restraint and space**, and the one photographic subject it can use
honestly is **people** — the individuals who would actually be on the engagement.

## Anti-patterns

These are the `CONS` equivalent of the drawing sheet in `ARC`. None may be a default styling device:

- Stock handshakes, boardroom tables, laptop-and-coffee desks, glass towers, city skylines at dusk.
- Abstract network graphics, node meshes, globes, circuitry, "connection" motifs.
- Generic upward arrows, rising bar charts and growth curves used as decoration.
- **The 2×2 matrix used as ornament.** This is the sector's signature failure. A framework diagram
  is legitimate only where the section role is the framework itself, and never in a hero.
- Maturity ladders, pyramids, funnels and wheels deployed to look rigorous.
- Jargon compounds — *synergistic transformation enablement*, *value unlock*, *holistic
  end-to-end*. Consulting copy earns authority by being plainer than expected, not denser.
- Technical-document metaphors generally: the constraint in `standards/01-AUTHORING-STANDARD.md`
  applies here with force, because this sector is the most tempted by them.

## Composition Devices

The anti-pattern list above was not enough on its own. `CONS-S02` was authored against it, passed
every prohibition in it, and was still rejected as technical — because the list said what not to
build and never said what to build. So this section is the positive half, and it governs every
`CONS` section.

### The idiom that was rejected

A content section built out of **full-width ruled rows**: a numeral in a left gutter, text in the
middle, a right-aligned uppercase label column, and a hairline between every row. That is a table.
It reads as a schedule, a register or a contents page whatever the palette is, and it is the same
failure this workspace already corrected in `ARC`. Specifically banned as default devices:

- a hairline rule under every item in a list;
- a right-aligned metadata or label column;
- a numeral gutter used as a table column rather than as a graphic element;
- text-only boxes presented as cards.

**A card without media is a table cell with rounded corners.** Corners and colour never fixed this;
structure does.

### The devices to build with

Every supplied reference composes its content sections from these. Use them:

| Device | What it looks like |
| --- | --- |
| **Card grid** | Three or four up, each card carrying its own image area above a short label and a title |
| **Horizontal slider / snap rail** | Tall image cards, the next one peeking past the frame edge so the reader can see there is more |
| **Featured card + compact cards** | One item given double width or height and a large image, the rest compact around it |
| **Offset / staggered gallery** | Two columns of image cards, one column dropped so pairs never align |
| **Numbered card set** | 01–06 as graphic numerals inside cards, one card held in the accent as the live module |
| **Badge over media** | A pill sitting on top of an image area, marking one item |
| **Pill labels** | Category and discipline names as pills, never as tracked uppercase in a side column |
| **Big-numeral stat row** | Figures at display size with a small label beside them, no boxes |

### The test to apply before a section is finished

1. **Where is the media?** A content section should carry a reserved image area in most of its items,
   not one slot bolted to the side. Count them.
2. **Would this survive as a table?** If the layout could be rewritten as rows and columns without
   losing anything, it *is* a table and must be rebuilt.
3. **Is the hierarchy in the scale, or in the rules?** Modern composition separates items by size,
   ground and space. Document composition separates them with lines.

4. **Has this skeleton been used at this variant already?** Not by memory — by running
   `node review/check-composition-collisions.js <sector>`. It fingerprints every study and reports
   same-variant matches, exact and near.

   This test exists because the rule above it failed in practice. `CONS-S07-002` was authored as a
   near-copy of `CONS-S05-002` — statement, offset voice, wide plate, one column of numbered blocks,
   a second plate, an underlined link — and its own comment header claimed it varied the device
   while moving one element. **Checking a section against the two above it by eye does not scale
   past about four sections.** Two adjacent sections sharing a skeleton is the worst case, because
   the reader meets them back to back.

   A reported match is not automatically a defect; two sections may legitimately share a simple
   shape. Every one has to be looked at, and the decision recorded in the batch document.

Move toward: large confident type, generous negative space, editorial pacing, real portraiture,
one decisive accent, media in every card, and a stated position rather than a described capability.

## Page Rhythm — The Rule Above The Section

A study is authored alone and judged alone, and that is how the previous two rules were written. It
is not how the catalog is used. **Variant N of every section stacks into one page**, so a rule that
makes each section good can still make the page bad.

That is exactly what happened after *Composition Devices* was added. The correction there —
"a card without media is a table cell with rounded corners" — was read as *put an image in every
card*, and `S02`, `S03` and `S04` were each authored as a six-card grid with six reserved images.
Alone, every one of them works. Stacked, the reader gets four consecutive bands of identical image
tiles, which no real website looks like.

### The three section shapes

Every section is authored as one of these, and the shape is recorded in its batch document:

| Shape | What it is | Media |
| --- | --- | --- |
| **A — Item grid** | Cards, tiles or panels, media in every item | 5–8 areas |
| **B — Anchored** | One or two large images anchoring text-led content: image left with the points right, a lead image with blocks beside it, a bento where only the big tiles carry photography | 1–3 areas |
| **C — Type and colour** | No reserved media. Composition carried by scale, colour fields, pills and space | 0 areas |

**Shape B is the default, not shape A.** A page made only of A is a catalogue; a page made only of C
is a document. B is what most of a real website is, and A and C are the accents.

### The rule

1. **Never more than two consecutive sections in shape A** at the same variant.
2. **Every assembled page must contain at least one shape C.** Written first as "one in any run of
   six", which produced exactly one C study in twenty-five — the rule was satisfiable by ignoring it.
   It is now per variant: read down a variant's sections and if none is C, one of them is wrong.
3. **A section is not entitled to media just because it could have some.** Ask what the photograph
   is of. If the honest answer is "something related to this topic", there is no photograph — there
   is a grey rectangle standing in for one, and the section is better built from type and colour.
4. A section authored as C must record why in its batch document, exactly as a study with no media
   slot must.
5. When a section is authored, **read the two sections above it at the same variant first.** Its
   shape is chosen against them, not in isolation.

### Why B is worth designing well

"Image left, points right" sounds like the safe option and is usually the strongest one: the
photograph gets enough space to be a photograph rather than a thumbnail, and the copy gets to be a
list somebody can actually read. Most of the supplied references use it more than they use grids.
What makes it modern is the same thing that makes anything modern here — scale, one accent, generous
space, pills instead of tracked labels, and **no hairline row rules anywhere in the list**.

## What May Not Be Invented

| Element | Treatment |
| --- | --- |
| Year the practice was founded | **Placeholder demo value** — see below |
| Engagements completed | **Placeholder demo value** — see below |
| People / consultants / partners | **Placeholder demo value** — see below |
| Offices | **Placeholder demo value** — see below |
| Industries and disciplines covered | **Real** — generic vocabulary, not a claim |
| **Named clients or logos** | **Forbidden in every section.** Confidentiality is the sector brief's own limitation, and it applies above `S24`, not only inside it |
| *Value delivered, £/$ figures, ROI multiples* | **Omitted** — asserts a measurement nobody ran |
| *Client retention %, satisfaction %, NPS* | **Omitted** — asserts a survey system |
| *Awards, rankings, tier placements* | **Omitted** — invented bodies and judgements |
| A named individual in a portrait slot | **Reserved** — the slot says what the portrait is, never who |

## Placeholder Demo Values

A study is judged on its composition, and an empty dashed box at counter scale does not show the
composition — it shows a hole. So **the firm's own countable facts carry placeholder demo values**
rather than an em dash: a founding year, a count of engagements, a count of offices or people.

Three conditions make that safe, and all three are mandatory:

1. **Marked in the markup.** Every filled figure carries `data-placeholder="true"`, so ingestion can
   find and clear all of them mechanically.
2. **Declared in the meta block.** `<meta name="placeholder-data" content="...">` names what is
   filled, so a study announces its own demo content without anyone reading the markup.
3. **Recorded in the study comment and the batch document**, with the values written out.

**The line this does not cross.** A demo value is only ever the firm's own countable fact, one it
would already know. These stay excluded whatever the reason, because a placeholder version of them
is a claim about somebody else or about a measurement that was never taken:

- named clients, client logos, testimonial attributions;
- awards, rankings, tier placements, certifications, scheme memberships;
- retention %, satisfaction %, NPS, ROI multiples, value-delivered figures;
- anything a regulator would treat as a representation.

### The firm's own people

A person is not a countable fact, so this needed deciding rather than assuming. The line:

**The firm's own team may carry placeholder names.** A design study for a firm that does not exist
needs something legible where a name goes, a leadership section reserved down to dashes is unusable,
and a placeholder surname marked `data-placeholder="true"` is clearable in one pass. Use an initial
and a surname — `A. Whitfield` — which reads as a placeholder rather than as a person.

**Third-party people may not.** A named client contact, a testimonial attribution, a quoted analyst,
a referee: all still forbidden, because a placeholder version of those is a claim about somebody
else. The difference is who the invention is about.

### Client quotes

The rule above forbids a testimonial attribution but never said what a testimonials section may
therefore contain. Read strictly it forbids the section outright; read loosely it permits a
placeholder job title, which is the same claim in smaller type. The line, drawn in `S09`:

**The quote sentence may be placeholder demo text.** Unattributed, it makes no representation about
any person or company — it is the section showing its composition, the way a placeholder count does.
Mark it `data-placeholder="true"` like any other, and declare it in the meta block.

**Nothing identifying may be attached to it.** Not a name, a role, a job title, a company, a sector,
an industry, a headshot or a logo — placeheld or otherwise. A placeholder job title is a smaller
version of the claim this rule already forbids, and *"Group CFO, a leading insurer"* invents a person
as surely as a full name does.

**What may be attached is the firm's own material:** the situation the quote came out of (the `S02`
vocabulary), the stage it was said at (the `S05` stages), and the firm's own disclosure policy — what
a reader is permitted to do to verify it. Those are the firm speaking about itself, which is the test
this whole section of the contract turns on.

**And the portrait stays reserved.** A name can be placeheld; a face cannot. Portrait areas remain
labelled empty areas, and their label describes the role rather than repeating the placeholder name —
so no study ever presents a fabricated individual as a real one.

**Media areas stay reserved.** A photograph cannot be placeheld with plausible fiction the way a
number can, and the media policy's purpose — no fabricated people, projects or places — is
untouched by this. The dashed portrait areas remain, and remain intended output.

## The Two Halves Of A Theme

| Fixed across every section at this variant | Free to differ in every section |
| --- | --- |
| Ground, ink and ink-soft values | Composition and grid |
| The accent, and what it is allowed to do | Media-to-text ratio |
| Font stack and type scale ratio | Asymmetry and alignment |
| Corner radius and border weight | Section rhythm and order |
| Slot treatment and reserved-field styling | Which device carries the hierarchy |

Variant N of every `CONS` section combines into website N. Variety comes from the right-hand column;
two studies at the same variant that share a layout fail this contract as surely as two that share
no palette.

## The Five CONS Themes

### 001 — Paper · Universal / Safe

| Token | Value |
| --- | --- |
| `--paper` / `--ink` / `--ink-soft` | `#f7f6f3` / `#14161a` / `#585d66` |
| `--line` | `#dedcd6` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#e8e6e0` / `#b7b4ac` / `#55585e` |
| `--accent` / `--accent-ink` | `#2f4fe0` electric indigo / `#ffffff` |
| Radius | `14px`, pills `999px` |
| Register | Daylight, legible, broadly reusable. The workhorse. |

### 002 — Sable · Premium / Editorial

| Token | Value |
| --- | --- |
| `--paper` / `--ink` / `--ink-soft` | `#f2efe9` / `#1a1714` / `#6b6459` |
| `--line` | `#dcd6ca` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#e6e1d7` / `#bcb3a4` / `#5f5950` |
| `--accent` / `--accent-ink` | `#9a5b2c` bronze / `#ffffff` |
| Radius | `4px` — sharper than 001; publication, not app |
| Register | Fewest elements, largest type, most air. Lowest density of the five. |

### 003 — Field · Structured / Visual Modular

| Token | Value |
| --- | --- |
| `--paper` / `--ink` / `--ink-soft` | `#eff1f4` / `#0e1216` / `#525c66` |
| `--line` | `#d7dde2` |
| `--card` | `#ffffff` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#e2e7eb` / `#adb7c0` / `#4c555e` |
| `--accent` / `--accent-ink` | `#12856a` deep emerald / `#ffffff` |
| Radius | `18px` |
| Register | Zoned and modular. Bays, cards, a visible system. The accent marks the live bay. |

### 004 — Signal · Conversion-led

| Token | Value |
| --- | --- |
| `--paper` / `--ink` / `--ink-soft` | `#ffffff` / `#0a0b0d` / `#54585e` |
| `--line` | `#e5e5e5` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#f0f0f0` / `#c3c3c3` / `#4e5157` |
| `--accent` / `--accent-ink` | `#e0402f` decisive red / `#ffffff` |
| Radius | pills `999px`, panels `12px` |
| Register | One action dominates, and the page says what that action actually is. |

### 005 — Midnight · Art-directed / Distinctive

| Token | Value |
| --- | --- |
| `--paper` / `--ink` / `--ink-soft` | `#0b0d12` / `#f2f3f5` / `#989ca6` |
| `--line` | `#272b33` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#14171e` / `#474d58` / `#c6cad1` |
| `--accent` / `--accent-ink` | `#7c6cf7` electric violet / `#0b0d12` |
| Radius | `26px` |
| Register | Dark ground, oversized line, the largest portrait field. The most photographic of the five. |

## Shared Across All Five

- Frame `max-width: 1320px`, padding `clamp(22px, 3.6vw, 58px)`.
- Font stack `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.
  `h1/h2` 800, `h3/h4` 750.
- Uppercase eyebrow, `0.8rem`, `letter-spacing: 0.085em`.
- Reserved media areas: dashed `--slot-edge`, `--slot` ground, uppercase `--slot-ink` label that
  states **what the photograph is**, never who is in it.
- Reserved value fields: an em dash with a visually hidden label naming the figure.
- Breakpoints at `860px` and `560px`; a `prefers-reduced-motion` block in every study.
- No global header, primary navigation or footer — the section-shell rule.

## Text Budget

| Role | Target visible words |
| --- | --- |
| Hero, CTA, breadcrumb | 40–90 |
| Standard content section | 90–170 |
| **Structured content section** | **170–230** |
| Detail page section (`S23`–`S27`) | 150–230 |
| Absolute ceiling, any study | **250** |

### The band measures prose, not completeness

The budget exists to stop essays, not to stop sections doing their job. A section whose role
genuinely carries **structured fields** — process stages with their outputs, engagement models with
what each includes, pricing tiers, FAQ — sits in the structured band and is authored **at full
capacity**: every field the role actually needs is present.

The test is not the word count. It is:

- Would a real firm's version of this section have this field? Then it belongs.
- Is any single element a paragraph of prose? Then it is over budget whatever the total says.

A structured section at 220 words made of short labelled fields is correct. A standard section at
150 words made of three paragraphs is not. **Cutting a required field to hit a number is the wrong
correction** — it produces a section that looks tidy and cannot be used.

# Detailing Pass — the reference register applied to CONS

Status: ACTIVE from 17 September 2026. This pass **supersedes the Composition Devices table, the
Shared-Across-All-Five rules and the five theme tables above for the design layer of every `CONS`
study.** The register, the four buyer questions, the anti-patterns, What May Not Be Invented, the
placeholder-demo-value rules, the page-rhythm shapes and the text budget all stand; the pills, the
14–26px radii, the dashed slot edges, the badge-over-media and the dark 005 ground go. The register
is `../../standards/08-VISUAL-REFERENCE-STYLE.md`, read after `WELL` (the light reading) and `CON`
(the heavy reading). `CONS` is the register's **editorial** reading: the sector has no honest
photograph but people, so it is carried by type — and this pass gives the type a hand.

## The CONS reading in one sentence

    A firm's own publication: a serif display voice with one italic word, a partner's pencil in
    the margin — circled words, underline strokes, margin notes, brackets — serif word-numerals
    at display scale, ghost glyphs behind the composition, hairlines and one accent, and the
    portrait as the only photograph.

## What CONS translates

| Register element | CONS reading |
| --- | --- |
| Display voice | The register's serif (Georgia stack), weight 400, `clamp(2.4rem, 4.6vw, 5.2rem)`, `line-height: 0.95`, `letter-spacing: -0.03em`, **one italic word** in the accent. Item titles in the sans at 700. No uppercase display — that is `CON`'s voice. |
| Statement | Serif italic at `clamp(1.3rem, 2.2vw, 2rem)` for the pull-sentence, the margin note and the client quote. |
| Eyebrows and labels | `0.6–0.7rem`, 700, tracking `0.16–0.2em`, uppercase, with a small stroke mark where it helps. |
| **Word-numerals** | Indices are serif italic words — *One, Two, Three* — in the accent at `2.4–4rem`, never a digit. The giant ghost index of register device 6 is the same word at `clamp(5rem, 12vw, 11rem)` in the line tone. |
| Rules | 1px hairlines for structure; **one 3px accent bar** per composition — the *pencil rule* — on the head, the live cell or the promoted row. Never two. |
| Paper | Paper, sable, field, white, chalk — see the theme table. Bands are the paper darkened 4–6%. **No dark ground, no dark panel**: theme 005 loses its midnight and keeps its violet. |
| Radius | `0–2px` on everything. Actions 0. No pills: category and discipline names are bordered chips at 2px, `0.6rem` tracked. |
| Media fields | Bare, flat, **people only**: 4:5 and 1:1 portraits, a 3:2 or 16:10 *at-work* field (a team in a room, by role), never a skyline, never a desk. Slate labels bottom-left: `PORTRAIT AREA · 4:5`, `AT WORK · 3:2`, `THE ROOM · 16:10`. Sections with no honest subject stay shape C and carry no field. |
| Reserved and placeholder figures | The firm's own counts keep their **placeholder demo values** from V1, marked `data-placeholder="true"`, drawn in the serif at counter scale (`2.2–3.4rem`) with the tracked label beneath — no box. Reserved values (a client, a title not yet written, a date) are bordered slots at 2px holding the word *Reserved*. Reserved prose is drawn as flat media-tone measures. |
| Actions | 1px bordered rectangle, radius 0, uppercase tracked, with a leading stroke mark where it helps; the second route an underlined link with `↗`. Hover inverts to ink. |
| **The pencil layer** | Behind or across a composition, one figure per study in the line tone or the accent, inline SVG, `aria-hidden`, `pointer-events: none`, `vector-effect: non-scaling-stroke`: `001` a **ghost glyph** — a serif question mark, ampersand or section sign at `clamp(12rem, 30vw, 28rem)` in the line tone behind the head; `002` a **pencil ellipse** circling the italic word (a slightly irregular closed path in the accent, 1.5px); `003` **ruled margin** — a left margin line and faint horizontal rules behind the grid, like a notebook page; `004` an **underline stroke** beneath the display's key phrase (a long wavering path in the accent, 3px) and a circled word-numeral on the live row; `005` a **bracket** — a tall curly brace or square bracket in the line tone grouping a column, with the ghost word-numeral. No study in a section repeats another's figure; nothing sits over body text; nothing above 12% visual weight. |
| **The margin note** | Once per study where V1 has a sentence that reads as an aside: a serif italic line in the accent, `0.95–1.05rem`, set in the outer margin with a 1px leader and a small pencil mark, `<aside>` in the markup. It carries V1 copy, never new copy. |
| **The marks** | A 24×24 stroke set at `stroke-width: 1.6`, `currentColor`, round joins, used small (1.1–1.5rem) beside labels and on actions: pencil, speech line, question mark in a circle, two people, one person, clock, calendar, document, folder, compass, balance, chair, door, telephone, envelope, pin, arrow-out, tick in a circle, struck circle (*not this*), bracket. No icon grid, no icon as ornament. |
| Density | Fuller than `WELL`, quieter than `CON`: a composition carries its head, one pencil figure, a chip row or ruled ledger, a portrait or a word-numeral column, and one action or foot line. Text budget unchanged. |

## CONS themes for the detailing pass

| Variant | Name | paper | ink | muted | line | media | band | accent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Paper & Indigo | `#f6f5f1` | `#15171b` | `#5b5f68` | `#dad8d1` | `#e6e4dd` | `#edebe5` | `#2f4fe0` |
| 002 | Sable & Bronze | `#f2efe8` | `#1b1713` | `#6a635a` | `#d9d2c6` | `#e5dfd4` | `#eae5db` | `#9a5b2c` |
| 003 | Field & Emerald | `#eff1f2` | `#0f1417` | `#535c63` | `#d3d9dc` | `#e0e5e7` | `#e6eaec` | `#12856a` |
| 004 | White & Signal | `#fcfcfb` | `#0b0c0e` | `#55595f` | `#e4e4e2` | `#eeeeec` | `#f3f3f0` | `#d63a2a` |
| 005 | Chalk & Violet | `#f3f2f7` | `#121219` | `#5c5b69` | `#d6d4e0` | `#e3e1ea` | `#e9e7ef` | `#6b4fd8` |

A second token, `--no` (`#8f1f14`, deep red; on 004 `#7a1a10` so it reads apart from the accent),
carries refusal only — *what we will not claim*, *not our client*, *what this page will not do* — as
an edge, a top rule or an icon stroke. Never a surface behind body text. No study introduces a
second accent.

## Sector rules that remain in force

The four questions, the anti-patterns (no 2×2 as ornament, no network, no arrows-up, no
handshake, no skyline), What May Not Be Invented, the placeholder rules (own counts, own people,
unattributed quotes — marked and declared), the shape A/B/C rule per variant, the text budget and
the section-shell rule are unchanged. The checker for this pass is `cslcheck.ps1`: it enforces the
theme tokens, the namespace, the flat register (no pill, dashed edge, shadow or gradient, radius
over 8px), inline-SVG-only graphics (`aria-hidden`, no `image`, `use` or `script` inside), the
shell rule, the claims vocabulary (retention, satisfaction, NPS, ROI, award, ranked, tier, trusted
by, %), the digit rule (no digit in visible copy outside a `data-placeholder` element), field
parity across the five studies, and the h1 rule.

## Completion record — 18 September 2026

The detailing pass is applied to all one hundred and thirty-five `CONS` studies, S01 through S27.
Every section carries a `BATCH-V2.md` design record beside its `BATCH-V1.md`; every study passes
`cslcheck.ps1` (tokens, namespace, flat register, inline-SVG-only, reduced-motion rule, shell rule,
h1 rule, digit and claims vocabulary, placeholder declaration, field parity) and was rendered and
read at 1440. The only parity gaps recorded are V1's own wordings, listed per section.

What the pass settled beyond the tables above, and what the next sector should inherit:

- **The pencil layer is assigned by variant, not by section**: `001` a ghost glyph or ghost
  word-numeral in the line tone behind the head (`@`, `¶`, `×`, `§`, `&`, `?`, `‡`, `∴`, `Two`),
  `002` the pencil ellipse round the one italic word, `003` the ruled margin drawn behind the
  whole composition, `004` the underline stroke under the phrase that carries the ask, `005` the
  bracket grouping the display column. Sections with no head (S22) put the ghost behind the row
  and the ellipse round the current page.
- **Word-numerals, never digits, outside a placeholder.** Every `01 / 02` index in V1 became
  *One … Six* in the serif italic accent (or STAGE ONE / STEP ONE chips in `004`, roman numerals
  on a stage strip); counts that are demo values stay digits inside `data-placeholder` elements
  and nowhere else. V1 copy that carried `stage 03` or `Case 01` was reworded to the same.
- **`--no` (deep red, `#8f1f14`; `#7a1a10` on 004)** carries refusal across the sector: the
  route that is you leaving (S18), the cost that can end in a no (S19), the three verdicts the firm
  agrees with (S20), the way out (S21), *what we got wrong* (S24), the retraction note (S25, S26),
  *what is not here* (S27). It is an edge, a chip border, a struck-seal stroke — never a surface
  behind body text, never a second accent.
- **Fields are bare and labelled by what they are**, never by who is in them: PORTRAIT AREA,
  AT WORK, THE ROOM, THE DESK, THE PROPOSAL, THE DOOR, MAP AREA · RESERVED SLOT. Ratios are
  stated in the label and chosen so a field never outruns its caption column (3:1 and 2:1 plates,
  4:5 portraits, 21:9 strips); a map area is a slot that names itself a slot.
- **The one ask is a statement or a bordered rectangle, never a form.** S18 carries no form by
  argument; S19 and S23 carry the hour as an underlined link or a bordered action with a clock
  mark; S20's ask is a statement with no link at all; S25's *tell us* is a band, not a box.
- **Detail pages S23–S27 keep V1's plain `data-region="page-context"` block with the one
  `<h1>`**, as the assembly stand-in for S21 and S22; the checker's hero list was extended to
  S23–S27 for that reason. Variant N of S21–S27 names the same person, service, engagement and
  office, so the six pages assemble into one site.
- **Two claims terms are allowed by exception and recorded**: `satisfaction` and ` roi ` in S08
  where V1 refuses them by name, and ` award` in S26 where V1 says none are listed.
