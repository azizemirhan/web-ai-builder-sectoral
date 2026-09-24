# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S03
- Section Name: Client Segments
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 15 studies; S01-S03 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S03-001 | Universal / Safe | Ivory & Olive | A | Three audience photographs above open descriptions |
| FIN-S03-002 | Premium / Editorial | Rosewood | A | Editorial audience rows with photographs and adjacent text |
| FIN-S03-003 | Structured / Visual Modular | Lagoon | A | Wide audience introduction above two complementary panels |
| FIN-S03-004 | Conversion-led | Iris | A | Violet portrait panels with prominent eligibility disclosures |
| FIN-S03-005 | Art-directed / Distinctive | Ink & Apricot | A | Dark portrait sequence with a raised apricot centre panel |

All five raw files are authored. Closed visible copy is 133 words. All three
eligibility disclosures expanded remain within the 230-word limit.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding S01/S02 studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Three proposed audience contexts: individuals and families, independent professionals,
and business teams. These are sample groupings, not verified claims that the firm
serves every group. Eligibility, geographic limits, relevant services and engagement
requirements remain explicit reserved fields. No client relationships, financial
outcomes, coverage, professional authorisation or suitability decisions are invented.

## Media Slots

Three approved audience-context photographs per study; fifteen slots total.

| Audience slot | Expected type and purpose | Accessibility / fallback |
| --- | --- | --- |
| Individuals and families | Consented household-context photograph supporting recognition of the audience | Named article, reserved-photo label and visible caption; retain allocated space without imagery |
| Independent professionals | Consented independent-working context photograph | Named article, reserved-photo label and visible caption; retain allocated space without imagery |
| Business teams | Consented team-working context photograph | Named article, reserved-photo label and visible caption; retain allocated space without imagery |

Before ingestion, obtain licence, provenance, consent and final descriptive alt text.
Generic people imagery must not imply an actual client relationship or endorsement.
The complete audience description remains understandable with empty media regions.

## Interaction and Responsive Decisions

One labelled section with H2 contains three named articles with unique H3 headings.
Each article includes one native Audience and fit disclosure. They open independently
and may all remain open. No submission, automated suitability assessment, dead links,
frameworks, raw scripts or remote dependencies.

Mobile keeps each photograph with its audience text and restores a single reading
order. The featured panel's spacing was refined after visual review. Scoped CSS has
border-box descendants, controlled text measures, visible focus, reduced-motion
handling and summaries at least 48px tall. S02 and S03 are consecutive A sections;
use B or C for the next same-variant section to preserve structural variety.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Metadata, unique IDs, three articles/headings, three media slots and copy budgets
  checked. No document or element overflow, including all disclosures open.
- Every disclosure accepts focus, meets target height, opens and closes correctly.
- Five desktop and five phone screenshots visually reviewed; checks repeated after
  the mobile spacing correction.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five audience layouts](../../../review/finance-segments.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-segments.ps1

Measured heights: ../../../review/finance-segments-heights.json.
Next: S04-advisors-experts.
