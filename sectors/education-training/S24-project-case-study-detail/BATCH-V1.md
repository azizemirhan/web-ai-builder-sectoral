# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S24
- Section Name: Programme Outcome / Cohort Case Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 120 studies, S01-S24 authored.

## Studies

All five studies are AUTHORED. Each contains 185 visible words, shape B and three
reserved media slots. Each represents one anonymised cohort case, not a work index.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S24-001 | Universal / Safe | Apricot | Warm introduction beside a large work image, followed by paired stages |
| EDU-S24-002 | Premium / Editorial | Mulberry | Editorial panorama with open narrative and a two-image process sequence |
| EDU-S24-003 | Structured / Visual Modular | Cobalt | Blue context module with an unequal evidence and narrative grid |
| EDU-S24-004 | Conversion-led | Iris | Case narrative with an integrated programme exploration panel |
| EDU-S24-005 | Art-directed / Distinctive | Afterhours | Oversized dark introduction and asymmetrical evidence with a lime reflection |

## Research Metadata and Scope

Sources: user continuation request; S24 README and its sector limitation; education
theme contract; existing S10 student projects; preceding S22/S23 studies;
authoring standard and media policy. Research date: 2026-09-14.
External research: NONE. Document-metaphor justification: NONE.

The design follows one body of student work through context, approach and delivery.
Title, programme, anonymised cohort, period, contributor roles, brief, decisions
and reflection remain explicit placeholders. No client, student identity, project,
success rate, employment outcome or testimonial is fabricated. Generic introduction
copy frames how to read a case; it does not assert that an actual project occurred.

The single Explore programmes link reaches the matching existing S02 study as a
local review destination. It is a catalogue handoff, not a claim that a particular
programme or named person contributed. Verified specific relationships and routes
can replace the reserved context during integration.

## Media Slots

Fifteen slots total: the same three purposes in every variant.

| Slot | Purpose | Expected type | Accessibility and fallback |
| --- | --- | --- | --- |
| overview | Establish the completed body of work | Approved photograph or image of the final artefact | Reserved-image label and visible caption; retain allocated space until supplied |
| process | Document a stage and connect it to decisions | Approved process photograph or work-in-progress capture | Describe the actual stage and relevant visual detail in final alt text; reserved caption remains without media |
| detail | Support the delivery and reflection narrative | Approved close view of the delivered work | Describe the evidenced detail, without inferring outcomes; reserved caption remains without media |

Final assets require provenance, licensing and any necessary participant consent.
Remove identifying material where the cohort must remain anonymised. Replace slot
captions with verified stage descriptions and credits; do not use invented imagery
as project evidence. The narrative stays understandable while assets are absent.

## Responsive and Interaction Decisions

001 balances a split introduction and overview with two subsequent stages. 002
uses a wide panoramic opening and open editorial context. 003 groups context and
evidence in unequal columns. 004 pairs each process image with its narrative and
ends in a purple exploration panel. 005 offsets the final detail stage within an
asymmetrical composition and closes with a lime reflection band.

Below 800px, content follows DOM order: introduction, overview, facts, brief,
development, delivered detail and programme exploration. No carousel, horizontal
scroll, sticky rail or hidden narrative. Media becomes 250px high on phones.
The case remains readable without scripts. Controls have visible focus and at
least 44px target height, with full-width phone links.

S22: C / C / C / C / C. S23: C / C / C / C / C. S24: B / B / B / B / B.
Media is central to this role and is deliberately reserved at substantial scale.
Scoped CSS, border-box sizing and reduced-motion treatment are included.
Raw JavaScript, frameworks, remote assets and runtime dependencies: NONE.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow; heading, unique IDs and metadata checked.
- Three media slots and three contextual facts checked in each variant.
- Programme links accept keyboard focus and meet target-height requirements.
- All five matching S02 destinations exist.
- Five desktop and five mobile screenshots visually reviewed. Mobile divider and
  the intended desktop stage offset were corrected after review.
- All studies fit the 150-230-word detail target.
- Gallery passed five frames, filtering, mobile width, pressed states, full-size
  links and restoration checks. Cached measured heights support local-file previews.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five cohort cases](../../../review/education-case-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-case-detail.ps1

Measured heights: ../../../review/education-case-detail-heights.json.
Next: S25-article-insight-detail.
