// V2 modern pass — construction-contractors
// SUPERSEDED for any section reworked against CONSTRUCTION-THEME-CONTRACT.md: those studies
// declare their theme tokens directly and must not be re-processed by this pass.
// Rewrites the scoped stylesheet of every study: one uniform frame width, a display
// typographic scale, softer geometry, an accent system, and real depth.
// Content, markup and the catalog's isolation rules are untouched.

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..', 'sectors', 'construction-contractors');
const ONLY = process.argv[2] || '';          // e.g. "S27" to limit the pass
const FRAME = 1320;

// ---------- colour helpers ----------
const hex = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16));
const toHex = c => '#' + c.map(v => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, '0')).join('');
const mix = (a, b, t) => { const x = hex(a), y = hex(b); return toHex(x.map((v, i) => v * (1 - t) + y[i] * t)); };
const lum = h => { const c = hex(h).map(v => v / 255).map(v => v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4);
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };

// one accent family per section, so a section reads as a set
// Black and white only: the accent is a value, not a hue.
const ACCENT_LIGHT = Array(9).fill('#141414');
const ACCENT_DARK = Array(9).fill('#f0f0f0');

// ---------- type scale ----------
function scaleRem(n) {
  if (n < 0.62) return Math.max(0.74, n * 1.34);
  if (n < 0.78) return 0.8;
  if (n < 0.94) return 1.0;
  if (n < 1.06) return 1.1;
  if (n < 1.45) return n * 1.18;
  if (n < 2.2) return n * 1.22;
  return n * 1.26;
}
const r3 = n => Math.round(n * 1000) / 1000;

function scaleFontSizes(css) {
  // clamp(min, fluid, max)
  css = css.replace(/font-size:\s*clamp\(\s*([\d.]+)rem\s*,\s*([\d.]+)vw\s*,\s*([\d.]+)rem\s*\)/g,
    (m, a, v, c) => {
      const na = scaleRem(parseFloat(a)), nc = scaleRem(parseFloat(c));
      const nv = parseFloat(v) * (nc / parseFloat(c));
      return `font-size: clamp(${r3(na)}rem, ${r3(nv)}vw, ${r3(nc)}rem)`;
    });
  // plain rem
  css = css.replace(/font-size:\s*([\d.]+)rem\b/g,
    (m, a) => `font-size: ${r3(scaleRem(parseFloat(a)))}rem`);
  return css;
}

function calmTracking(css) {
  return css.replace(/letter-spacing:\s*(0?\.\d+)em/g, (m, v) => {
    const n = parseFloat(v);
    if (n >= 0.13) return 'letter-spacing: 0.085em';
    if (n >= 0.09) return 'letter-spacing: 0.07em';
    return m;
  });
}

function softenGeometry(css) {
  return css.replace(/border-radius:\s*([\d.]+)px/g, (m, v) => {
    const n = parseFloat(v);
    if (n >= 100) return m;              // pills stay pills
    if (n <= 4) return 'border-radius: 10px';
    if (n <= 10) return 'border-radius: 16px';
    if (n <= 16) return 'border-radius: 22px';
    return 'border-radius: 26px';
  });
}

function uniformFrame(css, scope) {
  const re = new RegExp(`(${scope.replace(/\./g, '\\.')} \\.shell \\{[\\s\\S]*?\\})`);
  return css.replace(re, block => block
    .replace(/max-width:\s*[\d.]+px/, `max-width: ${FRAME}px`)
    .replace(/padding:\s*[^;]+;/, 'padding: clamp(40px, 5vw, 92px) clamp(22px, 3.6vw, 58px);'));
}

// selectors whose block paints a card, so they can carry depth
function collect(css, test) {
  const out = [];
  const re = /([^{}]+)\{([^{}]*)\}/g;
  let m;
  while ((m = re.exec(css)) !== null) {
    const sel = m[1].trim(), body = m[2];
    if (sel.startsWith('@') || !sel.startsWith('.con-')) continue;
    if (test(body, sel)) out.push(sel.replace(/\s+/g, ' '));
  }
  return [...new Set(out)];
}

function heightOf(body) {
  const m = body.match(/(?:min-)?height:\s*(?:clamp\(\s*([\d.]+)px|([\d.]+)px)/);
  if (!m) return null;
  return parseFloat(m[1] || m[2]);
}

function pass(file, sectionIndex) {
  const src = fs.readFileSync(file, 'utf8');
  const styleM = src.match(/<style>([\s\S]*?)<\/style>/);
  if (!styleM) return null;
  if (/v2 modern pass/.test(src)) return 'already';

  const scope = '.' + (src.match(/data-study-id="([^"]+)"/)[1].toLowerCase());
  const ground = src.match(/body \{ margin: 0; background: (#[0-9a-f]{6}); \}/)[1];
  const dark = lum(ground) < 0.35;
  const accent = (dark ? ACCENT_DARK : ACCENT_LIGHT)[sectionIndex % 9];

  let css = styleM[1];
  const hasVar = n => new RegExp(`--${n}:`).test(css);
  const fill = hasVar('fill') ? 'var(--fill)' : mix(ground, dark ? '#ffffff' : '#000000', 0.07);
  const line = hasVar('line') ? 'var(--line)' : mix(ground, dark ? '#ffffff' : '#000000', 0.14);

  const cards = collect(css, b => /background:\s*var\(--card\)/.test(b) || /background:\s*#f{3,6}\b/i.test(b));
  const platesAll = collect(css, b => /border:\s*1px dashed/.test(b));
  // a media area declares a real height; a caption placeholder does not
  const plateHeight = sel => {
    const m = css.match(new RegExp(sel.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\s*\\{([^{}]*)\\}'));
    return m ? heightOf(m[1]) : null;
  };
  const plates = platesAll.filter(sel => (plateHeight(sel) || 0) >= 140);
  const smallPlates = platesAll.filter(sel => (plateHeight(sel) || 0) < 140);
  const eyebrows = ['.eyebrow', '.kicker', '.tag', '.step'].filter(c => new RegExp(`\\${c}\\b`).test(css));

  css = scaleFontSizes(css);
  css = calmTracking(css);
  css = softenGeometry(css);
  css = uniformFrame(css, scope);

  const tintTop = mix(ground, accent, dark ? 0.16 : 0.1);
  const tintSoft = mix(ground, accent, dark ? 0.24 : 0.14);
  const accentInk = dark ? accent : mix(accent, '#111111', 0.12);
  const shadow = dark ? '0 26px 60px rgba(0, 0, 0, 0.45)' : '0 22px 50px rgba(23, 26, 21, 0.09)';
  const cardEdge = dark ? mix(ground, '#ffffff', 0.1) : mix(ground, '#000000', 0.06);

  const add = [];
  add.push('\n/* ---- v2 modern pass: frame, accent, depth ---- */');
  add.push(`${scope} {`);
  add.push(`  --v2-accent: ${accent};`);
  add.push(`  --v2-soft: ${tintSoft};`);
  add.push(`  background: linear-gradient(180deg, ${mix(ground, accent, dark ? 0.1 : 0.05)} 0%, ${ground} 30%);`);
  add.push(`  font-size: 1.06rem;`);
  add.push('}');
  add.push(`${scope} h2 { font-weight: 800; }`);
  add.push(`${scope} h3, ${scope} h4 { font-weight: 750; }`);

  if (eyebrows.length) {
    add.push(`${scope} ${eyebrows.join(`, ${scope} `)} {`);
    add.push('  display: inline-block;');
    add.push('  padding: 7px 15px;');
    add.push('  border-radius: 999px;');
    add.push(`  background: ${tintSoft};`);
    add.push(`  color: ${accentInk};`);
    add.push('  font-weight: 700;');
    add.push('  letter-spacing: 0.075em;');
    add.push('}');
  }

  if (cards.length) {
    add.push(`${cards.join(', ')} {`);
    add.push('  border-radius: 26px;');
    add.push(`  box-shadow: ${shadow};`);
    add.push(`  border: 1px solid ${cardEdge};`);
    add.push('}');
  }

  if (plates.length) {
    add.push(`${plates.join(', ')} {`);
    add.push('  height: auto;');
    add.push('  min-height: clamp(200px, 21vw, 320px);');
    add.push('  border-radius: 26px;');
    add.push(`  border: 2px dashed ${mix(mix(ground, dark ? '#ffffff' : '#000000', 0.16), accent, 0.42)};`);
    add.push(`  background: linear-gradient(145deg, ${mix(ground, accent, dark ? 0.2 : 0.13)} 0%, ${fill} 100%);`);
    add.push('}');
    add.push(`${plates.map(s => s + ' span').join(', ')} {`);
    add.push(`  color: ${accentInk};`);
    add.push('  font-weight: 700;');
    add.push('}');
  }

  // caption-sized placeholders keep their size and only take the new edge
  if (smallPlates.length) {
    add.push(`${smallPlates.join(', ')} {`);
    add.push(`  border: 1px dashed ${mix(mix(ground, dark ? '#ffffff' : '#000000', 0.16), accent, 0.42)};`);
    add.push('  border-radius: 14px;');
    add.push('}');
  }

  add.push(`${scope} .slot {`);
  add.push('  border-radius: 999px;');
  add.push('  padding: 4px 15px;');
  add.push(`  background: ${tintSoft};`);
  add.push(`  color: ${accentInk};`);
  add.push('  font-weight: 600;');
  add.push('}');

  // --- the hero: the opening band becomes a panel rather than a ruled paragraph ---
  const named = ['.head', '.mast', '.top', '.masthead', '.lede', '.opening', '.intro', '.banner']
    .filter(c => new RegExp(`\\${c}\\b`).test(css));
  // fall back to the opening band only when it is a real container near the top
  let heroClasses = [];
  if (named.length) heroClasses = [named[0]];
  else {
    const bodyHtml = (src.match(/<body>([\s\S]*)<\/body>/) || ['', ''])[1];
    const shellStart = bodyHtml.search(/<section[^>]*class="shell"/);
    if (shellStart >= 0) {
      const kids = [];
      let depth = 0;
      const re2 = /<(\/?)([a-z][a-z0-9]*)\b[^>]*?(\/?)>/gi;
      re2.lastIndex = bodyHtml.indexOf('>', shellStart) + 1;
      let mm;
      while ((mm = re2.exec(bodyHtml)) !== null && kids.length < 4) {
        const closing = mm[1] === '/', tag = mm[2].toLowerCase(), self = mm[3] === '/';
        if (['br', 'hr', 'img', 'input', 'meta'].includes(tag) || self) continue;
        if (!closing) { if (depth === 0) kids.push(tag); depth++; }
        else { depth--; if (depth < 0) break; }
      }
      const i = kids.findIndex(t => t === 'div');
      if (i === 0 || i === 1) heroClasses = [`.shell > div:nth-of-type(1)`];
    }
  }
  // the hero always ends up dark enough for white type, whatever the study's ground
  const heroStart = lum(accent) > 0.42 ? mix(accent, '#000000', 0.3) : accent;
  const heroMid = mix(heroStart, '#000000', 0.3);
  const heroEnd = mix(heroStart, '#000000', 0.52);
  const heroInk = '#ffffff';
  const heroInk2 = mix('#ffffff', heroStart, 0.3);
  const S2 = scope + scope;   // doubled scope: outranks the study's own rules

  // a hero panel is only right when the opening band actually holds the headline
  if (heroClasses.length) {
    const bodyHtml2 = (src.match(/<body>([\s\S]*)<\/body>/) || ['', ''])[1];
    const cls = heroClasses[0].replace(/^\./, '').replace(/ >.*$/, '');
    const at = /^\.shell/.test(heroClasses[0])
      ? bodyHtml2.search(/<section[^>]*class="shell"/)
      : bodyHtml2.indexOf(`class="${cls}"`);
    const h2at = bodyHtml2.indexOf('<h2');
    if (at < 0 || h2at < at || h2at - at > 900) heroClasses = [];
  }
  if (heroClasses.length) {
    const heroSel = heroClasses.map(c => `${S2} ${c}`).join(', ');
    add.push(`${heroSel} {`);
    add.push('  padding: clamp(30px, 4vw, 64px);');
    add.push('  border-radius: 34px;');
    add.push('  border: none;');
    add.push(`  background: linear-gradient(135deg, ${heroStart} 0%, ${heroMid} 58%, ${heroEnd} 100%);`);
    add.push(`  color: ${heroInk};`);
    add.push(`  box-shadow: ${shadow};`);
    add.push('  margin-bottom: clamp(26px, 3.2vw, 48px);');
    add.push('}');
    const strong = ['h2', 'h3', 'h4', 'b', 'strong', 'p b', 'li b', 'span b', 'dt', 'div b'];
    const quiet = ['p', 'li', 'span', 'dd', 'div p', 'div li', 'p span', '.said', '.note'];
    add.push(heroClasses.map(c => strong.map(k => `${S2} ${c} ${k}`).join(', ')).join(', ') + ' {');
    add.push(`  color: ${heroInk};`);
    add.push('}');
    add.push(heroClasses.map(c => quiet.map(k => `${S2} ${c} ${k}`).join(', ')).join(', ') + ' {');
    add.push(`  color: ${heroInk2};`);
    add.push('}');
    add.push(heroClasses.map(c => [`${c} .eyebrow`, `${c} .kicker`, `${c} .slot`, `${c} .tag`]
      .map(x => `${S2} ${x}`).join(', ')).join(', ') + ' {');
    add.push('  background: rgba(255, 255, 255, 0.16);');
    add.push(`  color: ${heroInk};`);
    add.push('}');
    // reserved measures inside the hero read as translucent, not as raw fill
    add.push(heroClasses.map(c => ['i', '.bars i', '.lines i', '.measures i', '.bar', '.rule']
      .map(k => `${S2} ${c} ${k}`).join(', ')).join(', ') + ' {');
    add.push('  background: rgba(255, 255, 255, 0.24);');
    add.push('}');
    add.push(heroClasses.map(c => `${S2} ${c} .plate, ${S2} ${c} .plate span`).join(', ') + ' {');
    add.push('  background: rgba(255, 255, 255, 0.1);');
    add.push('  border-color: rgba(255, 255, 255, 0.3);');
    add.push(`  color: ${heroInk2};`);
    add.push('}');
  } else {
    // no opening container: the headline itself carries the colour
    add.push(`${S2} .shell > h2 {`);
    add.push('  padding: clamp(26px, 3.4vw, 54px);');
    add.push('  border-radius: 34px;');
    add.push(`  background: linear-gradient(135deg, ${heroStart} 0%, ${heroMid} 58%, ${heroEnd} 100%);`);
    add.push(`  color: ${heroInk};`);
    add.push(`  box-shadow: ${shadow};`);
    add.push('  max-width: none;');
    add.push('}');
    add.push(`${S2} .shell > h2 span, ${S2} .shell > h2 b, ${S2} .shell > h2 em, ${S2} .shell > h2 i {`);
    add.push(`  color: ${heroInk};`);
    add.push('}');
  }

  // --- section rhythm: air between the bands, and no hairline crowding ---
  add.push(`${scope} .shell > * { margin-bottom: clamp(26px, 3.2vw, 50px); }`);
  add.push(`${scope} .shell > *:last-child { margin-bottom: 0; }`);

  // --- the document frame goes: hard rules become soft panels ---
  const framed = collect(css, b => /border:\s*[2-9]px solid/.test(b) && /padding:/.test(b));
  if (framed.length) {
    add.push(`${framed.join(', ')} {`);
    add.push('  border: none;');
    add.push('  border-radius: 30px;');
    add.push('  padding: clamp(22px, 2.8vw, 44px);');
    add.push(`  background: ${mix(ground, dark ? '#ffffff' : '#ffffff', dark ? 0.06 : 0.55)};`);
    add.push(`  box-shadow: ${shadow};`);
    add.push('}');
  }

  // --- micro-labels lead with the accent ---
  add.push('');

  const out = src.replace(/<style>[\s\S]*?<\/style>/, '<style>' + css + add.join('\n') + '</style>');
  fs.writeFileSync(file, out);
  return 'done';
}

const sections = fs.readdirSync(ROOT).filter(d => /^S\d\d-/.test(d)).sort();
let n = 0, skipped = 0;
for (const s of sections) {
  if (ONLY && !s.startsWith(ONLY)) continue;
  const idx = parseInt(s.slice(1, 3), 10);
  const dir = path.join(ROOT, s, 'raw');
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.html'))) {
    const res = pass(path.join(dir, f), idx);
    if (res === 'done') n++; else skipped++;
  }
}
console.log(`v2 pass applied to ${n} studies (${skipped} skipped)`);
