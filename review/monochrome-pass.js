// MONOCHROME PASS — SUPERSEDED. DO NOT RE-RUN ON construction-contractors.
//
// This pass removed all colour from the sector. The sector direction requires one
// high-visibility accent, and CONSTRUCTION-THEME-CONTRACT.md now assigns one per theme, so
// re-running this would destroy the accents of every reworked study. It is kept for reference
// and for sectors that have not been themed. The guard below makes the destructive case explicit.
//
// Monochrome pass — black and white only.
//
// Desaturating a colour palette produces mud: three hues of the same lightness become
// three identical greys. So this is not a conversion, it is a re-grading. Every study's
// palette is re-laid on a ten-step black-to-white ramp in its original order, so tones
// that used to differ by hue now differ by value, which is the only thing left.
//
// Markup, content and layout are untouched.

const fs = require('fs');
const path = require('path');

const ROOT = process.argv[3] ||
  path.join(__dirname, '..', 'sectors', 'construction-contractors');
const ONLY = process.argv[2] || '';
if (/construction-contractors/.test(ROOT) && !process.env.ALLOW_MONOCHROME_RERUN) {
  console.error('Refusing to run: construction-contractors is on CONSTRUCTION-THEME-CONTRACT.md,');
  console.error('which assigns a chromatic accent per theme. This pass would delete those accents.');
  console.error('Set ALLOW_MONOCHROME_RERUN=1 only if you intend exactly that.');
  process.exit(1);
}

// ---------- greyscale ----------
const toLin = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
const toSrgb = v => Math.round(255 * (v <= 0.0031308 ? v * 12.92 : 1.055 * v ** (1 / 2.4) - 0.055));
function greyValue(r, g, b) {
  const y = 0.2126 * toLin(r) + 0.7152 * toLin(g) + 0.0722 * toLin(b);
  return Math.max(0, Math.min(255, toSrgb(y)));
}
const hh = n => n.toString(16).padStart(2, '0');
const greyHex = n => '#' + hh(n) + hh(n) + hh(n);
function hexGrey(hex) {
  let h = hex.slice(1);
  if (h.length === 3) h = h.split('').map(c => c + c).join('');
  if (h.length !== 6) return null;
  return greyValue(parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16));
}

// the ramp: ten steps, black to white
const RAMP = [17, 43, 68, 94, 122, 150, 180, 210, 236, 255];
const rampHex = i => greyHex(RAMP[Math.max(0, Math.min(RAMP.length - 1, i))]);
const nearestRamp = v => {
  let best = 0;
  for (let i = 1; i < RAMP.length; i++) if (Math.abs(RAMP[i] - v) < Math.abs(RAMP[best] - v)) best = i;
  return best;
};

// ---------- files ----------
const files = [];
for (const s of fs.readdirSync(ROOT).filter(d => /^S\d\d-/.test(d)).sort()) {
  if (ONLY && !s.startsWith(ONLY)) continue;
  const dir = path.join(ROOT, s, 'raw');
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.html'))) files.push(path.join(dir, f));
}

// ---------- grounds ----------
// White paper or black paper, nothing muddy in between. Four light steps, spaced far
// enough apart to tell one study from the next on a contact sheet; one black.
const LIGHT_STEPS = [250, 241, 232, 223, 214];
const groundFor = {};
const bySection = {};
for (const f of files) {
  const src = fs.readFileSync(f, 'utf8');
  const g = (src.match(/body \{ margin: 0; background: (#[0-9a-f]{6}); \}/) || [])[1];
  if (!g) continue;
  const sec = path.basename(path.dirname(path.dirname(f)));
  (bySection[sec] = bySection[sec] || []).push({ f, g, grey: hexGrey(g) });
}
for (const sec of Object.keys(bySection)) {
  const items = bySection[sec];
  const darks = items.filter(i => i.grey < 70).sort((a, b) => a.grey - b.grey);
  const lights = items.filter(i => i.grey >= 70).sort((a, b) => b.grey - a.grey);
  darks.forEach((it, i) => { groundFor[it.f] = { from: it.g, to: greyHex(14 + i * 12), dark: true }; });
  lights.forEach((it, r) => {
    groundFor[it.f] = { from: it.g, to: greyHex(LIGHT_STEPS[r % LIGHT_STEPS.length]), dark: false };
  });
}

// ---------- the pass ----------
const HUES = { orange: 'a', red: 'b', green: 'c', blue: 'd', amber: 'e', gold: 'f',
  teal: 'g', navy: 'h', purple: 'i', pink: 'j', yellow: 'k', cyan: 'l', rust: 'm' };

let done = 0;
for (const f of files) {
  const src = fs.readFileSync(f, 'utf8');
  const m = src.match(/<style>([\s\S]*?)<\/style>/);
  if (!m) continue;
  if (/monochrome: hand-graded/.test(src)) continue;   // graded by hand, leave it alone
  let css = m[1];
  const gm = groundFor[f] || { to: '#f5f5f5', dark: false };

  // 1. every colour becomes a grey
  css = css.replace(/#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b/g, x => { const v = hexGrey(x); return v === null ? x : greyHex(v); });
  css = css.replace(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)/g,
    (x, r, g, b, a) => { const v = greyValue(+r, +g, +b);
      return a === undefined ? `rgb(${v}, ${v}, ${v})` : `rgba(${v}, ${v}, ${v}, ${a})`; });

  // 2. re-grade the study's own palette onto the ramp, in its original order,
  //    so tones that used to differ by hue now differ by value
  const rootRe = new RegExp(`\\.con-s\\d\\d-\\d\\d\\d \\{([\\s\\S]*?)\\n\\}`);
  const rootM = css.match(rootRe);
  if (rootM) {
    const vars = [...rootM[1].matchAll(/(--[a-z0-9-]+):\s*(#[0-9a-f]{6});/g)]
      .map(x => ({ name: x[1], hex: x[2], v: hexGrey(x[2]) }))
      .filter(x => x.name !== '--paper');
    const uniq = [...new Set(vars.map(x => x.v))].sort((a, b) => a - b);
    if (uniq.length > 1) {
      const map = {};
      uniq.forEach((v, i) => {
        const step = Math.round(i * (RAMP.length - 1) / (uniq.length - 1));
        map[v] = rampHex(step);
      });
      for (const v of uniq) css = css.split(greyHex(v)).join(map[v]);
    }
  }

  // 2b. blocks that used to be told apart by hue are told apart by value instead:
  //     every mid-tone panel background is pushed onto a wide four-step ladder.
  const BLOCK_LADDER = ['#0f0f0f', '#2e2e2e', '#4d4d4d', '#6c6c6c', '#8b8b8b'];
  const blockVars = new Set();
  for (const r of css.matchAll(/\{([^{}]*)\}/g)) {
    const b = r[1];
    if (!/padding:|border-radius:/.test(b)) continue;
    for (const v of b.matchAll(/background:\s*var\((--[a-z0-9-]+)\)/g)) blockVars.add(v[1]);
    for (const v of b.matchAll(/background:\s*var\((--[a-z0-9-]+),/g)) blockVars.add(v[1]);
  }
  // the catalog routes block colours through a --tone indirection, so follow one hop
  for (const name of [...blockVars]) {
    for (const hop of css.matchAll(new RegExp(`${name}:\\s*var\\((--[a-z0-9-]+)\\)`, 'g'))) {
      blockVars.add(hop[1]);
    }
  }
  const blocks = [...blockVars]
    .map(name => {
      const d = css.match(new RegExp(`${name}:\\s*(#[0-9a-f]{6})`));
      return d ? { name, hex: d[1], v: hexGrey(d[1]) } : null;
    })
    .filter(x => x && x.v >= 40 && x.v <= 235 && !/card|paper|fill|surface|line|ink|edge|rule/.test(x.name))
    .sort((a, b) => a.v - b.v);
  if (blocks.length > 1) {
    blocks.forEach((blk, i) => {
      const step = BLOCK_LADDER[Math.min(i, BLOCK_LADDER.length - 1)];
      css = css.replace(new RegExp(`(${blk.name}:\\s*)#[0-9a-f]{6}`), `$1${step}`);
    });
  }

  // 3. any remaining literal grey snaps to the ramp, so the whole sector shares one scale
  css = css.replace(/#([0-9a-f]{2})\1\1\b/g, (x, p) => rampHex(nearestRamp(parseInt(p, 16))));

  // 4. the ground is assigned, not derived: white paper or black paper
  css = css.replace(/(body \{ margin: 0; background: )#[0-9a-f]{6}( \}\;?)?/, `$1${gm.to}$2`);
  css = css.replace(/body \{ margin: 0; background: #[0-9a-f]{6}; \}/, `body { margin: 0; background: ${gm.to}; }`);
  css = css.replace(/(--paper:\s*)#[0-9a-f]{6}/, `$1${gm.to}`);
  css = css.replace(/(\.con-s\d\d-\d\d\d \{[\s\S]*?background: linear-gradient\(180deg, )#[0-9a-f]{6}( 0%, )#[0-9a-f]{6}( 30%\))/,
    `$1${gm.dark ? greyHex(Math.min(255, parseInt(gm.to.slice(1, 3), 16) + 10)) : greyHex(Math.max(0, parseInt(gm.to.slice(1, 3), 16) - 8))}$2${gm.to}$3`);

  // 5. the hero is the one solid black on the page, and it is black on every study
  css = css.replace(/background: linear-gradient\(135deg, #[0-9a-f]{6} 0%, #[0-9a-f]{6} 58%, #[0-9a-f]{6} 100%\)/g,
    'background: linear-gradient(135deg, #2b2b2b 0%, #141414 58%, #000000 100%)');
  if (gm.dark) {
    css = css.replace(/(border-radius: 34px;\n\s*border: none;)/g, 'border-radius: 34px;\n  border: 1px solid #444444;');
  }

  // 5b. contrast guard. Hue used to do some of the separating; with it gone, a light
  //     panel can end up under white type. Resolve one level of variable and push any
  //     pair that lands closer than ninety levels apart.
  const varMap = {};
  for (const d of css.matchAll(/(--[a-z0-9-]+):\s*(#[0-9a-f]{6});/g)) varMap[d[1]] = d[2];
  const resolve = raw => {
    if (!raw) return null;
    const lit = raw.match(/#([0-9a-f]{6})/);
    if (lit) return parseInt(lit[1].slice(0, 2), 16);
    const v = raw.match(/var\((--[a-z0-9-]+)/);
    if (v && varMap[v[1]]) return parseInt(varMap[v[1]].slice(1, 3), 16);
    return null;
  };
  css = css.replace(/\{([^{}]*)\}/g, (whole, b) => {
    const colM = b.match(/(?:^|;|\n)\s*color:\s*([^;]+);/);
    const bgM = b.match(/background(?:-color)?:\s*(#[0-9a-f]{6}|var\(--[a-z0-9-]+\));/);
    if (!colM || !bgM) return whole;
    const c = resolve(colM[1]), g = resolve(bgM[1]);
    if (c === null || g === null || Math.abs(c - g) >= 90) return whole;
    const fixed = c > 127 ? '#3a3a3a' : '#f2f2f2';
    return whole.replace(bgM[0], bgM[0].replace(bgM[1], fixed));
  });

  // 6. a variable named after a hue has no place in a black and white catalog
  for (const [hue, letter] of Object.entries(HUES)) {
    css = css.replace(new RegExp(`--${hue}\\b`, 'g'), `--tone-${letter}`);
    css = css.replace(new RegExp(`--([a-z0-9-]+)-${hue}\\b`, 'g'), `--$1-tone-${letter}`);
  }

  fs.writeFileSync(f, src.replace(/<style>[\s\S]*?<\/style>/, '<style>' + css + '</style>'));
  done++;
}
console.log(`monochrome pass applied to ${done} studies`);
