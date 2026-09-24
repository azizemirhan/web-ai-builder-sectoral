# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S08
- Section Name: Engineering Process
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 40 studies; S01-S08 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S08-001 | Universal / Safe | Sunlit | A | Open horizontal sequence with circular stage numbers |
| ENG-S08-002 | Premium / Editorial | Terracotta | A | Editorial process rows beneath a split introduction |
| ENG-S08-003 | Structured / Visual Modular | Tidal | A | Progressively inset process bands with a contrasting final stage |
| ENG-S08-004 | Conversion-led | Daybreak | A | Preparation-led first stage beside the introduction, followed by later stages |
| ENG-S08-005 | Art-directed / Distinctive | Night Current | A | Dark descending triptych ending in a lime handover stage |

All five studies are AUTHORED. Closed copy is 140 words, or 148 in 004.
Opening the first disclosure increases this to 150 or 158 words respectively.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S06 and S07 studies, authoring standard
and media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Frame the brief, shape the approach and prepare the handover form an illustrative
process. The introduction explicitly describes a possible path and requires stages,
deliverables and responsibilities to be agreed for the site and available services.
This is not a verified provider workflow. Each disclosure reserves confirmed inputs,
reviews, approvals or handover responsibilities. No durations, outcomes, service
guarantees or credentials are invented. Supply verified workflow details before
publication.

Each Explore this stage control opens its own native details content. Accessible
names identify the stage. There are no dead links, pretend submissions, global
headers or footers, raw scripts or remote runtime dependencies.

## Composition, Media and Responsive Decisions

The five established themes remain consistent. Different sequence layouts,
number treatments, stage emphasis and introduction placement distinguish the
studies. A labelled ordered list preserves the stage sequence, with a labelled
H3 for each item under the section H2. No blueprint, schedule or document metaphor.

Media slots: NONE. The process is communicated through ordered stages, typography
and colour; the preceding infrastructure section provides photographic context.
S06 was A and S07 was B; S08 begins a new A sequence.

Below 850px all stages stack in DOM order. Progressive insets and descending
positions reset, and expanded details remain in normal flow. Scoped CSS includes
border-box descendants, visible focus, reduced-motion treatment and controls at
least 44px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed, first-open or all-open.
- Metadata, unique IDs, labelled headings and three stage groups checked;
  ordered-list markup inspected.
- All disclosures open, close, accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five process layouts](../../../review/energy-process.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-process.ps1

Measured heights: ../../../review/energy-process-heights.json.
Next: S09-certifications-standards.
