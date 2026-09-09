// Structural collision check across a sector's studies.
//
//   node review/check-composition-collisions.js [sector-directory-name]
//
// Why this exists: CONSULTING-THEME-CONTRACT.md says two studies at the same variant that share a
// layout fail the contract as surely as two that share no palette. That rule was being checked by
// eye across thirty-five studies, and it failed — CONS-S07-002 was authored as a near-copy of
// CONS-S05-002 (statement, offset voice, wide plate, one-column numbered blocks, second plate,
// underlined link). Reading a section against the two above it is not enough once a sector is
// several sections deep; the comparison has to be mechanical.
//
// It builds a structural fingerprint per study and reports studies at the SAME VARIANT whose
// fingerprints are identical or near-identical. A collision is not automatically a defect — two
// sections may legitimately share a simple shape — but every collision has to be looked at.

const fs = require('fs');
const path = require('path');

const SECTOR = process.argv[2] || 'consulting-b2b-professional-services';
const ROOT = path.join(__dirname, '..', 'sectors', SECTOR);

// --- helpers ---------------------------------------------------------------

function styleOf(src) {
  const m = src.match(/<style>([\s\S]*?)<\/style>/);
  return m ? m[1] : '';
}

function ruleBody(css, cls) {
  // find the declaration block for a scoped rule ending in `.cls`
  const idx = css.indexOf(' .' + cls + ' {');
  if (idx === -1) return '';
  const open = css.indexOf('{', idx);
  const close = css.indexOf('}', open);
  return close === -1 ? '' : css.slice(open + 1, close);
}

function columnCount(css, cls) {
  const body = ruleBody(css, cls);
  const m = body.match(/grid-template-columns:\s*([^;]+);/);
  if (!m) return body.includes('display: flex') ? 'flex' : '1';
  const v = m[1];
  const rep = v.match(/repeat\((\d+)/);
  if (rep) return rep[1];
  const parts = v.split(')').filter(p => /minmax|fr|auto|px/.test(p));
  return String(parts.length || 1);
}

// Where does the media sit inside a repeated item?
function mediaPlacement(css, body) {
  if (!/class="(shot|plate|artefact|banner|anchor|numplate)/.test(body)) return 'none';
  const shot = ruleBody(css, 'shot') || ruleBody(css, 'plate');
  if (/border-radius: *999px/.test(shot)) return 'circle';
  if (/position: absolute/.test(css) && /class="scrim"/.test(body)) return 'behind';
  // media before or after the text inside a card?
  const item = body.match(/<li>[\s\S]*?<\/li>/);
  if (item) {
    const t = item[0];
    const iShot = t.search(/class="(shot|plate|numplate)/);
    const iText = t.search(/<h3|class="(sit|bind|what)/);
    if (iShot !== -1 && iText !== -1) return iShot < iText ? 'itemTop' : 'itemFoot';
  }
  return 'band';
}

function fingerprint(file) {
  const src = fs.readFileSync(file, 'utf8').replace(/<!--[\s\S]*?-->/g, '');
  const css = styleOf(src);
  // Page-level studies (S23-S27) use <article class="shell">; section studies use <section>.
  // Matching only <section> made every page study fingerprint as an empty sequence, which the
  // near-match scorer then read as a 100% match between any two of them.
  const shell = (src.match(/<(section|article) class="shell"[^>]*>([\s\S]*?)<\/\1>/) || ['', '', ''])[2];

  // Some studies wrap their whole body in a single structural wrapper (<div class="col">, "page").
  // Scanning only the first indentation level then yields a degenerate 1-2 token sequence, and the
  // near-match scorer reads two degenerate sequences as a 100% match. When the top level is that
  // thin, scan one level deeper instead. Studies with a real top-level sequence are unaffected.
  const topLevel = (shell.match(/^ {4}<(?:div|ul|ol|p)\s+class="/gm) || []).length;
  const indent = topLevel < 3 && /^ {6}<(?:div|ul|ol|p)\s+class="/m.test(shell) ? 6 : 4;

  const seq = [];
  const re = new RegExp('^ {' + indent + '}<(div|ul|ol|p)\\s+class="([^"]+)"', 'gm');
  let m;
  while ((m = re.exec(shell))) {
    const tag = m[1];
    const cls = m[2].split(' ')[0];
    if (cls === 'head') seq.push('HEAD' + (/grid-template-columns/.test(ruleBody(css, 'head')) ? '2' : '1'));
    else if (cls === 'eyebrow') seq.push('HEAD1');
    else if (cls === 'second') seq.push('VOICE');
    else if (/^(shot|plate|artefact|banner|anchor)/.test(cls)) seq.push('MEDIA');
    else if (/^(coda|foot)$/.test(cls)) seq.push('FOOT');
    else if (/argue|challenge|claim|panel|close|band|pull|action/.test(cls)) seq.push('PANEL');
    else if (tag === 'ul' || tag === 'ol' || /body|bays|bento|stages|modules|spread|credits|fields|markets|people|cases|routes|grid|rail|gallery|panels|index|pairs|cards|lines/.test(cls))
      seq.push('LIST' + columnCount(css, cls));
    else seq.push(cls.toUpperCase().slice(0, 6));
  }

  const dev = [];
  if (/scroll-snap-type/.test(css)) dev.push('rail');
  if (/position: sticky/.test(css)) dev.push('sticky');
  if (/margin[^:]*: *-\d/.test(css)) dev.push('overlap');
  if (/linear-gradient\(to top/.test(css)) dev.push('scrim');
  if (/grid-row: span/.test(css)) dev.push('bento');
  if (/nth-child\(even\)/.test(css)) dev.push('alternate');
  if (/columns: *[2-9]/.test(css)) dev.push('masonry');
  if (css.indexOf("first-child { grid-column: 1 / -1") !== -1 || css.indexOf("first-child { grid-column: span") !== -1) dev.push('featured');

  return {
    seq: seq.join('>'),
    media: mediaPlacement(css, shell),
    dev: dev.sort().join('+') || '-'
  };
}

// --- run -------------------------------------------------------------------

const secs = fs.readdirSync(ROOT)
  .filter(d => /^S\d\d-/.test(d))
  .sort()
  .filter(d => {
    const raw = path.join(ROOT, d, 'raw');
    return fs.existsSync(raw) && fs.readdirSync(raw).some(f => f.endsWith('.html'));
  });

const byVariant = {};
for (const d of secs) {
  for (const v of ['001', '002', '003', '004', '005']) {
    const id = d.slice(0, 3);
    const f = path.join(ROOT, d, 'raw', 'CONS-' + id + '-' + v + '.html');
    if (!fs.existsSync(f)) continue;
    (byVariant[v] = byVariant[v] || []).push(Object.assign({ sec: id }, fingerprint(f)));
  }
}

let clashes = 0, near = 0;
console.log('COMPOSITION COLLISION CHECK — ' + SECTOR + '\n');
for (const v of Object.keys(byVariant).sort()) {
  console.log('--- variant ' + v + ' ---');
  for (const r of byVariant[v]) {
    console.log('  ' + r.sec + '  ' + r.seq.padEnd(40) + r.media.padEnd(9) + r.dev);
  }
  const seen = {};
  for (const r of byVariant[v]) {
    const key = r.seq + '|' + r.media + '|' + r.dev;
    if (seen[key]) { clashes++; console.log('  !! COLLISION: ' + seen[key] + ' and ' + r.sec); }
    else seen[key] = r.sec;
  }

  // Near matches. Exact equality is not enough: CONS-S07-002 differed from CONS-S05-002 by one
  // token and was the same composition. Anything above the threshold has to be looked at.
  const rows = byVariant[v];
  for (let i = 0; i < rows.length; i++) {
    for (let j = i + 1; j < rows.length; j++) {
      const a = rows[i], b = rows[j];
      if (a.seq === b.seq && a.media === b.media && a.dev === b.dev) continue;
      const ta = a.seq.split('>'), tb = b.seq.split('>');
      const pool = tb.slice();
      let common = 0;
      for (const t of ta) { const k = pool.indexOf(t); if (k !== -1) { common++; pool.splice(k, 1); } }
      const sim = (2 * common) / (ta.length + tb.length);
      if (sim >= 0.8) {
        near++;
        console.log('  ~~ NEAR MATCH (' + Math.round(sim * 100) + '%): ' + a.sec + ' and ' + b.sec);
      }
    }
  }
  console.log('');
}
console.log((clashes === 0 ? 'NO EXACT COLLISIONS' : clashes + ' EXACT COLLISION(S)') + ' · ' + (near === 0 ? 'no near matches' : near + ' near match(es) to review'));
