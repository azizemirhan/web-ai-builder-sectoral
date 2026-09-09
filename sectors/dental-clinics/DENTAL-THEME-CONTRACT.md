# DENTAL THEME CONTRACT

Sector: `Dental Clinics` · Prefix: `DN` · Written with `DN-S01` and governing all twenty-seven sections.

This file is the sector's register, anti-patterns, media rules, claims limits and five themes. Every
`DN` study is authored against it, and every batch document records where it applies it.

---

## The Sector's Design Problem

Consulting's problem is that judgement has no photograph. Dentistry's is the opposite: **there are
too many photographs, and they are all the same three.**

    A model with teeth that do not occur in nature, laughing.
    A gloved hand holding an instrument near an open mouth.
    An empty white surgery that could be any clinic on earth.

The first is not a patient. The second is a picture of the thing being feared. The third is a picture
of nothing. All three are on almost every dental website, and none of them is evidence of anything.

## The Governing Constraint — Nobody Is Browsing

> **Nobody arrives at a dentist's website in a good mood.**

This is the fact the whole sector designs around wrongly. Dental sites are built as if the visitor
were shopping — comparing, browsing, being tempted. They are not. They are **bracing.** The dominant
emotion is anxiety, and it has three named sources:

| The fear | What the sector does about it | What it should do |
| --- | --- | --- |
| **It will hurt** | Claims *pain-free* and *gentle*, which are unverifiable and in most jurisdictions regulated | Say what happens, and who can stop it |
| **It will cost more than they say** | Advertises *from £X* | Give the whole cost in writing before anything starts |
| **They will judge me for leaving it** | Says nothing at all | **Say it** |

The third is the one nobody addresses and the one that keeps people away for years. A design that
answers it is doing something no competitor is doing, and it costs nothing to be honest about.

---

## Anti-Patterns

Specifically banned as default devices across all twenty-seven sections:

- **The stock smile model.** A person who is not a patient, with teeth that are not real, is the
  single most common image in the sector and it is evidence of nothing.
- **The open mouth.** No study reserves an image of a mouth, teeth in close-up, or a dental chart of
  a jaw. It is the fear image and it belongs in a clinical record, not on a homepage.
- **Instruments near a face.** A drill, a probe or a syringe in frame with a person is the same
  failure with better lighting.
- **The empty white surgery.** A room with nobody in it, shot wide, is a picture of a room that could
  be anywhere.
- **Tooth iconography.** A cartoon molar as a bullet, a logo, or a decorative motif.
- **Aqua and whitening-blue palettes.** The cyan-to-white gradient is the sector's visual default and
  reads as a product claim about tooth colour.
- **Sparkle, shine and gleam effects.** Star glints on teeth, radial gradients behind a smile.
- **Countdown offers on treatment.** Scarcity applied to healthcare.
- **Award badges and star ratings** as a design element.
- **Before/after used as an outcome promise.** See *Claims Limits*.

## The Media Rule

**Ask what the photograph is of.** In this sector three subjects are honest and the rest are not:

| Honest | Why |
| --- | --- |
| **The room the visitor will actually sit in** | It is the room, and they are about to be in it |
| **The people who will actually treat them** | Named by role, mid-work or mid-sentence, never posed against a window |
| **The equipment the text names** | If the copy says a scanner replaces the mould, the scanner is a legitimate subject |

Everything else is a grey rectangle standing in for a photograph. A reserved area's label states
**what the photograph is** and never who is in it, and no label ever describes a mouth.

**Portraits stay reserved.** A name can be placeheld; a face cannot.

---

## Claims Limits

Dental advertising is regulated in most jurisdictions, and the workspace takes a conservative line
rather than a jurisdiction-specific one. These are authoring rules for placeholder studies, not legal
advice; a real clinic's copy must be checked against its own regulator.

**Never written, in any study:**

- **Outcome guarantees.** No *guaranteed results*, *permanent*, *lasts a lifetime*.
- **Comfort claims.** No *pain-free*, *painless*, *completely gentle*. What may be said is what is
  done: an anaesthetic is offered, a signal stops the work, a break is available.
- **Superiority claims.** No *best*, *leading*, *number one*, *award-winning*, *voted*.
- **Fabricated credentials.** Registration numbers, specialist titles, qualifications and memberships
  are verifiable facts about real people. **They are reserved, never invented** — the same rule the
  workspace applies to people everywhere.
- **Fabricated prices.** A price stated must be complete. A study that cannot state a complete price
  states the **policy** instead — *the whole cost in writing before anything starts* — which is a
  commitment rather than a figure.
- **Patient testimonials, ratings or reviews with attribution.** No named patients, no star counts.
- **Before/after images as outcome promises.** `S05` and `S24` are scoped to anonymised treatment
  context. A reserved before/after area, where a study uses one, is labelled as **one case, not a
  typical result**, and never carries a face.

**Permitted placeholder data:** the clinic's own countable and checkable facts — how many surgeries,
how many years open, opening days, whether emergency slots are held back, whether anyone works on
commission. Marked `data-placeholder="true"`.

**The clinic's own people** may carry placeholder names in the form initial-and-surname
(`J. Okafor`). Third-party people — patients, referrers, named specialists elsewhere — may not.
Pronouns are never invented: a placeholder person is *they*.

---

## Composition Devices

The anti-pattern list is the negative half. This is the positive half, and it governs every section.

**Banned as default devices:**

- a hairline rule under every item in a list;
- a right-aligned metadata or label column;
- a numeral gutter used as a table column rather than as a graphic element;
- **text-only boxes presented as cards.** A card without media is a table cell with rounded corners.

**Build with these:**

| Device | What it looks like |
| --- | --- |
| **Card grid** | Three or four up, each card carrying its own image area above a short label and a title |
| **Featured card + compacts** | One item given double width and a large image, the rest compact around it |
| **Horizontal snap rail** | Tall image cards, the next peeking past the frame edge |
| **Offset / staggered gallery** | Two columns of image cards, one dropped so pairs never align |
| **Numbered card set** | 01–06 as graphic numerals, one card held in the accent |
| **Badge over media** | A pill sitting on an image area, marking one item |
| **Pill labels** | Category names as pills, never as tracked uppercase in a side column |
| **Big-numeral stat row** | Figures at display size with a small label beside them, no boxes |
| **Joined modules** | A row sharing one `2px` seam so several parts read as one object |

### The test before a section is finished

1. **Where is the media?** Count the reserved areas, and check each against the media rule above.
2. **Would this survive as a table?** If it could be rewritten as rows and columns without losing
   anything, it *is* a table and must be rebuilt.
3. **Is the hierarchy in the scale, or in the rules?** Separate items by size, ground and space.
4. **Has this skeleton been used at this variant already?** Run
   `node review/check-composition-collisions.js dental-clinics`.

---

## Page Rhythm — The Rule Above The Section

**Variant N of every section stacks into one page**, so a rule that makes each section good can still
make the page bad.

| Shape | What it is | Media |
| --- | --- | --- |
| **A — Item grid** | Cards, tiles or panels, media in every item | 5–8 areas |
| **B — Anchored** | One or two large images anchoring text-led content | 1–3 areas |
| **C — Type and colour** | No reserved media. Scale, colour fields, pills and space | 0 areas |

**Shape B is the default.** A page made only of A is a catalogue; a page made only of C is a document.

1. **Never more than two consecutive sections in shape A** at the same variant.
2. **Every assembled page must contain at least one shape C.**
3. **A section is not entitled to media just because it could have some.**
4. A section authored as C records why in its batch document.
5. When a section is authored, **read the two sections above it at the same variant first.**

---

## Text Budget

| Role | Target visible words |
| --- | --- |
| Hero, CTA, breadcrumb | 40–90 |
| Standard content section | 90–170 |
| **Structured content section** | **170–230** |
| Detail page section (`S23`–`S27`) | 150–230 |
| Absolute ceiling, any study | **250** |

The band measures prose, not completeness. A structured section carrying real fields is authored at
full capacity; **cutting a required field to hit a number is the wrong correction.** A single element
that is a paragraph of prose is over budget whatever the total says.

---

## The Five Themes

Variant = theme, fixed for all twenty-seven sections. The palette deliberately avoids the sector's
aqua-and-white default; no theme uses cyan, and no theme uses red as its accent, because red in a
dental context reads as blood and emergency.

| Variant | Theme | Ground | Ink | Accent | Radius |
| --- | --- | --- | --- | --- | ---: |
| `001` | **Chalk** | `#f6f4f1` | `#16181b` | `#1f6f5c` forest | `16px` |
| `002` | **Linen** | `#f3efe8` | `#1b1714` | `#a2543a` terracotta | `2px` |
| `003` | **Slate** | `#eef0f2` | `#0f1316` | `#2c5fd0` ultramarine | `20px` |
| `004` | **Daylight** | `#ffffff` | `#0a0b0d` | `#e08b2c` amber | `24px`, pills |
| `005` | **Dusk** | `#14161a` | `#f2f1ef` | `#6ea8a0` sea green | `26px` |

Supporting tokens per theme are set in each study and must not drift: `--ink-soft` for secondary text
at AA or better, `--line` for hairlines, `--card` for raised grounds, and `--slot` / `--slot-edge` /
`--slot-ink` for reserved media areas.

### Fixed across all themes

- Frame `max-width: 1320px`; breakpoints at `1100`, `980`, `860` and `560px`.
- A `prefers-reduced-motion` block in every study.
- Scoped CSS namespaced to `.dn-sNN-VVV`. No framework, CDN or remote runtime dependency of any kind.
- No global header, primary navigation or footer — the section-shell rule.
- Secondary text must reach **AA**. A colour that is deliberately quiet is still content.

---

## What Moving Toward Looks Like

Large confident type, generous negative space, warm grounds rather than clinical white, real
photography of rooms and people, one decisive accent, and **a stated commitment rather than a
described feeling.** *Gentle, caring dentistry* is what a clinic says when it has nothing to state.
