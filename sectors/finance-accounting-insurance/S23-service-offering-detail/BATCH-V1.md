# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S23
- Section Name: Advisory / Financial Service Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-16
- Sector total: 115 studies; S01-S23 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S23-001 | Universal / Safe | Ivory & Olive | B | Detail body beside a supporting photograph and enquiry column |
| FIN-S23-002 | Premium / Editorial | Rosewood | B | Editorial column beneath a panoramic photograph and an at-a-glance row |
| FIN-S23-003 | Structured / Visual Modular | Lagoon | B | Modular tiles for scope, stages and suitability with a compact photograph in the closing band |
| FIN-S23-004 | Conversion-led | Iris | B | Detail body beside a persistent enquiry panel that releases to flow at tablet |
| FIN-S23-005 | Art-directed / Distinctive | Ink & Apricot | C | Dark stage spine with apricot numerals and an in-page index rail |

All five raw files are authored. Visible copy, reserved fields included, is 217, 229,
217, 217 and 230 words against the 150-230 detail band. S21 ran B C B C B and S22 ran
C at every variant, so no A sequence exists to extend; a detail page carries media as
support rather than subject, so no A was authored here either. The C moves to 005,
where the stage spine carries the page in type and colour alone.

## Research Metadata and Scope

Sources: user continuation request, canonical section README, FIN-S21 and FIN-S22
studies, the S02 services index, and FINANCE-THEME-CONTRACT.md. Research date:
2026-09-16. External research: NONE. Document-metaphor justification: NONE.

This is the depth page behind one entry in the S02 services index. Every study carries
the same eleven content responsibilities: category line, offering title, overview,
what it includes, what it does not include, how it runs in three stages, who it is for
and the conditions that apply, related offerings, a route to enquire, a preparation
note, and a reserved photograph or its deliberate absence. All firm-specific content
is a reserved field in brackets; the visible copy is neutral invitation language and
makes no claim about availability, fees, outcomes, turnaround or regulatory status.
Stage names and contents are reserved rather than invented, because a firm's
engagement sequence is a fact about the firm.

## Media Slots

One reserved offering-context photograph in 001, 002, 003 and 004; four slots total.
None in 005. Desktop regions are 280px tall in 001, 340px panoramic in 002, a square
in the closing band of 003 and 220px in 004's rail. Each slot has allocated space, a
visible reserved-image label, an accessible description and a named caption field.
Media illustrates the offering and never carries it: every page reads complete with
the slot empty. Obtain licensing, provenance, applicable participant consent and
final descriptive alt text before publication.

## Interaction and Responsive Decisions

Relative links only, all within the sector and at the same variant: the enquiry route
goes to S19 contact and S20 consultation, related offerings to S02, and reading to
S13. No form, no email field, no script, no external dependency. A native details
element exposes a preparation note without implying submission or contact delivery.
005 adds an in-page index of anchor links, which degrade to plain links. Link and
summary targets are at least 44px tall. Focus is a 3px accent outline; inside 004's
accent-field panel the outline switches to paper so that it contrasts with its actual
surface.

Body measure is held to 64-66ch at every width where columns exist. 001 and 004 pair
the body with a right column at 1.2/0.8; 004's panel is sticky at desktop and
releases to normal flow at 1100px, before it can compete with the body. 002 centres a
66ch column beneath the panorama. 003 runs three-tile rows for scope and stages and
a three-column closing band. 005 holds a 220px index rail beside a 72ch spine; the
rail becomes a wrapped row at 1100px and the spine tightens at 850 and 560px. Below
850px every layout is a single column and photographs reduce to 190-260px. Reduced
motion disables all animation and transition.

## QA

- Passed structural checks on all five: theme tokens and radius per contract, host
  background, 1400px frame, reduced-motion block, namespace scoping, tag balance, no
  dependency, no claim, no figure, relative links only, focus-visible present, and no
  solid divider carrying its own max-width.
- Content parity: fourteen shared fields plus four same-variant link targets, 90/90
  slots present across the five studies.
- Measured heights at 1440, 768, 390 and 320px are in the review folder; the tallest
  study is 002 at 320px, 3095px, and the shortest desktop study is 003 at 1261px.
- Rendered and read at 1440 and 390px. Three faults were found and fixed before the
  batch closed: a head divider cut short by its own max-width in 001; a general
  `li+li` margin displacing the second and third stage tiles in 003's grid; and a
  68ch head constraint wrapping 005's title early. The body/rail column ratio in 001
  and 004 was rebalanced from 1.35/0.65 to 1.2/0.8 to close a dead gap beside the
  measure.
- A 390px screenshot taken directly from a 390px Chrome window is not a 390px render:
  headless Chrome enforces a wider minimum window and crops. Phone renders are
  therefore captured through a 390px iframe inside a wider window, which is also how
  the heights are measured.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five service detail layouts](../../../review/finance-service-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-service-detail.ps1

Measured heights: ../../../review/finance-service-detail-heights.json.
Next: S24-project-case-study-detail.
