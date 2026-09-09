// SUPERSEDED — do not use as a gate.
//
// This asserted that every CON study is black and white. That rule came from the monochrome
// pass, and it contradicts the sector's own direction, which requires "concrete and asphalt
// neutrals with ONE high-visibility accent". Studies reworked against
// sectors/construction-contractors/CONSTRUCTION-THEME-CONTRACT.md carry a chromatic accent by
// design and will report here as failures. They are not failures.
//
// Kept only to measure how much of the sector is still un-reworked: a "failure" below means a
// study HAS been brought onto the theme contract.
const fs = require('fs');
const path = require('path');
const SECTOR = process.argv[2] && !/^Sdd$/.test(process.argv[2]) ? process.argv[2] : 'construction-contractors';
const ROOT = path.join(__dirname, '..', 'sectors', SECTOR);

let fail = 0, n = 0;
const spread = [];

for (const s of fs.readdirSync(ROOT).filter(d => /^S\d\d-/.test(d)).sort()) {
  const dir = path.join(ROOT, s, 'raw');
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.html'))) {
    const id = f.replace('.html', '');
    const src = fs.readFileSync(path.join(dir, f), 'utf8');
    const css = (src.replace(/<!--[\s\S]*?-->/g, '').match(/<style>([\s\S]*?)<\/style>/) || ['', ''])[1];
    n++;

    const bad = [];
    for (const m of css.matchAll(/#([0-9a-fA-F]{6})\b/g)) {
      const h = m[1];
      if (!(h.slice(0, 2).toLowerCase() === h.slice(2, 4).toLowerCase()
         && h.slice(2, 4).toLowerCase() === h.slice(4, 6).toLowerCase())) bad.push('#' + h);
    }
    for (const m of css.matchAll(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/g)) {
      if (!(m[1] === m[2] && m[2] === m[3])) bad.push(m[0] + ')');
    }
    const named = css.match(/\b(red|blue|green|orange|purple|teal|navy|gold|brown|pink|yellow|cyan|magenta)\b/gi);
    if (named) bad.push(...named);

    if (bad.length) { fail++; console.log(`FAIL  ${id}  colour found  :: ${[...new Set(bad)].slice(0, 5).join(', ')}`); }

    const g = (src.match(/body \{ margin: 0; background: (#[0-9a-f]{6}); \}/) || [])[1];
    spread.push([id, g]);
  }
}

const grounds = spread.map(x => x[1]);
const keyed = spread.map(x => x[0].slice(0, 7) + '|' + x[1]);   // unique per section
const dup = keyed.filter((g, i) => keyed.indexOf(g) !== i);
console.log(`\n${n} studies checked`);
console.log('duplicate grounds:', dup.length ? [...new Set(dup)].join(',') : 'none');
const vals = grounds.map(g => parseInt(g.slice(1, 3), 16)).sort((a, b) => a - b);
console.log(`ground range: ${vals[0]} .. ${vals[vals.length - 1]} (of 255), ${new Set(vals).size} distinct values`);
console.log(fail === 0 ? 'BLACK AND WHITE: PASS' : `${fail} STUDY(IES) STILL CARRY COLOUR`);
