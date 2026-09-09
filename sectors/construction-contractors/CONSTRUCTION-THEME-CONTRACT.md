# Construction & Contractors — Theme Contract

Prefix `CON`. This document makes the variant number a **theme**, not only a research direction.

## Why This Exists

`../../standards/01-AUTHORING-STANDARD.md` currently reads the five variants as independent
authoring territories: *"not production enums and not visual styles to be applied."* That reading
produced a catalog where the twenty-seven `001` studies of a sector share no palette, no type scale
and no geometry, and therefore cannot be assembled into a page.

The catalog is used the other way round. **The sections are combined.** `S01-001` sits above
`S02-001`, which sits above `S03-001`, and the result has to read as one website.

So the variant number carries a theme:

    Variant N of every section in a sector = website N of that sector.
    Five sections roles combined at the same variant = one coherent site.

## The Two Halves Of A Theme

| Fixed across every section at this variant | Free to differ in every section |
| --- | --- |
| Ground, ink and ink-soft values | Composition and grid |
| The accent, and what it is allowed to do | Media-to-text ratio |
| Font stack and type scale ratio | Asymmetry and alignment |
| Corner radius and border weight | Section rhythm and order |
| Slot (reserved media) treatment | Which device carries the hierarchy |
| Button shape and focus ring | Number and proportion of media areas |

**Variety comes from the right-hand column.** A hero and a testimonials block at the same variant
are completely different compositions that are obviously from the same site. Two studies that share
a layout are a failure of this contract just as much as two that share no palette.

## The Five CON Themes

The sector direction fixes the register: *concrete and asphalt neutrals with one high-visibility
accent.* Each theme is one reading of that sentence. Accents are the sector's own vocabulary —
safety orange, burnt amber, structural blue, high-vis yellow — never a decorative brand colour.

### 001 — Site White · Universal / Safe

| Token | Value |
| --- | --- |
| `--paper` | `#f5f5f3` concrete white |
| `--ink` | `#101112` |
| `--ink-soft` | `#5a5d61` |
| `--line` | `#dcdcd8` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#e6e6e2` / `#b9b9b3` / `#55585b` |
| `--accent` / `--accent-ink` | `#e8541f` safety orange / `#ffffff` |
| Radius | `14px`, pills `999px` |
| Register | Daylight, dependable, high legibility. The workhorse theme. |

### 002 — Bone · Premium / Editorial

| Token | Value |
| --- | --- |
| `--paper` | `#efece6` warm bone |
| `--ink` | `#16130f` |
| `--ink-soft` | `#6a655c` |
| `--line` | `#dad5cb` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#e4e0d7` / `#bdb6a8` / `#5f5a51` |
| `--accent` / `--accent-ink` | `#b4531d` burnt amber / `#ffffff` |
| Radius | `4px` — sharper than 001; editorial, not soft |
| Register | Fewer elements, larger type, more air. Lowest text density of the five. |

### 003 — Steel · Structured / Visual Modular

| Token | Value |
| --- | --- |
| `--paper` | `#eef1f3` cool steel |
| `--ink` | `#0d1114` |
| `--ink-soft` | `#56616b` |
| `--line` | `#d5dbdf` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#e1e6e9` / `#aeb8bf` / `#4e5860` |
| `--accent` / `--accent-ink` | `#1f5fd0` structural blue / `#ffffff` |
| Radius | `18px` |
| Register | Zoned and modular. Cards, bays, a visible grid. The accent marks the active zone. |

### 004 — High-Vis · Conversion-led

| Token | Value |
| --- | --- |
| `--paper` | `#ffffff` |
| `--ink` | `#0a0a0a` |
| `--ink-soft` | `#55585c` |
| `--line` | `#e4e4e4` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#efefef` / `#c2c2c2` / `#4f5155` |
| `--accent` / `--accent-ink` | `#ffd400` high-vis yellow / `#0a0a0a` (dark ink on yellow) |
| Radius | pills `999px`, panels `12px` |
| Register | One action dominates. The accent is a surface, not a detail. |

### 005 — Night Plant · Art-directed / Distinctive

| Token | Value |
| --- | --- |
| `--paper` | `#0c0d0e` |
| `--ink` | `#f4f4f2` |
| `--ink-soft` | `#9a9d9f` |
| `--line` | `#2c2e30` |
| `--slot` / `--slot-edge` / `--slot-ink` | `#161819` / `#4a4d50` / `#c8cbcd` |
| `--accent` / `--accent-ink` | `#ff5c1a` electric orange / `#0c0d0e` |
| Radius | `26px` |
| Register | Dark ground, large media, oversized line. The most photographic of the five. |

## Shared Across All Five

Constants that do not change with the theme:

- Frame `max-width: 1320px`, padding `clamp(22px, 3.6vw, 58px)`.
- Font stack `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.
  Heavy grotesque weights: `h1/h2` 800, `h3/h4` 750.
- Uppercase eyebrow, `0.8rem`, `letter-spacing: 0.085em`.
- Reserved media areas: dashed `--slot-edge`, `--slot` ground, uppercase `--slot-ink` label.
- Reserved value fields: an em dash with a visually hidden label naming the figure.
- Breakpoints at `860px` and `560px`; a `prefers-reduced-motion` block in every study.

## Text Budget

The measured `CON` catalog averaged **552 visible words** per study against 40–80 in the supplied
modern references. The budget from here:

| Role | Target visible words |
| --- | --- |
| Hero, CTA, breadcrumb | 40–90 |
| Standard content section | 90–170 |
| Detail page section (`S23`–`S27`) | 150–230 |
| Absolute ceiling, any study | **250** |

Prose paragraphs are the failure mode this replaces. A section argues through **headings, short
labelled rows and reserved fields**, not through essays.

## What Does Not Change

Study IDs, the reserved-field policy, the fabrication ban, the safety rules and the section-shell
rule all stand exactly as written in the sector direction and each section README. This contract
governs visual system and text budget only.
