# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A subpage hero is not a page — it is the **top of every page that is not the home page**, and it has to work for the treatment page, the article, the profile and the department alike. So the study is a **template**, and everything that would be page-specific is bracketed and reserved: the page area, the page title, who the page is for and where it does not apply, and the image caption.

The only fixed copy is the one line a subpage hero can honestly say before it knows what page it is on: *Read what this page covers, and who it is for, before you go further.* Everything else is a slot. Inventing a title here would invent a page.

This is the one section where the **scope line** — *who this page is for, and where it does not apply* — is part of the hero rather than the body. In this sector the top of a page is where the limit belongs, not the bottom.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S21-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the page title beside its context | column rules behind the head | 1 reserved · 4 | 38 |
| `HC-S21-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the title above a panorama | open bracket at the head | 1 reserved · 4 | 39 |
| `HC-S21-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the head as a two-cell plate | bordered two-cell plate, 1px line shared | 1 reserved · 4 | 38 |
| `HC-S21-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the title alone, measured | measure rule under the title's second half | none · 3 | 31 |
| `HC-S21-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the head framed | corner frame at the head | 1 reserved · 4 | 38 |

The five run **31–39 words**, just under the contract's hero band of 40–90. That is deliberate and is the consequence of the role: with every page-specific value reserved, the only countable copy is one fixed sentence. The band applies to a hero carrying a page's own words; there are none here to carry, and padding the template with filler to reach forty would put invented copy into a file whose whole purpose is to hold the slot open.

**004 carries three placeholders against four in the others** because it is the one variant with no media, and therefore no image caption. It is the conversion-led direction, where the title and the scope line are the whole composition.

## What was designed

The register's five structure devices applied to the smallest possible composition, so that each one is legible on its own: the 001 column rules standing behind a two-column head; the 002 open bracket with the title left and the lead and scope line set at the baseline opposite, above a 21:9 panorama; the 003 plate as two cells sharing one 1px line, copy on the band tone; the 004 measure rule under the second half of the title, which is the only ink the variant adds; the 005 corner frame holding the whole head.

The accent falls on the **second half of the title**, so a page called two things in one line reads as one emphasis and not two. The scope line always sits **below a rule** — hairline in 001, 002, 003 and 005, the 3px accent lead rule in 004 — because the limit is the last thing the hero says.

**No `<h1>` anywhere else in this sector's body sections**; here it is correct, because a subpage hero is the top of a page. No clinician name, figure, price, hour or claim — there is nothing in the file to attach one to. No SVG, no icon, no badge, no global header or navigation.

## Verification

- `hccheck.ps1 -Sec S21 -Fields 'Clinic|Page area|Approved page title|Read what this page covers|Who this page is for'` — ALL CHECKS PASS; parity 25/25. `<h1>` present and single (hero role); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; four placeholders per study (three in 004), declared in the `placeholder-data` meta.
- Correction during the pass: `.scope` in 001, 004 and 005 carried both a `border-top` and a `max-width`, which the contract forbids on one element — the rule belongs to the section and the measure to the text. The measure is now `padding-right` and the rule runs to the column edge.
- Rendered and read at 1440.
