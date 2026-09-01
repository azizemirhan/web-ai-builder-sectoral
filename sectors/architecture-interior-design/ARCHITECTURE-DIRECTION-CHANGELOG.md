# Architecture & Interior Design — Direction Changelog

A short record of how this sector's authoring direction changed. It is not a standard and not a
design guide: the direction lives in `./ARCHITECTURE-DESIGN-DIRECTION.md` and the evidence lives in
`./ARCHITECTURE-REWORK-MANIFEST.md`.

## Phase 0 — Audit Baseline (`9db527e`)

146 authored `ARC` studies were read and measured. The finding: the catalog is structurally
diverse but not visually diverse. 34 studies use a heavy technical-document metaphor, 49 are HIGH
or EXCESSIVE in text density, 15 carry a global site header, and 42 carry no media at all. Of the
25 studies the user named individually, 22 sit in the `003` and `005` slots — `003` had been read
as *more fields and more prose*, `005` as *make it look like a professional document*.

Recorded in `./ARCHITECTURE-REWORK-MANIFEST.md`. No design work.

## Phase 1 — Global Authoring Standard Correction (`17dfb9e`)

Because both misreadings were defensible against the old wording, the correction was made in the
global standard rather than study by study:

- `003` redefined as **Structured / Visual Modular**, `005` as **Art-directed / Distinctive**.
- Added the visual-first principle, text-density guidance, the separation of visible website copy
  from research notes, the technical/professional document-metaphor constraint, the section-shell
  rule and reference-image interpretation.
- Strengthened the media policy on reserved areas, fabrication and media density, and made
  responsive behavior part of the archetype.

Study IDs were not changed. Authored studies were not retro-fitted.

## Phase 2 — Architecture Sector Reconciliation (this change)

Translates the global correction into an Architecture design language and reconciles the sector's
section contracts.

**Created**

- `./ARCHITECTURE-DESIGN-DIRECTION.md` — the sector's visual language, anti-patterns, copy
  direction, media direction, Architecture section-shell rule, the Architecture reading of the five
  directions, and the section authoring questions.
- `./ARCHITECTURE-DIRECTION-CHANGELOG.md` — this file.

**Updated**

- `./SECTOR-BRIEF.md` — now states the visual-first direction and links the direction document.
- `./README.md` — direction and changelog pointers; S28 wording aligned with the provisional
  status.
- All 27 section READMEs, S01–S27.

**Direction labels reconciled**

Every S01–S27 README now uses 001 Universal / Safe · 002 Premium / Editorial · 003 Structured /
Visual Modular · 004 Conversion-led · 005 Art-directed / Distinctive, each with a section-specific
reading of what `003` and `005` mean for that role. S01–S20 previously had no direction table at
all — they were identity stubs — and now carry a full section contract. Study IDs are unchanged.

**Sections with clarified responsibilities**

| Section | Clarification |
| --- | --- |
| S01 Hero | Hero only: no global header, navigation, footer or drawing title block. |
| S03 Services | States what is offered; must not collapse into S06 Design Process. |
| S04 Project Typologies | Building typologies stay semantically separate from audience personas. |
| S05 Design Philosophy | How the studio thinks; not who it is, and not an essay or clause set. |
| S06 Design Process | Visual phase progression; programme and schedule aesthetics are not the default. |
| S07 Studio About | Who the practice is; not a second manifesto, not a colophon. |
| S08 Architects & Designers | Portrait-led roster; CV-sheet and register aesthetics retired. |
| S09 Awards & Publications | Covers, tear sheets and imagery instead of a bibliography. |
| S10 Capabilities | Visual capability groups instead of a consultant matrix. |
| S11 Materials & Sustainability | Visual materiality: samples and textures, not material schedules. |
| S12 Client Testimonials | Editorial quotation composition; no fabricated testimonials. |
| S13 Featured Project Case Study | A section, not the S24 page; no dossier framing. |
| S14 Project Gallery | Conventional grid capped at 3 × 3 = 9 visible media slots, a maximum not a requirement. |
| S15 Sectors & Markets | Image-led markets; maps and matrices are not a styling device. |
| S16 Press & News | Editorial cards instead of a press register. |
| S17 Studio Locations | Location cards and studio imagery instead of a coordinate atlas. |
| S18 Studio Stats | Large figures and short labels; no spreadsheets; real numbers only. |
| S19 Project Inquiry | Modern form composition; not a working sheet. |
| S20 Consultation CTA | Concise invitation; not an agenda document. |
| S21 Subpage Hero | A conventional website internal-page hero, not a dossier cover or metadata register. |
| S22 Breadcrumb | A conventional breadcrumb; not sibling navigation, a pager, contents or a key plan. |
| S23 Service Detail | A full visual service detail page with a stated baseline content capacity. |
| S24 Project Detail | A portfolio-style project page; no dossiers or drawing issue sets. |
| S25 Article Detail | A contemporary editorial page; no global chrome, no uncontrolled text density. |
| S26 Profile | Portrait-led; not a curriculum sheet or capability matrix. |
| S27 Location Detail | Place-led; not arrival diagrams or coordinate sheets. |

**Sections intentionally unchanged in substance**

- **S02 Selected Projects** — the user accepted the current design direction. Its README gained the
  reconciled direction labels and the standard boundary notes only; no new requirement was
  introduced that the authored set does not already meet.

**Excluded**

- `S28-blog-list-pages/` — untouched. It remains provisional, outside the planned catalog count,
  and outside the sector design direction until its taxonomy is decided.

**Not done in this phase**

No HTML was modified, no `BATCH-V1.md` was updated, no responsive implementation was fixed and no
review output was regenerated. Batch documents still carry the previous direction labels in their
own planned-study tables; reconciling them is later work.
