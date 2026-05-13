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

DOMAIN_PROFILES = {
    "finance": {
        "metric": "Portfolio NAV",
        "unit": "index points",
        "periods": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "categories": ["Large cap", "Credit", "Private equity", "Rates", "Cash", "Hedges"],
        "segments": ["Equity", "Credit", "Cash", "Private", "Hedges"],
        "stages": ["Sourced", "Screened", "Partner review", "Term sheet", "Closed"],
        "drivers": ["Revenue", "COGS", "Opex", "Other", "Tax", "Net"],
        "assumptions": ["Exit multiple", "Revenue CAGR", "Gross margin", "WACC", "Churn", "Opex ratio"],
        "scenarios": ["Base", "1d VaR", "10d VaR", "2008", "Liquidity"],
        "radar": ["Growth", "Margin", "Moat", "Team", "Risk", "Timing"],
        "x_axis": "Volatility",
        "y_axis": "Return",
        "flows": ["LPs", "Balance sheet", "Fund", "Equity", "Credit", "Reserves"],
    },
    "office": {
        "metric": "Focus hours",
        "unit": "hours per teammate",
        "periods": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sprint", "Review", "Ship"],
        "categories": ["Meetings", "Deep work", "Approvals", "Docs", "Support", "Handoffs"],
        "segments": ["Meetings", "Tasks", "Docs", "Reviews", "Admin"],
        "stages": ["Sent", "Opened", "Replied", "Assigned", "Resolved"],
        "drivers": ["Planned", "Meetings", "Review", "Legal", "Exec", "Available"],
        "assumptions": ["Hiring", "Meeting load", "Review SLA", "Focus time", "Blocked work", "Support load"],
        "scenarios": ["Base", "Launch week", "Reorg", "Hiring freeze", "Incident"],
        "radar": ["Urgency", "Ambiguity", "Dependency", "Load", "Morale", "Focus"],
        "x_axis": "Workload",
        "y_axis": "Cycle time",
        "flows": ["Draft", "Review", "Approval", "Archive", "Legal", "Finance"],
    },
    "education": {
        "metric": "Mastery score",
        "unit": "student percentile",
        "periods": ["Week 1", "Week 2", "Week 3", "Week 4", "Midterm", "Week 6", "Week 7", "Final"],
        "categories": ["Algebra", "Reading", "Science", "Writing", "Projects", "Attendance"],
        "segments": ["Module A", "Module B", "Module C", "Practice", "Assessment"],
        "stages": ["Flagged", "Outreach", "Tutoring", "Practice", "Recovered"],
        "drivers": ["Baseline", "Practice", "Absence", "Tutoring", "Exam", "Mastery"],
        "assumptions": ["Time limit", "Question mix", "Reading load", "Prereqs", "Hints", "Retakes"],
        "scenarios": ["Standard", "Timed", "Advanced", "Remote", "No support"],
        "radar": ["Concepts", "Fluency", "Reasoning", "Writing", "Collab", "Confidence"],
        "x_axis": "Study hours",
        "y_axis": "Mastery",
        "flows": ["Intro", "Practice", "Quiz", "Project", "Pass", "Retake"],
    },
    "health": {
        "metric": "Care quality",
        "unit": "clinical score",
        "periods": ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Week 2", "Week 3", "Week 4"],
        "categories": ["Triage", "Consult", "Labs", "Treatment", "Follow-up", "Discharge"],
        "segments": ["Primary", "Specialist", "Pharmacy", "Remote", "Emergency"],
        "stages": ["Intake", "Triage", "Consult", "Treatment", "Discharge"],
        "drivers": ["Baseline", "Staffing", "Labs", "Medication", "Follow-up", "Outcome"],
        "assumptions": ["Acuity", "Staffing", "No-show", "Adherence", "Bed supply", "Readmit"],
        "scenarios": ["Base", "Flu surge", "No-shows", "Staff gap", "Readmit spike"],
        "radar": ["Safety", "Access", "Experience", "Efficacy", "Cost", "Equity"],
        "x_axis": "Risk score",
        "y_axis": "Care cost",
        "flows": ["Referral", "Diagnosis", "Treatment", "Follow-up", "Recovered", "Escalated"],
    },
    "ecommerce": {
        "metric": "Gross merchandise value",
        "unit": "USD thousands",
        "periods": ["Search", "View", "Cart", "Checkout", "Pay", "Repeat", "Loyalty", "Winback"],
        "categories": ["Apparel", "Beauty", "Home", "Electronics", "Grocery", "Sports"],
        "segments": ["Organic", "Paid", "Email", "Marketplace", "Stores"],
        "stages": ["View", "Cart", "Checkout", "Payment", "Purchase"],
        "drivers": ["List price", "Discount", "Shipping", "Returns", "Fees", "Margin"],
        "assumptions": ["Price", "Discount", "Shipping", "Ad spend", "Return rate", "Stockout"],
        "scenarios": ["Base", "Promo", "Stockout", "Free ship", "Return spike"],
        "radar": ["Traffic", "Conversion", "Margin", "Inventory", "Loyalty", "Service"],
        "x_axis": "CAC",
        "y_axis": "LTV",
        "flows": ["Product view", "Cart", "Bundle", "Checkout", "Purchase", "Repeat"],
    },
    "social": {
        "metric": "Active users",
        "unit": "daily users",
        "periods": ["D1", "D3", "D7", "D14", "D21", "D30", "D45", "D60"],
        "categories": ["Creators", "Comments", "Shares", "Groups", "Moderation", "Messages"],
        "segments": ["Video", "Text", "Live", "Groups", "DM"],
        "stages": ["Signup", "Profile", "Follow", "First post", "Return"],
        "drivers": ["New users", "Posts", "Reports", "Appeals", "Backlog", "Resolved"],
        "assumptions": ["Feed rank", "Creator supply", "Safety", "Notifications", "Churn", "Virality"],
        "scenarios": ["Base", "Viral post", "Safety event", "Creator drop", "Spam wave"],
        "radar": ["Safety", "Activity", "Diversity", "Supply", "Retention", "Trust"],
        "x_axis": "Reach",
        "y_axis": "Engagement",
        "flows": ["Creator", "Topic", "Community", "Follow", "Share", "Return"],
    },
    "entertainment": {
        "metric": "Watch time",
        "unit": "streaming hours",
        "periods": ["Pre", "Launch", "Wk 1", "Wk 2", "Wk 3", "Wk 4", "Catalog", "Long tail"],
        "categories": ["Drama", "Comedy", "Music", "Sports", "Kids", "Documentary"],
        "segments": ["Trailer", "Premiere", "Search", "Playlist", "Recommendation"],
        "stages": ["Awareness", "Trailer", "Follow", "Intent", "Purchase"],
        "drivers": ["Opening", "Marketing", "Theaters", "Streaming", "Licensing", "Profit"],
        "assumptions": ["Release date", "Campaign", "Reviews", "Churn", "Catalog pull", "Price"],
        "scenarios": ["Base", "Hit", "Weak reviews", "Delay", "Platform promo"],
        "radar": ["Reach", "Loyalty", "Monetization", "Brand fit", "Buzz", "Shelf life"],
        "x_axis": "Audience size",
        "y_axis": "Engagement rate",
        "flows": ["Trailer", "Show", "Playlist", "Channel", "Ticket", "Merch"],
    },
    "gaming": {
        "metric": "Daily active players",
        "unit": "players",
        "periods": ["Patch", "D1", "D3", "D7", "D14", "Event", "Season", "Finale"],
        "categories": ["Tutorial", "PvP", "Co-op", "Store", "Guilds", "Ranked"],
        "segments": ["Currency", "Cosmetics", "Boosts", "Events", "Inventory"],
        "stages": ["Install", "Tutorial", "Level 5", "Core loop", "Return"],
        "drivers": ["Base fare", "Rewards", "Store", "Fees", "Support", "Net"],
        "assumptions": ["Damage", "Cooldown", "XP rate", "Drop rate", "Match size", "Queue"],
        "scenarios": ["Base", "Patch", "Event", "Outage", "Balance change"],
        "radar": ["Skill", "Spend", "Social", "Completion", "Risk", "Retention"],
        "x_axis": "Workload",
        "y_axis": "Injury risk",
        "flows": ["Source", "Sink", "Wallet", "Store", "Crafting", "Inventory"],
    },
}

PROFILE_FALLBACKS = {
    "content-creation": ("Audience reach", "views", ["Ideas", "Draft", "Edit", "Schedule", "Publish", "Repurpose"], ["Shorts", "Newsletter", "Podcast", "Guide", "Community"]),
    "enterprise-services": ("Annual recurring revenue", "USD thousands", ["Leads", "Qualified", "Proposal", "Legal", "Closed", "Renewed"], ["SMB", "Mid-market", "Enterprise", "Support", "Services"]),
    "cybersecurity": ("Open risk", "risk points", ["Identity", "Endpoint", "Network", "Cloud", "Data", "Training"], ["Critical", "High", "Medium", "Low", "Accepted"]),
    "ai-agent": ("Task success rate", "eval pass rate", ["Planning", "Search", "Code", "Browser", "Verify", "Ship"], ["Model", "Tools", "Latency", "Cost", "Safety"]),
    "real-estate": ("Net operating income", "USD thousands", ["Office", "Retail", "Industrial", "Multifamily", "Hospitality", "Land"], ["Inquiry", "Tour", "Offer", "Lease", "Move-in"]),
    "hr": ("Headcount plan", "employees", ["Engineering", "Sales", "Ops", "Design", "Support", "People"], ["Sourced", "Screen", "Onsite", "Offer", "Accepted"]),
    "mobility": ("Trip volume", "rides", ["Airport", "Downtown", "Suburb", "Campus", "Events", "Depot"], ["Request", "Matched", "Accepted", "Arrived", "Completed"]),
    "travel": ("Booking demand", "bookings", ["Paris", "Tokyo", "NYC", "Beach", "Mountain", "Business"], ["Search", "Quote", "Checkout", "Confirm", "Check-in"]),
    "biotech": ("Biomarker response", "assay score", ["Target A", "Target B", "CMC", "Safety", "Sites", "Regulatory"], ["Screened", "Eligible", "Consented", "Randomized", "Completed"]),
    "legal": ("Matter volume", "open matters", ["Contracts", "Privacy", "Labor", "IP", "Litigation", "Compliance"], ["Intake", "Redline", "Negotiate", "Approve", "Sign"]),
    "government": ("Service demand", "cases", ["Permits", "Benefits", "Transit", "Housing", "Public works", "Health"], ["Submitted", "Reviewed", "Corrected", "Approved", "Issued"]),
    "manufacturing": ("Production output", "units", ["Line A", "Line B", "Quality", "Maintenance", "Suppliers", "Shipping"], ["Created", "Triaged", "Scheduled", "Completed", "Verified"]),
    "energy": ("Grid load", "MWh", ["Solar", "Wind", "Gas", "Storage", "Hydro", "Imports"], ["Forecast", "Dispatch", "Storage", "Grid", "Load"]),
    "retail": ("Same-store sales", "USD thousands", ["Grocery", "Apparel", "Pharmacy", "Home", "Beauty", "Electronics"], ["Exposure", "Redeem", "Purchase", "Repeat", "Loyalty"]),
    "crypto": ("Protocol volume", "USD millions", ["Wallets", "Pools", "Bridge", "DEX", "Lending", "Staking"], ["Wallet", "Pool", "Bridge", "Protocol", "Treasury"]),
    "fashion": ("Sell-through rate", "units sold", ["Outerwear", "Denim", "Footwear", "Accessories", "Knitwear", "Runway"], ["Concept", "Sample", "Buy", "Launch", "Sold-through"]),
    "sports": ("Team rating", "performance index", ["Starters", "Bench", "Training", "Tickets", "Media", "Merch"], ["Reach", "Engage", "Intent", "Purchase", "Renew"]),
    "pets": ("Wellness score", "care score", ["Food", "Vet", "Grooming", "Insurance", "Toys", "Training"], ["Listed", "Viewed", "Applied", "Visited", "Adopted"]),
}


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    clean_domain_dirs(catalog)
    for domain in catalog["domains"]:
        for chart in domain["charts"]:
            domain_dir = ROOT / domain["slug"]
            domain_dir.mkdir(parents=True, exist_ok=True)
            (domain_dir / f"{chart['slug']}.html").write_text(
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

    for domain in catalog["domains"]:
        domain_dir = ROOT / domain["slug"]
        if not domain_dir.exists():
            continue
        expected = {f"{chart['slug']}.html" for chart in domain["charts"]}
        for child in domain_dir.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
                continue
            if child.suffix == ".html" and child.name not in expected:
                child.unlink()


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
        "chart, then open only that chart's HTML file.",
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
            path = f"{domain['slug']}/{chart['slug']}.html"
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
    data = sample_data(domain, chart)
    viz = render_visual(domain, chart, data)
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

  <section id="chart-preview" class="frame" aria-label="{html.escape(chart['title'])} example">
    <div class="chart-head">
      <div>
        <h2 class="chart-title">{html.escape(sample_chart_title(domain, chart, data))}</h2>
        <div class="chart-meta">{html.escape(sample_chart_meta(domain, chart, data))}</div>
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


def profile_for(domain: dict) -> dict:
    if domain["slug"] in DOMAIN_PROFILES:
        return DOMAIN_PROFILES[domain["slug"]]
    metric, unit, categories, segments = PROFILE_FALLBACKS[domain["slug"]]
    return {
        "metric": metric,
        "unit": unit,
        "periods": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"],
        "categories": categories,
        "segments": segments,
        "stages": segments[:5],
        "drivers": ["Baseline", "Gain", "Cost", "Delay", "Recovery", "Net"],
        "assumptions": categories[:6],
        "scenarios": ["Base", "Upside", "Delay", "Shock", "Stress"],
        "radar": categories[:6],
        "x_axis": categories[0],
        "y_axis": metric,
        "flows": categories[:3] + segments[:3],
    }


def rotate(items: list[str], seed: int) -> list[str]:
    if not items:
        return items
    pivot = seed % len(items)
    return items[pivot:] + items[:pivot]


def series_values(seed: int, count: int, low: int = 32, high: int = 88) -> list[int]:
    span = high - low
    values = []
    current = low + seed % max(1, span)
    for i in range(count):
        drift = ((seed // (i + 3)) + i * 11) % 17 - 6
        current = max(low, min(high, current + drift))
        values.append(current)
    return values


def sample_data(domain: dict, chart: dict) -> dict:
    seed = sum(ord(ch) for ch in f"{domain['slug']}:{chart['slug']}")
    profile = profile_for(domain)
    categories = rotate(profile["categories"], seed)
    segments = rotate(profile["segments"], seed // 3)
    stages = rotate(profile["stages"], seed // 5)
    data = {
        "seed": seed,
        "metric": profile["metric"],
        "unit": profile["unit"],
        "periods": rotate(profile["periods"], seed // 7),
        "categories": categories,
        "segments": segments,
        "stages": stages,
        "drivers": rotate(profile["drivers"], seed // 11),
        "assumptions": rotate(profile["assumptions"], seed // 13),
        "scenarios": rotate(profile["scenarios"], seed // 17),
        "radar": rotate(profile["radar"], seed // 19),
        "flows": rotate(profile["flows"], seed // 23),
        "x_axis": profile["x_axis"],
        "y_axis": profile["y_axis"],
        "series": series_values(seed, 12),
    }
    if chart["slug"] == "yield-curve":
        data["metric"] = "Treasury yield"
        data["unit"] = "yield percent"
        data["periods"] = ["1M", "3M", "1Y", "2Y", "5Y", "10Y", "30Y", "Long"]
        data["x_axis"] = "Maturity"
        data["y_axis"] = "Yield"
    if "vitals" in chart["slug"]:
        data["metric"] = "Patient vitals score"
        data["unit"] = "clinical index"
    return data


def sample_chart_title(domain: dict, chart: dict, data: dict) -> str:
    title = chart["title"].lower()
    if chart["type"] == "line":
        return f"{domain['name']} {chart['title']} for {data['metric'].lower()}"
    if chart["type"] == "area":
        return f"{domain['name']} cumulative {data['metric'].lower()}"
    if chart["type"] == "funnel":
        return f"{domain['name']} {data['stages'][0].lower()} to {data['stages'][-1].lower()}"
    if chart["type"] == "sankey":
        return f"{domain['name']} flow between {data['flows'][0].lower()} and {data['flows'][-1].lower()}"
    if chart["type"] == "kpi":
        return f"{domain['name']} operating KPI snapshot"
    if chart["type"] == "stress":
        return f"{domain['name']} scenario stress test"
    return f"{domain['name']} {title} example"


def sample_chart_meta(domain: dict, chart: dict, data: dict) -> str:
    return f"illustrative {data['unit']} / {domain['slug']} sample data"


def render_visual(domain: dict, chart: dict, data: dict) -> str:
    chart_type = chart["type"]
    random.seed(data["seed"])
    if chart_type == "line":
        return svg_line(data, area=False)
    if chart_type == "area":
        return svg_line(data, area=True)
    if chart_type == "drawdown":
        return svg_drawdown(data)
    if chart_type == "grouped-bar":
        return svg_grouped_bar(data)
    if chart_type == "stacked-bar":
        return svg_stacked_bar(data)
    if chart_type == "horizontal-bar":
        return svg_horizontal_bar(data)
    if chart_type == "donut":
        return svg_donut(data)
    if chart_type == "scatter":
        return svg_scatter(data, bubbles=False)
    if chart_type == "bubble":
        return svg_scatter(data, bubbles=True)
    if chart_type == "heatmap":
        return svg_heatmap(data)
    if chart_type == "matrix":
        return svg_matrix(data)
    if chart_type == "calendar":
        return svg_calendar(data)
    if chart_type == "treemap":
        return svg_treemap(data)
    if chart_type == "candlestick":
        return svg_candlestick(data)
    if chart_type == "depth":
        return svg_depth(data)
    if chart_type == "frontier":
        return svg_frontier(data)
    if chart_type == "fan":
        return svg_fan(data)
    if chart_type == "funnel":
        return svg_funnel(data)
    if chart_type == "sankey":
        return svg_sankey(data)
    if chart_type == "waterfall":
        return svg_waterfall(data)
    if chart_type == "tornado":
        return svg_tornado(data)
    if chart_type == "radar":
        return svg_radar(data)
    if chart_type == "table":
        return html_table(data)
    if chart_type == "cohort":
        return html_cohort(data)
    if chart_type == "kpi":
        return html_kpi(data)
    if chart_type == "stress":
        return svg_stress(data)
    return svg_line(data, area=False)


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


def svg_line(data: dict, area: bool) -> str:
    values = data["series"]
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
    period_labels = (data["periods"] * 2)[:6]
    labels = "".join(
        f'<text class="label" x="{82 + i * 164}" y="384">{html.escape(label)}</text>'
        for i, label in enumerate(period_labels)
    )
    inner = f"""{grid()}
  {area_path}
  <polyline points="{polyline(points)}" fill="none" stroke="{PALETTE['teal']}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="{points[-1][0]:.1f}" cy="{points[-1][1]:.1f}" r="6" fill="{PALETTE['clay']}"/>
  <text class="label" x="42" y="62">High</text>
  <text class="label" x="42" y="354">{html.escape(data['metric'])}</text>
  {labels}"""
    return svg_shell(inner)


def svg_drawdown(data: dict) -> str:
    base = data["seed"] % 5
    values = [0, -3 - base, -8, -5 - base, -12, -22 + base, -18, -11, -7 - base, -4, -9, -2]
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
  <text class="label" x="36" y="60">0</text>
  <text class="label" x="30" y="354">{html.escape(data['metric'])}</text>"""
    return svg_shell(inner)


def svg_grouped_bar(data: dict) -> str:
    labels = (data["periods"] * 2)[:4]
    base = data["seed"] % 12
    series = [[46 + base + i * 7, 52 + base + i * 6, 57 + base + i * 5, 63 + base + i * 4] for i in range(3)]
    colors = [PALETTE["teal"], PALETTE["clay"], PALETTE["olive"]]
    bars = []
    x0, y0, width, height = 110, 54, 740, 300
    for i, label in enumerate(labels):
        base_x = x0 + i * 180
        bars.append(f'<text class="label" x="{base_x + 32}" y="386">{html.escape(label)}</text>')
        for j, values in enumerate(series):
            h = values[i] / 90 * height
            x = base_x + j * 34
            y = y0 + height - h
            bars.append(f'<rect x="{x}" y="{y:.1f}" width="26" height="{h:.1f}" rx="4" fill="{colors[j]}"/>')
    for j, label in enumerate(data["categories"][:3]):
        bars.append(f'<rect x="{612 + j * 92}" y="30" width="14" height="14" rx="3" fill="{colors[j]}"/><text class="label" x="{632 + j * 92}" y="42">{html.escape(label[:10])}</text>')
    inner = f"{grid(width=760, x=82)}\n  " + "\n  ".join(bars)
    return svg_shell(inner)


def svg_stacked_bar(data: dict) -> str:
    stacks = [[18 + (data["seed"] + i * 3 + j * 5) % 18 for j in range(3)] for i in range(4)]
    colors = [PALETTE["teal"], PALETTE["gold"], PALETTE["clay"]]
    bars = []
    for i, stack in enumerate(stacks):
        x = 150 + i * 170
        y = 354
        for j, value in enumerate(stack):
            h = value * 3.2
            y -= h
            bars.append(f'<rect x="{x}" y="{y:.1f}" width="86" height="{h:.1f}" fill="{colors[j]}"/>')
        bars.append(f'<text class="label" x="{x + 8}" y="386">{html.escape((data["periods"] * 2)[i][:10])}</text>')
    for j, label in enumerate(data["segments"][:3]):
        bars.append(f'<rect x="{620 + j * 88}" y="30" width="14" height="14" rx="3" fill="{colors[j]}"/><text class="label" x="{640 + j * 88}" y="42">{html.escape(label[:9])}</text>')
    inner = f"{grid(width=760, x=82)}\n  " + "\n  ".join(bars)
    return svg_shell(inner)


def svg_horizontal_bar(data: dict) -> str:
    labels = data["categories"][:6]
    raw = series_values(data["seed"], 6, 18, 78)
    values = [raw[i] if i % 3 != 0 else -raw[i] // 2 for i in range(6)]
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


def svg_donut(data: dict) -> str:
    raw = series_values(data["seed"], 5, 10, 38)
    total = sum(raw)
    values = [round(v / total * 100) for v in raw]
    values[-1] += 100 - sum(values)
    slices = list(zip(values, [PALETTE["teal"], PALETTE["clay"], PALETTE["olive"], PALETTE["gold"], PALETTE["blue"]]))
    cx, cy, r = 300, 210, 132
    start = -90
    paths = []
    labels = []
    names = data["segments"][:5]
    for i, (value, color) in enumerate(slices):
        end = start + value / 100 * 360
        paths.append(donut_slice(cx, cy, r, 66, start, end, color))
        labels.append(f'<rect x="560" y="{116 + i * 42}" width="16" height="16" rx="3" fill="{color}"/><text class="small" x="588" y="{129 + i * 42}">{html.escape(names[i])} {value}%</text>')
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


def svg_scatter(data: dict, bubbles: bool) -> str:
    points = [((data["seed"] + i * 9) % 70 + 10, (data["seed"] // 3 + i * 7) % 28 + 5, (data["seed"] // 5 + i * 11) % 28 + 10) for i in range(8)]
    dots = []
    for x, y, size in points:
        cx = 92 + x / 80 * 800
        cy = 354 - y / 34 * 288
        r = size / 3 if bubbles else 6
        dots.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{PALETTE["teal"]}" opacity="0.78"/>')
    inner = f"""{grid()}
  {" ".join(dots)}
  <text class="label" x="410" y="406">{html.escape(data['x_axis'])}</text>
  <text class="label" x="24" y="210" transform="rotate(-90 24 210)">{html.escape(data['y_axis'])}</text>"""
    return svg_shell(inner)


def svg_heatmap(data: dict) -> str:
    rows = data["categories"][:5]
    cols = (data["periods"] * 2)[:6]
    cells = []
    for r, row in enumerate(rows):
        cells.append(f'<text class="small" x="58" y="{96 + r * 48}">{html.escape(row[:12])}</text>')
        for c, _ in enumerate(cols):
            val = (data["seed"] + r * 13 + c * 17) % 9
            colors = [PALETTE["rust"], "#CF6B52", PALETTE["oat"], "#9BAE78", PALETTE["olive"]]
            color = colors[min(4, max(0, val // 2))]
            cells.append(f'<rect x="{150 + c * 112}" y="{70 + r * 48}" width="88" height="34" rx="5" fill="{color}"/>')
    for c, col in enumerate(cols):
        cells.append(f'<text class="label" x="{176 + c * 112}" y="48">{html.escape(col[:8])}</text>')
    return svg_shell("\n  ".join(cells), height=380)


def svg_matrix(data: dict) -> str:
    labels = [label[:7] for label in data["categories"][:6]]
    cells = []
    for r, row in enumerate(labels):
        cells.append(f'<text class="label" x="90" y="{91 + r * 44}">{row}</text>')
        cells.append(f'<text class="label" x="{158 + r * 72}" y="48">{row}</text>')
        for c, _ in enumerate(labels):
            distance = abs(r - c)
            color = [PALETTE["teal"], "#88B0A6", PALETTE["oat"], "#D99B7C", PALETTE["rust"]][min((distance + data["seed"]) % 5, 4)]
            cells.append(f'<rect x="{146 + c * 72}" y="{66 + r * 44}" width="52" height="32" rx="4" fill="{color}"/>')
    return svg_shell("\n  ".join(cells), height=380)


def svg_calendar(data: dict) -> str:
    cells = []
    for week in range(13):
        for day in range(5):
            val = (data["seed"] + week * 7 + day * 5) % 6
            color = [PALETTE["gray100"], PALETTE["oat"], "#BFCB9D", PALETTE["olive"], PALETTE["teal"], PALETTE["clay"]][val]
            cells.append(f'<rect x="{94 + week * 58}" y="{82 + day * 48}" width="36" height="32" rx="5" fill="{color}"/>')
    months = "".join(f'<text class="label" x="{96 + i * 174}" y="52">{html.escape(m[:8])}</text>' for i, m in enumerate((data["periods"] * 2)[:5]))
    return svg_shell(months + "\n  " + "\n  ".join(cells), height=380)


def svg_treemap(data: dict) -> str:
    labels = data["categories"][:6]
    rects = [
        (60, 60, 310, 230, PALETTE["teal"], labels[0]),
        (382, 60, 210, 138, PALETTE["olive"], labels[1]),
        (604, 60, 256, 138, PALETTE["clay"], labels[2]),
        (382, 212, 154, 120, PALETTE["gold"], labels[3]),
        (548, 212, 144, 120, PALETTE["blue"], labels[4]),
        (704, 212, 156, 120, PALETTE["oat"], labels[5]),
    ]
    parts = []
    for x, y, w, h, color, label in rects:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{color}"/><text x="{x + 16}" y="{y + 30}" font-family="var(--sans)" font-size="15" fill="{PALETTE["slate"]}">{html.escape(label[:18])}</text>')
    return svg_shell("\n  ".join(parts), height=390)


def svg_candlestick(data: dict) -> str:
    candles = []
    for i in range(14):
        x = 104 + i * 56
        high = 78 + (data["seed"] + i * 19) % 94
        low = high + 118 + (i * 11) % 54
        open_y = high + 42 + (i * 13) % 48
        close_y = high + 44 + ((i + 3) * 17) % 58
        color = PALETTE["teal"] if close_y < open_y else PALETTE["rust"]
        body_y = min(open_y, close_y)
        body_h = max(18, abs(close_y - open_y))
        candles.append(f'<line x1="{x}" y1="{high}" x2="{x}" y2="{low}" stroke="{color}" stroke-width="3"/><rect x="{x - 12}" y="{body_y}" width="24" height="{body_h}" rx="3" fill="{color}"/>')
    return svg_shell(f"{grid()}\n  " + "\n  ".join(candles))


def svg_depth(data: dict) -> str:
    bids = [(82, 310), (190, 284), (302, 246), (416, 190), (480, 132)]
    asks = [(480, 132), (548, 184), (662, 224), (790, 270), (902, 310)]
    inner = f"""{grid()}
  <polygon points="82,354 {polyline(bids)} 480,354" fill="{PALETTE['teal']}" opacity="0.28"/>
  <polyline points="{polyline(bids)}" fill="none" stroke="{PALETTE['teal']}" stroke-width="4"/>
  <polygon points="480,354 {polyline(asks)} 902,354" fill="{PALETTE['rust']}" opacity="0.24"/>
  <polyline points="{polyline(asks)}" fill="none" stroke="{PALETTE['rust']}" stroke-width="4"/>
  <line x1="480" y1="72" x2="480" y2="354" stroke="{PALETTE['slate']}" stroke-dasharray="5 6"/>
  <text class="label" x="430" y="386">{html.escape(data['metric'])}</text>"""
    return svg_shell(inner)


def svg_frontier(data: dict) -> str:
    frontier = [(120, 320), (210, 260), (330, 205), (480, 166), (650, 138), (820, 128)]
    dots = []
    for i in range(20):
        x = 124 + (data["seed"] + i * 41) % 690
        y = 324 - ((data["seed"] // 3 + i * 37) % 190)
        dots.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{PALETTE["gray500"]}" opacity="0.55"/>')
    inner = f"""{grid()}
  {" ".join(dots)}
  <polyline points="{polyline(frontier)}" fill="none" stroke="{PALETTE['clay']}" stroke-width="4"/>
  <circle cx="480" cy="166" r="8" fill="{PALETTE['teal']}"/>
  <text class="label" x="410" y="406">{html.escape(data['x_axis'])}</text>
  <text class="label" x="24" y="214" transform="rotate(-90 24 214)">{html.escape(data['y_axis'])}</text>"""
    return svg_shell(inner)


def svg_fan(data: dict) -> str:
    x0, y0, width, height = 82, 54, 820, 300
    xs = [x0 + i * width / 7 for i in range(8)]
    bump = data["seed"] % 8
    low = [(x, y0 + height - (36 + bump + i * 2) / 96 * height) for i, x in enumerate(xs)]
    mid = [(x, y0 + height - (50 + bump + i * 6) / 96 * height) for i, x in enumerate(xs)]
    high = [(x, y0 + height - (66 + bump + i * 9) / 96 * height) for i, x in enumerate(xs)]
    band = low + list(reversed(high))
    inner = f"""{grid()}
  <polygon points="{polyline(band)}" fill="{PALETTE['oat']}" opacity="0.85"/>
  <polyline points="{polyline(mid)}" fill="none" stroke="{PALETTE['teal']}" stroke-width="4"/>
  <text class="label" x="740" y="104">P90</text>
  <text class="label" x="740" y="308">P10</text>"""
    return svg_shell(inner)


def svg_funnel(data: dict) -> str:
    start = 740 - data["seed"] % 80
    widths = [start, int(start * .82), int(start * .62), int(start * .42), int(start * .25)]
    labels = data["stages"][:5]
    parts = []
    for i, w in enumerate(widths):
        x = 480 - w / 2
        y = 58 + i * 58
        color = [PALETTE["teal"], PALETTE["olive"], PALETTE["gold"], PALETTE["clay"], PALETTE["rust"]][i]
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="42" rx="6" fill="{color}"/><text x="480" y="{y + 27}" text-anchor="middle" font-family="var(--sans)" font-size="15" fill="{PALETTE["slate"]}">{html.escape(labels[i])}</text>')
    return svg_shell("\n  ".join(parts), height=390)


def svg_sankey(data: dict) -> str:
    nodes = (data["flows"] * 2)[:6]
    flows = [
        (nodes[0], 80, 112, nodes[2], 430, 166, PALETTE["teal"]),
        (nodes[1], 80, 246, nodes[2], 430, 166, PALETTE["olive"]),
        (nodes[2], 530, 166, nodes[3], 780, 92, PALETTE["clay"]),
        (nodes[2], 530, 166, nodes[4], 780, 196, PALETTE["gold"]),
        (nodes[2], 530, 166, nodes[5], 780, 296, PALETTE["blue"]),
    ]
    parts = []
    for _, x1, y1, _, x2, y2, color in flows:
        parts.append(f'<path d="M{x1 + 110},{y1} C{x1 + 220},{y1} {x2 - 120},{y2} {x2},{y2}" fill="none" stroke="{color}" stroke-width="28" opacity="0.55"/>')
    node_boxes = [(nodes[0], 80, 82), (nodes[1], 80, 216), (nodes[2], 420, 136), (nodes[3], 780, 62), (nodes[4], 780, 166), (nodes[5], 780, 266)]
    for label, x, y in node_boxes:
        parts.append(f'<rect x="{x}" y="{y}" width="126" height="60" rx="8" fill="{PALETTE["paper"]}" stroke="{PALETTE["gray300"]}" stroke-width="1.5"/><text class="small" x="{x + 14}" y="{y + 36}">{html.escape(label[:12])}</text>')
    return svg_shell("\n  ".join(parts), height=390)


def svg_waterfall(data: dict) -> str:
    vals = [150 + data["seed"] % 50, -32 - data["seed"] % 22, -20 - data["seed"] % 18, 24 + data["seed"] % 26, -14 - data["seed"] % 12, 112 + data["seed"] % 42]
    labels = data["drivers"][:6]
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
        parts.append(f'<rect x="{x}" y="{y:.1f}" width="76" height="{h:.1f}" rx="5" fill="{color}"/><text class="label" x="{x}" y="374">{html.escape(labels[i][:10])}</text>')
        running += value if i != len(vals) - 1 else 0
    return svg_shell(f"{grid(width=790)}\n  " + "\n  ".join(parts))


def svg_tornado(data: dict) -> str:
    labels = data["assumptions"][:6]
    parts = []
    for i, label in enumerate(labels):
        y = 70 + i * 45
        left = 120 - i * 12
        right = 160 - i * 10
        parts.append(f'<text class="small" x="98" y="{y + 18}">{html.escape(label[:16])}</text><rect x="{480 - left}" y="{y}" width="{left}" height="26" rx="5" fill="{PALETTE["rust"]}"/><rect x="480" y="{y}" width="{right}" height="26" rx="5" fill="{PALETTE["teal"]}"/>')
    return svg_shell(f'<line class="axis" x1="480" y1="50" x2="480" y2="350"/>\n  {" ".join(parts)}')


def svg_radar(data: dict) -> str:
    cx, cy = 480, 210
    axes = data["radar"][:6]
    rings = []
    for r in [55, 100, 145]:
        pts = [polar(cx, cy, r, -90 + i * 60) for i in range(6)]
        rings.append(f'<polygon points="{polyline(pts)}" fill="none" stroke="{PALETTE["gray300"]}" stroke-width="1.5"/>')
    scores = [72 + (data["seed"] + i * 17) % 74 for i in range(6)]
    pts = [polar(cx, cy, scores[i], -90 + i * 60) for i in range(6)]
    labels = []
    for i, label in enumerate(axes):
        lx, ly = polar(cx, cy, 174, -90 + i * 60)
        labels.append(f'<text class="label" x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle">{html.escape(label[:12])}</text>')
    inner = "\n  ".join(rings + [f'<polygon points="{polyline(pts)}" fill="{PALETTE["teal"]}" opacity="0.35" stroke="{PALETTE["teal"]}" stroke-width="4"/>'] + labels)
    return svg_shell(inner, height=430)


def html_table(data: dict) -> str:
    rows = [
        (label, f"{series_values(data['seed'] + i, 1, 8, 44)[0]}.0%", data["unit"], data["scenarios"][i % len(data["scenarios"])])
        for i, label in enumerate(data["segments"][:5])
    ]
    body = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows
    )
    return f"""<div style="overflow:auto">
  <table style="width:100%; border-collapse:separate; border-spacing:0; border:1.5px solid {PALETTE['gray300']}; border-radius:8px; overflow:hidden">
    <thead><tr style="background:{PALETTE['gray100']}"><th>Segment</th><th>Share</th><th>Unit</th><th>Scenario</th></tr></thead>
    <tbody>{body}</tbody>
  </table>
</div>
<style>
  th, td {{ text-align:left; padding:14px 16px; border-bottom:1px solid {PALETTE['gray100']}; white-space:nowrap; }}
  th {{ font:600 12px var(--mono); color:{PALETTE['gray500']}; text-transform:uppercase; letter-spacing:.06em; }}
  td {{ font-size:14px; color:{PALETTE['gray700']}; }}
</style>"""


def html_cohort(data: dict) -> str:
    rows = []
    cohorts = (data["periods"] * 2)[:6]
    for r, cohort in enumerate(cohorts):
        cells = [f"<th>{cohort}</th>"]
        for c in range(6):
            if c < r:
                cells.append("<td></td>")
            else:
                value = max(38, 96 - (c - r) * 9 - r * 3 - data["seed"] % 7)
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


def html_kpi(data: dict) -> str:
    vals = series_values(data["seed"], 4, 12, 86)
    labels = data["categories"][:4]
    cards = [
        (labels[0], f"{vals[0]}", data["unit"]),
        (labels[1], f"{vals[1]}%", "conversion"),
        (labels[2], f"{vals[2]}", "throughput"),
        (labels[3], f"{vals[3]}%", "quality"),
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


def svg_stress(data: dict) -> str:
    bars = series_values(data["seed"], 5, 46, 178)
    labels = data["scenarios"][:5]
    parts = []
    for i, value in enumerate(bars):
        x = 140 + i * 140
        y = 342 - value
        color = [PALETTE["teal"], PALETTE["olive"], PALETTE["gold"], PALETTE["clay"], PALETTE["rust"]][i]
        parts.append(f'<rect x="{x}" y="{y}" width="86" height="{value}" rx="5" fill="{color}"/><text class="label" x="{x}" y="374">{html.escape(labels[i][:10])}</text>')
    return svg_shell(f"{grid(width=780)}\n  " + "\n  ".join(parts))


if __name__ == "__main__":
    main()
