# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S16
- Section Name: Tuition Pricing
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 80 studies, S01-S16 authored.

## Planned Studies

All five studies are AUTHORED, shape C, with zero media slots.
Each contains 119 visible words closed and 143 with both disclosures expanded.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S16-001 | Universal / Safe | Apricot | Warm programme fee panel beside a clear introduction |
| EDU-S16-002 | Premium / Editorial | Mulberry | Editorial tuition amount above an open cost breakdown |
| EDU-S16-003 | Structured / Visual Modular | Cobalt | Blue planning introduction beside grouped tuition context |
| EDU-S16-004 | Conversion-led | Iris | Purple tuition spotlight joined to payment information |
| EDU-S16-005 | Art-directed / Distinctive | Afterhours | Oversized lime tuition amount with a contrasting terms panel |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S14/S15 studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

One programme fee demonstrates each layout. Programme name, amount, currency, billing
period, inclusions, additional costs, taxes, fee category, study mode and validity
remain bracketed placeholders. Payment disclosures reserve the deposit, payment dates,
instalment eligibility, charges, accepted methods and official fee contact. The second
disclosure reserves withdrawal, refund, deferral and fee-change terms.

No real fees or policies were supplied. A visible notice states that institutional
confirmation is awaited. No fabricated price, discount, financing promise, repayment
calculator, checkout or enrolment action. The matching S02 link is an existing review
route for programme exploration. Confirm the full fee context before publication.
Scholarships and funding remain the responsibility of S17.

## Responsive and Interaction Decisions

- 001: warm fee panel beside an introduction; phones stack the panel and cost facts.
- 002: large tuition typography above an open cost band; phones place terms after facts.
- 003: blue planning introduction beside grouped fee context; phones lead with the blue
  field, then amount and cost information.
- 004: purple amount spotlight attached to a pale terms area; phones stack both regions,
  preserving the prominent payment and cancellation disclosures.
- 005: oversized lime amount above open facts and a contrasting terms panel; phones
  place the terms panel below cost context.

Each study has one section H2, one programme article/H3, four definition-list facts,
two independent native details and one matching catalogue link. Both disclosures start
closed and can remain open together. Controls have visible keyboard focus and minimum
44px height. No JavaScript is required in the raw studies.

S14, S15 and S16: C / C / C / C / C.
One fee composition and its supporting facts avoid a repeated pricing-tier grid.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, viewport selection and iframe height handling.

## Media Slots

NONE. Amount, billing context, terms and colour carry this section.
No fake institution branding, financial badges or decorative document metaphor.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with disclosures closed or both open.
- Metadata, unique IDs, section heading, one programme, four facts and zero media checked.
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

[Compare five tuition designs](../../../review/education-tuition.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-tuition.ps1

Measured heights: ../../../review/education-tuition-heights.json.
Next: S17-scholarships-funding.

