# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S21
- Section Name: Subpage Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 105 studies, S01-S21 authored.

## Planned Studies

All five studies are AUTHORED. Variants 001, 002 and 005 contain 47 visible words;
003 and 004 contain 44. The inherited scaffold territory names are updated to the
current authoring standard for 003 and 005.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S21-001 | Universal / Safe | Apricot | B | 1 | Clear admissions page title beside a contained welcome photograph |
| EDU-S21-002 | Premium / Editorial | Mulberry | B | 1 | Editorial page heading above a shallow panoramic welcome image |
| EDU-S21-003 | Structured / Visual Modular | Cobalt | C | 0 | Blue title field alongside contextual application guidance |
| EDU-S21-004 | Conversion-led | Iris | C | 0 | Purple page-title band above a focused application handoff |
| EDU-S21-005 | Art-directed / Distinctive | Afterhours | B | 1 | Large dark page title with a compact curved welcome photograph |

## Research Metadata and Scope

Sources: user continuation request; section README and its universal S21 role;
sector brief; ../EDUCATION-THEME-CONTRACT.md; preceding S19/S20 batch records;
existing S07 admissions guide; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

All variants represent the Admissions & enrolment internal page. Study information
provides category context; the title identifies the page immediately. A short
introduction frames application preparation. A concise scope line identifies
application preparation, programme requirements and enrolment steps.

The single Read the admissions guide link reaches the matching existing S07 study
as a local review handoff. No application is submitted. Replace this route with
the verified page-body destination when integrating. No competing CTA, breadcrumb,
global navigation, homepage positioning or detailed admissions body is included.
No dates, fees, admission guarantees or institution-specific policies are invented.

## Responsive and Interaction Decisions

- 001: page title and context beside a contained rounded welcome-space photograph.
- 002: large editorial title alongside context above a shallow panoramic image.
- 003: a blue title field beside application context, single action and scope.
- 004: a purple title band above an introduction and focused guide handoff.
- 005: large dark page typography beside a compact curved image; context and action
  sit beneath the title at desktop width.

All phone layouts keep the title and context before media, and the single action
takes available width. Scope text wraps without truncation. Media reduces to 210px
height on phones; no large homepage-style stage is introduced.

Each study has one labelled section, one H2 and one contextual link, following the
catalogue heading convention. No other heading, article, disclosure or global shell.
Controls have visible keyboard focus, at least 44px height and reduced-motion treatment.

S19: B / B / C / C / B. S20: C / B / C / C / B.
S21: B / B / C / C / B. This is a separate internal-page role; the preceding shapes
were reviewed for theme continuity rather than as a requirement to append it to a home page.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, preview widths and iframe height handling.

## Media Slots

Three total: one reserved admissions welcome-space photograph in 001, 002 and 005.
Each has a visible caption and accessible reserved-image description. Use actual
institution imagery with appropriate permissions and descriptive alt text before
publication. The labelled slot stays reserved without a file and page context remains
understandable. 003 and 004 demonstrate the internal-page hero without media.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow.
- Metadata, unique IDs, accessible H2, one contextual route and media counts checked.
- Link accepts keyboard focus and has at least 44px height.
- Matching S07 destinations exist.
- Five desktop and five 390px screenshots visually reviewed.
- Every study fits the 40-90-word hero budget.
- Scoped CSS and theme variables, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size links
  and restoration of all previews.
- Measured heights support local-file previews when live sizing is unavailable.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five subpage heroes](../../../review/education-subpage-hero.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-subpage-hero.ps1

Measured heights: ../../../review/education-subpage-hero-heights.json.
Next: S22-breadcrumb-context-navigation.

