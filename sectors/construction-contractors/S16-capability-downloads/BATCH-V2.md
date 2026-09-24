# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S16` — Capability Downloads · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the figures are in the documents and none is on the page; what is in it / who it is for / when it stops being true; the six documents; two gated and the reason named; the signature rule; no brochure, certificate image, undated document or download count; issue date, revision, renewal, signatory, file and contact reserved; no link to any file — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S16-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — gate cells, document sheets | setting-out grid behind the head | Three bordered gate-policy cells with padlock icons (open / closed / struck envelope); six bordered document sheets sharing one hairline system — title column with a document icon and gate chip, three cells for contents / audience / expiry with the expiry on the band tone behind a tape edge, and a record column of reserved slots; refusal note with tags | 18 slots | 890 |
| `CON-S16-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — ruled chapters, margin ledger | levelling circle behind the head | Two-column essay under the tape rule; six ruled chapters with the document icon at counter scale, gate chip and WRITTEN FOR in the margin, the title and contents in the centre with STOPS BEING TRUE as a tracked headline, and a bordered right-margin ledger of reserved slots; two bordered closing cells, the gate reason tape-topped | 18 slots | 986 |
| `CON-S16-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 + 4 — rule bands, bordered cells | dimension line with ticks behind the head | Three tinted bands sorted by what makes each document stop being true, each with a rule icon (calendar / cycle / site) and the rule at headline size, and bordered document cells at two, three and one across — icon, gate chip, contents, audience, a tape-edged STOPS BEING TRUE line and a reserved slot row; bordered three-cell foot | 15 slots | 876 |
| `CON-S16-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — question rows with one action each | chevron run behind the closing band | Display with tape underline; seven bordered rows — IF YOU ARE TRYING TO with the question at headline size, then the answering document as a cell with icon, gate chip, contents, reserved slots and one bordered action; the two no-document rows tape-topped on the band tone with inverted actions routing to the walk or the bid page; tape-topped closing band; ruled foot. All anchors in-page | 10 slots | 627 |
| `CON-S16-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — hierarchy inverted | cut-earth hatching down the left margin | Six ruled entries in which the expiry rule is set at display size and the title is a tracked caption beside the document icon and gate chip, with the audience in a hairline margin column; tape-topped gate band; HELD AGAINST EVERY DOCUMENT as a bordered record of reserved fields at counter scale; ruled foot | 5 slots | 766 |

## What changed from V1

Each document carries a stroke icon (document set, matrix, shield, signature, sequence, exchange arrows), a bordered gate chip (open padlock / closed padlock inverted) and the expiry as the tape-marked element — band-tone cell, tracked headline, tape-edged line, or display headline by variant; the reserved record is a bordered slot ledger; the refusals are muted tags beside a struck document. `004`'s actions are the register's bordered rectangles with a leading icon, in-page only. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S16 -Fields 'Issue date|File format and size|Revision reference'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no issue date, revision, renewal date, signatory, file size, contact, figure or count — every one a reserved slot with a visually-hidden label; no anchor to any file.
- Rendered and read at 1440. No corrections needed.
