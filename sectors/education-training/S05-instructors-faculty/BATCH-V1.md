# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S05
- Section Name: Instructors Faculty
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 25 studies, S01-S05 authored.

## Planned Studies

All five studies are AUTHORED. Each raw filename matches its study ID.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S05-001 | Universal / Safe | Apricot | A | 3 | 128 / 158 | Three equal portrait cards with open profile text |
| EDU-S05-002 | Premium / Editorial | Mulberry | A | 3 | 128 / 158 | Featured portrait beside two compact editorial profiles |
| EDU-S05-003 | Structured / Visual Modular | Cobalt | A | 3 | 128 / 158 | Introductory side column beside three horizontal faculty modules |
| EDU-S05-004 | Conversion-led | Iris | A | 3 | 128 / 158 | Open portrait columns with prominent background controls |
| EDU-S05-005 | Art-directed / Distinctive | Afterhours | A | 3 | 128 / 158 | Staggered dark portrait gallery with contrasting curved crops |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S03 and S04 batch records and raw studies;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Three reserved faculty records demonstrate the section capacity. Each includes
name, subject area, teaching role, subject focus and teaching approach. Native
disclosures reserve verified experience, qualifications and programme responsibilities.
No real faculty information was supplied. All person-specific text is bracketed
and marked data-placeholder. Names, identities, credentials and employment history
are not invented. Portraits are intentionally empty.

This is a faculty overview. S26 is still scaffolded, so no profile-detail navigation
is implied. Background information opens locally. The catalogue link reaches the
existing matching S02 study and does not imply a verified instructor assignment.

The five designs differ through grouping, prominence, column proportions, portrait
crops and placement of introductory content. The same concise content is retained.
No academic crests, faux certificates, technical documents or classical decoration.

## Responsive and Interaction Decisions

- 001: three equal columns become horizontal profiles on tablets, then image-above-text on phones.
- 002: one featured profile accompanies two compact profiles; tablets and phones restore a linear sequence.
- 003: a desktop side introduction leads three horizontal modules; tablet puts the introduction first,
  and phone modules stack portraits above the text.
- 004: split introductory text leads three open portrait columns. Purple background controls remain
  prominent as the profiles stack on smaller screens.
- 005: desktop portrait offsets and different curves create an asymmetric gallery;
  tablet offsets release and phones show each complete profile in sequence.

Each profile has an independent native details/summary disclosure. All three can
remain open. The plus indicator rotates when expanded. Summary and catalogue controls
have visible focus treatment and at least 44px height.

S03 shapes: C / B / A / C / B. S04: B / B / C / C / B.
S05: A / A / A / A / A. No consecutive A run exists at S05.
Manual comparison used; the CONS-specific composition checker does not validate education.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosures provide the required interaction.
- Gallery JavaScript: local preview selection, viewport width and height handling.

## Media Slots

Each study has Instructor portrait 1, Instructor portrait 2 and Instructor portrait 3:
15 reserved areas total. Purpose: associate each eventual instructor with their profile.
Expected type: verified portrait of the actual instructor, with appropriate consent.
Fallback: labelled empty figures with accessible reserved-portrait descriptions.
No generated faces, remote portraits or invented people. Actual media requires
provenance, permission and accurate alternative text.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with all profile disclosures closed or open.
- Metadata, unique IDs, region and section H2 checked; three named profile articles,
  three H3 headings and three reserved portraits in every study.
- Native disclosures open and close; keyboard focusability and minimum control height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded visible copy: 158 words per study.
- No raw scripts, frameworks, remote assets or global shell.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- Gallery passed: five frames, variant filtering, mobile width, pressed state,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run; Design Lab ingestion not performed.

## Review

[Compare five faculty designs](../../../review/education-faculty.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-faculty.ps1

Measured heights: ../../../review/education-faculty-heights.json.
Next: S06-curriculum-learning-path.
