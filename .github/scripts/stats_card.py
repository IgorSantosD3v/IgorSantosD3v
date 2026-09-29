"""Gera o card animado de estatísticas do GitHub (dark e light).

Uso: python stats_card.py <pasta_saida>
Variáveis: GITHUB_TOKEN (obrigatória), GH_LOGIN (usuário), STATS_MOCK (json local para teste).
"""
import datetime as dt
import json
import os
import sys
import urllib.request
from xml.sax.saxutils import escape

LOGIN = os.environ.get("GH_LOGIN", "IgorSantosD3v")
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist"
WEEKS = 26

QUERY = """
query($login: String!) {
  user(login: $login) {
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes {
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

THEMES = {
    "dark": dict(bg="#0d1117", card="#161b22", stroke="#30363d", text="#e6edf3", muted="#8b949e",
                 blue="#58a6ff", green="#3fb950", amber="#d29922", purple="#bc8cff", track="#21262d",
                 heat=["#161b22", "#0e2a4d", "#1f4f8f", "#2f74c6", "#58a6ff"]),
    "light": dict(bg="#ffffff", card="#f6f8fa", stroke="#d0d7de", text="#1f2328", muted="#57606a",
                  blue="#0969da", green="#1a7f37", amber="#9a6700", purple="#8250df", track="#eaeef2",
                  heat=["#ebedf0", "#b6d4f5", "#78aef0", "#3b82e0", "#0969da"]),
}
FONT = "'JetBrains Mono','Fira Code',Consolas,Menlo,'DejaVu Sans Mono',monospace"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def fetch():
    mock = os.environ.get("STATS_MOCK")
    if mock:
        with open(mock, encoding="utf-8") as f:
            return json.load(f)
    body = json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"Erro na API do GitHub: {data['errors']}")
    return data["data"]["user"]


def fmt(d):
    return d.strftime("%d/%m")


def compute(user):
    cal = user["contributionsCollection"]["contributionCalendar"]
    days = [(dt.date.fromisoformat(d["date"]), d["contributionCount"])
            for w in cal["weeks"] for d in w["contributionDays"]]
    days.sort()
    today = dt.date.today()
    days = [d for d in days if d[0] <= today]

    # sequência atual (se hoje ainda está zerado, conta a partir de ontem)
    cur, cur_start = 0, None
    idx = len(days) - 1
    if idx >= 0 and days[idx][1] == 0:
        idx -= 1
    while idx >= 0 and days[idx][1] > 0:
        cur += 1
        cur_start = days[idx][0]
        idx -= 1

    best, best_range, run, run_start = 0, None, 0, None
    for d, c in days:
        if c > 0:
            run += 1
            run_start = run_start or d
            if run > best:
                best, best_range = run, (run_start, d)
        else:
            run, run_start = 0, None

    langs = {}
    for repo in user["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            name = e["node"]["name"]
            langs.setdefault(name, [0, e["node"]["color"] or "#8b949e"])
            langs[name][0] += e["size"]
    total_size = sum(v[0] for v in langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: kv[1][0], reverse=True)[:6]
    top = [(n, v[1], v[0] / total_size * 100) for n, v in top]

    weeks = cal["weeks"][-WEEKS:]
    grid = [[(dt.date.fromisoformat(d["date"]), d["contributionCount"]) for d in w["contributionDays"]] for w in weeks]

    return dict(total=cal["totalContributions"], cur=cur, cur_start=cur_start, best=best, best_range=best_range,
                repos=user["repositories"]["totalCount"], langs=top, grid=grid, today=today)


def ring(cx, cy, r, frac, color, t, delay):
    circ = 2 * 3.14159265 * r
    length = max(frac, 0.0001) * circ
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{t["track"]}" stroke-width="6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round" '
            f'transform="rotate(-90 {cx} {cy})" stroke-dasharray="{length:.1f} {circ:.1f}" '
            f'style="--len:{length:.1f};animation-delay:{delay}s" class="ring"/>')


def render(s, t):
    W, H = 900, 370
    o = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Estatísticas do GitHub de {LOGIN}">
<style>
.lbl{{font-family:{FONT};font-size:11px;letter-spacing:1.5px;fill:{t["muted"]}}}
.num{{font-family:{SANS};font-weight:700;fill:{t["text"]}}}
.tl{{font-family:{SANS};font-size:13px;font-weight:700;fill:{t["text"]}}}
.ts{{font-family:{SANS};font-size:12px;fill:{t["muted"]}}}
.ln{{font-family:{SANS};font-size:13px;fill:{t["text"]}}}
.lp{{font-family:{FONT};font-size:12px;fill:{t["muted"]}}}
.tile{{opacity:0;animation:rise .7s cubic-bezier(.2,.8,.2,1) forwards}}
.ring{{stroke-dashoffset:var(--len);animation:draw 1.4s cubic-bezier(.2,.8,.2,1) forwards}}
.cell{{transform-box:fill-box;transform-origin:center;transform:scale(0);animation:pop .45s cubic-bezier(.3,1.6,.5,1) forwards}}
.seg{{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow .9s cubic-bezier(.2,.8,.2,1) forwards}}
.fade{{opacity:0;animation:fade .6s ease forwards}}
.scan{{animation:scan 6s linear infinite}}
@keyframes rise{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
@keyframes pop{{to{{transform:scale(1)}}}}
@keyframes grow{{to{{transform:scaleX(1)}}}}
@keyframes fade{{to{{opacity:1}}}}
@keyframes scan{{0%{{transform:translateX(0);opacity:0}}8%{{opacity:1}}92%{{opacity:1}}100%{{transform:translateX({WEEKS*15}px);opacity:0}}}}
</style>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{t["bg"]}" stroke="{t["stroke"]}"/>
<text x="20" y="32" class="lbl">ATIVIDADE NO GITHUB</text>
<text x="{W-20}" y="32" text-anchor="end" class="lbl">ATUALIZADO EM {s["today"].strftime("%d/%m/%Y")}</text>''']

    best = max(s["best"], 1)
    cur_sub = f'desde {fmt(s["cur_start"])}' if s["cur"] else "bora commitar hoje"
    best_sub = f'{fmt(s["best_range"][0])} a {fmt(s["best_range"][1])}' if s["best_range"] else "12 meses"
    tiles = [
        (f'{s["total"]:,}'.replace(",", "."), 1.0, t["blue"], "Contribuições", "últimos 12 meses"),
        (str(s["cur"]), s["cur"] / best, t["green"], "Sequência atual", cur_sub),
        (str(s["best"]), 1.0, t["amber"], "Maior sequência", best_sub),
        (str(s["repos"]), 1.0, t["purple"], "Repositórios", "públicos"),
    ]
    tw, gap = 206, 12
    for i, (num, frac, color, title, sub) in enumerate(tiles):
        x = 20 + i * (tw + gap)
        d = i * 0.15
        size = 20 if len(num) <= 3 else 16
        o.append(f'<g class="tile" style="animation-delay:{d}s">'
                 f'<rect x="{x}" y="50" width="{tw}" height="96" rx="10" fill="{t["card"]}" stroke="{t["stroke"]}"/>'
                 + ring(x + 50, 98, 30, frac, color, t, d + 0.2) +
                 f'<text x="{x+50}" y="{98 + size*0.36:.1f}" text-anchor="middle" class="num" style="font-size:{size}px">{num}</text>'
                 f'<text x="{x+94}" y="93" class="tl">{title}</text>'
                 f'<text x="{x+94}" y="112" class="ts">{escape(sub)}</text></g>')

    # heatmap
    hx, hy, cs = 20, 200, 15
    o.append(f'<text x="{hx}" y="182" class="lbl">ÚLTIMAS {WEEKS} SEMANAS</text>')
    mx = max((c for w in s["grid"] for _, c in w), default=0) or 1
    for wi, week in enumerate(s["grid"]):
        for d, c in week:
            lvl = 0 if c == 0 else max(1, min(4, -(-4 * c // mx)))
            row = (d.weekday() + 1) % 7
            o.append(f'<rect class="cell" style="animation-delay:{0.5 + wi*0.035:.3f}s" x="{hx + wi*cs}" y="{hy + row*cs}" '
                     f'width="12" height="12" rx="3" fill="{t["heat"][lvl]}"><title>{d.strftime("%d/%m/%Y")}: {c}</title></rect>')
    o.append(f'<rect class="scan" x="{hx-2}" y="{hy-3}" width="14" height="{7*cs+3}" rx="4" fill="{t["blue"]}" fill-opacity=".14"/>')
    ly = hy + 7 * cs + 22
    o.append(f'<text x="{hx}" y="{ly+9}" class="ts">menos</text>')
    for k in range(5):
        o.append(f'<rect x="{hx + 45 + k*15}" y="{ly}" width="12" height="12" rx="3" fill="{t["heat"][k]}"/>')
    o.append(f'<text x="{hx + 45 + 5*15 + 6}" y="{ly+9}" class="ts">mais</text>')

    # linguagens
    lx, lw = 470, 410
    o.append(f'<text x="{lx}" y="182" class="lbl">LINGUAGENS · REPOS PÚBLICOS</text>')
    o.append(f'<clipPath id="bar"><rect x="{lx}" y="200" width="{lw}" height="12" rx="6"/></clipPath>'
             f'<rect x="{lx}" y="200" width="{lw}" height="12" rx="6" fill="{t["track"]}"/><g clip-path="url(#bar)">')
    shown = sum(p for _, _, p in s["langs"]) or 100
    cx = lx
    for i, (name, color, pct) in enumerate(s["langs"]):
        w = lw * pct / shown
        o.append(f'<rect class="seg" style="animation-delay:{0.6 + i*0.12:.2f}s" x="{cx:.1f}" y="200" width="{w+0.5:.1f}" height="12" fill="{color}"/>')
        cx += w
    o.append("</g>")
    for i, (name, color, pct) in enumerate(s["langs"]):
        col, row = i % 2, i // 2
        x = lx + col * 210
        y = 245 + row * 28
        o.append(f'<g class="fade" style="animation-delay:{1.0 + i*0.1:.2f}s">'
                 f'<circle cx="{x+6}" cy="{y-4}" r="5" fill="{color}"/>'
                 f'<text x="{x+18}" y="{y}" class="ln">{escape(name)}</text>'
                 f'<text x="{x+190}" y="{y}" text-anchor="end" class="lp">{pct:.1f}%</text></g>')
    if not s["langs"]:
        o.append(f'<text x="{lx}" y="245" class="ts">Nenhuma linguagem encontrada</text>')
    o.append("</svg>")
    return "\n".join(o)


def main():
    stats = compute(fetch())
    os.makedirs(OUT, exist_ok=True)
    for name, t in THEMES.items():
        path = os.path.join(OUT, f"github-stats-{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(stats, t))
        print("gerado", path)


if __name__ == "__main__":
    main()
