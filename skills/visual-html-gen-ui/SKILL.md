---
name: visual-html-gen-ui
description: Use when an agent needs standalone HTML chart examples for a specific domain, especially to design data-rich UI artifacts without loading a large chart library into context.
---

# Visual HTML Gen UI

Use this skill when you need a standalone HTML chart example for a
specific product domain. Start here, choose the relevant domain and
chart, then open only that chart's HTML file.

The examples are self-contained HTML documents using inline CSS and
SVG. They are intended as visual references that agents can adapt into
product screens, reports, dashboards, and deliverables.

## How To Use

1. Pick the domain that matches the user's problem.
2. Open the linked chart file, not the whole skill directory.
3. Reuse the chart structure, labels, spacing, and interaction pattern
   as a starting point.
4. Replace sample data, copy, and colors with project-specific values.

## Domain Catalog

### Finance

Capital markets, investment research, portfolio analytics, risk, and private-market operating metrics.

- [Line Chart](finance/line-chart.html) - Show price, NAV, revenue, or macro trend changes over time.
- [Area Chart](finance/area-chart.html) - Emphasize accumulated scale such as AUM, deposits, or net inflows.
- [Grouped Bar Chart](finance/grouped-bar-chart.html) - Compare multiple companies, quarters, or scenarios side by side.
- [Stacked Bar Chart](finance/stacked-bar-chart.html) - Break revenue, holdings, or portfolio exposure into components.
- [Donut Allocation](finance/donut-allocation.html) - Summarize asset allocation, sector weight, or capital deployment.
- [Risk Return Scatter](finance/risk-return-scatter.html) - Position strategies or assets by volatility and return.
- [Valuation Bubble](finance/valuation-bubble.html) - Compare valuation, growth, and market capitalization in one view.
- [Sector Rotation Heatmap](finance/sector-rotation-heatmap.html) - Track sector strength, factor rotation, or weekly flows.
- [Market Map Treemap](finance/market-map-treemap.html) - Show market capitalization or portfolio weight by company and sector.
- [Candlestick Chart](finance/candlestick-chart.html) - Display OHLC market action for trader-facing views.
- [Depth Chart](finance/depth-chart.html) - Visualize bid and ask liquidity around the current price.
- [Drawdown Chart](finance/drawdown-chart.html) - Expose peak-to-trough losses for a fund or strategy.
- [Equity Curve](finance/equity-curve.html) - Show cumulative strategy or fund growth over time.
- [Rolling Sharpe](finance/rolling-sharpe.html) - Track risk-adjusted return quality through time.
- [Efficient Frontier](finance/efficient-frontier.html) - Compare portfolio choices by expected return and volatility.
- [Monte Carlo Fan](finance/monte-carlo-fan.html) - Present a range of possible future portfolio paths.
- [Deal Funnel](finance/deal-funnel.html) - Summarize VC or lending pipeline conversion by stage.
- [Capital Flow Sankey](finance/capital-flow-sankey.html) - Show how capital moves between sources, vehicles, and uses.
- [Correlation Matrix](finance/correlation-matrix.html) - Expose relationships between assets, factors, or sectors.
- [Factor Exposure](finance/factor-exposure.html) - Show portfolio sensitivity to value, momentum, quality, and size.
- [Risk Attribution](finance/risk-attribution.html) - Break total risk into sector, factor, security, and currency drivers.
- [Waterfall Profit Bridge](finance/waterfall-profit-bridge.html) - Explain movement from revenue to net income or EBITDA.
- [Tornado Sensitivity](finance/tornado-sensitivity.html) - Rank model assumptions by effect on valuation or IRR.
- [Company Score Radar](finance/company-score-radar.html) - Score a company or fund across multiple qualitative dimensions.
- [Trading Calendar Heatmap](finance/calendar-heatmap.html) - Show daily returns, trading activity, or cash movement intensity.
- [Yield Curve](finance/yield-curve.html) - Display rates across maturities for macro and fixed-income analysis.
- [Cap Table](finance/cap-table.html) - Present ownership, share classes, and dilution after financing.
- [Capital Cohort Retention](finance/cohort-retention.html) - Analyze customer or portfolio cohort quality over time.
- [Unit Economics](finance/unit-economics.html) - Compare CAC, LTV, payback, gross margin, and burn efficiency.
- [VaR Stress Test](finance/var-stress-test.html) - Show expected loss bands under normal and stressed scenarios.

### Office

Workplace productivity, meetings, task execution, communication, approvals, and team operations.

- [Meeting Load Timeline](office/meeting-load-timeline.html) - Track recurring and ad hoc meeting load against protected focus time.
- [Task Status Stacked Bar](office/task-status-stacked-bar.html) - Break internal operating queues into done, active, blocked, and waiting states.
- [Workspace Calendar Heatmap](office/calendar-heatmap.html) - Reveal high-pressure days where reviews, deadlines, and handoffs collide.
- [Email Response Funnel](office/email-response-funnel.html) - Track high-priority announcements from sent to resolved follow-up.
- [Document Flow Sankey](office/document-flow-sankey.html) - Visualize policy or operating documents moving through owner, review, approval, and rework paths.
- [Team Capacity Bars](office/team-capacity-bars.html) - Compare available hours, committed work, and interruptions by team.
- [Approval Waterfall](office/approval-waterfall.html) - Explain business days added by manager, legal, finance, and executive gates.
- [Workspace Utilization Heatmap](office/workspace-utilization-heatmap.html) - Show room, desk, and focus-space usage by daypart.
- [Knowledge Base Treemap](office/knowledge-base-treemap.html) - Map documentation coverage, stale-doc risk, and ownership gaps by operating area.
- [Workload Risk Radar](office/workload-risk-radar.html) - Score operating risk across urgency, ambiguity, dependencies, load, focus, and morale.

### Education

Learning progress, classroom operations, curriculum quality, assessment, and student support analytics.

- [Learning Progress Line](education/learning-progress-line.html) - Track standards mastery growth across a semester and expose plateaus before finals.
- [Grade Distribution Bars](education/grade-distribution-bars.html) - Compare proficiency bands across class sections after a shared assessment.
- [Mastery Heatmap](education/mastery-heatmap.html) - Map concept mastery by learner group so teachers can plan reteach blocks.
- [Attendance Calendar](education/attendance-calendar.html) - Reveal absence, tardy, and participation pressure across a school month.
- [Learner Cohort Retention](education/cohort-retention.html) - Track course completion and continued participation by enrollment cohort.
- [Curriculum Coverage Treemap](education/curriculum-coverage-treemap.html) - Show instructional time and assessment weight by standards cluster.
- [Intervention Funnel](education/intervention-funnel.html) - Track students from risk flag to family outreach, tutoring, practice, and recovery.
- [Learning Path Sankey](education/learning-path-sankey.html) - Show learners moving from diagnostic placement through modules, retakes, and outcomes.
- [Rubric Score Radar](education/rubric-score-radar.html) - Summarize writing or project performance across rubric dimensions.
- [Assessment Stress Test](education/assessment-stress-test.html) - Compare expected performance under timed, supported, remote, and advanced assessment conditions.

### Health

Patient monitoring, care operations, population health, appointment flow, and clinical quality views.

- [Vitals Trend Line](health/vitals-trend-line.html) - Track remote blood pressure readings against escalation thresholds between visits.
- [Symptom Severity Area](health/symptom-severity-area.html) - Show symptom burden after discharge before readmission risk rises.
- [Patient Flow Funnel](health/patient-flow-funnel.html) - Summarize emergency department flow from arrival to discharge decision.
- [Appointment Calendar](health/appointment-calendar.html) - Show clinic appointment load, no-show clusters, and follow-up gaps by day.
- [Ward Utilization Heatmap](health/ward-utilization-heatmap.html) - Reveal inpatient bed and nurse coverage pressure by ward and shift block.
- [Care Pathway Sankey](health/care-pathway-sankey.html) - Visualize referral, diagnosis, treatment, follow-up, recovery, and escalation paths.
- [Population Risk Scatter](health/population-risk-scatter.html) - Position patient cohorts by clinical risk, cost, and care-management priority.
- [Treatment Response Cohort](health/treatment-response-cohort.html) - Track treatment response and adherence by start-month cohort.
- [Clinical Quality Radar](health/clinical-quality-radar.html) - Score clinical quality across safety, access, experience, outcomes, equity, and cost.
- [Readmission Stress Test](health/readmission-stress-test.html) - Compare readmission risk under staffing, follow-up, and surge scenarios.

### Ecommerce

Online retail conversion, merchandising, inventory, customer value, promotions, and fulfillment analytics.

- [Revenue Line](ecommerce/revenue-line.html) - Track daily GMV and promotion lift across a campaign window.
- [Checkout Funnel](ecommerce/checkout-funnel.html) - Track shoppers from product view through cart, checkout, payment, and purchase.
- [Category Sales Stacked Bar](ecommerce/category-sales-stacked-bar.html) - Break category sales by online, marketplace, and store-assisted channels.
- [Product Margin Waterfall](ecommerce/product-margin-waterfall.html) - Explain product contribution margin after discounts, fulfillment, returns, and fees.
- [Inventory Heatmap](ecommerce/inventory-heatmap.html) - Reveal stockout and overstock risk by SKU family and fulfillment region.
- [Shopper Cohort Retention](ecommerce/customer-cohort-retention.html) - Track repeat purchase retention by acquisition cohort and first-order channel.
- [LTV CAC KPI](ecommerce/ltv-cac-kpi.html) - Compare LTV, CAC, payback, contribution margin, and repeat rate.
- [Basket Affinity Sankey](ecommerce/basket-affinity-sankey.html) - Show basket paths from anchor products into bundles, add-ons, and repeat purchases.
- [SKU Performance Treemap](ecommerce/sku-performance-treemap.html) - Map SKU contribution, hero products, and long-tail drag by product family.
- [Promo Sensitivity Tornado](ecommerce/promo-sensitivity-tornado.html) - Rank discount, free shipping, return rate, and ad-spend assumptions by profit effect.

### Social

Community growth, engagement, creator networks, moderation, content propagation, and retention.

- [Active Users Line](social/active-users-line.html) - Track DAU, WAU, or MAU growth across a period.
- [Engagement Area](social/engagement-area.html) - Emphasize accumulated sessions, reactions, comments, or shares.
- [Activation Funnel](social/activation-funnel.html) - Track users from signup to profile completion, first follow, first post, and return.
- [Creator Network Sankey](social/creator-network-sankey.html) - Show audience movement between creators, topics, and communities.
- [Topic Heatmap](social/topic-heatmap.html) - Reveal topic momentum by day or community segment.
- [Community Treemap](social/community-treemap.html) - Map communities by active users, posts, or moderation load.
- [User Cohort Retention](social/user-cohort-retention.html) - Track retained users by signup cohort and age.
- [Influence Bubble](social/influence-bubble.html) - Compare creators by reach, engagement rate, and audience size.
- [Moderation Waterfall](social/moderation-waterfall.html) - Explain report queue changes from inflow, automation, review, appeals, and backlog.
- [Community Health Radar](social/community-health-radar.html) - Score safety, activity, diversity, creator supply, and retention.

### Entertainment

Streaming, music, film, live events, audience behavior, releases, and catalog performance.

- [Viewership Line](entertainment/viewership-line.html) - Track streams, tickets, or watch time around release windows.
- [Catalog Share Donut](entertainment/catalog-share-donut.html) - Summarize watch time or revenue by genre, studio, or catalog segment.
- [Box Office Stacked Bar](entertainment/box-office-stacked-bar.html) - Break revenue by market, format, or week.
- [Audience Retention Cohort](entertainment/audience-retention-cohort.html) - Track return viewing or subscriber retention by content cohort.
- [Release Calendar Heatmap](entertainment/release-calendar-heatmap.html) - Show release density, campaigns, or audience activity by day.
- [Genre Momentum Heatmap](entertainment/genre-momentum-heatmap.html) - Reveal genre demand shifts across weeks or platforms.
- [Playlist Flow Sankey](entertainment/playlist-flow-sankey.html) - Show listener or viewer movement between playlists, shows, and channels.
- [Talent Score Radar](entertainment/talent-score-radar.html) - Score an artist or title across reach, loyalty, monetization, and brand fit.
- [Campaign Funnel](entertainment/campaign-funnel.html) - Track awareness, trailer views, follows, intent, and purchase.
- [Title Portfolio Treemap](entertainment/title-portfolio-treemap.html) - Map catalog performance by title, franchise, or genre.

### Gaming

Game telemetry, player progression, economy balance, monetization, matchmaking, and live ops.

- [DAU Line](gaming/dau-line.html) - Track active players through seasons, patches, and events.
- [Level Progression Funnel](gaming/level-progression-funnel.html) - Show players advancing through tutorial, early levels, and core loop.
- [Economy Sankey](gaming/economy-sankey.html) - Visualize currency sources, sinks, and player inventory flow.
- [Session Calendar](gaming/session-calendar.html) - Reveal play session intensity by day.
- [Mode Popularity Stacked Bar](gaming/mode-popularity-stacked-bar.html) - Break playtime by game mode or playlist.
- [Matchmaking Heatmap](gaming/matchmaking-heatmap.html) - Show queue time or match quality by skill band and region.
- [Player Retention Cohort](gaming/player-retention-cohort.html) - Track retention by install cohort and lifecycle day.
- [Item Sales Treemap](gaming/item-sales-treemap.html) - Map item, skin, or bundle revenue contribution.
- [Balance Tornado](gaming/balance-tornado.html) - Rank tuning variables by effect on win rate or progression speed.
- [Player Segment Radar](gaming/player-segment-radar.html) - Compare player segments across skill, spend, social, completion, and risk.

### Content Creation

Creator workflow, publishing cadence, audience growth, monetization, editorial planning, and performance.

- [Publishing Cadence Line](content-creation/publishing-cadence-line.html) - Track posts, videos, newsletters, or assets shipped over time.
- [Content Pipeline Funnel](content-creation/content-pipeline-funnel.html) - Track ideas through draft, edit, review, scheduled, and published.
- [Channel Mix Donut](content-creation/channel-mix-donut.html) - Summarize output or revenue by channel.
- [Audience Growth Area](content-creation/audience-growth-area.html) - Emphasize accumulated followers, subscribers, or reach.
- [Editorial Calendar Heatmap](content-creation/editorial-calendar-heatmap.html) - Show publishing load and gaps by day.
- [Content Performance Treemap](content-creation/content-performance-treemap.html) - Map views, revenue, or engagement by content piece or series.
- [Creator Retention Cohort](content-creation/creator-retention-cohort.html) - Track repeat viewers, subscribers, or paid supporters by cohort.
- [Platform Flow Sankey](content-creation/platform-flow-sankey.html) - Show audience movement across discovery, follow, email, community, and purchase.
- [Monetization KPI](content-creation/monetization-kpi.html) - Compare RPM, conversion, paid support, payback, and revenue per fan.
- [Format Score Radar](content-creation/format-score-radar.html) - Score formats across reach, depth, effort, reuse, and monetization.

### Enterprise Services

B2B sales, delivery, support, customer success, implementation, and account health analytics.

- [ARR Line](enterprise-services/arr-line.html) - Track recurring revenue or contracted backlog over time.
- [Sales Pipeline Funnel](enterprise-services/sales-pipeline-funnel.html) - Summarize leads, qualified opportunities, proposals, negotiation, and closed won.
- [Implementation Sankey](enterprise-services/implementation-sankey.html) - Show customer movement across kickoff, setup, integration, training, and go-live.
- [Ticket Heatmap](enterprise-services/ticket-heatmap.html) - Reveal support load by severity and product area.
- [Account Health Radar](enterprise-services/account-health-radar.html) - Score customers across adoption, support, expansion, sentiment, and renewal risk.
- [Service Margin Waterfall](enterprise-services/service-margin-waterfall.html) - Explain gross margin from contract value through labor, travel, support, and overrun.
- [Customer Retention Cohort](enterprise-services/customer-retention-cohort.html) - Track logo or revenue retention by contract cohort.
- [SLA Calendar](enterprise-services/sla-calendar.html) - Show SLA breaches or incident pressure by day.
- [Account Portfolio Treemap](enterprise-services/portfolio-treemap.html) - Map revenue or effort by account, segment, or service line.
- [Sales Efficiency KPI](enterprise-services/sales-efficiency-kpi.html) - Compare CAC, payback, expansion, win rate, and burn efficiency.

### Cybersecurity

Threat detection, incidents, vulnerability management, risk posture, response operations, and control health.

- [Incident Line](cybersecurity/incident-line.html) - Track incidents, alerts, or suspicious activity through time.
- [Severity Stacked Bar](cybersecurity/severity-stacked-bar.html) - Break findings into critical, high, medium, and low severity.
- [Attack Path Sankey](cybersecurity/attack-path-sankey.html) - Show attacker movement from entry vector to lateral movement and objective.
- [Vulnerability Heatmap](cybersecurity/vulnerability-heatmap.html) - Map vulnerability count or risk by asset class and severity.
- [Response Funnel](cybersecurity/response-funnel.html) - Track alerts from triggered to triaged, investigated, contained, and resolved.
- [Asset Risk Treemap](cybersecurity/asset-risk-treemap.html) - Map risk contribution by application, host, or business unit.
- [Control Maturity Radar](cybersecurity/control-maturity-radar.html) - Score identity, endpoint, network, detection, backup, and training controls.
- [Phishing Calendar](cybersecurity/phishing-calendar.html) - Reveal phishing activity or training completion by day.
- [Risk Reduction Waterfall](cybersecurity/risk-reduction-waterfall.html) - Explain risk movement from new findings, patches, compensating controls, and exceptions.
- [Breach Stress Test](cybersecurity/breach-stress-test.html) - Compare estimated losses under baseline, ransomware, data leak, and outage scenarios.

### AI Agent

Agent workflows, model performance, tool use, evaluation, cost, latency, safety, and autonomy analytics.

- [Task Success Line](ai-agent/task-success-line.html) - Track agent task success rate across eval runs or product releases.
- [Latency Area](ai-agent/latency-area.html) - Emphasize cumulative latency or runtime cost across workflow stages.
- [Tool Use Sankey](ai-agent/tool-use-sankey.html) - Show agent movement between planning, search, code, browser, and verification tools.
- [Eval Heatmap](ai-agent/eval-heatmap.html) - Map pass rate by task family and capability dimension.
- [Failure Funnel](ai-agent/failure-funnel.html) - Track failures from detected issue to repro, root cause, fix, and verified pass.
- [Model Cost Scatter](ai-agent/model-cost-scatter.html) - Position models or prompts by quality and cost.
- [Agent Cohort Retention](ai-agent/agent-cohort-retention.html) - Track repeat workflow success by task cohort over versions.
- [Capability Radar](ai-agent/capability-radar.html) - Score an agent across planning, tool use, coding, browsing, safety, and memory.
- [Token Waterfall](ai-agent/token-waterfall.html) - Explain token use from system context, retrieved docs, reasoning, tool output, and answer.
- [Safety Stress Test](ai-agent/safety-stress-test.html) - Compare failure rates under normal, adversarial, long-context, and tool-error scenarios.

### Real Estate

Property valuation, leasing, occupancy, market supply, rent, cap rates, and asset operations.

- [Price Index Line](real-estate/price-index-line.html) - Track property price, rent index, or cap-rate movement over time.
- [Occupancy Area](real-estate/occupancy-area.html) - Emphasize leased area or occupancy scale through time.
- [Lease Funnel](real-estate/lease-funnel.html) - Track prospects through inquiry, tour, offer, lease, and move-in.
- [Asset Portfolio Treemap](real-estate/portfolio-treemap.html) - Map NOI, value, or square footage by asset and submarket.
- [Market Heatmap](real-estate/market-heatmap.html) - Show rent growth, vacancy, or absorption by market and property type.
- [Development Waterfall](real-estate/development-waterfall.html) - Explain project return from land, construction, financing, lease-up, and exit.
- [Tenant Cohort Retention](real-estate/tenant-cohort-retention.html) - Track tenant renewal and retention by lease-start cohort.
- [Valuation Sensitivity Tornado](real-estate/valuation-sensitivity-tornado.html) - Rank cap rate, rent growth, vacancy, and financing assumptions by value impact.
- [Asset Score Radar](real-estate/asset-score-radar.html) - Score a property by location, income, condition, tenant quality, and risk.
- [Cashflow Stress Test](real-estate/cashflow-stress-test.html) - Compare cashflow under vacancy, rate shock, construction delay, and recession scenarios.

### HR

Workforce planning, recruiting, performance, retention, engagement, compensation, and people operations.

- [Headcount Line](hr/headcount-line.html) - Track headcount, openings, or hiring plan over time.
- [Recruiting Funnel](hr/recruiting-funnel.html) - Track candidates from sourced to screen, onsite, offer, and accepted.
- [Department Mix Stacked Bar](hr/department-mix-stacked-bar.html) - Break workforce by function, location, level, or employment type.
- [Attrition Calendar](hr/attrition-calendar.html) - Reveal resignation or absence patterns by day or month.
- [Engagement Heatmap](hr/engagement-heatmap.html) - Map engagement or survey scores by team and dimension.
- [Compensation Scatter](hr/compensation-scatter.html) - Position employees or roles by compensation and performance band.
- [Promotion Cohort](hr/promotion-cohort.html) - Track career progression and promotion rates by starting cohort.
- [Org Treemap](hr/org-treemap.html) - Map headcount or payroll by organization unit.
- [Performance Radar](hr/performance-radar.html) - Score a role or team across impact, collaboration, craft, ownership, and growth.
- [Workforce Risk Stress Test](hr/workforce-risk-stress-test.html) - Compare staffing gaps under attrition, hiring freeze, demand spike, and reorg scenarios.

### Mobility

Urban mobility, ride hailing, fleet operations, routing, utilization, safety, and multimodal transport.

- [Trip Volume Line](mobility/trip-volume-line.html) - Track rides, deliveries, or passenger trips over time.
- [Fleet Utilization Area](mobility/fleet-utilization-area.html) - Emphasize active vehicles, idle capacity, or utilization scale.
- [Dispatch Funnel](mobility/dispatch-funnel.html) - Track requests through matched, accepted, arrived, completed, and rated.
- [Mobility Route Heatmap](mobility/route-heatmap.html) - Reveal demand or congestion by zone and time block.
- [Mode Share Donut](mobility/mode-share-donut.html) - Summarize trips by car, bike, transit, walking, or scooter.
- [Station Treemap](mobility/station-treemap.html) - Map usage by station, depot, or zone.
- [Driver Cohort Retention](mobility/driver-cohort-retention.html) - Track driver or rider retention by activation cohort.
- [Fare Waterfall](mobility/fare-waterfall.html) - Explain fare from base, distance, surge, incentives, fees, and margin.
- [Safety Radar](mobility/safety-radar.html) - Score operations across incidents, compliance, training, vehicle health, and response.
- [Demand Stress Test](mobility/demand-stress-test.html) - Compare service capacity under weather, event, outage, and demand spike scenarios.

### Travel

Trips, bookings, destinations, itinerary planning, hospitality, demand forecasting, and traveler experience.

- [Booking Line](travel/booking-line.html) - Track bookings, room nights, or ticket volume over time.
- [Destination Share Donut](travel/destination-share-donut.html) - Summarize trips by destination, region, or travel type.
- [Booking Funnel](travel/booking-funnel.html) - Track search, quote, checkout, payment, confirmation, and check-in.
- [Itinerary Sankey](travel/itinerary-sankey.html) - Show traveler movement across origin, destination, lodging, activity, and return.
- [Seasonality Calendar](travel/seasonality-calendar.html) - Reveal booking or travel intensity by day.
- [Travel Route Heatmap](travel/route-heatmap.html) - Map demand, occupancy, or price by route and month.
- [Hotel Portfolio Treemap](travel/hotel-portfolio-treemap.html) - Map revenue or nights by hotel, destination, or brand.
- [Traveler Retention Cohort](travel/traveler-retention-cohort.html) - Track repeat bookings by acquisition cohort.
- [Trip Margin Waterfall](travel/trip-margin-waterfall.html) - Explain margin from gross booking through discounts, fees, supplier cost, and support.
- [Experience Radar](travel/experience-radar.html) - Score travel experience across price, convenience, support, quality, and flexibility.

### Biotech

Drug discovery, clinical trials, lab operations, biomarkers, pipelines, safety, and R&D portfolio views.

- [Biomarker Line](biotech/biomarker-line.html) - Track biomarker or assay response over study time.
- [Trial Enrollment Funnel](biotech/trial-enrollment-funnel.html) - Track screened, eligible, consented, randomized, and completed subjects.
- [Pipeline Sankey](biotech/pipeline-sankey.html) - Show candidate movement through discovery, preclinical, phase, and approval stages.
- [Assay Heatmap](biotech/assay-heatmap.html) - Map assay response by compound and target.
- [Program Portfolio Treemap](biotech/portfolio-treemap.html) - Map program value, risk, or spend by therapeutic area.
- [Dose Response Scatter](biotech/dose-response-scatter.html) - Position cohorts by dose and response or adverse event rate.
- [Patient Cohort Retention](biotech/patient-cohort-retention.html) - Track follow-up, adherence, or endpoint capture by cohort.
- [R and D Waterfall](biotech/r-and-d-waterfall.html) - Explain R&D cash movement from funding, spend, milestones, grants, and runway.
- [Program Risk Radar](biotech/program-risk-radar.html) - Score a program across efficacy, safety, CMC, regulatory, IP, and market fit.
- [Clinical Stress Test](biotech/clinical-stress-test.html) - Compare timeline or cash need under enrollment delay, safety signal, and regulatory scenarios.

### Legal

Matter management, contracts, litigation, compliance, risk, billing, and legal operations dashboards.

- [Matter Volume Line](legal/matter-volume-line.html) - Track opened, closed, or active matters over time.
- [Contract Review Funnel](legal/contract-review-funnel.html) - Track contracts from intake to redline, negotiation, approval, and signature.
- [Case Stage Sankey](legal/case-stage-sankey.html) - Show matters moving through investigation, filing, discovery, settlement, and close.
- [Risk Heatmap](legal/risk-heatmap.html) - Map legal risk by business unit and issue type.
- [Billing Waterfall](legal/billing-waterfall.html) - Explain spend from budget through outside counsel, discounts, accruals, and variance.
- [Clause Treemap](legal/clause-treemap.html) - Map contract clause frequency or negotiation effort by clause type.
- [Compliance Calendar](legal/compliance-calendar.html) - Show filings, deadlines, audits, and policy updates by date.
- [Matter Cohort](legal/matter-cohort.html) - Track matter resolution or aging by intake cohort.
- [Case Merit Radar](legal/case-merit-radar.html) - Score matters across evidence, damages, precedent, cost, timing, and risk.
- [Litigation Stress Test](legal/litigation-stress-test.html) - Compare exposure under settlement, trial, appeal, and adverse judgment scenarios.

### Government

Public services, budgets, case queues, civic operations, policy outcomes, and infrastructure programs.

- [Service Demand Line](government/service-demand-line.html) - Track public service requests, permits, or cases over time.
- [Budget Allocation Donut](government/budget-allocation-donut.html) - Summarize budget by agency, program, or funding source.
- [Permit Funnel](government/permit-funnel.html) - Track applications through submitted, reviewed, corrected, approved, and issued.
- [Case Flow Sankey](government/case-flow-sankey.html) - Show case movement across intake, eligibility, review, service, and close.
- [District Heatmap](government/district-heatmap.html) - Map service need or outcome metrics by district and topic.
- [Program Treemap](government/program-treemap.html) - Map spend or outcomes by program area.
- [Deadline Calendar](government/deadline-calendar.html) - Show public hearings, filing deadlines, grant windows, and reporting dates.
- [Outcome Cohort](government/outcome-cohort.html) - Track participant outcomes by intake cohort.
- [Policy Score Radar](government/policy-score-radar.html) - Score policy options across cost, reach, equity, feasibility, and risk.
- [Budget Stress Test](government/budget-stress-test.html) - Compare budget gap under inflation, revenue decline, demand spike, and disaster scenarios.

### Manufacturing

Production, quality, supply chain, maintenance, throughput, yield, and factory operations analytics.

- [Production Line](manufacturing/production-line.html) - Track output, yield, or throughput over shifts and weeks.
- [Quality Stacked Bar](manufacturing/quality-stacked-bar.html) - Break production into pass, rework, scrap, and hold states.
- [Defect Heatmap](manufacturing/defect-heatmap.html) - Map defect rate by station and defect type.
- [Supply Flow Sankey](manufacturing/supply-flow-sankey.html) - Show material flow from suppliers to lines, inventory, and shipment.
- [OEE KPI](manufacturing/oee-kpi.html) - Compare availability, performance, quality, cycle time, and scrap efficiency.
- [Line Utilization Calendar](manufacturing/line-utilization-calendar.html) - Reveal shift utilization or downtime by day.
- [Product Mix Treemap](manufacturing/product-mix-treemap.html) - Map output, revenue, or margin by product family.
- [Maintenance Funnel](manufacturing/maintenance-funnel.html) - Track work orders from created to triaged, scheduled, completed, and verified.
- [Cost Waterfall](manufacturing/cost-waterfall.html) - Explain cost movement from materials, labor, energy, rework, and logistics.
- [Factory Risk Radar](manufacturing/factory-risk-radar.html) - Score a plant across safety, quality, capacity, maintenance, supply, and cost.

### Energy

Generation, demand, grid operations, trading, storage, renewables, emissions, and asset performance.

- [Load Line](energy/load-line.html) - Track power demand, generation, or price over time.
- [Generation Stack Area](energy/generation-stack-area.html) - Emphasize generation mix or supply stack over time.
- [Fuel Mix Donut](energy/fuel-mix-donut.html) - Summarize generation or consumption by energy source.
- [Grid Heatmap](energy/grid-heatmap.html) - Map load, congestion, or outage risk by region and hour.
- [Dispatch Sankey](energy/dispatch-sankey.html) - Show energy flow from generation sources to grid, storage, and load.
- [Asset Treemap](energy/asset-treemap.html) - Map capacity, revenue, or emissions by asset.
- [Price Risk Scatter](energy/price-risk-scatter.html) - Position markets or assets by price volatility and margin.
- [Emissions Waterfall](energy/emissions-waterfall.html) - Explain emissions movement from demand, efficiency, renewables, offsets, and fuel mix.
- [Project Sensitivity Tornado](energy/project-sensitivity-tornado.html) - Rank price, capex, capacity factor, and financing assumptions by project return effect.
- [Supply Stress Test](energy/supply-stress-test.html) - Compare reserve margin under outage, heat wave, fuel shock, and demand spike scenarios.

### Retail

Store operations, category management, merchandising, footfall, inventory, promotions, and basket analytics.

- [Same Store Sales Line](retail/same-store-sales-line.html) - Track same-store sales, footfall, or conversion over time.
- [Category Mix Stacked Bar](retail/category-mix-stacked-bar.html) - Break store sales into category or department components.
- [Store Traffic Calendar](retail/store-traffic-calendar.html) - Reveal footfall or transaction pressure by day.
- [Shelf Availability Heatmap](retail/shelf-availability-heatmap.html) - Map availability or stockout risk by store and category.
- [Basket Sankey](retail/basket-sankey.html) - Show basket flow between entry category, attached items, and checkout.
- [Store Treemap](retail/store-treemap.html) - Map revenue, margin, or traffic by store.
- [Promotion Funnel](retail/promotion-funnel.html) - Track shoppers from exposure to redemption, purchase, repeat, and loyalty.
- [Loyalty Cohort Retention](retail/loyalty-cohort-retention.html) - Track repeat shopping by loyalty cohort.
- [Margin Waterfall](retail/margin-waterfall.html) - Explain gross margin from sales through markdowns, shrink, labor, and logistics.
- [Store Score Radar](retail/store-score-radar.html) - Score a store across traffic, conversion, availability, service, and shrink.

### Crypto

Token markets, DeFi liquidity, wallets, protocol revenue, on-chain behavior, risk, and exchange operations.

- [Token Price Line](crypto/token-price-line.html) - Track token price, index level, or protocol metric over time.
- [Liquidity Depth Chart](crypto/liquidity-depth-chart.html) - Visualize bid and ask liquidity around the current token price.
- [Wallet Cohort Retention](crypto/wallet-cohort-retention.html) - Track active wallet retention by first transaction cohort.
- [DeFi Flow Sankey](crypto/defi-flow-sankey.html) - Show value movement between wallets, pools, bridges, and protocols.
- [Protocol Treemap](crypto/protocol-treemap.html) - Map TVL, fees, or volume by protocol or chain.
- [Chain Heatmap](crypto/chain-heatmap.html) - Reveal transaction, gas, or fee intensity by chain and day.
- [Portfolio Donut](crypto/portfolio-donut.html) - Summarize wallet, fund, or treasury allocation by asset.
- [Yield Risk Scatter](crypto/yield-risk-scatter.html) - Position pools by yield and risk or impermanent loss.
- [Liquidation Waterfall](crypto/liquidation-waterfall.html) - Explain collateral movement from price shock, margin call, liquidation, fees, and residual.
- [Protocol Stress Test](crypto/protocol-stress-test.html) - Compare losses under depeg, oracle failure, bridge exploit, and liquidity drain scenarios.

### Fashion

Collections, merchandising, trend signals, inventory, brand performance, runway, and customer style analytics.

- [Trend Line](fashion/trend-line.html) - Track search, sell-through, or social buzz for a style trend.
- [Collection Mix Donut](fashion/collection-mix-donut.html) - Summarize assortment by category, fabric, color, or price tier.
- [Sell Through Stacked Bar](fashion/sell-through-stacked-bar.html) - Break sales by collection, channel, or lifecycle stage.
- [Color Heatmap](fashion/color-heatmap.html) - Map color demand by region, month, or product line.
- [Runway To Retail Funnel](fashion/runway-to-retail-funnel.html) - Track looks from concept to sample, buy, launch, and sold-through.
- [Assortment Treemap](fashion/assortment-treemap.html) - Map revenue or units by style, category, or collection.
- [Customer Cohort Retention](fashion/customer-cohort-retention.html) - Track repeat purchase behavior by customer cohort.
- [Brand Affinity Sankey](fashion/brand-affinity-sankey.html) - Show movement between inspiration, category, collection, and purchase.
- [Markdown Waterfall](fashion/markdown-waterfall.html) - Explain margin movement from full price through markdown, returns, and inventory cost.
- [Style Score Radar](fashion/style-score-radar.html) - Score a look across trend, fit, margin, availability, and brand fit.

### Sports

Team performance, player development, game operations, fan engagement, training, and commercial sports metrics.

- [Performance Line](sports/performance-line.html) - Track wins, points, pace, or rating across games and weeks.
- [Player Usage Stacked Bar](sports/player-usage-stacked-bar.html) - Break minutes, touches, or possessions by player or role.
- [Shot Heatmap](sports/shot-heatmap.html) - Map shot quality, attempts, or scoring zones.
- [Training Calendar](sports/training-calendar.html) - Reveal training load, recovery, or match congestion by day.
- [Fan Funnel](sports/fan-funnel.html) - Track fans from reach to engagement, ticket intent, purchase, and loyalty.
- [Roster Treemap](sports/roster-treemap.html) - Map salary, minutes, or contribution by player group.
- [Injury Risk Scatter](sports/injury-risk-scatter.html) - Position players by workload and injury risk or fatigue score.
- [Season Ticket Cohort](sports/season-ticket-cohort.html) - Track renewal or attendance by buyer cohort.
- [Match Flow Sankey](sports/match-flow-sankey.html) - Show possession or play flow between zones and outcomes.
- [Athlete Score Radar](sports/athlete-score-radar.html) - Score an athlete across skill, speed, endurance, decision, and availability.

### Pets

Pet health, care routines, marketplace behavior, adoption, insurance, services, and owner engagement.

- [Wellness Line](pets/wellness-line.html) - Track weight, activity, symptoms, or wellness score over time.
- [Care Calendar](pets/care-calendar.html) - Show feeding, medication, grooming, vaccination, or visit adherence by day.
- [Adoption Funnel](pets/adoption-funnel.html) - Track pets from listed to viewed, applied, visited, approved, and adopted.
- [Service Mix Donut](pets/service-mix-donut.html) - Summarize spending or bookings by grooming, vet, food, insurance, and toys.
- [Clinic Flow Sankey](pets/clinic-flow-sankey.html) - Show movement from appointment reason to diagnosis, treatment, and follow-up.
- [Breed Health Heatmap](pets/breed-health-heatmap.html) - Map common risk or care metrics by breed and age group.
- [Subscription Cohort Retention](pets/subscription-cohort-retention.html) - Track repeat orders or plan retention by signup cohort.
- [Product Treemap](pets/product-treemap.html) - Map pet product revenue by category or brand.
- [Claim Waterfall](pets/claim-waterfall.html) - Explain insurance claim value from invoice, deductible, exclusions, copay, and reimbursement.
- [Pet Profile Radar](pets/pet-profile-radar.html) - Score care needs across activity, diet, grooming, medical, training, and socialization.

## Maintenance

Maintainers should add or edit chart HTML files one at a time, update this
index by hand, and update the matching gallery card in `index.html` in the
same change.
