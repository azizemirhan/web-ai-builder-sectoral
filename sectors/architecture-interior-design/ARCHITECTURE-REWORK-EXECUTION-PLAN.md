# Architecture & Interior Design — Rework Execution Plan

## Status

Phase 3 — Final Planning. Classification and execution planning only. No study, batch record,
standard, section README or review artifact was modified in this phase.

## Inputs

| Input | Reference |
| --- | --- |
| Phase 0 — audit baseline | `9db527e` · `./ARCHITECTURE-REWORK-MANIFEST.md` |
| Phase 1 — global authoring standard correction | `17dfb9e` · `../../standards/01-AUTHORING-STANDARD.md` |
| Phase 2 — Architecture direction and section contracts | `db1aff7` · `./ARCHITECTURE-DESIGN-DIRECTION.md`, all S01–S27 READMEs |
| Review pipeline repair | `062a5ec` · `../../review/index.html`, `../../review/architecture-contact-sheet.pdf` |
| Accepted pilot | `cab18d5`, `49c7498`, `10f456b` · `ARC-S06-003` |

Visual review source for this phase: the regenerated contact sheet — 146 studies, one A3 landscape
page each, desktop / tablet / phone side by side, 146/146 real measured heights, no clipping. It
was not regenerated during Phase 3.

**Source-of-truth order** used wherever inputs conflicted: explicit current user decisions →
current global authoring standard → Architecture Design Direction → current section README →
existing batch structural intent → existing implementation → historical direction terminology.
Historical raw intent did not override a corrected rule anywhere in this plan.

## Current Design Principles

Applied to every classification below:

1. **Architecture presentation is primarily visual.** Distinctiveness comes from photography, media
   hierarchy, space, proportion, typography, materiality, editorial rhythm and interaction.
2. **Technical and professional document metaphors are not the sector's default styling device.**
   The test applied per study was whether the metaphor is *driving* the design, not whether a word
   like `SHEET` or `PLATE` appears.
3. **No universal word limit.** Density was judged against the role: does the content need this
   text, or was it added to make the study feel different?
4. **Reserved media areas are intended output.** `IMAGE AREA`, `VIDEO AREA`, `PORTRAIT AREA`,
   `SAMPLE AREA`, `MAP AREA`, `PLATE AREA`, `PROJECT MEDIA` and equivalents were judged on size,
   position, hierarchy and intended relationship — never on being empty. **No study in this plan is
   downgraded for an empty slot**, and no correction proposes inventing media, projects, people,
   awards or addresses.
5. **A section study contains its own role only** — no global header, primary navigation, footer or
   announcement bar unless that component is the role being authored.
6. **Responsive behaviour is part of the archetype**, authored rather than inherited.

## Classification Definitions

| Status | Meaning |
| --- | --- |
| `KEEP` | Current design satisfies the corrected section contract. |
| `MINOR_FIX` | Core visual and structural design remains valid; only limited changes — header removal, light copy reduction, small spacing or semantic correction, minor breakpoint fix. |
| `REWORK` | The topology has useful value and should survive, but visual expression or content balance needs significant revision. |
| `REBUILD` | The current interpretation is fundamentally wrong for the section role. |
| `BUG_FIX` | The design concept is accepted; the implementation is broken. |
| `DEFER` | Outside the current catalog (S28 only). |

**Decision source**

| Source | Meaning |
| --- | --- |
| `USER_REQUIRED` | Named or covered by an explicit user instruction. Mandatory minimum scope. |
| `AUDIT_ADDED` | This audit's recommendation under the corrected rules. The user decides whether it runs. |
| `KEEP_CONFIRMED` | Explicitly confirmed as no-change by the user. |
| `IMPLEMENTED_PILOT` | Already reworked and accepted. |
| `IMPLEMENTATION` | Change driven by an implementation defect rather than by direction. |

## Executive Summary

141 authored studies across S01–S27 (135 planned + 6 extension variants). S28's five studies are
deferred and excluded from every total.

| Status | Count |
| --- | --- |
| KEEP | 72 |
| MINOR_FIX | 14 |
| REWORK | 27 |
| REBUILD | 28 |
| BUG_FIX | 0 |
| **Total** | **141** |

69 studies carry work. 48 of those are user-required; 21 are audit-added. `ARC-S06-003` is already
implemented and accepted and is counted under KEEP.

What the work actually consists of:

- **49 technical-document corrections** — 33 where a heavy metaphor drives the whole composition
  (sheet, register, ledger, dossier, annex, atlas, programme, curriculum, issue set, key plan,
  measurement drawing) and 16 where a moderate register (field lists, metadata indexes, citation
  blocks, colophons, directory tables) is the element being removed. This is the single largest
  cause of rework in the sector, and it is concentrated almost entirely in the `005` slot.
- **37 text-density corrections**, concentrated in S23–S27, which average 414 visible words against
  137 for the sector core.
- **10 header/shell corrections** — all five S01 studies and all five S25 studies.
- **Seven sections that currently carry no media at all in one or more studies** (S09, S10, S15,
  S17, S18, S21, and S23-003/004) need media slots *introduced* during correction, not merely
  rearranged. A section with no slot cannot become image-led by editing.
- **One confirmed responsive failure** (`ARC-S08-007`) and seven studies queued for verification.

The corrected `005` reading is the largest single behavioural change: 20 of the 28 REBUILDs are
`005` or `003` studies whose sector-native answer was professional paperwork.

## User-Required Corrections

48 studies, mandatory minimum scope.

| Section | Studies | Basis |
| --- | --- | --- |
| S01 | 001, 002, 003, 004, 005 | Global rule: hero only; remove header/navigation. 005 additionally carries a drawing-sheet metaphor. |
| S06 | 005 | Named: too technical, too text-heavy. |
| S08 | 003, 007 | Named: 003 too technical/text-heavy; 007 broken at every width. |
| S09 | 001, 003, 005 | Named: too technical / too text-heavy. |
| S10 | 005 | Named. |
| S11 | 003, 005 | Named. |
| S12 | 005 | Named. |
| S13 | 003 | Named. |
| S14 | 003 | Named; gallery to 3 × 3 = 9. |
| S15 | 003, 005 | Named. |
| S16 | 003 | Named. |
| S17 | 003, 005 | Named. |
| S18 | 002, 003, 005 | Named. |
| S19 | 005 | Named: working-sheet style not wanted. |
| S20 | 005 | Named: agenda-document style not wanted. |
| S21 | 001, 002, 003, 004, 005 | Role clarification: conventional internal-page hero. |
| S22 | 002, 003, 004, 005 | Role clarification: conventional breadcrumb only. 001 is the reference and needs no change. |
| S23 | 001, 002, 003, 004, 005 | Role clarification: visual service detail page; whole-section content balance. |
| S24 | 003, 005 | Named: too technical, too document-oriented. |
| S25 | 001, 002, 003, 004, 005 | Phase 3 §16: global header/navigation must be removed. |

`ARC-S06-003` is user-required and **already delivered** — see *Implemented Pilot*.

## Audit-Added Corrections

21 studies. Recommendations under the corrected rules; the user decides whether they run. Phase 0
recommendations were re-evaluated rather than carried forward automatically — `ARC-S14-001`
(eight frames) and `ARC-S24-002` (folio label) were dropped back to KEEP because the metaphor does
not drive the design and the count is within the 3 × 3 maximum.

| Study | Status | Why, under current rules |
| --- | --- | --- |
| `ARC-S03-003` | REWORK | Specification-style field list closes every card. |
| `ARC-S03-005` | REBUILD | Sheet block and stamped register drive the composition. |
| `ARC-S04-003` | REWORK | Scope field pairs read as a specification list. |
| `ARC-S04-005` | REWORK | Plate-index and catalogue framing; highest density in S04. |
| `ARC-S05-003` | REWORK | Text-first: six prose rows against one media area. |
| `ARC-S05-005` | REBUILD | Contract document — clause numbering, revision and status stamps. |
| `ARC-S07-005` | REWORK | Colophon framing is a print-document metaphor. |
| `ARC-S08-005` | REBUILD | Register metaphor reduces portraits to labelled cells. |
| `ARC-S08-009` | MINOR_FIX | 241 words in a roster section; rail behaviour to verify. |
| `ARC-S10-003` | REWORK | Twenty-four inventory lines with mode stamps; no media. |
| `ARC-S13-005` | REWORK | Sheet framing and a change schedule around a strong comparison. |
| `ARC-S14-005` | REWORK | Sheet framing, axis labels and NTS notation around a good ordering idea. |
| `ARC-S24-001` | MINOR_FIX | Closing project-facts ledger block is documentary. |
| `ARC-S26-001` | MINOR_FIX | 373 words against a single portrait. |
| `ARC-S26-003` | REWORK | Personnel record with a table — the family rejected in S08-003. |
| `ARC-S26-004` | MINOR_FIX | 450 words against a single portrait. |
| `ARC-S26-005` | REBUILD | Bid CV sheet with a coverage matrix and issue apparatus. |
| `ARC-S27-001` | MINOR_FIX | 351 words against one photographic area. |
| `ARC-S27-003` | REWORK | Three tables, 448 words, no photography. |
| `ARC-S27-004` | MINOR_FIX | 466 words and no photographic media. |
| `ARC-S27-005` | REWORK | Keyed-plan register — the device excluded from S22. |

## Implemented Pilot

`ARC-S06-003` — **KEEP / IMPLEMENTED_PILOT**, status `REWORKED — ACCEPTED`. Five-stage semantic
progression, one lead media field, five phase media fields, concise copy, no dossier styling,
responsive QA passed at 1440 / 1280 / 1024 / 768 / 430 / 390 / 320, batch record updated. It is a
**quality and direction reference, not a layout template**: future `003` studies must reach the same
standard through their own section role, and no plan entry below proposes copying its grid.

## Section-Level Execution Summary

| Section | Studies | KEEP | MINOR_FIX | REWORK | REBUILD | Batch | Diversity |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| S01 Hero | 5 | 0 | 3 | 2 | 0 | 1 | RISK |
| S02 Selected Projects | 5 | 5 | 0 | 0 | 0 | — | PASS |
| S03 Services | 7 | 5 | 0 | 1 | 1 | 3 | PASS |
| S04 Project Typologies | 5 | 3 | 0 | 2 | 0 | 3 | PASS |
| S05 Design Philosophy | 5 | 3 | 0 | 1 | 1 | 3 | RISK |
| S06 Design Process | 5 | 4 | 0 | 0 | 1 | 3 | RISK |
| S07 Studio About | 5 | 4 | 0 | 1 | 0 | 4 | RISK |
| S08 Architects & Designers | 9 | 5 | 1 | 1 | 2 | 4 | RISK |
| S09 Awards & Publications | 5 | 2 | 0 | 1 | 2 | 4 | RISK |
| S10 Capabilities | 5 | 3 | 0 | 1 | 1 | 3 | RISK |
| S11 Materials & Sustainability | 5 | 3 | 0 | 0 | 2 | 3 | RISK |
| S12 Client Testimonials | 5 | 4 | 0 | 0 | 1 | 4 | RISK |
| S13 Featured Project Case Study | 5 | 3 | 0 | 2 | 0 | 5 | PASS |
| S14 Project Gallery | 5 | 3 | 0 | 2 | 0 | 5 | RISK |
| S15 Sectors & Markets | 5 | 3 | 0 | 0 | 2 | 3 | RISK |
| S16 Press & News | 5 | 4 | 0 | 1 | 0 | 4 | PASS |
| S17 Studio Locations | 5 | 3 | 0 | 1 | 1 | 4 | RISK |
| S18 Studio Stats | 5 | 2 | 0 | 1 | 2 | 4 | RISK |
| S19 Project Inquiry | 5 | 4 | 0 | 0 | 1 | 5 | RISK |
| S20 Consultation CTA | 5 | 4 | 0 | 0 | 1 | 5 | RISK |
| S21 Subpage Hero | 5 | 0 | 0 | 3 | 2 | 1 | RISK |
| S22 Breadcrumb | 5 | 1 | 1 | 0 | 3 | 1 | RISK |
| S23 Service Detail | 5 | 0 | 0 | 3 | 2 | 2 | RISK |
| S24 Project Detail | 5 | 2 | 1 | 0 | 2 | 2 | RISK |
| S25 Article Detail | 5 | 0 | 4 | 1 | 0 | 2 | PASS |
| S26 Profile | 5 | 1 | 2 | 1 | 1 | 2 | RISK |
| S27 Location Detail | 5 | 1 | 2 | 2 | 0 | 2 | RISK |
| **Total** | **141** | **72** | **14** | **27** | **28** | | |

## Study-by-Study Execution Records

Each record reads: **ID · direction · final status · decision source**. `Batch` records whether the
section's `BATCH-V1.md` must be updated after the HTML work.

### S01 — Hero

Section rule for all five: **hero only**. No global header, primary navigation, site shell or
footer. Composition otherwise good → MINOR_FIX; document styling also driving the design → REWORK.

#### ARC-S01-001 · 001 Universal / Safe · MINOR_FIX · USER_REQUIRED

- **Concept:** Split hero — wordmark bar and primary nav above a left type column and a right image field.
- **Preserve:** left-type / right-image split; the type ramp; the image-field proportion; the whitespace.
- **Remove:** global site header; primary navigation.
- **Replace with:** nothing — the split composition stands on its own once the chrome is gone.
- **Media:** one image field, unchanged, holding the right half of the split as the primary visual element.
- **Copy:** LOW — 42 visible words, correct for the role; no reduction needed.
- **Responsive:** unchanged two-column to single-column reflow; re-verify the top spacing once the header band is removed so the title does not sit against the viewport edge.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S01-002 · 002 Premium / Editorial · MINOR_FIX · USER_REQUIRED

- **Concept:** Full-bleed image ground with an overlaid display headline and a three-stage strip beneath.
- **Preserve:** the full-bleed media relationship; the display type treatment; the stage strip rhythm.
- **Remove:** global header and navigation.
- **Replace with:** —
- **Media:** one full-bleed field, unchanged; it is the composition and must keep its full-viewport scale.
- **Copy:** LOW — 74 words; no change.
- **Responsive:** full-bleed field holds at every width; verify the overlay contrast band still reads once the header no longer occupies the top of the frame.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Closest existing S01 study to the corrected direction; use as the S01 reference after the header is removed.

#### ARC-S01-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Oversized uppercase display headline over a dense index of typologies, scope and project records.
- **Preserve:** the display headline scale; the asymmetric composition; the idea that this hero carries more than one line of information.
- **Remove:** global header and navigation; the metadata index read as a technical register (typology / scope / record columns).
- **Replace with:** a modular visual supporting block — two or three small project media modules, or a short editorial line plus one image module — so the extra capacity is carried by structure and media rather than by fields.
- **Media:** currently one image area; raise to two or three small modules so the modular reading is visual. The lead image keeps its scale.
- **Copy:** LOW — 77 words today; hold at or below that after the index becomes modules.
- **Responsive:** modules reflow 3 → 2 → 1 beneath the headline; the headline must remain the first thing read at every width.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Escalated from the Phase 0 MINOR_FIX. Under the corrected `003` reading a metadata index is exactly the failure pattern, and replacing it is more than a limited change.

#### ARC-S01-004 · 004 Conversion-led · MINOR_FIX · USER_REQUIRED

- **Concept:** Conversion hero — full-bleed field, right-aligned title block and a circular primary action.
- **Preserve:** the circular action device; the right-aligned title block; the calm full-bleed field.
- **Remove:** global header and navigation.
- **Replace with:** —
- **Media:** one full-bleed field, unchanged.
- **Copy:** LOW — 54 words; no change.
- **Responsive:** unchanged; verify the circular action keeps a 44px target and does not collide with the title block at 390 and 320 once the header band is gone.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S01-005 · 005 Art-directed / Distinctive · REWORK · USER_REQUIRED

- **Concept:** Drawing-sheet hero — title block with SHEET / SET / SCALE / REVISION / STATUS fields ruled under the headline.
- **Preserve:** the ruled horizontal discipline as a purely graphic device; the wide plate area and its proportion.
- **Remove:** the title-block register and every drawing field (SHEET, SET, SCALE, REVISION, STATUS); the global header.
- **Replace with:** an art-directed hero built from the plate and the type — an oversized headline crossing the plate edge, or an off-axis title against a wide image field. The horizontal rules may stay only as a compositional line, carrying no labels.
- **Media:** the wide plate becomes the dominant element rather than a field inside a sheet; enlarge it to at least half the hero height.
- **Copy:** LOW — 61 words; unchanged in volume, but the field labels stop being copy.
- **Responsive:** wide plate re-proportions rather than shrinking; the headline must not clip at 320 once it is scaled up.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** REWORK rather than REBUILD: the ruled horizontal structure and the plate relationship are worth keeping; only the documentary apparatus goes.

### S02 — Selected Projects

**User decision: no design change.** All five remain KEEP. Not reopened on aesthetic grounds, and
no new requirement is introduced that the authored set does not already meet. No implementation
defect was found in the contact-sheet review.

#### ARC-S02-001 · 001 Universal / Safe · KEEP · KEEP_CONFIRMED

- **Concept:** Editorial project grid — serif display title beside four project cards at mixed sizes.
- **Preserve:** the mixed-size card rhythm; the serif display heading; the asymmetry.
- **Remove / Replace with:** — · —
- **Media:** four project areas; unchanged.
- **Copy:** LOW — 54 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S02-002 · 002 Premium / Editorial · KEEP · KEEP_CONFIRMED

- **Concept:** Two-up residential pairing with a large uppercase title and a right-aligned standfirst.
- **Preserve:** the two-up spread; the uppercase display title.
- **Remove / Replace with:** — · —
- **Media:** two project areas; unchanged.
- **Copy:** LOW — 80 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S02-003 · 003 Structured / Visual Modular · KEEP · KEEP_CONFIRMED

- **Concept:** Numbered three-column project sequence with short architectural context lines.
- **Preserve:** the numbered sequence; equal card weighting.
- **Remove / Replace with:** — · —
- **Media:** three project areas; unchanged.
- **Copy:** LOW — 97 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Already satisfies the corrected `003` reading — capacity carried by a module grid, not by fields.

#### ARC-S02-004 · 004 Conversion-led · KEEP · KEEP_CONFIRMED

- **Concept:** Collage of unequal project frames with a vertical WORKS wordmark and one conversion route.
- **Preserve:** the unequal collage; the vertical display word; the single route.
- **Remove / Replace with:** — · —
- **Media:** six project areas; unchanged.
- **Copy:** LOW — 43 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S02-005 · 005 Art-directed / Distinctive · KEEP · KEEP_CONFIRMED

- **Concept:** Centred title over a six-card gallery grid with category filter words.
- **Preserve:** the six-card grid; the filter row.
- **Remove / Replace with:** — · —
- **Media:** six project areas; unchanged.
- **Copy:** LOW — 67 words.
- **Responsive:** unchanged.
- **Batch:** NONE

### S03 — Services

Section rule: Services state **what the studio offers** and must not collapse into Design Process.

#### ARC-S03-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Four service cards, each with its own image area, title and short description.
- **Preserve:** the image-per-service card model.
- **Remove / Replace with:** — · —
- **Media:** four image areas, one per service; unchanged.
- **Copy:** MEDIUM — 128 words across four services; proportionate.
- **Responsive:** unchanged 4 → 2 → 1 card reflow.
- **Batch:** NONE

#### ARC-S03-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial services page — serif display heading, four labelled image cards, principles list.
- **Preserve:** the serif display heading; the four-card media row.
- **Remove / Replace with:** — · —
- **Media:** five image areas; unchanged.
- **Copy:** LOW — 92 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference for the corrected direction.

#### ARC-S03-003 · 003 Structured / Visual Modular · REWORK · AUDIT_ADDED

- **Concept:** Three services described with image, paragraph and a Stages / Output / Typologies field list.
- **Preserve:** the three-column media-and-narrative structure; the image-per-service relationship; the service set itself.
- **Remove:** the specification-style field list closing each card (Stages / Output / Typologies).
- **Replace with:** one short editorial line per service in place of the field triple, and a second media module per column so the extra capacity is visual — a wide image plus a detail image, or an image plus a caption strip.
- **Media:** raise from three to six areas — a primary and a supporting field per service.
- **Copy:** MEDIUM → LOW; from 136 words to roughly 90 once the field lists become single lines.
- **Responsive:** three columns → two → one; media pairs stack rather than shrink.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S03-004 · 004 Conversion-led · KEEP · —

- **Concept:** Horizontal service catalogue with a scroll rail and paired prev/next controls.
- **Preserve:** the scroll rail and its keyboard controls; the six-image media rail.
- **Remove / Replace with:** — · —
- **Media:** six image areas on the rail; unchanged.
- **Copy:** HIGH — 216 words, at the top of the acceptable band for six services with a rail. Optional trim only; not required.
- **Responsive:** rail behaviour at 430 / 390 / 320 is in the verification queue (affordance and keyboard route).
- **Batch:** NONE

#### ARC-S03-005 · 005 Art-directed / Distinctive · REBUILD · AUDIT_ADDED

- **Concept:** Services expressed as work stages under a drawing-sheet block (SHEET / SET / ENGAGEMENT / STATUS) with a stamped footer register.
- **Preserve:** the four-stage progression as content; the four stage image areas.
- **Remove:** the sheet block and every sheet field; the stamped footer register; the ruled document frame.
- **Replace with:** **replacement structural territory — an art-directed service sequence**: four stages as large alternating image-and-type bands, each stage a full-width media field with a short title set against it, the sequence carried by scale change rather than by a frame.
- **Media:** four stage areas retained but enlarged from cells inside a sheet to full-width bands; media becomes the primary element.
- **Copy:** MEDIUM — 110 words; hold, but redistribute as one line per stage plus a lead statement.
- **Responsive:** alternating bands become a single stacked sequence at 768 and below; media keeps a fixed aspect rather than collapsing.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with S06's process sequence — this is *what is offered at each stage*, and S06 is *how a project runs*. Keep the S03 version service-named and media-dominant.

#### ARC-S03-006 · extension variant · KEEP · —

- **Concept:** Paired media-and-card rows — a serif heading column beside three image/text service rows.
- **Preserve:** the paired row rhythm.
- **Remove / Replace with:** — · —
- **Media:** three image areas; unchanged.
- **Copy:** MEDIUM — 110 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S03-007 · extension variant · KEEP · —

- **Concept:** Corner-media bento — four service cards around two image blocks.
- **Preserve:** the bento arrangement.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** MEDIUM — 124 words.
- **Responsive:** unchanged.
- **Batch:** NONE

### S04 — Project Typologies

Section rule: building typologies stay semantically separate from audience personas; `005` must not
default to an atlas or taxonomy document.

#### ARC-S04-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Four typologies as large right-aligned uppercase names against a single tall media panel.
- **Preserve:** the right-aligned typographic listing; the tall panel proportion.
- **Remove / Replace with:** — · —
- **Media:** one tall typology panel; unchanged.
- **Copy:** LOW — 64 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference for typographic restraint.

#### ARC-S04-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial typology set — mixed serif/sans question headline, four labelled columns, image row.
- **Preserve:** the mixed serif/sans headline device; the per-typology image row.
- **Remove / Replace with:** — · —
- **Media:** four image areas; unchanged.
- **Copy:** MEDIUM — 120 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S04-003 · 003 Structured / Visual Modular · REWORK · AUDIT_ADDED

- **Concept:** Typologies as a four-field record with scope values, beside two tall image areas.
- **Preserve:** the two tall image areas and their proportion; the compact layout; the four-typology content.
- **Remove:** the scope field pairs read as a specification list.
- **Replace with:** each typology as a small visual module — a short editorial line under a typology name, grouped in a two-by-two beside the plates — so the structure is modular rather than tabulated.
- **Media:** two tall areas retained; add one small area per typology module if the two-by-two needs anchoring, taking the section to four.
- **Copy:** LOW — 76 words; hold.
- **Responsive:** plates and modules swap from side-by-side to stacked at 768; modules go two-up then one-up.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S04-004 · 004 Conversion-led · KEEP · —

- **Concept:** Three typology series as bordered image panels with a routing question and two actions.
- **Preserve:** the series grouping; the routing question; one image per series.
- **Remove / Replace with:** — · —
- **Media:** three series image areas; unchanged.
- **Copy:** MEDIUM — 119 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S04-005 · 005 Art-directed / Distinctive · REWORK · AUDIT_ADDED

- **Concept:** Typology catalogue with plate references (PLATE AREA · R-01), tabbed switching and prev/next controls.
- **Preserve:** the tabbed typology switching — the only interaction model of its kind in S04; the index rail as a navigation device.
- **Remove:** the plate reference numbering and catalogue framing; the descriptive paragraphs that make this the densest S04 study.
- **Replace with:** each tab revealing a large project image with a short typology statement; the index rail restyled as plain typographic navigation rather than a plate index.
- **Media:** two plate areas → three or four project areas, one per typology, each filling the panel rather than sitting inside a catalogue frame.
- **Copy:** HIGH → LOW; from 331 words to roughly 100, one short statement per typology.
- **Responsive:** tabs become a stacked accordion or a scrollable tab row with a visible affordance at 480 and below; every typology must remain reachable without script.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S05 — Design Philosophy

Section rule: how the studio **thinks**, not who it is; no long theoretical essays and no clause or
register sheets.

#### ARC-S05-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Philosophy stated as two headline statements with supporting paragraphs and two image areas.
- **Preserve:** the two-statement structure; media punctuating the text.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** MEDIUM — 136 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S05-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Oversized lowercase 'philosophy' wordmark over a centred manifesto paragraph.
- **Preserve:** the wordmark device; the centred manifesto.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** MEDIUM — 104 words.
- **Responsive:** unchanged; wordmark scales without clipping.
- **Batch:** NONE
- **Notes:** Positive reference for typographic distinctiveness.

#### ARC-S05-003 · 003 Structured / Visual Modular · REWORK · AUDIT_ADDED

- **Concept:** Six numbered positions as icon-led rows with a single supporting image area.
- **Preserve:** the icon-led row rhythm; the numbering; the scannable hierarchy.
- **Remove:** two of the six positions; the paragraph-length body under each remaining position.
- **Replace with:** four positions as visual modules, each pairing its icon and one short line with its own media area, so the section reads as a grid of positions rather than a column of prose.
- **Media:** one area → four, one per remaining position.
- **Copy:** MEDIUM → LOW; from 186 words to roughly 90.
- **Responsive:** four modules 2 × 2 at desktop → 2 × 2 at tablet → single column at 480, media keeping its aspect.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S05-004 · 004 Conversion-led · KEEP · —

- **Concept:** Conversion-led philosophy — short statement, pull quote and two actions beside a tall plate.
- **Preserve:** the pull-quote device; the tall plate.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** LOW — 84 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S05-005 · 005 Art-directed / Distinctive · REBUILD · AUDIT_ADDED

- **Concept:** Design principles set as numbered contract clauses with Clause / Applies to / Revision / Status fields.
- **Preserve:** the wide band media and its scale; the four-principle content model.
- **Remove:** clause numbering; the Applies-to / Revision / Status apparatus; the ruled document frame.
- **Replace with:** **replacement structural territory — an art-directed principles page**: one wide band image at the top, then four principles set as oversized type at different scales across a generous field, each with a single supporting line, no rules and no numbering apparatus.
- **Media:** one wide band retained and enlarged; add one further image field between the principles so media punctuates the type.
- **Copy:** MEDIUM → LOW; from 198 words to roughly 100.
- **Responsive:** the type field reflows to a single column with the scale relationships preserved proportionally; the band image re-proportions rather than cropping to a sliver.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with `ARC-S05-002`, which is already a large-type composition. Differentiate by using four principles at mixed scale plus media, against 002's single wordmark and centred paragraph.

### S06 — Design Process

Section rule: visual phase progression; programme, schedule and drawing-document aesthetics are not
the default.

#### ARC-S06-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Four stages as columns, each closing on a named deliverable, above a wide process image.
- **Preserve:** the 'ends with' deliverable device; the wide media band.
- **Remove / Replace with:** — · —
- **Media:** one wide band area; unchanged.
- **Copy:** MEDIUM — 152 words.
- **Responsive:** unchanged 4 → 2 → 1 column reflow.
- **Batch:** NONE

#### ARC-S06-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial stage sequence — large numerals, serif headings and one image area per stage.
- **Preserve:** the numeral-led stage rhythm; per-stage media.
- **Remove / Replace with:** — · —
- **Media:** four stage areas; unchanged.
- **Copy:** MEDIUM — 163 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference alongside the implemented `003`.

#### ARC-S06-003 · 003 Structured / Visual Modular · KEEP · IMPLEMENTED_PILOT

- **Concept:** One large lead media field above a five-up modular phase grid; each module is a media area, a numeral, a short title and one line.
- **Preserve:** everything — this is the accepted implementation. Five-stage semantic progression, lead media field, five phase media fields, concise copy, no dossier styling.
- **Remove / Replace with:** — · — (out of the rework queue)
- **Media:** six reserved areas — one lead plus five phase areas.
- **Copy:** LOW — 93 words.
- **Responsive:** five columns → six-track 3 + 2 span arrangement at 1024 → two columns with the fifth spanning full width at 768 → single column at 480. Verified at all seven widths.
- **Batch:** NONE — already updated (`REWORKED — ACCEPTED`).
- **Notes:** Quality and direction reference only. Not a layout template: no other study in this plan should reproduce its grid.

#### ARC-S06-004 · 004 Conversion-led · KEEP · —

- **Concept:** Numbered client-facing route from first conversation to design stages, ending in two actions.
- **Preserve:** the 'you always know which stage you are in' framing.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** MEDIUM — 168 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S06-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Project programme — a workstream-by-stage matrix with sheet, set, revision and status fields and no media at all.
- **Preserve:** the content idea that the studio's involvement spans every stage, expressed as narrative rather than as a matrix.
- **Remove:** the programme matrix; the workstream rows; the sheet / set / revision / status fields; the ruled document frame.
- **Replace with:** **replacement structural territory — an art-directed process narrative**: a single continuous horizontal or diagonal progression of large media fields, each field a stage, with stage names set as oversized type crossing the media edges and no numbering apparatus.
- **Media:** from none to five stage fields — this section currently has zero slots in this study and cannot become visual without introducing them.
- **Copy:** LOW — 93 words today; hold, redistributed as one short line per stage.
- **Responsive:** the horizontal progression becomes a vertical sequence at 768 with the scale relationships preserved; no fixed-width slivers, and every stage keeps a legible media proportion when its slot is empty.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with the implemented `003` (lead field + equal module grid) or with `002` (numerals + one image per stage). The distinguishing device here is a continuous, scale-varying progression rather than a repeated module.

### S07 — Studio About

Section rule: who the practice is; not a second manifesto, not a colophon.

#### ARC-S07-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Four scattered image areas beside a short studio statement and three attribute words.
- **Preserve:** the scattered image composition; the whitespace confidence.
- **Remove / Replace with:** — · —
- **Media:** four image areas; unchanged.
- **Copy:** LOW — 83 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S07-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Large display title with a principal portrait plate and a belief statement.
- **Preserve:** the display title; the principal plate.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** LOW — 79 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S07-003 · 003 Structured / Visual Modular · KEEP · —

- **Concept:** Serif question headline with a principal portrait and a four-field attribute row.
- **Preserve:** the question-as-headline device; the attribute row as short visual modules.
- **Remove / Replace with:** — · —
- **Media:** three image areas; unchanged.
- **Copy:** MEDIUM — 103 words. The attribute row is four short labelled facts, not a metadata register, and stays.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S07-004 · 004 Conversion-led · KEEP · —

- **Concept:** Oversized uppercase studio statement with two chips and a two-column supporting note.
- **Preserve:** the oversized statement.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** LOW — 84 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S07-005 · 005 Art-directed / Distinctive · REWORK · AUDIT_ADDED

- **Concept:** Studio described as a monograph colophon with a ruled 'learn more' row and a plate area.
- **Preserve:** the wordmark scale; the single plate; the restraint.
- **Remove:** the colophon labelling and its print-document framing; the ruled label row.
- **Replace with:** the same wordmark and plate composed as a studio portrait — the plate enlarged and offset against the wordmark, with a two-line statement replacing the colophon entries.
- **Media:** one plate retained and enlarged; add a second smaller studio image so the composition is media-led rather than type-only.
- **Copy:** LOW — 87 words; hold.
- **Responsive:** wordmark and plate stack at 768 with the plate keeping its aspect; the wordmark must not clip at 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Differentiate from `ARC-S07-004`, which is already an oversized type statement. Here the plate must carry at least half the composition.

### S08 — Architects & Designers

Section rule: portrait-led; CV-sheet, register and bid-document aesthetics retired.

#### ARC-S08-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Four-portrait roster with name and role beneath each.
- **Preserve:** the portrait grid.
- **Remove / Replace with:** — · —
- **Media:** four portrait areas; unchanged.
- **Copy:** LOW — 54 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S08-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial roster — role label, name and one responsibility line under each portrait.
- **Preserve:** the role-first labelling.
- **Remove / Replace with:** — · —
- **Media:** four portrait areas; unchanged.
- **Copy:** LOW — 85 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S08-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Six-post roster with a portrait strip above a dense list of responsibilities and paired profile/contact buttons per row.
- **Preserve:** the six-post coverage; all six portrait areas; the idea that a larger team can be shown at once.
- **Remove:** the dense responsibility prose under each post; the paired buttons on every row.
- **Replace with:** a portrait-led module grid — one portrait, name, role and a single short line per person, with one route out of the section rather than twelve; capacity carried by the grid, not by the text under it.
- **Media:** six portrait areas retained and enlarged; portraits become the dominant element of each module.
- **Copy:** MEDIUM → LOW; from 158 words to roughly 80, one line per person.
- **Responsive:** 3 × 2 → 2 × 3 → single column; portrait and identity stay paired through every reflow.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S08-004 · 004 Conversion-led · KEEP · —

- **Concept:** Conversion roster — four portraits each with a direct 'talk with' action and a routing line.
- **Preserve:** the per-person action model.
- **Remove / Replace with:** — · —
- **Media:** four portrait areas; unchanged.
- **Copy:** LOW — 94 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S08-005 · 005 Art-directed / Distinctive · REBUILD · AUDIT_ADDED

- **Concept:** Practice register — six posts as ruled table-like columns under a SHEET reference, portraits reduced to labelled cells.
- **Preserve:** the six-post content model.
- **Remove:** the register structure; the SHEET reference; the ruled column framing that turns portraits into cells.
- **Replace with:** **replacement structural territory — a portrait-led asymmetric people composition**: portraits at deliberately unequal sizes across an off-grid field, names set small beside them, no rules and no reference apparatus.
- **Media:** six portrait areas retained but re-proportioned to unequal sizes; portraits become the composition rather than cell contents.
- **Copy:** LOW — 53 words; hold.
- **Responsive:** the asymmetric field becomes a two-column then single-column stack that keeps the size variation proportionally; no portrait may fall below a legible proportion.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with `ARC-S08-006` (featured plate + thumbnail strip) or with the reworked `003` (equal module grid). The device here is unequal scale across an off-grid field.

#### ARC-S08-006 · extension variant · KEEP · —

- **Concept:** Featured member with a large portrait plate above a four-portrait thumbnail strip.
- **Preserve:** the featured-plus-strip hierarchy.
- **Remove / Replace with:** — · —
- **Media:** five portrait areas; unchanged.
- **Copy:** LOW — 98 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S08-007 · extension variant · REBUILD · USER_REQUIRED

- **Concept:** Expanding filmstrip — six fixed-width tab panels, only the selected one revealing a name; collapsed panels are 42–96px slivers.
- **Preserve:** the accessible tablist implementation (real tablist, arrow-key handling, names exposed) as a reusable technique — not the composition.
- **Remove:** the collapsed-sliver mechanism; the fixed panel widths; the dependency on filled media for the composition to read at all.
- **Replace with:** **replacement structural territory — a portrait-led team layout that reads with empty slots**: full-size portrait modules in a grid, with any expand/collapse behaviour operating on a module that is already legible closed.
- **Media:** six portrait areas retained at a proportion that reads when empty — the current failure is that an empty 42px sliver shows nothing at any width.
- **Copy:** HIGH → LOW; from 346 words to roughly 90.
- **Responsive:** grid reflow 3 → 2 → 1 with no horizontal overflow at any width. This is the one confirmed responsive failure in the sector and the replacement must be verified at all seven widths.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** REBUILD rather than BUG_FIX: the failure is conceptual — the composition depends on media being present — so repairing the breakpoints would not fix it.

#### ARC-S08-008 · extension variant · KEEP · —

- **Concept:** Edge-bleeding card row that scrolls horizontally, each card carrying a portrait and a role line.
- **Preserve:** the edge-bleed rhythm; the horizontal scroll as a deliberate device.
- **Remove / Replace with:** — · —
- **Media:** four portrait areas; unchanged.
- **Copy:** MEDIUM — 185 words.
- **Responsive:** **in the verification queue.** Cards clip at the viewport edge by design; the scroll affordance and keyboard route must be confirmed at 768 / 430 / 390 / 320 before this KEEP is final. If the affordance is missing the status becomes BUG_FIX.
- **Batch:** NONE

#### ARC-S08-009 · extension variant · MINOR_FIX · AUDIT_ADDED

- **Concept:** Lead card with contact routes beside a buttoned rail of three further portraits.
- **Preserve:** the lead-card hierarchy; the rail; the honest placeholder contact routes.
- **Remove:** roughly a third of the visible copy — 241 words is high for a roster section.
- **Replace with:** —
- **Media:** three portrait areas; unchanged.
- **Copy:** HIGH → MEDIUM; target roughly 150 words.
- **Responsive:** **in the verification queue.** Rail behaviour at tablet width must be confirmed before this fix is closed.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S09 — Awards & Publications

Section rule: covers, tear sheets and project imagery instead of a bibliography. Four of five
studies currently carry **no media at all**; slots must be introduced, not rearranged.

#### ARC-S09-001 · 001 Universal / Safe · REWORK · USER_REQUIRED

- **Concept:** Two parallel lists of award and publication records with year columns; no media.
- **Preserve:** the awards / publications split; the placeholder-token discipline; the year column only where real data exists.
- **Remove:** the bibliography reading — record rows presented as parallel text lists with no visual anchor.
- **Replace with:** each recognition as a card carrying a cover or project image with the award or publication name and one short context line beneath; the split preserved as two columns of cards rather than two lists.
- **Media:** from none to six areas — one per recognition card. This is the core of the correction.
- **Copy:** MEDIUM → LOW; from 142 words to roughly 90 as rows become cards.
- **Responsive:** two columns of cards → one column at 768; cards keep their media proportion when the slot is empty.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S09-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial recognition page — a tear-sheet plate beside a selected record list.
- **Preserve:** the tear-sheet plate relationship; the premium serif register.
- **Remove / Replace with:** — · —
- **Media:** one tear-sheet area; unchanged.
- **Copy:** LOW — 73 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference and the model for the rest of S09.

#### ARC-S09-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Full record table — year, record, project, kind and a 'field to fill' column, with a counts rail; no media.
- **Preserve:** the idea of one combined record set rather than split lists.
- **Remove:** the table entirely; the counts rail; the field-to-fill column.
- **Replace with:** **replacement structural territory — an editorial recognition-card sequence**: a modular grid of recognition cards, each with a cover or project area, the record name and a single line, grouped by year as visual bands rather than as table rows.
- **Media:** from none to nine areas across the grid.
- **Copy:** MEDIUM → LOW; from 192 words to roughly 100.
- **Responsive:** 3 → 2 → 1 card grid; year bands remain as headings, never as a horizontally scrolling table.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S09-004 · 004 Conversion-led · KEEP · —

- **Concept:** Press-office conversion layout — coverage list beside a press-kit request panel.
- **Preserve:** the press-office panel; the editor-facing route.
- **Remove / Replace with:** — · —
- **Media:** none. Acceptable here: the role is a request panel, and the section's media correction is carried by 001, 003 and 005.
- **Copy:** MEDIUM — 118 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S09-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Back-matter citations — keyed [A-01] / [P-01] entries in bibliographic form under a SHEET reference; no media, highest density in S09.
- **Preserve:** the keying idea that each record belongs to a project, expressed as a visual pairing rather than a citation key.
- **Remove:** the citation format; the bracket keys; the SHEET reference; the back-matter framing.
- **Replace with:** **replacement structural territory — an art-directed recognition spread**: two or three oversized cover or spread fields at unequal scale, each with the recognition set beside it in large type, and a press quotation as a full-width statement.
- **Media:** from none to three large fields.
- **Copy:** HIGH → LOW; from 287 words to roughly 90.
- **Responsive:** unequal fields stack to a single column keeping their scale relationship; the quotation must not clip at 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with the reworked 001 (card grid) or 003 (modular sequence). The device here is a small number of oversized fields, not a grid.

### S10 — Capabilities

Section rule: visual capability groups instead of a consultant matrix. **No study in this section
carries a media area today**; slots must be introduced.

#### ARC-S10-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Three capability groups with in-house / consultant marks on each line.
- **Preserve:** the delivery-mode marking, which is genuinely useful and stated in words rather than symbols.
- **Remove / Replace with:** — · —
- **Media:** none today; one supporting field is optional in a later pass, not required for this status.
- **Copy:** MEDIUM — 163 words; proportionate to three groups.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S10-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Four numbered capacities with short sub-lists, set as an editorial two-by-two.
- **Preserve:** the four-capacity framing; the calm editorial structure.
- **Remove / Replace with:** — · —
- **Media:** none today; optional later.
- **Copy:** MEDIUM — 197 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S10-003 · 003 Structured / Visual Modular · REWORK · AUDIT_ADDED

- **Concept:** Six capability groups behind native disclosure controls, each listing four lines with mode stamps — twenty-four inventory lines and no media.
- **Preserve:** the script-free disclosure pattern; the grouping into capability areas.
- **Remove:** roughly half the inventory lines; the mode stamps repeated on every line.
- **Replace with:** four capability groups as visual modules, each with its own media area and a short summary, with disclosure revealing three or four lines rather than a full inventory.
- **Media:** from none to four areas, one per group — the change that turns this from an inventory into a capability presentation.
- **Copy:** HIGH → MEDIUM; from 293 words to roughly 150.
- **Responsive:** modules 2 × 2 → single column; disclosure stays keyboard operable and script-free at every width.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S10-004 · 004 Conversion-led · KEEP · —

- **Concept:** Three entry routes — 'you have a site / a building / drawings' — each naming a first piece of work.
- **Preserve:** the three-route model; the plain language.
- **Remove / Replace with:** — · —
- **Media:** none today; optional later.
- **Copy:** MEDIUM — 195 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference — the strongest conversion logic in the sector.

#### ARC-S10-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Annex A schedule of services — numbered clauses A1.1–A4.4 with INCLUDED / ON REQUEST / NOT OFFERED stamps; no media.
- **Preserve:** the three-state scope distinction as content, if it can be expressed visually rather than as stamps.
- **Remove:** the annex framing; clause numbering; the stamp column; the schedule structure.
- **Replace with:** **replacement structural territory — an art-directed capability composition**: three or four large media fields, each standing for a capability area, with the capability named in oversized type across it and the three-state distinction expressed as short plain-language lines beneath.
- **Media:** from none to four large fields.
- **Copy:** HIGH → LOW; from 216 words to roughly 100.
- **Responsive:** large fields stack to a single column; type scales down without clipping at 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S11 — Materials & Sustainability

Section rule: **visual materiality** — samples, textures and close-ups are the content. Both flagged
studies currently contain no material imagery at all.

#### ARC-S11-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Six materials, each with a sample area, a use line and a 'what we ask of it' line.
- **Preserve:** the sample-per-material model; the questioning device.
- **Remove / Replace with:** — · —
- **Media:** six sample areas; unchanged.
- **Copy:** HIGH — 263 words across six materials with two lines each; proportionate. Optional trim only.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Closest S11 study to the corrected direction.

#### ARC-S11-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Material board of five sample areas beside four selection questions.
- **Preserve:** the board arrangement.
- **Remove / Replace with:** — · —
- **Media:** five sample areas; unchanged.
- **Copy:** MEDIUM — 166 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S11-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Material record — six entries with used-for / finish / maintenance / end-of-life / evidence fields; no material imagery.
- **Preserve:** the reserved 'evidence' field as a content idea — it is a claims-policy device and must survive in some form.
- **Remove:** the five-field record per material; the specification-record structure.
- **Replace with:** **replacement structural territory — a modular material grid**: each material a module built on a large sample area with the material name, one use line and the reserved evidence field beneath, so the capacity is carried by the grid of samples rather than by fields.
- **Media:** from none to six sample areas — the single most important change in this section.
- **Copy:** HIGH → LOW; from 260 words to roughly 100.
- **Responsive:** 3 → 2 → 1 module grid; sample areas keep a proportion that still reads as material at 320 rather than collapsing to bands.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with `002`'s board: this one is a regular module grid with per-material information; the board is a loose arrangement with questions.

#### ARC-S11-004 · 004 Conversion-led · KEEP · —

- **Concept:** Sample-set request — a sample box media area beside four numbered contents and two actions.
- **Preserve:** the physical sample-set offer.
- **Remove / Replace with:** — · —
- **Media:** one sample box area; unchanged.
- **Copy:** MEDIUM — 139 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S11-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Annotated wall build-up — five drawn layer bands read outside-to-inside under a SHEET reference; no photographic media.
- **Preserve:** the layer-by-layer reasoning as narrative content.
- **Remove:** the technical detail drawing; the annotation apparatus; the SHEET reference; the drawn layer bands as the primary visual device.
- **Replace with:** **replacement structural territory — an art-directed material study**: three or four oversized texture fields at close range, each with a single line about what the material is asked to do, composed as a full-bleed sequence rather than a diagram.
- **Media:** from five drawn bands to four photographic texture fields.
- **Copy:** HIGH → LOW; from 263 words to roughly 90.
- **Responsive:** full-bleed fields stack; each keeps enough height to read as texture at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S12 — Client Testimonials

Section rule: editorial quotation composition; no fabricated testimonials. Density is inherently
high because quotations are the content.

#### ARC-S12-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Featured quote over an image with four supporting quote cards.
- **Preserve:** the featured-over-image treatment; the card rhythm.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** HIGH — 232 words; the content is quotations and needs them.
- **Responsive:** unchanged; quotation and attribution stay together.
- **Batch:** NONE

#### ARC-S12-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Single stepped testimonial with a large display word and a position readout.
- **Preserve:** the stepper interaction and its live region; the display word.
- **Remove / Replace with:** — · —
- **Media:** one portrait area; unchanged.
- **Copy:** EXCESSIVE by count — 437 words — but the page holds five quotations of which one is visible at a time. The content needs the text; the *visible* density is low. No reduction required.
- **Responsive:** **in the verification queue** — confirm the stepper controls keep a 44px target and the live region announces correctly at 390 and 320.
- **Batch:** NONE

#### ARC-S12-003 · 003 Structured / Visual Modular · KEEP · —

- **Concept:** Quote wall of six testimonials interleaved with two project reference cards.
- **Preserve:** the interleaved project references; the uneven wall rhythm.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** HIGH — 260 words, inherent to a quote wall.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S12-004 · 004 Conversion-led · KEEP · —

- **Concept:** Three testimonials with one set over an image, closing on a references request.
- **Preserve:** the 'ask for the rest' panel; the honest permission language.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** HIGH — 210 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S12-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Annex B client references — keyed [REF-01] statements with relationship, signatory and dated fields.
- **Preserve:** the distinction between a written reference and a lifted marketing quote — a real professional idea worth keeping as content.
- **Remove:** the annex framing; the bracket keys; the relationship / signatory / dated field rows; the ruled document structure.
- **Replace with:** **replacement structural territory — an art-directed quotation composition**: one quotation set at display scale across a large project image, with two further quotations at smaller scale beneath, attribution reduced to a role and a project reference.
- **Media:** one plate area → three project areas, with the lead area enlarged to carry the display quotation.
- **Copy:** HIGH → MEDIUM; from 309 words to roughly 150, three quotations rather than a reference set.
- **Responsive:** display quotation reflows without clipping at 320; quotation and attribution never separate.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with `001`, which is already a featured quote over an image. Differentiate by scale: here the quotation is display-sized and the image is the ground, and there are three quotations rather than five cards.

### S13 — Featured Project Case Study

Section rule: a **section**, not the S24 page; no dossier framing.

#### ARC-S13-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Case study with a lead image, a metadata rail and two narrative sections.
- **Preserve:** the lead image plus metadata rail.
- **Remove / Replace with:** — · —
- **Media:** three image areas; unchanged.
- **Copy:** MEDIUM — 185 words.
- **Responsive:** unchanged; rail releases to flow.
- **Batch:** NONE

#### ARC-S13-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Held plate beside a scrolling account of the project.
- **Preserve:** the held-plate interaction; the premium register.
- **Remove / Replace with:** — · —
- **Media:** one held plate; unchanged.
- **Copy:** HIGH — 204 words; acceptable beside a held plate. Optional trim.
- **Responsive:** **in the verification queue** — confirm the held/sticky plate releases to normal flow at 768 and below rather than pinning over the text.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S13-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Project dossier — facts band, account column, numbered decisions and a credits grid, with three plates.
- **Preserve:** the 'decisions, in order' content model; all three plates; the numbered decision sequence.
- **Remove:** the dossier framing; the facts band presented as a record strip; the credits grid.
- **Replace with:** each decision as an image-and-text module at larger media scale, with the facts reduced to three or four concise metadata items set beside the lead plate rather than banded across the top.
- **Media:** three plates retained and enlarged — the lead plate to at least half the section height.
- **Copy:** HIGH → MEDIUM; from 272 words to roughly 160.
- **Responsive:** decision modules alternate at desktop and stack at 768; plates keep their aspect rather than shrinking to strips.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S13-004 · 004 Conversion-led · KEEP · —

- **Concept:** Case study opening on the client's first sentence, closing on a conversation invitation.
- **Preserve:** the opening-sentence device.
- **Remove / Replace with:** — · —
- **Media:** two image areas; unchanged.
- **Copy:** HIGH — 225 words. Optional trim.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S13-005 · 005 Art-directed / Distinctive · REWORK · AUDIT_ADDED

- **Concept:** Existing/proposed plate pairs with an annotation line and a schedule of change.
- **Preserve:** the matched existing/proposed pairing — a genuinely strong sector idea; all four plates; the annotation line as a short caption.
- **Remove:** the sheet framing and plate references; the schedule-of-change table.
- **Replace with:** the pairs presented at full width as a before/after sequence with the annotation as a single caption per pair, and the change content redistributed into those captions.
- **Media:** four plates retained and enlarged to full-width pairs.
- **Copy:** HIGH → MEDIUM; from 266 words to roughly 140.
- **Responsive:** pairs sit side by side at desktop and stack as labelled before/after at 768 and below — never a preserved overlap or a fixed-width comparison.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Distinct from the reworked `003`: that one is a decision sequence, this one is a paired comparison. Both must keep their own device.

### S14 — Project Gallery

Section rule: conventional visible grid maximum **3 × 3 = 9** media items. A maximum, not a
requirement; editorial and carousel presentations may use fewer.

#### ARC-S14-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Eight gallery images across four aspect ratios with short record captions.
- **Preserve:** the mixed-ratio rhythm; the eight-frame arrangement.
- **Remove / Replace with:** — · —
- **Media:** eight image areas — within the nine maximum; no reduction required.
- **Copy:** LOW — 93 words.
- **Responsive:** unchanged; spans remap at each step so no cell drops below half the grid.
- **Batch:** NONE
- **Notes:** Phase 0 raised the frame count as an open question. Resolved here: eight is inside the 3 × 3 maximum, so this returns to KEEP.

#### ARC-S14-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Four plates presented one at a time with monograph-style captions on hairlines.
- **Preserve:** the one-at-a-time sequencing; the caption discipline.
- **Remove / Replace with:** — · —
- **Media:** four plate areas; unchanged.
- **Copy:** MEDIUM — 122 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** 'Plate' captioning is a label, not a driving metaphor; renaming to plain captions is optional and not required for this status.

#### ARC-S14-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Contact sheet — eighteen equal frames above a numbered legend of eighteen entries.
- **Preserve:** the single-ratio discipline that makes frames genuinely comparable; the grid as the section's structural idea.
- **Remove:** nine of the eighteen frames; the numbered legend entirely; the contact-sheet framing.
- **Replace with:** a 3 × 3 grid of nine images at one consistent ratio, each carrying a short caption in place of a legend number, with generous gutters so the grid reads as a gallery rather than a sheet.
- **Media:** eighteen frames → nine, at a single ratio.
- **Copy:** MEDIUM → LOW; from 157 words to roughly 60 once the legend is gone.
- **Responsive:** 3 × 3 → 2-up → 1-up, the ratio held constant at every step.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S14-004 · 004 Conversion-led · KEEP · —

- **Concept:** Six gallery images interrupted once by a project-book request band.
- **Preserve:** the single interruption band.
- **Remove / Replace with:** — · —
- **Media:** six image areas; unchanged.
- **Copy:** MEDIUM — 161 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S14-005 · 005 Art-directed / Distinctive · REWORK · AUDIT_ADDED

- **Concept:** Gallery ordered by scale — situation, building, room, detail — under a SHEET reference with axis labels and 'not to scale' notation.
- **Preserve:** the far-to-close scale ordering, which is the strongest sector-native idea in S14; the nine-image count, which already meets the maximum.
- **Remove:** the SHEET reference; the axis labels; the NTS notation; the ruled sheet frame.
- **Replace with:** the same ordering expressed through image scale itself — the situation image full-bleed, the building and room images at reducing widths, the detail images small and close — so the sequence is legible from proportion rather than from labels.
- **Media:** nine areas retained, re-proportioned from equal cells to a descending scale sequence.
- **Copy:** HIGH → LOW; from 225 words to roughly 70, one short caption per group.
- **Responsive:** the descending scale sequence stacks and keeps its relative proportions; the full-bleed opener stays full-bleed at every width.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Differentiation from the reworked `003` is essential — both land on nine images. `003` is one ratio in a regular grid; `005` is nine images at deliberately unequal scale in a narrative order.

### S15 — Sectors & Markets

Section rule: image-led markets; maps, matrices and atlases are not a styling device. Both flagged
studies have **no media at all**.

#### ARC-S15-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Six market cards, each with an image field, short description and an explore link.
- **Preserve:** the six-card market grid; image per market.
- **Remove / Replace with:** — · —
- **Media:** six image areas; unchanged.
- **Copy:** MEDIUM — 118 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S15-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Three broad fields with large numerals and generous image blocks.
- **Preserve:** the numeral-led field rhythm; the generous image blocks.
- **Remove / Replace with:** — · —
- **Media:** three image areas; unchanged.
- **Copy:** LOW — 80 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S15-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Capability matrix — markets as rows against architecture / interiors / reuse columns with Core / Selective values; no media.
- **Preserve:** the idea that disciplines combine differently per market, expressed as short lines rather than as cells.
- **Remove:** the matrix entirely; the row/column structure; the Core/Selective value grid.
- **Replace with:** **replacement structural territory — a modular market grid**: each market a module with its own image area, the market name, and one line naming which disciplines it combines, so the comparison is readable module by module rather than as a table.
- **Media:** from none to six areas, one per market module.
- **Copy:** LOW — 88 words; hold, redistributed across modules.
- **Responsive:** 3 → 2 → 1 module grid; nothing becomes a horizontally scrolling table at any width.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Convergence risk with `001`, which is already a six-card market grid. Differentiate: `001` is a card grid with descriptions and links; `003` is a comparison grid whose modules carry the discipline combination as their content.

#### ARC-S15-004 · 004 Conversion-led · KEEP · —

- **Concept:** Four pathway cards routing a visitor by project type toward one conversation.
- **Preserve:** the pathway routing; the plain language.
- **Remove / Replace with:** — · —
- **Media:** none today; optional later.
- **Copy:** MEDIUM — 120 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S15-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Practice atlas — a scale-by-context grid of nine cells, one marked 'open territory'; no media.
- **Preserve:** the scale-versus-context idea as narrative, not as a matrix.
- **Remove:** the atlas grid; the axis structure; the cell notation.
- **Replace with:** **replacement structural territory — an art-directed market sequence**: three or four full-bleed market images at unequal heights, each with the market named in oversized type and one line placing it on the scale-versus-context idea.
- **Media:** from none to four full-bleed fields.
- **Copy:** MEDIUM → LOW; from 125 words to roughly 80.
- **Responsive:** full-bleed fields stack, each keeping enough height to read as an image at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S16 — Press & News

Section rule: editorial cards instead of a press register.

#### ARC-S16-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Featured studio note with an image beside four secondary update links.
- **Preserve:** the feature/list split.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** LOW — 82 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S16-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Journal-style issue page — one long read plus three note cards, each with an image.
- **Preserve:** the long-read plus notes structure.
- **Remove / Replace with:** — · —
- **Media:** four image areas; unchanged.
- **Copy:** LOW — 92 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S16-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Press-room archive — a filterable date / type / title / topic table of six entries; no media.
- **Preserve:** the filter-by-type idea and its script-free interaction; the six-entry coverage.
- **Remove:** the table structure; the four-column row format.
- **Replace with:** a visual archive — each entry a card with a thumbnail area, headline, date and type chip, filtered by the same control; capacity carried by the card grid.
- **Media:** from none to six thumbnail areas.
- **Copy:** MEDIUM — 115 words; roughly held, redistributed into cards.
- **Responsive:** 3 → 2 → 1 card grid; the filter row wraps rather than scrolling off the edge.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S16-004 · 004 Conversion-led · KEEP · —

- **Concept:** Press room with a current feature and three resource panels for editors.
- **Preserve:** the three-resource panel model; the honesty about not using publication logos.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** MEDIUM — 109 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S16-005 · 005 Art-directed / Distinctive · KEEP · —

- **Concept:** Pin-up press desk — a cover note and three pinned cards on a board.
- **Preserve:** the pin-board arrangement.
- **Remove / Replace with:** — · —
- **Media:** four image areas; unchanged.
- **Copy:** MEDIUM — 102 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** A spatial metaphor rather than a documentary one — a pin board is a studio object, not professional paperwork. Stays.

### S17 — Studio Locations

Section rule: location cards and studio imagery instead of a coordinate atlas.

#### ARC-S17-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Three studio cards with an image, address lines and a details link.
- **Preserve:** the three-card location grid.
- **Remove / Replace with:** — · —
- **Media:** three image areas; unchanged.
- **Copy:** LOW — 79 words.
- **Responsive:** unchanged; address stays first-class at small widths.
- **Batch:** NONE

#### ARC-S17-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Studio portraits — one principal location given a large panel, two smaller beneath.
- **Preserve:** the principal-plus-two hierarchy.
- **Remove / Replace with:** — · —
- **Media:** three image areas; unchanged.
- **Copy:** LOW — 70 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S17-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Studio directory table — location, address, access and local time columns; no media.
- **Preserve:** the access and local-time content, which is genuinely useful; the three-location coverage.
- **Remove:** the directory table; the column structure.
- **Replace with:** location cards carrying a studio image, the address, and access and local-time as two short lines beneath — the same information, grouped visually per location instead of tabulated across locations.
- **Media:** from none to three studio image areas.
- **Copy:** LOW — 96 words; hold.
- **Responsive:** cards 3 → 2 → 1; address and access lines never truncate.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Convergence risk with `001`. Differentiate: `001` is a card grid with a details link; `003` carries the full practical set — access, local time, address — inside each card.

#### ARC-S17-004 · 004 Conversion-led · KEEP · —

- **Concept:** Visit-led locations page — one featured studio with actions and three alternative routes.
- **Preserve:** the visit-first framing.
- **Remove / Replace with:** — · —
- **Media:** one image area; unchanged.
- **Copy:** MEDIUM — 114 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S17-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Practice atlas — three studios as lettered coordinate cells on a network diagram; no media.
- **Preserve:** the shared-practice framing as narrative content.
- **Remove:** the coordinate cells; the network diagram; the lettering system.
- **Replace with:** **replacement structural territory — an art-directed studio-network composition**: three large city or studio images at unequal scale, each with the city name in oversized type, and one line connecting them as a single practice.
- **Media:** from none to three large fields.
- **Copy:** LOW — 95 words; hold.
- **Responsive:** unequal fields stack keeping their scale relationship; city names scale without clipping.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S18 — Studio Stats

Section rule: large figures, short labels, no spreadsheets or measured drawings; **every real
number must be verifiable in production use** and placeholder figures must be obviously placeholder.

#### ARC-S18-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Four large figures with short labels and one-line context.
- **Preserve:** the large-figure scale; the one-line context per figure.
- **Remove / Replace with:** — · —
- **Media:** none today; optional supporting imagery later.
- **Copy:** LOW — 79 words.
- **Responsive:** unchanged 4 → 2 × 2 → 1.
- **Batch:** NONE
- **Notes:** Positive reference — already the treatment the user described.

#### ARC-S18-002 · 002 Premium / Editorial · REWORK · USER_REQUIRED

- **Concept:** Editorial stat block — a large '1' anchoring three supporting figures under a measure label, on a ruled grid.
- **Preserve:** the 'one shared practice' anchoring figure — a strong idea; the editorial hierarchy between the anchor and the supporting figures.
- **Remove:** the sheet/measure label; the ruled grid framing that makes it read as a data sheet.
- **Replace with:** the anchor figure at display scale against a studio image, with the three supporting figures set beneath in plain type and no rules.
- **Media:** from none to one large supporting field behind or beside the anchor figure.
- **Copy:** LOW — 66 words; hold.
- **Responsive:** anchor figure scales down without clipping; supporting figures go 3 → 1 at 480.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S18-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Practice data index — six measures as a numbered table with a context column; no media.
- **Preserve:** the principle that every figure carries its own context, and the honest labelling of figures as illustrative.
- **Remove:** the table; the numbering; the context column as a table cell.
- **Replace with:** **replacement structural territory — a modular figure grid**: six modules, each a large numeral with a short label and its context line, grouped two or three across, with two image fields breaking the grid so it reads as a composition rather than a dataset.
- **Media:** from none to two fields inside the grid.
- **Copy:** LOW — 99 words; hold.
- **Responsive:** 3 → 2 → 1 module grid; numerals scale rather than wrap.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S18-004 · 004 Conversion-led · KEEP · —

- **Concept:** Three figures framed around collaboration, closing on one action.
- **Preserve:** the collaboration framing.
- **Remove / Replace with:** — · —
- **Media:** none today; optional later.
- **Copy:** LOW — 94 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S18-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Measurement drawing — four figures set on a dimension-line field with 'not to scale' notation.
- **Preserve:** the dimension-line rhythm only as a purely graphic idea, if it is reused at all; the four-figure content.
- **Remove:** the measurement-drawing metaphor; the dimension lines as an annotation system; the NTS notation.
- **Replace with:** **replacement structural territory — a large-stat composition**: four figures at very large scale across a generous field, one paired with a full-bleed studio image, the relationships expressed by placement and scale rather than by dimension lines.
- **Media:** one measure band → one full-bleed field plus one supporting field.
- **Copy:** LOW — 86 words; hold.
- **Responsive:** figures reflow to a stacked sequence keeping their scale hierarchy; the full-bleed field re-proportions.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with the reworked `002` (single anchor figure + image) or the rebuilt `003` (module grid). Here all four figures are large and the composition is spatial.

### S19 — Project Inquiry

Section rule: modern form composition; not a working sheet. Media is legitimately absent in this
role.

#### ARC-S19-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Two-part inquiry form — about you and about the project — with a three-step progress line.
- **Preserve:** the two-part grouping; the step indicator; the honest consent line.
- **Remove / Replace with:** — · —
- **Media:** none; appropriate to the role.
- **Copy:** LOW — 94 words.
- **Responsive:** unchanged; fields full width and tappable at small widths.
- **Batch:** NONE

#### ARC-S19-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Three-question editorial inquiry with a large numeral and a single send action.
- **Preserve:** the three-question reduction; the restraint.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 76 words.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference.

#### ARC-S19-003 · 003 Structured / Visual Modular · KEEP · —

- **Concept:** Detailed brief form with contact and project groups, stage radios and a scope field.
- **Preserve:** the stage-radio grouping; the detailed-brief territory.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 77 words. Form-heavy by role, not by metaphor: the fields are the content.
- **Responsive:** unchanged; two-column groups collapse in a sensible order.
- **Batch:** NONE

#### ARC-S19-004 · 004 Conversion-led · KEEP · —

- **Concept:** Situation-first inquiry — three starting points feeding one short form.
- **Preserve:** the situation-first routing.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** MEDIUM — 116 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S19-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Inquiry laid out as a working project sheet with coordinate fields and an 'issue the brief' action.
- **Preserve:** the short field set — the form itself is fine; only its framing is wrong.
- **Remove:** the working-sheet layout; the coordinate field apparatus; the 'issue' language; the ruled sheet frame.
- **Replace with:** **replacement structural territory — an image-framed enquiry**: the short form set in a generous field beside one large contextual project image, with a display-scale invitation line above it and no ruled apparatus.
- **Media:** from none to one large contextual field — the element that makes this the *art-directed* variant rather than a second clean form.
- **Copy:** LOW — 82 words; hold.
- **Responsive:** image and form sit side by side at desktop and stack at 768 with the form first; fields stay full width and tappable at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Convergence risk with `002`, which is already a restrained short form. The image field and display invitation are what keep them apart — without media this study would duplicate `002`.

### S20 — Consultation CTA

Section rule: concise invitation; not an agenda document.

#### ARC-S20-001 · 001 Universal / Safe · KEEP · —

- **Concept:** Centred consultation panel with two actions and three reassurance points.
- **Preserve:** the reassurance points.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 54 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S20-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial session card — large numeral, three agenda lines and one action.
- **Preserve:** the numeral-led session framing.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 58 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S20-003 · 003 Structured / Visual Modular · KEEP · —

- **Concept:** Consultation menu of three formats with best-for and format columns.
- **Preserve:** the three-format comparison.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 99 words. The comparison is light and genuinely useful; converting the columns to cards is optional, not required.
- **Responsive:** unchanged; the comparison stacks rather than scrolling horizontally.
- **Batch:** NONE

#### ARC-S20-004 · 004 Conversion-led · KEEP · —

- **Concept:** Consultation request with session type, date and time-window fields.
- **Preserve:** the three-step confirmation framing; the honesty that nothing is connected.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 79 words.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S20-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Meeting sheet — a 20/20/20 agenda laid out as a ruled document with an agenda axis.
- **Preserve:** the three-part agenda content — the hour is a useful thing to describe.
- **Remove:** the meeting-sheet layout; the agenda axis; the ruled document frame; the timing notation as apparatus.
- **Replace with:** **replacement structural territory — a full-bleed invitation**: one large studio or project image carrying a display-scale invitation line, with the three agenda parts as three short lines beneath and a single action.
- **Media:** from none to one full-bleed field.
- **Copy:** MEDIUM → LOW; from 107 words to roughly 70.
- **Responsive:** full-bleed field re-proportions rather than cropping to a band; the action stays above the fold at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Convergence risk with `002` (numeral-led session card, also agenda-based). The full-bleed image and display line are the separation; `002` stays type-only and compact.

### S21 — Subpage Hero

**Role clarification, all five.** A conventional website internal-page hero: background-image,
contained-image, split-image, typography-only or compact banner, carrying a page title, an optional
short description, an optional contextual label and an optional CTA. It must not be a dossier
cover, register, metadata database, folio, drawing sheet or contents table. **Four of five studies
have no media area at all** — image-led forms require slots to be introduced.

#### ARC-S21-001 · 001 Universal / Safe · REWORK · USER_REQUIRED

- **Concept:** Subpage header — eyebrow, page title, standfirst and a four-field metadata row.
- **Preserve:** the eyebrow / title / standfirst spine; the no-image case, which the set needs.
- **Remove:** the four-field metadata row that makes it read as a document header.
- **Replace with:** the simple, classic internal-page hero — eyebrow, title, one-line description, generous space, at most one small contextual label in place of the metadata row.
- **Media:** none, deliberately. This is the typography-only member of the set.
- **Copy:** LOW — 86 words → roughly 45 once the metadata row is gone.
- **Responsive:** title first at every width; the label wraps rather than truncating.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S21-002 · 002 Premium / Editorial · REWORK · USER_REQUIRED

- **Concept:** Title block above a contained 21:9 image strip — the closest study to the clarified intent.
- **Preserve:** the contained strip and its proportion; the title block above it.
- **Remove:** the caption apparatus and record labelling around the strip.
- **Replace with:** a premium image-led subpage hero — the same contained strip, larger, with the page title and one description line, and no caption furniture.
- **Media:** one contained strip retained and enlarged; it stays *contained* rather than full-bleed so it differs from 005.
- **Copy:** LOW — 86 words → roughly 40.
- **Responsive:** strip re-proportions from 21:9 toward 16:9 and 3:2 as width falls, never collapsing to a band.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S21-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Dense page header with an eight-field metadata grid and an on-this-page contents list — a dossier cover.
- **Preserve:** the idea that a long page may need in-page contents, recorded here as belonging elsewhere (S22 or the page body), not in the hero.
- **Remove:** the eight-field metadata grid; the contents list; the dossier framing.
- **Replace with:** **replacement structural territory — a structured split hero**: page title and one description line in one half, a contained image module in the other, with at most two short contextual labels — modular, but composed of type and media rather than fields.
- **Media:** from none to one image module.
- **Copy:** MEDIUM → LOW; from 133 words to roughly 45.
- **Responsive:** split becomes stacked at 768 with the title first; the image module keeps its aspect.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S21-004 · 004 Conversion-led · REWORK · USER_REQUIRED

- **Concept:** Subpage header with a single contextual action panel beside the title.
- **Preserve:** the single contextual action rule — exactly right for this role.
- **Remove:** the panel framing around the action; the long explanatory copy.
- **Replace with:** a context- and CTA-aware hero — title, one short line, and one action set inline rather than in a bordered panel.
- **Media:** optional single contained image; may stay media-free if the set needs the balance.
- **Copy:** MEDIUM → LOW; from 121 words to roughly 45.
- **Responsive:** action drops below the title at 768 and stays a full-width target at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S21-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Running head and folio — part/folio references above the page title.
- **Preserve:** the type scale only. Nothing structural survives.
- **Remove:** the folio and running-head apparatus; the part references; the print-document framing.
- **Replace with:** **replacement structural territory — a full-bleed image-background banner**: the page title set large over a background image field, with an optional short description, and no reference apparatus. This is the image-background member of the set.
- **Media:** from none to one full-bleed background field.
- **Copy:** LOW — 81 words → roughly 35.
- **Responsive:** background field re-proportions and keeps a legible title contrast band at every width; it must still read as a hero when the slot is empty.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S22 — Breadcrumb / Context Navigation

**Role clarification, all five.** Function must remain a conventional website breadcrumb —
`Home / Projects / Residential / Project Name`. Variation is allowed in typography, separator
treatment, container, spacing, background and subtle context. Project pagers, sibling navigation,
contents navigation, key plans, technical locators, mini sitemaps and indexes are not allowed as
the primary function. Media: none in any variant — this role is navigation, not presentation.

#### ARC-S22-001 · 001 Universal / Safe · KEEP · USER_REQUIRED

- **Concept:** Plain four-level breadcrumb trail with the current page marked programmatically.
- **Preserve:** the trail markup, the `aria-current` handling and the wrapping behaviour — this is the section's reference implementation.
- **Remove / Replace with:** — · —
- **Media:** none.
- **Copy:** LOW — 60 words.
- **Responsive:** unchanged; wraps rather than truncating.
- **Batch:** NONE
- **Notes:** Confirmed against the clarified role. No change required.

#### ARC-S22-002 · 002 Premium / Editorial · MINOR_FIX · USER_REQUIRED

- **Concept:** Uppercase trail with a separate 'back to parent' return link.
- **Preserve:** the trail and its quiet uppercase register; the premium spacing.
- **Remove:** the second navigation landmark, which slightly broadens the role beyond a breadcrumb. The return link may stay as an inline element inside the single breadcrumb landmark.
- **Replace with:** —
- **Media:** none.
- **Copy:** LOW — 63 words.
- **Responsive:** unchanged.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S22-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Context bar — trail plus sibling-page chips plus an on-this-page contents list.
- **Preserve:** the narrow-width scroll-region technique, which is a good solution to a long trail.
- **Remove:** the sibling-page chips; the on-this-page contents list — both are excluded from this role.
- **Replace with:** **replacement structural territory — a contained breadcrumb bar**: the trail inside a full-width tinted container with generous padding and a subtle collection label, using the existing scroll-region technique when the trail is long.
- **Media:** none.
- **Copy:** MEDIUM → LOW; from 116 words to roughly 30 once the chips and contents go.
- **Responsive:** the scroll region is retained with a visible affordance and a keyboard route; the trail is never hidden.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S22-004 · 004 Conversion-led · REBUILD · USER_REQUIRED

- **Concept:** Trail above a previous/next project pager with a contextual link.
- **Preserve:** the rule that a link names its destination in full rather than saying 'next'.
- **Remove:** the previous/next project pager — breadcrumbs are not project navigation.
- **Replace with:** **replacement structural territory — a breadcrumb with one contextual continuation**: the trail, followed inline by a single named onward link belonging to the current branch (for example the parent collection), still inside one navigation landmark.
- **Media:** none.
- **Copy:** MEDIUM → LOW; from 101 words to roughly 30.
- **Responsive:** trail wraps; the continuation link drops beneath it at 480 rather than truncating.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S22-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Sheet-reference trail beside a nine-cell key plan locating the page in a set.
- **Preserve:** the triple-marking of the current state — marked by text, not by fill alone — as an accessibility technique.
- **Remove:** the key plan entirely; the sheet references; the drawing-set locator concept.
- **Replace with:** **replacement structural territory — a typographically distinctive breadcrumb**: the trail set at unusual scale or letter-spacing on a contrasting ground, with a hairline rule and a distinctive separator glyph, and nothing else.
- **Media:** none.
- **Copy:** MEDIUM → LOW; from 119 words to roughly 25.
- **Responsive:** the enlarged trail wraps to two lines rather than scrolling; separators stay legible at 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** This is the study that proves `005` can be distinctive without changing a component's role. Distinctiveness here is type and ground only.

### S23 — Architecture / Interior Service Detail

**Whole-section correction, all five.** A visual service detail page. Useful content capacity —
guidance, not a template: service hero/title, short intro, large image or video, three to four
service aspects, image-and-text content, simple process, a relevant project, a concise FAQ, a CTA.
The five studies must remain structurally distinct. Current set averages 630 visible words with
almost no media; that ratio is the correction.

#### ARC-S23-001 · 001 Universal / Safe · REWORK · USER_REQUIRED

- **Concept:** Service page — breadcrumb, title beside a facts rail, included/excluded pair, stages, related services. 485 words, two small image areas.
- **Preserve:** the included/excluded distinction as content; the enquiry close; the responsive rail behaviour, which already releases correctly.
- **Remove:** roughly half the body copy; the included/excluded lists presented as specification columns.
- **Replace with:** the clarified flow at its plainest — title area, short intro, one large media field, three to four aspects as cards, one image-and-text block, a simple process strip, a related project, a short FAQ, the CTA. Included/excluded becomes two short lists inside one aspect card.
- **Media:** two small areas → one large lead field plus three aspect areas plus one project area.
- **Copy:** EXCESSIVE → MEDIUM; from 485 words to roughly 230, distributed across visual sections.
- **Responsive:** rail releases to flow at 1024; the lead field re-proportions; aspect cards go 4 → 2 → 1.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S23-002 · 002 Premium / Editorial · REWORK · USER_REQUIRED

- **Concept:** Editorial service essay at a single measure with a colophon of service facts at the foot. 528 words, one wide plate.
- **Preserve:** the wide plate; the calm single measure; the editorial voice.
- **Remove:** the colophon of service facts; roughly half the essay.
- **Replace with:** an editorial service page paced by media — the wide plate as an opening field, two further image-and-text passages breaking the measure, the facts reduced to a short line beneath the title, and a quiet CTA at the close.
- **Media:** one wide plate → one lead field plus two in-body fields.
- **Copy:** EXCESSIVE → MEDIUM; from 528 words to roughly 250.
- **Responsive:** measure holds at wide widths; in-body media reflows without widening the column.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S23-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Scope document — numbered clauses 1.0–6.0, a deliverables table and a question register. 764 words, no media. The most document-like study in the sector.
- **Preserve:** the FAQ content as a short question set; the completeness of the scope information as source material for the aspects.
- **Remove:** clause numbering; the deliverables table; the question register; the entire document frame.
- **Replace with:** **replacement structural territory — a modular visual service page**: a lead media field, then the service explained as a grid of four aspect modules each with its own image area, a simple three-step process strip, one project example, and a short accordion FAQ. Capacity comes from the module grid and disclosure, never from clause prose.
- **Media:** from none to one lead field plus four aspect areas plus one project area.
- **Copy:** EXCESSIVE → MEDIUM; from 764 words to roughly 250, with the longest material behind the FAQ accordion.
- **Responsive:** aspect modules 4 → 2 → 1; accordion stays script-free and fully reachable.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S23-004 · 004 Conversion-led · REWORK · USER_REQUIRED

- **Concept:** Decision-ordered service page closing on a labelled placeholder enquiry form. 553 words, no media.
- **Preserve:** the self-selection pair — honestly sending the wrong reader elsewhere; the real accessible enquiry form; the enquiry close.
- **Remove:** roughly half the prose; the argument-in-text structure that carries the page today.
- **Replace with:** the same decision order shown rather than argued — a large lead field, the self-selection pair as two image-backed cards, two short aspects, a project example, then the form.
- **Media:** from none to one lead field plus two card areas plus one project area.
- **Copy:** EXCESSIVE → MEDIUM; from 553 words to roughly 240.
- **Responsive:** cards stack; the form stays full width with tappable fields at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S23-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Responsibility ledger — five stages split into studio-does / you-provide columns across a spine. 819 words, the highest in the sector.
- **Preserve:** the stage-by-stage responsibility content, expressed briefly; the four-frame record strip as media.
- **Remove:** the ledger structure; the two-column responsibility split; the spine; roughly three quarters of the copy.
- **Replace with:** **replacement structural territory — an art-directed service story**: full-bleed media fields alternating with display-scale statements, the five stages reduced to five short lines set against imagery, and a single closing action. The service is told visually; responsibilities appear as one short paragraph, not as a ledger.
- **Media:** four record images → four full-bleed fields plus one closing field.
- **Copy:** EXCESSIVE → LOW/MEDIUM; from 819 words to roughly 200.
- **Responsive:** full-bleed fields keep proportion and stack; display statements scale without clipping at 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S24 — Project Detail

Section rule: a portfolio-style project page. No dossiers, issue sets, drawing registers,
schedule-led compositions or drawing-sheet navigation.

#### ARC-S24-001 · 001 Universal / Safe · MINOR_FIX · AUDIT_ADDED

- **Concept:** Three-chapter project case study — context, approach, delivery — with a project-facts ledger at the foot.
- **Preserve:** the three-chapter narrative; the lead image scale; all five image areas.
- **Remove:** the closing project-facts ledger block as a ruled record.
- **Replace with:** the same facts as three or four concise metadata items set beneath the lead image.
- **Media:** five image areas; unchanged.
- **Copy:** HIGH — 251 words; light trim only.
- **Responsive:** unchanged.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Closest S24 study to the desired direction; the fix is contained to the closing block.

#### ARC-S24-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Long-form editorial case study in three chapters with a chapter jump bar and pull statements.
- **Preserve:** the chapter structure; the pull statements; media throughout.
- **Remove / Replace with:** — · —
- **Media:** six image areas; unchanged.
- **Copy:** HIGH — 259 words, proportionate to a project page.
- **Responsive:** **in the verification queue** — confirm the chapter jump bar behaves at 430 / 390 / 320 and does not become a clipped horizontal strip.
- **Batch:** NONE
- **Notes:** The 'folio' label is a word, not a driving metaphor; renaming it is optional and does not change the status.

#### ARC-S24-003 · 003 Structured / Visual Modular · REBUILD · USER_REQUIRED

- **Concept:** Project dossier with a workstream table, numbered drawings (PLAN / NTS) and a credits ledger.
- **Preserve:** the workstream content as short narrative; the five media areas as a quantity.
- **Remove:** the dossier framing; the workstream table; the drawing numbering and NTS notation; the credits ledger.
- **Replace with:** **replacement structural territory — a modular project page**: project hero, concise metadata line, then the project told through image-and-text modules — one per workstream — and a controlled gallery of no more than nine frames, closing on related projects.
- **Media:** five drawing/record areas → one hero field, four module areas and a gallery block; photographic rather than drawn.
- **Copy:** HIGH → MEDIUM; from 251 words to roughly 180.
- **Responsive:** modules alternate then stack; the gallery reflows 3 → 2 → 1 with no horizontal scroll.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S24-004 · 004 Conversion-led · KEEP · —

- **Concept:** Case study connecting situation, response and delivery to related expertise and a next project.
- **Preserve:** the related-expertise and next-project routes.
- **Remove / Replace with:** — · —
- **Media:** five image areas; unchanged.
- **Copy:** HIGH — 222 words; optional trim.
- **Responsive:** unchanged.
- **Batch:** NONE

#### ARC-S24-005 · 005 Art-directed / Distinctive · REBUILD · USER_REQUIRED

- **Concept:** Project organised as an architectural issue set — cover sheet, drawing set, decisions and a register.
- **Preserve:** the 'four moves' decision content as narrative.
- **Remove:** the issue-set structure; the cover sheet; the sheet references and NTS notation; the register; the drawing-sheet navigation.
- **Replace with:** **replacement structural territory — an image-first project narrative**: a full-bleed opening image, then the four moves as full-width media passages with display-scale statements between them, closing on a quiet metadata line and a related project.
- **Media:** six drawing areas → six photographic fields, the first full-bleed and the rest at varying widths.
- **Copy:** HIGH → MEDIUM; from 316 words to roughly 170.
- **Responsive:** full-width passages stack and keep their proportions; statements scale without clipping.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with the rebuilt `003`. `003` is a module grid with a gallery; `005` is a linear full-bleed narrative with no grid.

### S25 — Article / Insight Detail

**Section rule:** a real article may legitimately carry more copy and is not penalised for body
text. But the global header and navigation must be removed from all five — the references these
were built from included site chrome, and the section-shell rule takes precedence. Judge editorial
rhythm, media structure and metadata density, not word count alone.

#### ARC-S25-001 · 001 Universal / Safe · MINOR_FIX · USER_REQUIRED

- **Concept:** Journal article — back chip, title beside a ruled meta column, lead image, author rail, related block.
- **Preserve:** the article anatomy; the related-reading block; all four image areas.
- **Remove:** the global site header and primary navigation; roughly a fifth of the body copy.
- **Replace with:** —
- **Media:** four areas; unchanged. The lead image keeps its scale as the article's opening field.
- **Copy:** EXCESSIVE → HIGH; from 379 words to roughly 300 — legitimate for an article once the chrome is gone.
- **Responsive:** unchanged; measure holds, meta column releases to flow.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S25-002 · 002 Premium / Editorial · MINOR_FIX · USER_REQUIRED

- **Concept:** Magazine sheet on a grey ground — publication bar, film area, large centred display headline, interview.
- **Preserve:** the centred display headline — the best in S25; the sheet-on-ground device; the film area.
- **Remove:** the publication bar acting as a site header.
- **Replace with:** a short publication line beneath the headline if the context is needed at all.
- **Media:** one film area; add one in-body field so a 400-word article is not carried by a single image.
- **Copy:** EXCESSIVE → HIGH; from 398 words to roughly 320.
- **Responsive:** unchanged; the display headline scales without clipping at 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S25-003 · 003 Structured / Visual Modular · REWORK · USER_REQUIRED

- **Concept:** Blog article between two sidebars with pull quote, share row, author box, related posts and a comment form — nine stacked regions, 461 words, a masthead bar.
- **Preserve:** the comment form and author box as content models; the centre column measure, which holds well.
- **Remove:** the masthead bar; one of the two sidebars; roughly three of the nine regions.
- **Replace with:** a single-sidebar article with the surviving regions given more space and media between them — the structure remains the modular member of the set, but modules are visual rather than merely numerous.
- **Media:** five areas; redistribute so at least two sit inside the body rather than in the rails.
- **Copy:** EXCESSIVE → HIGH; from 461 words to roughly 330.
- **Responsive:** sidebar releases beneath the article at 1024; comment form fields stay full width at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S25-004 · 004 Conversion-led · MINOR_FIX · USER_REQUIRED

- **Concept:** Article with a pinned meta rail, uppercase headline, dark in-body contact card and an oversized related band.
- **Preserve:** the oversized related band; the in-body contact card; the pinned rail behaviour.
- **Remove:** the global header, its primary navigation and the standing CTA in that bar; roughly a fifth of the copy.
- **Replace with:** —
- **Media:** six areas; unchanged — the strongest media count in S25.
- **Copy:** EXCESSIVE → HIGH; from 420 words to roughly 330.
- **Responsive:** rail releases to flow before it competes with the body.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S25-005 · 005 Art-directed / Distinctive · MINOR_FIX · USER_REQUIRED

- **Concept:** Cream feature with a mixed-scale serif title, unequal plate pair and a credits register beside the body.
- **Preserve:** the mixed-scale display title; the unequal plate pair — the best media rhythm in the extended sections.
- **Remove:** the category navigation acting as a site header; the credits register as a ruled block.
- **Replace with:** credits as a short byline line beneath the title.
- **Media:** four plate areas; unchanged.
- **Copy:** EXCESSIVE → HIGH; from 373 words to roughly 320.
- **Responsive:** the plate pair keeps its inequality when stacked.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

### S26 — Architect / Designer Profile

Section rule: portrait-led. Not a curriculum sheet, bid CV, verification form or capability matrix.
The reserved-field device for unverifiable credentials is a claims-policy content type and survives
any visual change.

#### ARC-S26-001 · 001 Universal / Safe · MINOR_FIX · AUDIT_ADDED

- **Concept:** Profile with portrait paired to identity, post description, attachments, reserved background and a contact rail.
- **Preserve:** the portrait/identity pairing rule, which holds structurally at every width; the reserved-field content type.
- **Remove:** roughly a third of the copy; the reserved-fields register presented as a ruled block.
- **Replace with:** the reserved fields as a short quiet list beneath the biography.
- **Media:** one portrait area → one portrait plus two selected-project areas, so a 300-word page is not carried by a single image.
- **Copy:** EXCESSIVE → HIGH; from 373 words to roughly 260.
- **Responsive:** portrait and identity stay paired; contact rail releases to flow.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S26-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** Editorial profile — tall portrait plate beside a quiet identity column and a written statement.
- **Preserve:** the tall portrait plate relationship.
- **Remove / Replace with:** — · —
- **Media:** one portrait plate; unchanged.
- **Copy:** HIGH — 300 words; proportionate for a profile page. Optional trim.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference for S26.

#### ARC-S26-003 · 003 Structured / Visual Modular · REWORK · AUDIT_ADDED

- **Concept:** Personnel record — identity band, open field register, stage-involvement table and reserved-fields block.
- **Preserve:** the involvement-by-stage content expressed briefly; the openness (nothing hidden behind controls); the reserved-field device.
- **Remove:** the field register; the stage-involvement table; the record framing.
- **Replace with:** a portrait-led modular profile — portrait and identity at the head, then four modules (focus, disciplines, selected projects, related services) each with a short line and, where relevant, a small media area.
- **Media:** one portrait → one portrait plus three project areas inside the modules.
- **Copy:** EXCESSIVE → MEDIUM; from 383 words to roughly 200.
- **Responsive:** modules 2 × 2 → single column; portrait and identity never separate.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Same family as `ARC-S08-003`; correcting them together keeps the section and the roster consistent.

#### ARC-S26-004 · 004 Conversion-led · MINOR_FIX · AUDIT_ADDED

- **Concept:** Profile ordered around asking for this person, with help list, alternatives and introduction steps.
- **Preserve:** the 'ask for someone else' routing — honest and distinctive; the single clear route.
- **Remove:** roughly a third of the copy — 450 words is the highest in S26.
- **Replace with:** —
- **Media:** one portrait area → one portrait plus one project area.
- **Copy:** EXCESSIVE → HIGH; from 450 words to roughly 280.
- **Responsive:** unchanged.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S26-005 · 005 Art-directed / Distinctive · REBUILD · AUDIT_ADDED

- **Concept:** Bid curriculum sheet — issue line, coverage matrix of project type against stage, verification block.
- **Preserve:** the coverage content as short prose; the verification idea as a reserved field rather than a block.
- **Remove:** the CV sheet; the coverage matrix; the issue line; the verification apparatus.
- **Replace with:** **replacement structural territory — an art-directed profile**: an oversized portrait field filling much of the opening, the name set across it at display scale, then a short statement and a strip of the person's projects.
- **Media:** one portrait → one oversized portrait field plus a three-image project strip.
- **Copy:** EXCESSIVE → LOW/MEDIUM; from 353 words to roughly 180.
- **Responsive:** the oversized portrait re-proportions rather than cropping to a band; the project strip becomes a stack at 480.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** Must not converge with `002`, which is already a tall portrait plate beside a column. Here the portrait is the ground and the name crosses it.

### S27 — Studio / Location Detail

Section rule: place-led. Not arrival diagrams, coordinate sheets, technical registers or
letter-keyed plans. The reserved map area is a policy device and survives; address and contact
detail stay first-class at small widths.

#### ARC-S27-001 · 001 Universal / Safe · MINOR_FIX · AUDIT_ADDED

- **Concept:** Location page with address, contact and hours above the image, then what happens here and getting here.
- **Preserve:** the address-before-media ordering, which is correct for the role; the reserved map slot.
- **Remove:** roughly a third of the copy.
- **Replace with:** —
- **Media:** one image plus one map area → add two further place images so the page is carried by photography.
- **Copy:** EXCESSIVE → HIGH; from 351 words to roughly 240.
- **Responsive:** unchanged; address remains first at small widths.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S27-002 · 002 Premium / Editorial · KEEP · —

- **Concept:** The place described as a building — compact address line, lead plate, prose and a plate pair.
- **Preserve:** the compact address line above the lead plate; the three plates.
- **Remove / Replace with:** — · —
- **Media:** three plates plus map; unchanged — the best media presence in S27.
- **Copy:** HIGH — 331 words; optional trim.
- **Responsive:** unchanged.
- **Batch:** NONE
- **Notes:** Positive reference for S27.

#### ARC-S27-003 · 003 Structured / Visual Modular · REWORK · AUDIT_ADDED

- **Concept:** Location details sheet — identification band and three tables (contact, hours by day, access and arrival); no photography.
- **Preserve:** the reserved-field discipline for addresses and durations; the completeness of the practical information.
- **Remove:** all three tables; the identification band.
- **Replace with:** the same practical information as visual modules — a contact module, an opening module and an access module, each with a short list, arranged around a lead place image.
- **Media:** one map area → one lead place image plus two supporting images plus the map.
- **Copy:** EXCESSIVE → MEDIUM; from 448 words to roughly 240.
- **Responsive:** modules 3 → 1; nothing becomes a horizontally scrolling table; contact details stay first-class at 390 and 320.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S27-004 · 004 Conversion-led · MINOR_FIX · AUDIT_ADDED

- **Concept:** Visit-ordered location page with address inside the decision header and arrangement steps.
- **Preserve:** the visit-first ordering; the honesty about promising no times.
- **Remove:** roughly a third of the copy — 466 words is the highest in S27.
- **Replace with:** —
- **Media:** one map area → add two place images; this study currently has no photographic media.
- **Copy:** EXCESSIVE → HIGH; from 466 words to roughly 280.
- **Responsive:** unchanged.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK

#### ARC-S27-005 · 005 Art-directed / Distinctive · REWORK · AUDIT_ADDED

- **Concept:** Arrival key — lettered approach steps keyed to a reserved plan area, with a floor key inside.
- **Preserve:** the arrival-sequence content, which is genuinely useful; the principle that the sequence survives an empty plan because the steps are text.
- **Remove:** the keyed-plan register; the lettering system; the floor key; the plan area as the primary device.
- **Replace with:** the arrival sequence as a photographic sequence — three or four place images taken along the approach, each with one short line, with the reserved map kept as a quiet closing element.
- **Media:** one plan plus one map → three place images plus the map; the plan area is retired.
- **Copy:** EXCESSIVE → MEDIUM; from 404 words to roughly 200.
- **Responsive:** the image sequence stacks; each image keeps a proportion that reads when empty.
- **Batch:** UPDATE_REQUIRED_AFTER_HTML_REWORK
- **Notes:** The keyed-plan device is the same family the user excluded from S22; retiring it here keeps the two roles consistent.

## Post-Rework Diversity Review

The question this answers: after the planned corrections, do the five studies in each section still
differ **structurally**, or has the correction produced a new monotony? The failure mode to avoid is
every corrected study becoming image-left / text-right, a three-card grid, or an oversized headline
over one image.

**PASS — 6 sections.** S02 (unchanged), S03, S04, S13, S16, S25.

**RISK — 21 sections.** Each risk below names the variants that could collapse into each other and
the device that must keep them apart. These are constraints on Phase 4, not reasons to change a
classification.

| Section | Risk | Variants at risk | Separating device required |
| --- | --- | --- | --- |
| S01 | RISK | 003 ↔ 005 | Both lose a documentary block and gain media. 003 must stay a *modular* hero (small media modules under a headline); 005 must stay a single large plate with off-axis type. |
| S05 | RISK | 003 ↔ 005 ↔ 002 | Three type-led philosophy compositions. 002 keeps one wordmark and one paragraph; 003 becomes a four-module grid with per-position media; 005 becomes mixed-scale principles over a wide band image. |
| S06 | RISK | 005 ↔ 003 (implemented) ↔ 002 | 002 is numerals with one image per stage; 003 is a lead field plus an equal module grid; 005 must be a continuous scale-varying progression, not a third module row. |
| S07 | RISK | 005 ↔ 004 | Both are large-type studio statements. 005 must give at least half its composition to an enlarged plate; 004 stays type-only. |
| S08 | RISK | 003 ↔ 005 ↔ 007 ↔ 006 | Four portrait-led outcomes. 003 = equal module grid; 005 = unequal off-grid scale; 007 = grid that reads with empty slots and optional expansion; 006 = featured plate plus thumbnail strip. |
| S09 | RISK | 001 ↔ 003 ↔ 005 ↔ 002 | All four become visual recognition. 001 = two columns of cards; 003 = year-banded module grid; 005 = two or three oversized fields; 002 = single tear sheet beside a list. |
| S10 | RISK | 003 ↔ 005 | Both gain their first media. 003 = four modules with disclosure; 005 = large fields with oversized capability names. |
| S11 | RISK | 003 ↔ 005 ↔ 001 ↔ 002 | All material-led. 001 = six samples with two lines each; 002 = loose board with questions; 003 = regular module grid; 005 = full-bleed close-range texture sequence. |
| S12 | RISK | 005 ↔ 001 | Both quote-over-image. 005 must be display-scale quotation with the image as ground and three quotations; 001 stays a featured quote plus four cards. |
| S14 | RISK | 003 ↔ 005 | Both land on nine images. 003 = one ratio, regular 3 × 3; 005 = nine images at deliberately unequal scale in far-to-close order. |
| S15 | RISK | 003 ↔ 001 ↔ 005 | 001 = six market cards with descriptions and links; 003 = comparison modules carrying discipline combinations; 005 = four full-bleed fields with oversized market names. |
| S17 | RISK | 003 ↔ 001 ↔ 005 ↔ 002 | 001 = three cards with a details link; 003 = cards carrying the full practical set; 002 = principal-plus-two hierarchy; 005 = three unequal city fields. |
| S18 | RISK | 002 ↔ 003 ↔ 005 ↔ 001 | All become large figures. 001 = four equal figures; 002 = one anchor figure against an image; 003 = six-module grid broken by two image fields; 005 = four figures at very large scale with a full-bleed field. |
| S19 | RISK | 005 ↔ 002 | Both short forms. 005 is only distinct because of its large contextual image field and display invitation; without media it duplicates 002. |
| S20 | RISK | 005 ↔ 002 | Both agenda-based invitations. 005 must be full-bleed and image-led; 002 stays compact and type-only. |
| S21 | RISK | all five | Five conventional subpage heroes. Enforced separation: 001 typography-only, 002 contained image strip, 003 split with an image module, 004 CTA-aware, 005 full-bleed background. |
| S22 | RISK | all five | One component, five variants. Enforced separation: 001 plain trail, 002 uppercase with an inline return, 003 contained tinted bar, 004 trail plus one named continuation, 005 type-distinctive on a contrasting ground. |
| S23 | RISK | all five | All five follow the same clarified content capacity. Enforced separation: 001 plain sectioned page, 002 editorial measure with media passages, 003 module grid with accordion FAQ, 004 decision cards with a form, 005 full-bleed story. |
| S24 | RISK | 003 ↔ 005 ↔ 001/002/004 | 003 = module grid plus a controlled gallery; 005 = linear full-bleed narrative with no grid; the three KEEP studies already differ by chapter structure and conversion path. |
| S26 | RISK | 003 ↔ 005 ↔ 002 | 002 = tall plate beside a column; 003 = portrait plus four information modules; 005 = oversized portrait as ground with the name across it. |
| S27 | RISK | 003 ↔ 005 ↔ 002 ↔ 001 | 001 = address-first with supporting images; 002 = lead plate plus plate pair; 003 = practical modules around a lead image; 005 = photographic arrival sequence. |

**Sector-level risk.** 20 of the 28 REBUILDs sit in the `003` and `005` slots. If Phase 4 answers
every one of them with "large media field plus oversized type", the catalog will have traded one
monotony for another. The per-section separating devices above are the control; each Phase 4 batch
should be checked against its section's row before the section is closed.

## Implementation Batches

69 work items. Sections are grouped so that foundational roles are settled before the pages that sit
on top of them.

### Batch 1 — Shell and foundational roles (14 items)

S01, S21, S22. Settles the section-shell rule and the two roles whose definition was misread.

| Status | Studies |
| --- | --- |
| MINOR_FIX | `ARC-S01-001`, `ARC-S01-002`, `ARC-S01-004`, `ARC-S22-002` |
| REWORK | `ARC-S01-003`, `ARC-S01-005`, `ARC-S21-001`, `ARC-S21-002`, `ARC-S21-004` |
| REBUILD | `ARC-S21-003`, `ARC-S21-005`, `ARC-S22-003`, `ARC-S22-004`, `ARC-S22-005` |
| BUG_FIX | — |

### Batch 2 — Detail page architecture (21 items)

S23, S24, S25, S26, S27. The densest work in the sector: 414 average visible words and the header
contamination in S25.

| Status | Studies |
| --- | --- |
| MINOR_FIX | `ARC-S24-001`, `ARC-S25-001`, `ARC-S25-002`, `ARC-S25-004`, `ARC-S25-005`, `ARC-S26-001`, `ARC-S26-004`, `ARC-S27-001`, `ARC-S27-004` |
| REWORK | `ARC-S23-001`, `ARC-S23-002`, `ARC-S23-004`, `ARC-S25-003`, `ARC-S26-003`, `ARC-S27-003`, `ARC-S27-005` |
| REBUILD | `ARC-S23-003`, `ARC-S23-005`, `ARC-S24-003`, `ARC-S24-005`, `ARC-S26-005` |
| BUG_FIX | — |

### Batch 3 — Expertise and process (13 items)

S03, S04, S05, S06, S10, S11, S15.

| Status | Studies |
| --- | --- |
| MINOR_FIX | — |
| REWORK | `ARC-S03-003`, `ARC-S04-003`, `ARC-S04-005`, `ARC-S05-003`, `ARC-S10-003` |
| REBUILD | `ARC-S03-005`, `ARC-S05-005`, `ARC-S06-005`, `ARC-S10-005`, `ARC-S11-003`, `ARC-S11-005`, `ARC-S15-003`, `ARC-S15-005` |
| BUG_FIX | — |

### Batch 4 — People, trust and studio (15 items)

S07, S08, S09, S12, S16, S17, S18. Contains the sector's only confirmed responsive failure.

| Status | Studies |
| --- | --- |
| MINOR_FIX | `ARC-S08-009` |
| REWORK | `ARC-S07-005`, `ARC-S08-003`, `ARC-S09-001`, `ARC-S16-003`, `ARC-S17-003`, `ARC-S18-002` |
| REBUILD | `ARC-S08-005`, `ARC-S08-007`, `ARC-S09-003`, `ARC-S09-005`, `ARC-S12-005`, `ARC-S17-005`, `ARC-S18-003`, `ARC-S18-005` |
| BUG_FIX | — |

### Batch 5 — Portfolio and conversion (6 items)

S13, S14, S19, S20.

| Status | Studies |
| --- | --- |
| MINOR_FIX | — |
| REWORK | `ARC-S13-003`, `ARC-S13-005`, `ARC-S14-003`, `ARC-S14-005` |
| REBUILD | `ARC-S19-005`, `ARC-S20-005` |
| BUG_FIX | — |

**Outside the batches.** S02 — five KEEP by user decision, not scheduled. `ARC-S06-003` — already
implemented and accepted.

## BATCH-V1 Update Requirements

Batch documents are **not** touched in Phase 3. After each study's HTML work lands, its section
`BATCH-V1.md` must be updated to match: the planned-studies row (direction name and status), the
study record (structural intent, layout model, density, media mode, responsive strategy, content
ceiling), the media-slot table where slots are added or removed, and the QA block.

| Section | Batch update | Reason |
| --- | --- | --- |
| S01, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27 | UPDATE_REQUIRED_AFTER_HTML_REWORK | 26 sections carry at least one changed study. |
| S02 | NONE | No study changes. |

Media-slot tables need particular attention in **S06-005, S09-001/003/005, S10-003/005, S11-003,
S15-003/005, S16-003, S17-003/005, S18-002/003, S21-003/005, S23-003/004 and S27-003/004**, where
studies gain their first reserved media areas. `ARC-S06-003`'s batch record is already current and
must not be rewritten.

## Responsive Verification Queue

Verification only — nothing in this queue is repaired in Phase 3, and a study listed here keeps the
status recorded above unless verification finds a defect, in which case it becomes `BUG_FIX`.

### Confirmed

| Study | Finding |
| --- | --- |
| `ARC-S08-007` | Expanding filmstrip whose unselected panels are fixed 42–96px slivers. With reserved media areas empty — the normal state — those slivers render as blank columns at every width, and the strip overflows rather than reflowing. Conceptual as well as responsive, which is why it is REBUILD rather than BUG_FIX. |

### Possible — user-named

| Study | What to verify |
| --- | --- |
| `ARC-S08-008` | Cards bleed past the viewport edge by design; confirm the horizontal scroll affordance and keyboard route at 768 / 430 / 390 / 320. |
| `ARC-S08-009` | Lead card plus buttoned rail; confirm rail behaviour at tablet width. |

### Possible — audit-added

Horizontal, sticky or stepped mechanisms that the contact sheet cannot settle on its own. No
clipping or overflow was observed in the regenerated sheet for any of them; these are confirmations,
not defects.

| Study | What to verify |
| --- | --- |
| `ARC-S03-004` | Horizontal service scroll rail — affordance and keyboard controls at narrow widths. |
| `ARC-S04-005` | Tabbed typology switching with prev/next controls — every typology reachable without script at 480 and below. |
| `ARC-S12-002` | Stepper controls — 44px targets and live-region announcement at 390 and 320. |
| `ARC-S13-002` | Held/sticky plate — confirm it releases to normal flow at 768 rather than pinning over the text. |
| `ARC-S24-002` | Chapter jump bar — confirm it wraps rather than becoming a clipped horizontal strip. |

All 141 studies declare the 1280 / 1024 / 768 / 480 / 360 breakpoint ladder, and all 146 rendered
at their real measured heights in the regenerated contact sheet with no clipping.

## Deferred Work

**S28 — `S28-blog-list-pages/`**

- Status: **DEFERRED · PROVISIONAL · OUTSIDE CURRENT CATALOG**
- Five studies (`ARC-BLOG-LIST-001`–`005`), excluded from every count in this plan.
- Not modified, not reconciled, not renumbered. Its taxonomy, section number and study IDs are a
  governance question to be settled separately.
- Recorded observations from Phase 0, carried forward without action: all five carry global site
  headers and footers, one carries invented personal names, and the IDs do not follow the
  `ARC-S<NN>-<VVV>` rule.

**Also deferred**

- `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` roll-up counters still read `NOT_STARTED`
  for Architecture — a workspace-level pass, not part of this sector's rework.
- Section READMEs and batch documents in the other 19 sectors still carry the previous direction
  names in their planned-study tables; the Phase 1 transitional note governs them until reconciled.

## Phase 4 Entry Gate

| Requirement | State |
| --- | --- |
| Every S01–S27 authored study has a final status | PASS — 141/141 |
| Every REWORK has Preserve / Remove / Replace | PASS — 27/27 |
| Every REBUILD has a replacement structural territory | PASS — 28/28 |
| Every user-required correction accounted for | PASS — 48 pending + 1 implemented |
| Audit-added changes separated | PASS — 21, listed separately |
| Diversity review complete | PASS — 27 sections reviewed, 6 PASS / 21 RISK with named separating devices |
| Execution batches complete | PASS — 5 batches, 69 items, reconciling to the classification totals |
| Responsive queue exists | PASS — 1 confirmed, 7 to verify |
| S28 excluded | PASS — deferred, outside all totals |
| No unresolved S21–S27 role ambiguity | PASS — S21, S22 and S23 role clarifications applied per study; S24–S27 judged against the Phase 2 contracts |

**GATE: PASS.**

Phase 4 may begin with Batch 1. Nothing in this document authorises a change to any HTML, batch
record, standard, section README or review artifact.
