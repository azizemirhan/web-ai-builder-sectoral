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

The page also carries a PDF export: pick sections or individual studies, and the
browser prints one landscape page per study showing it at desktop, tablet and
phone width side by side. So that each study can be scaled to fit a printed page,
this script measures every study's rendered height at those three widths with
headless Chrome and writes the numbers into the page. Measurements are cached in
review/.heights.json and only re-taken when a file changes.

    python3 review/build-index.py              # measure changed studies, then build
    python3 review/build-index.py --no-measure # build with cached or default heights
    python3 review/build-index.py --pdf        # also print the whole sector to
                                               # review/architecture-contact-sheet.pdf
"""

import hashlib
import html
import json
import os
import re
import concurrent.futures
import itertools
import subprocess
import sys
import threading
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTORS = ROOT / "sectors"
OUT = ROOT / "review" / "index.html"
PDF_OUT = ROOT / "review" / "architecture-contact-sheet.pdf"
CACHE = ROOT / "review" / ".heights.json"

# Widths the PDF export prints side by side, and the fallback heights used when a
# study has never been measured (long enough not to cut a page off mid-way).
PDF_CSS = r"""
/* --- PDF export: toolbar button --------------------------------------- */
.tools { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.pdfbtn {
  min-height: 36px; padding: 0 16px;
  background: #f2f2f0; color: #101114;
  border: 1px solid #f2f2f0; border-radius: 999px;
  font: inherit; font-size: 0.75rem; font-weight: 600; cursor: pointer;
}
.pdfbtn:hover { background: #fff; }

/* --- PDF export: picker ------------------------------------------------ */
.pickr {
  width: min(1000px, 94vw); max-height: 88vh; padding: 0;
  color: #f2f2f0; background: #17181c;
  border: 1px solid rgba(242, 242, 240, 0.24); border-radius: 12px;
}
.pickr::backdrop { background: rgba(8, 9, 11, 0.74); }
.pickr__form { display: flex; flex-direction: column; max-height: 88vh; }
.pickr__head { padding: 16px 20px; border-bottom: 1px solid rgba(242, 242, 240, 0.16); }
.pickr__head h2 { margin: 0 0 4px; font-size: 0.9375rem; font-weight: 600; }
.pickr__head p { margin: 0; font-size: 0.75rem; color: #a7a9ad; max-width: 74ch; }
.pickr__opts {
  display: flex; flex-wrap: wrap; gap: 10px 26px; align-items: flex-start;
  padding: 12px 20px; border-bottom: 1px solid rgba(242, 242, 240, 0.12);
}
.pickr fieldset { margin: 0; padding: 0; border: 0; }
.pickr legend {
  padding: 0 0 6px; font-size: 0.625rem; letter-spacing: 0.12em;
  text-transform: uppercase; color: #a7a9ad;
}
.pickr__opts label { display: inline-flex; align-items: center; gap: 7px; margin-right: 14px; font-size: 0.75rem; }
.pickr__bulk { margin-left: auto; display: flex; gap: 8px; align-items: flex-end; }
.pickr__bulk button, .pickr__foot button {
  min-height: 34px; padding: 0 14px;
  background: transparent; color: #f2f2f0;
  border: 1px solid rgba(242, 242, 240, 0.3); border-radius: 999px;
  font: inherit; font-size: 0.75rem; cursor: pointer;
}
.pickr__bulk button:hover, .pickr__foot button:hover { border-color: rgba(242, 242, 240, 0.7); }
.pickr__list { overflow: auto; padding: 6px 20px 16px; flex: 1 1 auto; }
.secrow { border-bottom: 1px solid rgba(242, 242, 240, 0.1); }
.secrow__top { display: flex; align-items: center; gap: 10px; padding: 9px 0; }
.secrow__top label { display: inline-flex; align-items: center; gap: 9px; font-size: 0.8125rem; cursor: pointer; }
.secrow__id {
  display: inline-block; min-width: 34px; padding: 2px 7px;
  border: 1px solid rgba(242, 242, 240, 0.28); border-radius: 4px;
  font-size: 0.625rem; letter-spacing: 0.08em; text-align: center;
}
.secrow__n { margin-left: auto; font-size: 0.6875rem; color: #a7a9ad; }
.secrow__toggle {
  min-height: 30px; padding: 0 10px; background: transparent; color: #d5d6d8;
  border: 1px solid rgba(242, 242, 240, 0.2); border-radius: 999px;
  font: inherit; font-size: 0.625rem; cursor: pointer;
}
.secrow__kids { display: none; padding: 0 0 10px 44px; }
.secrow__kids[data-open="1"] { display: block; }
.secrow__kids ul { margin: 0; padding: 0; list-style: none; display: grid; gap: 4px; }
.secrow__kids label { display: inline-flex; align-items: baseline; gap: 8px; font-size: 0.75rem; color: #d5d6d8; }
.secrow__kids .t { color: #a7a9ad; }
.pickr__foot {
  display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
  padding: 14px 20px; border-top: 1px solid rgba(242, 242, 240, 0.16);
}
.pickr__count { margin: 0; font-size: 0.75rem; color: #a7a9ad; }
.pickr__foot .go { margin-left: auto; background: #f2f2f0; color: #101114; border-color: #f2f2f0; font-weight: 600; }
.pickr__warn { margin: 0; width: 100%; font-size: 0.6875rem; color: #ffce8a; }

/* --- PDF export: print view -------------------------------------------- */
#pdfroot { display: none; }
body.pdfmode #pdfroot { display: block; }
body.pdfmode > .masthead, body.pdfmode > main { display: none; }
.pdfbar {
  position: sticky; top: 0; z-index: 5;
  display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
  padding: 12px clamp(14px, 2.4vw, 34px);
  background: rgba(16, 17, 20, 0.96); border-bottom: 1px solid rgba(242, 242, 240, 0.16);
}
.pdfbar p { margin: 0; font-size: 0.75rem; color: #a7a9ad; }
.pdfbar button {
  min-height: 34px; padding: 0 14px; background: transparent; color: #f2f2f0;
  border: 1px solid rgba(242, 242, 240, 0.3); border-radius: 999px;
  font: inherit; font-size: 0.75rem; cursor: pointer;
}
.pdfbar .print { margin-left: auto; background: #f2f2f0; color: #101114; border-color: #f2f2f0; font-weight: 600; }
.pdfpages { padding: 18px clamp(14px, 2.4vw, 34px) 40px; }
.pdfpage {
  position: relative; margin: 0 auto 20px; padding: 0;
  background: #fff; color: #111214; overflow: hidden;
}
.pdfpage__head {
  display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap;
  height: 26px; padding: 0 2px; border-bottom: 1px solid #d9d9d6;
  font-size: 10px; letter-spacing: 0.02em;
}
.pdfpage__head b { font-size: 11px; letter-spacing: 0.06em; }
.pdfpage__head span { color: #5b5e63; }
.pdfpage__head .sec { margin-left: auto; color: #5b5e63; }
.pdfrow { display: flex; align-items: flex-start; gap: 14px; padding-top: 8px; }
.pdfdev__cap {
  margin: 0 0 4px; font-size: 8px; letter-spacing: 0.14em;
  text-transform: uppercase; color: #5b5e63;
}
.pdfhold { position: relative; overflow: hidden; border: 1px solid #d9d9d6; background: #fff; }
.pdfhold iframe { position: absolute; top: 0; left: 0; border: 0; transform-origin: top left; }

@media print {
  html, body { background: #fff !important; }
  .pdfbar { display: none !important; }
  .pdfpages { padding: 0 !important; }
  .pdfpage { margin: 0 !important; break-after: page; page-break-after: always; }
  .pdfpage:last-child { break-after: auto; page-break-after: auto; }
}
"""

PDF_JS = r"""
(function () {
  var raw = document.getElementById('pdf-data');
  if (!raw) return;
  var DATA = JSON.parse(raw.textContent);
  var WIDTHS = DATA.widths;                       // [1440, 768, 390]
  var LABELS = ['Desktop', 'Tablet', 'Phone'];
  var PAPER = { a3: [420, 297], a4: [297, 210] }; // mm, landscape
  var MARGIN = 8;                                 // mm
  var GAP = 14;                                   // px between device columns

  var dlg = document.getElementById('pickr');
  var openBtn = document.getElementById('pdfopen');
  var list = document.getElementById('pickr-list');
  var count = document.getElementById('pickr-count');
  var warn = document.getElementById('pickr-warn');
  var root = document.getElementById('pdfroot');
  var pageStyle = document.getElementById('pdf-pagesize');

  function mm(v) { return v * 96 / 25.4; }
  function el(tag, cls) { var n = document.createElement(tag); if (cls) n.className = cls; return n; }

  /* ---- picker ------------------------------------------------------- */
  var bySection = [];
  DATA.studies.forEach(function (st) {
    var g = bySection[bySection.length - 1];
    if (!g || g.id !== st.sec) { g = { id: st.sec, name: st.secName, items: [] }; bySection.push(g); }
    g.items.push(st);
  });

  bySection.forEach(function (g) {
    var row = el('div', 'secrow');
    var top = el('div', 'secrow__top');

    var lab = el('label');
    var cb = el('input');
    cb.type = 'checkbox'; cb.checked = true; cb.setAttribute('data-sec', g.id);
    var idb = el('span', 'secrow__id'); idb.textContent = g.id;
    var nm = el('span'); nm.textContent = g.name;
    lab.appendChild(cb); lab.appendChild(idb); lab.appendChild(nm);

    var n = el('span', 'secrow__n'); n.textContent = g.items.length + ' tasarım';
    var tog = el('button', 'secrow__toggle');
    tog.type = 'button'; tog.textContent = 'Tasarımlar';
    tog.setAttribute('aria-expanded', 'false');

    top.appendChild(lab); top.appendChild(n); top.appendChild(tog);

    var kids = el('div', 'secrow__kids');
    kids.id = 'kids-' + g.id;
    tog.setAttribute('aria-controls', kids.id);
    var ul = el('ul');
    g.items.forEach(function (st) {
      var li = el('li');
      var l = el('label');
      var c = el('input');
      c.type = 'checkbox'; c.checked = true; c.setAttribute('data-id', st.id); c.setAttribute('data-sec', g.id);
      var t = el('span'); t.textContent = st.id;
      var tt = el('span', 't'); tt.textContent = st.terr ? '· ' + st.terr : '';
      l.appendChild(c); l.appendChild(t); l.appendChild(tt);
      li.appendChild(l); ul.appendChild(li);
    });
    kids.appendChild(ul);

    tog.addEventListener('click', function () {
      var open = kids.getAttribute('data-open') === '1';
      kids.setAttribute('data-open', open ? '0' : '1');
      tog.setAttribute('aria-expanded', String(!open));
    });
    cb.addEventListener('change', function () {
      kids.querySelectorAll('input[data-id]').forEach(function (c) { c.checked = cb.checked; });
      refresh();
    });
    kids.addEventListener('change', function () { syncSection(g.id); refresh(); });

    row.appendChild(top); row.appendChild(kids);
    list.appendChild(row);
  });

  function syncSection(sec) {
    var kids = Array.prototype.slice.call(list.querySelectorAll('input[data-id][data-sec="' + sec + '"]'));
    var on = kids.filter(function (c) { return c.checked; }).length;
    var head = list.querySelector('input[data-sec="' + sec + '"]:not([data-id])');
    head.checked = on === kids.length;
    head.indeterminate = on > 0 && on < kids.length;
  }

  function selected() {
    var ids = {};
    list.querySelectorAll('input[data-id]').forEach(function (c) { if (c.checked) ids[c.getAttribute('data-id')] = 1; });
    return DATA.studies.filter(function (s) { return ids[s.id]; });
  }

  function devices() {
    return [0, 1, 2].filter(function (i) {
      var b = document.querySelector('input[name="dev"][value="' + i + '"]');
      return b && b.checked;
    });
  }

  function refresh() {
    var n = selected().length;
    var d = devices().length;
    count.textContent = n + ' tasarım · ' + n + ' sayfa · ' + d + ' cihaz görünümü';
    warn.textContent = n > 40
      ? 'Bu kadar çok sayfa hazırlanırken tarayıcı yavaşlayabilir; her sayfa canlı olarak yeniden çiziliyor.'
      : '';
    document.getElementById('pickr-go').disabled = n === 0 || d === 0;
  }

  document.getElementById('pickr-all').addEventListener('click', function () {
    list.querySelectorAll('input[type="checkbox"]').forEach(function (c) { c.checked = true; c.indeterminate = false; });
    refresh();
  });
  document.getElementById('pickr-none').addEventListener('click', function () {
    list.querySelectorAll('input[type="checkbox"]').forEach(function (c) { c.checked = false; c.indeterminate = false; });
    refresh();
  });
  Array.prototype.slice.call(document.querySelectorAll('input[name="dev"], input[name="paper"]'))
    .forEach(function (i) { i.addEventListener('change', refresh); });

  openBtn.addEventListener('click', function () {
    refresh();
    if (dlg.showModal) { dlg.showModal(); } else { dlg.setAttribute('open', ''); }
  });
  document.getElementById('pickr-close').addEventListener('click', function () {
    if (dlg.close) { dlg.close(); } else { dlg.removeAttribute('open'); }
  });

  /* ---- build the print view ------------------------------------------ */
  document.getElementById('pickr-go').addEventListener('click', function () {
    var items = selected();
    var devs = devices();
    var paper = document.querySelector('input[name="paper"]:checked').value;
    if (dlg.close) { dlg.close(); } else { dlg.removeAttribute('open'); }
    build(items, devs, paper);
  });

  function build(items, devs, paper) {
    var dims = PAPER[paper];
    var availW = mm(dims[0] - 2 * MARGIN);
    var availH = mm(dims[1] - 2 * MARGIN);
    var contentH = availH - 48;

    pageStyle.textContent = '@page { size: ' + paper.toUpperCase() + ' landscape; margin: ' + MARGIN + 'mm; }';

    root.innerHTML = '';
    var bar = el('div', 'pdfbar');
    var status = el('p');
    status.textContent = 'Sayfalar hazırlanıyor…';
    var back = el('button'); back.type = 'button'; back.textContent = '← Listeye dön';
    var printBtn = el('button', 'print'); printBtn.type = 'button';
    printBtn.textContent = 'Yazdır / PDF olarak kaydet';
    printBtn.disabled = true;
    bar.appendChild(back); bar.appendChild(status); bar.appendChild(printBtn);
    root.appendChild(bar);

    var pages = el('div', 'pdfpages');
    root.appendChild(pages);

    var frames = [];
    items.forEach(function (st) {
      var page = el('section', 'pdfpage');
      page.style.width = availW + 'px';
      page.style.height = availH + 'px';

      var head = el('div', 'pdfpage__head');
      var b = el('b'); b.textContent = st.id;
      var t = el('span'); t.textContent = st.terr || '';
      var sec = el('span', 'sec'); sec.textContent = st.sec + ' · ' + st.secName;
      head.appendChild(b); head.appendChild(t); head.appendChild(sec);
      page.appendChild(head);

      var row = el('div', 'pdfrow');
      var cols = devs.map(function (i) {
        var col = el('div', 'pdfdev');
        var cap = el('p', 'pdfdev__cap');
        var hold = el('div', 'pdfhold');
        var f = el('iframe');
        f.setAttribute('data-src', st.rel);
        f.setAttribute('title', st.id + ' — ' + LABELS[i] + ' ' + WIDTHS[i]);
        f.setAttribute('scrolling', 'no');
        f.setAttribute('tabindex', '-1');
        hold.appendChild(f);
        col.appendChild(cap); col.appendChild(hold);
        row.appendChild(col);
        frames.push(f);
        return { w: WIDTHS[i], h: st.h[i] || 2400, label: LABELS[i], cap: cap, hold: hold, frame: f };
      });
      page.appendChild(row);
      pages.appendChild(page);

      // Each column is scaled so the whole study fits the printed page height. The height
      // baked in at build time is the starting point; if the browser can read the study's
      // real height once it has loaded (same-origin, e.g. served over http), that wins.
      function layout() {
        var scales = cols.map(function (c) { return Math.min(1, contentH / c.h); });
        var gaps = GAP * (cols.length - 1);
        var total = cols.reduce(function (a, c, i) { return a + c.w * scales[i]; }, 0);
        if (total + gaps > availW) {
          var k = (availW - gaps) / total;
          scales = scales.map(function (v) { return v * k; });
        }
        cols.forEach(function (c, i) {
          c.hold.style.width = Math.round(c.w * scales[i]) + 'px';
          c.hold.style.height = Math.round(c.h * scales[i]) + 'px';
          c.frame.style.width = c.w + 'px';
          c.frame.style.height = c.h + 'px';
          c.frame.style.transform = 'scale(' + scales[i] + ')';
          c.cap.textContent = c.label + ' ' + c.w + ' · ' + c.h + 'px';
        });
      }
      layout();

      cols.forEach(function (c) {
        c.frame.addEventListener('load', function () {
          try {
            var d = c.frame.contentDocument;
            if (d) {
              var real = Math.max(d.documentElement.scrollHeight, d.body ? d.body.scrollHeight : 0);
              if (real > 200 && Math.abs(real - c.h) > 8) { c.h = real; layout(); }
            }
          } catch (e) { /* cross-origin (file://): keep the height baked in at build time */ }
        });
      });
    });

    document.body.classList.add('pdfmode');
    window.scrollTo(0, 0);

    back.addEventListener('click', function () {
      document.body.classList.remove('pdfmode');
      root.innerHTML = '';
    });
    printBtn.addEventListener('click', function () { window.print(); });

    loadFrames(frames, function (done, all) {
      status.textContent = 'Hazırlanıyor… ' + done + ' / ' + all;
    }, function () {
      status.textContent = items.length + ' sayfa hazır · ' + paper.toUpperCase() + ' yatay';
      printBtn.disabled = false;
      setTimeout(function () { window.print(); }, 600);
    });
  }

  function loadFrames(frames, onProgress, done) {
    var i = 0, active = 0, finished = 0, CONC = 4;
    if (!frames.length) { done(); return; }
    function start() {
      while (active < CONC && i < frames.length) {
        (function (f) {
          active++;
          var settled = false;
          var timer = setTimeout(settle, 15000);
          function settle() {
            if (settled) return;
            settled = true;
            clearTimeout(timer);
            f.removeEventListener('load', settle);
            active--; finished++;
            onProgress(finished, frames.length);
            if (finished === frames.length) { done(); } else { start(); }
          }
          f.addEventListener('load', settle);
          f.src = f.getAttribute('data-src');
        })(frames[i++]);
      }
    }
    start();
  }

  refresh();
})();
"""

PDF_WIDTHS = (1440, 768, 390)
FALLBACK_H = {1440: 2400, 768: 3200, 390: 4600}

# Viewport heights the measuring frames use, so a study sized in vh resolves against a
# realistic screen rather than against an arbitrary probe height.
VIEWPORT_H = {1440: 900, 768: 1024, 390: 844}

# Bumped when the measuring method changes, so cached numbers taken the old way are retaken.
MEASURE_VERSION = 2

CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
)

MEASURE_HEAD = """<!doctype html>
<meta charset="utf-8">
<title>height measurement</title>
<body style="margin:0">
<pre id="out">PENDING</pre>
"""

# Every iframe is in the static markup on purpose: a document's load event waits for its
# frames, so measuring on window load means the numbers are in the DOM before Chrome dumps
# it. Creating the frames from script instead needs --virtual-time-budget, which turns one
# quick run into a stall.
MEASURE_TAIL = """<script>
window.addEventListener('load', function () {
  var rows = {};
  Array.prototype.forEach.call(document.querySelectorAll('iframe'), function (f) {
    var i = f.getAttribute('data-i'), w = f.getAttribute('data-w');
    var vh = parseInt(f.getAttribute('data-vh'), 10) || 0, h = 0;
    try {
      var d = f.contentDocument, de = d.documentElement, b = d.body;
      // scrollHeight can never report less than the viewport, so it is right for a study
      // taller than the frame and wrong for a short one. Below the frame height the body's
      // own box is the real extent — that is what keeps a breadcrumb from claiming 300px.
      var sh = Math.max(de ? de.scrollHeight : 0, b ? b.scrollHeight : 0);
      if (sh > vh) {
        h = sh;
      } else if (b) {
        var r = b.getBoundingClientRect();
        var mb = parseFloat(getComputedStyle(b).marginBottom) || 0;
        h = Math.ceil(r.bottom + mb);
      } else {
        h = sh;
      }
      if (!isFinite(h) || h <= 0) { h = sh; }
    } catch (e) { h = 0; }
    rows[i] = rows[i] || [];
    rows[i].push(w + ':' + h);
  });
  var lines = Object.keys(rows).map(function (i) { return 'ROW ' + i + ' ' + rows[i].join(' '); });
  document.getElementById('out').textContent = 'BEGIN ' + lines.join(' ; ') + ' END';
});
</script>
</body>
"""

# Startup work a measurement run has no use for. Without these a run can stall on
# component updates or background network calls.
CHROME_FLAGS = (
    "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
    "--allow-file-access-from-files", "--disable-background-networking",
    "--disable-component-update", "--disable-client-side-phishing-detection",
    "--disable-default-apps", "--disable-extensions", "--disable-sync", "--no-pings",
    "--mute-audio", "--metrics-recording-only", "--disable-crash-reporter",
    "--disable-breakpad", "--disable-search-engine-choice-screen",
    "--disable-features=Translate,MediaRouter,OptimizationHints,BackForwardCache",
    "--window-size=1600,900",
)

CHUNK = 12          # studies per browser run
MEASURE_TIMEOUT = 180
PDF_TIMEOUT = 900

# A run that fails takes its whole group with it, so the group is retried smaller and
# finally one at a time. A study that fails alone is a real failure, not a crowded run.
MEASURE_PASSES = (CHUNK, 4, 1)


def find_chrome():
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    for name in ("google-chrome", "chromium", "chromium-browser"):
        found = subprocess.run(["which", name], capture_output=True, text=True).stdout.strip()
        if found:
            return found
    return None


def load_cache():
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return {}


def measure_chunk(chrome, files, workdir):
    """Measure a group of studies in one browser run. Returns {index: {width: height}}."""
    parts = [MEASURE_HEAD]
    for i, f in enumerate(files):
        for w in PDF_WIDTHS:
            parts.append(
                '<iframe data-i="%d" data-w="%d" data-vh="%d" src="%s" '
                'style="border:0;display:block;width:%dpx;height:%dpx"></iframe>\n'
                % (i, w, VIEWPORT_H[w], html.escape(f.as_uri(), quote=True), w, VIEWPORT_H[w]))
    parts.append(MEASURE_TAIL)

    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "measure.html"
        page.write_text("".join(parts), encoding="utf-8")
        dump = Path(tmp) / "dump.html"
        # --dump-dom writes the DOM as soon as the page has loaded, but the browser it was
        # launched from does not reliably exit afterwards: Chrome's updater keeps the run
        # alive, so waiting for the process to finish is waiting for nothing. Watch the dump
        # for the marker instead and stop the browser we started as soon as it appears.
        try:
            with dump.open("w", encoding="utf-8") as fh:
                proc = subprocess.Popen(
                    [chrome, *CHROME_FLAGS, "--user-data-dir=%s" % workdir,
                     "--dump-dom", page.as_uri()],
                    stdout=fh, stderr=subprocess.DEVNULL)
        except OSError:
            return {}
        out = ""
        deadline = time.time() + MEASURE_TIMEOUT
        try:
            while time.time() < deadline:
                out = dump.read_text(encoding="utf-8", errors="ignore")
                if "BEGIN " in out and " END" in out:
                    break
                if proc.poll() is not None:
                    out = dump.read_text(encoding="utf-8", errors="ignore")
                    break
                time.sleep(0.2)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=5)

    m = re.search(r"BEGIN (.*?) END", out, re.S)
    if not m:
        return {}
    rows = {}
    for row in m.group(1).split(";"):
        parts = row.split()
        if len(parts) < 2 or parts[0] != "ROW":
            continue
        idx = int(parts[1])
        heights = {}
        for pair in parts[2:]:
            w, _, h = pair.partition(":")
            if w.isdigit() and h.isdigit() and int(h) > 0:
                heights[int(w)] = int(h)
        if len(heights) == len(PDF_WIDTHS):
            rows[idx] = heights
    return rows


def measure_all(studies, quiet=False):
    """Fill each study's 'heights' from the cache, measuring what has changed.

    Studies that a browser run fails to return are retried in smaller runs and finally
    one at a time, so a single bad run cannot leave a study on a default height. Anything
    still unmeasured after the last pass keeps its default and is reported; the next build
    retries it.

    Measurement only reads the study files — each is loaded into an iframe from its own
    file:// URI — and writes nothing but review/.heights.json.
    """
    cache = load_cache()
    stale = []
    for st in studies:
        rel = st["file"].relative_to(ROOT).as_posix()
        digest = hashlib.sha1(st["file"].read_bytes()).hexdigest()[:16]
        st["_rel"], st["_sha"] = rel, digest
        hit = cache.get(rel)
        if hit and hit.get("sha") == digest and hit.get("v") == MEASURE_VERSION:
            st["heights"] = {int(k): v for k, v in hit["h"].items()}
        else:
            stale.append(st)

    if stale:
        chrome = find_chrome()
        if not chrome:
            if not quiet:
                print("  no Chrome found — using default heights for %d study(ies)" % len(stale))
        else:
            if not quiet:
                print("  measuring %d study(ies)…" % len(stale))
            pending, ok = list(stale), 0
            with tempfile.TemporaryDirectory() as tmp:
                for attempt, size in enumerate(MEASURE_PASSES):
                    if not pending:
                        break
                    if not quiet and attempt:
                        print("  retry pass %d: %d study(ies), %d per run…"
                              % (attempt, len(pending), size), flush=True)
                    missed = []
                    for n in range(0, len(pending), size):
                        group = pending[n:n + size]
                        rows = measure_chunk(chrome, [g["file"] for g in group],
                                             Path(tmp) / ("p%d-%d" % (attempt, n)))
                        for idx, st in enumerate(group):
                            heights = rows.get(idx)
                            if heights:
                                st["heights"] = heights
                                cache[st["_rel"]] = {"sha": st["_sha"], "v": MEASURE_VERSION,
                                                     "h": {str(k): v for k, v in heights.items()}}
                                ok += 1
                            else:
                                missed.append(st)
                        if not quiet:
                            print("    %d/%d measured" % (ok, len(stale)), flush=True)
                    # Persisted after every pass so an interrupted run keeps its progress.
                    CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True), encoding="utf-8")
                    pending = missed
            if not quiet and pending:
                print("  %d study(ies) unmeasured after %d passes — they keep default heights:"
                      % (len(pending), len(MEASURE_PASSES)))
                for st in pending:
                    print("    %s" % st["_rel"])

    for st in studies:
        st.setdefault("heights", dict(FALLBACK_H))
        for w in PDF_WIDTHS:
            if not st["heights"].get(w):
                st["heights"][w] = FALLBACK_H[w]



# --- Printed contact sheet ------------------------------------------------
# The page's own PDF button is the interactive route: it builds the same pages in the
# browser from the same measured heights and hands them to the print dialog. This is the
# batch route for the whole sector, and it exists because that dialog needs a person.
# Every frame is in the static markup, so the document's load event waits for all of
# them and Chrome can print without a virtual clock.

PDF_PAPER = {"a3": (420, 297), "a4": (297, 210)}   # mm, landscape
PDF_MARGIN_MM = 8
PDF_GAP = 14                                        # px between device columns
PDF_HEAD_H = 48                                     # px reserved for the page header
PDF_LABELS = ("Desktop", "Tablet", "Phone")

PRINT_CSS = """
@page { size: %(paper)s landscape; margin: %(margin)dmm; }
html, body { margin: 0; background: #fff; color: #111214;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
.pdfpage { position: relative; margin: 0; padding: 0; background: #fff; overflow: hidden;
  break-after: page; page-break-after: always; }
.pdfpage:last-child { break-after: auto; page-break-after: auto; }
.pdfpage__head { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap;
  height: 26px; padding: 0 2px; border-bottom: 1px solid #d9d9d6;
  font-size: 10px; letter-spacing: 0.02em; }
.pdfpage__head b { font-size: 11px; letter-spacing: 0.06em; }
.pdfpage__head span { color: #5b5e63; }
.pdfpage__head .sec { margin-left: auto; color: #5b5e63; }
.pdfrow { display: flex; align-items: flex-start; gap: %(gap)dpx; padding-top: 8px; }
.pdfdev__cap { margin: 0 0 4px; font-size: 8px; letter-spacing: 0.14em;
  text-transform: uppercase; color: #5b5e63; }
.pdfhold { position: relative; overflow: hidden; border: 1px solid #d9d9d6; background: #fff; }
.pdfhold iframe { position: absolute; top: 0; left: 0; border: 0; transform-origin: top left; }
"""


def mm_px(v):
    return v * 96 / 25.4


def print_view(studies, paper="a3"):
    """Build the standalone print page: one landscape page per study, three widths side by side."""
    w_mm, h_mm = PDF_PAPER[paper]
    avail_w = mm_px(w_mm - 2 * PDF_MARGIN_MM)
    avail_h = mm_px(h_mm - 2 * PDF_MARGIN_MM)
    content_h = avail_h - PDF_HEAD_H

    out = ["<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n",
           "<title>Architecture &amp; Interior Design — contact sheet</title>\n<style>",
           PRINT_CSS % {"paper": paper.upper(), "margin": PDF_MARGIN_MM, "gap": PDF_GAP},
           "</style>\n</head>\n<body>\n"]

    for st in studies:
        heights = [st["heights"][w] for w in PDF_WIDTHS]
        # Scale each column so the whole study fits the page height, then, if the three
        # scaled columns are wider than the page, shrink them together until they fit.
        scales = [min(1.0, content_h / float(h)) for h in heights]
        gaps = PDF_GAP * (len(PDF_WIDTHS) - 1)
        total = sum(w * s for w, s in zip(PDF_WIDTHS, scales))
        if total + gaps > avail_w:
            k = (avail_w - gaps) / total
            scales = [s * k for s in scales]

        out.append('<section class="pdfpage" style="width:%dpx;height:%dpx">\n'
                   % (round(avail_w), round(avail_h)))
        out.append('<div class="pdfpage__head"><b>%s</b><span>%s</span>'
                   '<span class="sec">%s &#183; %s</span></div>\n'
                   % (esc(st["id"]), esc(st.get("territory", "")),
                      esc(st["section_id"]), esc(st["section_name"])))
        out.append('<div class="pdfrow">\n')
        for i, w in enumerate(PDF_WIDTHS):
            h, sc = heights[i], scales[i]
            out.append(
                '<div class="pdfdev"><p class="pdfdev__cap">%s %d &#183; %dpx</p>'
                '<div class="pdfhold" style="width:%dpx;height:%dpx">'
                '<iframe src="%s" title="%s" scrolling="no" tabindex="-1" loading="eager" '
                'style="width:%dpx;height:%dpx;transform:scale(%.4f)"></iframe>'
                '</div></div>\n'
                % (PDF_LABELS[i], w, h, round(w * sc), round(h * sc),
                   esc(st["file"].as_uri()), esc("%s %s" % (st["id"], PDF_LABELS[i])),
                   w, h, sc))
        out.append('</div>\n</section>\n')

    out.append("</body>\n</html>\n")
    return "".join(out)


def render_pdf(studies, dest, paper="a3", quiet=False):
    """Print the contact sheet with headless Chrome. Returns True on success."""
    chrome = find_chrome()
    if not chrome:
        print("  no Chrome found — cannot print the contact sheet")
        return False
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "print-view.html"
        page.write_text(print_view(studies, paper), encoding="utf-8")
        if dest.exists():
            dest.unlink()
        cmd = [chrome, *CHROME_FLAGS, "--user-data-dir=%s" % (Path(tmp) / "udd"),
               "--no-pdf-header-footer", "--print-to-pdf-no-header",
               "--print-to-pdf=%s" % dest, page.as_uri()]
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError:
            return False
        # Chrome does not reliably exit once it has written the file, so wait for the file
        # to appear and stop growing instead of waiting for the process.
        deadline = time.time() + PDF_TIMEOUT
        last, stable = -1, 0
        try:
            while time.time() < deadline:
                size = dest.stat().st_size if dest.exists() else 0
                if size and size == last:
                    stable += 1
                    if stable >= 6:
                        break
                else:
                    stable = 0
                last = size
                if proc.poll() is not None and dest.exists():
                    break
                time.sleep(0.5)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=5)
    return dest.exists() and dest.stat().st_size > 0


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
                "section_id": section_dir.name.split("-")[0],
                "section_name": section_name(section_dir),
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

    data = []
    for s in sections:
        for st in s["studies"]:
            data.append({
                "id": st["id"],
                "sec": s["id"],
                "secName": s["name"],
                "terr": st["territory"] or "",
                "rel": "../" + st["file"].relative_to(ROOT).as_posix(),
                "h": [st["heights"][w] for w in PDF_WIDTHS],
            })

    return TEMPLATE.format(
        sector=esc(sector_label),
        total=total,
        sections=len(sections),
        nav=nav,
        blocks="\n\n".join(blocks),
        pdf_css=PDF_CSS,
        pdf_js=PDF_JS,
        data_json=json.dumps({"widths": list(PDF_WIDTHS), "studies": data},
                             separators=(",", ":")).replace("</", "<\\/"),
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
{pdf_css}
</style>
<style id="pdf-pagesize">@page {{ size: A3 landscape; margin: 8mm; }}</style>
</head>

<body>

<header class="masthead">
  <div class="shell">
    <div class="masthead__row">
      <div>
        <h1>{sector} &#183; review contact sheet</h1>
        <p class="count">{total} studies across {sections} sections &#183; live previews, two columns</p>
      </div>
      <div class="tools">
        <div class="widths" role="group" aria-label="Preview viewport width">
          <button type="button" data-w="1440" data-h="900" aria-pressed="true">Desktop 1440</button>
          <button type="button" data-w="768" data-h="1000" aria-pressed="false">Tablet 768</button>
          <button type="button" data-w="390" data-h="844" aria-pressed="false">Phone 390</button>
        </div>
        <button type="button" class="pdfbtn" id="pdfopen">PDF üret</button>
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

<dialog class="pickr" id="pickr" aria-labelledby="pickr-h">
  <div class="pickr__form">
    <div class="pickr__head">
      <h2 id="pickr-h">PDF üret</h2>
      <p>
        Seçilen her tasarım için bir yatay sayfa: solda desktop, ortada tablet, sağda telefon
        genişliği yan yana. Hazırlandığında tarayıcının yazdırma penceresi açılır &#8212; oradan
        <b>PDF olarak kaydet</b> seçilir.
      </p>
    </div>

    <div class="pickr__opts">
      <fieldset>
        <legend>Kağıt</legend>
        <label><input type="radio" name="paper" value="a3" checked> A3 yatay</label>
        <label><input type="radio" name="paper" value="a4"> A4 yatay</label>
      </fieldset>
      <fieldset>
        <legend>Cihaz görünümleri</legend>
        <label><input type="checkbox" name="dev" value="0" checked> Desktop 1440</label>
        <label><input type="checkbox" name="dev" value="1" checked> Tablet 768</label>
        <label><input type="checkbox" name="dev" value="2" checked> Telefon 390</label>
      </fieldset>
      <div class="pickr__bulk">
        <button type="button" id="pickr-all">Tümünü seç</button>
        <button type="button" id="pickr-none">Temizle</button>
      </div>
    </div>

    <div class="pickr__list" id="pickr-list"></div>

    <div class="pickr__foot">
      <p class="pickr__count" id="pickr-count"></p>
      <button type="button" id="pickr-close">Kapat</button>
      <button type="button" class="go" id="pickr-go">Sayfaları hazırla</button>
      <p class="pickr__warn" id="pickr-warn"></p>
    </div>
  </div>
</dialog>

<div id="pdfroot"></div>

<script id="pdf-data" type="application/json">{data_json}</script>
<script>
{pdf_js}
</script>
</body>
</html>
"""


def main():
    sector_dir = SECTORS / "architecture-interior-design"
    sections = collect(sector_dir)

    studies = [st for s in sections for st in s["studies"]]
    if "--no-measure" in sys.argv:
        cache = load_cache()
        for st in studies:
            hit = cache.get(st["file"].relative_to(ROOT).as_posix())
            st["heights"] = {int(k): v for k, v in hit["h"].items()} if hit else dict(FALLBACK_H)
            for w in PDF_WIDTHS:
                st["heights"].setdefault(w, FALLBACK_H[w])
    else:
        measure_all(studies)

    OUT.write_text(render(sections, "Architecture & Interior Design"), encoding="utf-8")
    total = sum(len(s["studies"]) for s in sections)
    print("wrote %s" % OUT.relative_to(ROOT))

    if "--pdf" in sys.argv:
        print("printing %d studies to %s…" % (len(studies), PDF_OUT.relative_to(ROOT)), flush=True)
        if render_pdf(studies, PDF_OUT):
            print("wrote %s (%.1f MB)" % (PDF_OUT.relative_to(ROOT),
                                          PDF_OUT.stat().st_size / 1048576.0))
        else:
            print("  contact sheet not written")
    for s in sections:
        print("  %s %-28s %d studies" % (s["id"], s["name"], len(s["studies"])))
    print("  total: %d studies across %d sections" % (total, len(sections)))


if __name__ == "__main__":
    main()
