# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S19
- Section Name: Contact Admissions
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 95 studies, S01-S19 authored.

## Planned Studies

All five studies are AUTHORED. Variants 001, 002 and 005 have 114 visible words
closed and 146 expanded; 003 and 004 have 111 closed and 143 expanded.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S19-001 | Universal / Safe | Apricot | B | 1 | Welcoming admissions photograph beside open contact details |
| EDU-S19-002 | Premium / Editorial | Mulberry | B | 1 | Editorial admissions introduction above a wide contact band |
| EDU-S19-003 | Structured / Visual Modular | Cobalt | C | 0 | Blue email field beside concise enquiry guidance |
| EDU-S19-004 | Conversion-led | Iris | C | 0 | Purple introduction beside prominent admissions contact information |
| EDU-S19-005 | Art-directed / Distinctive | Afterhours | B | 1 | Dark admissions story with a curved image and lime preparation panel |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S17/S18 studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

One admissions team demonstrates each composition. Team name, programme/campus remit,
email, phone with country code, opening hours, time zone, office address and appointment
requirements remain bracketed placeholders. Accessible communication formats, language
assistance and visit arrangements are also reserved. A visible notice states that the
contact details await confirmation.

The preparation disclosure gives general guidance to have a programme of interest,
intended start date, questions and an existing application reference ready.
No real contact information was supplied. There are no invented email/telephone links,
office addresses, staff identities, response-time promises, enquiry forms or submission
confirmations. No personal data is collected. Populate verified contact information
and appropriate mailto/tel links before publication.

The catalogue link reaches the matching existing S02 raw study as a review destination.
It is labelled programme exploration and does not imply contacting admissions.

## Responsive and Interaction Decisions

- 001: warm welcome photograph beside open details, with email taking the full width.
- 002: editorial introduction and photograph above contact rows and enquiry guidance.
- 003: a blue email/contact field beside a white guidance area.
- 004: purple introduction beside an emphasized email field and preparation disclosure.
- 005: curved welcome photograph beside lime team typography and a lime guidance panel.

Tablet and phone layouts restore a linear reading sequence. Phone photographs use
260px height and contact facts stack. Both native disclosures can remain open together.

Each study has one section H2, one admissions article/H3, a four-field definition list,
two native disclosures and one matching programme link. Controls have visible keyboard
focus and minimum 44px height. No raw JavaScript is required.

S17: B / B / C / C / B. S18: A / A / A / A / A.
S19: B / B / C / C / B, breaking the preceding item comparison.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, viewport selection and iframe height handling.

## Media Slots

Three total: one reserved admissions welcome-space photograph in 001, 002 and 005.
Each has a visible caption and accessible reserved-image description. Use an actual
welcome environment with suitable permissions and descriptive alt text before publication.
No fabricated adviser portrait. Without an image, the labelled slot stays reserved
and the contact information remains understandable. 003 and 004 have no media.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with disclosures closed or both open.
- Metadata, unique IDs, section heading, one contact, four facts and media counts checked.
- Both native disclosures open and close; keyboard focus and minimum target heights checked.
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

[Compare five admissions contact designs](../../../review/education-contact.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-contact.ps1

Measured heights: ../../../review/education-contact-heights.json.
Next: S20-final-apply-enroll-cta.

