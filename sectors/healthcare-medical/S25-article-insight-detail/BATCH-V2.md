# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S25` — Article / Patient Resource Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The brief rules out *any advice a regulated sector may not publish without qualification*, and the sector contract rules out medical advice outright. That leaves one honest kind of patient resource: an article about **the appointment**, not about the condition.

> **How to describe a change you can see** — A short guide to the first thing you will be asked, written so you can answer it.

Four headings, each a real `<h2>`, because the brief asks for a heading structure:

- **Start with when** — the most useful thing you can say is when it started, and what it looked like *then*.
- **Say what changed, not what it is** — *bigger, darker, raised, sore, itchy, bleeding, spreading.* Plain words. Nobody expects you to know the right one.
- **Say what you did** — anything you put on it, took, or stopped.
- **Say what worries you** — if you are frightened of something in particular, say the word. It will not make it more likely, and it will change what gets ruled out.

Then the sentence that makes it publishable: **What this is not.** *It does not say what a change is, what to do about it, or whether to worry. It says how to be understood by somebody who can answer that.*

**The attribution is real structure with reserved values.** A fabricated author, publication or date is forbidden, so the page carries the fields a reviewed patient resource must have — *Author* and *Last checked* — with both values bracketed and the author given by role rather than by name. Leaving the apparatus out would have been easier and less honest: the structure records that the page is supposed to be attributed and reviewed.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S25-001` | Universal / Safe | 001 Linen & Sage | C | 1 — the article, with its apparatus beside it | column rules behind the head | none · 2 | 189 |
| `HC-S25-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the editorial reading, offset column | open bracket at the head | 1 reserved · 3 | 196 |
| `HC-S25-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the article as one plate, with contents | bordered plate, 1px lines shared | 1 reserved · 3 | 228 |
| `HC-S25-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — *see*, measured | measure rule under the title's last word | none · 2 | 189 |
| `HC-S25-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the article framed, the body on the band tone | corner frame at the head | 1 reserved · 3 | 197 |

All five sit inside the contract's detail band of 170–230.

**Two studies are `C`, and each records why.** 001: a visitor who arrived to read something is not helped by a photograph above it. 004: this article exists to get somebody ready to speak, and a picture would delay that.

**003 is the only variant carrying the in-page contents** the brief allows — four anchors to the article's own headings, in the band-tone cell beside the reading column. They are the heading text verbatim, not abbreviations, because a contents list that does not match its headings is a small lie.

## What was designed

The article is a **reading column with its apparatus kept out of it**. What the article is not, the attribution and the adjacent reading never interrupt the four sections: they sit in a narrow column opposite (001, 004), below the lead rule (002), in their own plate row (003), or after the limit (005). The sections themselves are hairline-separated, the heading in ink and the line beneath it in the muted tone, at a measure of 42–46rem in the variants that set one.

The accent falls on the **last word of the title** — *see* — which is the word the whole article is about; 004 measures it with the structure-layer rule instead of colouring it.

Media, where it exists, is one of the three honest subjects and is never a person standing in for a patient: the two chairs in the consulting room as 002's 21:9 lead image, the consulting room at 4:3 in 003's head row, the plan being written at 4:3 beside 005's attribution — the article ending where the writing starts.

No SVG, no icon, no badge, no share row, no author portrait, no reading-time figure, no global header or footer.

## Verification

- `hccheck.ps1 -Sec S25 -Fields 'Patient resource|Start with when|Say what changed|Say what you did|Say what worries you|What this is not|Written and checked by|Read next'` — ALL CHECKS PASS; parity 40/40. `<h1>` present and single (detail page), with four `<h2>` section headings beneath it; no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no claim term; no digit in visible copy outside the field ratio labels; two placeholders per study, three where there is a caption. All links point at same-variant S23, S16 and S05 studies and resolve on disk; 003's four anchors resolve to its own heading ids.
- Rendered and read at 1440. Corrections: 004's attribution block carried both a border and a `max-width`, which the contract forbids on one element, and the measure was moved to `padding-right`; 003 first ran to 236 words because the contents duplicate the headings, and two headings were tightened — *Say what you did about it* to *Say what you did*, *Say what you are worried about* to *Say what worries you* — which brought every study into band and reads better; 005's attribution row was bottom-aligned to a taller field and was set to start with a narrower field column.
