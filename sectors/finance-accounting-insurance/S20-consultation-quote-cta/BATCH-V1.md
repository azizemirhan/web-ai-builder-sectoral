# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S20
- Section Name: Consultation Quote CTA
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 100 studies; S01-S20 authored. Core catalogue authoring complete.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S20-001 | Universal / Safe | Ivory & Olive | C | Closing invitation beside a rounded next-step panel |
| FIN-S20-002 | Premium / Editorial | Rosewood | C | Editorial invitation with a wide action row |
| FIN-S20-003 | Structured / Visual Modular | Lagoon | C | Centred invitation in a generous teal field |
| FIN-S20-004 | Conversion-led | Iris | C | Oversized violet heading beside the action |
| FIN-S20-005 | Art-directed / Distinctive | Ink & Apricot | C | Apricot closing invitation on a dark ground |

All five raw files are authored. Closed visible copy is 91 words; expanded copy
is 117 words. S19 used shape A; this typographic C section resets the sequence.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

The section invites a discussion about consultation or quote scope. Availability,
initial fees, inclusions, eligibility, follow-up and agreement terms remain reserved.
Quote preparation notes reserve scope, timing, assumptions, exclusions and costs.
No free consultation, price, guaranteed quote, appointment or response time is invented.

## Media Slots

None. Typography, colour and the primary action carry the closing invitation.

## Interaction and Responsive Decisions

One labelled section with H2 contains a primary Explore contact options link and
a native Preparing for a quote disclosure. Each link opens the authored S19 contact
study with the same variant number. These local catalogue destinations still contain
reserved contact information. There is no booking, request submission or quote generation.
At ingestion map the link to the approved site contact route.

Desktop compositions vary through split layouts, a wide action row, a centred field
and coloured heading panels. Tablet and phone keep heading, invitation, action, terms
and disclosure in order. Scoped CSS includes wrapping, border-box sizing, visible
focus, reduced-motion handling, a 52px action and 48px summary target.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, heading, shape C, primary action destination
  and closed/expanded copy budgets.
- Verified all five relative contact destination files exist.
- No document or element overflow with the disclosure closed or open.
- Link and summary accept focus and meet target height; disclosure opens/closes.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five consultation layouts](../../../review/finance-consultation.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-consultation.ps1

Measured heights: ../../../review/finance-consultation-heights.json.
Next: S21-subpage-hero.
