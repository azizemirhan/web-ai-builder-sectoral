# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S02
- Section Name: Programs Courses
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 10 studies, S01-S02 authored.

## Planned Studies

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S02-001 | Universal / Safe | Apricot | A | 3 | 133 / 160 | Three equal media-led programme cards |
| EDU-S02-002 | Premium / Editorial | Mulberry | A | 3 | 133 / 160 | Featured horizontal programme above two compact courses |
| EDU-S02-003 | Structured / Visual Modular | Cobalt | A | 3 | 133 / 160 | Introductory side column beside joined programme modules |
| EDU-S02-004 | Conversion-led | Iris | A | 3 | 140 / 167 | Open comparison columns with prominent information controls |
| EDU-S02-005 | Art-directed / Distinctive | Afterhours | A | 3 | 133 / 160 | Staggered dark course gallery with alternating image shapes |

## Research and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; preceding S01 raw/batch records.
External research: NONE. Document-metaphor justification: NONE.

Three reserved programme records demonstrate capacity in each design. Each contains
subject, programme title, focus/audience, format, duration, entry requirements,
full fees and next start. No actual programme or institution data was supplied.
All programme-specific text uses explicit bracketed placeholders and data-placeholder
markers. No course, accreditation, outcome, entry condition, fee or date is invented.

The section is a programme overview, not a category index or a complete course detail
page. There are no invented search results, meaningless filters or fake enrolment
actions. Three records are enough to show hierarchy without filling the screen with
a repetitive catalogue. The five compositions differ in grouping, proportions and
media arrangement, not copy quantity.

## Responsive and Interaction Decisions

- 001: three equal cards become a single column below 760px.
- 002: the featured programme spans the opening row. Two compact image-and-text
  programmes follow; tablet becomes a single row sequence, then phones stack
  each image above its associated content.
- 003: the introduction is a desktop side column; below 1100px it leads the joined
  modules. Below 760px modules stack. Format and duration align side by side on phones.
- 004: the introductory decision note accompanies open programme columns. Information
  controls receive the accent fill. Phones show complete programmes in sequence.
- 005: desktop cards have staggered positions and different image crops. On phones
  the offsets release and all programme information stays with the matching image.

Native details/summary elements reveal entry, fees and start-date fields without
JavaScript. Each programme can be opened independently; all can stay open together.
The plus rotates when expanded. No modal or external navigation is needed to compare
the reserved information. The overview retains visible format/duration when closed.

S01 shape row: B / B / B / C / B. S02: A / A / A / A / A.
This is the first item-grid section; no consecutive A run exists. S01 is the only
preceding education section. The CONS-specific composition checker is not used
to claim education validation.

## Media Register

Fifteen reserved photo areas total: each study has Learning studio,
Practical learning space and Shared study space, one per programme.
Purpose: relate programme content to its actual learning context.
Expected type: verified photographs associated with the eventual real programme.
Fallback: labelled empty figures preserve the composition and remain understandable.
All areas have visible captions and accessible reserved-photo labels.
No generated faces, invented student work or remote assets. Actual imagery needs
provenance, permission and accurate alt text.

## S01 Connection

S01's temporary catalogue-status disclosures are now native links to the matching
S02 raw study. The hero's visual design remains; its CTA reaches this catalogue.
All five destinations exist and match the variant. These are review routes,
not production URLs. Neither destination claims that reserved programmes are available.

## QA

- S02: 20 Chrome viewport checks at 1440, 768, 390 and 320px.
- No document/element overflow with all programme disclosures closed or open.
- Stable IDs, unique IDs, one section H2 and three programme articles.
- Native disclosures open and close; keyboard focus and 44px minimum controls checked.
- All five desktop and 390px screenshots reviewed; mobile fact alignment refined.
- All-expanded word count stays below 250.
- Gallery: five previews, variant filtering, mobile width, pressed state,
  restore-all and full-size links passed.
- S01 CTA integration: 20 viewport checks, focus/target size and matching routes checked.
- Cached S02 gallery heights reserve room for all disclosures open when local-file
  permissions prevent live measurement.
- No raw JavaScript, framework, remote asset or global shell.
- Reduced-motion CSS included; git diff --check has no whitespace errors.
- Cross-browser and screen-reader testing not run. No Design Lab ingestion claimed.

## Review

[Compare five programme layouts](../../../review/education-programmes.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-programmes.ps1

Measured heights: ../../../review/education-programmes-heights.json.
Next: S03-course-categories.

