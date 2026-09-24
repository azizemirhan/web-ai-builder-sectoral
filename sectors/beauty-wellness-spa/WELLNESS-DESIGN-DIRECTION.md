# Beauty, Wellness & Spa — Design Direction

Sector: Beauty, Wellness & Spa · Prefix: `WELL`

This document is the sector application of the global authoring system. It does not replace
`../../standards/01-AUTHORING-STANDARD.md`, `../../standards/03-MEDIA-POLICY.md` or
`../../standards/05-RESPONSIVE-QA.md`; where the global standard and this document could be read
as competing, the global standard governs and this document supplies the Beauty, Wellness & Spa
reading of it.

It applies to every `WELL` section, S01–S27, and is written before authoring begins so that the
sector is not corrected after the fact.

## Position

**Beauty, wellness and spa web design is primarily atmospheric.**

The subject of this sector is how a place and a treatment *feel* — calm, care, touch, light,
texture, ritual and time. A study earns its place by composing that atmosphere, not by listing
what is on offer. Copy supports the composition; it does not substitute for it.

The second half of the position matters as much as the first: **this sector is adjacent to
medicine and must not borrow its visual register.** A wellness site that looks like a clinical
system has not become more credible; it has lost the only thing the visitor came for.

## Sector Range

The sector spans day spas, hotel and destination spas, massage and therapy studios, hair and
beauty salons, nail and lash studios, skin clinics, and medical-aesthetic practices.

The catalog target is the **broad wellness and spa register**, not the medical-aesthetic end of
the range. Medical aesthetics is the part of this sector that pulls hardest toward clinical
charts, protocol tables and evidence grids, and it is the reason the anti-pattern list below is
longer than in most sectors. A study may be credible and calm at the same time; where the two
appear to conflict, calm is this sector's default and clinical is the exception that must be
justified in the batch document.

## Primary Visual Language

- treatment room and interior photography
- spa and studio architecture
- skin, hand and detail photography
- product, tool and material still life
- water, steam, stone, linen, wood, clay and botanical texture
- natural light and soft shadow
- practitioner portraiture
- calm colour fields — warm neutrals, sand, clay, muted green, off-white
- generous negative space
- soft edges and rounded forms
- unhurried, spacious pacing
- tactile materiality
- restrained editorial typography

## Reference Register

A `WELL` study should generally feel closer to:

- a contemporary spa or wellness brand site
- a premium skincare or body-care brand
- a boutique hotel or hospitality site
- an editorial beauty or wellbeing publication
- a considered, calm retail experience

than to:

- a medical clinic or hospital site
- a clinical treatment record
- a tariff sheet or price register
- a pharmacy or supplement catalogue
- an ingredient specification sheet
- a before/after evidence dossier
- salon booking-software admin UI

## Anti-patterns

The following must **not** be used as a default `WELL` styling device:

- clinical chart and patient-record aesthetics
- treatment protocol tables
- session, dosage or course schedules
- medical consent or intake form imitation
- before/after evidence grids presented as proof
- ingredient or INCI specification tables
- tariff sheets and price registers that occupy most of the layout
- certification, diploma and accreditation walls used as the main device
- percentage-claim panels and "clinical results" charts
- star-rating dashboards and review-score matrices
- pharmacy-style product specification cards
- booking-system administrative UI imitation
- device and machine specification blocks

These are not absolutely forbidden. Under *Technical and Professional Document Metaphors* in
`../../standards/01-AUTHORING-STANDARD.md` one may be used where the user or a supplied reference
explicitly asks for that visual concept, or where the role genuinely requires that artifact, and
where the result still works as a modern web interface. The justification is recorded in the
section's batch document.

What they must not do is define the general `WELL` visual identity. The failure this sector is
most likely to produce is a catalog whose most "distinctive" studies are the ones that look most
like a clinic's paperwork.

## Claims, Evidence and Regulation

Beauty and wellness claims are regulated in most markets, and this sector carries two section
roles built directly on top of that risk: `S05-results-before-after` and
`S24-project-case-study-detail`. The sector brief already limits S24 to anonymised programme
context. This section extends that reading to the whole sector.

No `WELL` study may contain:

- an efficacy claim, a percentage, a success rate or a duration-to-result figure
- the words *clinically proven*, *guaranteed*, *permanent*, *cure*, *heals*, *risk-free* or an
  equivalent, applied to a treatment
- a diagnosis, a named medical condition presented as treatable, or medical advice
- an invented practitioner name, qualification, licence, registration or professional body
- an invented client, testimonial attribution, review score or rating
- an invented price, package value, discount or membership term presented as real
- a fabricated before/after image, comparison or outcome

**Structure is authored; evidence is reserved.** A before/after role is composed as a comparison
*structure* — paired reserved media areas, a slider or a toggle — with neutral placeholder labels
and no outcome text. A pricing role is composed as a pricing *structure* with placeholder tokens
rather than invented figures. A testimonial role is composed as a quotation *structure* with
neutral placeholder text and no attributed name or score.

Where a supplied reference contains a real result claim, a real percentage, a real price or a
real client, take the composition and leave the claim. This is the same rule as reference-image
interpretation in the global standard, applied to the content layer rather than the chrome layer.

## Copy Direction

Visible `WELL` website copy should generally be:

- concise
- calm and unhurried
- sensory rather than technical
- warm without being effusive
- easy to scan
- paired with visual content

Avoid:

- clinical or pharmaceutical register
- ingredient essays and mechanism-of-action explanation
- promise and outcome language
- placeholder essays and long explanatory prose
- treatment descriptions written to prove content capacity
- stacked superlatives

This sector genuinely requires detailed content on treatment detail, article detail, practitioner
profile and location detail pages. Those pages manage detail through visual sections, media,
headings, concise modules, progressive disclosure, accordions where appropriate and clearly
separated blocks — not through uninterrupted copy.

## Media Direction

The media policy in `../../standards/03-MEDIA-POLICY.md` applies unchanged. Do not invent people,
clients, results, products, brands, prices, certifications or addresses. Reserved media areas are
valid, intended output and an empty one is not a defect.

`WELL` studies should reserve visual space, at the right scale and position, for:

- treatment room and interior photography
- spa, studio and reception space
- detail and texture imagery — skin, hands, water, stone, linen, botanical
- product and tool still life
- practitioner portraits
- paired comparison areas where the role is a before/after structure
- ambient or treatment video where appropriate

A `WELL` study must not become text-only solely because real media cannot be fabricated. This is
the sector where that failure is most damaging: a spa page with no imagery has not demonstrated
its role, it has removed it. Use quiet placeholders to represent future media.

Media density still applies. Prefer fewer, larger, better-proportioned areas over many small
thumbnails — a wall of treatment thumbnails reads as a catalogue, not as a spa.

## Section Shell — Beauty, Wellness & Spa

An individual `WELL` study must not include a site-wide header, primary global navigation, a
global footer or an unrelated announcement bar, unless that component is itself the target role.

- **S01 Hero: hero only.** No logo, no navigation, no header shell, no booking bar docked as
  site chrome.
- **Detail pages (S23–S27):** internal page content architecture is allowed; global website
  chrome is not.
- **Reference screenshots that contain a header must be read selectively.** Extract the requested
  role; do not reproduce the surrounding chrome because it happened to be in the frame. Spa and
  salon references very often carry a sticky "Book now" header — that bar is site chrome, not
  part of the section, unless the section being authored is the booking role.

## The Five Directions in Beauty, Wellness & Spa

Study IDs do not change with these names. `WELL-S01-003` remains `WELL-S01-003`.

| Variant | Direction | `WELL` reading |
| --- | --- | --- |
| 001 | Universal / Safe | The dependable, image-supported version of the role that any spa, salon or studio could ship. |
| 002 | Premium / Editorial | Skincare-brand and boutique-hospitality pacing: large calm media, refined typography, whitespace, fewer and more deliberate blocks. |
| 003 | Structured / Visual Modular | More content capacity carried by **visual structure** — grouped modules, panels, media pairings, disclosure — not by longer menus, more fields or a price table. |
| 004 | Conversion-led | The booking or enquiry route shapes the composition, while the section keeps its content role. |
| 005 | Art-directed / Distinctive | The strongest sensory, material and typographic composition the role can carry while staying usable — not a clinical document. |

The three traps this sector should expect:

- **003 must not become a price list or a treatment menu table.** Several roles here are
  inherently list-shaped — `S02 Treatments`, `S11 Pricing`, `S12 Memberships`, `S15 FAQ`. Their
  003 studies carry capacity through modules, grouping, imagery and progressive disclosure. If
  removing half the copy destroys the reason the study is different, it is not a successful 003.
- **004 must not turn every section into a booking widget.** Booking is this sector's native
  action, which makes the risk higher here than anywhere else in the catalog. The section's
  content role stays primary; the booking route is integrated into it, not substituted for it.
  Five sections whose 004 is the same embedded form is a failed set, not a converted one.
- **005 must not reach for the clinical register.** Every study 001–005 is already sector-aware.
  This sector feels like itself through light, texture, material, skin, water, calm colour,
  space and typographic restraint — not through charts, protocols, evidence grids or
  certification walls.

## Section Authoring Questions

Before authoring any `WELL` study, answer:

1. What is the primary **visual** element of this role?
2. What must a visitor understand immediately?
3. Does the composition feel calm and tactile rather than clinical?
4. Can media carry part of the meaning instead of additional prose?
5. Does 003 remain visually modular rather than becoming a menu or a tariff?
6. Does 004 keep the section's own role, or has it become a form?
7. Does 005 look distinctive without borrowing medical or administrative paperwork?
8. Is every claim, price, name, rating and result reserved rather than invented?
9. Would this composition still look like a modern website once real spa media is inserted?

Each section README records its own answers to questions 1 and 2 under *Authoring Questions*.

## Scope

This direction covers `WELL` sections S01–S27. No `S28` or higher exists in this sector and none
is planned; sector-native extensions are outside the planned catalog and would be governed only
after their taxonomy is decided.

## Detailing Pass — the reference register applied to WELL

Effective from the detailing pass (September 2026). Every `WELL` study is re-authored to the
register recorded in `../../standards/08-VISUAL-REFERENCE-STYLE.md`, which was derived from the
user-confirmed KEEP set of the Architecture sector. The **content** of each study — governing idea,
role, shared fields, claims and evidence limits — is retained; the **design layer** is rewritten.

### What WELL keeps from the register unchanged

Bare flat media fields with a corner slate label; serif display voice with one italic word;
structure by hairline rules and tinted bands, never by white cards or dark panels; one earth
accent used small; thin-bordered or underlined actions; low copy density; asymmetric editorial
grids; the ten rhythm devices.

### What WELL translates

| Register element | WELL reading |
| --- | --- |
| Paper temperature | Warmer and softer than architecture: linen, bone, mist, sand, ivory. |
| Corner radius | Large media fields may carry up to 6px; small tiles 3px; actions 2px. Never pills. |
| Serif role | Display **and** statement; the italic word is the sector's only ornament. |
| Media subjects | The treatment room; hands and skin in detail; stone, linen, water, steam, clay, botanicals as still life; product and tool still life; the practitioner at work, by role. |
| Slate labels | `ROOM`, `DETAIL`, `STILL LIFE`, `TEXTURE`, `PORTRAIT AREA`, `IMAGE AREA · 4:5`. |
| Accent | One per variant, from the WELL table below; on eyebrow, numeral, arrow, hover, italic word. |
| Bands | Tinted paper only; no dark bands, no saturated fields. |

### WELL themes for the detailing pass

| Variant | Name | paper | ink | muted | line | media | accent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Linen & Olive | `#f2f0ea` | `#23281f` | `#6a6d62` | `#d3d0c5` | `#e1dfd5` | `#5a6b48` |
| 002 | Bone & Clay | `#f6f1ea` | `#2a2420` | `#6f665e` | `#dbd1c5` | `#e7ded3` | `#a5583a` |
| 003 | Mist & Moss | `#eef0ee` | `#1f2624` | `#5f6764` | `#cdd2cf` | `#dcdfdb` | `#2f5c4b` |
| 004 | Sand & Ochre | `#f7f2e8` | `#2b251d` | `#6e655a` | `#dfd6c8` | `#e9e1d2` | `#9a6b2a` |
| 005 | Ivory & Plum | `#f8f4f3` | `#2b2226` | `#6d6266` | `#e0d6d9` | `#eae1e3` | `#6e3b4e` |

Media tone is the paper darkened; the slate label uses the muted colour. Focus outline uses the
accent. No study introduces a second accent.

### Sector rules that remain in force

The anti-pattern list, the claims and evidence limits, the section-shell rule and the reserved
`.slot` convention above are unchanged. Reserved fields stay empty and are drawn as media fields,
not as dashed boxes with sentences inside them.

### Detailing pass — completion record

All 135 `WELL` studies (S01–S27) were re-authored in this register on 16 September 2026. Each
section carries a `BATCH-V2.md` beside its `BATCH-V1.md`; V1 remains the authoring record
(content, claims limits, reserved fields), V2 the design record. Sector-wide rules the pass added
or clarified:

- **Device rotation across a section's five studies.** No two studies in a section share a
  register device, and the conversion study (`004`) alternates between the tinted band, the ruled
  column and the ruled sheet across sections so the direction does not become one shape.
- **Reserved facts are bordered slots on hairlines** — a 1px `--line` rectangle at 2px radius
  holding an em dash, with a visually hidden label — never a chip, never a dashed box.
- **Reserved text is drawn at prose cadence.** Where a title, standfirst, quotation or body cannot
  be written, it is a flat media-tone block sized to the lines it will hold (short / medium / long),
  so measure and rhythm can be judged before a word exists.
- **Portraits use the offset tab** (register device 10) and stay inside a `<figure>` whose
  `<figcaption>` holds the reserved name.
- **No gradients, no rotation, no type over a photograph.** Where V1 used a repeating gradient
  (S12-005), a tilt (S17-005) or a scrim (S16-005, S13), the pass found the same reading in flat
  marks, offset and overlap, or type crossing a field's edge.
- **Sections that require markup the shell rule otherwise forbids:** `S06` and `S19` carry native
  forms; `S22` and `S25-003` carry a named `<nav>`; `S21` carries the page's single `<h1>`. The
  checker (`wellcheck.ps1`) takes `-AllowForm` and `-AllowNav` for exactly those sections.
- **Height discipline at 1440:** core sections sit under ~1300px; detail pages (S23–S27) and the
  gallery route (S13-005) may run longer and are paced by chapters rather than compressed.
