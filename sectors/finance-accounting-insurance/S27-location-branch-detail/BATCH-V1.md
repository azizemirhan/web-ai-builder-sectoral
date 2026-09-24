# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S27
- Section Name: Office Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-16
- Sector total: 135 studies; S01-S27 authored. The sector catalogue is complete.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S27-001 | Universal / Safe | Ivory & Olive | B | Address and contact block first, beside a reserved map area, with an office photograph and the visit details beneath |
| FIN-S27-002 | Premium / Editorial | Rosewood | C | Address set as display type, contact and hours as a ruled ledger, visit details in a centred column; no map, no photograph |
| FIN-S27-003 | Structured / Visual Modular | Lagoon | B | Address, contact and hours tiles in the first row, a reserved map beside getting-here, a photograph beside people and services |
| FIN-S27-004 | Conversion-led | Iris | B | Address, contact and visit route in an accent panel that leads, a reserved map beside it, visit details in three columns |
| FIN-S27-005 | Art-directed / Distinctive | Ink & Apricot | C | Wayfinding card: the address in apricot display type, a ruled contact strip, arrival, services and people in three columns; no map, no photograph |

All five raw files are authored. Visible copy, reserved fields included, is 161, 162,
163, 154 and 163 words against the 150-230 detail band. S25 ran B B C B B and S26 ran
B C B B B; this row is B C B B C, the first row in the S21-S27 architecture to carry
two type-only studies. Both are deliberate: a map here is a reserved slot, not a
service, and an office page whose whole content is a verified address is honest when
it lets the address do the work.

## Research Metadata and Scope

Sources: user continuation request, canonical section README and its warning that a
plausible fabricated address is this role's failure mode, the S18 offices index,
FIN-S23 to FIN-S26 and FINANCE-THEME-CONTRACT.md. Research date: 2026-09-16. External
research: NONE. Document-metaphor justification: NONE.

This is the depth page behind one entry in S18. Every study carries the same
responsibilities: region label, office name, staffed-office or meeting-location
status, address in four reserved lines, local telephone and email, visiting hours
with timezone, appointment requirements, what happens at this location, getting here
(entrance and transport, parking, access, on arrival), people based here, a route to
plan a visit, and a return to the index. Every address line, contact detail, hour,
arrival note and person is a bracketed reserved field. No coordinate, postcode,
telephone number, hour or direction is invented anywhere in the batch, and no study
links a telephone or email because there is nothing verified to link.

The address and contact block is the first content after the title in every study,
and on a phone it precedes every map area and photograph.

## Media Slots

Five reserved slots across the batch: a map area and an office photograph in 001 and
003, a map area alone in 004, and none in 002 or 005. Every map area is a labelled
region with an accessible description stating that no map service is embedded, and a
visible caption saying a map appears only once the address has been verified. The two
studies without slots say the same in a note. No study loads a third-party map, a
tile, a script or any remote resource. Office photographs, where reserved, have a
caption field and sit below the address and visit details.

## Interaction and Responsive Decisions

Relative links only, at the same variant: the visit route to S19, people to S04, the
return to S18. No form, no script, no external dependency. Targets are at least 44px
tall. Focus is a 3px accent outline, switched to paper inside 004's accent panel.

001 pairs the address card with the map at .9/1.1, then three detail tiles and a
full-width photograph. 002 is a single column under a display-type address and a
four-column ledger. 003 runs a three-tile row, then map beside getting-here, then
photograph beside services and people. 004 leads with the accent panel beside the
map, then three detail tiles. 005 sets the address card full width and the details
in three columns. Below 850px every pairing stacks with the address block first,
maps become 16:9, and ledgers drop to two columns then one. Reduced motion disables
all animation and transition.

## QA

- Passed structural checks on all five: theme tokens and radius per contract, host
  background, 1400px frame, reduced-motion block, namespace scoping, tag balance, no
  dependency, no claim, no figure, relative links only, focus-visible present, no
  solid divider carrying its own max-width, no inline style attribute.
- Content parity: twenty-one shared fields plus three same-variant link targets,
  120/120 slots present.
- Measured heights at 1440, 768, 390 and 320px are in the review folder; the tallest
  study is 003 at 768px, 2788px, where three two-column rows stack.
- Rendered and read at 1440 and 390px, including the address-first order on a phone.
  The first pass came in at 129-138 words, under the band; an on-arrival reserved
  field and a preparation sentence were added to every study as required content
  rather than padding, and 001's getting-here list gained its missing row spacing.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five office detail layouts](../../../review/finance-office-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-office-detail.ps1

Measured heights: ../../../review/finance-office-detail-heights.json.
Next: none. S01-S27 are authored; the sector awaits Design Lab ingestion.
