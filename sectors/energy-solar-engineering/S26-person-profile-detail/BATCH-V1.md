# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S26
- Section Name: Engineer / Expert Profile
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 130 studies; S01-S26 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S26-001 | Universal / Safe | Sunlit | B | Portrait and identity rail beside a continuous biography |
| ENG-S26-002 | Premium / Editorial | Terracotta | B | Editorial name and portrait opening above paired biography columns |
| ENG-S26-003 | Structured / Visual Modular | Tidal | B | Compact portrait, teal identity panel and offset biography |
| ENG-S26-004 | Conversion-led | Daybreak | B | Blue portrait profile with a prominent contact pathway |
| ENG-S26-005 | Art-directed / Distinctive | Night Current | B | Centered identity, arched portrait and lime biography opening |

Visible copy: 159 words per study; all biography content is always visible.

## Research Metadata and Scope

Sources: user continuation request, section README, theme contract, preceding
studies and repository media policy. Research date: 2026-09-15. External research:
NONE. Document-metaphor justification: NONE.

Each study describes exactly one person. Name, professional role, focus, biography,
working approach, contributions and background are explicit reserved fields.
No qualifications, registrations, memberships, awards, employers or project credits
are invented. Contributions must distinguish the person's responsibilities from
team achievements and have publication permission. Specific work or service links
are deferred until an actual relationship is supplied; existing sample projects
are not falsely attributed to this unnamed person.

## Portrait

One portrait per study; five reserved slots total. Expected type: a photograph of
the named real person with consent to appear. Its purpose is recognition and
identity. The portrait remains paired with the name within the identity container
at every width. A visible caption and accessible label identify the reserved slot.
Before ingestion, supply consent, licensing, provenance and accurate alternative
text. Fallback: retain the labelled allocated portrait area; the full profile
remains understandable without an image.

## Interaction and Responsive Decisions

One labelled section has an H2 and one named article with four H3 biography groups.
No hidden biography, disclosure, raw script, form or invented social link. A native
contact link opens the existing S20 variant with the same number. This is a route
to team contact options, without implying direct delivery to a named expert.
The destination contains reserved contact fields that require real details before
publication. Production contact routing belongs to ingestion.

Desktop layouts vary identity placement, portrait proportions, biography columns
and contact emphasis. Mobile uses normal document flow, retains the complete
profile and pairs the identity with its portrait. Scoped CSS includes readable
text measures, border-box descendants, visible focus, a 44px minimum link target
and reduced-motion treatment. No remote dependencies. S24, S25 and S26 use shape B.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Identity metadata, heading structure, unique IDs, portrait count and word budget
  checked. Biography visibility and portrait/identity grouping passed.
- No document or element overflow.
- Contact links accept focus, meet target height and retain matching variant IDs.
  Every relative destination verified on disk.
- Five desktop and five phone screenshots visually reviewed. Editorial column
  alignment refined and browser checks repeated.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five expert profiles](../../../review/energy-profile-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-profile-detail.ps1

Measured heights: ../../../review/energy-profile-detail-heights.json.
Next: S27-location-branch-detail.
