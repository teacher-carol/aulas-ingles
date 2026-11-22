"""Gerador das páginas interativas (aula e tarefa). Conteúdo original, sem recursos externos."""
import html, json, random, os, sys

FONT = "system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"
CSS = """*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;font-family:%F%;background:#0e2b21;color:#1f2a25;height:100vh;height:100dvh;overflow:hidden;-webkit-text-size-adjust:100%}
button,.card{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.slide{display:none;position:absolute;top:0;left:0;right:0;bottom:0;padding:40px 24px calc(110px + env(safe-area-inset-bottom));-webkit-overflow-scrolling:touch;background:#f6f2e7;overflow:auto;flex-direction:column;gap:18px}
.slide.on{display:flex}
.slide.dark{background:#133b2d;color:#f6f2e7}
.slide.accent{background:#ff7a1a;color:#1c1a17}
.wrap{max-width:1100px;width:100%;margin:0 auto;display:flex;flex-direction:column;gap:18px}
h1{font-size:clamp(40px,7vw,72px);margin:0;line-height:1.05}
h2{font-size:clamp(28px,5vw,46px);margin:0;line-height:1.15}
h3{font-size:24px;margin:0}
p,li{font-size:22px;line-height:1.45;margin:0}
.k{font-size:15px;letter-spacing:3px;text-transform:uppercase;font-weight:800;color:#e8630a}
.dark .k{color:#ffb36b}.accent .k{color:#1c1a17}
.tip{font-size:18px;opacity:.8}
.big{font-size:clamp(24px,3.5vw,34px);font-weight:700;line-height:1.35}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:12px}
.cards{display:flex;gap:14px;flex-wrap:wrap}
.box{flex:1;min-width:200px;background:#fff;color:#1f2a25;border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:8px}
.dark .box{background:#1e5442;color:#f6f2e7}
.box.bad{border:4px solid #e0453a}.box.good{border:4px solid #2fae66}
.card{background:#fff;color:#1f2a25;border-radius:18px;padding:18px;cursor:pointer;position:relative}
.dark .card{background:#1e5442;color:#f6f2e7}
.card::after{content:'🔊';position:absolute;top:10px;right:12px;font-size:18px}
.card:active{transform:scale(.97)}
.v{font-size:22px;font-weight:700;padding-right:22px}.p{font-size:28px;font-weight:800;color:#e8630a}
.dark .p{color:#ffb36b}
table{border-collapse:collapse;background:#fff;color:#1f2a25;border-radius:16px;overflow:hidden;width:100%;max-width:700px}
td,th{font-size:24px;padding:12px 18px;border-bottom:2px solid #e4dccb;text-align:left}
th{color:#e8630a}
.q{background:#fff;color:#1f2a25;border-radius:16px;padding:14px 18px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.dark .q{background:#1e5442;color:#f6f2e7}
.q .t{font-size:21px;font-weight:700;flex:1 1 100%}
button.o{font:600 19px %F%;padding:9px 16px;border-radius:999px;border:2px solid #c9c0ab;background:#f6f2e7;color:#1f2a25;cursor:pointer}
button.o.ok{background:#2fae66;border-color:#2fae66;color:#fff}
button.o.bad{background:#e0453a;border-color:#e0453a;color:#fff}
.story{background:#fff;color:#1f2a25;border-radius:18px;padding:22px;font-size:22px;line-height:2}
.dark .story{background:#1e5442;color:#f6f2e7}
.story .q{display:inline-flex;padding:4px;gap:4px;background:transparent;vertical-align:middle}
.story button.o{font-size:16px;padding:4px 10px}
button.spk,button.listen{font:700 19px %F%;padding:9px 16px;border-radius:12px;border:none;background:#ff7a1a;color:#1c1a17;cursor:pointer}
.score{font:700 22px %F%;color:#e8630a;min-height:28px}
.dark .score{color:#ffb36b}
.reset{font:600 16px %F%;padding:8px 14px;border-radius:10px;border:none;background:#1f2a25;color:#fff;cursor:pointer;align-self:flex-start}
.dark .reset{background:#ffb36b;color:#1f2a25}
.total{font:800 clamp(60px,12vw,120px) %F%;color:#ffb36b;margin:0}
.nav{position:fixed;bottom:0;left:0;right:0;height:calc(70px + env(safe-area-inset-bottom));padding-bottom:env(safe-area-inset-bottom);background:#0e2b21;display:flex;align-items:center;justify-content:center;gap:20px;color:#f6f2e7;font:600 18px %F%;z-index:5}
.nav button{font:700 18px %F%;padding:10px 22px;border-radius:12px;border:none;background:#ff7a1a;color:#1c1a17;cursor:pointer}
""".replace("%F%", FONT)

JS = r"""
var S=[].slice.call(document.querySelectorAll('.slide')),i=0;
function show(n){i=Math.max(0,Math.min(S.length-1,n));S.forEach(function(s,k){s.classList.toggle('on',k===i)});document.getElementById('num').textContent=(i+1)+' / '+S.length;total();S[i].scrollTop=0;}
document.getElementById('prev').onclick=function(){show(i-1)};
document.getElementById('next').onclick=function(){show(i+1)};
document.addEventListener('keydown',function(e){if(e.key==='ArrowRight')show(i+1);if(e.key==='ArrowLeft')show(i-1);});
var VOICES=[];function loadV(){try{VOICES=speechSynthesis.getVoices()||[];}catch(e){}}
if(window.speechSynthesis){loadV();speechSynthesis.onvoiceschanged=loadV;}
function say(t){if(!window.speechSynthesis||!t)return;try{if(speechSynthesis.speaking||speechSynthesis.pending)speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=0.85;var v=null;for(var k=0;k<VOICES.length;k++){if(VOICES[k].lang&&VOICES[k].lang.replace('_','-').indexOf('en-US')===0){v=VOICES[k];break;}}if(v)u.voice=v;speechSynthesis.speak(u);}catch(e){}}
[].forEach.call(document.querySelectorAll('.card'),function(c){c.onclick=function(){say(c.getAttribute('data-say'))}});
[].forEach.call(document.querySelectorAll('button.spk,button.listen'),function(b){b.onclick=function(){say(b.getAttribute('data-say'))}});
function score(s){var qs=s.querySelectorAll('.q'),el=s.querySelector('.score'),ok=0,done=0;[].forEach.call(qs,function(q){if(q.dataset.done){done++;if(q.dataset.done==='ok')ok++;}});if(el)el.textContent=done?('Score: '+ok+' / '+qs.length):'';}
function gameScores(){var out=[],n=0;S.forEach(function(s){var qs=s.querySelectorAll('.q');if(!qs.length)return;n++;var ok=0;[].forEach.call(qs,function(q){if(q.dataset.done==='ok')ok++;});out.push({g:n,name:s.getAttribute('data-name')||('Game '+n),ok:ok,t:qs.length});});return out;}
function total(){var el=document.getElementById('total');if(!el)return;var gs=gameScores(),ok=0,t=0;gs.forEach(function(x){ok+=x.ok;t+=x.t;});el.textContent=ok+' / '+t;var m=document.getElementById('msg');if(m){var r=t?ok/t:0;m.textContent=r>=0.87?'⭐ Amazing! You are a star!':r>=0.62?'⚽ Great game! Almost perfect!':r>=0.3?'👏 Good job! Practice a little more and try again!':'🚀 Play the games and come back to see your score!';}if(i===S.length-1)saveBest(ok,t);}
var KEY=document.body.getAttribute('data-key');
function saveBest(ok,t){try{var d=JSON.parse(localStorage.getItem(KEY)||'{}');if(!d.best||ok>d.best){d.best=ok;localStorage.setItem(KEY,JSON.stringify(d));}showBest(t);}catch(e){}}
function showBest(t){try{var d=JSON.parse(localStorage.getItem(KEY)||'{}');var el=document.getElementById('best');if(el&&d.best)el.textContent='🏅 Your best score: '+d.best+(t?' / '+t:'');}catch(e){}}
var TEACHER_PHONE=''; // WhatsApp da professora (opcional): só números, ex: 5583999999999
var sendB=document.getElementById('send');
if(sendB)sendB.onclick=function(){var gs=gameScores(),ok=0,t=0;gs.forEach(function(x){ok+=x.ok;t+=x.t;});var txt='📚 '+document.body.getAttribute('data-student')+' | '+document.title+'\n'+gs.map(function(x){return x.name+': '+x.ok+'/'+x.t}).join('\n')+'\nTotal: '+ok+'/'+t+' ✅';location.href='https://wa.me/'+TEACHER_PHONE+'?text='+encodeURIComponent(txt);};
[].forEach.call(document.querySelectorAll('.q'),function(q){[].forEach.call(q.querySelectorAll('button.o'),function(b){b.onclick=function(){
  var right=b.hasAttribute('data-ok');b.classList.add(right?'ok':'bad');
  if(!q.dataset.done)q.dataset.done=right?'ok':'bad';
  if(right){[].forEach.call(q.querySelectorAll('button.o'),function(x){x.disabled=true});say(q.getAttribute('data-speak'));}
  score(q.closest('.slide'));}})});
[].forEach.call(document.querySelectorAll('.reset'),function(r){r.onclick=function(){var s=r.closest('.slide');[].forEach.call(s.querySelectorAll('.q'),function(q){delete q.dataset.done;[].forEach.call(q.querySelectorAll('button.o'),function(b){b.classList.remove('ok','bad');b.disabled=false;});});score(s);}});
show(0);
"""

E = html.escape
rnd = random.Random(42)


def opts_html(opts, shuffle=True):
    """opts: lista, primeira é a correta."""
    items = [(o, j == 0) for j, o in enumerate(opts)]
    if shuffle:
        for _ in range(5):
            rnd.shuffle(items)
            if items[0][1] is False or len(items) == 1:
                break
    return "".join(f'<button class="o"{" data-ok" if ok else ""}>{E(o)}</button>' for o, ok in items)


def q_html(q):
    # q: dict(t=prompt, o=[correct, ...], listen=str, speak=str|False, fixed=bool, okidx=int)
    opts = q["o"]
    if "okidx" in q:  # ordem fixa com resposta em posição definida
        k = q["okidx"]
        body = "".join(f'<button class="o"{" data-ok" if j == k else ""}>{E(o)}</button>' for j, o in enumerate(opts))
        correct = opts[k]
    else:
        body = opts_html(opts, not q.get("fixed"))
        correct = opts[0]
    speak = q.get("speak", correct)
    sp = f' data-speak="{E(speak)}"' if speak else ""
    head = ""
    if q.get("listen"):
        head += f'<button class="spk" data-say="{E(q["listen"])}">🔊 {E(q.get("label", "Listen"))}</button>'
    if q.get("t"):
        head = f'<span class="t">{q["t"]}</span>' + head
    return f'<div class="q"{sp}>{head}{body}</div>'


def slide(s):
    cls = s.get("cls", "")
    name = f' data-name="{E(s["name"])}"' if s.get("name") else ""
    out = [f'<section class="slide {cls}"{name}><div class="wrap">']
    if s.get("k"):
        out.append(f'<p class="k">{s["k"]}</p>')
    if s.get("pre"):
        out.append(s["pre"])
    if s.get("h"):
        out.append(f'<h2>{s["h"]}</h2>' if not s.get("h1") else f'<h1>{s["h"]}</h1>')
    if s.get("html"):
        out.append(s["html"])
    if s.get("cards"):
        out.append('<p class="tip">🔊 Click a card to listen. Repeat out loud!</p><div class="grid">')
        for a, b in s["cards"]:
            out.append(f'<div class="card" data-say="{E(a)}... {E(b)}"><div class="v">{E(a)}</div><div class="p">{E(b)}</div></div>')
        out.append("</div>")
    if s.get("qs"):
        if s.get("tip"):
            out.append(f'<p class="tip">{s["tip"]}</p>')
        out.append('<p class="score"></p>')
        out += [q_html(q) for q in s["qs"]]
        out.append('<button class="reset">Try again</button>')
    if s.get("story"):
        out.append('<p class="score"></p><div class="story">')
        full = []
        for seg in s["story"]:
            if isinstance(seg, str):
                out.append(E(seg)); full.append(seg)
            else:
                out.append(q_html({"o": seg, "speak": False})); full.append(seg[0])
        out.append("</div>")
        out.append(f'<button class="listen" data-say="{E("".join(full))}">🔊 Listen to the answer</button>')
        out.append('<button class="reset">Try again</button>')
    if s.get("final"):
        out.append('<p class="total" id="total">0</p><p id="msg" class="big"></p>')
        out.append(f'<p>{s["final"]}</p><p id="best" class="tip"></p>')
        if s.get("send", True):
            out.append('<button id="send" class="spk" style="align-self:flex-start;font-size:22px;padding:14px 22px">📲 Send my score to the teacher</button>')
        out.append('<p>Show this screen to your mom! 📸</p><p class="tip">Want a better score? Go back and click "Try again".</p>')
    if s.get("after"):
        out.append(s["after"])
    out.append("</div></section>")
    return "\n".join(out)


def page(title, student, key, slides, path):
    body = "\n".join(slide(s) for s in slides)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<style>{CSS}</style>
</head>
<body data-key="{E(key)}" data-student="{E(student)}">
{body}
<div class="nav"><button id="prev">← Back</button><span id="num"></span><button id="next">Next →</button></div>
<script>{JS}</script>
</body>
</html>
"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(doc)


def boxes(items, cls=""):
    return '<div class="cards">' + "".join(f'<div class="box {cls}">{x}</div>' for x in items) + "</div>"


def wrong_right(wrong, right):
    return ('<div class="cards"><div class="box bad"><p style="font-weight:800;color:#e0453a">❌ WRONG</p>'
            + "".join(f'<p class="big">{w}</p>' for w in wrong)
            + '</div><div class="box good"><p style="font-weight:800;color:#2fae66">✅ CORRECT</p>'
            + "".join(f'<p class="big">{r}</p>' for r in right) + "</div></div>")
