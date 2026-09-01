# Architecture & Interior Design — Rework Manifest

## Phase

Phase 0 — Audit Baseline. Inventory, classification and diagnosis only. No design work.

## Audit Date

2026-09-01

## Scope

Sector: **Architecture & Interior Design** (prefix `ARC`).

Every authored `ARC` study on disk was audited, not the planned catalog on paper. The audit covers
28 section directories: the 20 sector-core sections `S01`–`S20`, the seven universal extended
sections `S21`–`S27`, and one unplanned directory `S28-blog-list-pages` that exists in the working
tree. 146 study files were read and measured.

Each study was assessed on evidence rather than recollection:

- visible word count (tags, comments, CSS and script stripped);
- number of reserved media areas;
- presence of a global site header or primary navigation;
- visible technical-document labels (`SHEET`, `REVISION`, `ISSUED FOR`, `DOSSIER`, `REGISTER`,
  `LEDGER`, `ATLAS`, `ANNEX`, `CLAUSE`, `FOLIO`, `PROGRAMME`, `SCHEDULE`, `SPECIFICATION`,
  `CURRICULUM`, `DRAWING SET`, `KEY PLAN`, `NTS`);
- table and definition-list density;
- declared territory and layout model from each study's own `<meta>` block.

Text-density bands used throughout: **LOW** under 100 visible words, **MEDIUM** 100–199,
**HIGH** 200–349, **EXCESSIVE** 350 or more.

## User Direction

The following review feedback is authoritative and is recorded as given. It is not reinterpreted
in this document.

### Global

1. Technical-document visual styles are no longer the dominant Architecture direction.
2. Highly text-heavy compositions must be reduced.
3. Architecture designs should become more visual and aesthetically driven.
4. Designs should prioritise media, typography, layout, whitespace, visual rhythm and spatial hierarchy.
5. Where a section study contains a global website header or navigation, it should later be removed
   unless navigation is that section's own role.
6. Hero studies must contain the hero only; global headers must later be removed from them.
7. Empty image, video and portrait areas are intentional reserved media areas and are **not** bugs.

Styles being moved away from as a default: drawing sheets, issue sets, dossiers, registers, ledgers,
technical matrices, CV sheets, programme sheets, schedules, specification-like layouts, revision
blocks, scale/NTS notation used as decorative language, architectural documentation metaphors and
highly text-heavy technical compositions.

Direction to move toward: strong architectural, interior and material imagery; large visual fields;
editorial composition; typography; whitespace; spatial hierarchy; asymmetry where appropriate;
image/text relationships; premium visual presentation; contemporary web design.

### Per-section notes as supplied

| Section | Studies named | Issue as stated |
| --- | --- | --- |
| S01 Hero | all | Remove global headers/navigation; hero only |
| S02 Selected Projects | — | No design changes requested |
| S06 Design Process | S06-003, S06-005 | Too technical, too text-heavy |
| S08 Architects & Designers | S08-003 | Too technical, too text-heavy |
| S08 Architects & Designers | S08-007 | Broken on desktop, tablet and mobile |
| S09 Awards & Publications | S09-001, S09-003, S09-005 | Too technical / too text-heavy |
| S10 Capabilities | S10-005 | Too technical, too text-heavy |
| S11 Materials & Sustainability | S11-003, S11-005 | Too technical, too text-heavy |
| S12 Client Testimonials | S12-005 | Too technical, too text-heavy |
| S13 Featured Project Case Study | S13-003 | Too technical, too text-heavy |
| S14 Project Gallery | S14-003 | Too technical; gallery must be 3x3 = 9 images |
| S15 Sectors & Markets | S15-003, S15-005 | Too technical, too text-heavy |
| S16 Press & News | S16-003 | Too technical, too text-heavy |
| S17 Studio Locations | S17-003, S17-005 | Too technical, too text-heavy |
| S18 Studio Stats | S18-002, S18-003, S18-005 | Too technical / too text-heavy |
| S19 Project Inquiry | S19-005 | Too technical; working-sheet style not desired |
| S20 Consultation CTA | S20-005 | Too technical; agenda-document style not desired |
| S21 Subpage Hero | all | Role misunderstood; conventional website internal-page heroes wanted |
| S22 Breadcrumb / Context Navigation | all | Role misunderstood; conventional breadcrumbs only |
| S23 Service Detail | all | Too much text, too technical, insufficient visual storytelling |
| S24 Project Detail | S24-003, S24-005 | Too technical, too document-oriented |

The clarified S23 content balance supplied by the user, recorded as guidance rather than as a
mandatory template: subpage hero → short service introduction → major image/video area →
3–4 concise service aspects → image + text content → simple process → relevant project example →
concise FAQ → CTA.

The clarified S21 role: simple internal page title banner, image-background subpage hero,
no-image typography hero, split text/image hero, contained image hero or elegant compact banner —
with or without a background image area, and never a dossier cover, metadata register, drawing
sheet, document folio or specification header.

The clarified S22 role: conventional website breadcrumbs (`Home / Projects / Residential /
Project Name`). The five variants may differ visually but must remain breadcrumb navigation, and
must not broaden into project navigation systems, key plans, drawing-set locators, page-contents
systems, sibling indexes or technical navigation maps.

## Classification Definitions

| Status | Meaning |
| --- | --- |
| `KEEP` | Structural and visual direction is suitable; no meaningful redesign required. |
| `MINOR_FIX` | Core design is suitable; later correction is small — header removal, copy trim, spacing, minor responsive or semantic cleanup. |
| `REWORK` | The core idea survives but the composition needs substantial visual revision. |
| `REBUILD` | The design interpretation is fundamentally wrong for the section role and should be replaced with a different direction. |
| `BUG_FIX` | Concept acceptable; implementation or responsive behaviour is broken. |
| `NOT_AUTHORED` | A planned study that does not exist on disk. |

Secondary flag `ADDITIONAL_REVIEW_CANDIDATE` marks a study the **user did not name** but which
appears to conflict with the new direction. For those studies the recorded status is this audit's
recommendation only. **The user decides whether they are actually reworked.** A flagged study is
not the same as a user decision and must not be treated as one in Phase 1.

## Global Findings

| Measure | Count |
| --- | --- |
| Planned ARC studies (S01–S27 × 5) | 135 |
| Authored studies audited | 146 |
| — planned IDs authored | 135 |
| — extension variants (S03-006/007, S08-006–009) | 6 |
| — unplanned S28 studies | 5 |
| KEEP | 73 |
| MINOR_FIX | 18 |
| REWORK | 27 |
| REBUILD | 28 |
| BUG_FIX | 0 |
| NOT_AUTHORED | 0 |
| ADDITIONAL_REVIEW_CANDIDATE (flag) | 25 |
| Studies addressed by the user | 50 |
| — of those, an explicit *no change* decision (S02) | 5 |
| — sections addressed as a whole (S01, S02, S21, S22, S23) | 25 |
| — studies named individually | 25 |
| Global header / navigation contamination | 15 |
| HEAVY technical-document metaphor | 34 |
| HIGH or EXCESSIVE text density | 49 |
| Confirmed responsive/implementation failure | 1 |
| Studies carrying intentional reserved media areas | 104 |
| Studies with no media area at all | 42 |

### A. Is the current Architecture catalog structurally diverse?

Structurally, yes. The five-territory model produced genuinely different geometries in most
sections, and several sections (S02, S03, S07, S08, S13, S14, S24) offer five clearly distinct
compositions. Diversity fails in a different dimension: **visual register**. A large part of the
catalog reaches for the same visual answer — a ruled document — whenever a section needs to feel
architectural.

### B. Is the repeated technical-document metaphor reducing visual diversity?

Yes. 34 of 146 studies use a heavy document metaphor, and they cluster in the
sector-native slot of almost every section. The result is that the most 'distinctive' study in
many sections is the least visual one, and the sector-native territory has effectively collapsed
into a single register with different labels: sheet, register, ledger, annex, dossier, atlas,
programme, curriculum, key plan.

### C. Are the problems concentrated in the 003 and 005 variants?

Overwhelmingly. Five sections were addressed as a whole (S01, S02, S21, S22, S23). Of the
25 studies the user named **individually**, the variant distribution is:

- variant `001`: 1 study
- variant `002`: 1 study
- variant `003`: 11 studies
- variant `005`: 11 studies
- variant `007`: 1 study

That is 22 of 25 in the 003 and 005 slots alone.

The 003 (Dense / Information-heavy) and 005 (Sector-native / Distinctive) territories are where
the failure pattern lives. 003 was read as *more fields and more prose*; 005 was read as *make it
look like a professional document*. Both readings are defensible against the current wording of
`standards/01-AUTHORING-STANDARD.md`, which defines the territories by information density and
sector nativity without a visual ceiling — which is why this is a standards question in Phase 1,
not only a per-study correction.

### D. Which sections need conceptual clarification rather than individual fixes?

- **S21 Subpage Hero** — the role itself was misunderstood; four of five studies need replacing.
- **S22 Breadcrumb / Context Navigation** — the role was broadened beyond breadcrumbs; only 001
  (and arguably 002) survive as authored.
- **S23 Service Detail** — the content balance is wrong across all five studies, not the geometry.
- **S09 Awards & Publications**, **S18 Studio Stats** — sections where the majority of studies
  carry no media at all and present the content as records.
- **S28** — a governance question before a design question; see Global Structural Issues.

### E. Which designs should act as positive references?

See **Positive Reference Studies** below. In short: S02 as a whole, S03-002, S04-001, S05-002,
S06-002, S07-001/002, S08-006, S09-002, S10-004, S11-002, S13-002, S15-002, S16-002, S19-002,
S24-001, S25-005, S26-002 and S27-002.

## Section Summary

### S01 — Hero

Studies authored: **5**  ·  KEEP: 0  ·  MINOR_FIX: 4  ·  REWORK: 1  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Composition and media use are strong across the set; every study is image-led and low on copy.
- **Primary weakness:** All five carry a global site header and navigation that does not belong in a hero section study; 005 additionally uses a drawing-sheet title block.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Five headers with no site chrome, one of which replaces the sheet metaphor with an image-led or typographic treatment.

### S02 — Selected Projects

Studies authored: **5**  ·  KEEP: 5  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Genuinely varied, image-led project presentation with the lowest copy in the sector.
- **Primary weakness:** None identified; the user has ruled out changes here.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Unchanged.

### S03 — Services

Studies authored: **7**  ·  KEEP: 5  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** Every study pairs a service with its own media area; two extension variants add bento and paired-row rhythms.
- **Primary weakness:** 003 ends each card in a specification-style field list and 005 wraps the stages in a drawing sheet.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Same media-led card and row models, with the sheet and field-list apparatus removed.

### S04 — Project Typologies

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 2  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Typologies are presented typographically and with real media in four of five studies.
- **Primary weakness:** 005 turns the section into a plate catalogue; 003 uses scope field pairs.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Typographic and image-led typology presentation; the tabbed switching kept but re-skinned.

### S05 — Design Philosophy

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** Two genuinely distinctive typographic studies (002, 004) and a calm two-statement opener.
- **Primary weakness:** 005 is a clause-and-revision contract document; 003 is text-dominant with a single media area.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Editorial principles with large imagery and fewer, shorter positions.

### S06 — Design Process

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** 002 shows exactly the desired direction: numerals, serif headings and one image per stage.
- **Primary weakness:** 005 is a programme matrix with no media at all and 003 turns each stage into a field table.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** A visual, web-native process sequence; the programme matrix retired.

### S07 — Studio About

Studies authored: **5**  ·  KEEP: 4  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** The most consistently image-led and low-copy section in the sector.
- **Primary weakness:** 005 frames the studio as a print colophon.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Largely unchanged, with the colophon labelling removed.

### S08 — Architects & Designers

Studies authored: **9**  ·  KEEP: 6  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** Portrait media is present in every study and the set covers six different roster geometries.
- **Primary weakness:** 003 reads as a personnel list, 005 as a register, and 007 does not render usably at any width.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Portrait-led roster patterns; the sliver filmstrip replaced and the register retired.

### S09 — Awards & Publications

Studies authored: **5**  ·  KEEP: 2  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** 002 proves the section can be visual — a tear sheet beside a short record list.
- **Primary weakness:** Three of five studies carry no media at all and present recognition as lists, tables or citations.
- **Section diversity:** WEAK
- **Visual direction after corrections:** Covers, tear sheets, project imagery and short recognition lines instead of bibliography.

### S10 — Capabilities

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** 004's three entry routes are the best conversion logic in the sector.
- **Primary weakness:** No study in the section carries a single media area, and 005 is an appointment annex.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Capability presentation with imagery and fewer inventory lines.

### S11 — Materials & Sustainability

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** 001 and 002 already use sample areas as the primary visual material.
- **Primary weakness:** 003 and 005 — the two the user flagged — contain no material imagery at all.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Material samples, textures and short sustainability principles.

### S12 — Client Testimonials

Studies authored: **5**  ·  KEEP: 4  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** Four of five studies are usable testimonial presentations with clear attribution discipline.
- **Primary weakness:** 005 reproduces a prequalification annex; text density is high across the section by nature.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Editorial testimonial presentation; the annex replaced.

### S13 — Featured Project Case Study

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 2  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Plates and narrative are paired in every study; 005 carries a strong existing/proposed comparison.
- **Primary weakness:** 003 is framed as a dossier with a credits grid; 005 wraps its comparison in sheet apparatus.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Portfolio-driven case studies keeping the decision sequence and the before/after pairing.

### S14 — Project Gallery

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 2  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Four of five studies are genuinely image-led with varied ratios.
- **Primary weakness:** 003 shows eighteen frames with a numbered legend; 005 uses sheet framing.
- **Section diversity:** STRONG
- **Visual direction after corrections:** A controlled gallery capped at 3x3, keeping the scale ordering idea.

### S15 — Sectors & Markets

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** 001 and 002 are image-led and low-copy.
- **Primary weakness:** 003 and 005 are matrices with no media; the section has the least media overall.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Market presentation carried by imagery rather than by capability matrices.

### S16 — Press & News

Studies authored: **5**  ·  KEEP: 4  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** 002 and 005 give the section two distinct editorial identities.
- **Primary weakness:** 003 is a tabular archive index with no media.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Visual archive and press-room presentation.

### S17 — Studio Locations

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** Location imagery is present in 001, 002 and 004.
- **Primary weakness:** 003 is a directory table and 005 a coordinate atlas, neither carrying media.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Location cards and studio imagery with short access lines.

### S18 — Studio Stats

Studies authored: **5**  ·  KEEP: 2  ·  MINOR_FIX: 0  ·  REWORK: 1  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** 001 already demonstrates the large-figure treatment the user described.
- **Primary weakness:** Three of five studies were flagged; the section carries almost no media anywhere.
- **Section diversity:** WEAK
- **Visual direction after corrections:** Large figures, short supporting copy and supporting imagery.

### S19 — Project Inquiry

Studies authored: **5**  ·  KEEP: 4  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** Four of five studies are clean, low-friction inquiry forms with real labels.
- **Primary weakness:** 005 is a working project sheet; the section carries no media by role.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Contemporary inquiry forms; the sheet metaphor retired.

### S20 — Consultation CTA

Studies authored: **5**  ·  KEEP: 4  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** Compact, low-friction consultation invitations.
- **Primary weakness:** 005 is an agenda document.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Elegant consultation invitations.

### S21 — Subpage Hero

Studies authored: **5**  ·  KEEP: 0  ·  MINOR_FIX: 0  ·  REWORK: 3  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** Two studies (002, 004) are close to a conventional subpage hero.
- **Primary weakness:** The section as authored interpreted the role as a document header rather than a website internal-page hero.
- **Section diversity:** WEAK
- **Visual direction after corrections:** Five conventional internal-page heroes: image-background, typographic, split, contained and compact banner.

### S22 — Breadcrumb / Context Navigation

Studies authored: **5**  ·  KEEP: 1  ·  MINOR_FIX: 1  ·  REWORK: 0  ·  REBUILD: 3  ·  BUG_FIX: 0

- **Primary strength:** 001 is exactly the conventional breadcrumb the user described and is fully accessible.
- **Primary weakness:** Three of five studies broaden breadcrumbs into sibling navigation, project paging or a drawing-set locator.
- **Section diversity:** WEAK
- **Visual direction after corrections:** Five breadcrumb variants that stay breadcrumbs.

### S23 — Architecture / Interior Service Detail

Studies authored: **5**  ·  KEEP: 0  ·  MINOR_FIX: 0  ·  REWORK: 3  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** The section covers the full service contract and the responsive rail behaviour is correct.
- **Primary weakness:** Every study is text-first: 485-819 visible words with little or no media; two are outright documents.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** The clarified service flow: hero, short intro, major media, 3-4 aspects, image+text, simple process, example, short FAQ, CTA.

### S24 — Project Detail

Studies authored: **5**  ·  KEEP: 3  ·  MINOR_FIX: 0  ·  REWORK: 0  ·  REBUILD: 2  ·  BUG_FIX: 0

- **Primary strength:** 001, 002 and 004 are portfolio-shaped with strong media presence.
- **Primary weakness:** 003 and 005 reproduce a dossier and a drawing issue set.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Portfolio-driven project pages with large imagery and concise metadata.

### S25 — Studio Journal / Article Detail

Studies authored: **5**  ·  KEEP: 0  ·  MINOR_FIX: 4  ·  REWORK: 1  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Media presence is the strongest of the extended sections and the display typography is distinctive.
- **Primary weakness:** All five carry site headers taken from the supplied references, and all five exceed 350 visible words.
- **Section diversity:** STRONG
- **Visual direction after corrections:** Article pages without global chrome and with lighter copy.

### S26 — Architect / Designer Profile

Studies authored: **5**  ·  KEEP: 1  ·  MINOR_FIX: 2  ·  REWORK: 1  ·  REBUILD: 1  ·  BUG_FIX: 0

- **Primary strength:** The portrait/identity pairing rule is implemented structurally and holds at every width.
- **Primary weakness:** 003 and 005 are a personnel record and a CV sheet; the section is text-heavy throughout.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Portrait-led profiles with concise facts and the reserved-field content type kept.

### S27 — Studio / Location Detail

Studies authored: **5**  ·  KEEP: 1  ·  MINOR_FIX: 2  ·  REWORK: 2  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** 002 shows the section can be place-led and premium; the reserved map slot is an honest device.
- **Primary weakness:** 003 and 005 are record sheets and keyed plans; only one study carries real photography.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Place-led location pages with photography, address first and a reserved map.

### S28 — Blog / Index List Pages (unplanned)

Studies authored: **5**  ·  KEEP: 0  ·  MINOR_FIX: 5  ·  REWORK: 0  ·  REBUILD: 0  ·  BUG_FIX: 0

- **Primary strength:** Four distinct index/list compositions with high media presence.
- **Primary weakness:** All five carry global site headers and footers; the section number itself is outside the allocated catalog.
- **Section diversity:** ACCEPTABLE
- **Visual direction after corrections:** Pending a governance decision on whether S28 exists at all.

## Study-by-Study Manifest

Every authored study appears once. `Media slots` records intentional reserved media areas —
their emptiness is by design and is never counted as a defect.

### S01 — Hero

#### ARC-S01-001

- **Section / variant:** S01 · 001
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Split hero: wordmark bar and primary nav above a left type column and a right image field.
- **What works:** Clean type ramp, generous whitespace, image field is a real compositional element rather than decoration.
- **Problem:** Carries a full global site header and primary navigation inside a hero section study.
- **Later correction direction:** Remove the global header/navigation so the study is the hero only; keep the split composition.
- **Must preserve:** The left-type / right-image split, the type scale, the image field proportion.
- **Media slots:** 1 image area
- **Header/nav contamination:** YES
- **Technical-document metaphor:** NONE
- **Text density:** LOW (42 visible words)
- **Responsive concern:** NONE
- **Notes:** Header removal is the only change the user asked for in this study.

#### ARC-S01-002

- **Section / variant:** S01 · 002
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Full-bleed image ground with an overlaid display headline and a three-stage strip beneath.
- **What works:** Strongest image-led hero in the set; large visual field, restrained copy, good stage rhythm.
- **Problem:** Global header and navigation sit inside the hero study.
- **Later correction direction:** Remove the header; keep the full-bleed field and the stage strip.
- **Must preserve:** Full-bleed media relationship and the display type treatment.
- **Media slots:** 1 full-bleed image area
- **Header/nav contamination:** YES
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (74 visible words)
- **Responsive concern:** NONE
- **Notes:** Closest existing S01 study to the new visual direction.

#### ARC-S01-003

- **Section / variant:** S01 · 003
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Oversized uppercase display headline over a dense index of typologies, scope and project records.
- **What works:** Confident typographic scale; the index gives the hero real information density without tables.
- **Problem:** Global header present; the metadata index reads as a technical register rather than a hero.
- **Later correction direction:** Remove the header and soften the index into an editorial supporting line or a small project strip.
- **Must preserve:** The display headline scale and the asymmetric composition.
- **Media slots:** 1 image area
- **Header/nav contamination:** YES
- **Technical-document metaphor:** MODERATE
- **Text density:** LOW (77 visible words)
- **Responsive concern:** NONE
- **Notes:** Index block is borderline against the new direction — review with the S01 set.

#### ARC-S01-004

- **Section / variant:** S01 · 004
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Conversion hero: full-bleed field, right-aligned title block and a circular primary action.
- **What works:** Clear single action, calm composition, image does the work.
- **Problem:** Global header and navigation inside the hero study.
- **Later correction direction:** Remove the header; keep the action-led composition.
- **Must preserve:** The circular action device and the right-aligned title block.
- **Media slots:** 1 full-bleed image area
- **Header/nav contamination:** YES
- **Technical-document metaphor:** NONE
- **Text density:** LOW (54 visible words)
- **Responsive concern:** NONE

#### ARC-S01-005

- **Section / variant:** S01 · 005
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Drawing-sheet hero: title block, sheet/set/scale/revision/status fields ruled under the headline.
- **What works:** Sector-specific identity and a strong ruled structure.
- **Problem:** Explicit drawing-sheet metaphor (SHEET, SET, SCALE, REVISION, STATUS) plus a global header.
- **Later correction direction:** Replace the title-block register with an image-led or typographic hero; remove the header.
- **Must preserve:** The ruled horizontal discipline and the wide plate area.
- **Media slots:** 1 image area
- **Header/nav contamination:** YES
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (61 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged S01 globally for header removal; the sheet metaphor also conflicts with the new direction.

### S02 — Selected Projects

#### ARC-S02-001

- **Section / variant:** S02 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Editorial project grid: serif display title beside four project cards at mixed sizes.
- **What works:** Image-led, asymmetric, premium serif treatment, minimal copy.
- **Later correction direction:** No change requested.
- **Must preserve:** The mixed-size card rhythm and the serif display heading.
- **Media slots:** 4 project image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (54 visible words)
- **Responsive concern:** NONE
- **Notes:** User decision: no design changes for S02.

#### ARC-S02-002

- **Section / variant:** S02 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Two-up residential pairing with a large uppercase title and a right-aligned standfirst.
- **What works:** Strong premium restraint; the pairing reads as a selected-works spread.
- **Later correction direction:** No change requested.
- **Must preserve:** The two-up spread and the uppercase display title.
- **Media slots:** 2 project image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (80 visible words)
- **Responsive concern:** NONE
- **Notes:** User decision: no design changes for S02.

#### ARC-S02-003

- **Section / variant:** S02 · 003
- **Status:** `KEEP`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Numbered three-column project sequence with short architectural context lines.
- **What works:** Comparable cards, clear numbering, restrained copy.
- **Later correction direction:** No change requested.
- **Must preserve:** The numbered sequence and equal card weighting.
- **Media slots:** 3 project image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (97 visible words)
- **Responsive concern:** NONE
- **Notes:** User decision: no design changes for S02.

#### ARC-S02-004

- **Section / variant:** S02 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Collage of unequal project frames with a vertical WORKS wordmark and one conversion route.
- **What works:** Most visually distinctive S02 study; genuine collage rhythm.
- **Later correction direction:** No change requested.
- **Must preserve:** The unequal collage and the vertical display word.
- **Media slots:** 6 project image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (43 visible words)
- **Responsive concern:** NONE
- **Notes:** User decision: no design changes for S02.

#### ARC-S02-005

- **Section / variant:** S02 · 005
- **Status:** `KEEP`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Centred title over a six-card gallery grid with category filter words.
- **What works:** Clean gallery grid, even rhythm, low copy.
- **Later correction direction:** No change requested.
- **Must preserve:** The six-card grid and the filter row.
- **Media slots:** 6 project image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (67 visible words)
- **Responsive concern:** NONE
- **Notes:** User decision: no design changes for S02.

### S03 — Services

#### ARC-S03-001

- **Section / variant:** S03 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four service cards, each with its own image area, title and short description.
- **What works:** Image-per-service relationship; balanced copy; scales cleanly.
- **Later correction direction:** Optional light copy trim in a later pass.
- **Must preserve:** The image-per-service card model.
- **Media slots:** 4 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (128 visible words)
- **Responsive concern:** NONE

#### ARC-S03-002

- **Section / variant:** S03 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial services page: serif display heading, four labelled image cards, principles list.
- **What works:** Premium editorial register with real media rhythm and low text.
- **Later correction direction:** None required.
- **Must preserve:** The serif display heading and the four-card media row.
- **Media slots:** 5 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (92 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for the new direction.

#### ARC-S03-003

- **Section / variant:** S03 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Three services described with image, paragraph and a stages/output/typologies field list.
- **What works:** Good media-plus-narrative pairing.
- **Problem:** Each card ends in a specification-style field list (Stages / Output / Typologies).
- **Later correction direction:** Convert the field lists into short editorial lines or drop them; keep the media relationship.
- **Must preserve:** The three-column media and narrative structure.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (136 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: field-list tail is the only technical element.

#### ARC-S03-004

- **Section / variant:** S03 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Horizontal service catalogue with a scroll rail and paired prev/next controls.
- **What works:** Strong media rail; a genuinely different navigation model in the set.
- **Problem:** Text density sits at the top of the acceptable band.
- **Later correction direction:** Light copy trim only.
- **Must preserve:** The scroll rail and its keyboard controls.
- **Media slots:** 6 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (216 visible words)
- **Responsive concern:** NONE

#### ARC-S03-005

- **Section / variant:** S03 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Services expressed as work stages under a drawing-sheet block (SHEET / SET / ENGAGEMENT / STATUS).
- **What works:** The stage sequence itself is useful and sector-true.
- **Problem:** Sheet metaphor and the stamped footer register dominate the composition.
- **Later correction direction:** Rebuild as a visual stage sequence — imagery per stage, no sheet framing.
- **Must preserve:** The four-stage progression and the stage image areas.
- **Media slots:** 4 stage image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (110 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate under the new global direction.

#### ARC-S03-006

- **Section / variant:** S03 · 006
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Paired media-and-card rows: a serif heading column beside three image/text service rows.
- **What works:** Clean alternation of media and copy; premium serif register.
- **Later correction direction:** None required.
- **Must preserve:** The paired row rhythm.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (110 visible words)
- **Responsive concern:** NONE
- **Notes:** Extension variant authored from a supplied reference.

#### ARC-S03-007

- **Section / variant:** S03 · 007
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Corner-media bento: four service cards around two image blocks.
- **What works:** Bento composition gives visual variety without heavy copy.
- **Later correction direction:** None required.
- **Must preserve:** The bento arrangement.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (124 visible words)
- **Responsive concern:** NONE
- **Notes:** Extension variant authored from a supplied reference.

### S04 — Project Typologies

#### ARC-S04-001

- **Section / variant:** S04 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four typologies as large right-aligned uppercase names against a single tall media panel.
- **What works:** Bold typographic listing with one strong media field; very low text.
- **Later correction direction:** None required.
- **Must preserve:** The right-aligned typographic listing and the tall panel.
- **Media slots:** 1 typology panel
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (64 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for typographic restraint.

#### ARC-S04-002

- **Section / variant:** S04 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial typology set: mixed serif/sans question headline, four labelled columns, image row.
- **What works:** Elegant editorial voice with a media row per typology.
- **Later correction direction:** None required.
- **Must preserve:** The mixed serif/sans headline device.
- **Media slots:** 4 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (120 visible words)
- **Responsive concern:** NONE

#### ARC-S04-003

- **Section / variant:** S04 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Typologies as a four-field record with scope values, beside two tall image areas.
- **What works:** Two tall plates give it real visual weight; copy is short.
- **Problem:** Scope field pairs read as a specification list.
- **Later correction direction:** Loosen the scope fields into short editorial lines.
- **Must preserve:** The two tall image areas and the compact layout.
- **Media slots:** 2 tall image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** LOW (76 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: mild, not a document metaphor.

#### ARC-S04-004

- **Section / variant:** S04 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three typology series as bordered image panels with a routing question and two actions.
- **What works:** Clear conversion path, image per series.
- **Later correction direction:** Light copy trim only.
- **Must preserve:** The series-based grouping and the routing question.
- **Media slots:** 3 series image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (119 visible words)
- **Responsive concern:** NONE

#### ARC-S04-005

- **Section / variant:** S04 · 005
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Typology catalogue with plate references (PLATE AREA · R-01), tabs and prev/next controls.
- **What works:** Tabbed typology switching is a genuinely different interaction model.
- **Problem:** Plate-index register and catalogue framing; highest text density in S04.
- **Later correction direction:** Keep the tabbed typology switching but present entries as project imagery, not plates.
- **Must preserve:** The tab interaction and the index rail.
- **Media slots:** 2 plate areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (331 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: plate/catalogue metaphor.

### S05 — Design Philosophy

#### ARC-S05-001

- **Section / variant:** S05 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Philosophy stated as two headline statements with supporting paragraphs and two image areas.
- **What works:** Calm editorial rhythm; media punctuates the text.
- **Later correction direction:** None required.
- **Must preserve:** The two-statement structure.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (136 visible words)
- **Responsive concern:** NONE

#### ARC-S05-002

- **Section / variant:** S05 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Oversized lowercase 'philosophy' wordmark over a centred manifesto paragraph.
- **What works:** Distinctive typographic identity; the wordmark carries the page.
- **Later correction direction:** None required.
- **Must preserve:** The wordmark device and the centred manifesto.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (104 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for typographic distinctiveness.

#### ARC-S05-003

- **Section / variant:** S05 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Six numbered positions as icon-led rows with a single supporting image area.
- **What works:** Scannable, icon-supported, clear hierarchy.
- **Problem:** Six dense rows of prose with only one media area; reads text-first.
- **Later correction direction:** Reduce to four positions and raise the media presence.
- **Must preserve:** The icon-led row rhythm.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (186 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: text-dominant rather than technical.

#### ARC-S05-004

- **Section / variant:** S05 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Conversion-led philosophy: short statement, pull quote and two actions beside a tall plate.
- **What works:** Low text, strong quote, clear route.
- **Later correction direction:** None required.
- **Must preserve:** The pull-quote device and the tall plate.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (84 visible words)
- **Responsive concern:** NONE

#### ARC-S05-005

- **Section / variant:** S05 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Statement of design principles set as numbered clauses with Clause/Applies to/Revision/Status.
- **What works:** The wide banner image and the ruled clause hierarchy are handsome.
- **Problem:** Explicit contract-document metaphor: clause numbering, revision and status stamps.
- **Later correction direction:** Rebuild as an editorial principles page — large imagery, four short principles, no clause apparatus.
- **Must preserve:** The wide band media and the four-principle content model.
- **Media slots:** 1 wide band image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (198 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: same family as the studies the user rejected elsewhere.

### S06 — Design Process

#### ARC-S06-001

- **Section / variant:** S06 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four stages as columns, each closing on a named deliverable, above a wide process image.
- **What works:** Clear stage rhythm, one strong media band, moderate copy.
- **Later correction direction:** Light copy trim only.
- **Must preserve:** The 'ends with' deliverable device.
- **Media slots:** 1 wide band image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (152 visible words)
- **Responsive concern:** NONE

#### ARC-S06-002

- **Section / variant:** S06 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial stage sequence: large numerals, serif headings and one image area per stage.
- **What works:** Best media-to-stage ratio in S06; premium and calm.
- **Later correction direction:** None required.
- **Must preserve:** The numeral-led stage rhythm and per-stage media.
- **Media slots:** 4 stage image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (163 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for how S06-003 could be reworked.

#### ARC-S06-003

- **Section / variant:** S06 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Five stages, each with output / studio does / you provide field rows beside a small image.
- **What works:** Media is present for every stage and the sequence is legible.
- **Problem:** Field rows make each stage read as a specification table; too technical and text-heavy.
- **Later correction direction:** Keep five visual stages; replace the three-field rows with one short line and larger imagery.
- **Must preserve:** The five-stage sequence and the per-stage media areas.
- **Media slots:** 5 stage image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (186 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S06-004

- **Section / variant:** S06 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Numbered client-facing route from first conversation to design stages, ending in two actions.
- **What works:** Conversion-clear, low technical language.
- **Later correction direction:** Light copy trim only.
- **Must preserve:** The 'you always know which stage you are in' framing.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (168 visible words)
- **Responsive concern:** NONE

#### ARC-S06-005

- **Section / variant:** S06 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Project programme: a workstream-by-stage matrix with sheet, set, revision and status fields.
- **What works:** Honest about not inventing dates; the matrix is technically well made.
- **Problem:** Pure programme document — matrix, revision block, no media at all.
- **Later correction direction:** Rebuild as a visual process presentation; the programme metaphor should not return.
- **Must preserve:** The idea that the studio's involvement spans every stage.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (93 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S07 — Studio About

#### ARC-S07-001

- **Section / variant:** S07 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four scattered image areas beside a short studio statement and three attribute words.
- **What works:** Image-led, very low text, confident whitespace.
- **Later correction direction:** None required.
- **Must preserve:** The scattered image composition.
- **Media slots:** 4 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (83 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S07-002

- **Section / variant:** S07 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Large 'Designing Spaces' display title with a principal portrait plate and a belief statement.
- **What works:** Premium editorial; type and media carry it.
- **Later correction direction:** None required.
- **Must preserve:** The display title and principal plate.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (79 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S07-003

- **Section / variant:** S07 · 003
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Serif question headline with a principal portrait and a four-field attribute row.
- **What works:** Warm editorial voice, good media presence.
- **Later correction direction:** Light copy trim only.
- **Must preserve:** The question-as-headline device.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (103 visible words)
- **Responsive concern:** NONE

#### ARC-S07-004

- **Section / variant:** S07 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Oversized uppercase studio statement with two chips and a two-column supporting note.
- **What works:** Bold typographic hero-like treatment; minimal copy.
- **Later correction direction:** None required.
- **Must preserve:** The oversized statement.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (84 visible words)
- **Responsive concern:** NONE

#### ARC-S07-005

- **Section / variant:** S07 · 005
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Studio described as a monograph colophon with a ruled 'learn more' row and plate area.
- **What works:** Distinctive and restrained; the wordmark treatment is strong.
- **Problem:** Colophon framing is a print-document metaphor.
- **Later correction direction:** Keep the wordmark and plate; drop the colophon labelling.
- **Must preserve:** The wordmark scale and the single plate.
- **Media slots:** 1 plate area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** LOW (87 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: light-to-moderate document metaphor.

### S08 — Architects & Designers

#### ARC-S08-001

- **Section / variant:** S08 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four-portrait roster with name and role beneath each.
- **What works:** Simple, portrait-led, minimal copy.
- **Later correction direction:** None required.
- **Must preserve:** The portrait grid.
- **Media slots:** 4 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (54 visible words)
- **Responsive concern:** NONE

#### ARC-S08-002

- **Section / variant:** S08 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial roster: role label, name and one responsibility line under each portrait.
- **What works:** Good balance of portrait and copy.
- **Later correction direction:** None required.
- **Must preserve:** The role-first labelling.
- **Media slots:** 4 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (85 visible words)
- **Responsive concern:** NONE

#### ARC-S08-003

- **Section / variant:** S08 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Six-post roster with a portrait strip above a dense list of responsibilities and profile/contact buttons.
- **What works:** Covers a full team; each post has a portrait.
- **Problem:** Reads as a personnel list: dense responsibility prose plus paired buttons per row.
- **Later correction direction:** Reduce to a portrait-led grid with one short line per person; drop the paired buttons.
- **Must preserve:** The six-post coverage and portrait areas.
- **Media slots:** 6 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (158 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S08-004

- **Section / variant:** S08 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Conversion roster: four portraits each with a direct 'talk with' action and a routing line.
- **What works:** Clear single action per person, low copy.
- **Later correction direction:** None required.
- **Must preserve:** The per-person action model.
- **Media slots:** 4 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (94 visible words)
- **Responsive concern:** NONE

#### ARC-S08-005

- **Section / variant:** S08 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Practice register: six posts as ruled table-like columns under a SHEET reference.
- **What works:** Compact and orderly.
- **Problem:** Register/sheet metaphor; portraits are reduced to labelled cells.
- **Later correction direction:** Rebuild as a portrait-led team presentation.
- **Must preserve:** The six-post content model.
- **Media slots:** 6 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (53 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: register metaphor.

#### ARC-S08-006

- **Section / variant:** S08 · 006
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Featured member with a large portrait plate above a four-portrait thumbnail strip.
- **What works:** Good hierarchy; the featured plate is a strong visual anchor.
- **Later correction direction:** None required.
- **Must preserve:** The featured-plus-strip hierarchy.
- **Media slots:** 5 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (98 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S08-007

- **Section / variant:** S08 · 007
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Expanding filmstrip: six fixed-width tab panels, only the selected one revealing a name.
- **What works:** The interaction is accessible in markup (real tablist, arrow keys, names exposed).
- **Problem:** Broken at every width as reported: collapsed panels are fixed 42-96px slivers that show nothing while media slots are empty, and the strip overflows rather than reflowing. The failure is conceptual, not only responsive — the composition depends on media to be readable at all.
- **Later correction direction:** Rebuild as a portrait-led team layout that reads with empty media slots; do not carry the sliver mechanism forward.
- **Must preserve:** The accessible tablist implementation is reusable elsewhere.
- **Media slots:** 6 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** HIGH (346 visible words)
- **Responsive concern:** CONFIRMED
- **Notes:** User flagged as broken on desktop, tablet and mobile. Root cause is the collapsed-sliver concept plus fixed widths, so REBUILD rather than BUG_FIX.

#### ARC-S08-008

- **Section / variant:** S08 · 008
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Edge-bleeding card row that scrolls horizontally, each card carrying a portrait and a role line.
- **What works:** The bleed and scroll give the section movement.
- **Problem:** Cards clip at the viewport edge by design; verify the scroll affordance on tablet.
- **Later correction direction:** Light responsive verification only.
- **Must preserve:** The edge-bleed rhythm.
- **Media slots:** 4 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (185 visible words)
- **Responsive concern:** POSSIBLE

#### ARC-S08-009

- **Section / variant:** S08 · 009
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Lead card with contact routes beside a buttoned rail of three further portraits.
- **What works:** Lead-plus-rail hierarchy works; contact routes are honest placeholders.
- **Problem:** Text density is high for a roster section.
- **Later correction direction:** Copy trim; verify rail behaviour at tablet width.
- **Must preserve:** The lead-card hierarchy.
- **Media slots:** 3 portrait areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** HIGH (241 visible words)
- **Responsive concern:** POSSIBLE

### S09 — Awards & Publications

#### ARC-S09-001

- **Section / variant:** S09 · 001
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Two parallel lists of award and publication records with year columns.
- **What works:** Honest token treatment; clean two-column rhythm.
- **Problem:** No media at all; reads as a bibliography rather than recognition.
- **Later correction direction:** Rework toward covers, tear sheets or project imagery with short recognition lines.
- **Must preserve:** The awards/publications split and the token discipline.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (142 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S09-002

- **Section / variant:** S09 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial recognition page: a tear-sheet plate beside a selected record list.
- **What works:** The only S09 study with real media presence; premium serif register.
- **Later correction direction:** None required.
- **Must preserve:** The tear-sheet plate relationship.
- **Media slots:** 1 tear sheet area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (73 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for reworking the rest of S09.

#### ARC-S09-003

- **Section / variant:** S09 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Full record table: year, record, project, kind and a 'field to fill' column, with a counts rail.
- **What works:** Rigorous and honest about being a template.
- **Problem:** A data table with no media; the most document-like study in S09.
- **Later correction direction:** Rebuild as a visual recognition presentation; the table should not return.
- **Must preserve:** The idea of one combined record rather than split lists.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (192 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S09-004

- **Section / variant:** S09 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Press-office conversion layout: coverage list beside a press-kit request panel.
- **What works:** Clear route for editors; low technical framing.
- **Problem:** No media area, but the section role tolerates it here.
- **Later correction direction:** Optional: add a media slot in a later pass.
- **Must preserve:** The press-office panel.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (118 visible words)
- **Responsive concern:** NONE

#### ARC-S09-005

- **Section / variant:** S09 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Back-matter citations: keyed [A-01]/[P-01] entries in bibliographic form under a SHEET reference.
- **What works:** Citation discipline is intellectually honest.
- **Problem:** Explicit monograph back-matter document; no media; highest text density in S09.
- **Later correction direction:** Rebuild as an editorial recognition page with covers, quotes or project imagery.
- **Must preserve:** The keying idea that each record belongs to a project.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (287 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S10 — Capabilities

#### ARC-S10-001

- **Section / variant:** S10 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three capability groups with in-house / consultant marks on each line.
- **What works:** The in-house vs consultant distinction is genuinely useful and clearly marked in words.
- **Problem:** No media area.
- **Later correction direction:** Consider adding one supporting media field in a later pass.
- **Must preserve:** The delivery-mode marking.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (163 visible words)
- **Responsive concern:** NONE

#### ARC-S10-002

- **Section / variant:** S10 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four numbered capacities with short sub-lists, set as an editorial two-by-two.
- **What works:** Calm structure; reads as positioning rather than inventory.
- **Problem:** No media area.
- **Later correction direction:** Optional media in a later pass.
- **Must preserve:** The four-capacity framing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (197 visible words)
- **Responsive concern:** NONE

#### ARC-S10-003

- **Section / variant:** S10 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Six capability groups behind native disclosure controls, each listing four lines with modes.
- **What works:** Disclosure keeps the section short; the interaction is script-free.
- **Problem:** Twenty-four capability lines plus mode stamps read as an inventory document; no media.
- **Later correction direction:** Reduce the inventory and introduce imagery; keep disclosure only if the content stays short.
- **Must preserve:** The script-free disclosure pattern.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** HIGH (293 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: dense inventory.

#### ARC-S10-004

- **Section / variant:** S10 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three entry routes ('you have a site / a building / drawings') each naming a first piece of work.
- **What works:** Excellent conversion logic; plain language, no technical framing.
- **Problem:** No media area.
- **Later correction direction:** Optional media in a later pass.
- **Must preserve:** The three-route model.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (195 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for conversion-led studies.

#### ARC-S10-005

- **Section / variant:** S10 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Annex A schedule of services: numbered clauses A1.1-A4.4 with INCLUDED / ON REQUEST / NOT OFFERED stamps.
- **What works:** The scope-stamp idea is honest and sector-true.
- **Problem:** An appointment annex reproduced as a web section; no media; heavy document metaphor.
- **Later correction direction:** Rebuild as a visual capability presentation; the annex framing should not return.
- **Must preserve:** The three-state scope distinction, if expressed visually.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (216 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S11 — Materials & Sustainability

#### ARC-S11-001

- **Section / variant:** S11 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Six materials, each with a sample area, a use line and a 'what we ask of it' line.
- **What works:** Real sample media per material; the questioning device is distinctive.
- **Problem:** Text density is at the top of the band.
- **Later correction direction:** Light copy trim.
- **Must preserve:** The sample-per-material model.
- **Media slots:** 6 sample areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** HIGH (263 visible words)
- **Responsive concern:** NONE
- **Notes:** Closest S11 study to the desired material-led direction.

#### ARC-S11-002

- **Section / variant:** S11 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Material board of five sample areas beside four selection questions.
- **What works:** Board composition is visual and low-text.
- **Later correction direction:** None required.
- **Must preserve:** The board arrangement.
- **Media slots:** 5 sample areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (166 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S11-003

- **Section / variant:** S11 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Material record: six entries with used-for / finish / maintenance / end-of-life / evidence fields.
- **What works:** The reserved 'evidence' field is an honest device.
- **Problem:** A specification record with no material imagery at all — the opposite of what the section needs.
- **Later correction direction:** Rebuild around material samples and textures with concise principles.
- **Must preserve:** The reserved evidence field as a content idea.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (260 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S11-004

- **Section / variant:** S11 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Sample-set request: a sample box media area beside four numbered contents and two actions.
- **What works:** Conversion-clear and material-led.
- **Later correction direction:** None required.
- **Must preserve:** The physical sample-set offer.
- **Media slots:** 1 sample box area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (139 visible words)
- **Responsive concern:** NONE

#### ARC-S11-005

- **Section / variant:** S11 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Annotated wall build-up: five layer bands read outside-to-inside under a SHEET reference.
- **What works:** Genuinely sector-native and carefully annotated.
- **Problem:** A technical detail drawing rendered as a web section; no photographic media; heavy metaphor.
- **Later correction direction:** Rebuild toward material imagery and short sustainability principles.
- **Must preserve:** The layer-by-layer reasoning as narrative content.
- **Media slots:** 5 layer bands (drawn)
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (263 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S12 — Client Testimonials

#### ARC-S12-001

- **Section / variant:** S12 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Featured quote over an image with four supporting quote cards.
- **What works:** Image-backed feature quote; clear card rhythm.
- **Problem:** Text density is high, as quotes require.
- **Later correction direction:** Light trim only.
- **Must preserve:** The featured-over-image treatment.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** HIGH (232 visible words)
- **Responsive concern:** NONE

#### ARC-S12-002

- **Section / variant:** S12 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Single stepped testimonial with a large display word and a position readout.
- **What works:** Strong editorial device; accessible stepper with a live region.
- **Problem:** Word count is the highest in S12 because five quotes are held in the page.
- **Later correction direction:** Consider shortening the placeholder quotes.
- **Must preserve:** The stepper interaction and the display word.
- **Media slots:** 1 portrait area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** EXCESSIVE (437 visible words)
- **Responsive concern:** NONE

#### ARC-S12-003

- **Section / variant:** S12 · 003
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Quote wall of six testimonials interleaved with two project reference cards.
- **What works:** Uneven wall rhythm is deliberate and works.
- **Problem:** High text density inherent to a quote wall.
- **Later correction direction:** Light trim only.
- **Must preserve:** The interleaved project references.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (260 visible words)
- **Responsive concern:** NONE

#### ARC-S12-004

- **Section / variant:** S12 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three testimonials with one set over an image, closing on a references request.
- **What works:** Good conversion framing; honest permission language.
- **Later correction direction:** None required.
- **Must preserve:** The 'ask for the rest' panel.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** HIGH (210 visible words)
- **Responsive concern:** NONE

#### ARC-S12-005

- **Section / variant:** S12 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Annex B client references: keyed [REF-01] statements with relationship, signatory and dated fields.
- **What works:** Distinguishes a reference from a marketing quote — a real professional idea.
- **Problem:** Prequalification annex reproduced as a web section; heavy document metaphor and high text.
- **Later correction direction:** Rebuild as an editorial testimonial presentation.
- **Must preserve:** The distinction between a written reference and a lifted quote.
- **Media slots:** 1 plate area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (309 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S13 — Featured Project Case Study

#### ARC-S13-001

- **Section / variant:** S13 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Case study with a lead image, a metadata rail and two narrative sections.
- **What works:** Balanced; media leads and copy supports.
- **Later correction direction:** Light copy trim.
- **Must preserve:** The lead image plus metadata rail.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (185 visible words)
- **Responsive concern:** NONE

#### ARC-S13-002

- **Section / variant:** S13 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Held plate beside a scrolling account of the project.
- **What works:** The held-image device is distinctive and premium.
- **Problem:** Text runs long beside the held plate.
- **Later correction direction:** Light copy trim.
- **Must preserve:** The held-plate interaction.
- **Media slots:** 1 held plate
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (204 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S13-003

- **Section / variant:** S13 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Project dossier: facts band, account column, numbered decisions and a credits grid.
- **What works:** Three plates and a clear decision sequence.
- **Problem:** Dossier framing plus a credits grid make it read as a document.
- **Later correction direction:** Keep the decision sequence and plates; drop the dossier and credits apparatus, raise media scale.
- **Must preserve:** The 'decisions, in order' content model and the three plates.
- **Media slots:** 3 plate areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (272 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S13-004

- **Section / variant:** S13 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Case study opening on the client's first sentence, closing on a conversation invitation.
- **What works:** Strong narrative hook; honest about not claiming outcomes.
- **Later correction direction:** Light copy trim.
- **Must preserve:** The opening-sentence device.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (225 visible words)
- **Responsive concern:** NONE

#### ARC-S13-005

- **Section / variant:** S13 · 005
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Existing/proposed plate pairs with an annotation line and a schedule of change.
- **What works:** The matched-pair comparison is a genuinely strong sector idea with four plates.
- **Problem:** Sheet framing, plate references and a change schedule push it into document territory.
- **Later correction direction:** Keep the before/after pairing; remove the sheet apparatus and the schedule table.
- **Must preserve:** The matched existing/proposed pairing.
- **Media slots:** 4 plate areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (266 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: the comparison idea is worth preserving.

### S14 — Project Gallery

#### ARC-S14-001

- **Section / variant:** S14 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Eight gallery images across four aspect ratios with short record captions.
- **What works:** Image-led, low text, varied ratios.
- **Problem:** Eight frames — check against the user's 3x3 preference for the section.
- **Later correction direction:** Confirm the image-count target with the user; otherwise no change.
- **Must preserve:** The mixed-ratio rhythm.
- **Media slots:** 8 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (93 visible words)
- **Responsive concern:** NONE
- **Notes:** The 3x3 instruction was given for S14-003; carry the question to the whole section.

#### ARC-S14-002

- **Section / variant:** S14 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four plates presented one at a time with monograph-style captions on hairlines.
- **What works:** Premium sequencing; each plate holds the measure.
- **Problem:** 'Plate' captioning is a light print metaphor.
- **Later correction direction:** Optional: rename plates to plain captions.
- **Must preserve:** The one-at-a-time sequencing.
- **Media slots:** 4 plate areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (122 visible words)
- **Responsive concern:** NONE

#### ARC-S14-003

- **Section / variant:** S14 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Contact sheet: eighteen equal frames above a numbered legend of eighteen entries.
- **What works:** One ratio across the sheet makes frames genuinely comparable.
- **Problem:** Too many images and a photographic contact-sheet document metaphor with a long legend.
- **Later correction direction:** Reduce to a 3x3 grid of nine images and drop the numbered legend; keep one consistent ratio.
- **Must preserve:** The single-ratio discipline.
- **Media slots:** 18 frames
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (157 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical; gallery must be 3x3 = 9 images.

#### ARC-S14-004

- **Section / variant:** S14 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Six gallery images interrupted once by a project-book request band.
- **What works:** The interruption is a good conversion device inside a gallery.
- **Later correction direction:** None required.
- **Must preserve:** The single interruption band.
- **Media slots:** 6 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (161 visible words)
- **Responsive concern:** NONE

#### ARC-S14-005

- **Section / variant:** S14 · 005
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Gallery ordered by scale — situation, building, room, detail — under a SHEET reference.
- **What works:** The scale ordering is a strong sector-native idea and already lands on nine images.
- **Problem:** Sheet framing, axis labels and 'not to scale' notation.
- **Later correction direction:** Keep the scale ordering; remove the sheet apparatus.
- **Must preserve:** The far-to-close ordering and the nine-image count.
- **Media slots:** 9 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (225 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: ordering idea is worth preserving.

### S15 — Sectors & Markets

#### ARC-S15-001

- **Section / variant:** S15 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Six market cards, each with an image field, short description and an explore link.
- **What works:** Image per market, clean grid, low copy.
- **Later correction direction:** None required.
- **Must preserve:** The six-card market grid.
- **Media slots:** 6 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (118 visible words)
- **Responsive concern:** NONE

#### ARC-S15-002

- **Section / variant:** S15 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three broad fields with large numerals and generous image blocks.
- **What works:** Premium editorial rhythm; very low text.
- **Later correction direction:** None required.
- **Must preserve:** The numeral-led field rhythm.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (80 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S15-003

- **Section / variant:** S15 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Capability matrix: markets as rows against architecture / interiors / reuse columns with Core/Selective values.
- **What works:** Compact and comparable.
- **Problem:** A capability table with no media; reads as an internal matrix.
- **Later correction direction:** Rebuild as a visual market presentation.
- **Must preserve:** The idea that disciplines combine differently per market.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (88 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S15-004

- **Section / variant:** S15 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four pathway cards routing a visitor by project type toward one conversation.
- **What works:** Clear conversion routing, plain language.
- **Problem:** No media area.
- **Later correction direction:** Optional media in a later pass.
- **Must preserve:** The pathway routing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (120 visible words)
- **Responsive concern:** NONE

#### ARC-S15-005

- **Section / variant:** S15 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Practice atlas: a scale-by-context grid of nine cells, one marked 'open territory'.
- **What works:** Intellectually neat; the axis idea is memorable.
- **Problem:** An atlas/matrix diagram with no media; explicitly the technical-diagram family.
- **Later correction direction:** Rebuild as a visual market presentation.
- **Must preserve:** The scale-versus-context idea as narrative, not as a matrix.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (125 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S16 — Press & News

#### ARC-S16-001

- **Section / variant:** S16 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Featured studio note with an image beside four secondary update links.
- **What works:** Feature-plus-list is the right shape for a news section.
- **Later correction direction:** None required.
- **Must preserve:** The feature/list split.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (82 visible words)
- **Responsive concern:** NONE

#### ARC-S16-002

- **Section / variant:** S16 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Journal-style issue page: one long read plus three note cards, each with an image.
- **What works:** Editorial and image-led with very low copy.
- **Later correction direction:** None required.
- **Must preserve:** The long-read plus notes structure.
- **Media slots:** 4 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (92 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S16-003

- **Section / variant:** S16 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Press-room archive: a filterable date/type/title/topic table of six entries.
- **What works:** Filter chips and a scannable index.
- **Problem:** A tabular archive index with no media; reads as a database view.
- **Later correction direction:** Rework into a visual archive — thumbnails, date and title, no table.
- **Must preserve:** The filter-by-type idea.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (115 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S16-004

- **Section / variant:** S16 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Press room with a current feature and three resource panels for editors.
- **What works:** Clear editor-facing routes; honest about not using publication logos.
- **Later correction direction:** None required.
- **Must preserve:** The three-resource panel model.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (109 visible words)
- **Responsive concern:** NONE

#### ARC-S16-005

- **Section / variant:** S16 · 005
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Pin-up press desk: a cover note and three pinned cards on a board.
- **What works:** Distinctive board metaphor that is spatial rather than documentary.
- **Later correction direction:** None required.
- **Must preserve:** The pin-board arrangement.
- **Media slots:** 4 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (102 visible words)
- **Responsive concern:** NONE

### S17 — Studio Locations

#### ARC-S17-001

- **Section / variant:** S17 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three studio cards with an image, address lines and a details link.
- **What works:** Image per location, low copy.
- **Later correction direction:** None required.
- **Must preserve:** The three-card location grid.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (79 visible words)
- **Responsive concern:** NONE

#### ARC-S17-002

- **Section / variant:** S17 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Studio portraits: one principal location given a large panel, two smaller beneath.
- **What works:** Good hierarchy between a principal studio and the others.
- **Later correction direction:** None required.
- **Must preserve:** The principal-plus-two hierarchy.
- **Media slots:** 3 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (70 visible words)
- **Responsive concern:** NONE

#### ARC-S17-003

- **Section / variant:** S17 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Studio directory table: location, address, access and local time columns.
- **What works:** Compact and genuinely useful information.
- **Problem:** A directory table with no media.
- **Later correction direction:** Rework into location cards with imagery and short access lines.
- **Must preserve:** The access and local-time content.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** LOW (96 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S17-004

- **Section / variant:** S17 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Visit-led locations page: one featured studio with actions and three alternative routes.
- **What works:** Conversion-clear, warm language.
- **Later correction direction:** None required.
- **Must preserve:** The visit-first framing.
- **Media slots:** 1 image area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (114 visible words)
- **Responsive concern:** NONE

#### ARC-S17-005

- **Section / variant:** S17 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Practice atlas: three studios as lettered coordinate cells on a network diagram.
- **What works:** Distinctive diagrammatic identity.
- **Problem:** Coordinate/atlas diagram with no media; technical-diagram family.
- **Later correction direction:** Rebuild as a visual studio-network presentation.
- **Must preserve:** The shared-practice framing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (95 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S18 — Studio Stats

#### ARC-S18-001

- **Section / variant:** S18 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Four large figures with short labels and one-line context.
- **What works:** Exactly the large-number treatment the user described as desirable.
- **Problem:** No media area.
- **Later correction direction:** Optional media in a later pass.
- **Must preserve:** The large-figure scale.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (79 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for S18 direction.

#### ARC-S18-002

- **Section / variant:** S18 · 002
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Editorial stat block: a large '1' anchoring three supporting figures under a measure label.
- **What works:** The single anchoring figure is a strong idea.
- **Problem:** Sheet/measure framing and a ruled grid make it read as a data sheet.
- **Later correction direction:** Keep the anchoring figure; loosen the ruled framing and add media.
- **Must preserve:** The 'one shared practice' anchor.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** LOW (66 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S18-003

- **Section / variant:** S18 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Practice data index: six measures as a numbered table with a context column.
- **What works:** Honest labelling of every figure as illustrative.
- **Problem:** A data table with no media.
- **Later correction direction:** Rebuild as large figures with short supporting copy and imagery.
- **Must preserve:** The 'context attached to every figure' principle.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (99 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

#### ARC-S18-004

- **Section / variant:** S18 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three figures framed around collaboration, closing on one action.
- **What works:** Conversion-led without inventing capability claims.
- **Problem:** No media area.
- **Later correction direction:** Optional media in a later pass.
- **Must preserve:** The collaboration framing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (94 visible words)
- **Responsive concern:** NONE

#### ARC-S18-005

- **Section / variant:** S18 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Measurement drawing: four figures set on a dimension-line field with 'not to scale' notation.
- **What works:** Visually striking and sector-native.
- **Problem:** An architectural measurement sheet used as decoration; the metaphor the user is moving away from.
- **Later correction direction:** Rebuild as large elegant figures with media.
- **Must preserve:** The dimension-line rhythm as a purely graphic idea, if reused at all.
- **Media slots:** 1 measure band
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (86 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too text-heavy.

### S19 — Project Inquiry

#### ARC-S19-001

- **Section / variant:** S19 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Two-part inquiry form: about you and about the project, with a three-step progress line.
- **What works:** Clean form structure, real labels, honest consent line.
- **Later correction direction:** None required.
- **Must preserve:** The two-part grouping and step indicator.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (94 visible words)
- **Responsive concern:** NONE

#### ARC-S19-002

- **Section / variant:** S19 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three-question editorial inquiry with a large numeral and a single send action.
- **What works:** Very low friction; premium restraint.
- **Later correction direction:** None required.
- **Must preserve:** The three-question reduction.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (76 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference.

#### ARC-S19-003

- **Section / variant:** S19 · 003
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Detailed brief form with contact and project groups, stage radios and a scope field.
- **What works:** Appropriate for a detailed-brief territory; clearly labelled.
- **Problem:** Form-heavy by role, not by metaphor.
- **Later correction direction:** None required.
- **Must preserve:** The stage-radio grouping.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (77 visible words)
- **Responsive concern:** NONE

#### ARC-S19-004

- **Section / variant:** S19 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Situation-first inquiry: three starting points feeding one short form.
- **What works:** Best conversion logic in S19.
- **Later correction direction:** None required.
- **Must preserve:** The situation-first routing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** MEDIUM (116 visible words)
- **Responsive concern:** NONE

#### ARC-S19-005

- **Section / variant:** S19 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Inquiry laid out as a working project sheet with coordinate fields and an 'issue the brief' action.
- **What works:** Distinctive framing.
- **Problem:** Working-sheet/coordinate metaphor, explicitly not wanted.
- **Later correction direction:** Rebuild as a clean contemporary inquiry form.
- **Must preserve:** The short field set.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (82 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical; working-sheet style not desired.

### S20 — Consultation CTA

#### ARC-S20-001

- **Section / variant:** S20 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Centred consultation panel with two actions and three reassurance points.
- **What works:** Simple, calm, low friction.
- **Later correction direction:** None required.
- **Must preserve:** The reassurance points.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (54 visible words)
- **Responsive concern:** NONE

#### ARC-S20-002

- **Section / variant:** S20 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial session card: large numeral, three agenda lines and one action.
- **What works:** Premium restraint; reads as an invitation.
- **Later correction direction:** None required.
- **Must preserve:** The numeral-led session framing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (58 visible words)
- **Responsive concern:** NONE

#### ARC-S20-003

- **Section / variant:** S20 · 003
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Consultation menu of three formats with best-for and format columns.
- **What works:** Genuinely useful comparison; light table.
- **Problem:** Borderline tabular presentation.
- **Later correction direction:** Optional: convert the table to cards.
- **Must preserve:** The three-format comparison.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (99 visible words)
- **Responsive concern:** NONE

#### ARC-S20-004

- **Section / variant:** S20 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Consultation request with session type, date and time-window fields.
- **What works:** Clear request flow; honest that nothing is connected.
- **Later correction direction:** None required.
- **Must preserve:** The three-step confirmation framing.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (79 visible words)
- **Responsive concern:** NONE

#### ARC-S20-005

- **Section / variant:** S20 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Meeting sheet: a 20/20/20 agenda laid out as a ruled document with an agenda axis.
- **What works:** The one-hour agenda idea is useful.
- **Problem:** Working-sheet/agenda-document style, explicitly not wanted.
- **Later correction direction:** Rebuild as an elegant consultation invitation.
- **Must preserve:** The three-part agenda content.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (107 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical; agenda-document style not desired.

### S21 — Subpage Hero

#### ARC-S21-001

- **Section / variant:** S21 · 001
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Subpage header: eyebrow, page title, standfirst and a four-field metadata row.
- **What works:** Type hierarchy is clean and the no-image case is handled.
- **Problem:** The metadata row makes it read as a document header rather than a website subpage hero.
- **Later correction direction:** Rework into a conventional typographic subpage hero; drop the metadata register.
- **Must preserve:** The eyebrow/title/standfirst spine and the no-image variant.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** LOW (86 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S21 as conventional internal-page heroes.

#### ARC-S21-002

- **Section / variant:** S21 · 002
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Title block above a contained 21:9 image strip.
- **What works:** Closest study to the clarified intent — a contained image hero.
- **Problem:** Caption apparatus and record labelling still read as documentation.
- **Later correction direction:** Refine into a contained-image subpage hero; simplify the labels.
- **Must preserve:** The contained strip proportion.
- **Media slots:** 1 contained strip
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (86 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S21 as conventional internal-page heroes.

#### ARC-S21-003

- **Section / variant:** S21 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Dense page header with an eight-field metadata grid and an on-this-page contents list.
- **What works:** Information-rich and orderly.
- **Problem:** Reads as a dossier cover with a technical metadata register — explicitly excluded.
- **Later correction direction:** Rebuild as a conventional subpage hero.
- **Must preserve:** The idea that a long page may need in-page contents, if it belongs elsewhere.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (133 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S21 as conventional internal-page heroes.

#### ARC-S21-004

- **Section / variant:** S21 · 004
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Subpage header with a single contextual action panel beside the title.
- **What works:** Single-action discipline suits a subpage hero.
- **Problem:** Panel framing and long explanatory copy weaken the hero reading.
- **Later correction direction:** Rework into a conventional hero with one action; shorten the copy.
- **Must preserve:** The single contextual action rule.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (121 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S21 as conventional internal-page heroes.

#### ARC-S21-005

- **Section / variant:** S21 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Running head and folio: part/folio references above the page title.
- **What works:** Distinctive print identity.
- **Problem:** Document folio metaphor — explicitly excluded from this role.
- **Later correction direction:** Rebuild as an image-background or typographic subpage hero.
- **Must preserve:** Nothing structural; the type scale only.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** LOW (81 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S21 as conventional internal-page heroes.

### S22 — Breadcrumb / Context Navigation

#### ARC-S22-001

- **Section / variant:** S22 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Plain four-level breadcrumb trail with the current page marked programmatically.
- **What works:** Exactly the conventional breadcrumb the user described; correct semantics.
- **Later correction direction:** Keep as the reference implementation for the section.
- **Must preserve:** The trail markup, aria-current handling and wrapping behaviour.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** NONE
- **Text density:** LOW (60 visible words)
- **Responsive concern:** NONE
- **Notes:** Matches the clarified S22 role.

#### ARC-S22-002

- **Section / variant:** S22 · 002
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Uppercase trail with a separate 'back to parent' return link.
- **What works:** Still a breadcrumb; the return link is a small, familiar web pattern.
- **Problem:** The second landmark slightly broadens the role.
- **Later correction direction:** Confirm whether the return link stays; otherwise keep.
- **Must preserve:** The trail and its quiet register.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** LOW (63 visible words)
- **Responsive concern:** NONE
- **Notes:** Within the clarified role, pending confirmation of the return link.

#### ARC-S22-003

- **Section / variant:** S22 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Context bar: trail plus sibling-page chips plus an on-this-page contents list.
- **What works:** Rich local context and a good narrow-width scroll region.
- **Problem:** Broadens breadcrumbs into a page-contents and sibling-navigation system — explicitly excluded.
- **Later correction direction:** Rebuild as a conventional breadcrumb variant.
- **Must preserve:** The narrow-width scroll-region technique.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (116 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S22 as conventional breadcrumbs only.

#### ARC-S22-004

- **Section / variant:** S22 · 004
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Trail above a previous/next project pager with a contextual link.
- **What works:** Pager links name their destinations in full.
- **Problem:** Turns breadcrumbs into project navigation — explicitly excluded.
- **Later correction direction:** Rebuild as a conventional breadcrumb variant.
- **Must preserve:** The full-destination naming rule.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** MEDIUM (101 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S22 as conventional breadcrumbs only.

#### ARC-S22-005

- **Section / variant:** S22 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Sheet-reference trail beside a nine-cell key plan locating the page in a set.
- **What works:** Sector-native and accessible (position marked three ways).
- **Problem:** A drawing-set locator — explicitly excluded from the breadcrumb role.
- **Later correction direction:** Rebuild as a conventional breadcrumb variant.
- **Must preserve:** The triple-marking of current state (not fill alone).
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** MEDIUM (119 visible words)
- **Responsive concern:** NONE
- **Notes:** User clarified S22 as conventional breadcrumbs only.

### S23 — Architecture / Interior Service Detail

#### ARC-S23-001

- **Section / variant:** S23 · 001
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Service page: breadcrumb, title beside a facts rail, included/excluded pair, stages, related services.
- **What works:** Covers the full service contract and the rail releases correctly on narrow screens.
- **Problem:** 485 visible words with only two small image areas; included/excluded lists read as specification.
- **Later correction direction:** Rework toward the clarified flow: hero, short intro, major media, 3-4 aspects, image+text, simple process, example, short FAQ, CTA.
- **Must preserve:** The included/excluded distinction as content and the enquiry close.
- **Media slots:** 2 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** EXCESSIVE (485 visible words)
- **Responsive concern:** NONE
- **Notes:** User: S23 output does not meet the target.

#### ARC-S23-002

- **Section / variant:** S23 · 002
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Editorial service essay at a single measure with a colophon of service facts at the foot.
- **What works:** Premium register; one strong wide plate.
- **Problem:** 528 words of essay with a single media area; colophon is a print-document device.
- **Later correction direction:** Rework into a visual service page with more media and less prose.
- **Must preserve:** The wide plate and the calm measure.
- **Media slots:** 1 wide plate
- **Header/nav contamination:** NO
- **Technical-document metaphor:** MODERATE
- **Text density:** EXCESSIVE (528 visible words)
- **Responsive concern:** NONE
- **Notes:** User: S23 output does not meet the target.

#### ARC-S23-003

- **Section / variant:** S23 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Scope document: numbered clauses 1.0-6.0, a deliverables table and a question register.
- **What works:** Rigorous and complete as a scope statement.
- **Problem:** 764 words, a table, clause numbering and no media — the most document-like study in the sector.
- **Later correction direction:** Rebuild against the clarified service-detail flow.
- **Must preserve:** The FAQ content as a short question set.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** EXCESSIVE (764 visible words)
- **Responsive concern:** NONE
- **Notes:** User: S23 output does not meet the target.

#### ARC-S23-004

- **Section / variant:** S23 · 004
- **Status:** `REWORK`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Decision-ordered service page closing on a labelled placeholder enquiry form.
- **What works:** Honest self-selection (sends the wrong reader elsewhere) and a real accessible form.
- **Problem:** 553 words and no media; the page argues in prose rather than showing the service.
- **Later correction direction:** Rework with major media, fewer words, and the enquiry kept.
- **Must preserve:** The self-selection pair and the enquiry close.
- **Media slots:** none
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (553 visible words)
- **Responsive concern:** NONE
- **Notes:** User: S23 output does not meet the target.

#### ARC-S23-005

- **Section / variant:** S23 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Responsibility ledger: five stages split into studio-does / you-provide columns across a spine.
- **What works:** Genuinely sector-true content and a four-frame record strip.
- **Problem:** 819 words — the highest in the sector — in an explicit ledger structure.
- **Later correction direction:** Rebuild against the clarified service-detail flow; the ledger should not return as a layout.
- **Must preserve:** The stage-by-stage responsibility content, expressed briefly.
- **Media slots:** 4 record images
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** EXCESSIVE (819 visible words)
- **Responsive concern:** NONE
- **Notes:** User: S23 output does not meet the target.

### S24 — Project Detail

#### ARC-S24-001

- **Section / variant:** S24 · 001
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Three-chapter project case study: context, approach and delivery, with a project-facts ledger at the foot.
- **What works:** Portfolio-shaped; large lead image and a clear chapter rhythm.
- **Problem:** The closing 'project facts / ledger' block is mildly documentary.
- **Later correction direction:** Light: soften the facts block into concise project metadata.
- **Must preserve:** The three-chapter narrative and the lead image scale.
- **Media slots:** 5 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (251 visible words)
- **Responsive concern:** NONE
- **Notes:** Not user-flagged; closest S24 study to the desired portfolio direction.

#### ARC-S24-002

- **Section / variant:** S24 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Long-form editorial case study in three chapters with a chapter jump bar and pull statements.
- **What works:** Strong editorial voice; media appears throughout.
- **Problem:** 'Folio' labelling is a light print metaphor.
- **Later correction direction:** Light: drop the folio label.
- **Must preserve:** The chapter structure and pull statements.
- **Media slots:** 6 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (259 visible words)
- **Responsive concern:** NONE
- **Notes:** Not user-flagged.

#### ARC-S24-003

- **Section / variant:** S24 · 003
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Project dossier with a workstream table, numbered drawings (PLAN / NTS) and a credits ledger.
- **What works:** Thorough; drawings and record slots are clearly labelled.
- **Problem:** Dossier framing, workstream table and NTS notation — the document family the user is moving away from.
- **Later correction direction:** Rebuild as a portfolio-driven project page: strong hero, concise metadata, large imagery, short narrative.
- **Must preserve:** The workstream content as short narrative.
- **Media slots:** 5 drawing/record areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (251 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too document-oriented.

#### ARC-S24-004

- **Section / variant:** S24 · 004
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Case study connecting situation, response and delivery to related expertise and a next project.
- **What works:** Good conversion path out of a project page.
- **Problem:** Text density is high for a portfolio page.
- **Later correction direction:** Light copy trim.
- **Must preserve:** The related-expertise and next-project routes.
- **Media slots:** 5 image areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (222 visible words)
- **Responsive concern:** NONE
- **Notes:** Not user-flagged.

#### ARC-S24-005

- **Section / variant:** S24 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** YES
- **Additional review candidate:** NO
- **Current structural concept:** Project organised as an architectural issue set: cover sheet, drawing set, decisions and a register.
- **What works:** Sector-native and internally consistent.
- **Problem:** Drawing issue set, sheet references and NTS notation — explicitly on the list to avoid.
- **Later correction direction:** Rebuild as a portfolio-driven project page.
- **Must preserve:** The 'four moves' decision content.
- **Media slots:** 6 drawing areas
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** HIGH (316 visible words)
- **Responsive concern:** NONE
- **Notes:** User flagged: too technical, too document-oriented.

### S25 — Studio Journal / Article Detail

#### ARC-S25-001

- **Section / variant:** S25 · 001
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Journal article with a back chip, title beside a ruled meta column, lead image, author rail and related block.
- **What works:** Good article anatomy; media in the lead and in the related block.
- **Problem:** Carries a global site header and primary navigation; 379 visible words.
- **Later correction direction:** Remove the global header under the new global rule; light copy trim.
- **Must preserve:** The article anatomy and the related-reading block.
- **Media slots:** 4 image areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (379 visible words)
- **Responsive concern:** NONE
- **Notes:** Built 1:1 from a user-supplied reference that included the header — confirm the header removal against that instruction.

#### ARC-S25-002

- **Section / variant:** S25 · 002
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Magazine sheet on a grey ground: publication bar, film area, large centred display headline, interview.
- **What works:** Strong premium editorial identity; the display headline is the best in S25.
- **Problem:** Publication bar acts as a site header; 398 words with one media area.
- **Later correction direction:** Remove or reduce the bar; keep the display headline and film area.
- **Must preserve:** The centred display headline and the sheet-on-ground device.
- **Media slots:** 1 film area
- **Header/nav contamination:** YES
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (398 visible words)
- **Responsive concern:** NONE
- **Notes:** Reference-driven header; same confirmation question as S25-001.

#### ARC-S25-003

- **Section / variant:** S25 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Blog article between two sidebars with pull quote, share row, author box, related posts and a comment form.
- **What works:** Complete blog anatomy; the centre column holds its measure.
- **Problem:** Masthead bar plus 461 words and nine stacked regions make it the densest S25 study.
- **Later correction direction:** Reduce the region count and the sidebars; remove the masthead.
- **Must preserve:** The comment form and author box as content models.
- **Media slots:** 5 image areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** MODERATE
- **Text density:** EXCESSIVE (461 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: density, not technical metaphor.

#### ARC-S25-004

- **Section / variant:** S25 · 004
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Article with a pinned meta rail, uppercase headline, dark in-body contact card and an oversized related band.
- **What works:** The related band and the in-body card are visually strong.
- **Problem:** Global header with a primary nav and a standing CTA; 420 words.
- **Later correction direction:** Remove the global header; keep the rail and related band.
- **Must preserve:** The oversized related band.
- **Media slots:** 6 image areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (420 visible words)
- **Responsive concern:** NONE
- **Notes:** Reference-driven header; confirm removal.

#### ARC-S25-005

- **Section / variant:** S25 · 005
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Cream feature with a mixed-scale serif title, unequal plate pair and a credits register beside the body.
- **What works:** Best media rhythm in S25; the mixed-scale title is distinctive.
- **Problem:** Category nav acts as a site header; the credits register is a light document device; 373 words.
- **Later correction direction:** Remove the header; keep the plates and title device; simplify the credits.
- **Must preserve:** The mixed-scale display title and the unequal plate pair.
- **Media slots:** 4 plate areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** MODERATE
- **Text density:** EXCESSIVE (373 visible words)
- **Responsive concern:** NONE
- **Notes:** Reference-driven header; confirm removal.

### S26 — Architect / Designer Profile

#### ARC-S26-001

- **Section / variant:** S26 · 001
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Profile with portrait paired to identity, post description, attachments, reserved background and a contact rail.
- **What works:** The portrait/identity pairing rule is implemented structurally and holds at every width.
- **Problem:** 373 words with a single portrait; the reserved-fields register adds bulk.
- **Later correction direction:** Trim copy and raise media presence; keep the reserved-field device.
- **Must preserve:** The portrait/identity pairing and the reserved-field content type.
- **Media slots:** 1 portrait area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (373 visible words)
- **Responsive concern:** NONE
- **Notes:** Reserved fields are a media/claims-policy device, not decoration.

#### ARC-S26-002

- **Section / variant:** S26 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Editorial profile: tall portrait plate beside a quiet identity column and a written statement.
- **What works:** Premium and restrained; the tall plate carries the page.
- **Later correction direction:** Light copy trim only.
- **Must preserve:** The tall portrait plate relationship.
- **Media slots:** 1 portrait plate
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (300 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for S26.

#### ARC-S26-003

- **Section / variant:** S26 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Personnel record: identity band, open field register, stage-involvement table and reserved-fields block.
- **What works:** Rigorous and fully open (nothing hidden behind controls).
- **Problem:** A personnel record with a table and 383 words; the same family the user rejected in S08-003.
- **Later correction direction:** Rework into a portrait-led profile with concise facts.
- **Must preserve:** The involvement-by-stage content, expressed briefly.
- **Media slots:** 1 portrait
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** EXCESSIVE (383 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: matches the pattern the user flagged elsewhere.

#### ARC-S26-004

- **Section / variant:** S26 · 004
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Profile ordered around asking for this person, with help list, alternatives and introduction steps.
- **What works:** Honest routing to another post; clear single route.
- **Problem:** 450 words with one portrait.
- **Later correction direction:** Trim copy; raise media presence.
- **Must preserve:** The 'ask for someone else' routing.
- **Media slots:** 1 portrait area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (450 visible words)
- **Responsive concern:** NONE

#### ARC-S26-005

- **Section / variant:** S26 · 005
- **Status:** `REBUILD`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Bid curriculum sheet: issue line, coverage matrix of project type against stage, verification block.
- **What works:** Distinctive and sector-true; involvement stated in words, not marks.
- **Problem:** A CV sheet with a matrix and revision/issue apparatus — explicitly on the list to avoid.
- **Later correction direction:** Rebuild as a visual profile; the CV-sheet metaphor should not return.
- **Must preserve:** The coverage content as short prose.
- **Media slots:** 1 portrait
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** EXCESSIVE (353 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: CV sheet is named in the avoid list.

### S27 — Studio / Location Detail

#### ARC-S27-001

- **Section / variant:** S27 · 001
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Location page with address, contact and hours above the image, then what happens here and getting here.
- **What works:** Address-first ordering is correct for the role; reserved map slot is honest.
- **Problem:** 351 words with one photographic area.
- **Later correction direction:** Trim copy; raise media presence.
- **Must preserve:** The address-before-media ordering and the reserved map slot.
- **Media slots:** 1 image + 1 map area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (351 visible words)
- **Responsive concern:** NONE

#### ARC-S27-002

- **Section / variant:** S27 · 002
- **Status:** `KEEP`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** The place described as a building: compact address line, lead plate, prose and a plate pair.
- **What works:** Best media presence in S27; premium editorial register.
- **Later correction direction:** Light copy trim.
- **Must preserve:** The compact address line above the lead plate.
- **Media slots:** 3 plates + map
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (331 visible words)
- **Responsive concern:** NONE
- **Notes:** Positive reference for S27.

#### ARC-S27-003

- **Section / variant:** S27 · 003
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Location details sheet: identification band and three tables (contact, hours by day, access and arrival).
- **What works:** Complete operational information; reserved fields instead of invented values.
- **Problem:** Three tables, 448 words and no photography — a record sheet.
- **Later correction direction:** Rework into a visual location page with imagery and a short details block.
- **Must preserve:** The reserved-field discipline for addresses and durations.
- **Media slots:** 1 map area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** EXCESSIVE (448 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: matches the pattern the user flagged in S17-003.

#### ARC-S27-004

- **Section / variant:** S27 · 004
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** NO
- **Current structural concept:** Visit-ordered location page with address inside the decision header and arrangement steps.
- **What works:** Clear visit logic; honest about promising no times.
- **Problem:** 466 words and no photographic media.
- **Later correction direction:** Trim copy; add place imagery.
- **Must preserve:** The visit-first ordering.
- **Media slots:** 1 map area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** LIGHT
- **Text density:** EXCESSIVE (466 visible words)
- **Responsive concern:** NONE

#### ARC-S27-005

- **Section / variant:** S27 · 005
- **Status:** `REWORK`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Arrival key: lettered approach steps keyed to a reserved plan area, with a floor key inside.
- **What works:** Genuinely useful arrival information; letters are text so the sequence survives an empty plan.
- **Problem:** Keyed-plan register and 404 words; close to the key-plan device the user excluded in S22.
- **Later correction direction:** Rework into a visual arrival presentation with photography.
- **Must preserve:** The arrival-sequence content.
- **Media slots:** 1 plan + 1 map area
- **Header/nav contamination:** NO
- **Technical-document metaphor:** HEAVY
- **Text density:** EXCESSIVE (404 visible words)
- **Responsive concern:** NONE
- **Notes:** Additional candidate: keyed-plan family.

### S28 — Blog / Index List Pages (unplanned)

#### ARC-BLOG-LIST-001

- **Section / variant:** S28 · 001
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Events calendar index grouped by month with date columns, tags and a subscribe band.
- **What works:** Strong editorial index; clear date rhythm.
- **Problem:** Carries a full site header, footer and utility navigation inside a section study.
- **Later correction direction:** Remove the global header/footer chrome under the new global rule.
- **Must preserve:** The month grouping and date column.
- **Media slots:** 10 media areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** MODERATE
- **Text density:** HIGH (227 visible words)
- **Responsive concern:** NONE
- **Notes:** Outside the planned S01-S27 catalog; see Global Structural Issues.

#### ARC-BLOG-LIST-002

- **Section / variant:** S28 · 002
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Archive board of event cards with large dates and an advertising slot.
- **What works:** Dense but visual; the date treatment is distinctive.
- **Problem:** Site header and utility navigation; an AD slot inside a section study.
- **Later correction direction:** Remove global chrome; confirm whether an advertising slot belongs in this catalog.
- **Must preserve:** The large-date card treatment.
- **Media slots:** 12 media areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** MODERATE
- **Text density:** MEDIUM (134 visible words)
- **Responsive concern:** NONE
- **Notes:** Outside the planned S01-S27 catalog.

#### ARC-BLOG-LIST-003

- **Section / variant:** S28 · 003
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Nine-card journal grid with date, category chip, title and read-more link.
- **What works:** Clean 3x3 grid, image per card, low copy per card.
- **Problem:** Global header and breadcrumb chrome inside a section study.
- **Later correction direction:** Remove global chrome; otherwise sound.
- **Must preserve:** The 3x3 card grid.
- **Media slots:** 10 media areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (283 visible words)
- **Responsive concern:** NONE
- **Notes:** Outside the planned catalog; the grid is a useful reference for S14's 3x3 target.

#### ARC-BLOG-LIST-004

- **Section / variant:** S28 · 004
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Magazine index with two featured stories above a recent list, closing on a newsletter band.
- **What works:** Good featured/recent hierarchy.
- **Problem:** Global header, footer and subscribe chrome inside a section study.
- **Later correction direction:** Remove global chrome.
- **Must preserve:** The featured/recent hierarchy.
- **Media slots:** 10 media areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** LIGHT
- **Text density:** HIGH (251 visible words)
- **Responsive concern:** NONE
- **Notes:** Outside the planned catalog.

#### ARC-BLOG-LIST-005

- **Section / variant:** S28 · 005
- **Status:** `MINOR_FIX`
- **User explicitly flagged:** NO
- **Additional review candidate:** YES
- **Current structural concept:** Editorial index with a hero story, breaking-news column, flash-news rail, top authors and a banner slot.
- **What works:** Rich magazine composition with strong media presence.
- **Problem:** Global header and footer; invented author names; an advertising banner slot; 339 words.
- **Later correction direction:** Remove global chrome; review the named authors against the media/claims policy.
- **Must preserve:** The hero-plus-rail composition.
- **Media slots:** 13 media areas
- **Header/nav contamination:** YES
- **Technical-document metaphor:** MODERATE
- **Text density:** EXCESSIVE (339 visible words)
- **Responsive concern:** NONE
- **Notes:** Outside the planned catalog. Author names (Laura Bennett, Robert Edition, Daniel Cross, Sophia Turner) are invented people — flag for policy review.

## Additional Review Candidates

These studies were **not** named by the user. They are recorded here because they show the same
pattern the user rejected elsewhere. The status attached to each is this audit's recommendation;
the decision belongs to the user.

| Study | Recommended status | Why it was flagged |
| --- | --- | --- |
| `ARC-S03-003` | REWORK | Each card ends in a specification-style field list (Stages / Output / Typologies). |
| `ARC-S03-005` | REBUILD | Sheet metaphor and the stamped footer register dominate the composition. |
| `ARC-S04-003` | REWORK | Scope field pairs read as a specification list. |
| `ARC-S04-005` | REWORK | Plate-index register and catalogue framing; highest text density in S04. |
| `ARC-S05-003` | REWORK | Six dense rows of prose with only one media area; reads text-first. |
| `ARC-S05-005` | REBUILD | Explicit contract-document metaphor: clause numbering, revision and status stamps. |
| `ARC-S07-005` | REWORK | Colophon framing is a print-document metaphor. |
| `ARC-S08-005` | REBUILD | Register/sheet metaphor; portraits are reduced to labelled cells. |
| `ARC-S10-003` | REWORK | Twenty-four capability lines plus mode stamps read as an inventory document; no media. |
| `ARC-S13-005` | REWORK | Sheet framing, plate references and a change schedule push it into document territory. |
| `ARC-S14-005` | REWORK | Sheet framing, axis labels and 'not to scale' notation. |
| `ARC-S25-001` | MINOR_FIX | Carries a global site header and primary navigation; 379 visible words. |
| `ARC-S25-002` | MINOR_FIX | Publication bar acts as a site header; 398 words with one media area. |
| `ARC-S25-003` | REWORK | Masthead bar plus 461 words and nine stacked regions make it the densest S25 study. |
| `ARC-S25-004` | MINOR_FIX | Global header with a primary nav and a standing CTA; 420 words. |
| `ARC-S25-005` | MINOR_FIX | Category nav acts as a site header; the credits register is a light document device; 373 words. |
| `ARC-S26-003` | REWORK | A personnel record with a table and 383 words; the same family the user rejected in S08-003. |
| `ARC-S26-005` | REBUILD | A CV sheet with a matrix and revision/issue apparatus — explicitly on the list to avoid. |
| `ARC-S27-003` | REWORK | Three tables, 448 words and no photography — a record sheet. |
| `ARC-S27-005` | REWORK | Keyed-plan register and 404 words; close to the key-plan device the user excluded in S22. |
| `ARC-BLOG-LIST-001` | MINOR_FIX | Carries a full site header, footer and utility navigation inside a section study. |
| `ARC-BLOG-LIST-002` | MINOR_FIX | Site header and utility navigation; an AD slot inside a section study. |
| `ARC-BLOG-LIST-003` | MINOR_FIX | Global header and breadcrumb chrome inside a section study. |
| `ARC-BLOG-LIST-004` | MINOR_FIX | Global header, footer and subscribe chrome inside a section study. |
| `ARC-BLOG-LIST-005` | MINOR_FIX | Global header and footer; invented author names; an advertising banner slot; 339 words. |

## Global Structural Issues

1. **The sector-native territory has collapsed into one register.** Across S01, S03, S05, S06,
   S08, S09, S10, S11, S12, S13, S14, S15, S17, S18, S19, S20, S22, S23, S24, S26 and S27 the 005
   study is a document of some kind. The territory label asks for *sector-native*; the catalog
   answered *architectural paperwork* almost every time.

2. **`standards/01-AUTHORING-STANDARD.md` does not constrain visual register.** It requires the
   five studies to differ structurally and warns against cosmetic variation, but sets no ceiling on
   document metaphors or text density. The failure pattern is compliant with the standard as
   written. Changing the standard is a Phase 1 decision and is deliberately not made here.

3. **Header/navigation contamination has two different causes.** In S01 the header was authored
   into a hero section. In S25 and S28 it came from reference images the user supplied and asked to
   be followed closely. Global rule 5 and the earlier 'follow the references' instruction point in
   opposite directions for those ten studies; this document records the conflict rather than
   resolving it.

4. **`S28-blog-list-pages` is outside the allocated catalog.** `standards/02-NAMING-AND-ID-STANDARD.md`
   states that S28 and above are reserved, not allocated and not created. Five studies exist there
   with IDs `ARC-BLOG-LIST-001..005`, which also do not follow the `ARC-S<NN>-<VVV>` ID rule. This
   is a governance question — does the section exist, under what number, with what IDs — and it
   should be answered before any design decision about those five files.

5. **Text density rises sharply in the extended detail-page sections.** S01–S20 average 137
   visible words per study and S21–S22 average 97, but S23–S27 average 414 — three times the
   sector-core figure. The detail-page roles were authored as documents to read rather than pages
   to look at, which is precisely the S23 complaint, and it repeats in S25, S26 and S27.

6. **Media absence is concentrated.** 42 studies carry no reserved media area at all. Some of that
   is legitimate — S19, S20 and S22 are form, invitation and breadcrumb roles where media is not
   expected — but the rest is not: S09 (4 of 5), S10 (5 of 5), S15 (3 of 5), S18 (4 of 5) and
   S21 (4 of 5, where an image-background hero is now explicitly wanted). A section with no media
   slot cannot become image-led without new slots being introduced during correction.

7. **One study carries invented personal names.** `ARC-BLOG-LIST-005` lists four named authors.
   Every other study in the sector uses tokens (`Team member 01`, `Author 01`). Flagged for
   media/claims-policy review, not for design review.

## Positive Reference Studies

Studies that already demonstrate the direction the user asked for. These should be the reference
points when the flagged studies are corrected.

| Study | Why it is a reference |
| --- | --- |
| `ARC-S01-002` | Full-bleed media field with a display headline and minimal copy — the hero direction, once the header is removed. |
| `ARC-S02-001` | Editorial project grid: asymmetric, image-led, almost no text. |
| `ARC-S02-004` | Collage of unequal frames with a vertical display word; visually distinctive without any document language. |
| `ARC-S03-002` | Serif display heading over four labelled image cards; premium and low-copy. |
| `ARC-S04-001` | Typologies carried entirely by type and one tall media panel. |
| `ARC-S05-002` | Oversized lowercase wordmark as the whole composition. |
| `ARC-S06-002` | Numerals, serif stage headings and one image per stage — the model for reworking S06-003 and S06-005. |
| `ARC-S07-001` | Scattered image areas with a short statement; the most whitespace-confident study in the sector. |
| `ARC-S07-002` | Display title plus principal plate; premium editorial about-page. |
| `ARC-S08-006` | Featured portrait plate above a thumbnail strip; clear hierarchy without a register. |
| `ARC-S09-002` | Tear-sheet plate beside a short record list — proof that recognition can be visual. |
| `ARC-S10-004` | Three entry routes in plain language; the strongest conversion logic in the sector. |
| `ARC-S11-002` | Material board of sample areas with four short questions. |
| `ARC-S13-002` | Held plate beside a moving account; a genuinely premium case-study device. |
| `ARC-S15-002` | Three fields with large numerals and generous image blocks. |
| `ARC-S16-002` | Journal issue page: one long read plus three image cards. |
| `ARC-S19-002` | Three questions and one action; premium restraint in a form role. |
| `ARC-S24-001` | Portfolio-shaped case study with a large lead image and three chapters. |
| `ARC-S25-005` | Mixed-scale serif title with an unequal plate pair; best media rhythm in the extended sections. |
| `ARC-S26-002` | Tall portrait plate beside a quiet identity column. |
| `ARC-S27-002` | Place described as a building, with three plates and a compact address line. |

## Responsive Issues

| Study | Severity | Finding |
| --- | --- | --- |
| `ARC-S08-007` | CONFIRMED | Reported broken on desktop, tablet and mobile. Root cause: the composition is an expanding filmstrip whose unselected panels are fixed 42–96px slivers. With reserved media areas empty — the workspace's normal state — those slivers render as blank columns at every width, and the strip overflows rather than reflowing at narrow widths. The failure is conceptual as well as responsive, which is why it is classified `REBUILD` rather than `BUG_FIX`. |
| `ARC-S08-008` | POSSIBLE | Cards bleed past the viewport edge by design; the horizontal scroll affordance should be verified on tablet before it is trusted. |
| `ARC-S08-009` | POSSIBLE | Lead card plus buttoned rail; rail behaviour at tablet width should be verified. |

No other study showed a confirmed responsive failure in this audit. All 146 studies declare the
1280 / 1024 / 768 / 480 / 360 breakpoint ladder. Rendering verification in real browsers at 1440,
1280, 1024, 768, 430, 390 and 320 was **not** performed in Phase 0 and remains outstanding.

## Media Slot Notes

Empty reserved media areas were treated as intentional throughout this audit, in line with the
media policy and with the user's global note 7. No study was downgraded because a slot is empty,
and no correction direction in this document proposes filling a slot with invented imagery.

Reserved area labels found in the catalog: `IMAGE AREA`, `PLATE AREA`, `PORTRAIT AREA`,
`SAMPLE AREA`, `SAMPLE BOX AREA`, `MAP AREA`, `FILM AREA`, `TEAR SHEET AREA`, `PLAN AREA`,
`FRAME 01–18`, `DRAWING 01/02`, `MEDIA PENDING`.

Two related observations that are about **absence of slots**, not about empty slots:

- 42 studies define no media area at all. In S19, S20 and S22 that is appropriate to the role; in
  S09, S10, S15, S18 and S21 it is the reason those sections cannot become image-led without new
  slots being introduced during correction.
- The map and plan areas in S27, and the reserved-field registers in S26, are policy devices —
  they exist so that addresses, coordinates and credentials are never invented. They should survive
  any visual rework as content types even if their presentation changes completely.

## Phase 1 Inputs

Carried forward as inputs, not as decisions:

1. **Correction queue by severity.** REBUILD first (role misunderstandings and document
   metaphors), then REWORK, then MINOR_FIX (header removal and copy trims).
2. **Three role clarifications to apply before any redesign:** S21 as conventional internal-page
   heroes, S22 as conventional breadcrumbs, S23 to the clarified content balance.
3. **A standards question:** whether `01-AUTHORING-STANDARD.md` should constrain visual register
   and text density for the 003 and 005 territories. Not changed in Phase 0.
4. **A governance question:** whether `S28-blog-list-pages` exists, under what section number, and
   with what study IDs.
5. **A conflict to resolve:** global rule 5 (remove headers) against the earlier instruction to
   follow supplied references closely in S25 and S28.
6. **An explicit numeric target:** S14-003 to 3×3 = 9 gallery images; whether the same cap applies
   to the rest of S14 is an open question.
7. **Media slots to introduce** in sections that currently have none, if those sections are to
   become image-led.
8. **Batch documents will need updating** after corrections; they are untouched in Phase 0.

## Explicitly Out of Scope

- Any change to authored `.html` studies.
- Any change to `BATCH-V1.md` files, section READMEs, the sector README or `SECTOR-BRIEF.md`.
- Any change to `standards/`.
- Any change to the variant/territory system.
- Regenerating the review contact sheet.
- Design Lab, the promotion pipeline, screenshots and media assets.
- Review, normalisation, survivor-selection and promotion decisions, which belong to Design Lab.

---

**NO DESIGN FILE WAS MODIFIED IN PHASE 0.**
