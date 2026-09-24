# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S04
- Section Name: Advisors Experts
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 20 studies; S01-S04 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S04-001 | Universal / Safe | Ivory & Olive | B | Paired adviser portraits beside a calm team introduction |
| FIN-S04-002 | Premium / Editorial | Rosewood | B | Editorial portrait pair above an inset team narrative |
| FIN-S04-003 | Structured / Visual Modular | Lagoon | B | Teal team narrative beside two compact portrait anchors |
| FIN-S04-004 | Conversion-led | Iris | B | Violet adviser introduction beside stacked portraits |
| FIN-S04-005 | Art-directed / Distinctive | Ink & Apricot | B | Dark arched portrait pair above an apricot team statement |

All five raw files are authored. Visible copy is 118 words with the disclosure
closed and 140 words expanded. Two portrait anchors support one collective team
narrative. Shape B follows the preceding two A sections to maintain variety.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Names, roles, service scope, contact arrangements and professional backgrounds
remain explicit reserved fields. No invented people, qualifications, professional
authorisation, availability or financial outcomes. Approved background information
must clearly identify the adviser to whom each statement applies.

## Media Slots

Two adviser portrait photographs per study; ten slots total. Each portrait supports
recognition of the person identified by its adjacent name and role. The figure is
accessibly named by that identity; a reserved-image label is visible in each slot.

Before ingestion, obtain person-approved photographs, consent, licence and provenance.
Replace reserved labels with descriptive alt text identifying the correct adviser.
Keep the allocated space and visible reserved caption until approved assets exist.
Do not use generic or synthetic people as representations of actual team members.
The team narrative remains usable without photographs.

## Interaction and Responsive Decisions

One labelled section with H2, two named portrait figures and one team-context article
with H3. A native Roles and professional background disclosure opens independently
without scripting. No invented profile routes, dead links, submission forms, external
dependencies or raw scripts.

Scoped CSS supports visible focus, reduced motion, border-box descendants, readable
text measures and summary targets at least 48px tall. Portraits stack on phones and
stay paired with their captions. Editorial offsets are removed below 850px.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Metadata, unique IDs, section/article headings, portrait identity pairing, two media
  slots and closed/expanded copy budgets checked.
- No document or element overflow; native disclosure focus, target height and
  open/close behavior passed.
- Five desktop and five phone screenshots visually reviewed; checks repeated after
  correcting mobile portrait spacing.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five adviser layouts](../../../review/finance-advisors.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-advisors.ps1

Measured heights: ../../../review/finance-advisors-heights.json.
Next: S05-regulatory-trust.
