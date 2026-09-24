# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S09
- Section Name: Student Testimonials
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 45 studies, S01-S09 authored.

## Planned Studies

All five studies are AUTHORED; raw filenames match study IDs.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S09-001 | Universal / Safe | Apricot | A | 3 | 136 / 160 | Three warm quotation cards with compact portraits |
| EDU-S09-002 | Premium / Editorial | Mulberry | A | 3 | 136 / 160 | Featured editorial story above two supporting voices |
| EDU-S09-003 | Structured / Visual Modular | Cobalt | A | 3 | 136 / 160 | Side introduction beside three horizontal story modules |
| EDU-S09-004 | Conversion-led | Iris | A | 3 | 136 / 160 | Purple featured quotation beside two open perspectives |
| EDU-S09-005 | Art-directed / Distinctive | Afterhours | A | 3 | 136 / 160 | Staggered dark stories with varied curved portrait crops |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S07/S08 raw studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Three reserved student reflections demonstrate programme choice, the learning
experience and study routines. All quotation text is an explicit bracketed content
placeholder, not an invented endorsement. Names, programme, study period, learning
context and reflection date also remain reserved. A visible notice states that
testimonials await confirmation. No actual student testimony was supplied.

No invented identity, rating, success story, employer, salary, graduation result or
employment guarantee. Before publication, each quotation must be supplied by its
actual author, checked against the source and used with appropriate permission.
Portrait and attribution consent must also be established. The generic closing
note makes clear that a story represents an individual experience.

Each story is a named article with a blockquote and student-name H3. Native story
context disclosures reveal additional reserved context. The catalogue link reaches
the matching existing S02 raw study; it is a review route, not a production URL.
There are no fabricated video controls, carousel pages or full-story destinations.

Visual variation comes from grouping, quote scale, portrait proportions, colour
and placement of introductory content. Copy quantity stays consistent.

## Responsive and Interaction Decisions

- 001: three equal quotation cards become a single column, keeping portrait and attribution together.
- 002: a large editorial story leads two supporting stories; tablet restores a single sequence,
  and phones place compact portraits above each quotation.
- 003: a side introduction accompanies horizontal modules; tablets move the introduction first,
  and phones stack each portrait and story inside its module.
- 004: a purple featured story spans two supporting perspectives on desktop;
  phones show the feature and then both supporting stories in order.
- 005: staggered portrait-led columns become a linear sequence; phone portraits are compact.

Three independent details/summary controls can remain open together. Plus indicators
rotate when expanded. Controls include visible focus treatment and at least 44px height.

S07 shapes: C / B / C / C / B. S08: C / B / C / C / B.
S09: A / A / A / A / A. This starts a new A run, with no consecutive grid section.
Manual composition comparison used; the CONS-specific checker does not validate education.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosures provide interaction.
- Gallery JavaScript: local variant selection, preview widths and frame height handling.

## Media Slots

Each study reserves Student portrait 1, Student portrait 2 and Student portrait 3:
15 areas total. Purpose: associate a real student with their eventual approved reflection.
Expected type: verified portrait with appropriate permission. Fallback: visibly labelled
empty portrait area with an accessible reserved-portrait description. Empty areas are
intentional. No generated faces, remote portraits or invented students included.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with all three disclosures closed or open.
- Metadata, unique IDs, section region, H2, three named articles, H3 headings,
  reserved blockquotes and portrait areas checked.
- Native disclosures open and close; focusability and minimum target height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded visible copy: 160 words per study.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, variant filtering, mobile width, pressed states,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five testimonial designs](../../../review/education-testimonials.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-testimonials.ps1

Measured heights: ../../../review/education-testimonials-heights.json.
Next: S10-student-projects.
