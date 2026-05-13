#!/usr/bin/env python3
"""Build the GitHub Pages gallery from the visual-html-gen-ui catalog."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "skills" / "visual-html-gen-ui" / "catalog.json"
OUTPUT_PATH = REPO_ROOT / "index.html"


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    OUTPUT_PATH.write_text(render_page(catalog), encoding="utf-8")


def render_page(catalog: dict) -> str:
    domains = catalog["domains"]
    chart_count = sum(len(domain["charts"]) for domain in domains)
    toc = "\n".join(render_toc_link(domain) for domain in domains)
    sections = "\n\n".join(
        render_domain_section(index + 1, domain) for index, domain in enumerate(domains)
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Visual HTML Gen UI - Chart Gallery</title>
<style>
  :root {{
    --ivory:  #FAF9F5;
    --paper:  #FFFFFF;
    --slate:  #141413;
    --clay:   #D97757;
    --clay-d: #B85C3E;
    --oat:    #E3DACC;
    --olive:  #788C5D;
    --teal:   #4D8A8B;
    --blue:   #5277A3;
    --gold:   #C99A42;
    --g100:   #F0EEE6;
    --g200:   #E6E3DA;
    --g300:   #D1CFC5;
    --g500:   #87867F;
    --g700:   #3D3D3A;
    --serif: ui-serif, Georgia, "Times New Roman", Times, serif;
    --sans: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    --mono: ui-monospace, "SF Mono", Menlo, Monaco, Consolas, monospace;
    --toc-offset: 190px;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    background: var(--ivory);
    color: var(--slate);
    font-family: var(--sans);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}
  .wrap {{ max-width: 1120px; margin: 0 auto; padding: 0 32px 140px; }}
  header.masthead {{
    padding: 80px 0 56px;
    border-bottom: 1.5px solid var(--g300);
    margin-bottom: 12px;
  }}
  .hero-grid {{
    display: grid;
    grid-template-columns: 1fr 360px;
    gap: 48px;
    align-items: end;
  }}
  .eyebrow {{
    font-family: var(--mono);
    font-size: 12px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--g500);
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .eyebrow::before {{
    content: "";
    width: 24px;
    height: 1.5px;
    background: var(--clay);
  }}
  h1 {{
    font-family: var(--serif);
    font-weight: 500;
    font-size: 58px;
    line-height: 1.06;
    letter-spacing: 0;
    margin: 0 0 8px;
    max-width: none;
    white-space: nowrap;
  }}
  h1 em {{
    color: var(--clay);
    font-style: italic;
  }}
  .intro {{
    font-size: 16.5px;
    color: var(--g700);
    margin: 22px 0 0;
    max-width: 650px;
  }}
  code {{
    font-family: var(--mono);
    font-size: 0.92em;
    background: var(--g100);
    border: 1px solid var(--g300);
    border-radius: 5px;
    padding: 1px 5px;
  }}
  .hero-fig {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    align-items: end;
  }}
  .pane {{
    border-radius: 10px;
    border: 1.5px solid var(--g300);
    background: var(--paper);
    padding: 14px;
    aspect-ratio: 4/5;
    display: flex;
    flex-direction: column;
    gap: 7px;
    position: relative;
  }}
  .pane.domain {{
    background: var(--g100);
    transform: rotate(-2.5deg) translateY(6px);
  }}
  .pane.chart {{
    transform: rotate(1.5deg);
    border-color: var(--slate);
    box-shadow: 0 12px 32px rgba(20,20,19,.10);
  }}
  .tag {{
    position: absolute;
    top: -10px;
    left: 12px;
    font-family: var(--mono);
    font-size: 9.5px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    background: var(--ivory);
    padding: 2px 7px;
    border: 1.5px solid var(--g300);
    border-radius: 6px;
    color: var(--g500);
  }}
  .pane.chart .tag {{ border-color: var(--slate); color: var(--slate); }}
  .l {{ height: 6px; border-radius: 3px; background: var(--g300); }}
  .w90 {{ width: 90%; }} .w82 {{ width: 82%; }} .w75 {{ width: 75%; }}
  .w70 {{ width: 70%; }} .w60 {{ width: 60%; }} .w50 {{ width: 50%; }}
  .pane.chart .l {{ background: var(--g200); }}
  .blk {{
    border-radius: 5px;
    flex: 1;
    background: linear-gradient(135deg, var(--oat), #ECE1CF);
    position: relative;
    overflow: hidden;
  }}
  .blk::after {{
    content: "";
    position: absolute;
    left: 16%;
    right: 16%;
    top: 30%;
    height: 36%;
    border: 2px solid var(--clay);
    border-radius: 50%;
    opacity: .75;
  }}
  .row {{
    display: flex;
    gap: 6px;
    align-items: flex-end;
  }}
  .bar {{ flex: 1; border-radius: 3px 3px 0 0; }}
  .b1 {{ height: 14px; background: var(--olive); }}
  .b2 {{ height: 30px; background: var(--clay); }}
  .b3 {{ height: 20px; background: var(--oat); }}
  .b4 {{ height: 36px; background: var(--slate); }}
  nav.toc {{
    position: sticky;
    top: 12px;
    z-index: 20;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    padding: 14px 16px;
    margin: 18px -16px 10px;
    background: rgba(250, 249, 245, .94);
    border: 1.5px solid var(--g300);
    border-radius: 10px;
    backdrop-filter: blur(12px);
    transition: padding 180ms ease, border-color 180ms ease, box-shadow 180ms ease, background 180ms ease;
  }}
  nav.toc.is-stuck {{
    padding: 10px 12px;
    background: rgba(250, 249, 245, .97);
    box-shadow: 0 12px 30px rgba(20,20,19,.09);
  }}
  nav.toc a {{
    font-size: 12.5px;
    padding: 7px 14px;
    border: 1.5px solid var(--g300);
    border-radius: 999px;
    text-decoration: none;
    color: var(--g700);
    background: var(--paper);
    transition: border-color 120ms, color 120ms, background 120ms, transform 120ms;
    display: inline-flex;
    align-items: center;
    gap: 7px;
  }}
  nav.toc a .n {{
    font-family: var(--mono);
    font-size: 10px;
    color: var(--g500);
  }}
  nav.toc a:hover {{
    border-color: var(--slate);
    color: var(--slate);
    transform: translateY(-1px);
  }}
  nav.toc a:hover .n {{ color: var(--clay); }}
  nav.toc a.is-active {{
    border-color: var(--slate);
    color: var(--slate);
    background: var(--g100);
  }}
  nav.toc a.is-active .n {{ color: var(--clay); }}
  .summary {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin: 30px 0 0;
    max-width: 430px;
  }}
  .stat {{
    background: var(--paper);
    border: 1.5px solid var(--g300);
    border-radius: 8px;
    padding: 14px 16px 13px;
  }}
  .stat strong {{
    display: block;
    font-family: var(--serif);
    font-weight: 500;
    font-size: 30px;
    line-height: 1;
    margin-bottom: 7px;
  }}
  .stat span {{
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--g500);
  }}
  .toc-sentinel {{
    height: 1px;
    margin-top: -1px;
  }}
  details.domain-section {{
    margin-top: 72px;
    scroll-margin-top: var(--toc-offset);
  }}
  .domain-summary {{
    display: block;
    list-style: none;
    cursor: pointer;
    border-radius: 8px;
    padding: 8px 10px;
    margin: -8px -10px 10px;
    transition: background 140ms ease;
  }}
  .domain-summary::-webkit-details-marker {{ display: none; }}
  .domain-summary:hover {{ background: var(--g100); }}
  .domain-summary:focus-visible {{
    outline: 2px solid var(--clay);
    outline-offset: 4px;
  }}
  .sec-head {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 8px;
  }}
  .sec-head .idx {{
    font-family: var(--mono);
    font-size: 13px;
    color: var(--clay);
    font-weight: 600;
    width: 34px;
    flex-shrink: 0;
  }}
  .sec-head h2 {{
    font-family: var(--serif);
    font-weight: 500;
    font-size: 27px;
    margin: 0;
    letter-spacing: 0;
  }}
  .count {{
    font-family: var(--mono);
    font-size: 11px;
    color: var(--g500);
    background: var(--g100);
    padding: 2px 8px;
    border-radius: 999px;
    white-space: nowrap;
  }}
  .toggle {{
    margin-left: auto;
    width: 30px;
    height: 30px;
    border: 1.5px solid var(--g300);
    border-radius: 999px;
    background: var(--ivory);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    position: relative;
    flex-shrink: 0;
    transition: background 160ms ease, border-color 160ms ease;
  }}
  .toggle::before,
  .toggle::after {{
    content: "";
    position: absolute;
    left: 8px;
    right: 8px;
    top: 50%;
    height: 1.5px;
    background: var(--g700);
    border-radius: 999px;
    transform: translateY(-50%);
    transition: opacity 140ms ease, transform 160ms ease, background 160ms ease;
  }}
  .toggle::after {{
    transform: translateY(-50%) rotate(90deg);
  }}
  details[open] .toggle {{ background: var(--g100); }}
  details[open] .toggle::after {{
    opacity: 0;
    transform: translateY(-50%) rotate(90deg) scaleX(.2);
  }}
  .domain-summary:hover .toggle {{ border-color: var(--g500); }}
  .domain-summary:hover .toggle::before,
  .domain-summary:hover .toggle::after {{ background: var(--slate); }}
  .sec-intro {{
    font-size: 14.5px;
    color: var(--g700);
    max-width: 760px;
    margin: 0 0 24px 50px;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(316px, 1fr));
    gap: 20px;
    margin-left: 50px;
  }}
  a.card {{
    display: flex;
    flex-direction: column;
    background: var(--paper);
    border: 1.5px solid var(--g300);
    border-radius: 8px;
    text-decoration: none;
    color: inherit;
    transition: transform 150ms ease, box-shadow 150ms ease, border-color 150ms ease;
    overflow: hidden;
  }}
  a.card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(20,20,19,.10);
    border-color: var(--slate);
  }}
  .thumb {{
    height: 178px;
    background: var(--paper);
    border-bottom: 1.5px solid var(--g200);
    display: block;
    padding: 0;
    transition: background 150ms ease;
    overflow: hidden;
    position: relative;
  }}
  a.card:hover .thumb {{ background: var(--oat); }}
  .preview-frame {{
    width: 960px;
    height: 540px;
    border: 0;
    transform: scale(0.34);
    transform-origin: 0 0;
    pointer-events: none;
    background: var(--ivory);
  }}
  .preview-shade {{
    position: absolute;
    inset: auto 0 0;
    height: 32px;
    background: linear-gradient(to bottom, rgba(250,249,245,0), var(--paper));
    pointer-events: none;
  }}
  .body {{
    padding: 18px 20px 16px;
    display: flex;
    flex-direction: column;
    flex: 1;
  }}
  .title {{
    font-family: var(--serif);
    font-size: 19px;
    font-weight: 500;
    line-height: 1.22;
    color: var(--slate);
    margin-bottom: 7px;
    letter-spacing: 0;
  }}
  .desc {{
    font-size: 13.5px;
    color: var(--g700);
    line-height: 1.5;
    margin-bottom: 16px;
    flex: 1;
  }}
  .signals {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 0 0 14px;
  }}
  .signals span {{
    font-family: var(--mono);
    font-size: 10.5px;
    color: var(--g700);
    background: var(--g100);
    border: 1px solid var(--g200);
    border-radius: 999px;
    padding: 2px 7px;
  }}
  .file {{
    font-family: var(--mono);
    font-size: 11px;
    color: var(--g500);
    border-top: 1px solid var(--g100);
    padding-top: 11px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
  }}
  .file span:first-child {{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }}
  .arrow {{ transition: transform 150ms ease; color: var(--g300); }}
  a.card:hover .file {{ color: var(--clay); }}
  a.card:hover .arrow {{ transform: translateX(3px); color: var(--clay); }}
  footer {{
    margin-top: 100px;
    border-top: 1.5px solid var(--g300);
    padding-top: 36px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 20px;
    flex-wrap: wrap;
    font-size: 13px;
    color: var(--g500);
  }}
  footer .k {{ font-family: var(--serif); font-style: italic; color: var(--g700); font-size: 15px; }}
  footer a {{ color: var(--clay); text-decoration-color: var(--oat); text-underline-offset: 3px; }}
  @media (max-width: 880px) {{
    .hero-grid {{ grid-template-columns: 1fr; }}
    .hero-fig {{ max-width: 400px; margin-top: 28px; }}
    h1 {{ font-size: 48px; }}
  }}
  @media (max-width: 720px) {{
    .wrap {{ padding: 0 20px 96px; }}
    header.masthead {{ padding: 52px 0 38px; }}
    h1 {{ font-size: 38px; }}
    .summary {{ grid-template-columns: 1fr; }}
    nav.toc {{ margin-left: 0; margin-right: 0; }}
    .sec-intro, .grid {{ margin-left: 0; }}
    .sec-head {{ gap: 10px; flex-wrap: wrap; }}
    .sec-head .idx {{ width: auto; }}
    .toggle {{ margin-left: 0; }}
  }}
  @media (max-width: 420px) {{
    h1 {{ font-size: 32px; }}
    nav.toc a {{ font-size: 12px; padding: 6px 11px; }}
  }}
</style>
</head>
<body>
<div class="wrap">
  <header class="masthead">
    <div class="hero-grid">
      <div>
        <div class="eyebrow">Standalone chart HTML for agents</div>
        <h1>Visual HTML <em>Gen UI</em></h1>
        <p class="intro">
          A domain-indexed catalog of self-contained chart pages. Each file is a static
          <code>.html</code> reference an agent can open, inspect, and adapt without loading the whole library into context.
        </p>
        <div class="summary" aria-label="Catalog summary">
          <div class="stat"><strong>{len(domains)}</strong><span>domains</span></div>
          <div class="stat"><strong>{chart_count}</strong><span>chart pages</span></div>
        </div>
      </div>
      <div class="hero-fig" aria-hidden="true">
        <div class="pane domain">
          <span class="tag">domains</span>
          <span class="l w90"></span><span class="l w75"></span><span class="l w82"></span>
          <span class="l w60"></span><span class="l w90"></span><span class="l w70"></span>
          <span class="l w82"></span><span class="l w50"></span><span class="l w75"></span>
          <span class="l w90"></span><span class="l w60"></span>
        </div>
        <div class="pane chart">
          <span class="tag">charts</span>
          <span class="l w60"></span>
          <span class="blk"></span>
          <span class="row"><span class="bar b1"></span><span class="bar b2"></span><span class="bar b3"></span><span class="bar b4"></span></span>
          <span class="l w75"></span><span class="l w50"></span>
        </div>
      </div>
    </div>
  </header>
  <div class="toc-sentinel" aria-hidden="true"></div>
  <nav class="toc" aria-label="Domain table of contents">
{toc}
  </nav>

{sections}

  <footer>
    <span class="k">visual-html-gen-ui</span>
    <span>Generated from <code>skills/visual-html-gen-ui/catalog.json</code></span>
    <a href="https://github.com/iFurySt/visual-html-gen-ui">GitHub</a>
  </footer>
</div>
<script>
  const toc = document.querySelector(".toc");
  const sentinel = document.querySelector(".toc-sentinel");
  const tocLinks = [...document.querySelectorAll(".toc a")];
  const domains = [...document.querySelectorAll(".domain-section")];

  if (toc && sentinel) {{
    const updateTocOffset = () => {{
      document.documentElement.style.setProperty("--toc-offset", `${{toc.offsetHeight + 34}}px`);
    }};
    const updateTocState = () => {{
      toc.classList.toggle("is-stuck", window.scrollY > sentinel.offsetTop);
    }};
    updateTocOffset();
    updateTocState();
    window.addEventListener("scroll", updateTocState, {{ passive: true }});
    window.addEventListener("resize", () => {{
      updateTocOffset();
      updateTocState();
    }});
  }}

  const scrollToDomain = (target, behavior = "smooth") => {{
    const offset = (toc?.offsetHeight || 0) + 34;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({{ top: Math.max(0, top), behavior }});
  }};

  tocLinks.forEach((link) => {{
    link.addEventListener("click", (event) => {{
      event.preventDefault();
      const target = document.querySelector(link.getAttribute("href"));
      if (target && "open" in target) {{
        target.open = true;
        history.pushState(null, "", link.hash);
        scrollToDomain(target, "smooth");
        toc?.classList.add("is-stuck");
        tocLinks.forEach((item) => item.classList.remove("is-active"));
        link.classList.add("is-active");
      }}
    }});
  }});

  const openHashedDomain = () => {{
    if (!location.hash) {{
      return null;
    }}
    const target = document.querySelector(location.hash);
    if (target && "open" in target) {{
      target.open = true;
      return target;
    }}
    return null;
  }};

  const alignToHash = () => {{
    const target = openHashedDomain();
    if (!target) {{
      return;
    }}
    setTimeout(() => scrollToDomain(target, "auto"), 0);
    setTimeout(() => scrollToDomain(target, "auto"), 250);
  }};

  alignToHash();
  window.addEventListener("hashchange", alignToHash);

  if (tocLinks.length && domains.length) {{
    const activeById = new Map(tocLinks.map((link) => [link.hash.slice(1), link]));
    const setActiveDomain = (domain) => {{
      tocLinks.forEach((link) => link.classList.remove("is-active"));
      activeById.get(domain.id)?.classList.add("is-active");
    }};
    const updateActiveDomain = () => {{
      const stickyOffset = (toc?.offsetHeight || 0) + 28;
      const current = domains
        .filter((domain) => domain.getBoundingClientRect().top <= stickyOffset)
        .at(-1) || domains[0];
      setActiveDomain(current);
    }};
    updateActiveDomain();
    window.addEventListener("scroll", updateActiveDomain, {{ passive: true }});
    window.addEventListener("resize", updateActiveDomain);
  }}
</script>
</body>
</html>
"""


def render_toc_link(domain: dict) -> str:
    return (
        f'          <a href="#{html.escape(domain["slug"])}">'
        f'{html.escape(domain["name"])} <span class="n">{len(domain["charts"])}</span></a>'
    )


def render_domain_section(index: int, domain: dict) -> str:
    cards = "\n".join(render_card(domain, chart) for chart in domain["charts"])
    return f"""  <details class="domain-section" id="{html.escape(domain['slug'])}" open>
    <summary class="domain-summary">
      <div class="sec-head"><span class="idx">{index:02d}</span><h2>{html.escape(domain['name'])}</h2><span class="count">{len(domain['charts'])} charts</span><span class="toggle" aria-hidden="true"></span></div>
    </summary>
    <p class="sec-intro">{html.escape(domain['summary'])}</p>
    <div class="grid">
{cards}
    </div>
  </details>"""


def render_card(domain: dict, chart: dict) -> str:
    href = f"skills/visual-html-gen-ui/{domain['slug']}/{chart['slug']}.html"
    signal_tags = "".join(
        f"<span>{html.escape(signal)}</span>" for signal in chart.get("signals", [])[:3]
    )
    file_label = f"{domain['slug']}/{chart['slug']}.html"
    preview_doc = chart_preview_srcdoc(href)
    return f"""      <a class="card" href="{html.escape(href)}">
        <div class="thumb">
          <iframe class="preview-frame" srcdoc="{html.escape(preview_doc, quote=True)}" loading="lazy" title="{html.escape(chart['title'])} preview" tabindex="-1"></iframe>
          <span class="preview-shade" aria-hidden="true"></span>
        </div>
        <div class="body">
          <div class="title">{html.escape(chart["title"])}</div>
          <div class="desc">{html.escape(chart["purpose"])}</div>
          <div class="signals">{signal_tags}</div>
          <div class="file"><span>{html.escape(file_label)}</span><span class="arrow">-&gt;</span></div>
        </div>
      </a>"""


def chart_preview_srcdoc(href: str) -> str:
    chart_html = (REPO_ROOT / href).read_text(encoding="utf-8")
    style_match = re.search(r"<style>(.*?)</style>", chart_html, re.S)
    section_match = re.search(
        r'(<section id="chart-preview" class="frame"[\s\S]*?</section>)',
        chart_html,
    )
    if not style_match or not section_match:
        raise ValueError(f"unable to extract preview from {href}")

    base_style = style_match.group(1)
    section_html = section_match.group(1)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
{base_style}
html {{
  overflow: hidden;
}}
body {{
  margin: 0;
  padding: 14px;
  background: var(--ivory);
}}
.frame {{
  border-radius: 8px;
  padding: 18px;
}}
.note-grid {{
  display: none;
}}
</style>
</head>
<body>
{section_html}
</body>
</html>"""


if __name__ == "__main__":
    main()
