# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S01
- Section Name: Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 5 studies; S01 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S01-001 | Universal / Safe | Ivory & Olive | B | Warm split introduction with a generous conversation photograph |
| FIN-S01-002 | Premium / Editorial | Rosewood | B | Editorial portrait opening with a text column on the right |
| FIN-S01-003 | Structured / Visual Modular | Lagoon | B | Wide title and conversation prompt above a panoramic image |
| FIN-S01-004 | Conversion-led | Iris | C | Violet typography with a prominent conversation disclosure |
| FIN-S01-005 | Art-directed / Distinctive | Ink & Apricot | B | Dark oversized introduction, arched portrait and apricot invitation |

All five raw files are authored. Visible copy is 52 words closed / 71 expanded;
004 has 47 / 66 words because it has no media caption.

## Research Metadata

Sources: user continuation request and preference for modern styles, sector README,
sector brief, section README, authoring standard, media policy and batch template.
Research date: 2026-09-15. External research: NONE. Document-metaphor justification:
NONE. This starts the next sector in workspace folder order after energy completion.

The hero introduces an exploratory conversation without promising any financial
result or giving financial advice. Firm name, contact route, service scope and
eligibility remain explicit placeholders. No firm credentials, fees, returns,
coverage claims or client relationships are fabricated. The themes are defined in
../FINANCE-THEME-CONTRACT.md and retain their variant numbers in future sections.

The five compositions vary image placement, proportion, typography and the role of
the disclosure. Variant 004 intentionally uses type and colour without media to
concentrate attention on preparing for the first conversation.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native details provides the only interaction.

## Media Slots

| Slot | Studies | Purpose / expected type | Accessibility and fallback |
| --- | --- | --- | --- |
| conversation | 001, 002, 003, 005 | Approved photograph of a professional conversation; portrait or panoramic crop appropriate to the layout | Labelled, allocated region and visible caption; obtain participant consent, provenance, licence and descriptive alt text |
| none | 004 | Type and colour composition | All content is plain text and native disclosure |

Four reserved photographs total. Images must not imply an actual client or adviser
relationship without evidence. Empty reserved media is intended output.

## Interaction and Responsive Decisions

Each labelled region has an H2 and one native conversation-preparation disclosure.
It reveals a short preparation prompt and reserved firm contact/scope details. It
neither books nor submits anything. Future contact sections are not linked before
authoring; no dead hashes, fake routes, forms, global navigation or invented logos.

At smaller widths the title, introduction and disclosure remain together before
supporting media. Full copy survives reflow and disclosure expansion. Scoped CSS
includes border-box descendants, visible focus, reduced-motion treatment and a
minimum 54px summary target.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Identity metadata, unique IDs, heading count, media counts and word budgets checked.
- No document or element overflow, including expanded disclosure content.
- Native details opening, closing, focus and target height passed.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five finance heroes](../../../review/finance-hero.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-hero.ps1

Measured heights: ../../../review/finance-hero-heights.json.
The repository's Python contact-sheet builder currently targets architecture only;
this batch uses the dedicated finance review gallery.
Next: S02-services-solutions.
