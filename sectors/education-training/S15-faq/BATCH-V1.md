# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S15
- Section Name: FAQ
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 75 studies, S01-S15 authored.

## Planned Studies

All five studies are AUTHORED, shape C, with zero media slots.
Each contains 102 visible words closed and 161 with all six answers expanded.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S15-001 | Universal / Safe | Apricot | Warm side introduction and two flowing question groups |
| EDU-S15-002 | Premium / Editorial | Mulberry | Centred editorial introduction above paired question columns |
| EDU-S15-003 | Structured / Visual Modular | Cobalt | Wide question bands with separate topic labels |
| EDU-S15-004 | Conversion-led | Iris | Purple guidance panel beside a focused question sequence |
| EDU-S15-005 | Art-directed / Distinctive | Afterhours | Oversized dark introduction with stepped question groups |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S13/S14 batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Six questions address entry requirements, application dates, study costs, delivery
modes, learning support and qualifications. They are grouped under Before you apply
and Your learning experience. All answers are explicit bracketed placeholders with
data-placeholder markers. A visible notice states that institutional confirmation
is awaited. No invented requirements, dates, fees, support service or award.

The closing guidance encourages checking the selected programme. Its catalogue link
reaches the matching existing S02 raw study as a review route. Confirm institution-
and programme-specific answers before publication. No fake contact route, enquiry
form, search, chatbot response or structured-data claim is included.

## Responsive and Interaction Decisions

- 001: introduction beside a warm grouped question area; phones stack the two regions.
- 002: centred introduction above two editorial columns; phones remove the column offset.
- 003: wide topic bands with labels beside questions; phones place labels above answers.
- 004: purple guidance field with a catalogue CTA beside the question sequence; phones
  preserve the field first and show questions below.
- 005: oversized typography and stepped topic groups; phones remove indentation.
  Expanded answers receive a lime background and dark text.

Each study has one section H2, two topic H3s and six native details/summary controls.
All start closed. Multiple answers can remain open for comparison. The plus rotates
on expansion and is decorative; the question itself names the control.
Keyboard focus treatment and minimum 44px target heights are included.
No JavaScript is required in the raw studies.

S13: A / A / A / A / A. S14 and S15: C / C / C / C / C.
Typography and flowing questions continue the breathing space after the item grids.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, preview widths and iframe height handling.

## Media Slots

NONE. Questions, answer hierarchy and colour carry this section.
No decorative academic imagery, fictional staff portrait or technical document metaphor.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with all answers closed or open.
- Metadata, unique IDs, section heading, two topic headings and zero media checked.
- Six native disclosures open and close; keyboard focus and minimum target heights checked.
- Matching S02 destinations exist.
- Five desktop and five 390px screenshots visually reviewed.
- Expanded copy remains below the 250-word limit.
- Scoped CSS and theme variables, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size links
  and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five FAQ designs](../../../review/education-faq.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-faq.ps1

Measured heights: ../../../review/education-faq-heights.json.
Next: S16-tuition-pricing.

