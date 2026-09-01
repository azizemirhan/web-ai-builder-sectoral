# Authoring Standard

This document records the raw-study contract for every sector in the catalog.

Studies must:

- be standalone HTML;
- use scoped CSS;
- use vanilla JavaScript only when genuinely necessary;
- use no framework, CDN, or remote runtime dependency;
- carry a stable study ID and research metadata;
- follow the media-slot policy;
- provide accessible behavior;
- provide responsive behavior; and
- be documented by a section-level BATCH-V1.md created when authoring begins.

The target relationship with Design Lab is **validate, then ingest**. Conversion, rewriting,
production component extraction, and review decisions are outside this workspace.

## Default Study Directions

Each section is authored as five studies. Each study explores one authoring direction:

| Variant | Direction |
| --- | --- |
| 001 | Universal / Safe |
| 002 | Premium / Editorial |
| 003 | Structured / Visual Modular |
| 004 | Conversion-led |
| 005 | Art-directed / Distinctive |

These labels are authoring and research directions, not production enums and not visual styles to
be applied. Variants 006–010 may be used only when research demonstrates a genuinely missing
structural territory. The default target remains five studies per section.

The same five-direction model applies to every section role in the catalog, both the sector core
sections S01–S20 and the universal extended site architecture sections S21–S27.

**Study IDs do not change.** The direction names describe how a variant is researched and
composed; they are not part of the ID. `ARC-S06-003` remains `ARC-S06-003` whatever its direction
is called.

### 001 — Universal / Safe

Produce the most broadly reusable and understandable structural solution for the section role.

May use clear hierarchy, familiar web patterns, restrained visual treatment, predictable
interaction, strong accessibility and straightforward responsive behavior.

Safe does not mean generic or low quality. A 001 study should still feel appropriate to its
sector and should still be a design someone would ship.

### 002 — Premium / Editorial

Explore a more elevated, art-directed and editorial treatment.

May use stronger typography, larger media, asymmetry, whitespace, fewer but more intentional
content blocks, cinematic or publication-inspired pacing, and refined visual hierarchy.

Editorial does not mean long-form text by default, magazine imitation for its own sake, or
illegible experimental typography.

### 003 — Structured / Visual Modular

This direction replaces the earlier "Dense / Information-heavy" reading.

Support greater content capacity through **visual organisation**. A 003 study may hold more
information than 001 or 002, but its distinctiveness must come from structure, not from volume of
copy.

Legitimate devices include modular layout, clear grouping, cards or panels where appropriate,
image and text modules, expandable regions, visual hierarchy, progressive disclosure, tabs or
accordions where appropriate, structured media relationships, concise metadata, and useful
comparison structures.

Do not derive a 003 primarily from longer copy, tables covering most of the layout,
spreadsheet-like presentation, technical schedules, dossiers, document registers, specification
sheets or administrative forms.

**Test:** if removing half the copy destroys the reason the study is different, it is probably not
a successful 003. A 003 must be information-*capable*, not text-*dependent*.

### 004 — Conversion-led

Explore a version of the section where the desired next action materially shapes the composition.

The action may be a consultation, enquiry, booking, request, contact, application, comparison,
exploration, or a continuation into a relevant detail page.

Conversion must remain sector-appropriate. Do not automatically turn every 004 into a form, a
lead-generation funnel, a SaaS-style CTA panel, or an ecommerce pattern. The section's content
role stays primary; conversion is integrated into it deliberately.

### 005 — Art-directed / Distinctive

This direction replaces the earlier "Sector-native / Distinctive" reading.

Explore the strongest visually distinctive, memorable or unconventional web composition the
section role can carry while remaining usable, responsive, accessible, recognisably web-native,
and compatible with the section's actual role.

Differentiation may come from unusual but intentional image composition, strong crop
relationships, oversized typography, layering, asymmetry, horizontal sequencing, distinctive
spacing systems, cinematic media, art-directed grid systems, subtle motion, interaction, visual
storytelling, or an unexpected but usable composition.

**Every study 001–005 is already sector-aware.** 005 is not the sector's only sector-native study,
and it must not automatically reach for a professional document metaphor (see *Technical and
professional document metaphors* below). Sector influence may remain, but it must not become a
repeated gimmick across sections.

## Structural Diversity Requirement

The five studies in a section must differ **structurally**. They must not become five colour
schemes, five font themes, five cosmetic variants, or five copies of one grid with the content
swapped. A set that differs only in styling has not covered five directions, whatever its variant
numbers say.

Structural difference must be visible in at least several of:

- information architecture;
- layout topology;
- hierarchy;
- media relationship;
- content capacity;
- interaction;
- responsive strategy;
- conversion behavior.

This requirement is not weakened by the direction changes above. The correction is not "make
everything minimal" — it is "make structural diversity web-native and visually intentional".

## Visual-first Principle

Composition, not copy, carries a study. Prioritise media, composition, typography, spacing,
hierarchy, rhythm, proportion, interaction and responsive transformation. Copy supports the
composition.

**No variant may derive its distinctiveness primarily from having more text.**

There is no single word-count maximum for the whole catalog: a form section, a philosophy section
and a gallery section legitimately need different amounts of copy. The requirement is proportional
judgement — the visible copy in a study should be realistic for the page it represents.

## Text Density

Prefer concise headings, short supporting paragraphs, scannable blocks, progressive disclosure,
meaningful visual breaks, media-supported narrative and limited metadata.

Avoid repeated explanatory paragraphs written only to fill layout, long placeholder prose used as
visual texture, verbose study explanations inside the visible design, and technical content whose
only function is to prove content capacity.

## Visible Website Copy vs Research Notes

A study contains two kinds of writing and they must not be mixed:

| Kind | Belongs in |
| --- | --- |
| Content a visitor would see on the real website | the visible composition |
| Authoring, research, policy and compliance explanation | HTML comments, `<meta>` fields, BATCH-V1.md, section README |

A study must not display large explanatory notes — why the layout exists, how the placeholder
works, what policy it satisfies, why no real claim is being made — unless such text genuinely
belongs to the intended website.

This does not weaken the requirement to identify placeholder and non-evidence content clearly
during authoring. It relocates that identification out of the visitor-facing composition and into
the authoring documentation, where a reviewer can still find it.

## Technical and Professional Document Metaphors

Technical and professional document metaphors are **not forbidden absolutely. They are forbidden
as a default shortcut to sector distinctiveness.**

The pattern includes, among others: drawing sheet, issue sheet, dossier, register, ledger, CV
sheet, schedule, programme, specification, compliance form, spreadsheet, legal document, medical
chart, financial statement, engineering drawing, administrative record — and their notation:
sheet references, scale or NTS marks, revision stamps, issue numbers, clause numbering.

Such a metaphor may be used only when:

1. the user or a supplied reference explicitly asks for that visual concept, **or**
2. the section role genuinely requires that artifact,

**and** in either case

3. the result still works as a modern web interface.

Do not use one merely because it resembles the profession's paperwork. Where a study does use one,
record the justification in its BATCH-V1 record.

## Sector-native Does Not Mean Professional Paperwork

Sector relevance can come from content semantics, imagery relationships, vocabulary, interaction
behavior, real user intent, workflow, visual culture, proportion, materiality, and
industry-specific hierarchy.

Architecture can feel architectural through spatial imagery, project photography, material
studies, proportion, whitespace, refined typography and editorial sequencing. It does not require
drawing title blocks, NTS marks, issue numbers or revision stamps.

The same applies to every other sector. Do not default to healthcare as medical charts, law as
legal documents, finance as spreadsheets and statements, or engineering as blueprints, unless the
section role or an explicit instruction genuinely calls for it.

## Section-shell Rule

**A section study must contain only the section role being authored.**

Do not include a global header, global navigation, a site-wide footer, an announcement bar or a
complete website shell unless the section being authored *is* that global-shell role — a header,
footer or navigation section.

- A hero study is the hero only. No site header or navigation inside it.
- A detail-page study (S21–S27 and comparable page roles) may include the internal content
  architecture needed to demonstrate that page type, but still must not carry a global site header
  or footer unless the task specifically requires it.

## Reference-image Interpretation

Supplied references are structural and visual research input, not pixel targets.

If a reference contains a header, footer, unrelated site navigation, brand chrome or any other
component outside the requested role, do not reproduce those elements merely because they appear
in the screenshot. Extract only the parts relevant to the requested study.

Where a reference is to be followed closely, "closely" applies to the composition of the requested
role — its layout topology, proportion, media relationship and typographic register — not to the
surrounding page chrome.

## Media and Responsive Behavior

Media reservation, empty-slot rules and media density are governed by
`03-MEDIA-POLICY.md`. Responsive behavior as part of the archetype is governed by
`05-RESPONSIVE-QA.md`. Both apply to every direction, including 005.

## Transitional Note

The direction names above are current and authoritative from this revision onward.

Older section READMEs and existing BATCH-V1 documents across the catalog still carry the previous
names, "Dense / Information-heavy" and "Sector-native / Distinctive", in their planned-study
tables. Those files are reconciled in a later phase. Until then **this standard takes precedence**
over the older labels wherever they appear.

Already-authored studies are not retro-fitted by this revision. Their IDs, files and batch records
stay as they are; correction of specific studies is handled as sector work, not as a standards
change.
