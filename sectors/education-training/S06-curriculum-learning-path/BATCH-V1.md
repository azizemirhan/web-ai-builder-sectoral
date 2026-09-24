# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S06
- Section Name: Curriculum Learning Path
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 30 studies, S01-S06 authored.

## Planned Studies

All five studies are AUTHORED. Each raw filename matches its study ID.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S06-001 | Universal / Safe | Apricot | C | 0 | 86 / 140 | Continuous vertical learning sequence beside introductory content |
| EDU-S06-002 | Premium / Editorial | Mulberry | B | 1 | 90 / 144 | Editorial curriculum list paired with a tall practice photograph |
| EDU-S06-003 | Structured / Visual Modular | Cobalt | C | 0 | 86 / 140 | Oversized stage numbers across an open horizontal path |
| EDU-S06-004 | Conversion-led | Iris | C | 0 | 86 / 140 | Purple programme context beside spacious stage disclosures |
| EDU-S06-005 | Art-directed / Distinctive | Afterhours | B | 1 | 90 / 144 | Dark asymmetric learning path with curved practice imagery |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S04 and S05 raw/batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Four illustrative stages show how a curriculum can progress from introductory topics
through practice, application and review. Programme name, stage titles, content,
modules, activities, workload, duration and format remain bracketed placeholders
with data-placeholder markers. No curriculum was supplied, and the visible label
identifies this as an illustrative sequence. No invented dates, credits, qualification,
completion percentage or guaranteed outcome.

The section describes curriculum progression rather than a personal progress tracker.
Stage numbers indicate order, not completion. There are no checked milestones or
fabricated learning status. The programme catalogue link reaches the matching S02
raw study. This is a review route, not a production curriculum URL.

Visual differences come from sequence orientation, scale, grouping, media placement
and the role of colour. Short closed copy makes the path scannable; opening stages
reveals the content without exceeding the copy ceiling.

## Responsive and Interaction Decisions

- 001: a continuous vertical sequence accompanies a side introduction. Phones stack
  the introduction and path, keeping expanded content clear of the connecting line.
- 002: a tall photo accompanies open stage rows. Phones put stages before the image.
- 003: a four-stage horizontal typographic path becomes two columns on tablets and
  one on phones. The duration, decision note and catalogue route also stack.
- 004: a purple programme context field sits beside the path; phones place it first.
- 005: a curved media area accompanies the dark sequence and follows it on phones.

Each stage uses native details/summary and can open independently; all four can
remain open. Plus indicators rotate on expansion. An ordered list preserves the
sequence. All controls have visible focus treatment and at least 44px target height.

S04 shapes: B / B / C / C / B. S05: A / A / A / A / A.
S06: C / B / C / C / B. No consecutive A run continues into S06.
Variant 003 is an open typographic sequence, with no repeated media or card grid.
Manual composition comparison used; the CONS-specific checker does not validate education.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosures provide interaction.
- Gallery JavaScript: local variant selection, preview widths and frame height handling.

## Media Slots

| Study | Slot | Purpose / expected type | Accessibility / fallback |
| --- | --- | --- | --- |
| 001 | None | Typography and the connected sequence carry the design | No media required |
| 002 | Practical learning in progress | Verified contextual photograph | Labelled reserved figure and accessible description |
| 003 | None | Oversized numbers and open stage typography carry the design | No media required |
| 004 | None | Coloured programme context and stage sequence carry the design | No media required |
| 005 | Practical learning in progress | Verified contextual photograph | Labelled reserved figure and accessible description |

Two reserved photo areas total. Empty media slots are intentional. Actual imagery
requires provenance, permission and accurate alternative text. No generated faces,
invented learner work or remote assets.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with all four stage disclosures closed or open.
- Metadata, unique IDs, section region, H2 and four ordered stages checked.
- Native disclosures open and close; focusability and minimum control height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded visible copy: 140-144 words.
- Scoped CSS, explicit border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, variant filtering, mobile width, pressed states,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five curriculum designs](../../../review/education-curriculum.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-curriculum.ps1

Measured heights: ../../../review/education-curriculum-heights.json.
Next: S07-admissions-enrollment.
