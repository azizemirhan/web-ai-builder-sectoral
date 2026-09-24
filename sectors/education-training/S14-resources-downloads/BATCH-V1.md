# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S14
- Section Name: Resources Downloads
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 70 studies, S01-S14 authored.

## Planned Studies

All five studies are AUTHORED, shape C, with zero media slots.
Each contains 103 visible words closed and 117 expanded.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S14-001 | Universal / Safe | Apricot | Warm split introduction and open resource overview |
| EDU-S14-002 | Premium / Editorial | Mulberry | Oversized resource title above an editorial information band |
| EDU-S14-003 | Structured / Visual Modular | Cobalt | Blue resource introduction beside modular file context |
| EDU-S14-004 | Conversion-led | Iris | Purple resource spotlight beside prominent access information |
| EDU-S14-005 | Art-directed / Distinctive | Afterhours | Expressive dark resource title with a lime access panel |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S12/S13 batch records and S11 raw study;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

One featured learning resource demonstrates each composition. Title, description,
file format and size, language, verified revision date, programme/year, covered topics,
source owner, reuse permissions, accessible formats and support contact remain explicit
placeholders. No downloadable file was supplied.

The visible availability notice explains that a verified file is awaited. There is
no fabricated download, inactive download button, fake file size, invented publication
date or signup gate. Native resource details provide useful local interaction.
The catalogue link reaches the matching existing S02 study as a review destination.
Supply the actual file, its verified metadata and an accessible download link before
publication. Do not present the catalogue link as the resource download.

## Responsive and Interaction Decisions

- 001: a split introduction and warm resource panel; phone stacks the panel and its facts.
- 002: oversized resource typography leads a horizontal information band; narrow screens
  place the access information below the file context.
- 003: blue introduction beside modular resource facts; phone leads with the blue field.
- 004: purple resource spotlight attached to a pale access area; phone stacks the fields,
  retaining the prominent resource-details disclosure.
- 005: oversized lime resource title above open facts and a lime access panel; phone
  puts the access panel after the facts.

Each study has one section H2, one resource article/H3, a four-field definition list,
one native disclosure and one matching catalogue link. Keyboard focus treatment and
44px minimum control heights are included. Details operate without JavaScript.

S12 and S13 shapes: A / A / A / A / A. S14: C / C / C / C / C.
Every variant breaks the preceding two-section A run through one resource composition,
rather than another collection of repeated items. Manual comparison used;
the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, preview widths and iframe height handling.

## Media Slots

NONE. Resource typography, file context and colour carry these layouts.
No fabricated publication cover, document mockup or institutional identity.
The design remains understandable without media; a real downloadable resource
and associated metadata are required to replace the explicit unavailable state.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with resource details closed or open.
- Metadata, unique IDs, section heading, one resource, four facts and zero media checked.
- Native details open and close; keyboard focus and minimum target heights checked.
- Matching S02 destinations exist.
- Five desktop and five 390px screenshots visually reviewed.
- Expanded visible copy remains below the 250-word limit.
- Scoped CSS and theme variables, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size links
  and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five resource designs](../../../review/education-resources.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-resources.ps1

Measured heights: ../../../review/education-resources-heights.json.
Next: S15-faq.

