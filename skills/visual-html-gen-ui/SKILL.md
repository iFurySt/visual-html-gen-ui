---
name: visual-html-gen-ui
description: Use when an agent needs standalone HTML chart examples for a specific domain, especially to design data-rich UI artifacts without loading a large chart library into context.
---

# Visual HTML Gen UI

Use this skill when you need a standalone HTML chart example for a
specific product domain. Start here, choose the relevant domain and
chart, then open only that chart's `index.html` file.

The examples are self-contained HTML documents using inline CSS and
SVG. They are intended as visual references that agents can adapt into
product screens, reports, dashboards, and generated artifacts.

## How To Use

1. Pick the domain that matches the user's problem.
2. Open the linked chart file, not the whole skill directory.
3. Reuse the chart structure, labels, spacing, and interaction pattern
   as a starting point.
4. Replace sample data, copy, and colors with project-specific values.

## Domain Catalog

### Finance

Capital markets, investment research, portfolio analytics, risk, and private-market operating metrics.

- [Line Chart](finance/line-chart/index.html) - Show price, NAV, revenue, or macro trend changes over time.
- [Area Chart](finance/area-chart/index.html) - Emphasize accumulated scale such as AUM, deposits, or net inflows.
- [Grouped Bar Chart](finance/grouped-bar-chart/index.html) - Compare multiple companies, quarters, or scenarios side by side.
- [Stacked Bar Chart](finance/stacked-bar-chart/index.html) - Break revenue, holdings, or portfolio exposure into components.
- [Donut Allocation](finance/donut-allocation/index.html) - Summarize asset allocation, sector weight, or capital deployment.
- [Risk Return Scatter](finance/risk-return-scatter/index.html) - Position strategies or assets by volatility and return.
- [Valuation Bubble](finance/valuation-bubble/index.html) - Compare valuation, growth, and market capitalization in one view.
- [Sector Rotation Heatmap](finance/sector-rotation-heatmap/index.html) - Track sector strength, factor rotation, or weekly flows.
- [Market Map Treemap](finance/market-map-treemap/index.html) - Show market capitalization or portfolio weight by company and sector.
- [Candlestick Chart](finance/candlestick-chart/index.html) - Display OHLC market action for trader-facing views.
- [Depth Chart](finance/depth-chart/index.html) - Visualize bid and ask liquidity around the current price.
- [Drawdown Chart](finance/drawdown-chart/index.html) - Expose peak-to-trough losses for a fund or strategy.
- [Equity Curve](finance/equity-curve/index.html) - Show cumulative strategy or fund growth over time.
- [Rolling Sharpe](finance/rolling-sharpe/index.html) - Track risk-adjusted return quality through time.
- [Efficient Frontier](finance/efficient-frontier/index.html) - Compare portfolio choices by expected return and volatility.
- [Monte Carlo Fan](finance/monte-carlo-fan/index.html) - Present a range of possible future portfolio paths.
- [Deal Funnel](finance/deal-funnel/index.html) - Summarize VC or lending pipeline conversion by stage.
- [Capital Flow Sankey](finance/capital-flow-sankey/index.html) - Show how capital moves between sources, vehicles, and uses.
- [Correlation Matrix](finance/correlation-matrix/index.html) - Expose relationships between assets, factors, or sectors.
- [Factor Exposure](finance/factor-exposure/index.html) - Show portfolio sensitivity to value, momentum, quality, and size.
- [Risk Attribution](finance/risk-attribution/index.html) - Break total risk into sector, factor, security, and currency drivers.
- [Waterfall Profit Bridge](finance/waterfall-profit-bridge/index.html) - Explain movement from revenue to net income or EBITDA.
- [Tornado Sensitivity](finance/tornado-sensitivity/index.html) - Rank model assumptions by effect on valuation or IRR.
- [Company Score Radar](finance/company-score-radar/index.html) - Score a company or fund across multiple qualitative dimensions.
- [Calendar Heatmap](finance/calendar-heatmap/index.html) - Show daily returns, trading activity, or cash movement intensity.
- [Yield Curve](finance/yield-curve/index.html) - Display rates across maturities for macro and fixed-income analysis.
- [Cap Table](finance/cap-table/index.html) - Present ownership, share classes, and dilution after financing.
- [Cohort Retention](finance/cohort-retention/index.html) - Analyze customer or portfolio cohort quality over time.
- [Unit Economics](finance/unit-economics/index.html) - Compare CAC, LTV, payback, gross margin, and burn efficiency.
- [VaR Stress Test](finance/var-stress-test/index.html) - Show expected loss bands under normal and stressed scenarios.

### Office

Workplace productivity, meetings, task execution, communication, approvals, and team operations.

- [Meeting Load Timeline](office/meeting-load-timeline/index.html) - Show how meeting hours change by week or team.
- [Task Status Stacked Bar](office/task-status-stacked-bar/index.html) - Break planned work into done, in progress, blocked, and deferred states.
- [Calendar Heatmap](office/calendar-heatmap/index.html) - Reveal high-pressure days for meetings, deadlines, or handoffs.
- [Email Response Funnel](office/email-response-funnel/index.html) - Track message conversion from sent to opened, replied, and resolved.
- [Document Flow Sankey](office/document-flow-sankey/index.html) - Visualize how documents move between draft, review, approval, and archive.
- [Team Capacity Bars](office/team-capacity-bars/index.html) - Compare available capacity against committed workload by team.
- [Approval Waterfall](office/approval-waterfall/index.html) - Explain cycle-time additions from review, legal, finance, and executive approval.
- [Workspace Utilization Heatmap](office/workspace-utilization-heatmap/index.html) - Show desk, room, or location utilization patterns.
- [Knowledge Base Treemap](office/knowledge-base-treemap/index.html) - Map documentation coverage by department or topic area.
- [Workload Risk Radar](office/workload-risk-radar/index.html) - Score teams across urgency, ambiguity, dependency, load, and morale risk.

### Education

Learning progress, classroom operations, curriculum quality, assessment, and student support analytics.

- [Learning Progress Line](education/learning-progress-line/index.html) - Show mastery or completion growth across a semester.
- [Grade Distribution Bars](education/grade-distribution-bars/index.html) - Compare score bands across classes, sections, or terms.
- [Mastery Heatmap](education/mastery-heatmap/index.html) - Map skill mastery by module and learner group.
- [Attendance Calendar](education/attendance-calendar/index.html) - Reveal daily attendance, absence, or participation intensity.
- [Cohort Retention](education/cohort-retention/index.html) - Track student retention or course completion by intake cohort.
- [Curriculum Coverage Treemap](education/curriculum-coverage-treemap/index.html) - Show instructional time or content weight by curriculum area.
- [Intervention Funnel](education/intervention-funnel/index.html) - Track students from flagged risk to outreach, support, and recovery.
- [Learning Path Sankey](education/learning-path-sankey/index.html) - Show how learners move across tracks, modules, and outcomes.
- [Rubric Score Radar](education/rubric-score-radar/index.html) - Summarize student or class performance across rubric dimensions.
- [Assessment Stress Test](education/assessment-stress-test/index.html) - Compare performance under standard, timed, and advanced assessment conditions.

### Health

Patient monitoring, care operations, population health, appointment flow, and clinical quality views.

- [Vitals Trend Line](health/vitals-trend-line/index.html) - Track a patient metric such as glucose, heart rate, or blood pressure over time.
- [Symptom Severity Area](health/symptom-severity-area/index.html) - Emphasize cumulative symptom burden or recovery progress.
- [Patient Flow Funnel](health/patient-flow-funnel/index.html) - Summarize intake, triage, consult, treatment, and discharge conversion.
- [Appointment Calendar](health/appointment-calendar/index.html) - Show appointment density, no-shows, or follow-up adherence by day.
- [Ward Utilization Heatmap](health/ward-utilization-heatmap/index.html) - Reveal bed, room, or clinician utilization by time block.
- [Care Pathway Sankey](health/care-pathway-sankey/index.html) - Visualize patient movement across referral, diagnosis, treatment, and follow-up.
- [Population Risk Scatter](health/population-risk-scatter/index.html) - Position patient groups by risk score and cost or complexity.
- [Treatment Response Cohort](health/treatment-response-cohort/index.html) - Track response or adherence cohorts over follow-up periods.
- [Clinical Quality Radar](health/clinical-quality-radar/index.html) - Score a program across safety, access, experience, efficacy, and cost.
- [Readmission Stress Test](health/readmission-stress-test/index.html) - Compare expected readmission or complication losses under stress scenarios.

### Ecommerce

Online retail conversion, merchandising, inventory, customer value, promotions, and fulfillment analytics.

- [Revenue Line](ecommerce/revenue-line/index.html) - Show gross merchandise value or revenue trend over time.
- [Checkout Funnel](ecommerce/checkout-funnel/index.html) - Track shoppers through product view, cart, checkout, payment, and purchase.
- [Category Sales Stacked Bar](ecommerce/category-sales-stacked-bar/index.html) - Break sales into category, channel, or region components.
- [Product Margin Waterfall](ecommerce/product-margin-waterfall/index.html) - Explain margin from list price through discounts, shipping, returns, and fees.
- [Inventory Heatmap](ecommerce/inventory-heatmap/index.html) - Reveal stock risk by SKU and warehouse or region.
- [Customer Cohort Retention](ecommerce/customer-cohort-retention/index.html) - Track repeat purchase retention by acquisition cohort.
- [LTV CAC KPI](ecommerce/ltv-cac-kpi/index.html) - Compare acquisition efficiency, LTV, payback, and contribution margin.
- [Basket Affinity Sankey](ecommerce/basket-affinity-sankey/index.html) - Show product pairings and category paths in baskets.
- [SKU Performance Treemap](ecommerce/sku-performance-treemap/index.html) - Map SKU revenue or contribution by product family.
- [Promo Sensitivity Tornado](ecommerce/promo-sensitivity-tornado/index.html) - Rank price, discount, shipping, and ad spend assumptions by profit effect.

### Social

Community growth, engagement, creator networks, moderation, content propagation, and retention.

- [Active Users Line](social/active-users-line/index.html) - Track DAU, WAU, or MAU growth across a period.
- [Engagement Area](social/engagement-area/index.html) - Emphasize accumulated sessions, reactions, comments, or shares.
- [Activation Funnel](social/activation-funnel/index.html) - Track users from signup to profile completion, first follow, first post, and return.
- [Creator Network Sankey](social/creator-network-sankey/index.html) - Show audience movement between creators, topics, and communities.
- [Topic Heatmap](social/topic-heatmap/index.html) - Reveal topic momentum by day or community segment.
- [Community Treemap](social/community-treemap/index.html) - Map communities by active users, posts, or moderation load.
- [User Cohort Retention](social/user-cohort-retention/index.html) - Track retained users by signup cohort and age.
- [Influence Bubble](social/influence-bubble/index.html) - Compare creators by reach, engagement rate, and audience size.
- [Moderation Waterfall](social/moderation-waterfall/index.html) - Explain report queue changes from inflow, automation, review, appeals, and backlog.
- [Community Health Radar](social/community-health-radar/index.html) - Score safety, activity, diversity, creator supply, and retention.

### Entertainment

Streaming, music, film, live events, audience behavior, releases, and catalog performance.

- [Viewership Line](entertainment/viewership-line/index.html) - Track streams, tickets, or watch time around release windows.
- [Catalog Share Donut](entertainment/catalog-share-donut/index.html) - Summarize watch time or revenue by genre, studio, or catalog segment.
- [Box Office Stacked Bar](entertainment/box-office-stacked-bar/index.html) - Break revenue by market, format, or week.
- [Audience Retention Cohort](entertainment/audience-retention-cohort/index.html) - Track return viewing or subscriber retention by content cohort.
- [Release Calendar Heatmap](entertainment/release-calendar-heatmap/index.html) - Show release density, campaigns, or audience activity by day.
- [Genre Momentum Heatmap](entertainment/genre-momentum-heatmap/index.html) - Reveal genre demand shifts across weeks or platforms.
- [Playlist Flow Sankey](entertainment/playlist-flow-sankey/index.html) - Show listener or viewer movement between playlists, shows, and channels.
- [Talent Score Radar](entertainment/talent-score-radar/index.html) - Score an artist or title across reach, loyalty, monetization, and brand fit.
- [Campaign Funnel](entertainment/campaign-funnel/index.html) - Track awareness, trailer views, follows, intent, and purchase.
- [Title Portfolio Treemap](entertainment/title-portfolio-treemap/index.html) - Map catalog performance by title, franchise, or genre.

### Gaming

Game telemetry, player progression, economy balance, monetization, matchmaking, and live ops.

- [DAU Line](gaming/dau-line/index.html) - Track active players through seasons, patches, and events.
- [Level Progression Funnel](gaming/level-progression-funnel/index.html) - Show players advancing through tutorial, early levels, and core loop.
- [Economy Sankey](gaming/economy-sankey/index.html) - Visualize currency sources, sinks, and player inventory flow.
- [Session Calendar](gaming/session-calendar/index.html) - Reveal play session intensity by day.
- [Mode Popularity Stacked Bar](gaming/mode-popularity-stacked-bar/index.html) - Break playtime by game mode or playlist.
- [Matchmaking Heatmap](gaming/matchmaking-heatmap/index.html) - Show queue time or match quality by skill band and region.
- [Player Retention Cohort](gaming/player-retention-cohort/index.html) - Track retention by install cohort and lifecycle day.
- [Item Sales Treemap](gaming/item-sales-treemap/index.html) - Map item, skin, or bundle revenue contribution.
- [Balance Tornado](gaming/balance-tornado/index.html) - Rank tuning variables by effect on win rate or progression speed.
- [Player Segment Radar](gaming/player-segment-radar/index.html) - Compare player segments across skill, spend, social, completion, and risk.

### Content Creation

Creator workflow, publishing cadence, audience growth, monetization, editorial planning, and performance.

- [Publishing Cadence Line](content-creation/publishing-cadence-line/index.html) - Track posts, videos, newsletters, or assets shipped over time.
- [Content Pipeline Funnel](content-creation/content-pipeline-funnel/index.html) - Track ideas through draft, edit, review, scheduled, and published.
- [Channel Mix Donut](content-creation/channel-mix-donut/index.html) - Summarize output or revenue by channel.
- [Audience Growth Area](content-creation/audience-growth-area/index.html) - Emphasize accumulated followers, subscribers, or reach.
- [Editorial Calendar Heatmap](content-creation/editorial-calendar-heatmap/index.html) - Show publishing load and gaps by day.
- [Content Performance Treemap](content-creation/content-performance-treemap/index.html) - Map views, revenue, or engagement by content piece or series.
- [Creator Retention Cohort](content-creation/creator-retention-cohort/index.html) - Track repeat viewers, subscribers, or paid supporters by cohort.
- [Platform Flow Sankey](content-creation/platform-flow-sankey/index.html) - Show audience movement across discovery, follow, email, community, and purchase.
- [Monetization KPI](content-creation/monetization-kpi/index.html) - Compare RPM, conversion, paid support, payback, and revenue per fan.
- [Format Score Radar](content-creation/format-score-radar/index.html) - Score formats across reach, depth, effort, reuse, and monetization.

### Enterprise Services

B2B sales, delivery, support, customer success, implementation, and account health analytics.

- [ARR Line](enterprise-services/arr-line/index.html) - Track recurring revenue or contracted backlog over time.
- [Sales Pipeline Funnel](enterprise-services/sales-pipeline-funnel/index.html) - Summarize leads, qualified opportunities, proposals, negotiation, and closed won.
- [Implementation Sankey](enterprise-services/implementation-sankey/index.html) - Show customer movement across kickoff, setup, integration, training, and go-live.
- [Ticket Heatmap](enterprise-services/ticket-heatmap/index.html) - Reveal support load by severity and product area.
- [Account Health Radar](enterprise-services/account-health-radar/index.html) - Score customers across adoption, support, expansion, sentiment, and renewal risk.
- [Service Margin Waterfall](enterprise-services/service-margin-waterfall/index.html) - Explain gross margin from contract value through labor, travel, support, and overrun.
- [Customer Retention Cohort](enterprise-services/customer-retention-cohort/index.html) - Track logo or revenue retention by contract cohort.
- [SLA Calendar](enterprise-services/sla-calendar/index.html) - Show SLA breaches or incident pressure by day.
- [Portfolio Treemap](enterprise-services/portfolio-treemap/index.html) - Map revenue or effort by account, segment, or service line.
- [Sales Efficiency KPI](enterprise-services/sales-efficiency-kpi/index.html) - Compare CAC, payback, expansion, win rate, and burn efficiency.

### Cybersecurity

Threat detection, incidents, vulnerability management, risk posture, response operations, and control health.

- [Incident Line](cybersecurity/incident-line/index.html) - Track incidents, alerts, or suspicious activity through time.
- [Severity Stacked Bar](cybersecurity/severity-stacked-bar/index.html) - Break findings into critical, high, medium, and low severity.
- [Attack Path Sankey](cybersecurity/attack-path-sankey/index.html) - Show attacker movement from entry vector to lateral movement and objective.
- [Vulnerability Heatmap](cybersecurity/vulnerability-heatmap/index.html) - Map vulnerability count or risk by asset class and severity.
- [Response Funnel](cybersecurity/response-funnel/index.html) - Track alerts from triggered to triaged, investigated, contained, and resolved.
- [Asset Risk Treemap](cybersecurity/asset-risk-treemap/index.html) - Map risk contribution by application, host, or business unit.
- [Control Maturity Radar](cybersecurity/control-maturity-radar/index.html) - Score identity, endpoint, network, detection, backup, and training controls.
- [Phishing Calendar](cybersecurity/phishing-calendar/index.html) - Reveal phishing activity or training completion by day.
- [Risk Reduction Waterfall](cybersecurity/risk-reduction-waterfall/index.html) - Explain risk movement from new findings, patches, compensating controls, and exceptions.
- [Breach Stress Test](cybersecurity/breach-stress-test/index.html) - Compare estimated losses under baseline, ransomware, data leak, and outage scenarios.

### AI Agent

Agent workflows, model performance, tool use, evaluation, cost, latency, safety, and autonomy analytics.

- [Task Success Line](ai-agent/task-success-line/index.html) - Track agent task success rate across eval runs or product releases.
- [Latency Area](ai-agent/latency-area/index.html) - Emphasize cumulative latency or runtime cost across workflow stages.
- [Tool Use Sankey](ai-agent/tool-use-sankey/index.html) - Show agent movement between planning, search, code, browser, and verification tools.
- [Eval Heatmap](ai-agent/eval-heatmap/index.html) - Map pass rate by task family and capability dimension.
- [Failure Funnel](ai-agent/failure-funnel/index.html) - Track failures from detected issue to repro, root cause, fix, and verified pass.
- [Model Cost Scatter](ai-agent/model-cost-scatter/index.html) - Position models or prompts by quality and cost.
- [Agent Cohort Retention](ai-agent/agent-cohort-retention/index.html) - Track repeat workflow success by task cohort over versions.
- [Capability Radar](ai-agent/capability-radar/index.html) - Score an agent across planning, tool use, coding, browsing, safety, and memory.
- [Token Waterfall](ai-agent/token-waterfall/index.html) - Explain token use from system context, retrieved docs, reasoning, tool output, and answer.
- [Safety Stress Test](ai-agent/safety-stress-test/index.html) - Compare failure rates under normal, adversarial, long-context, and tool-error scenarios.

### Real Estate

Property valuation, leasing, occupancy, market supply, rent, cap rates, and asset operations.

- [Price Index Line](real-estate/price-index-line/index.html) - Track property price, rent index, or cap-rate movement over time.
- [Occupancy Area](real-estate/occupancy-area/index.html) - Emphasize leased area or occupancy scale through time.
- [Lease Funnel](real-estate/lease-funnel/index.html) - Track prospects through inquiry, tour, offer, lease, and move-in.
- [Portfolio Treemap](real-estate/portfolio-treemap/index.html) - Map NOI, value, or square footage by asset and submarket.
- [Market Heatmap](real-estate/market-heatmap/index.html) - Show rent growth, vacancy, or absorption by market and property type.
- [Development Waterfall](real-estate/development-waterfall/index.html) - Explain project return from land, construction, financing, lease-up, and exit.
- [Tenant Cohort Retention](real-estate/tenant-cohort-retention/index.html) - Track tenant renewal and retention by lease-start cohort.
- [Valuation Sensitivity Tornado](real-estate/valuation-sensitivity-tornado/index.html) - Rank cap rate, rent growth, vacancy, and financing assumptions by value impact.
- [Asset Score Radar](real-estate/asset-score-radar/index.html) - Score a property by location, income, condition, tenant quality, and risk.
- [Cashflow Stress Test](real-estate/cashflow-stress-test/index.html) - Compare cashflow under vacancy, rate shock, construction delay, and recession scenarios.

### HR

Workforce planning, recruiting, performance, retention, engagement, compensation, and people operations.

- [Headcount Line](hr/headcount-line/index.html) - Track headcount, openings, or hiring plan over time.
- [Recruiting Funnel](hr/recruiting-funnel/index.html) - Track candidates from sourced to screen, onsite, offer, and accepted.
- [Department Mix Stacked Bar](hr/department-mix-stacked-bar/index.html) - Break workforce by function, location, level, or employment type.
- [Attrition Calendar](hr/attrition-calendar/index.html) - Reveal resignation or absence patterns by day or month.
- [Engagement Heatmap](hr/engagement-heatmap/index.html) - Map engagement or survey scores by team and dimension.
- [Compensation Scatter](hr/compensation-scatter/index.html) - Position employees or roles by compensation and performance band.
- [Promotion Cohort](hr/promotion-cohort/index.html) - Track career progression and promotion rates by starting cohort.
- [Org Treemap](hr/org-treemap/index.html) - Map headcount or payroll by organization unit.
- [Performance Radar](hr/performance-radar/index.html) - Score a role or team across impact, collaboration, craft, ownership, and growth.
- [Workforce Risk Stress Test](hr/workforce-risk-stress-test/index.html) - Compare staffing gaps under attrition, hiring freeze, demand spike, and reorg scenarios.

### Mobility

Urban mobility, ride hailing, fleet operations, routing, utilization, safety, and multimodal transport.

- [Trip Volume Line](mobility/trip-volume-line/index.html) - Track rides, deliveries, or passenger trips over time.
- [Fleet Utilization Area](mobility/fleet-utilization-area/index.html) - Emphasize active vehicles, idle capacity, or utilization scale.
- [Dispatch Funnel](mobility/dispatch-funnel/index.html) - Track requests through matched, accepted, arrived, completed, and rated.
- [Route Heatmap](mobility/route-heatmap/index.html) - Reveal demand or congestion by zone and time block.
- [Mode Share Donut](mobility/mode-share-donut/index.html) - Summarize trips by car, bike, transit, walking, or scooter.
- [Station Treemap](mobility/station-treemap/index.html) - Map usage by station, depot, or zone.
- [Driver Cohort Retention](mobility/driver-cohort-retention/index.html) - Track driver or rider retention by activation cohort.
- [Fare Waterfall](mobility/fare-waterfall/index.html) - Explain fare from base, distance, surge, incentives, fees, and margin.
- [Safety Radar](mobility/safety-radar/index.html) - Score operations across incidents, compliance, training, vehicle health, and response.
- [Demand Stress Test](mobility/demand-stress-test/index.html) - Compare service capacity under weather, event, outage, and demand spike scenarios.

## Maintenance

Maintainers should edit `catalog.json`, run
`python3 scripts/build_charts.py`, then run
`python3 scripts/validate_skill.py` before committing.
