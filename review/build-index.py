#!/usr/bin/env python3
"""
Build review/index.html — a local contact sheet of every authored raw study.

This is a local viewing aid for the authoring workspace. It is not a study, it is
not the Design Lab gallery, and it records no review decisions. Re-run it after
authoring a section:

    python3 review/build-index.py

It reads each study's <meta> research fields, falls back to the section's
BATCH-V1.md for the territory when a study predates the meta convention, and
writes a single page grouped by section with two preview columns.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTORS = ROOT / "sectors"
OUT = ROOT / "review" / "index.html"


def meta(src, name):
    m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % re.escape(name), src)
    return html.unescape(m.group(1)) if m else ""


def doc_title(src):
    m = re.search(r"<title>(.*?)</title>", src, re.S)
    return html.unescape(m.group(1).strip()) if m else ""


def territories_from_batch(section_dir):
    """Map study id -> territory from '### ARC-SNN-NNN — Territory' headings."""
    batch = section_dir / "BATCH-V1.md"
    if not batch.exists():
        return {}
    found = {}
    for line in batch.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^###\s+(ARC-S\d{2}-\d{3})\s+[—-]\s+(.+?)\s*$", line)
        if m:
            found[m.group(1)] = m.group(2)
    return found


def section_name(section_dir):
    readme = section_dir / "README.md"
    if readme.exists():
        m = re.search(r"# Section Name\s*\n\s*\n(.+)", readme.read_text(encoding="utf-8"))
        if m:
            return m.group(1).strip()
    return section_dir.name


def collect(sector_dir):
    sections = []
    for section_dir in sorted(p for p in sector_dir.iterdir() if p.is_dir() and re.match(r"^S\d{2}-", p.name)):
        raw = section_dir / "raw"
        files = sorted(raw.glob("ARC-*.html")) if raw.exists() else []
        if not files:
            continue
        batch_terr = territories_from_batch(section_dir)
        studies = []
        for f in files:
            src = f.read_text(encoding="utf-8")
            sid = meta(src, "study-id") or f.stem
            studies.append({
                "id": sid,
                "file": f,
                "title": doc_title(src),
                "territory": meta(src, "territory") or batch_terr.get(sid, ""),
                "layout": meta(src, "layout-model", ),
                "density": meta(src, "density"),
                "media": meta(src, "media-mode"),
                "interaction": meta(src, "interaction"),
            })
        sections.append({
            "dir": section_dir,
            "id": section_dir.name.split("-")[0],
            "name": section_name(section_dir),
            "studies": studies,
        })
    return sections


def esc(s):
    return html.escape(s or "", quote=True)


def render(sections, sector_label):
    total = sum(len(s["studies"]) for s in sections)
    nav = "\n".join(
        '        <li><a href="#{sid}">{sid} <span>{name}</span> <b>{n}</b></a></li>'.format(
            sid=esc(s["id"]), name=esc(s["name"]), n=len(s["studies"]))
        for s in sections
    )

    blocks = []
    for s in sections:
        cards = []
        for st in s["studies"]:
            rel = "../" + st["file"].relative_to(ROOT).as_posix()
            facts = []
            for label, key in (("Layout", "layout"), ("Density", "density"),
                               ("Media", "media"), ("Interaction", "interaction")):
                if st[key]:
                    facts.append(
                        "            <div><dt>{l}</dt><dd>{v}</dd></div>".format(l=label, v=esc(st[key])))
            facts_html = "\n".join(facts) or "            <div><dt>Metadata</dt><dd>Not recorded in this study</dd></div>"
            cards.append("""        <li class="card">
          <div class="card__head">
            <h3>{sid}</h3>
            <p class="terr">{terr}</p>
          </div>
          <div class="frame" data-frame>
            <iframe src="{rel}" title="Preview of study {sid}" loading="lazy" tabindex="-1" scrolling="no"></iframe>
          </div>
          <dl class="facts">
{facts}
          </dl>
          <a class="open" href="{rel}" target="_blank" rel="noopener">Open study<span aria-hidden="true"> &#8599;</span></a>
        </li>""".format(sid=esc(st["id"]), terr=esc(st["territory"] or "—"), rel=esc(rel), facts=facts_html))

        blocks.append("""    <section class="group" id="{sid}" aria-labelledby="{sid}-h">
      <div class="group__head">
        <h2 id="{sid}-h"><span class="group__id">{sid}</span> {name}</h2>
        <p>{n} studies</p>
      </div>
      <ul class="grid">
{cards}
      </ul>
    </section>""".format(sid=esc(s["id"]), name=esc(s["name"]),
                         n=len(s["studies"]), cards="\n".join(cards)))

    return TEMPLATE.format(
        sector=esc(sector_label),
        total=total,
        sections=len(sections),
        nav=nav,
        blocks="\n\n".join(blocks),
    )


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Review contact sheet — {sector}</title>

<!--
  Local review aid for the Sector Design Authoring Workspace.
  NOT a raw study, NOT the Design Lab gallery, and it records no review decisions.
  Generated by review/build-index.py — re-run that script after authoring a section.
-->

<style>
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{
  margin: 0;
  background: #101114;
  color: #f2f2f0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}}
:focus-visible {{ outline: 2px solid #ffd479; outline-offset: 3px; }}
a {{ color: inherit; }}

.shell {{ max-width: 1560px; margin: 0 auto; padding: 0 clamp(14px, 2.4vw, 34px); }}

/* --- Masthead ------------------------------------------------------- */
.masthead {{
  position: sticky; top: 0; z-index: 10;
  background: rgba(16, 17, 20, 0.94);
  border-bottom: 1px solid rgba(242, 242, 240, 0.16);
  backdrop-filter: blur(8px);
}}
.masthead__row {{
  display: flex; align-items: center; justify-content: space-between;
  gap: 20px; flex-wrap: wrap; padding: 14px 0;
}}
.masthead h1 {{ margin: 0; font-size: 1rem; font-weight: 600; letter-spacing: -0.01em; }}
.masthead .count {{ margin: 2px 0 0; font-size: 0.75rem; color: #a7a9ad; }}

.widths {{ display: flex; gap: 6px; }}
.widths button {{
  min-height: 36px; padding: 0 14px;
  background: transparent; color: #f2f2f0;
  border: 1px solid rgba(242, 242, 240, 0.28); border-radius: 999px;
  font: inherit; font-size: 0.75rem; cursor: pointer;
}}
.widths button:hover {{ border-color: rgba(242, 242, 240, 0.6); }}
.widths button[aria-pressed="true"] {{ background: #f2f2f0; color: #101114; border-color: #f2f2f0; }}

/* --- Section nav ------------------------------------------------------ */
.sectionnav ul {{
  display: flex; flex-wrap: wrap; gap: 6px;
  margin: 0; padding: 0 0 12px; list-style: none;
}}
.sectionnav a {{
  display: inline-flex; align-items: baseline; gap: 7px;
  padding: 6px 12px; border-radius: 999px;
  border: 1px solid rgba(242, 242, 240, 0.18);
  font-size: 0.6875rem; text-decoration: none; color: #d5d6d8;
}}
.sectionnav a:hover {{ border-color: rgba(242, 242, 240, 0.5); color: #fff; }}
.sectionnav span {{ color: #a7a9ad; }}
.sectionnav b {{ font-weight: 600; color: #fff; }}

/* --- Groups ------------------------------------------------------------ */
.group {{ padding: clamp(28px, 3.4vw, 52px) 0 0; }}
.group__head {{
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 16px; flex-wrap: wrap;
  padding-bottom: 14px; margin-bottom: clamp(16px, 2vw, 24px);
  border-bottom: 1px solid rgba(242, 242, 240, 0.24);
}}
.group__head h2 {{ margin: 0; font-size: clamp(1.125rem, 1.9vw, 1.5rem); letter-spacing: -0.02em; font-weight: 500; }}
.group__id {{
  display: inline-block; margin-right: 10px; padding: 3px 9px;
  border: 1px solid rgba(242, 242, 240, 0.32); border-radius: 4px;
  font-size: 0.6875rem; letter-spacing: 0.1em; vertical-align: middle;
}}
.group__head p {{ margin: 0; font-size: 0.75rem; color: #a7a9ad; }}

/* --- Two-column card grid ----------------------------------------------- */
.grid {{
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: clamp(14px, 2vw, 28px);
  margin: 0; padding: 0; list-style: none;
}}
.card {{
  display: flex; flex-direction: column;
  background: #17181c; border: 1px solid rgba(242, 242, 240, 0.14); border-radius: 10px;
  overflow: hidden;
}}
.card__head {{
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 12px; flex-wrap: wrap; padding: 13px 15px;
  border-bottom: 1px solid rgba(242, 242, 240, 0.12);
}}
.card__head h3 {{ margin: 0; font-size: 0.8125rem; letter-spacing: 0.04em; font-weight: 600; }}
.terr {{ margin: 0; font-size: 0.6875rem; color: #a7a9ad; text-align: right; }}

/* Scaled live preview */
.frame {{
  position: relative; overflow: hidden;
  background: #fff; border-bottom: 1px solid rgba(242, 242, 240, 0.12);
}}
.frame iframe {{
  position: absolute; top: 0; left: 0;
  width: var(--fw, 1440px); height: var(--fh, 900px);
  border: 0; transform-origin: top left;
  transform: scale(var(--s, 0.3));
}}

.facts {{ margin: 0; padding: 12px 15px; display: grid; gap: 7px; flex: 1 1 auto; }}
.facts > div {{ display: grid; grid-template-columns: 74px minmax(0, 1fr); gap: 10px; align-items: baseline; }}
.facts dt {{ font-size: 0.625rem; letter-spacing: 0.1em; text-transform: uppercase; color: #a7a9ad; }}
.facts dd {{ margin: 0; font-size: 0.75rem; color: #e4e5e7; }}

.open {{
  display: block; padding: 12px 15px; border-top: 1px solid rgba(242, 242, 240, 0.12);
  font-size: 0.75rem; text-decoration: none; color: #f2f2f0;
}}
.open:hover {{ background: #1e2025; }}

footer {{
  padding: clamp(30px, 4vw, 60px) 0; margin-top: clamp(28px, 3.4vw, 48px);
  border-top: 1px solid rgba(242, 242, 240, 0.16);
  font-size: 0.75rem; color: #a7a9ad;
}}
footer p {{ margin: 0 0 6px; max-width: 76ch; }}

@media (max-width: 900px) {{
  .grid {{ grid-template-columns: minmax(0, 1fr); }}
}}

@media (prefers-reduced-motion: reduce) {{
  * {{ animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; scroll-behavior: auto !important; }}
}}
</style>
</head>

<body>

<header class="masthead">
  <div class="shell">
    <div class="masthead__row">
      <div>
        <h1>{sector} &#183; review contact sheet</h1>
        <p class="count">{total} studies across {sections} sections &#183; live previews, two columns</p>
      </div>
      <div class="widths" role="group" aria-label="Preview viewport width">
        <button type="button" data-w="1440" data-h="900" aria-pressed="true">Desktop 1440</button>
        <button type="button" data-w="768" data-h="1000" aria-pressed="false">Tablet 768</button>
        <button type="button" data-w="390" data-h="844" aria-pressed="false">Phone 390</button>
      </div>
    </div>
    <nav class="sectionnav" aria-label="Sections">
      <ul>
{nav}
      </ul>
    </nav>
  </div>
</header>

<main class="shell">

{blocks}

  <footer>
    <p>
      Local review aid for the Sector Design Authoring Workspace. This page is not a raw study,
      it is not the Design Lab gallery, and it records no review, normalisation, survivor-selection
      or promotion decision. Those belong to Design Lab.
    </p>
    <p>
      Previews are the real study files rendered in iframes at the selected viewport width and
      scaled down, so what is shown is the actual layout, not a screenshot. Regenerate this page
      with <code>python3 review/build-index.py</code> after authoring a section.
    </p>
  </footer>
</main>

<script>
(function () {{
  var frames = Array.prototype.slice.call(document.querySelectorAll('[data-frame]'));
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.widths button'));
  var W = 1440, H = 900;

  function layout() {{
    frames.forEach(function (f) {{
      var scale = f.clientWidth / W;
      f.style.setProperty('--s', scale);
      f.style.setProperty('--fw', W + 'px');
      f.style.setProperty('--fh', H + 'px');
      f.style.height = Math.round(H * scale) + 'px';
    }});
  }}

  buttons.forEach(function (b) {{
    b.addEventListener('click', function () {{
      W = parseInt(b.getAttribute('data-w'), 10);
      H = parseInt(b.getAttribute('data-h'), 10);
      buttons.forEach(function (o) {{ o.setAttribute('aria-pressed', String(o === b)); }});
      layout();
    }});
  }});

  window.addEventListener('resize', layout);
  window.addEventListener('load', layout);
  layout();
}})();
</script>
</body>
</html>
"""


def main():
    sector_dir = SECTORS / "architecture-interior-design"
    sections = collect(sector_dir)
    OUT.write_text(render(sections, "Architecture & Interior Design"), encoding="utf-8")
    total = sum(len(s["studies"]) for s in sections)
    print("wrote %s" % OUT.relative_to(ROOT))
    for s in sections:
        print("  %s %-28s %d studies" % (s["id"], s["name"], len(s["studies"])))
    print("  total: %d studies across %d sections" % (total, len(sections)))


if __name__ == "__main__":
    main()
