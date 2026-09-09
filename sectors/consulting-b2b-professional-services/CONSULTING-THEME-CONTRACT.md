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
