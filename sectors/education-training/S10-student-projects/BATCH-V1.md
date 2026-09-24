# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S10
- Section Name: Student Projects
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 50 studies, S01-S10 authored.

## Planned Studies

All five studies are AUTHORED; raw filenames match study IDs.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S10-001 | Universal / Safe | Apricot | A | 3 | 152 / 188 | Three open project columns with generous landscape images |
| EDU-S10-002 | Premium / Editorial | Mulberry | A | 3 | 152 / 188 | Featured horizontal project above two supporting works |
| EDU-S10-003 | Structured / Visual Modular | Cobalt | A | 3 | 152 / 188 | Side introduction beside three horizontal project modules |
| EDU-S10-004 | Conversion-led | Iris | A | 3 | 152 / 188 | Large featured project beside two compact works |
| EDU-S10-005 | Art-directed / Distinctive | Afterhours | A | 3 | 152 / 188 | Staggered dark gallery with varied image proportions |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S08/S09 raw studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Three reserved projects demonstrate the gallery capacity. Each has a programme,
project type, title, short description, student/team attribution and study period.
Native disclosures reserve the brief, methods, student contribution, reflection
and context. All project-specific text remains bracketed and data-placeholder marked.
A visible notice states that work and credits await confirmation.

No student work, identity, award, client, result or assessment grade is invented.
Actual project text and media need verified provenance, correct attribution and
permission before publication. The gallery is a project overview; no unauthored
case-detail route, fake media viewer or download is implied. The catalogue link
reaches the matching existing S02 raw study, as a review route.

Composition, grouping, image scale and information placement distinguish the designs.
Copy quantity remains consistent. No technical document or classical academic metaphor.

## Responsive and Interaction Decisions

- 001: three equal columns stack on smaller screens, keeping each project image and information together.
- 002: a wide featured project leads two supporting projects. Tablet uses a single sequence;
  phones stack each image above its description.
- 003: a side introduction accompanies three horizontal modules; tablet moves the introduction first,
  and phone modules stack their images above content.
- 004: a featured project spans two compact supporting works. Its purple process control
  remains prominent when projects stack on phones.
- 005: varied image heights and staggered positions create a dark gallery; smaller screens
  release the offsets and phones use consistent image heights.

Three independent native details/summary controls can remain open together.
Plus indicators rotate when expanded. Each article is named by its project H3.
Controls have visible focus treatment and at least 44px height.

S08 shapes: C / B / C / C / B. S09: A / A / A / A / A.
S10: A / A / A / A / A. This is the second consecutive A section for every variant;
S11 must use B or C to break the run. Manual comparison used; the CONS-specific
composition checker does not validate education studies.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosures provide interaction.
- Gallery JavaScript: local selection, preview widths and frame height handling.

## Media Slots

Each study reserves Student project 1, Student project 2 and Student project 3:
15 areas total. Purpose: present verified images of the eventual actual work.
Expected type: project photograph, artwork or screenshot with permission and attribution.
Fallback: visibly labelled empty figures with accessible reserved-project descriptions.
Empty media slots are intentional. Do not substitute invented student work or generated
projects for authentic evidence. Actual media needs accurate alternative text.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with all process disclosures closed or open.
- Metadata, unique IDs, section region, H2, three articles, H3 headings and media slots checked.
- Native disclosures open and close; focusability and minimum target height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded visible copy: 188 words per study.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, variant filtering, mobile width, pressed states,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five project galleries](../../../review/education-projects.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-projects.ps1

Measured heights: ../../../review/education-projects-heights.json.
Next: S11-accreditations.
