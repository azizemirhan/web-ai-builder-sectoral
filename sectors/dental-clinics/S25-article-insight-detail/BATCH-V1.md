# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S25
- Section Name: Oral Health Article / Patient Guide Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 125 studies, S01-S25 authored.
- Article: Make room for your questions.

## Planned Studies

| Study | Direction | Theme | Shape | Media | Words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S25-001 | Universal / Safe | Chalk | B | 1 | 166 | Open article with a reading column and supporting image rail |
| DN-S25-002 | Premium / Editorial | Linen | B | 1 | 165 | Split title/image opening followed by a centred continuous essay |
| DN-S25-003 | Structured / Visual Modular | Slate | B | 2 | Joined media strip above open reading chapters and a closing note |
| DN-S25-004 | Conversion-led | Daylight | C | 0 | 174 | Amber editorial emphasis above a calm single reading column |
| DN-S25-005 | Art-directed / Distinctive | Dusk | B | 2 | Centred dark opening, curved image and offset reading column |

## Research and Editorial Scope

Sources: user direction for five modern designs; section README;
../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; S18 resource batch; preceding S23 and S24
raw/batch records. External research: NONE.

The article is original, non-clinical editorial copy about expressing questions
at an appointment. It does not repeat historical S18 medical statements, prescribe
care, claim clinical benefit, advertise treatment or invent clinical citations.
All five studies present the complete same three-part article, not excerpts.

Author and publication date are explicit placeholders marked data-placeholder.
No named author, publication, review credential or publication date is fabricated.
The authoring date above is a repository record, not an article publication date.
The blockquote is original editorial emphasis, not patient testimony or an external
quotation. The page remains labelled Editorial draft.

004 interprets its conversion-led direction as helping the reader prepare a question
and choose further reading. No appointment CTA, sales form or marketing interruption
has been inserted into the article.

## Structure, Reading Comfort and Responsive Behaviour

- One semantic article per file with one H1, a standfirst, attribution, three named
  sections with H2 headings, and named related-reading navigation.
- Body text is 16px with 1.75 line height and a maximum measure of 62ch.
- 001 uses a supporting image rail on desktop; at 680px it moves above the prose
  with a compact adjacent editorial note. The article chapters retain their order.
- 002 centres the main essay in a 650px column. The opening image sits beside the
  title on desktop and follows it on phones. An editorial quote separates chapters.
- 003 demonstrates modular hierarchy through a joined image band and open columns,
  not text-only cards. Below 560px the article sections read in a single sequence.
- 004 is shape C because its short, conversation-focused article does not need a
  photograph. An amber colour field highlights the article's central sentence.
  The reading column and its short margin note stack below 680px.
- 005 uses a wide curved lead image, offset pull quote and prose, then a small
  context image beside further reading. All become normal vertical flow on phones.
- No sticky rails, progress widgets, contents menus or hidden paragraphs are needed
  for this short article. All content and native links work without JavaScript.

Document metaphor: NONE. Hierarchy comes from type, proportion, colour and space.
S23 shapes: B / B / B / C / B. S24: B / B / A / B / B.
S25: B / B / B / C / B. Manual comparison distinguishes the article from service
details and media-rich case narratives. The existing CONS-specific composition
checker is not used to claim dental validation.

## Media Register

Six reserved areas total. No bitmap assets or remote dependencies are introduced.

| Subject | Studies | Purpose | Expected type | Fallback |
| --- | --- | --- | --- | --- |
| Dentist in conversation | 001, 003, 005 | Support the conversation theme | Actual clinician mid-conversation, no identifiable patient | Labelled empty figure preserves its space |
| Consultation room | 002, 003, 005 | Establish the setting of a conversation | Actual clinic consultation space, no anonymous surgery glamour shot | Labelled colour area remains readable |

Visible captions name each subject; accessible labels identify the reserved photograph.
No mouth photos, tooth icons, stock smiles or generated portraits. Portraits remain
reserved. Real assets need provenance, permission, accurate captions and alt text at
integration. The article remains complete with every image slot empty.

## Routes and Integration

Each study has two same-variant related-reading links:
S23-service-offering-detail (A first dental consultation) and
S18-oral-health-resources (Browse patient resources).
All ten local targets exist. These are authoring review routes, not deployed URLs.
They do not submit data or claim that an appointment was requested.

There is no global header or footer. An assembled page must retain a single article
heading if S21 is used for its introduction. Populate verified attribution and
publication context before publishing the editorial draft.

## QA Record

- Headless Chrome: 20 viewport checks at 1440, 768, 390 and 320px.
- No document overflow or out-of-viewport elements at those widths.
- Stable study metadata, unique IDs, one H1 and labelled article checked.
- Native links focus successfully and meet the 44px target-height check.
- All ten destinations verified on disk.
- All five desktop and 390px screenshots visually reviewed.
- Words: 166 / 165 / 168 / 174 / 168.
- Gallery checks passed: five frames, variant filter, mobile width switch, pressed
  state, restore-all and full-size links.
- No raw JavaScript, frameworks, remote fonts or external stylesheets.
- Reduced-motion CSS included. git diff --check has no whitespace errors.
- Cross-browser and screen-reader testing were not run. No Design Lab ingestion,
  clinical review or publication approval is claimed.

## Review

[Five-study gallery](../../../review/dental-article-detail.html)

Regenerate from the repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-article-detail.ps1

Measured heights: ../../../review/dental-article-detail-heights.json.
Raw HTML is the source of truth.

