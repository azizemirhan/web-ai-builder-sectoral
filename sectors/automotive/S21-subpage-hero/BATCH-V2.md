# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A subpage hero is not a page — it is the **top of every page that is not the home page**. So the study is a **template**, and everything page-specific is bracketed: the page area, the page title, who the page is for and where it does not apply, and the image caption.

The only fixed copy is the one line a subpage hero can honestly say before it knows what page it is on: *Read what this page covers, and who it is for, before you go further.*

This is the one section where the **scope line** is part of the hero rather than the body. In this sector the top of a page is where the limit belongs.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S21-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the title beside its context | the bay lines behind the head | 1 reserved · 4 | 38 |
| `AUTO-S21-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the title above a panorama | the plate edge at the head | 1 reserved · 4 | 38 |
| `AUTO-S21-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the head as a two-cell plate | bordered plate, 1px line shared | 1 reserved · 4 | 39 |
| `AUTO-S21-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — the title alone, measured | the torque mark under the title | none · 3 | 31 |
| `AUTO-S21-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the head framed | the ramp frame | 1 reserved · 4 | 39 |

The five run **31–39 words**, just under the contract's hero band of 40–90. That is the consequence of the role: with every page-specific value reserved, the only countable copy is one fixed sentence. Padding the template with filler to reach forty would put invented copy into a file whose whole purpose is to hold the slot open.

**004 carries three placeholders against four in the others** because it is the one variant with no media, and therefore no image caption. It is also the `C`, and it records why: with every value reserved there is nothing a photograph could be of.

## What was designed

The register's five structure devices applied to the smallest possible composition, so each is legible on its own. **The emphasis device works even on a bracket**: the title's second half is set in serif italic in the accent — *[Approved page title]* — and in 004 it is measured by the torque mark instead, so the device appears once per composition either way.

The scope line always sits **below a rule** — hairline in 001, 002, 003 and 005, the 3px accent lead rule in 004 — because the limit is the last thing the hero says.

`<h1>` is correct here, and is one of the seven sections in this sector that carries one.

## Verification

- `autocheck.ps1 -Sec S21 -Fields 'Workshop|Page area|Approved page title|Read what this page covers|Who this page is for'` — ALL CHECKS PASS; parity 25/25. `<h1>` present and single (hero role); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no manufacturer, model, badge, plate, price or figure; no digit in visible copy outside the field ratio labels; four placeholders per study, three in 004.
- Rendered and read at 1440.
