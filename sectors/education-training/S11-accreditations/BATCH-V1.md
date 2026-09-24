# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S11
- Section Name: Accreditations
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 55 studies, S01-S11 authored.

## Planned Studies

All studies are AUTHORED; raw filenames match IDs. Each contains 94 words closed,
110 expanded, shape C and zero media slots.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S11-001 | Universal / Safe | Apricot | Warm split introduction and accreditation record |
| EDU-S11-002 | Premium / Editorial | Mulberry | Editorial organisation title above horizontal scope summary |
| EDU-S11-003 | Structured / Visual Modular | Cobalt | Blue organisation field beside scope and verification details |
| EDU-S11-004 | Conversion-led | Iris | Purple contextual introduction beside concise accreditation information |
| EDU-S11-005 | Art-directed / Distinctive | Afterhours | Large dark organisation typography beside open verification context |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S09/S10 raw studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

One reserved accreditation record demonstrates each composition. Accrediting body,
designation, institutional/programme scope, current register status and validity
dates remain bracketed placeholders with data-placeholder markers. Verification
details reserve the official register reference, source URL, date checked, locations,
delivery modes, conditions and exclusions. No real accreditation was supplied.

A visible notice states that information awaits verification. No invented accreditor,
logo, certification seal, registry link, status or credential. The source URL remains
plain reserved text until an actual record is supplied. The catalogue link reaches
the matching existing S02 raw study as a review route. Accreditation details must
be populated from confirmed official records before publication.

The designs differ through typography, placement of context, scope layout and colour
fields. No certificate, administrative document or classical academic metaphor.

## Responsive and Interaction Decisions

- 001: introduction and rounded record sit side by side; phones stack them and place values below labels.
- 002: a large issuer title leads three horizontal facts; phones stack the facts.
- 003: a blue issuer field accompanies scope and verification; phones show the field first.
- 004: a purple introductory field leads a separate accreditation record on phones.
- 005: oversized issuer typography accompanies scope details; phones restore one linear sequence.

Each study has one native verification disclosure and one matching catalogue link.
The disclosure can open and close without JavaScript; its plus rotates on expansion.
Controls have visible focus treatment and at least 44px height. Scope facts use a
definition list under a single issuer H3 and section H2.

S09 and S10 shapes: A / A / A / A / A. S11: C / C / C / C / C.
Every variant breaks the preceding two-section A run. Manual comparison used;
the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosure provides interaction.
- Gallery JavaScript: local selection, preview widths and frame height handling.

## Media Slots

NONE. Issuer typography, scope and colour carry the section. No verified accreditation
marks were supplied; no invented logos or ornamental certification seals are used.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with verification details closed or open.
- Metadata, unique IDs, region, H2, reserved issuer and three scope facts checked.
- Native disclosure opens and closes; focusability and minimum target height checked.
- Matching S02 destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded visible copy: 110 words per study.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size
  links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five accreditation designs](../../../review/education-accreditations.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-accreditations.ps1

Measured heights: ../../../review/education-accreditations-heights.json.
Next: S12-campus-facilities.
