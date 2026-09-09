# BATCH V1

## Batch Identity

- Sector: `Dental Clinics`
- Prefix: `DN`
- Section ID: `DN-S05`
- Section Name: `Smile Results`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

Fifth batch in the `DN` sector, authored against `../DENTAL-THEME-CONTRACT.md`. **The section `S03`
pointed at.** The sector stands at **25 studies**.

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Pairs | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `DN-S05-001` | Universal / Safe | 001 Chalk | **A** | The four rules first, then four cases as a grid | 4 | 185 |
| `DN-S05-002` | Premium / Editorial | 002 Linen | **B** | **One case shown properly**, the other three in type | 1 | 178 |
| `DN-S05-003` | Structured / Visual Modular | 003 Slate | **A** | Joined modules, **each carrying its own rule strip** | 4 | 204 |
| `DN-S05-004` | Conversion-led | 004 Daylight | **B** | **The selection ratio first**, at display size | 2 | 172 |
| `DN-S05-005` | Art-directed / Distinctive | 005 Dusk | **A** | **Every case captioned twice** — the second saying what it does not show | 4 | 214 |

## The Section Role

The before-and-after gallery, and the disclosures that make one readable.

## The Trap

A wall of thumbnails. Different light in each half, a wetter mouth in the second, a caption reading
*Veneers*, and a heading claiming five hundred smiles transformed. Every case looks like every other
case, none can be checked, and the reader stops believing the page before the third row.

## The Governing Idea

> **A before-and-after tells you nothing unless you know what changed between the two photographs
> besides the teeth.**

## The Debt To S03

`S03` refused a gallery outright — *those photographs are lit, chosen and unverifiable; the ones we
can show, and the rules that apply to them, are in smile results.* **This section owes the reader
those rules.** All five studies print all four, and no study softens the fourth.

## The Four Cases

Shared across all five studies, so the batch varies by composition rather than by copy. The last
column is the field nobody prints.

| Case | What was done | **Second photograph taken** |
| --- | --- | --- |
| Two chipped front teeth | Composite bonding, one visit | **the same day** |
| Discoloured after a root canal | Internal whitening and one crown, six weeks | **eleven months later** |
| Crowding, upper front | Aligners for fourteen months, then polishing | **four months after finishing** |
| A missing premolar | Implant, five months of healing | **two weeks after fitting** |

*Eleven months later* is the one that matters. A whitening result photographed on the day is not a
result, and the difference between *the same day* and *eleven months later* is the difference between
a claim and a fact. Both appear here, undisguised.

## The Four Rules

1. **Same camera, same light.** Both photographs, every case. Different light is most of what you see.
2. **Not retouched.** Cropped, and nothing else.
3. **We chose these.** Four shown out of sixty-one that year, and the clear ones were picked.
4. **One case each.** Not a typical result.

Rule three is the admission nothing in this sector makes out loud, and it costs the section the thing
every competitor leads with: the impression of abundance. **A reader counting fifty-seven unshown
cases is doing arithmetic no other clinic invites.**

## No Face, In Any Of Them

Every study closes on the same line, in full:

> **No face appears in any of these.** The pairs are cropped to the work, and consent covers that crop
> only.

The contract bans the stock smile and the open-mouth close-up; this section is where that ban costs
something, and the line states what was given up rather than quietly omitting it.

## The Five Compositions

- **`001`** — the safe reading: the rules printed **above** the pictures, at the same weight, then
  four cases in a grid.
- **`002`** — a grid forces every case down to a thumbnail and a two-word caption, and **the caption
  is where the honest information would have gone**. So one case takes the whole measure with all four
  rules attached to it, and the other three are a line each. **One case a reader can interrogate is
  worth four they can only look at.**
- **`003`** — four joined modules on one plate, **each carrying its own rule strip**, so no single case
  can travel without its timing and its *not a typical result*. The strip is per-item because a case
  lifted out of this section is a case stripped of its disclosure.
- **`004`** — **the ratio first**, at display size in a filled band, before the first image. A gallery
  converts on volume; this one opens by admitting the volume it is not showing, and then shows two.
- **`005`** — **every picture is captioned twice, once with what it shows and once with what it does
  not.** What it cost. How the shade looks in daylight. Fourteen months of wearing them. Five months
  of waiting. The payoff sets at display size: *a pair of photographs shows the last ten minutes of
  something that took months.*

`005` is the sector-native reading. The other four disclose the *conditions* of the photograph — the
light, the retouching, the selection, the timing — and those are honest but still about the image.
`005` goes after what the image cannot contain at all. **A gallery that prints its own blind spots
beside each case is telling the reader how to look at it**, which is the only thing it can honestly
offer someone who has already learned to distrust one.

## Verification Record

- Word band `170–230` (structured): **185 / 178 / 204 / 172 / 214.** All five in band.
- Content parity: **23 shared fields checked across all five studies, zero missing** — four case
  subjects, four treatments, four timings, all four rules, the selection ratio, the no-face line and
  the consent line.
- Tag balance: **0 unbalanced elements** across all five. No `<script>`, `<img>`, `<iframe>`, `<form>`
  or `<input>`; no absolute URL, no `@import`, no `<link>`; every rule scoped to its study namespace.
- Theme conformance: **5/5** match the contract's grounds, inks and accents. Frame `1320px` and the
  `prefers-reduced-motion` block present in all five.
- Claims scan: clean — no guarantee, no *transform*, no *pain-free* or *gentle*, no price, no
  credential, no `Dr` title, no testimonial, no patient name, no gendered pronoun, no award, no
  countdown.
- Composition collisions: **no exact match, no near matches** across the sector's twenty-five studies.
- Rendered at 1440px and read: all five correct.

### Found by the parity diff, before rendering

- **`005` had no `Not retouched` rule at all.** Its rules row carried three of the four, and *cropped,
  and nothing else* appeared nowhere in the study. The closing line's *cropped to the work* is about
  consent, not retouching, and it reads close enough to have covered the gap by eye. Caught
  mechanically, not visually — the same class of miss as the absent attachments block in
  `CONS-S26-004`. The fourth rule was restored and the rules row widened to four columns.
- **`005` measured 256 words**, twenty-six over the band and fifty over its nearest sibling. The
  overrun was the lead restating the governing idea that the display line already carries, and a
  five-word label repeated under four pictures. Trimmed to **214** by cutting the restatement and
  shortening the repeated label to *Does not show* — no rule and no case field was dropped to get
  there.

### The word counts were re-measured

The five headers declared counts from an earlier pass that disagreed with each other by up to thirty
words. All five were re-measured with one counter and the headers re-synced, so the numbers in the
table above and in the study headers are the same measurement.

### Found only by rendering

- **The `.rest h3` rule was missing in `004`.** The two listed cases rendered at the browser's default
  heading size with a default `1em` margin, while the two shown cases were tight and bold at
  `1.06rem` — so the study's own argument, that a listed case is the same case with less picture, was
  contradicted by the type. The rule was extended to cover both.
- **The divider above the display line in `005` stopped at `60ch`**, mid-air, over a rules row running
  the full width. It read as a truncated rule rather than a measure rule. The `max-width` came off,
  and the display line now sets on one line at desktop.

### Recorded, not chased

- The superiority scan flags *best* in `004` — from *you are looking at the best of a year, not the
  average of one*, which is an admission of selection and the opposite of a superiority claim.
- The Dusk accent `#6ea8a0` sits at hue 172 and saturation 0.25, just inside the aqua threshold the
  scan uses. It is the contract's accent, established across `S01`–`S04`, and it renders as a muted
  sage rather than a whitening blue. The threshold is what is tight here, not the colour.

### A tooling note

The Bash heredoc used to write scan scripts collapses `\\` to `\`, so any regex built by string
concatenation silently loses its escapes — `--paper:\\s*#f6f4f1` arrives as `--paper:s*#f6f4f1` and
reports every study as failing theme conformance and every tag as unbalanced. **Regex literals
survive; `new RegExp` over a concatenated string does not.** The first scan run of this batch was
entirely false positives because of it.

## What This Batch Fixes For The Rest Of The Sector

- **The four rules and the timing field**, inherited by `S24` for a single case study.
- **The no-face line is stated, not silently obeyed** — a refusal the reader can see is worth more
  than one they cannot.
- **The selection ratio is a printable fact**, and it belongs wherever this sector shows chosen work.
- **Run the parity diff before rendering.** It caught a missing rule that reads fine on the page.
