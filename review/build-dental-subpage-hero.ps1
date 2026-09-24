param()
$ErrorActionPreference = 'Stop'
$workspace = Split-Path -Parent $PSScriptRoot
$rawPath = Join-Path $workspace 'sectors/dental-clinics/S21-subpage-hero/raw'
$rows = @()
foreach ($file in (Get-ChildItem -LiteralPath $rawPath -Filter 'DN-S21-*.html' | Sort-Object Name)) {
  $source = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
  $title = [regex]::Match($source, '<title>(.*?)</title>').Groups[1].Value
  $layout = [regex]::Match($source, '<meta name="layout-model" content="([^"]+)">').Groups[1].Value
  $rows += @{ id = $file.BaseName; title = $title; layout = $layout; url = '../sectors/dental-clinics/S21-subpage-hero/raw/' + $file.Name }
}
if ($rows.Count -ne 5) { throw 'Expected exactly five DN-S21 studies.' }
$data = ConvertTo-Json -InputObject @($rows) -Depth 5 -Compress
$data = $data.Replace('<', '\u003c')
$measured = '{}'
$heightPath = Join-Path $PSScriptRoot 'dental-subpage-hero-heights.json'
if (Test-Path -LiteralPath $heightPath) { $measured = Get-Content -LiteralPath $heightPath -Raw -Encoding UTF8 }
$template = @'
<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dental Clinics — S21 Subpage Hero · 5 tasarım</title>
<style>
* { box-sizing: border-box; } body { margin: 0; background: #eceeea; color: #17221d; font: 15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
header { padding: 30px max(20px,calc((100% - 1440px)/2)); background: #17221d; color: #f1f4ee; }
header p { color: #c5cec6; margin: 6px 0 0; max-width: 65ch; } h1 { font-size: clamp(24px,4vw,38px); letter-spacing: -.04em; font-weight: 500; margin: 0; }
.controls { padding: 14px 20px; position: sticky; top: 0; z-index: 10; background: #f8f9f6; border-bottom: 1px solid #cbd1c9; display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; align-items: center; }
button,select { font: inherit; min-height: 44px; padding: 9px 16px; border: 1px solid #abb6ac; background: transparent; color: #17221d; border-radius: 999px; cursor: pointer; }
button[aria-pressed="true"] { background: #17221d; color: #f1f4ee; border-color: #17221d; }
:focus-visible { outline: 3px solid #387858; outline-offset: 3px; }
main { max-width: 1480px; padding: 28px 20px 70px; margin: 0 auto; }
article { margin-bottom: 36px; } .caption { display:flex; gap:20px; justify-content:space-between; align-items:center; margin-bottom:12px; } h2 { font-size:18px; font-weight:600; margin:0; } .caption p { font-size:12px; margin:4px 0 0; color:#536052; }
.caption a { color:inherit; font-size:13px; padding:12px 0; white-space:nowrap; text-underline-offset:4px; }
.frame { overflow:hidden; margin:auto; background:#fff; box-shadow:0 12px 35px #17221d0d; }
iframe { display:block; border:0; transform-origin:top left; }
@media(max-width:560px) { main { padding:20px 10px; } .caption { align-items:start; gap:10px; } .caption p { max-width:35ch; } h2 { font-size:15px; } }
</style>
</head>
<body>
<header><h1>Dental Clinics / Subpage Hero</h1><p>S21 için beş farklı kompozisyon. Gerçek HTML dosyaları; görsel alanları klinik fotoğrafları için ayrılmıştır.</p></header>
<div class="controls"><div role="group" aria-label="Önizleme genişliği"><button type="button" data-width="1440" aria-pressed="true">Masaüstü 1440</button> <button type="button" data-width="768" aria-pressed="false">Tablet 768</button> <button type="button" data-width="390" aria-pressed="false">Mobil 390</button></div><label for="variant">Tasarım</label><select id="variant"><option value="all">Beşini göster</option></select></div>
<main id="studies"></main>
<script type="application/json" id="data">__DATA__</script>
<script type="application/json" id="heights">__HEIGHTS__</script>
<script>
(function(){
  var rows=JSON.parse(document.getElementById('data').textContent), heights=JSON.parse(document.getElementById('heights').textContent);
  var main=document.getElementById('studies'), select=document.getElementById('variant'), width=1440, frames=[];
  function fit(frame) {
    var box=frame.parentElement, article=box.parentElement;
    if(article.hidden) return;
    var scale=Math.min(1, article.clientWidth/width);
    var h=(heights[frame.dataset.id]||{})[width] || (width===390 ? 1900 : 1150);
    frame.width=width;
    try { var section=frame.contentDocument.querySelector('[data-study-id]'); if(section) h=Math.ceil(section.getBoundingClientRect().height); } catch(e) {}
    frame.height=h; frame.style.width=width+'px'; frame.style.height=h+'px'; frame.style.transform='scale('+scale+')';
    box.style.width=(width*scale)+'px'; box.style.height=(h*scale)+'px';
  }
  rows.forEach(function(st){
    var option=document.createElement('option'); option.value=st.id; option.textContent=st.title; select.appendChild(option);
    var article=document.createElement('article'); article.id=st.id;
    var cap=document.createElement('div'); cap.className='caption';
    var copy=document.createElement('div'), title=document.createElement('h2'), desc=document.createElement('p');
    title.textContent=st.title; desc.textContent=st.layout; copy.append(title,desc);
    var link=document.createElement('a'); link.href=st.url; link.target='_blank'; link.rel='noopener'; link.textContent='Tam boyut ↗'; link.setAttribute('aria-label',st.id+' tam boyut aç');
    cap.append(copy,link); var box=document.createElement('div'); box.className='frame';
    var frame=document.createElement('iframe'); frame.title=st.title; frame.dataset.id=st.id; frame.loading='lazy';
    frame.addEventListener('load',function(){fit(frame); try {new ResizeObserver(function(){fit(frame);}).observe(frame.contentDocument.body);} catch(e){}});
    frame.src=st.url; box.appendChild(frame); article.append(cap,box); main.appendChild(article); frames.push(frame); fit(frame);
  });
  document.querySelectorAll('[data-width]').forEach(function(button){button.addEventListener('click',function(){
    width=Number(button.dataset.width); document.querySelectorAll('[data-width]').forEach(function(b){b.setAttribute('aria-pressed',String(b===button));});
    frames.forEach(fit); requestAnimationFrame(function(){frames.forEach(fit);});
  });});
  select.addEventListener('change',function(){main.querySelectorAll('article').forEach(function(a){a.hidden=select.value!=='all'&&a.id!==select.value;});frames.forEach(fit);});
  new ResizeObserver(function(){frames.forEach(fit);}).observe(main);
})();
</script>
</body>
</html>
'@
$output = $template.Replace('__DATA__', $data).Replace('__HEIGHTS__', $measured)
$destination = Join-Path $PSScriptRoot 'dental-subpage-hero.html'
[IO.File]::WriteAllText($destination, $output, [Text.UTF8Encoding]::new($false))
Write-Output 'Generated review/dental-subpage-hero.html (5 studies)'
