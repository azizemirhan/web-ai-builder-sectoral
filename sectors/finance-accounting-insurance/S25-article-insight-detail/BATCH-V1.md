# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S25
- Section Name: Financial Insight / Guidance Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-16
- Sector total: 125 studies; S01-S25 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S25-001 | Universal / Safe | Ivory & Olive | B | Article with an attribution row, a contained lead photograph and a single reading column |
| FIN-S25-002 | Premium / Editorial | Rosewood | B | Editorial piece with a panoramic lead, a centred reading column, a key-point inset and one in-body figure |
| FIN-S25-003 | Structured / Visual Modular | Lagoon | C | Reading page with a sticky in-page contents rail, numbered section modules and an attribution panel |
| FIN-S25-004 | Conversion-led | Iris | B | Reading column beside a right rail carrying a small lead photograph, related reading and a quiet conversation panel |
| FIN-S25-005 | Art-directed / Distinctive | Ink & Apricot | B | Dark reading page with an oversized title, an apricot standfirst, a shallow lead strip and a 20px measure with apricot section numerals |

All five raw files are authored. Visible copy, reserved fields included, is 152, 175,
158, 172 and 152 words against the 150-230 detail band. S23 ran B B B B C and S24 ran
B C A B B; this row is B B C B B, so no A sequence exists and page three carries
B, A and C in turn rather than repeating a shape.

## Research Metadata and Scope

Sources: user continuation request, canonical section README, the S13 resources index,
FIN-S23, FIN-S24 and FINANCE-THEME-CONTRACT.md. Research date: 2026-09-16. External
research: NONE. Document-metaphor justification: NONE.

This is the depth page behind one entry in S13, and it is judged on reading comfort.
Every study carries the same responsibilities: topic label, title, standfirst,
attribution (author or reviewer role, review date, jurisdiction where relevant), a
three-section body with headings, a general-information qualification, related
reading, a return to the index and a quiet route to a conversation. No author,
publication, date, citation or piece of advice is invented; every one is a reserved
field. The three body placeholders are section-specific author instructions rather
than one repeated string, because the heading hierarchy is the content of this role
and a template that hides it would be hiding the thing being judged.

The one sentence of visible copy that addresses advice says that the piece is general
information and not advice on the reader's circumstances, and it appears in all five.

## Media Slots

Five reserved slots across the batch: one lead in 001, a panoramic lead and one
in-body figure in 002, none in 003, one lead in 004's rail, and a shallow lead strip
in 005. Every slot has allocated space, a visible reserved-image label, an accessible
description and a caption field that belongs to the study rather than to alt text.
Body media sits inside the reading measure and never widens it; 002's in-body figure
is the only slot placed within the column and it inherits the column's width.

003 carries none: the structured reading is navigation and hierarchy, and a photograph
would compete with the contents rail for the reader's first glance.

## Interaction and Responsive Decisions

Relative links only, at the same variant: related reading and the return go to S13,
the conversation route to S19. 003 adds in-page anchors, which degrade to plain links.
No form, no script, no external dependency. Targets are at least 44px tall. Focus is
a 3px accent outline, switched to paper inside 004's accent panel.

The reading measure is 60-66ch in every study and the body font is 17-20px. 001 and
002 are single columns; 003 holds a 260px sticky rail beside a 64ch body; 004 holds a
64ch body beside a sticky 300px-plus rail; 005 sets a 200px byline column beside a
60ch body at 20px. Rails release at 1100px into a two-column row and to one column
at 850px. Below 560px bylines stack, bodies drop to 16-17px, and lead photographs
reduce to 150-200px. Reduced motion disables all animation and transition.

## QA

- Passed structural checks on all five: theme tokens and radius per contract, host
  background, 1400px frame, reduced-motion block, namespace scoping, tag balance, no
  dependency, no claim, no figure, relative links only, focus-visible present, no
  solid divider carrying its own max-width.
- Content parity: sixteen shared fields plus two same-variant link targets, 90/90
  slots present.
- Measured heights at 1440, 768, 390 and 320px are in the review folder; the tallest
  study is 002 at 1440px, 2431px, on account of the panoramic lead.
- Rendered and read at 1440 and 390px. The first pass came in at 137-160 words, three
  studies under the band; the body placeholders were rewritten as section-specific
  instructions rather than padded, which brought every study inside it.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five article detail layouts](../../../review/finance-article-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-article-detail.ps1

Measured heights: ../../../review/finance-article-detail-heights.json.
Next: S26-person-profile-detail.
