# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S10
- Section Name: Client Testimonials
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 50 studies; S01-S10 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S10-001 | Universal / Safe | Ivory & Olive | B | Client portrait beside a spacious first person account |
| FIN-S10-002 | Premium / Editorial | Rosewood | B | Editorial quote above a compact portrait and attribution |
| FIN-S10-003 | Structured / Visual Modular | Lagoon | B | Portrait beside a stacked introduction and testimonial |
| FIN-S10-004 | Conversion-led | Iris | B | Violet testimonial panel beside an intimate client portrait |
| FIN-S10-005 | Art-directed / Distinctive | Ink & Apricot | B | Dark arched client portrait alongside an apricot quotation |

All five raw files are authored. Closed visible copy is 104 words; expanded copy
is 129 words. One portrait and one account form each composition. Shape B breaks
the preceding S08/S09 sequence of two A sections.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

The quote, attribution, role, service context and date are explicitly reserved.
No testimonial, person, client relationship, rating or financial outcome is invented.
The account is intended to describe communication and the working relationship.
The context disclosure reserves source verification, publication permission and any
relevant relationship or incentive disclosure. Actual statements must preserve the
meaning of the approved account and must not imply typical or future results.

## Media Slots

One consented client portrait per study; five slots total. The photograph must depict
the same client whose account is attributed in that study. Obtain licence, provenance,
publication consent and final descriptive alt text before ingestion. Do not substitute
a stock or synthetic person as the actual client. If attribution is anonymous,
respect the same anonymity in the imagery and caption.

Every reserved region has allocated space, an accessible image description and a
visible reserved-image label plus a figure caption. Retain this labelled fallback
until an approved image exists; the account remains understandable without imagery.

## Interaction and Responsive Decisions

One labelled section with H2 contains a named portrait figure and one article with
H3. A blockquote is paired with its attribution inside an account figure. The native
About this account disclosure provides context without a carousel, autoplay, fabricated
review source, dead link, submission, raw script or external dependency.

Desktop layouts vary in portrait placement and quote emphasis. Tablet and phone use
a single reading order and 25px quote text on phones. Scoped CSS includes wrapping,
border-box descendants, visible focus, reduced-motion handling and a summary target
at least 48px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, section heading, article/H3 count, reserved
  blockquote, attribution, portrait-caption pairing, shape B and copy budgets.
- No document or element overflow, including expanded disclosure content.
- Native summary focus, target height, opening and closing passed.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five testimonial layouts](../../../review/finance-testimonials.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-testimonials.ps1

Measured heights: ../../../review/finance-testimonials-heights.json.
Next: S11-case-studies.
