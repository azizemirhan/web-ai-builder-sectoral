# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S26
- Section Name: Advisor / Expert Profile
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-16
- Sector total: 130 studies; S01-S26 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S26-001 | Universal / Safe | Ivory & Olive | B | Identity block pairing a portrait with name, role and focus, above a two-column profile and a contact panel |
| FIN-S26-002 | Premium / Editorial | Rosewood | C | Profile in type alone: name set large, role and focus as a running head, a centred column and a facts ledger; no portrait |
| FIN-S26-003 | Structured / Visual Modular | Lagoon | B | Identity card with a compact portrait and facts beside a modular grid of focus, work, background and contact tiles |
| FIN-S26-004 | Conversion-led | Iris | B | Contact route in an accent band directly under the identity row, then the profile body beside a facts rail |
| FIN-S26-005 | Art-directed / Distinctive | Ink & Apricot | B | Tall portrait beside the name set large, focus areas as apricot pills, the profile running beneath in two columns |

All five raw files are authored. Visible copy, reserved fields included, is 159, 156,
159, 158 and 159 words against the 150-230 detail band. S24 ran B C A B B and S25 ran
B B C B B; this row is B C B B B. The C sits at 002 because the role's own brief says a
profile must read completely with the portrait absent, and one study should prove it
rather than assert it.

## Research Metadata and Scope

Sources: user continuation request, canonical section README and its note that nothing
in this role may be invented, the S04 advisers index, FIN-S23 to FIN-S25 and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-16. External research: NONE.
Document-metaphor justification: NONE.

This is the depth page behind one entry in S04. Every study carries the same
responsibilities: team or office label, name, verified role, area of focus, how they
work, areas of focus, the services and work they are attached to, professional
background, team, office and languages, a contact route through the firm, a
preparation note, a statement that the page was supplied by the person and cleared
for publication, and a return to the index. Name, role, focus, background,
qualifications, registrations, office, languages and every link label are reserved
fields. No social handle, personal address, rating or testimonial appears. The one
route to the person is the firm's contact page at the same variant, and the visible
copy says so.

## Media Slots

Four reserved portrait slots, one each in 001, 003, 004 and 005; none in 002. A filled
slot means a real person who has consented to appear, and the accessible description
says so. Each portrait sits inside the same block as the name, role and focus at every
width, so that reflow can never place a name beside the wrong portrait: 001 and 005
pair them in a two-column identity grid that stacks in source order; 003 keeps both
inside one card; 004 pairs a circular portrait with the name in a fixed two-column
row that narrows rather than breaks. Portrait shapes vary by study: 4:5 in 001,
square in 003, circular in 004, 3:4 in 005. Every slot has allocated space, a visible
reserved label and a caption field, and every page reads complete without it.

## Interaction and Responsive Decisions

Relative links only, at the same variant: the contact route to S19, attached work to
S02 and S11, the return to S04. No form, no script, no external dependency. Targets
are at least 44px tall. Focus is a 3px accent outline, switched to paper or white
inside the accent-field contact panels of 003 and 004.

001 runs a 260px portrait beside the identity, then a 64ch body beside a contact
panel. 002 is a 60ch column under a large name. 003 holds a sticky 340px card beside a
two-column tile grid, and at 850px the card becomes a portrait-and-identity row above
the tiles. 004 places the contact band full-width under the identity, then a 64ch body
beside a facts rail. 005 runs a 3:4 portrait beside the name at .55/1 and the profile
in two columns below. Everything is a single column below 850px except 004's
identity row, which narrows to 120px at 560px. Reduced motion disables all animation
and transition.

## QA

- Passed structural checks on all five: theme tokens and radius per contract, host
  background, 1400px frame, reduced-motion block, namespace scoping, tag balance, no
  dependency, no claim, no figure, relative links only, focus-visible present, no
  solid divider carrying its own max-width.
- Content parity: nineteen shared fields plus four same-variant link targets, 115/115
  slots present.
- Measured heights at 1440, 768, 390 and 320px are in the review folder; the tallest
  study is 001 at 320px, 2320px, and the shortest desktop study is 003 at 993px.
- Rendered and read at 1440 and 390px, including the identity reflow in 001. One
  correction before close: the checker caught a facts rule in 001 carrying its own
  max-width, and the constraint was removed.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five profile layouts](../../../review/finance-profile-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-profile-detail.ps1

Measured heights: ../../../review/finance-profile-detail-heights.json.
Next: S27-location-branch-detail.
