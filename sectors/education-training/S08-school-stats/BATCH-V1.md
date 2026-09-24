# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S08
- Section Name: School Stats
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 40 studies, S01-S08 authored.

## Planned Studies

All studies are AUTHORED; raw filenames match study IDs.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S08-001 | Universal / Safe | Apricot | C | 0 | 97 / 116 | Four large figures across an open statistical strip |
| EDU-S08-002 | Premium / Editorial | Mulberry | B | 1 | 100 / 119 | Editorial photo beside two-by-two statistics |
| EDU-S08-003 | Structured / Visual Modular | Cobalt | C | 0 | 97 / 116 | Featured learner figure beside three compact measures |
| EDU-S08-004 | Conversion-led | Iris | C | 0 | 97 / 116 | Purple statistics field beside context and catalogue route |
| EDU-S08-005 | Art-directed / Distinctive | Afterhours | B | 1 | 100 / 119 | Offset dark statistics beside a curved photograph |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S06/S07 studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Four measures reserve learner, programme, teaching-team and learning-location counts.
No institutional figures were supplied. Each value is [—], marked data-placeholder,
with a measure-specific pending-confirmation label. Definitions and reporting period
remain reserved. A visible notice explains that the figures await confirmation.
No fabricated numbers, success rates, rankings, employment claims or animated counters.

Each definition list pairs a measure with its value and scope. A native disclosure
reserves source records, counting methods, exclusions, deduplication and verification
dates for each measure. The copy distinguishes institutional scale from individual
outcomes. Real figures require verified source data before publication.

Composition, scale, grouping and media placement distinguish the five studies.
The same concise content is used throughout. No technical dashboard or classical
institutional document metaphor is used.

## Responsive and Interaction Decisions

- 001: four open columns become two on tablets and one on phones, retaining divider padding.
- 002: a tall photo accompanies a two-by-two group; phones stack the measures before media.
- 003: a featured learner figure spans the height of three compact measures;
  phones show the feature followed by each measure in order.
- 004: the purple statistics field sits beside context; phones show context followed by the field.
- 005: alternating desktop offsets release on phones, with the curved image following the measures.

Each source disclosure opens locally without JavaScript. The catalogue link reaches
the matching existing S02 raw study; these are review routes, not production URLs.
No invented download, source URL or reporting dashboard is provided.

S06 shapes: C / B / C / C / B. S07: C / B / C / C / B.
S08: C / B / C / C / B. No consecutive A run exists. Media-free layouts use
typographic measures rather than repeated media cards. Manual comparison used;
the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosure provides interaction.
- Gallery JavaScript: local selection, preview width and height handling.

## Media Slots

002 and 005 each reserve one Shared learning environment photograph: two areas total.
Purpose: give context to institutional scale through verified learning-space imagery.
Expected type: photograph of an actual institutional learning environment, with provenance,
permission and accurate alt text. Fallback: labelled empty figure with accessible description.
001, 003 and 004 use typography and colour, so no media is needed.
Empty slots are intentional. No remote assets or generated identities included.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with source disclosures closed or open.
- Metadata, unique IDs, section region, H2, four measures and explicit pending values checked.
- Native disclosures open and close; focusability and minimum 44px control height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and mobile screenshots reviewed; mobile metric spacing and size refined.
- Expanded copy: 116-119 words.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, variant filtering, mobile width, pressed states,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five statistics designs](../../../review/education-stats.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-stats.ps1

Measured heights: ../../../review/education-stats-heights.json.
Next: S09-student-testimonials.
