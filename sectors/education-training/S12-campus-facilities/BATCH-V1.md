# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S12
- Section Name: Campus Facilities
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 60 studies, S01-S12 authored.

## Planned Studies

All five studies are AUTHORED, shape A, with three media slots each.
Each contains 148 visible words closed and 190 expanded.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S12-001 | Universal / Safe | Apricot | Three welcoming campus-space cards with broad photographs |
| EDU-S12-002 | Premium / Editorial | Mulberry | Alternating editorial learning-space features |
| EDU-S12-003 | Structured / Visual Modular | Cobalt | Campus introduction beside a joined facility mosaic |
| EDU-S12-004 | Conversion-led | Iris | Featured campus space above two compact facility summaries |
| EDU-S12-005 | Art-directed / Distinctive | Afterhours | Asymmetric dark campus gallery with varied image crops |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding section studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Three reserved learning spaces demonstrate each layout. Names, campus, facility
type, purpose, location, equipment, hours, booking requirements and accessibility
information remain explicit placeholders. No actual campus information was supplied.
A visible notice states that facilities await confirmation. No invented campus,
equipment claim, map, tour or booking destination is presented as real.
Each catalogue link reaches the matching existing S02 study for review.

## Responsive and Interaction Decisions

- 001: three equal photographic cards; tablet and phone use a single column.
- 002: alternating image/text rows; phone places every photograph above its text.
- 003: side introduction with a large card above two smaller cards; narrow screens stack them.
- 004: a wide featured space above two compact spaces; phone restores one linear sequence.
- 005: unequal columns, varied crops and vertical offsets; narrow screens remove the offsets.

Each study contains one section H2, three article H3s, three native access disclosures
and one programme catalogue link. Disclosure controls open and close without scripts,
have visible focus treatment and at least 44px target height. Reduced motion is supported.

S10 shapes: A / A / A / A / A. S11: C / C / C / C / C.
S12: A / A / A / A / A, starting a new A run. Manual comparison used;
the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE; native details provide interaction.
- Gallery JavaScript: local filters, viewport selection and iframe sizing.

## Media Slots

Fifteen reserved facility photographs across five studies. Each slot has a visible
learning-space label and an accessible reserved-photo description. Supply photographs
of the actual confirmed spaces, appropriate permissions and descriptive alternative
text before publication. No stock image is presented as a real campus.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with disclosures closed or all open.
- Metadata, unique IDs, section heading, three articles and three media slots checked.
- Native disclosures open and close; focusability and minimum target heights checked.
- Matching S02 destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded copy remains below the 250-word limit.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size
  links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five campus designs](../../../review/education-campus.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-campus.ps1

Measured heights: ../../../review/education-campus-heights.json.
Next: S13-events-webinars.
