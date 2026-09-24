# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S04
- Section Name: Learning Outcomes
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 20 studies, S01-S04 authored.

## Planned Studies

All five studies are AUTHORED. Each raw filename matches its study ID.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S04-001 | Universal / Safe | Apricot | B | 1 | 110 / 119 | Broad practical-learning photograph with open numbered outcomes |
| EDU-S04-002 | Premium / Editorial | Mulberry | B | 1 | 110 / 119 | Editorial outcome pairs beside a tall photograph |
| EDU-S04-003 | Structured / Visual Modular | Cobalt | C | 0 | 107 / 116 | Oversized learning verbs in an open typographic sequence |
| EDU-S04-004 | Conversion-led | Iris | C | 0 | 107 / 116 | Purple statement and catalogue route beside a capability stack |
| EDU-S04-005 | Art-directed / Distinctive | Afterhours | B | 1 | 110 / 119 | Asymmetric dark composition with a curved photograph |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S02 and S03 batch records and raw studies;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Four outcome dimensions demonstrate the content structure: understand, apply,
communicate and reflect. The programme name and specific capabilities remain
bracketed placeholders. A visible example label makes the illustrative scope clear.
No supplied programme data, credential, employment promise or success statistic exists.
The assessment disclosure reserves the actual task, evidence and criteria.
Course-specific outcomes must be supplied before publication.

The five designs vary in hierarchy, grouping, media proportions and placement,
and the role of the accent field. Copy volume stays consistent and concise.
No classical academic decoration or technical document metaphor is used.

## Responsive and Interaction Decisions

- 001: open outcome rows accompany a broad image; on phones, information precedes media.
- 002: a two-by-two group accompanies a tall image; phones show outcomes in order,
  followed by the image and assessment context.
- 003: the introduction sits beside large learning verbs; phones stack the two areas.
- 004: the purple introduction includes assessment and a catalogue route; the outcome
  list follows this field on phones.
- 005: a curved image and lime outcome headings form an asymmetric split; phones
  place the image after the learning information.

Each study has one native details/summary assessment disclosure, initially closed,
and a native link to its matching existing S02 programme study. The links are review
routes, not production course URLs. No JavaScript is required inside the raw studies.

S02 shapes: A / A / A / A / A. S03: C / B / A / C / B.
S04: B / B / C / C / B. S04-003 breaks the preceding pair of A sections.
Manual composition comparison used; no claim of education validation by the
CONS-specific composition checker.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native controls provide the interaction.
- Gallery JavaScript: local preview selection, viewport width and frame height handling.

## Media Slots

| Study | Slot | Purpose / expected type | Accessibility / fallback |
| --- | --- | --- | --- |
| 001 | Practical learning work | Verified photograph of relevant learning practice | Labelled reserved figure with accessible description |
| 002 | Practical learning work | Verified photograph of relevant learning practice | Labelled reserved figure with accessible description |
| 003 | None | Large typography carries the composition | No media required |
| 004 | None | The coloured introduction and outcomes carry the composition | No media required |
| 005 | Practical learning work | Verified photograph of relevant learning practice | Labelled reserved figure with accessible description |

Three media areas total. Empty media slots are intentional. Actual learning-work
photographs need provenance, permission and accurate alt text. No remote imagery,
invented student work or generated faces included.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with assessment disclosures closed or open.
- Study metadata, unique IDs, region and section H2 checked; no global shell.
- Native disclosures open and close; focusability and minimum 44px control height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded visible copy: 116-119 words, within the copy ceiling.
- No raw scripts, frameworks, remote assets or runtime dependencies.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- Gallery passed: five frames, variant selection, mobile width, pressed states,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content space when local-file access blocks live sizing.
- Cross-browser and screen-reader testing not run; Design Lab ingestion not performed.

## Review

[Compare the five outcome designs](../../../review/education-outcomes.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-outcomes.ps1

Measured heights: ../../../review/education-outcomes-heights.json.
Next: S05-instructors-faculty.
