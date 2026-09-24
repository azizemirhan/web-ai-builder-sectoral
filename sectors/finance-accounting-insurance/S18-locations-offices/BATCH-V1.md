# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S18
- Section Name: Locations Offices
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 90 studies; S01-S18 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S18-001 | Universal / Safe | Ivory & Olive | B | Office photograph beside an open visitor introduction |
| FIN-S18-002 | Premium / Editorial | Rosewood | B | Panoramic office above an editorial address layout |
| FIN-S18-003 | Structured / Visual Modular | Lagoon | B | Introduction and office information beside a tall image |
| FIN-S18-004 | Conversion-led | Iris | B | Visitor information and office image in a violet field |
| FIN-S18-005 | Art-directed / Distinctive | Ink & Apricot | B | Dark office panorama above an apricot visitor panel |

All five raw files are authored. Closed visible copy is 102 words; expanded copy
is 129 words. S17 used shape A; this B section resets the sequence.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Each variant presents one featured office introduction. Office name, physical
address, staffed-office or meeting-location status, visiting hours, timezone,
appointment requirements, services and local contact details remain reserved.
Arrival notes reserve verified entrance, transport, parking and accessibility
information. No real office, availability or accessibility feature is invented.
Directions and contact links require verified destinations before publication.

## Media Slots

One reserved office photograph per study; five slots total. Intended subject:
the verified exterior or reception of the named office. A generic building must
not be presented as an actual office. Confirm location identity and caption.

Each slot has allocated space, a visible reserved-image label, an accessible image
description and a named caption. Obtain licensing, provenance, property permissions,
applicable participant consent and final descriptive alt text before publication.
Exclude private records and identifying visitor details. Keep the labelled reserved
region as the fallback until approved imagery exists. Visitor information remains
understandable without photography.

## Interaction and Responsive Decisions

One labelled section with H2 contains one office article named by its H3. A native
Arrival and accessibility disclosure reveals reserved visitor guidance. No maps,
booking submissions, fabricated directions, raw scripts or external dependencies.

Desktop layouts vary through image proportions, order, split compositions and
coloured panels. Tablet and phone preserve introduction, image, caption and office
details in one reading order. Scoped CSS includes wrapping, border-box sizing,
visible focus, reduced-motion handling and summary targets of at least 48px.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, heading structure, reserved address and
  visiting fields, media-caption pairing and closed/expanded copy budgets.
- No document or element overflow with the disclosure closed or open.
- Summary accepts focus, meets target height and opens/closes correctly.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five office layouts](../../../review/finance-offices.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-offices.ps1

Measured heights: ../../../review/finance-offices-heights.json.
Next: S19-contact.
