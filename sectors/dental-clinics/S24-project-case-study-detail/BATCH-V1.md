# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S24
- Section Name: Treatment Case Context Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 120 studies, S01-S24 authored.

## Planned Studies

| Study | Direction | Theme | Shape | Media | Words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S24-001 | Universal / Safe | Chalk | B | 3 | 152 | Offset opening image pair, paired context and approach, separate follow-up composition |
| DN-S24-002 | Premium / Editorial | Linen | B | 3 | 160 | Centred opening, wide photograph and alternating editorial chapters |
| DN-S24-003 | Structured / Visual Modular | Slate | A | 5 | Two large and three compact media-led chapters in one case mosaic |
| DN-S24-004 | Conversion-led | Daylight | B | 3 | Case introduction beside a vertical narrative, amber enquiry band, final review chapter |
| DN-S24-005 | Art-directed / Distinctive | Dusk | B | 3 | Oversized dark opening, offset image pair and staggered narrative with a closing image |

## Research and Evidence Boundary

Sources: user request for five modern designs, section README,
../DENTAL-THEME-CONTRACT.md, ../../../standards/01-AUTHORING-STANDARD.md,
../../../standards/03-MEDIA-POLICY.md, S14 gallery batch, S05 historical batch,
and preceding S22/S23 raw and batch records. External research: NONE.

No verified patient case has been supplied. Historical S05 illustrative case details
are not treated as real evidence. Each study explicitly says the case account is
pending and uses bracketed data-placeholder fields for context, options, decisions,
stages, review observations, review interval, remaining concerns and care involved.
These fields demonstrate a complete case architecture without inventing its contents.

The page concerns one anonymised case, not a collection of treatments. It reserves
what was delivered and what was observed without supplying an invented outcome.
No patient identity, testimonial, clinical measurements, dates, treatment duration,
prices, credentials, before/after claim or comparison slider is fabricated.
There is no clinical guidance. The caveat distinguishes one case from a typical
result and distinguishes care-setting photographs from evidence of an outcome.

Document metaphor: NONE. Layout uses proportion, whitespace, colour fields and
media. No charts, technical registers, numbered metadata gutters or text-only cards.

## Media Register

All media is reserved; no bitmap or remote asset has been added.
There are 17 areas in the batch. Each has a visible subject label and an accessible
reserved-photograph label. Photographs must later depict actual care context.

| Subject | Studies | Purpose | Expected type | Empty fallback |
| --- | --- | --- | --- | --- |
| Consultation room | All five | Establish the setting in which the case was discussed | Actual consultation-space photograph, no patient material | Labelled colour reservation retains layout |
| Dentist in conversation | All five | Support the account of options and decisions | Actual staff member mid-conversation, no identifiable patient | Reserved figure, never a generated face |
| Review consultation room | All five | Locate the follow-up chapter without implying an outcome | Actual review setting | Labelled reservation remains readable |
| Treating clinician at work | 003 | Support the staged-care chapter | Actual clinician at work, no instruments near a face or mouth detail | Portrait remains reserved |
| Treating clinician in conversation | 003 | Accompany the care-involved field | Actual clinician, role and identity verified before use | Reserved portrait figure |

These are contextual images, not medical evidence. The batch does not claim they
document a real case yet. Real assets require provenance, permission, accurate
captions and descriptive alt text at integration. Avoid stock smiles, mouth imagery,
tooth icons and anonymous white-surgery glamour shots.

## Responsive and Structural Decisions

- 001 retains its offset two-image opening on phones, then stacks the open narrative
  and follow-up. The images remain distinct subjects, not a before/after pair.
- 002 turns centred introductory text left-aligned below 680px; editorial chapter
  labels lead their text. The supporting paired images retain a compact stagger.
- 003 changes the desktop two-plus-three mosaic to two columns below 860px and
  a single ordered sequence below 560px. Every card has its own media.
- 004 releases the introduction/narrative split below 860px. Its amber enquiry band
  and final review remain separate, preserving the full case reading order.
- 005 reduces media offsets and corner geometry on phones; its two narrative columns
  become one. The closing review image then leads the care-involved and enquiry area.

S22 shapes: C / C / C / C / C. S23: B / B / B / C / B.
S24: B / B / A / B / B. No consecutive item-grid run is introduced.
Manual comparison with S22/S23 confirms navigation, service description and case
narrative are separate roles. The existing composition checker assumes CONS filenames;
it is not used to claim dental composition validation.

## Navigation and Assembly

Two native links per study: same-variant S19-contact for personal questions and
S23-service-offering-detail for exploring a first consultation. All ten targets
exist. These are local review routes, not production URLs or a claim that a first
consultation was the service delivered in this reserved case.

The actual treatment and treating role remain reserved. No person link is invented
when no clinician is known. Add verified service/profile destinations with the real
case content during integration. There is one internal H1 and a named case-study-detail
section per standalone file, with no global header, navigation or footer.

## QA Record

- Headless Chrome: 20 checks across 1440, 768, 390 and 320px.
- No document overflow or out-of-viewport elements at the tested widths.
- Stable IDs and metadata, one H1 and a labelled section checked.
- Native links receive keyboard focus and have at least 44px height.
- All ten link destinations verified on disk.
- All five desktop and 390px screenshots visually reviewed.
- Visible word counts: 152, 160, 160, 175 and 152.
- Gallery checks passed: five frames, variant selection, mobile width selection,
  pressed state, restore-all and full-size links.
- No raw JavaScript or external dependencies. Reduced-motion CSS included.
- git diff --check completed without whitespace errors.
- Cross-browser and screen-reader testing were not run; no live case content
  validation or Design Lab ingestion is claimed.

## Review

[Five-study gallery](../../../review/dental-case-detail.html)

Regenerate from the repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-case-detail.ps1

Measured heights: ../../../review/dental-case-detail-heights.json.
Raw HTML is the source of truth.

