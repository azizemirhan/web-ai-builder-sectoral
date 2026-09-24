# FINANCE THEME CONTRACT

Sector: Finance, Accounting & Insurance. Prefix: FIN. Established with S01 on 2026-09-15.

## Design Intent

Modern, visually engaging compositions with generous space, confident system-sans
headings and purposeful human imagery. No technical or classical styling: avoid
financial dashboards, trading charts, fake statements, spreadsheets, seals, columns,
coins, performance gauges or faux regulatory documents. Differentiate layouts by
composition rather than copy volume or palette alone.

## Five Fixed Themes

Variant N retains its theme across subsequent sections for coherent page assembly.

| Variant | Theme | Ground | Ink | Accent | Media ground | Soft text | Radius |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Ivory & Olive | #faf8ef | #293224 | #52652c | #e3e6cc | #606653 | 28px |
| 002 | Rosewood | #fcf1ee | #442e35 | #a3425c | #efd6d9 | #75616b | 12px |
| 003 | Lagoon | #edf8f5 | #183b36 | #126957 | #cce5dc | #506d66 | 24px |
| 004 | Iris | #f5f2ff | #30294e | #6650b8 | #e0d9f4 | #696080 | 32px |
| 005 | Ink & Apricot | #1b2330 | #fff3e5 | #ffd1a1 | #334253 | #bfc9d4 | 32px |

001-004 accent controls may use white or paper text; 005 uses dark text on apricot.
Iris permits a paper disclosure on an accent field. Focus must contrast with its
actual surrounding surface. Use system sans, heading weight 500-650, max-width
1400px and desktop 60px, tablet 36px, phone 22px insets. No remote fonts.

## Facts and Media

Do not invent firms, people, client relationships, qualifications, registrations,
regulatory status, testimonials, fees, coverage, eligibility or service availability.
Do not fabricate returns, savings, tax outcomes, performance comparisons or guarantees.
Actual financial guidance and jurisdiction-specific claims require supplied evidence
and appropriate editorial review; structural samples use neutral invitation copy.
S24 is limited to anonymised engagement context without performance or outcome claims.

Reserve media under the repository policy. Photographs need participant consent,
licensing, provenance and final descriptive alt text before publication. A generic
conversation photo must not imply a real client, employee or endorsed relationship.
Every reserved slot needs a visible caption, accessible label and allocated space.

## Structure and Interaction

Directions: Universal / Safe; Premium / Editorial; Structured / Visual Modular;
Conversion-led; Art-directed / Distinctive. Shapes: A item grid, B one to three
anchored media areas, C type and colour. Avoid more than two consecutive A sections.
Read the previous two same-variant sections when available.

Copy targets: hero 40-90 words; ordinary sections 90-170; structured and detail roles
150-230 as appropriate; absolute ceiling 250. Complete required content takes priority
above padding. Standalone HTML with metadata, scoped CSS, border-box descendants,
responsive reflow, visible focus, 44px targets and reduced-motion treatment.
No frameworks, CDNs or raw scripts unless necessary. Native details may expose
preparation information while future contact routes remain unauthored. Do not imply
booking, submission or contact delivery through a purely local interaction.

# Detailing Pass — the modern register applied to FIN

Applies to every FIN study carrying `<meta name="batch" content="V2-detailing">`. Only the design
layer is re-authored: V1's content spine, reserved media, placeholders and claims limits are kept
exactly as written. Where this section and the V1 language above disagree on surface treatment
(radius, disclosure behaviour, decoration), this section governs the V2 studies.

## The reading

The register is `standards/08-VISUAL-REFERENCE-STYLE.md`, read for finance as **the quiet ledger**:
generous space, precise edges and nothing that performs confidence. Type carries the page — a
system-sans display at weight 550, `clamp(2.5rem, 4.8vw, 5rem)`, line-height 1.02, tracking −0.035em,
with exactly one accent phrase per composition. Supporting text sits in muted ink at 1.02–1.22rem.
Surfaces are square-edged (radius 2px on fields, chips and actions; 8px is the ceiling anywhere),
separated by hairlines rather than cards, and one 3px accent lead rule anchors each composition.

| V1 language | V2 translation |
| --- | --- |
| Rounded 12–32px cards and pill captions | 2px edges; captions beneath the field, never floating on it |
| Accent-filled hero panel (004) | Accent used for one phrase, one lead rule and one bordered action |
| `<details>` with a rotating plus | The disclosure opened as a row with its mark; no script runs |
| Photographic slot with overlaid caption | Empty flat field on the media tone with a bottom-left label and a caption beneath |
| Section-level numerals | Word numerals (One, Two, Three) in bordered chips |

## The plotted layer

One drawn layer per variant, in line tone (or accent where noted), always `aria-hidden` and
decorative. No chart, gauge, dashboard, seal, coin, column or faux document appears anywhere.

| Variant | Layer | Where |
| --- | --- | --- |
| 001 | **Column rules** — three quiet vertical hairlines, as a ledger rules its page | behind the head |
| 002 | **Open bracket** — a thin accent corner | above the headline |
| 003 | **Registration grid** — small crosses on a 48px field | drawn once behind the composition |
| 004 | **Span mark** — a measure rule with end risers, in accent | beneath the key phrase |
| 005 | **Corner frame** — a 3px accent L along the display column | the display column |

## Themes

| Variant | Theme | Paper | Ink | Muted | Line | Media | Band | Accent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Ivory & Olive | `#faf8ef` | `#293224` | `#606653` | `#e6e9d4` | `#e3e6cc` | `#f0f2e0` | `#52652c` |
| 002 | Rosewood | `#fcf1ee` | `#442e35` | `#75616b` | `#f0dcd9` | `#efd6d9` | `#f7e6e4` | `#a3425c` |
| 003 | Lagoon | `#edf8f5` | `#183b36` | `#506d66` | `#d4e8e1` | `#cce5dc` | `#ddf0ea` | `#126957` |
| 004 | Iris | `#f5f2ff` | `#30294e` | `#696080` | `#e2dcf5` | `#e0d9f4` | `#ebe6fa` | `#6650b8` |
| 005 | Ink & Apricot, inverted | `#1b2330` | `#fff3e5` | `#bfc9d4` | `#2f3a49` | `#334253` | `#26303f` | `#ffd1a1` |

`--no` is a graphite (`#6b6f78`, `#8d9aa8` on 005) used only as an edge, chip border or mark for a
refusal or an awaiting-confirmation token — never as a surface.

## Rules in force

Namespace `.fin-sNN-vvv`; `data-study-id="FIN-SNN-vvv"`; shell `width: min(100%, 88rem)`.
No header, navigation or footer except where V1 authored one (S22). No script anywhere: every V1
`<details>` opens as a row. No gradient, shadow, dashed border, pill or radius above 8px. Inline
SVG only, all decorative and `aria-hidden`. Entities, not CSS escapes, in content. No digit in
visible copy outside a placeholder element or a field's ratio label — counts are word numerals.
`<h1>` on S01, S21 and the detail pages S23–S27 only; every other section keeps `<h2>`.

No firm, person, client, qualification, registration, regulatory status, testimonial, fee, coverage,
eligibility or availability is invented, and no return, saving, tax outcome, performance comparison
or guarantee is stated. V1's bracketed placeholders carry `data-placeholder="true"` and are declared
in `<meta name="placeholder-data">`. Reserved photographs stay empty labelled fields (THE DESK, THE
MEETING, THE OFFICE, THE WORKSPACE, THE ADVISOR, THE TEAM, THE COVER, THE ENTRANCE) and a consented
portrait is never drawn.

## Checker

`fincheck.ps1 -Dir <raw> -Sec SNN [-Fields '...'] [-AllowForm] [-AllowNav] [-AllowClaims '...']`
verifies the theme tokens, namespace, batch token, structure and tag balance, the finance claims
vocabulary (guarantee, best, leading, number one, no. 1, award, voted, stars, rated, %, five-star,
world-class, ranked, top-rated, certified by, accredited by, regulated by, authorised by, returns
of, savings of, save up to, risk-free, tax-free, lowest fee, lowest price, cheapest), the digit
rule, the `<h1>` rule and content parity across the five studies.

## Completion record — 23 September 2026

The detailing pass is complete for all twenty-seven sections: one hundred and thirty-five FIN studies
re-authored in the register above. Every study carries `<meta name="batch" content="V2-detailing">`,
the namespace `.fin-sNN-vvv`, one of the five themes, its variant's plotted layer (column rules, open
bracket, registration grid, span mark, corner frame) and one 3px accent lead rule. Each section holds
a `BATCH-V2.md` design record beside its `BATCH-V1.md` authoring record, and each section README is
marked `RE-AUTHORED — V2 DETAILING PASS`.

Verified per section with `fincheck.ps1` (themes, namespace, batch token, structure, claims
vocabulary, digits, the `<h1>` rule, media parity, placeholder parity across the five studies): 27 of
27 sections report ALL CHECKS PASS. Seven sections carry a documented allowance: S11 for the V1
placeholder word *guarantee*, which appears only inside a bracketed placeholder as something a
verified summary must not promise; S22 and the five detail pages S23–S27 for V1's own navigation
landmarks (`-AllowNav`) — the breadcrumb trail, related offerings, involvement links, related
reading with the in-page contents, the works-on list and the people based at an office. No section
needed `-AllowForm`: there is no `<form>` anywhere in the sector.

Where a content slot is variant-specific in V1, the re-authored studies match V1's own split rather
than levelling it, and each section record states the count: the context caption in S24 (2 / 0 / 4 /
1 / 3), the image caption in S25 (1 / 2 / 0 / 1 / 1), the portrait caption in S26 (present in 001,
003, 004 and 005), *Areas of focus* in S26 (a visible heading in 001–004, an `aria-label` in 005),
and the map and office areas in S27 (both in 001 and 003, the map alone in 004, neither in 002 and
005, where V1 refuses both in the copy).

V1's content spine is kept whole throughout: no claim, figure, name, place, price, date or contact
detail is invented, every reserved image and map remains an empty labelled field with no third-party
service embedded, every V1 `<details>` disclosure opens as a row (no script runs anywhere in the
sector), and `<h1>` appears only on S01, S21 and the detail pages S23–S27.
