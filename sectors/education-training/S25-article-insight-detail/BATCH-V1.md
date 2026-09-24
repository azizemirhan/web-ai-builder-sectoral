# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S25
- Section Name: Article / Research Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 125 studies, S01-S25 authored.

## Studies

All five studies are AUTHORED. 001, 002 and 005 have 195 visible words; 003 and
004 have 189. The same complete short editorial appears in each composition.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S25-001 | Universal / Safe | Apricot | B | 1 | Warm reading column beside a quiet study-space image |
| EDU-S25-002 | Premium / Editorial | Mulberry | B | 1 | Editorial title and shallow panorama above a centred reading column |
| EDU-S25-003 | Structured / Visual Modular | Cobalt | C | 0 | Blue article introduction beside three grouped reading passages |
| EDU-S25-004 | Conversion-led | Iris | C | 0 | Open article with a focused further-reading rail |
| EDU-S25-005 | Art-directed / Distinctive | Afterhours | B | 1 | Oversized dark title, accented opening and curved supporting image |

## Research Metadata and Scope

Sources: user continuation request; S25 README; education theme contract;
preceding S23/S24 studies; existing S14 resources route; authoring standard and
media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Before you choose your next course is original sample editorial copy with a
standfirst and three complete passages: identifying an interest, considering an
ordinary week and reading the published course content. It contains no invented
institutional facts, research findings, citations, testimonials or outcome promises.
This explores the article role rather than simulating a research paper.

Author and publication date are explicit placeholders. No fake byline, timestamp
or publication identity is assigned. Confirm attribution and publication context
before using the study as published institutional content. The single Browse
learning resources link reaches the matching S14 raw study as a local review
handoff; it does not invent a related article or download.

## Reading and Responsive Decisions

Each study is one labelled article with one H2, three body H3 headings and a
further-reading H3. No primary navigation, enrolment form, marketing interruption,
contents menu, progress bar or unnecessary disclosure. Body copy remains readable
without JavaScript. Reading width is capped at 66ch, with 17px desktop body text
and 16px phone text, generous line height and consistent passage spacing.

001 places supporting media alongside the reading column. 002 places a shallow
panorama before a centred body. 003 separates introductory context and attribution
from three text groups. 004 gives the onward reading link a dedicated side panel
aligned with the end of the article. 005 adds a curved image and a lime opening
rule without turning that passage into an attributed quote.

Below 800px, columns return to normal flow: title, attribution, optional image,
body and related resources. Media becomes 240px high on phones. All controls have
visible focus and at least 44px target height; phone links use available width.
CSS is scoped with border-box sizing and reduced-motion treatment.

S23: C / C / C / C / C. S24: B / B / B / B / B. S25: B / B / C / C / B.
Raw scripts, frameworks, remote assets and runtime dependencies: NONE.

## Media Slots

Three total, one in 001, 002 and 005. Purpose: supporting atmosphere for reading
about learning. Expected type: an approved photograph of an actual quiet learning
space. Each slot includes a visible subject caption and accessible reserved-image
label. The allocated space and caption remain without an asset; the article is
complete independently of the photograph. Before publication supply provenance,
licensing, any needed consent, and final alt text describing the actual scene.
003 and 004 intentionally demonstrate comfortable reading without media.

## QA

- Passed 20 Chrome checks: all variants at 1440, 768, 390 and 320px.
- No document or element overflow; article identity, metadata and heading checked.
- Unique IDs, three body headings, two attribution fields and media counts checked.
- All five matching S14 destinations exist; links accept focus and meet target size.
- Five desktop and five phone screenshots visually reviewed. Attribution spacing
  and a mobile divider were refined after review.
- All variants fit the 150-230-word detail target.
- Gallery passed five frames, filtering, mobile width, pressed states, full-size
  links and restoration. Cached heights support local-file previews.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five article details](../../../review/education-article-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-article-detail.ps1

Measured heights: ../../../review/education-article-detail-heights.json.
Next: S26-person-profile-detail.
