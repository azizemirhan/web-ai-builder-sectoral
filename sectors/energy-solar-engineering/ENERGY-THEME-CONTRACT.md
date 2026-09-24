# ENERGY THEME CONTRACT

Sector: Energy, Solar & Engineering. Prefix: ENG. Established with S01 on 2026-09-14.

## Design Intent

Modern, visually engaging web compositions with confident typography, generous
space and purposeful imagery. Follow the user's preference against technical and
classical styles. No blueprint grids, circuit diagrams, control panels, gauges,
industrial dashboards, faux engineering documents or classical corporate decoration.
Technical content can be factual and readable without becoming a technical visual metaphor.

## Five Fixed Themes

Variant N retains its theme across subsequent sections for coherent page assembly.

| Variant | Theme | Ground | Ink | Accent | Media ground | Soft text | Radius |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Sunlit | #fff9ed | #29271f | #906100 | #efdfb9 | #69604d | 28px |
| 002 | Terracotta | #f7f0ea | #382820 | #a34427 | #e3cabb | #756153 | 8px |
| 003 | Tidal | #edf6f3 | #163a33 | #126b58 | #c7ded4 | #506d65 | 24px |
| 004 | Daybreak | #f0f4ff | #1d2c4b | #345bc4 | #d7e0f3 | #566784 | 30px |
| 005 | Night Current | #17251e | #f0f3e5 | #d4ec79 | #33483a | #b6c7b9 | 32px |

001-004 accent controls use white text; 005 uses dark text on lime. Tidal permits
paper controls on a teal field; Daybreak permits pale #f0eaff controls with #25376a
text on a blue field. Focus colours must contrast with their actual surrounding field.
System sans, no remote fonts. Frame max-width 1400px with desktop 60px, tablet 36px
and phone 22px insets. Heading weight 500-650. Large type and deliberate curves
are composition devices, not a requirement to repeat the same layout.

## Facts and Media

Reserve imagery under the repository media policy. Use actual solar installations,
site contexts, equipment and consented engineering work with verified provenance.
Do not invent clients, project ownership, system capacities, yields, savings,
payback periods, financing, emissions reductions, accreditations or guarantees.
Specific services, qualifications and service areas need supplied evidence.
No fabricated environmental claims or unsupported performance comparisons.

Reserved media needs a visible subject caption, accessible label and allocated
space. Before publication supply licensing, provenance and final descriptive alt
text. Generic aspirational copy may frame exploration without promising outcomes.

## Structure and Interaction

Five directions: Universal / Safe; Premium / Editorial; Structured / Visual
Modular; Conversion-led; Art-directed / Distinctive. Differentiate composition,
not only palette or copy. Shapes: A item grid, B one to three anchored media areas,
C type and colour. Avoid more than two consecutive A sections. Read the previous
two same-variant sections when available.

Copy targets: hero 40-90 words, ordinary content 90-170, structured content 170-230,
detail roles 150-230; absolute ceiling 250. Required content takes precedence over padding.
Standalone HTML, scoped CSS, explicit border-box descendants, responsive reflow,
44px minimum targets, visible keyboard focus and reduced-motion treatment.
No raw scripts unless needed, frameworks, CDNs or remote runtime dependencies.
Use native interactions or existing destinations while later sections remain
unauthored; no dead hashes, pretend quote submission or fake site assessment.

# Detailing Pass — the modern register applied to ENG

Status: ACTIVE from 21 September 2026. Governs the V2 re-authoring of all one hundred and
thirty-five `ENG` studies. Source: `../../standards/08-VISUAL-REFERENCE-STYLE.md`, read through the
sector's own intent — *energy possibilities, solutions, project evidence and practical enquiry
context, never a technical visual metaphor* — and through the one word the pass was asked for:
**modern**. Everything above this line (the design intent, the five themes by name, the facts and
media rules, the structure and interaction rules) stays in force; the pass rewrites only the design
layer. The V1 content spine of every study is kept whole.

## The ENG reading in one sentence

**A modern energy identity: a confident sans display with one phrase in the accent, bare warm
fields of the array, the site and the roofline, hairline structure, soft 8px corners, word-numeral
chips for every index, and one thin plotted stroke drawn behind the composition — never a blueprint
grid, a circuit, a gauge, a dashboard tile, a bolt, a stat counter or a lime button.**

Where the reference register's voice is a serif magazine, ENG's is a contemporary energy company:
the serif is dropped, the sans carries the display at strong scale and close tracking, and the
sector's confidence is carried by generous space and one accent per composition rather than by the
24–32px rounded slabs and tinted panels of V1. Numbers are the sector's temptation — capacities,
yields, savings, payback — and the register refuses them: every figure is V1's bracketed placeholder
or absent, and the copy carries word-numerals only.

## What ENG translates

| Reference device | ENG reading |
| --- | --- |
| Serif display with one italic word | **Sans display**, weight 600, `clamp(2.6rem, 5vw, 5.4rem)`, line-height 0.96, tracking −0.04em, sentence case, **one phrase in the accent** (`.ac`), never italic |
| Statement line | Sans 400, `clamp(1.05rem, 1.5vw, 1.3rem)`, line-height 1.4, ink |
| Item title | Sans 600, 1.1–1.8rem, tracking −0.03em; placeholders in `--muted` |
| Eyebrow | 0.64rem, 700, 0.2em tracked, accent, with a 24px stroke mark (sun, layers, pin, document, calendar, people, building, speech, arrow) |
| Index numeral | **Word-numeral chip** — ONE … SIX as a bordered 4px chip, 0.56rem tracked — never a digit, never a giant numeral |
| Hairlines + one accent rule | `--line` soft, ink strong, one 3px accent bar per composition (the *lead rule*; vertical in `005`) |
| Tinted band | Paper darkened (`--band`), 8px radius, never a card stack, never a dark panel |
| Bare media field | Flat `--media`, 8px radius, slate label bottom-left: `THE ARRAY · 3:2`, `THE ROOFLINE · 3:1`, `THE SITE · 4:3`, `THE FIELD · 3:2`, `THE WORKSHOP · 4:3`, `THE EQUIPMENT · 1:1`, `THE ENGINEER · 4:5`, `THE OFFICE · 3:2`; never a person named, never a stock sunset |
| Bordered rectangle action | 1px ink border, **4px radius**, uppercase 0.68rem tracked, leading arrow mark; second action an underlined link with `→` |
| Pencil / geometry layer | **Plotted layer**, one thin stroke per variant, in the line tone or the accent at low weight — see below |
| `--no` deep red | **`--no` is graphite, `#4a5560`**: the token for what is not promised, not yet verified and not included — an edge, a chip border or a struck-circle stroke, never a surface |

## The plotted layer, by variant

| Variant | Device | Where |
| --- | --- | --- |
| `001` | **Arc** — one thin horizon arc, a wide shallow curve in the line tone, `clamp(16rem, 34vw, 30rem)` wide | behind the head, right, clipped by the shell — daylight, not a gauge |
| `002` | **Rise** — one thin accent diagonal rising left to right, 1.5px, in the corner above the headline beside the eyebrow, never across the type — a roof pitch | `.head > svg.rise`, absolute |
| `003` | **Dot grid** — small dots on a 40px grid in the line tone, an SVG `<pattern>` — a raster, not a blueprint | behind the whole composition, `.draw` |
| `004` | **Outline** — a 1.5px accent outline, 4px radius, drawn round the key phrase | `.u` + `svg`, inline-block |
| `005` | **Margin bar** — the 3px accent lead rule set vertical along the left of the display column | `.frame` with `border-left` |

One device per study; the device is drawn once. It sits behind text (`z-index: 0`) or on the edge
of a phrase, never across a field.

## ENG themes for the detailing pass

The five contract themes are kept by name and accent; the grounds are tuned to the register (warm
or cool off-white, never a tinted slot floating on paper) and **Night Current is inverted** — the
register forbids a dark panel as a page ground, so `005` keeps the dark green as ink on a pale
sage paper and the lime accent is darkened to moss to reach AA as text.

| Variant | Theme | `--paper` | `--ink` | `--muted` | `--line` | `--media` | `--band` | `--accent` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `001` | Sunlit | `#fff9ed` | `#29271f` | `#69604d` | `#e9dcbf` | `#f3e7c9` | `#f8efd8` | `#906100` |
| `002` | Terracotta | `#f7f0ea` | `#382820` | `#756153` | `#e3d2c6` | `#ecdccf` | `#f1e6dd` | `#a34427` |
| `003` | Tidal | `#edf6f3` | `#163a33` | `#506d65` | `#cfe0d8` | `#dcebe4` | `#e4f0ea` | `#126b58` |
| `004` | Daybreak | `#f0f4ff` | `#1d2c4b` | `#566784` | `#d5deee` | `#e0e7f5` | `#e8edf8` | `#345bc4` |
| `005` | Night Current, inverted | `#eef2ec` | `#17251e` | `#566459` | `#d0d9d0` | `#dfe6dd` | `#e6ece4` | `#587a06` moss (darkened from `#d4ec79` for AA) |

`--no: #4a5560` on every theme. `--line-strong` is the ink. The sans is the system stack; no
serif anywhere in ENG; no web font. Radius is 8px on fields and bands, 4px on chips and actions —
V1's 28–32px corners are retired.

## Sector rules that remain in force

The design-intent exclusions above, unchanged: no blueprint grid, circuit diagram, control panel,
gauge, industrial dashboard, faux engineering document or classical corporate decoration; the pass
adds no bolt, no sun-ray burst, no stat counter and no map embed. The facts rules: no invented
client, project ownership, capacity, yield, saving, payback period, financing, emissions
reduction, accreditation or guarantee; services, qualifications and service areas stay as V1's
bracketed evidence placeholders. Placeholder values stay marked `data-placeholder="true"` and
declared in a `placeholder-data` meta; **no digit appears in visible copy outside a placeholder
element** (word-numerals elsewhere). Portraits stay reserved and labelled by role. Pronouns are
never invented.

## The checker

`engcheck.ps1` — theme tokens per variant, the `.eng-sNN-vvv` namespace, `batch = V2-detailing`,
`data-study-id`, reduced-motion, no script / iframe / img / remote URL / form / header / nav /
footer (form and nav allowed only where the role carries them), balanced tags, inline SVG only with
`aria-hidden`, radius ≤ 8px, no gradient / shadow / dashed / pill, no solid border with max-width on
one rule, the energy claims vocabulary (guarantee, best, leading, number one, award, voted, stars,
rated, %, five-star, world-class, ranked, top-rated, certified by, accredited by, payback, savings
of, lowest price, cheapest), the digit rule, one `<h1>` on hero-like and detail pages only, and
field parity across the five studies.

## Completion record — 23 September 2026

The detailing pass is complete for all twenty-seven sections: one hundred and thirty-five ENG studies
re-authored in the register above. Every study carries `<meta name="batch" content="V2-detailing">`,
the namespace `.eng-sNN-vvv`, one of the five themes, its variant's plotted layer (arc, rise, dot
grid, outline, margin bar) and one 3px accent lead rule. Each section holds a `BATCH-V2.md` design
record beside its `BATCH-V1.md` authoring record, and each section README is marked
`RE-AUTHORED — V2 DETAILING PASS`.

Verified per section with `engcheck.ps1` (themes, namespace, batch token, structure, claims
vocabulary, digits, media parity, placeholder parity across the five studies): 27 of 27 sections
report ALL CHECKS PASS. Three sections carry a documented allowance: S13 and S23 for the V1
placeholder words *payback* and *guarantee*, which appear only inside bracketed placeholders as
things a verified summary must state or must not promise; S18 for V1's static enquiry form
(`-AllowForm`) and S22 for V1's two navigation landmarks (`-AllowNav`).

V1's content spine is kept whole throughout: no claim, figure, name, place, price, date or contact
detail is invented, every reserved image remains an empty labelled field, every V1 `<details>`
disclosure opens as a row (no script runs anywhere in the sector), and `<h1>` appears only on S01,
S21 and the detail pages S23–S27.
