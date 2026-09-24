# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S19
- Section Name: Contact
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 95 studies; S01-S19 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S19-001 | Universal / Safe | Ivory & Olive | A | Introduction beside a clear contact sequence |
| FIN-S19-002 | Premium / Editorial | Rosewood | A | Three open editorial contact columns |
| FIN-S19-003 | Structured / Visual Modular | Lagoon | A | Featured contact beside two complementary channels |
| FIN-S19-004 | Conversion-led | Iris | A | Violet introduction beside open contact rows |
| FIN-S19-005 | Art-directed / Distinctive | Ink & Apricot | A | Dark editorial rows with apricot channel labels |

All five raw files are authored. Closed visible copy is 127 words; expanded copy
is 156 words. S18 used shape B, so this A section begins a new sequence.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Three proposed contact routes cover email, telephone and meeting arrangements.
Email addresses, responsible teams, telephone numbers, contact hours, timezone,
language options, reply expectations and meeting availability remain reserved.
No recipient, response-time promise, appointment or delivery mechanism is invented.
Preparation notes reserve approved enquiry guidance and confidential-document channels.
Add mailto, tel, meeting and privacy links only after their destinations are verified.

## Media Slots

None. Typography, spacing and colour distinguish the contact compositions.

## Interaction and Responsive Decisions

One labelled section with H2 contains three articles, each named by its H3. A native
Before the first conversation disclosure reveals reserved preparation information.
Contact headings are plain text. No simulated forms, submission feedback, booking,
data collection, raw scripts or external dependencies are included.

Desktop layouts vary through split introductions, open columns, a featured channel,
a coloured heading panel and editorial rows. Tablet and phone preserve the channel,
heading, contact scope and supporting note in one reading order. Scoped CSS includes
wrapping, border-box sizing, visible focus, reduced-motion handling and summary
targets of at least 48px.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, article-heading pairs, three contact
  channels, supporting notes and closed/expanded copy budgets.
- No document or element overflow with the disclosure closed or open.
- Summary accepts focus, meets target height and opens/closes correctly.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five contact layouts](../../../review/finance-contact.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-contact.ps1

Measured heights: ../../../review/finance-contact-heights.json.
Next: S20-consultation-quote-cta.
