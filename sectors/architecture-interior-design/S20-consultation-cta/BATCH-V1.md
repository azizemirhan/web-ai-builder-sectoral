# BATCH V1 — ARC S20 Consultation CTA

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S20
- Section Name: Consultation CTA
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S20-001 — Universal / Safe

- Structural intent / archetype: Centered consultation panel with primary and secondary actions plus expectation-setting details.
- Layout model: Bordered single-panel composition.
- Density: Low; two actions and three concise session notes.
- Media mode: No media required.
- Interaction: Native consultation and project-note links.
- Responsive strategy: Centered wide panel → stacked full-width mobile actions.
- Composer value: Reliable closing CTA for most architecture and interior studio pages.
- Limitation / content ceiling: Best as a page-ending action; it does not differentiate several consultation services.

### ARC-S20-002 — Premium / Editorial

- Structural intent / archetype: Editorial statement describing one useful first session through a three-part agenda.
- Layout model: Oversized numeric/title field paired with details, agenda and action.
- Density: Low with deliberate narrative pacing.
- Media mode: No media required.
- Interaction: One native request link.
- Responsive strategy: Split editorial sheet → stacked statement and agenda.
- Composer value: Frames consultation as a thoughtful working session rather than a generic sales call.
- Limitation / content ceiling: Assumes a single featured consultation format.

### ARC-S20-003 — Dense / Information-heavy

- Structural intent / archetype: Comparative menu of three consultation formats with purpose and delivery mode.
- Layout model: Five-column desktop index transforming into compact mobile records.
- Density: High; each option exposes audience, duration and format.
- Media mode: No media required.
- Interaction: Native session and guidance links.
- Responsive strategy: Table-like menu → labeled mobile records with retained action targets.
- Composer value: Useful when a practice offers several distinct ways to begin.
- Limitation / content ceiling: More than 4–5 formats would need grouping; service details must be verified before ingestion.

### ARC-S20-004 — Conversion-led

- Structural intent / archetype: Consultation request combining expectation-setting with a short scheduling form.
- Layout model: Introductory process panel beside a five-field request form.
- Density: Medium and directly action-oriented.
- Media mode: No media required.
- Interaction: Native select, date, contact fields and browser validation.
- Responsive strategy: Split request panel → stacked explanation and form → single-column mobile fields.
- Composer value: Reduces steps between interest and a specific consultation request.
- Limitation / content ceiling: No calendar availability, time-zone logic, confirmation or backend delivery is implemented.

### ARC-S20-005 — Sector-native / Distinctive

- Structural intent / archetype: Architecture-style meeting sheet dividing a consultation into context, priority and action.
- Layout model: Three-column agenda drawing with time blocks, vertical axis and closing request strip.
- Density: Medium-high and diagrammatic.
- Media mode: No media required; native HTML/CSS forms the sheet.
- Interaction: One native request link.
- Responsive strategy: Horizontal agenda → vertically stacked timed records with preserved axis.
- Composer value: Gives the consultation CTA a recognizable studio-workshop character.
- Limitation / content ceiling: Communicates one session structure, not a full booking or service catalogue.

## Research Metadata

- Research inputs: Workspace authoring standards, Architecture & Interior Design sector taxonomy and the established requirement to avoid generated visuals.
- Research date: 2026-08-31
- Structural territory rationale: The set covers universal closing action, editorial framing, option comparison, direct scheduling and architecture-native agenda territories.
- Differentiation notes: No live booking service, fee, availability, guaranteed response, factual duration or external destination is embedded.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S20-001 | No media slots | — | CTA meaning is entirely textual. |
| ARC-S20-002 | No media slots | — | Editorial composition uses native type and structure. |
| ARC-S20-003 | No media slots | — | Session comparison is entirely textual. |
| ARC-S20-004 | No media slots | — | Request form is entirely semantic and textual. |
| ARC-S20-005 | No media slots | — | Agenda marks are native CSS and non-essential to the textual agenda. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions, one clear H1, explicit form labels, visible keyboard focus and practical touch targets verified.
- Responsive QA: PASS — 35 in-browser checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — all CTA targets resolve; the request form blocks empty submission, focuses the first invalid field and accepts valid sample data before local-only submission.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — 0 media slots, embedded images, SVGs, video, gradients or background-image assets.

## Known Batch Boundaries

- The consultation request form submits only to its own local fragment and does not transmit or store data.
- Durations, session names and delivery modes are illustrative content rather than a factual service offer.
- Booking, calendar, time-zone, confirmation and backend submission behavior remain integration responsibilities.
