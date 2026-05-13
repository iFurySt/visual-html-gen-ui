#!/usr/bin/env python3
"""Build the visual-html-gen-ui skill from catalog.json."""

from __future__ import annotations

import html
import json
import math
import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"

PALETTE = {
    "ivory": "#FAF9F5",
    "paper": "#FFFFFF",
    "slate": "#141413",
    "clay": "#D97757",
    "rust": "#B04A3F",
    "oat": "#E3DACC",
    "olive": "#788C5D",
    "teal": "#4D8A8B",
    "blue": "#5277A3",
    "gold": "#C99A42",
    "gray100": "#F0EEE6",
    "gray300": "#D1CFC5",
    "gray500": "#87867F",
    "gray700": "#3D3D3A",
}


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    clean_domain_dirs(catalog)
    for domain in catalog["domains"]:
        for chart in domain["charts"]:
            chart_dir = ROOT / domain["slug"] / chart["slug"]
            chart_dir.mkdir(parents=True, exist_ok=True)
            (chart_dir / "index.html").write_text(
                render_chart_page(domain, chart),
                encoding="utf-8",
            )
    (ROOT / "SKILL.md").write_text(render_skill(catalog), encoding="utf-8")


def clean_domain_dirs(catalog: dict) -> None:
    keep = {domain["slug"] for domain in catalog["domains"]}
    skip = {"scripts"}
    for child in ROOT.iterdir():
        if not child.is_dir() or child.name in keep or child.name in skip:
            continue
        if child.name.startswith(".") or child.name == "__pycache__":
            continue
        shutil.rmtree(child)


def render_skill(catalog: dict) -> str:
    lines = [
        "---",
        f"name: {catalog['skill']['name']}",
        f"description: {catalog['skill']['description']}",
        "---",
        "",
        f"# {catalog['skill']['displayName']}",
        "",
        "Use this skill when you need a standalone HTML chart example for a",
        "specific product domain. Start here, choose the relevant domain and",
        "chart, then open only that chart's `index.html` file.",
        "",
        "The examples are self-contained HTML documents using inline CSS and",
        "SVG. They are intended as visual references that agents can adapt into",
        "product screens, reports, dashboards, and generated artifacts.",
        "",
        "## How To Use",
        "",
        "1. Pick the domain that matches the user's problem.",
        "2. Open the linked chart file, not the whole skill directory.",
        "3. Reuse the chart structure, labels, spacing, and interaction pattern",
        "   as a starting point.",
        "4. Replace sample data, copy, and colors with project-specific values.",
        "",
        "## Domain Catalog",
        "",
    ]

    for domain in catalog["domains"]:
        lines.extend(
            [
                f"### {domain['name']}",
                "",
                domain["summary"],
                "",
            ]
        )
        for chart in domain["charts"]:
            path = f"{domain['slug']}/{chart['slug']}/index.html"
            lines.append(f"- [{chart['title']}]({path}) - {chart['purpose']}")
        lines.append("")

    lines.extend(
        [
            "## Maintenance",
            "",
            "Maintainers should edit `catalog.json`, run",
            "`python3 scripts/build_charts.py`, then run",
            "`python3 scripts/validate_skill.py` before committing.",
            "",
        ]
    )
    return "\n".join(lines)


def render_chart_page(domain: dict, chart: dict) -> str:
    title = f"{domain['name']} - {chart['title']}"
    viz = render_visual(chart)
    signals = "\n".join(
        f"<li>{html.escape(signal)}</li>" for signal in chart.get("signals", [])
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
  :root {{
    --ivory: {PALETTE['ivory']};
    --paper: {PALETTE['paper']};
    --slate: {PALETTE['slate']};
    --clay: {PALETTE['clay']};
    --rust: {PALETTE['rust']};
    --oat: {PALETTE['oat']};
    --olive: {PALETTE['olive']};
    --teal: {PALETTE['teal']};
    --blue: {PALETTE['blue']};
    --gold: {PALETTE['gold']};
    --gray-100: {PALETTE['gray100']};
    --gray-300: {PALETTE['gray300']};
    --gray-500: {PALETTE['gray500']};
    --gray-700: {PALETTE['gray700']};
    --serif: ui-serif, Georgia, "Times New Roman", serif;
    --sans: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    --mono: ui-monospace, "SF Mono", Menlo, Monaco, Consolas, monospace;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--ivory);
    color: var(--slate);
    font-family: var(--sans);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}
  .page {{
    width: min(1120px, calc(100vw - 40px));
    margin: 0 auto;
    padding: 56px 0 96px;
  }}
  header {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 24px;
    align-items: end;
    margin-bottom: 28px;
    border-bottom: 1.5px solid var(--gray-300);
    padding-bottom: 22px;
  }}
  .eyebrow {{
    font-family: var(--mono);
    font-size: 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--gray-500);
    margin-bottom: 10px;
  }}
  h1 {{
    font-family: var(--serif);
    font-weight: 500;
    font-size: clamp(34px, 5vw, 56px);
    line-height: 1.04;
    letter-spacing: 0;
    margin: 0;
  }}
  .purpose {{
    max-width: 620px;
    margin: 16px 0 0;
    color: var(--gray-700);
    font-size: 16px;
  }}
  .stamp {{
    border: 1.5px solid var(--gray-300);
    background: var(--paper);
    border-radius: 8px;
    padding: 10px 12px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--gray-700);
    white-space: nowrap;
  }}
  .frame {{
    background: var(--paper);
    border: 1.5px solid var(--gray-300);
    border-radius: 8px;
    padding: 22px;
  }}
  .chart-head {{
    display: flex;
    justify-content: space-between;
    gap: 16px;
    align-items: start;
    margin-bottom: 16px;
  }}
  .chart-title {{
    font-family: var(--serif);
    font-size: 26px;
    line-height: 1.15;
    margin: 0;
    font-weight: 500;
  }}
  .chart-meta {{
    font-family: var(--mono);
    color: var(--gray-500);
    font-size: 12px;
  }}
  svg {{
    display: block;
    width: 100%;
    height: auto;
  }}
  .note-grid {{
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 18px;
    margin-top: 22px;
  }}
  .note {{
    border-top: 1.5px solid var(--gray-300);
    padding-top: 16px;
    color: var(--gray-700);
  }}
  .note h2 {{
    font-family: var(--mono);
    font-size: 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--gray-500);
    margin: 0 0 8px;
  }}
  .note p, .note ul {{ margin: 0; }}
  .note ul {{ padding-left: 18px; }}
  .axis {{ stroke: var(--gray-300); stroke-width: 1.5; }}
  .grid {{ stroke: var(--gray-100); stroke-width: 1.5; }}
  .label {{
    fill: var(--gray-500);
    font: 12px var(--mono);
  }}
  .small {{
    fill: var(--gray-700);
    font: 13px var(--sans);
  }}
  @media (max-width: 760px) {{
    .page {{ width: min(100vw - 28px, 1120px); padding-top: 32px; }}
    header, .note-grid {{ grid-template-columns: 1fr; }}
    .stamp {{ width: fit-content; }}
    .frame {{ padding: 16px; }}
    .chart-head {{ flex-direction: column; }}
  }}
</style>
</head>
<body>
<main class="page">
  <header>
    <div>
      <div class="eyebrow">{html.escape(domain['name'])} / {html.escape(chart['type'])}</div>
      <h1>{html.escape(chart['title'])}</h1>
      <p class="purpose">{html.escape(chart['purpose'])}</p>
    </div>
    <div class="stamp">standalone html</div>
  </header>

  <section class="frame" aria-label="{html.escape(chart['title'])} example">
    <div class="chart-head">
      <div>
        <h2 class="chart-title">{html.escape(sample_chart_title(chart))}</h2>
        <div class="chart-meta">{html.escape(sample_chart_meta(chart))}</div>
      </div>
      <div class="chart-meta">{html.escape(domain['slug'])}/{html.escape(chart['slug'])}</div>
    </div>
    {viz}
    <div class="note-grid">
      <div class="note">
        <h2>Use When</h2>
        <p>{html.escape(chart['purpose'])}</p>
      </div>
      <div class="note">
        <h2>Signals</h2>
        <ul>
          {signals}
        </ul>
      </div>
    </div>
  </section>
</main>
</body>
</html>
"""


def sample_chart_title(chart: dict) -> str:
    if "yield" in chart["slug"]:
        return "Treasury curve by maturity"
    if "cap-table" in chart["slug"]:
        return "Series B ownership snapshot"
    if "deal" in chart["slug"]:
        return "Pipeline conversion this quarter"
    if "unit" in chart["slug"]:
        return "Growth efficiency snapshot"
    return f"Sample {chart['title'].lower()}"


def sample_chart_meta(chart: dict) -> str:
    return "illustrative data / replace with project values"


def render_visual(chart: dict) -> str:
    chart_type = chart["type"]
    seed = sum(ord(ch) for ch in chart["slug"])
    random.seed(seed)
    if chart_type == "line":
        return svg_line(area=False)
    if chart_type == "area":
        return svg_line(area=True)
    if chart_type == "drawdown":
        return svg_drawdown()
    if chart_type == "grouped-bar":
        return svg_grouped_bar()
    if chart_type == "stacked-bar":
        return svg_stacked_bar()
    if chart_type == "horizontal-bar":
        return svg_horizontal_bar()
    if chart_type == "donut":
        return svg_donut()
    if chart_type == "scatter":
        return svg_scatter(bubbles=False)
    if chart_type == "bubble":
        return svg_scatter(bubbles=True)
    if chart_type == "heatmap":
        return svg_heatmap()
    if chart_type == "matrix":
        return svg_matrix()
    if chart_type == "calendar":
        return svg_calendar()
    if chart_type == "treemap":
        return svg_treemap()
    if chart_type == "candlestick":
        return svg_candlestick()
    if chart_type == "depth":
        return svg_depth()
    if chart_type == "frontier":
        return svg_frontier()
    if chart_type == "fan":
        return svg_fan()
    if chart_type == "funnel":
        return svg_funnel()
    if chart_type == "sankey":
        return svg_sankey()
    if chart_type == "waterfall":
        return svg_waterfall()
    if chart_type == "tornado":
        return svg_tornado()
    if chart_type == "radar":
        return svg_radar()
    if chart_type == "table":
        return html_table()
    if chart_type == "cohort":
        return html_cohort()
    if chart_type == "kpi":
        return html_kpi()
    if chart_type == "stress":
        return svg_stress()
    return svg_line(area=False)


def svg_shell(inner: str, height: int = 430) -> str:
    return f"""<svg viewBox="0 0 960 {height}" role="img" aria-label="Chart preview">
  <rect x="0" y="0" width="960" height="{height}" rx="8" fill="{PALETTE['ivory']}"/>
  {inner}
</svg>"""


def grid(width: int = 820, height: int = 300, x: int = 82, y: int = 54) -> str:
    lines = []
    for i in range(5):
        yy = y + i * height / 4
        lines.append(f'<line class="grid" x1="{x}" y1="{yy:.1f}" x2="{x + width}" y2="{yy:.1f}"/>')
    lines.append(f'<line class="axis" x1="{x}" y1="{y + height}" x2="{x + width}" y2="{y + height}"/>')
    lines.append(f'<line class="axis" x1="{x}" y1="{y}" x2="{x}" y2="{y + height}"/>')
    return "\n  ".join(lines)


def polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def svg_line(area: bool) -> str:
    values = [38, 42, 44, 51, 48, 57, 62, 68, 64, 71, 78, 84]
    x0, y0, width, height = 82, 54, 820, 300
    lo, hi = min(values) - 6, max(values) + 6
    points = [
        (x0 + i * width / (len(values) - 1), y0 + height - (v - lo) / (hi - lo) * height)
        for i, v in enumerate(values)
    ]
    area_path = ""
    if area:
        bottom = y0 + height
        area_points = [(points[0][0], bottom)] + points + [(points[-1][0], bottom)]
        area_path = f'<polygon points="{polyline(area_points)}" fill="{PALETTE["oat"]}" opacity="0.75"/>'
    labels = "".join(
        f'<text class="label" x="{82 + i * 164}" y="384">{label}</text>'
        for i, label in enumerate(["Jan", "Mar", "May", "Jul", "Sep", "Nov"])
    )
    inner = f"""{grid()}
  {area_path}
  <polyline points="{polyline(points)}" fill="none" stroke="{PALETTE['teal']}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="{points[-1][0]:.1f}" cy="{points[-1][1]:.1f}" r="6" fill="{PALETTE['clay']}"/>
  <text class="label" x="42" y="62">High</text>
  <text class="label" x="42" y="354">Low</text>
  {labels}"""
    return svg_shell(inner)


def svg_drawdown() -> str:
    values = [0, -3, -8, -5, -12, -22, -18, -11, -7, -4, -9, -2]
    x0, y0, width, height = 82, 54, 820, 300
    points = [
        (x0 + i * width / (len(values) - 1), y0 + abs(v) / 25 * height)
        for i, v in enumerate(values)
    ]
    bottom = y0
    area_points = [(points[0][0], bottom)] + points + [(points[-1][0], bottom)]
    inner = f"""{grid()}
  <line class="axis" x1="{x0}" y1="{y0}" x2="{x0 + width}" y2="{y0}"/>
  <polygon points="{polyline(area_points)}" fill="{PALETTE['rust']}" opacity="0.28"/>
  <polyline points="{polyline(points)}" fill="none" stroke="{PALETTE['rust']}" stroke-width="4" stroke-linecap="round"/>
  <text class="label" x="36" y="60">0%</text>
  <text class="label" x="30" y="354">-25%</text>"""
    return svg_shell(inner)


def svg_grouped_bar() -> str:
    labels = ["Q1", "Q2", "Q3", "Q4"]
    series = [[54, 62, 70, 78], [46, 52, 59, 66], [34, 41, 44, 52]]
    colors = [PALETTE["teal"], PALETTE["clay"], PALETTE["olive"]]
    bars = []
    x0, y0, width, height = 110, 54, 740, 300
    for i, label in enumerate(labels):
        base_x = x0 + i * 180
        bars.append(f'<text class="label" x="{base_x + 32}" y="386">{label}</text>')
        for j, values in enumerate(series):
            h = values[i] / 90 * height
            x = base_x + j * 34
            y = y0 + height - h
            bars.append(f'<rect x="{x}" y="{y:.1f}" width="26" height="{h:.1f}" rx="4" fill="{colors[j]}"/>')
    inner = f"{grid(width=760, x=82)}\n  " + "\n  ".join(bars)
    return svg_shell(inner)


def svg_stacked_bar() -> str:
    data = [[22, 18, 16], [26, 20, 19], [31, 22, 21], [34, 24, 26]]
    colors = [PALETTE["teal"], PALETTE["gold"], PALETTE["clay"]]
    bars = []
    for i, stack in enumerate(data):
        x = 150 + i * 170
        y = 354
        for j, value in enumerate(stack):
            h = value * 3.2
            y -= h
            bars.append(f'<rect x="{x}" y="{y:.1f}" width="86" height="{h:.1f}" fill="{colors[j]}"/>')
        bars.append(f'<text class="label" x="{x + 22}" y="386">S{i + 1}</text>')
    inner = f"{grid(width=760, x=82)}\n  " + "\n  ".join(bars)
    return svg_shell(inner)


def svg_horizontal_bar() -> str:
    labels = ["Value", "Quality", "Momentum", "Size", "Carry", "Low Vol"]
    values = [72, 58, 46, -28, 34, -18]
    rows = []
    xmid = 480
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 76 + i * 48
        rows.append(f'<text class="small" x="96" y="{y + 17}">{label}</text>')
        if value >= 0:
            rows.append(f'<rect x="{xmid}" y="{y}" width="{value * 4}" height="26" rx="5" fill="{PALETTE["teal"]}"/>')
        else:
            rows.append(f'<rect x="{xmid + value * 4}" y="{y}" width="{abs(value) * 4}" height="26" rx="5" fill="{PALETTE["rust"]}"/>')
    inner = f"""<line class="axis" x1="{xmid}" y1="50" x2="{xmid}" y2="360"/>
  {" ".join(rows)}"""
    return svg_shell(inner)


def svg_donut() -> str:
    slices = [(34, PALETTE["teal"]), (24, PALETTE["clay"]), (18, PALETTE["olive"]), (14, PALETTE["gold"]), (10, PALETTE["blue"])]
    cx, cy, r = 300, 210, 132
    start = -90
    paths = []
    labels = []
    names = ["Public equity", "Credit", "Cash", "Private", "Hedges"]
    for i, (value, color) in enumerate(slices):
        end = start + value / 100 * 360
        paths.append(donut_slice(cx, cy, r, 66, start, end, color))
        labels.append(f'<rect x="560" y="{116 + i * 42}" width="16" height="16" rx="3" fill="{color}"/><text class="small" x="588" y="{129 + i * 42}">{names[i]} {value}%</text>')
        start = end
    inner = "\n  ".join(paths + labels) + f'\n  <text x="{cx}" y="{cy - 6}" text-anchor="middle" font-family="var(--serif)" font-size="42" fill="{PALETTE["slate"]}">100%</text><text class="label" x="{cx}" y="{cy + 24}" text-anchor="middle">allocated</text>'
    return svg_shell(inner)


def donut_slice(cx: int, cy: int, r: int, inner: int, start: float, end: float, color: str) -> str:
    large = 1 if end - start > 180 else 0
    p1 = polar(cx, cy, r, start)
    p2 = polar(cx, cy, r, end)
    p3 = polar(cx, cy, inner, end)
    p4 = polar(cx, cy, inner, start)
    d = f"M {p1[0]:.1f} {p1[1]:.1f} A {r} {r} 0 {large} 1 {p2[0]:.1f} {p2[1]:.1f} L {p3[0]:.1f} {p3[1]:.1f} A {inner} {inner} 0 {large} 0 {p4[0]:.1f} {p4[1]:.1f} Z"
    return f'<path d="{d}" fill="{color}"/>'


def polar(cx: int, cy: int, r: int, angle: float) -> tuple[float, float]:
    rad = math.radians(angle)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def svg_scatter(bubbles: bool) -> str:
    points = [(18, 9, 12), (24, 13, 18), (31, 11, 10), (39, 17, 22), (47, 20, 28), (54, 22, 16), (63, 29, 34), (71, 26, 20)]
    dots = []
    for x, y, size in points:
        cx = 92 + x / 80 * 800
        cy = 354 - y / 34 * 288
        r = size / 3 if bubbles else 6
        dots.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{PALETTE["teal"]}" opacity="0.78"/>')
    inner = f"""{grid()}
  {" ".join(dots)}
  <text class="label" x="410" y="406">Volatility</text>
  <text class="label" x="24" y="210" transform="rotate(-90 24 210)">Return</text>"""
    return svg_shell(inner)


def svg_heatmap() -> str:
    rows = ["Tech", "Banks", "Energy", "Health", "Retail"]
    cols = ["Mon", "Tue", "Wed", "Thu", "Fri", "Wk"]
    cells = []
    for r, row in enumerate(rows):
        cells.append(f'<text class="small" x="58" y="{96 + r * 48}">{row}</text>')
        for c, _ in enumerate(cols):
            val = (r * 13 + c * 17) % 9
            colors = [PALETTE["rust"], "#CF6B52", PALETTE["oat"], "#9BAE78", PALETTE["olive"]]
            color = colors[min(4, max(0, val // 2))]
            cells.append(f'<rect x="{150 + c * 112}" y="{70 + r * 48}" width="88" height="34" rx="5" fill="{color}"/>')
    for c, col in enumerate(cols):
        cells.append(f'<text class="label" x="{176 + c * 112}" y="48">{col}</text>')
    return svg_shell("\n  ".join(cells), height=380)


def svg_matrix() -> str:
    labels = ["SPX", "NQ", "UST", "HY", "Gold", "BTC"]
    cells = []
    for r, row in enumerate(labels):
        cells.append(f'<text class="label" x="90" y="{91 + r * 44}">{row}</text>')
        cells.append(f'<text class="label" x="{158 + r * 72}" y="48">{row}</text>')
        for c, _ in enumerate(labels):
            distance = abs(r - c)
            color = [PALETTE["teal"], "#88B0A6", PALETTE["oat"], "#D99B7C", PALETTE["rust"]][min(distance, 4)]
            cells.append(f'<rect x="{146 + c * 72}" y="{66 + r * 44}" width="52" height="32" rx="4" fill="{color}"/>')
    return svg_shell("\n  ".join(cells), height=380)


def svg_calendar() -> str:
    cells = []
    for week in range(13):
        for day in range(5):
            val = (week * 7 + day * 5) % 6
            color = [PALETTE["gray100"], PALETTE["oat"], "#BFCB9D", PALETTE["olive"], PALETTE["teal"], PALETTE["clay"]][val]
            cells.append(f'<rect x="{94 + week * 58}" y="{82 + day * 48}" width="36" height="32" rx="5" fill="{color}"/>')
    months = "".join(f'<text class="label" x="{96 + i * 174}" y="52">{m}</text>' for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May"]))
    return svg_shell(months + "\n  " + "\n  ".join(cells), height=380)


def svg_treemap() -> str:
    rects = [
        (60, 60, 310, 230, PALETTE["teal"], "Mega cap"),
        (382, 60, 210, 138, PALETTE["olive"], "Banks"),
        (604, 60, 256, 138, PALETTE["clay"], "Energy"),
        (382, 212, 154, 120, PALETTE["gold"], "Health"),
        (548, 212, 144, 120, PALETTE["blue"], "Retail"),
        (704, 212, 156, 120, PALETTE["oat"], "Cash"),
    ]
    parts = []
    for x, y, w, h, color, label in rects:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{color}"/><text x="{x + 16}" y="{y + 30}" font-family="var(--sans)" font-size="15" fill="{PALETTE["slate"]}">{label}</text>')
    return svg_shell("\n  ".join(parts), height=390)


def svg_candlestick() -> str:
    candles = []
    for i in range(14):
        x = 104 + i * 56
        high = 78 + (i * 19) % 94
        low = high + 118 + (i * 11) % 54
        open_y = high + 42 + (i * 13) % 48
        close_y = high + 44 + ((i + 3) * 17) % 58
        color = PALETTE["teal"] if close_y < open_y else PALETTE["rust"]
        body_y = min(open_y, close_y)
        body_h = max(18, abs(close_y - open_y))
        candles.append(f'<line x1="{x}" y1="{high}" x2="{x}" y2="{low}" stroke="{color}" stroke-width="3"/><rect x="{x - 12}" y="{body_y}" width="24" height="{body_h}" rx="3" fill="{color}"/>')
    return svg_shell(f"{grid()}\n  " + "\n  ".join(candles))


def svg_depth() -> str:
    bids = [(82, 310), (190, 284), (302, 246), (416, 190), (480, 132)]
    asks = [(480, 132), (548, 184), (662, 224), (790, 270), (902, 310)]
    inner = f"""{grid()}
  <polygon points="82,354 {polyline(bids)} 480,354" fill="{PALETTE['teal']}" opacity="0.28"/>
  <polyline points="{polyline(bids)}" fill="none" stroke="{PALETTE['teal']}" stroke-width="4"/>
  <polygon points="480,354 {polyline(asks)} 902,354" fill="{PALETTE['rust']}" opacity="0.24"/>
  <polyline points="{polyline(asks)}" fill="none" stroke="{PALETTE['rust']}" stroke-width="4"/>
  <line x1="480" y1="72" x2="480" y2="354" stroke="{PALETTE['slate']}" stroke-dasharray="5 6"/>
  <text class="label" x="440" y="386">mid price</text>"""
    return svg_shell(inner)


def svg_frontier() -> str:
    frontier = [(120, 320), (210, 260), (330, 205), (480, 166), (650, 138), (820, 128)]
    dots = []
    for i in range(20):
        x = 124 + (i * 41) % 690
        y = 324 - ((i * 37) % 190)
        dots.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{PALETTE["gray500"]}" opacity="0.55"/>')
    inner = f"""{grid()}
  {" ".join(dots)}
  <polyline points="{polyline(frontier)}" fill="none" stroke="{PALETTE['clay']}" stroke-width="4"/>
  <circle cx="480" cy="166" r="8" fill="{PALETTE['teal']}"/>
  <text class="label" x="410" y="406">Volatility</text>
  <text class="label" x="24" y="214" transform="rotate(-90 24 214)">Expected return</text>"""
    return svg_shell(inner)


def svg_fan() -> str:
    x0, y0, width, height = 82, 54, 820, 300
    xs = [x0 + i * width / 7 for i in range(8)]
    low = [(x, y0 + height - (40 + i * 2) / 96 * height) for i, x in enumerate(xs)]
    mid = [(x, y0 + height - (52 + i * 6) / 96 * height) for i, x in enumerate(xs)]
    high = [(x, y0 + height - (68 + i * 9) / 96 * height) for i, x in enumerate(xs)]
    band = low + list(reversed(high))
    inner = f"""{grid()}
  <polygon points="{polyline(band)}" fill="{PALETTE['oat']}" opacity="0.85"/>
  <polyline points="{polyline(mid)}" fill="none" stroke="{PALETTE['teal']}" stroke-width="4"/>
  <text class="label" x="740" y="104">P90</text>
  <text class="label" x="740" y="308">P10</text>"""
    return svg_shell(inner)


def svg_funnel() -> str:
    widths = [760, 620, 460, 300, 170]
    labels = ["Sourced", "Screened", "Partner review", "Term sheet", "Closed"]
    parts = []
    for i, w in enumerate(widths):
        x = 480 - w / 2
        y = 58 + i * 58
        color = [PALETTE["teal"], PALETTE["olive"], PALETTE["gold"], PALETTE["clay"], PALETTE["rust"]][i]
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="42" rx="6" fill="{color}"/><text x="480" y="{y + 27}" text-anchor="middle" font-family="var(--sans)" font-size="15" fill="{PALETTE["slate"]}">{labels[i]}</text>')
    return svg_shell("\n  ".join(parts), height=390)


def svg_sankey() -> str:
    flows = [
        ("LPs", 80, 112, "Fund", 430, 166, PALETTE["teal"]),
        ("Balance sheet", 80, 246, "Fund", 430, 166, PALETTE["olive"]),
        ("Fund", 530, 166, "Equity", 780, 92, PALETTE["clay"]),
        ("Fund", 530, 166, "Credit", 780, 196, PALETTE["gold"]),
        ("Fund", 530, 166, "Reserves", 780, 296, PALETTE["blue"]),
    ]
    parts = []
    for _, x1, y1, _, x2, y2, color in flows:
        parts.append(f'<path d="M{x1 + 110},{y1} C{x1 + 220},{y1} {x2 - 120},{y2} {x2},{y2}" fill="none" stroke="{color}" stroke-width="28" opacity="0.55"/>')
    nodes = [("LPs", 80, 82), ("Balance sheet", 80, 216), ("Fund", 420, 136), ("Equity", 780, 62), ("Credit", 780, 166), ("Reserves", 780, 266)]
    for label, x, y in nodes:
        parts.append(f'<rect x="{x}" y="{y}" width="126" height="60" rx="8" fill="{PALETTE["paper"]}" stroke="{PALETTE["gray300"]}" stroke-width="1.5"/><text class="small" x="{x + 14}" y="{y + 36}">{label}</text>')
    return svg_shell("\n  ".join(parts), height=390)


def svg_waterfall() -> str:
    vals = [180, -42, -28, 36, -18, 128]
    labels = ["Revenue", "COGS", "Opex", "Other", "Tax", "Net"]
    parts = []
    baseline = 340
    running = 0
    for i, value in enumerate(vals):
        x = 100 + i * 130
        h = abs(value) * 1.2
        if i == 0 or i == len(vals) - 1:
            y = baseline - h
            color = PALETTE["teal"]
        else:
            y = baseline - (running + max(value, 0)) * 1.2
            color = PALETTE["olive"] if value > 0 else PALETTE["rust"]
        parts.append(f'<rect x="{x}" y="{y:.1f}" width="76" height="{h:.1f}" rx="5" fill="{color}"/><text class="label" x="{x}" y="374">{labels[i]}</text>')
        running += value if i != len(vals) - 1 else 0
    return svg_shell(f"{grid(width=790)}\n  " + "\n  ".join(parts))


def svg_tornado() -> str:
    labels = ["Exit multiple", "Revenue CAGR", "Gross margin", "WACC", "Churn", "Opex ratio"]
    parts = []
    for i, label in enumerate(labels):
        y = 70 + i * 45
        left = 120 - i * 12
        right = 160 - i * 10
        parts.append(f'<text class="small" x="98" y="{y + 18}">{label}</text><rect x="{480 - left}" y="{y}" width="{left}" height="26" rx="5" fill="{PALETTE["rust"]}"/><rect x="480" y="{y}" width="{right}" height="26" rx="5" fill="{PALETTE["teal"]}"/>')
    return svg_shell(f'<line class="axis" x1="480" y1="50" x2="480" y2="350"/>\n  {" ".join(parts)}')


def svg_radar() -> str:
    cx, cy = 480, 210
    axes = ["Growth", "Margin", "Moat", "Team", "Risk", "Timing"]
    rings = []
    for r in [55, 100, 145]:
        pts = [polar(cx, cy, r, -90 + i * 60) for i in range(6)]
        rings.append(f'<polygon points="{polyline(pts)}" fill="none" stroke="{PALETTE["gray300"]}" stroke-width="1.5"/>')
    scores = [132, 92, 118, 142, 74, 106]
    pts = [polar(cx, cy, scores[i], -90 + i * 60) for i in range(6)]
    labels = []
    for i, label in enumerate(axes):
        lx, ly = polar(cx, cy, 174, -90 + i * 60)
        labels.append(f'<text class="label" x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle">{label}</text>')
    inner = "\n  ".join(rings + [f'<polygon points="{polyline(pts)}" fill="{PALETTE["teal"]}" opacity="0.35" stroke="{PALETTE["teal"]}" stroke-width="4"/>'] + labels)
    return svg_shell(inner, height=430)


def html_table() -> str:
    rows = [
        ("Founders", "42.0%", "Common", "0.0%"),
        ("Seed investors", "18.5%", "Preferred", "1.0x"),
        ("Series A", "24.0%", "Preferred", "1.0x"),
        ("Series B", "12.5%", "Preferred", "1.5x"),
        ("Option pool", "3.0%", "Common", "0.0%"),
    ]
    body = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows
    )
    return f"""<div style="overflow:auto">
  <table style="width:100%; border-collapse:separate; border-spacing:0; border:1.5px solid {PALETTE['gray300']}; border-radius:8px; overflow:hidden">
    <thead><tr style="background:{PALETTE['gray100']}"><th>Holder</th><th>Ownership</th><th>Class</th><th>Preference</th></tr></thead>
    <tbody>{body}</tbody>
  </table>
</div>
<style>
  th, td {{ text-align:left; padding:14px 16px; border-bottom:1px solid {PALETTE['gray100']}; white-space:nowrap; }}
  th {{ font:600 12px var(--mono); color:{PALETTE['gray500']}; text-transform:uppercase; letter-spacing:.06em; }}
  td {{ font-size:14px; color:{PALETTE['gray700']}; }}
</style>"""


def html_cohort() -> str:
    rows = []
    cohorts = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    for r, cohort in enumerate(cohorts):
        cells = [f"<th>{cohort}</th>"]
        for c in range(6):
            if c < r:
                cells.append("<td></td>")
            else:
                value = max(38, 96 - (c - r) * 11 - r * 3)
                shade = 100 - value
                color = f"color-mix(in srgb, {PALETTE['teal']} {value}%, {PALETTE['ivory']})"
                cells.append(f'<td style="background:{color}">{value}%</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return f"""<div style="overflow:auto">
  <table class="cohort"><tbody>{''.join(rows)}</tbody></table>
</div>
<style>
  table.cohort {{ width:100%; border-collapse:separate; border-spacing:6px; }}
  .cohort th, .cohort td {{ min-width:92px; height:44px; border-radius:6px; text-align:center; font:13px var(--mono); }}
  .cohort th {{ color:{PALETTE['gray500']}; background:{PALETTE['gray100']}; }}
  .cohort td {{ color:{PALETTE['slate']}; }}
</style>"""


def html_kpi() -> str:
    cards = [
        ("CAC", "$4.2k", "-8% q/q"),
        ("LTV", "$31.8k", "7.6x CAC"),
        ("Payback", "9.4 mo", "healthy"),
        ("Burn multiple", "1.3x", "improving"),
    ]
    html_cards = "\n".join(
        f'<div class="kpi"><span>{label}</span><strong>{value}</strong><em>{meta}</em></div>'
        for label, value, meta in cards
    )
    return f"""<div class="kpi-grid">{html_cards}</div>
<style>
  .kpi-grid {{ display:grid; grid-template-columns:repeat(4, 1fr); gap:14px; }}
  .kpi {{ border:1.5px solid {PALETTE['gray300']}; border-radius:8px; padding:18px; background:{PALETTE['ivory']}; }}
  .kpi span {{ display:block; font:12px var(--mono); color:{PALETTE['gray500']}; text-transform:uppercase; letter-spacing:.06em; }}
  .kpi strong {{ display:block; font:500 34px var(--serif); color:{PALETTE['slate']}; margin:8px 0; }}
  .kpi em {{ font-style:normal; color:{PALETTE['olive']}; font:13px var(--mono); }}
  @media (max-width:760px) {{ .kpi-grid {{ grid-template-columns:1fr 1fr; }} }}
</style>"""


def svg_stress() -> str:
    bars = [46, 72, 110, 138, 178]
    labels = ["Base", "1d VaR", "10d VaR", "2008", "Liquidity"]
    parts = []
    for i, value in enumerate(bars):
        x = 140 + i * 140
        y = 342 - value
        color = [PALETTE["teal"], PALETTE["olive"], PALETTE["gold"], PALETTE["clay"], PALETTE["rust"]][i]
        parts.append(f'<rect x="{x}" y="{y}" width="86" height="{value}" rx="5" fill="{color}"/><text class="label" x="{x}" y="374">{labels[i]}</text>')
    return svg_shell(f"{grid(width=780)}\n  " + "\n  ".join(parts))


if __name__ == "__main__":
    main()
