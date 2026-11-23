"""Gera professora/index.html: índice de todas as aulas, por turma. Sem nomes de alunos."""
import os, re, html

ROOT = os.path.join(os.path.dirname(__file__), "..")
TURMAS = [("turma-a", "Turma A", "Nível A1 · terças"), ("turma-b", "Turma B", "Nível A2/B1 · terças")]
MESES = "jan fev mar abr mai jun jul ago set out nov dez".split()

def titulo(path):
    try:
        t = re.search(r"<title>(.*?)</title>", open(path, encoding="utf-8").read()).group(1)
        return html.unescape(re.sub(r"\s*\((aula|homework)\)$", "", t))
    except Exception:
        return ""

secoes = []
for pasta, nome, sub in TURMAS:
    base = os.path.join(ROOT, pasta)
    if not os.path.isdir(base):
        continue
    linhas = []
    for d in sorted(os.listdir(base)):
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})-", d)
        if not m:
            continue
        y, mo, dd = m.groups()
        tem_aula = os.path.exists(os.path.join(base, d, "aula", "index.html"))
        tem_tarefa = os.path.exists(os.path.join(base, d, "index.html"))
        tema = titulo(os.path.join(base, d, "aula", "index.html")) if tem_aula else titulo(os.path.join(base, d, "index.html"))
        bt = ""
        if tem_aula:
            bt += f'<a class="b aula" href="../{pasta}/{d}/aula/">📺 Aula</a>'
        if tem_tarefa:
            bt += f'<a class="b tarefa" href="../{pasta}/{d}/">📝 Tarefa</a>'
        linhas.append(f'<li><div class="dt"><b>{int(dd)}</b><span>{MESES[int(mo)-1]} {y}</span></div>'
                      f'<div class="tm">{html.escape(tema)}</div><div class="bts">{bt}</div></li>')
    secoes.append(f'<section><h2>{nome}</h2><p class="sub">{sub} · {len(linhas)} aulas</p><ul>{"".join(linhas)}</ul></section>')

doc = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minhas aulas</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;background:#f6f2e7;color:#1f2a25}}
header{{background:#133b2d;color:#f6f2e7;padding:28px 20px}}header h1{{margin:0;font-size:30px}}header p{{margin:6px 0 0;opacity:.8}}
main{{max-width:900px;margin:0 auto;padding:16px}}
nav{{display:flex;gap:10px;margin:8px 0 4px;flex-wrap:wrap}}nav a{{background:#ff7a1a;color:#1c1a17;text-decoration:none;font-weight:700;padding:8px 16px;border-radius:999px}}
section{{margin:22px 0}}h2{{margin:0;font-size:26px}}.sub{{margin:4px 0 12px;color:#5c6b63}}
ul{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}}
li{{background:#fff;border-radius:16px;padding:12px 14px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.dt{{display:flex;flex-direction:column;align-items:center;min-width:54px}}.dt b{{font-size:26px;line-height:1}}.dt span{{font-size:13px;color:#5c6b63}}
.tm{{flex:1;min-width:160px;font-weight:600;font-size:18px}}
.bts{{display:flex;gap:8px}}.b{{text-decoration:none;font-weight:700;padding:9px 14px;border-radius:12px;font-size:15px}}
.aula{{background:#133b2d;color:#fff}}.tarefa{{background:#ffe2c7;color:#1c1a17}}
footer{{text-align:center;color:#8a958f;font-size:13px;padding:20px}}
</style></head><body>
<header><h1>📚 Minhas aulas</h1><p>📺 Aula = para compartilhar a tela · 📝 Tarefa = link para mandar ao aluno</p></header>
<main><nav>{"".join(f'<a href="#{p}">{n}</a>' for p, n, _ in TURMAS)}</nav>
{"".join(s.replace("<section>", f'<section id="{TURMAS[i][0]}">', 1) for i, s in enumerate(secoes))}
</main><footer>Atualizado automaticamente a cada nova aula.</footer>
</body></html>
"""
os.makedirs(os.path.join(ROOT, "professora"), exist_ok=True)
open(os.path.join(ROOT, "professora", "index.html"), "w", encoding="utf-8").write(doc)
print("ok")
