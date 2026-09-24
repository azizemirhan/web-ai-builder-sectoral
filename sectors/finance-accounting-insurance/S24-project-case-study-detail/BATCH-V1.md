# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S24
- Section Name: Client Engagement / Case Context Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-16
- Sector total: 120 studies; S01-S24 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S24-001 | Universal / Safe | Ivory & Olive | B | Lead photograph above a metadata rail and a narrative column with a second photograph set inside it |
| FIN-S24-002 | Premium / Editorial | Rosewood | C | Long-form engagement narrative in a centred column with an inset agreement panel and a closing engagement record |
| FIN-S24-003 | Structured / Visual Modular | Lagoon | A | Documented media set of four captioned context photographs above narrative tiles, a stage row and the engagement record |
| FIN-S24-004 | Conversion-led | Iris | B | Narrative beside a left rail holding one context photograph and a similar-situation enquiry panel that releases at tablet |
| FIN-S24-005 | Art-directed / Distinctive | Ink & Apricot | B | Engagement told as three delivered stages, each an apricot-numbered card pairing a context photograph with what was handed over |

All five raw files are authored. Visible copy, reserved fields included, is 178, 162,
196, 186 and 205 words against the 150-230 detail band. S22 ran C at every variant and
S23 ran B B B B C; the A at 003 is the first in the S21-S27 architecture and does not
extend any sequence. The C sits at 002 rather than 005, so that page five does not
carry three type-only sections in a row.

## Research Metadata and Scope

Sources: user continuation request, canonical section README and its sector semantic
limitation, the S11 case-study index, FIN-S23 and FINANCE-THEME-CONTRACT.md. Research
date: 2026-09-16. External research: NONE. Document-metaphor justification: NONE.

This is the depth page behind one entry in the S11 index and inherits its limitation:
anonymised engagement context, no performance, return or outcome claim. Every study
carries the same responsibilities: engagement type and title, the situation, what was
agreed, the approach, what was delivered by stage, who was involved, an engagement
record of discipline, scope and period, a publication note, a return to the index and
a route to talk about a similar situation. Every firm-specific field is reserved in
brackets. The one sentence of visible copy that addresses results says that the
account describes the work and not its results, and it appears in all five.

## Media Slots

Ten reserved slots across the batch: two in 001, none in 002, four in 003, one in 004
and three in 005. Four slot purposes are defined, and each is named in the slot's
`data-media` value and its accessible description.

| Purpose | Expected type | Fallback |
| --- | --- | --- |
| engagement-context | The working environment for the engagement, with no client present and nothing identifying in frame | Labelled region remains; page reads complete without it |
| review-session | A consented review session showing the team's side only, not the client | As above |
| materials | Materials in review, photographed so that nothing is legible | As above |
| handover | The delivered set at handover, closed, with no readable content | As above |

002 carries none. An anonymised engagement has nothing honest to photograph that the
other four studies do not already reserve, and the editorial reading is stronger for
carrying the whole account in type. Every slot in the other four has allocated space,
a visible reserved-image label, an accessible description that states what must not
be in the frame, and a caption field. Obtain licensing, provenance, participant
consent and confirmation that no client is identifiable before publication.

## Interaction and Responsive Decisions

Relative links only, all at the same variant: the return goes to S11, the enquiry
route to S19, and the involved services and people to S02 and S04. No form, no
script, no disclosure, no external dependency. Targets are at least 44px tall. Focus
is a 3px accent outline, switched to paper inside 004's accent panel.

001 stacks a full-width lead photograph, then a 240px metadata rail beside a 66ch
narrative that carries the second photograph between the approach and the stages.
002 is a single 64ch column. 003 runs the four-slot set as a row, then three tiles,
then a three-tile stage row, then a two-column closing band. 004 holds a sticky left
rail of photograph, panel and metadata beside a 64ch body; the rail releases at
1100px into a two-column row and to one column at 850px. 005 lays each stage as a
three-column card of numeral, text and photograph, dropping to two columns at 1100px
and one at 850px. Reading order is source order at every width; no media set scrolls
horizontally. Reduced motion disables all animation and transition.

## QA

- Passed structural checks on all five: theme tokens and radius per contract, host
  background, 1400px frame, reduced-motion block, namespace scoping, tag balance, no
  dependency, no claim, no figure, relative links only, focus-visible present, no
  solid divider carrying its own max-width.
- Content parity: nineteen shared fields plus four same-variant link targets, 115/115
  slots present.
- Measured heights at 1440, 768, 390 and 320px are in the review folder; the tallest
  study is 003 at 320px, 3183px.
- Rendered and read at 1440 and 390px. Two corrections before close: a heading placed
  directly inside a definition list in 003 was moved into a wrapping section, and
  005's closing line was un-indented so it no longer chases a column it did not sit
  in. 001 gained spacing between the stage list and its closing sentence.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five case detail layouts](../../../review/finance-case-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-case-detail.ps1

Measured heights: ../../../review/finance-case-detail-heights.json.
Next: S25-article-insight-detail.
