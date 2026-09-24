# EDUCATION THEME CONTRACT

Sector: Education & Training. Prefix: EDU. Established with S01 on 2026-09-14.

## Design Intent

Use modern, visually engaging web compositions, following the user's direction.
Lead with curiosity and clear routes into learning. Different visitors may explore
an interest, return to study or consider a new subject; these are design scenarios,
not claims about a real institution's audience.

Avoid classical academic decoration and technical metaphors: crests, mortarboard
icons, blackboard equations, ruled notebooks, transcript tables, faux certificates
and administrative forms as default visual devices. No stock graduation celebration,
fake student quotes or fabricated employer/logo walls.

## Five Fixed Themes

Variant N retains its theme across subsequent sections so studies can form coherent pages.

| Variant | Theme | Ground | Ink | Accent | Media ground | Soft text | Base radius |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Apricot | #fff8ee | #24231f | #c44a21 | #f0dac0 | #625c52 | 24px |
| 002 | Mulberry | #f5eef2 | #30202d | #823b62 | #dfcbd5 | #675460 | 6px |
| 003 | Cobalt | #f0f3fa | #17253d | #2856c9 | #d8e0f0 | #536078 | 22px |
| 004 | Iris | #f7f4ff | #28213e | #6740bf | #e5dcf5 | #625a72 | 28px |
| 005 | Afterhours | #20241e | #f3f3e7 | #d3ed74 | #384337 | #bcc4b6 | 30px |

001-004 accent buttons use white text; 005 uses dark #20241e text on lime.
004 may use a pale #f0eaff control with #382059 text inside a purple field.
Supporting media colours may vary within the palette. Strong curves are deliberate
composition devices, not mandatory on every image in every section.

System sans stack, no remote font. Frame max-width 1400px; typical desktop inset
60px, tablet 36px, phone 22px. Heading weight 500-650, strong scale and close tracking.
Body measure should stay controlled. Minimum control target 44px; focus rings must
remain visible against their actual surroundings. Every study has scoped CSS,
explicit border-box descendants, responsive reflow and reduced-motion treatment.

## Truth and Media Rules

Follow the repository media policy. Reserve imagery with visible subject captions
and accessible labels. Appropriate subjects include actual teaching spaces, practical
studios, shared study settings and documented learning work with permission.
No invented student or instructor identity, qualification, accreditation, admission
requirement, price, timetable, ranking, success rate or employment outcome.
Real people and their work require suitable consent/provenance; portraits stay
reserved. Do not fabricate an institution to make the layout look complete.

Generic aspirational language is allowed without presenting outcomes as a promise.
Specific programmes, fees, funding, entry conditions, dates and staff information
must come from supplied facts or remain clearly reserved.

## Shape and Page Rhythm

Use A for item grids, B for one to three anchored media areas and C for type/colour.
Choose shape for the section's job; do not force media into every role.
Avoid more than two consecutive A sections and ensure some C breathing space in
an assembled page. Read the two preceding sections at the same variant when they
exist. Changing colour alone does not create a different composition.

Target visible copy: hero/CTA 40-90 words, ordinary content 90-170, structured content
170-230, detail roles 150-230; absolute ceiling 250. Targets guide clarity rather
than justify padding. Required fields and section responsibility take precedence.

## Interaction and Scope

Standalone HTML with no frameworks or remote dependencies. A study contains only
its own section role; no global header or footer unless that is the requested role.
Use real existing destinations or an honest native local interaction while later
sections are unauthored. Never create a dead hash link, invented enrolment action,
fake search result or fabricated application confirmation.


# Detailing Pass — the modern register applied to EDU

Status: ACTIVE from 21 September 2026. Governs the V2 re-authoring of all one hundred and
thirty-five `EDU` studies. Source: `../../standards/08-VISUAL-REFERENCE-STYLE.md`, read through
the sector's own intent — *lead with curiosity and clear routes into learning* — and through the
one word the pass was asked for: **modern**. Everything above this line (the design intent, the
five themes by name, the truth and media rules, the shape and rhythm rules, the interaction scope)
stays in force; the pass rewrites only the design layer. The V1 content spine of every study is
kept whole.

## The EDU reading in one sentence

**A modern learning identity: a confident sans display with one phrase in the accent, bare warm
fields of the studio, the shared table and the room, hairline structure, soft 8px corners,
word-numeral chips for every index, and one thin plotted stroke drawn behind the composition —
never a crest, a mortarboard, a ruled notebook, a stat tile or a lime button.**

Where the reference register's voice is a serif magazine, EDU's is a contemporary prospectus: the
serif is dropped, the sans carries the display at strong scale and close tracking as the contract
already asks, and the softness the sector's language needs is carried by an 8px radius on large
fields and bands — the register's ceiling — rather than by the 24–30px blobs and 999px pills of V1.

## What EDU translates

| Reference device | EDU reading |
| --- | --- |
| Serif display with one italic word | **Sans display**, weight 600, `clamp(2.6rem, 5vw, 5.4rem)`, line-height 0.96, tracking −0.04em, sentence case, **one word or phrase in the accent** (`.ac`), never italic, never bold-inside-bold |
| Statement line | Sans 400, `clamp(1.15rem, 1.8vw, 1.6rem)`, line-height 1.3, ink |
| Item title | Sans 600, 1.05–1.4rem, tracking −0.02em |
| Eyebrow | 0.64rem, 700, 0.2em tracked, accent, with a 24px stroke mark |
| Index numeral | **Word-numeral chip** — ONE … SIX as a bordered 4px chip, 0.56rem tracked — never a digit, never a giant numeral |
| Hairlines + one accent rule | Kept exactly: `--line` soft, ink strong, one 3px accent bar per composition (the *lead rule*; vertical in `005`) |
| Tinted band | Paper darkened (`--band`), 8px radius, never a card stack |
| Bare media field | Flat `--media`, 8px radius, slate label bottom-left: `THE STUDIO · 3:2`, `THE SHARED TABLE · 4:3`, `THE ROOM · 21:9`, `THE INSTRUCTOR · 4:5`, `THE WORK · 1:1`, `THE LIBRARY · 3:1`, `THE ENTRANCE · 3:2`; never a graduation, never a face named |
| Bordered rectangle action | 1px ink border, **4px radius**, uppercase 0.68rem tracked, leading mark; second action an underlined link with `→` |
| Pencil / geometry layer | **Plotted layer**, one thin stroke per variant, in the line tone or the accent at low weight — see below |
| `--no` deep red | **`--no` is graphite blue, `#3d4a5c`**: the token for what a course is not, who it is not for, what is not promised and what is still pending — an edge, a chip border or a struck-circle stroke, never a surface |

## The plotted layer, by variant

| Variant | Device | Where |
| --- | --- | --- |
| `001` | **Loop** — two overlapping thin rings, `clamp(12rem, 22vw, 20rem)`, in the line tone | behind the head, right, clipped by the shell |
| `002` | **Rise** — one thin accent diagonal rising left to right, 1.5px, in the corner above the headline beside the eyebrow, never across the type | `.head > svg.rise`, absolute |
| `003` | **Cross grid** — small plus marks on a 40px grid in the line tone, an SVG `<pattern>` | behind the whole composition, `.draw` |
| `004` | **Outline** — a 1.5px accent outline, 4px radius, drawn round the key phrase | `.u` + `svg`, inline-block |
| `005` | **Margin bar** — the 3px accent lead rule set vertical along the left of the display column | `.frame` with `border-left` |

One device per study; the device is drawn once. It sits behind text (`z-index: 0`) or on the edge
of a phrase, never across a field.

## EDU themes for the detailing pass

The five contract themes are kept by name and accent; the grounds are tuned to the register (warm
off-white, never a tinted slot floating on paper) and **Afterhours is inverted** — the register
forbids a dark panel as a page ground, so `005` keeps the lime family on a pale sage paper and the
accent is darkened to olive to reach AA as text.

| Variant | Theme | `--paper` | `--ink` | `--muted` | `--line` | `--media` | `--band` | `--accent` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `001` | Apricot | `#fbf6ee` | `#24231f` | `#625c52` | `#e3d9c9` | `#efe4d3` | `#f5ecdf` | `#c44a21` |
| `002` | Mulberry | `#f6f0f3` | `#30202d` | `#675460` | `#dccbd4` | `#e9dde4` | `#efe6eb` | `#823b62` |
| `003` | Cobalt | `#f1f3f9` | `#17253d` | `#536078` | `#d3dae8` | `#e1e6f1` | `#e9edf5` | `#2856c9` |
| `004` | Iris | `#f7f5fc` | `#28213e` | `#625a72` | `#dcd6ea` | `#e8e3f4` | `#efebf8` | `#6740bf` |
| `005` | Afterhours, inverted | `#f1f3ea` | `#20241e` | `#5d655a` | `#d3d8c6` | `#e2e6d6` | `#e9ecdf` | `#5b7413` olive (darkened from `#d3ed74` for AA) |

`--no: #3d4a5c` on every theme. `--line-strong` is the ink. The sans is the system stack; no
serif anywhere in EDU; no web font.

## Sector rules that remain in force

The design-intent exclusions above, unchanged: no crest, no mortarboard, no blackboard, no ruled
notebook, no transcript table, no faux certificate, no administrative form as a device, no stock
graduation, no fake student quote, no fabricated employer or logo wall. The truth rules: no invented
student or instructor identity, qualification, accreditation, admission requirement, price,
timetable, ranking, success rate or employment outcome. Placeholder demo values stay marked
`data-placeholder="true"` and declared in a `placeholder-data` meta; **no digit appears in visible
copy outside a placeholder element** (word-numerals elsewhere). Portraits stay reserved and are
labelled by role. Pronouns are never invented.

## The checker

`educheck.ps1` — theme tokens per variant, the `.edu-sNN-vvv` namespace, `batch = V2-detailing`,
`data-study-id`, reduced-motion, no script / iframe / img / remote URL / form / header / nav /
footer (form and nav allowed only where the role carries them), balanced tags, inline SVG only with
`aria-hidden`, radius ≤ 8px, no gradient / shadow / dashed / pill, no solid border with max-width on
one rule, the education claims vocabulary (guarantee, job-ready, best, leading, number one, award,
voted, stars, rated, %, five-star, world-class, ranked, top-rated, success / employment / pass /
placement rate, accredited by), the digit rule, one `<h1>` on hero-like and detail pages only, and
field parity across the five studies.

## Completion record — 21 September 2026

All twenty-seven sections — one hundred and thirty-five studies — carry the detailing pass. Every
study reads `batch = V2-detailing`, keeps its V1 content spine, placeholders, reserved fields,
routes and claims limits, and passes `educheck.ps1` with field parity across its five variants.
Each section holds a `BATCH-V2.md` design record beside its `BATCH-V1.md` authoring record, and
its README status reads RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION.

Decisions taken during the pass, recorded here so the next reader need not rediscover them:

- The `<h1>` belongs to S01, S21 and the detail pages S23–S27. V1 authored S21 and S23–S27 with
  an `<h2>`; the pass promotes those page titles to `<h1>` because each is the page the study
  owns. Every other section keeps `<h2>`.
- Claims tokens allowed only for V1's own refusals, kept verbatim: `award` in S15 (*Exact award…
  awarding body*), `guarantee` and `award` in S17 (*Eligibility does not guarantee an award*,
  *[Award period…]*), `guarantee` in S23 (*does not replace a formal assessment or guarantee an
  offer*). S22 is the only section with `<nav>` landmarks — V1's breadcrumb and local navigation.
- V1's `<details>` disclosures open as rows everywhere; V1's leads that say *Open each…* are kept
  as written.
- Record-shaped sections share one grammar: S11 accreditation → S14 resource → S16 tuition → S17
  funding → S19 admissions contact were derived from one another by substitution of the spine, so
  their five compositions correspond variant for variant. S10 projects and S12 campus spaces were
  derived from the S05 faculty compositions the same way; S13 events from S10 and S12.
- Shallow fields (3:1) are used where V1 called a panorama (S21-001/002, S24-002, S25-002,
  S27-001/002) so a full-width reserved image stays supporting rather than dominant.
- The refusal chip in the sector's `--no` graphite carries every *awaiting confirmation /
  verification* line; the amount in S16 is V1's bracketed `[Amount]` — no figure appears anywhere
  in visible copy.
