# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S17
- Section Name: Scholarships Funding
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 85 studies, S01-S17 authored.

## Planned Studies

All five studies are AUTHORED. Variants 001, 002 and 005 have 116 visible words
closed and 142 expanded; 003 and 004 have 113 closed and 139 expanded.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S17-001 | Universal / Safe | Apricot | B | 1 | Warm learning photograph beside an open funding overview |
| EDU-S17-002 | Premium / Editorial | Mulberry | B | 1 | Editorial funding story with a broad learning-space photograph |
| EDU-S17-003 | Structured / Visual Modular | Cobalt | C | 0 | Funding title beside a blue coverage field and eligibility context |
| EDU-S17-004 | Conversion-led | Iris | C | 0 | Purple opportunity introduction with prominent application details |
| EDU-S17-005 | Art-directed / Distinctive | Afterhours | B | 1 | Dark split funding story with a curved photograph and lime terms |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S15/S16 studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

One reserved scholarship or funding opportunity demonstrates each layout. Name,
provider, support type, coverage, currency, eligibility, programmes, study modes,
deadline, time zone, award duration and renewal conditions remain placeholders.
Application details reserve required documents, selection process, application route,
decision timeline and provider contact. Funding conditions reserve repayment obligations
if applicable, renewal criteria, exclusions and combining-award rules.

No actual award or provider information was supplied. A visible notice identifies
funding details as awaiting confirmation; eligibility is not presented as an award
guarantee. No invented provider, amount, deadline, approval claim or application link.
The programme catalogue link reaches the matching existing S02 review study.
Supply verified opportunity details and a real application destination before publication.

## Responsive and Interaction Decisions

- 001: a warm learning-space image accompanies the introduction beside open funding facts.
- 002: editorial introduction beside a broad image, with funding and application context below.
- 003: a blue coverage field and grouped facts accompany a white application context area.
- 004: purple guidance field beside funding facts and a prominent application disclosure.
- 005: dark split introduction and curved image beside lime opportunity typography and terms.

Tablet and phone layouts restore a linear reading sequence. At phone width, four
facts stack vertically; reserved images use 260px height. Both native disclosures
can remain open together without JavaScript.

Each study has one section H2, one opportunity article/H3, four definition-list facts,
two native disclosures and one matching programme link. Controls have visible keyboard
focus and minimum 44px height.

S15 and S16: C / C / C / C / C. S17: B / B / C / C / B.
Anchored photographs reintroduce media in three variants, with no repeated item grid.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, viewport selection and iframe height handling.

## Media Slots

Three total: one reserved shared-learning-space photograph in each of 001, 002 and 005.
Each has a visible caption and accessible reserved-image description. Use an actual
learning environment, appropriate permissions and descriptive alt text before publication.
Do not imply the photograph identifies an award recipient or proves funding outcomes.
The slot remains visibly reserved without an image; the funding information stands alone.
003 and 004 use typography and colour without media.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with disclosures closed or both open.
- Metadata, unique IDs, section heading, one opportunity, four facts and media counts checked.
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

[Compare five funding designs](../../../review/education-funding.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-funding.ps1

Measured heights: ../../../review/education-funding-heights.json.
Next: S18-locations-online-learning.

