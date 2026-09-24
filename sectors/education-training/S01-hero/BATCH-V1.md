# BATCH V1

Current integration note (S02): the initial disclosures documented below have been replaced by native same-variant S02 catalogue links. The original layout/media remain. All five links and 20 viewport checks passed. Historical disclosure QA below records the initial S01 authoring state.

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S01
- Section Name: Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 5 studies, S01 authored.

## Planned Studies

| Study | Direction | Theme | Shape | Media | Words closed / open | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S01-001 | Universal / Safe | Apricot | B | 2 | 61 / 77 | Split headline and offset learning-space pair |
| EDU-S01-002 | Premium / Editorial | Mulberry | B | 1 | 53 / 69 | Large editorial headline beside a tall studio image |
| EDU-S01-003 | Structured / Visual Modular | Cobalt | B | 3 | 63 / 79 | Broad opening above three unequal learning images |
| EDU-S01-004 | Conversion-led | Iris | C | 0 | 74 / 90 | Question-led headline with a purple exploration field |
| EDU-S01-005 | Art-directed / Distinctive | Afterhours | B | 2 | 53 / 69 | Oversized lime type above staggered image windows |

All five raw files use the matching stable ID as filename and metadata.

## Research Metadata

Sources: user's modern/non-classical direction; sector README and SECTOR-BRIEF;
section README; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; newly established
../EDUCATION-THEME-CONTRACT.md. External research: NONE.

The sector had no authored studies or theme contract. This batch establishes five
education-specific themes for subsequent sections. The hero frames exploring an
interest, returning to a subject and choosing a learning direction. No institution,
programme, delivery format, qualification, success statistic or employment promise
is invented. No teacher or learner is depicted or quoted.

Document-metaphor justification: NONE. No academic crest, administrative form,
certificate, transcript, chalkboard or technical schedule is presented.

## Differentiation and Responsive Behaviour

001 combines a readable introduction with an asymmetric two-image composition.
At 760px the copy and action lead; the shorter image retains an offset.

002 uses a tall single media anchor, lighter display typography and an editorial
closing line. On phones its image follows the headline and action.

003 supports visual capacity through three unequal image areas, rather than longer
copy. At 760px the first image spans the row; the two supporting images form a pair.
This is a hero media group, not a programme catalogue.

004 is intentionally shape C: the question and programme-exploration action carry
the composition. Its purple action field follows the introduction on phones.
No lead form, artificial urgency or enrolment claim.

005 uses lime display type on a dark olive ground and a lower pair of differently
cropped media windows. On phones the headline, action and media stay in that order.

This is the first education section, so no preceding two-section comparison exists.
S01 establishes the shape row B / B / B / C / B. Later batches must compare actual
layouts, not just theme colours. The CONS-specific collision checker is not counted
as education validation.

## Media Slots

Eight reserved photo areas total.

| Subject | Study | Purpose | Expected type | Fallback |
| --- | --- | --- | --- | --- |
| Collaborative learning space | 001 | Group-learning context | Actual institution learning-space photo | Labelled empty figure |
| Practical learning studio | 001, 003, 005 | Hands-on learning context | Verified studio photograph | Labelled empty figure |
| Learning studio | 002 | Large editorial anchor | Actual learning environment | Labelled empty figure |
| Group learning space | 003 | Primary learning context | Verified space photograph | Labelled empty figure |
| Independent study space | 003 | Supporting quiet-study context | Actual study setting | Labelled empty figure |
| Shared study space | 005 | Complement the practical studio | Verified shared learning space | Labelled empty figure |

All captions remain visible and each reservation has an accessible subject label.
No generated faces or external assets. Actual photography requires provenance,
permission and appropriate alt text. 004 intentionally has zero media.

## Interaction and Integration

S02-programs-courses is still scaffolded. The primary control is a native details/
summary disclosure that explains programme information is being prepared.
It is not a broken navigation link or a fabricated course catalogue.
Opening reveals a concise status message; closing restores the hero.

Replace this temporary disclosure with the confirmed programme route when the
catalogue destination is authored/integrated. No form sends data or claims enrolment.
The raw hero carries no JavaScript. The gallery uses its own script for previews.
Cached iframe heights reserve enough space for the expanded state when local-file
security prevents live access; accessible frames use live measurements.

## QA

- 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow in either disclosure state.
- Stable metadata, unique IDs, one H1 and labelled section checked.
- No global shell, frameworks, remote assets or broken links.
- Native disclosure starts closed, receives focus, opens and closes successfully.
- Control target height is at least 44px. Revealed status text is visible.
- All five desktop and 390px screenshots visually reviewed.
- Gallery tests passed: five frames, variant selection, mobile width, pressed state,
  restore-all and full-size links.
- Reduced-motion CSS included. git diff --check has no whitespace errors.
- Cross-browser and screen-reader testing were not run.
- No Design Lab ingestion or production publication claimed.

## Review

[Compare five education heroes](../../../review/education-hero.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-hero.ps1

Measured heights: ../../../review/education-hero-heights.json.
Next section: S02-programs-courses.

