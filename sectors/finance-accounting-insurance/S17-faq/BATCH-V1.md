# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S17
- Section Name: FAQ
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 85 studies; S01-S17 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S17-001 | Universal / Safe | Ivory & Olive | A | Introduction beside an open question sequence |
| FIN-S17-002 | Premium / Editorial | Rosewood | A | Editorial questions beneath a spacious introduction |
| FIN-S17-003 | Structured / Visual Modular | Lagoon | A | Two-column question collection with a full-width opening |
| FIN-S17-004 | Conversion-led | Iris | A | Introduction beside a violet question panel |
| FIN-S17-005 | Art-directed / Distinctive | Ink & Apricot | A | Centred introduction above an apricot question collection |

All five raw files are authored. Closed visible copy is 104 words; all five answers
open give 194 words. S16 used shape B, so this A section begins a new sequence.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Five proposed questions address service fit, initial preparation, scope and fees,
existing tools and changing circumstances. Each answer remains an explicitly
reserved field for approved business information. No eligibility, fee, compatibility,
service availability or response-time promise is invented. Confirm jurisdiction,
preparation channels, written terms, setup responsibilities and contact arrangements
before publication. There are no fabricated links or contact submissions.

## Media Slots

None. Typography, spacing and colour distinguish the question layouts.

## Interaction and Responsive Decisions

One labelled section with H2 contains five native details/summary pairs. All answers
start closed and may remain open together. Questions are the disclosure labels;
there are no redundant article headings, scripted accordion controls or dependencies.
The plus sign is decorative and rotates when its answer is open.

Desktop layouts vary between split introductions, an editorial sequence, independent
cards and coloured panels. Tablet and phone preserve question order in a single
column. Scoped CSS includes wrapping, border-box sizing, visible focus, reduced-motion
handling and summary targets of at least 56px.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, section heading, five FAQ entries, reserved
  answers and closed/all-open copy budgets.
- No document or element overflow, including after each answer opens and all open.
- Every summary accepts focus, meets target height and opens/closes its answer.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five FAQ layouts](../../../review/finance-faq.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-faq.ps1

Measured heights: ../../../review/finance-faq-heights.json.
Next: S18-locations-offices.
