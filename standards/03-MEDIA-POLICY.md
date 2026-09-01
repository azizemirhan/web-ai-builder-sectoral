# Media Policy

This policy applies to every authored raw study.

## Reserved Media Areas

- Represent required imagery and media through documented media slots.
- Record each slot's purpose, expected type, accessibility text requirement, and fallback behavior
  in batch metadata.
- Keep studies free of CDN and remote runtime dependencies.
- Do not embed production-owned assets or credentials.
- Ensure a study remains structurally understandable when optional media is unavailable.
- Treat licensing and provenance as required research metadata before ingestion.

Reserved regions such as `IMAGE AREA`, `VIDEO AREA`, `PORTRAIT AREA`, `PROJECT MEDIA` and
`SAMPLE AREA` are valid, intended output. **An empty reserved media area is not a failed design.**
It is the correct state of a study whose real media does not exist yet, and it must not be
recorded as a defect in QA or review.

## Do Not Fabricate

Do not invent projects, buildings, people, products, evidence, logos, awards, certifications,
ratings, publications, addresses or locations in order to make a study look visually complete.
Placeholder tokens and reserved fields are the correct answer where a real fact would be required.

## Reserve Enough Space for the Real Experience

Where the real final experience fundamentally depends on media, the structural study **should
reserve enough appropriate media space to demonstrate that relationship** — at the right scale,
in the right position, with the right proportion.

A visually oriented section must not quietly become text-only merely because real media cannot be
fabricated. A gallery with no media areas, a project page with one small thumbnail, or a materials
section with no sample areas has not demonstrated its role; it has avoided it.

## Media Density

A section should not prove capacity by displaying an excessive number of simultaneous media items.
Prefer controlled visual editing: fewer, better-placed, better-proportioned media areas that show
the intended relationship.

There is no single global maximum — a contact-sheet role and a hero role legitimately differ — but
excessive simultaneous media density is discouraged in every sector, and sector-level guidance may
set a specific conventional maximum for a particular section role.
