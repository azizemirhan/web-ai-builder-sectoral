// Structural check across every study in a sector — the constants that hold for every file.
//   node review/check-sector-structure.js [sector-directory-name]
// Defaults to construction-contractors.
const fs = require('fs');
const path = require('path');
const SECTOR = process.argv[2] && !/^Sdd$/.test(process.argv[2]) ? process.argv[2] : 'construction-contractors';
const ROOT = path.join(__dirname, '..', 'sectors', SECTOR);
const VOID = new Set(['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']);

let fail = 0, n = 0;
const chromatic = [];
const widths = {}, grounds = [];

function report(id, label, ok, detail) {
  if (!ok) { fail++; console.log(`FAIL  ${id}  ${label}${detail ? '  :: ' + detail : ''}`); }
}

for (const s of fs.readdirSync(ROOT).filter(d => /^S\d\d-/.test(d)).sort()) {
  const dir = path.join(ROOT, s, 'raw');
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.html'))) {
    const id = f.replace('.html', '');
    const src = fs.readFileSync(path.join(dir, f), 'utf8');
    const noComments = src.replace(/<!--[\s\S]*?-->/g, '');
    const css = (noComments.match(/<style>([\s\S]*?)<\/style>/) || [])[1] || '';
    const body = (noComments.match(/<body>([\s\S]*)<\/body>/) || [])[1] || '';
    const scope = '.' + (src.match(/data-study-id="([^"]+)"/) || [])[1].toLowerCase();
    n++;

    report(id, 'no script/iframe/img/svg/remote',
      !/<script|<iframe|<img|data:image|<svg|https?:\/\//i.test(noComments));
    report(id, 'no inline style attribute', !/\sstyle\s*=/i.test(body));

    const stripped = css.replace(/\/\*[\s\S]*?\*\//g, '');
    const rules = stripped.split('}').map(x => x.split('{')[0].trim()).filter(Boolean);
    const unscoped = rules.filter(sel => !sel.startsWith('@') && sel.split(',').some(one => {
      const t = one.trim();
      if (!t || t.startsWith('@') || t === 'html' || t === 'body') return false;
      return !t.startsWith(scope);
    }));
    report(id, 'scoped CSS', unscoped.length === 0, unscoped.slice(0, 2).join(' | '));

    const allHex = [...stripped.matchAll(/#[^\s;,)}]*/g)].map(x => x[0]);
    report(id, 'hex validity',
      allHex.every(h => /^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(h)),
      allHex.filter(h => !/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(h)).join(','));
    report(id, 'no 8-digit hex', !allHex.some(h => h.length === 9));
    report(id, 'ascii stylesheet', !/[^\x00-\x7F]/.test(stripped),
      (stripped.match(/[^\x00-\x7F]/g) || []).slice(0, 4).join(''));
    report(id, 'clamp arity',
      [...stripped.matchAll(/clamp\(([^)]*)\)/g)].every(m => m[1].split(',').length === 3));
    report(id, 'no vh unit', !/\d(?:\.\d+)?vh\b/.test(stripped));
    report(id, 'nothing at an angle',
      !/(rotate|skew|matrix3?d?\(|perspective|conic-gradient)/i.test(stripped));
    report(id, 'reduced motion', /prefers-reduced-motion/.test(css));

    const errs = [], stack = [];
    const re = /<(\/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(\/?)>/g;
    let m;
    while ((m = re.exec(body)) !== null) {
      const cl = m[1] === '/', nm = m[2].toLowerCase(), sf = m[3] === '/';
      if (VOID.has(nm) || sf) continue;
      if (!cl) stack.push(nm); else { const t = stack.pop(); if (t !== nm) errs.push(`</${nm}> vs <${t}>`); }
    }
    if (stack.length) errs.push('unclosed: ' + stack.join(','));
    report(id, 'nesting', errs.length === 0, errs.join(' | '));

    const w = (css.match(/max-width:\s*(\d+)px;\s*\n?\s*margin: 0 auto/) || [])[1]
      || (css.match(/\.shell \{[\s\S]*?max-width:\s*(\d+)px/) || [])[1];
    widths[w] = (widths[w] || 0) + 1;
    report(id, 'uniform frame width', w === '1320', `max-width ${w}`);
    // A study conforms to the sector's visual system either through the original mechanical
    // v2 pass, or — for studies reworked against CONSTRUCTION-THEME-CONTRACT.md — by declaring
    // the theme tokens directly. The contract supersedes the pass; both are accepted.
    report(id, 'theme system applied',
      /v2 modern pass/.test(css) || /--accent: *#[0-9a-fA-F]{6}/.test(css));
    if (/--accent: *#[0-9a-fA-F]{6}/.test(css)) {
      const acc = css.match(/--accent: *(#[0-9a-fA-F]{6})/)[1];
      const c = [1,3,5].map(i => parseInt(acc.slice(i,i+2),16));
      if (Math.max(...c) - Math.min(...c) > 12) chromatic.push(id);
    }

    const g = (src.match(/body \{ margin: 0; background: (#[0-9a-f]{6}); \}/) || [])[1];
    grounds.push(id.slice(0, 7) + '|' + g);   // black and white: grounds are unique per section
  }
}

console.log(`\n${n} studies checked`);
console.log('frame widths:', JSON.stringify(widths));
console.log('theme-contract accent:', chromatic.length + '/' + n + ' studies');
const dup = grounds.filter((g, i) => grounds.indexOf(g) !== i);
console.log('duplicate grounds:', dup.length ? [...new Set(dup)].join(',') : 'none');
console.log(fail === 0 ? 'ALL STRUCTURAL CHECKS PASS' : `${fail} CHECK(S) FAILED`);
