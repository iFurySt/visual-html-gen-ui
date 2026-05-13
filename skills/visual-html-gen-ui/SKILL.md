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

### Travel

Trips, bookings, destinations, itinerary planning, hospitality, demand forecasting, and traveler experience.

- [Booking Line](travel/booking-line/index.html) - Track bookings, room nights, or ticket volume over time.
- [Destination Share Donut](travel/destination-share-donut/index.html) - Summarize trips by destination, region, or travel type.
- [Booking Funnel](travel/booking-funnel/index.html) - Track search, quote, checkout, payment, confirmation, and check-in.
- [Itinerary Sankey](travel/itinerary-sankey/index.html) - Show traveler movement across origin, destination, lodging, activity, and return.
- [Seasonality Calendar](travel/seasonality-calendar/index.html) - Reveal booking or travel intensity by day.
- [Route Heatmap](travel/route-heatmap/index.html) - Map demand, occupancy, or price by route and month.
- [Hotel Portfolio Treemap](travel/hotel-portfolio-treemap/index.html) - Map revenue or nights by hotel, destination, or brand.
- [Traveler Retention Cohort](travel/traveler-retention-cohort/index.html) - Track repeat bookings by acquisition cohort.
- [Trip Margin Waterfall](travel/trip-margin-waterfall/index.html) - Explain margin from gross booking through discounts, fees, supplier cost, and support.
- [Experience Radar](travel/experience-radar/index.html) - Score travel experience across price, convenience, support, quality, and flexibility.

### Biotech

Drug discovery, clinical trials, lab operations, biomarkers, pipelines, safety, and R&D portfolio views.

- [Biomarker Line](biotech/biomarker-line/index.html) - Track biomarker or assay response over study time.
- [Trial Enrollment Funnel](biotech/trial-enrollment-funnel/index.html) - Track screened, eligible, consented, randomized, and completed subjects.
- [Pipeline Sankey](biotech/pipeline-sankey/index.html) - Show candidate movement through discovery, preclinical, phase, and approval stages.
- [Assay Heatmap](biotech/assay-heatmap/index.html) - Map assay response by compound and target.
- [Portfolio Treemap](biotech/portfolio-treemap/index.html) - Map program value, risk, or spend by therapeutic area.
- [Dose Response Scatter](biotech/dose-response-scatter/index.html) - Position cohorts by dose and response or adverse event rate.
- [Patient Cohort Retention](biotech/patient-cohort-retention/index.html) - Track follow-up, adherence, or endpoint capture by cohort.
- [R and D Waterfall](biotech/r-and-d-waterfall/index.html) - Explain R&D cash movement from funding, spend, milestones, grants, and runway.
- [Program Risk Radar](biotech/program-risk-radar/index.html) - Score a program across efficacy, safety, CMC, regulatory, IP, and market fit.
- [Clinical Stress Test](biotech/clinical-stress-test/index.html) - Compare timeline or cash need under enrollment delay, safety signal, and regulatory scenarios.

### Legal

Matter management, contracts, litigation, compliance, risk, billing, and legal operations dashboards.

- [Matter Volume Line](legal/matter-volume-line/index.html) - Track opened, closed, or active matters over time.
- [Contract Review Funnel](legal/contract-review-funnel/index.html) - Track contracts from intake to redline, negotiation, approval, and signature.
- [Case Stage Sankey](legal/case-stage-sankey/index.html) - Show matters moving through investigation, filing, discovery, settlement, and close.
- [Risk Heatmap](legal/risk-heatmap/index.html) - Map legal risk by business unit and issue type.
- [Billing Waterfall](legal/billing-waterfall/index.html) - Explain spend from budget through outside counsel, discounts, accruals, and variance.
- [Clause Treemap](legal/clause-treemap/index.html) - Map contract clause frequency or negotiation effort by clause type.
- [Compliance Calendar](legal/compliance-calendar/index.html) - Show filings, deadlines, audits, and policy updates by date.
- [Matter Cohort](legal/matter-cohort/index.html) - Track matter resolution or aging by intake cohort.
- [Case Merit Radar](legal/case-merit-radar/index.html) - Score matters across evidence, damages, precedent, cost, timing, and risk.
- [Litigation Stress Test](legal/litigation-stress-test/index.html) - Compare exposure under settlement, trial, appeal, and adverse judgment scenarios.

### Government

Public services, budgets, case queues, civic operations, policy outcomes, and infrastructure programs.

- [Service Demand Line](government/service-demand-line/index.html) - Track public service requests, permits, or cases over time.
- [Budget Allocation Donut](government/budget-allocation-donut/index.html) - Summarize budget by agency, program, or funding source.
- [Permit Funnel](government/permit-funnel/index.html) - Track applications through submitted, reviewed, corrected, approved, and issued.
- [Case Flow Sankey](government/case-flow-sankey/index.html) - Show case movement across intake, eligibility, review, service, and close.
- [District Heatmap](government/district-heatmap/index.html) - Map service need or outcome metrics by district and topic.
- [Program Treemap](government/program-treemap/index.html) - Map spend or outcomes by program area.
- [Deadline Calendar](government/deadline-calendar/index.html) - Show public hearings, filing deadlines, grant windows, and reporting dates.
- [Outcome Cohort](government/outcome-cohort/index.html) - Track participant outcomes by intake cohort.
- [Policy Score Radar](government/policy-score-radar/index.html) - Score policy options across cost, reach, equity, feasibility, and risk.
- [Budget Stress Test](government/budget-stress-test/index.html) - Compare budget gap under inflation, revenue decline, demand spike, and disaster scenarios.

### Manufacturing

Production, quality, supply chain, maintenance, throughput, yield, and factory operations analytics.

- [Production Line](manufacturing/production-line/index.html) - Track output, yield, or throughput over shifts and weeks.
- [Quality Stacked Bar](manufacturing/quality-stacked-bar/index.html) - Break production into pass, rework, scrap, and hold states.
- [Defect Heatmap](manufacturing/defect-heatmap/index.html) - Map defect rate by station and defect type.
- [Supply Flow Sankey](manufacturing/supply-flow-sankey/index.html) - Show material flow from suppliers to lines, inventory, and shipment.
- [OEE KPI](manufacturing/oee-kpi/index.html) - Compare availability, performance, quality, cycle time, and scrap efficiency.
- [Line Utilization Calendar](manufacturing/line-utilization-calendar/index.html) - Reveal shift utilization or downtime by day.
- [Product Mix Treemap](manufacturing/product-mix-treemap/index.html) - Map output, revenue, or margin by product family.
- [Maintenance Funnel](manufacturing/maintenance-funnel/index.html) - Track work orders from created to triaged, scheduled, completed, and verified.
- [Cost Waterfall](manufacturing/cost-waterfall/index.html) - Explain cost movement from materials, labor, energy, rework, and logistics.
- [Factory Risk Radar](manufacturing/factory-risk-radar/index.html) - Score a plant across safety, quality, capacity, maintenance, supply, and cost.

### Energy

Generation, demand, grid operations, trading, storage, renewables, emissions, and asset performance.

- [Load Line](energy/load-line/index.html) - Track power demand, generation, or price over time.
- [Generation Stack Area](energy/generation-stack-area/index.html) - Emphasize generation mix or supply stack over time.
- [Fuel Mix Donut](energy/fuel-mix-donut/index.html) - Summarize generation or consumption by energy source.
- [Grid Heatmap](energy/grid-heatmap/index.html) - Map load, congestion, or outage risk by region and hour.
- [Dispatch Sankey](energy/dispatch-sankey/index.html) - Show energy flow from generation sources to grid, storage, and load.
- [Asset Treemap](energy/asset-treemap/index.html) - Map capacity, revenue, or emissions by asset.
- [Price Risk Scatter](energy/price-risk-scatter/index.html) - Position markets or assets by price volatility and margin.
- [Emissions Waterfall](energy/emissions-waterfall/index.html) - Explain emissions movement from demand, efficiency, renewables, offsets, and fuel mix.
- [Project Sensitivity Tornado](energy/project-sensitivity-tornado/index.html) - Rank price, capex, capacity factor, and financing assumptions by project return effect.
- [Supply Stress Test](energy/supply-stress-test/index.html) - Compare reserve margin under outage, heat wave, fuel shock, and demand spike scenarios.

### Retail

Store operations, category management, merchandising, footfall, inventory, promotions, and basket analytics.

- [Same Store Sales Line](retail/same-store-sales-line/index.html) - Track same-store sales, footfall, or conversion over time.
- [Category Mix Stacked Bar](retail/category-mix-stacked-bar/index.html) - Break store sales into category or department components.
- [Store Traffic Calendar](retail/store-traffic-calendar/index.html) - Reveal footfall or transaction pressure by day.
- [Shelf Availability Heatmap](retail/shelf-availability-heatmap/index.html) - Map availability or stockout risk by store and category.
- [Basket Sankey](retail/basket-sankey/index.html) - Show basket flow between entry category, attached items, and checkout.
- [Store Treemap](retail/store-treemap/index.html) - Map revenue, margin, or traffic by store.
- [Promotion Funnel](retail/promotion-funnel/index.html) - Track shoppers from exposure to redemption, purchase, repeat, and loyalty.
- [Loyalty Cohort Retention](retail/loyalty-cohort-retention/index.html) - Track repeat shopping by loyalty cohort.
- [Margin Waterfall](retail/margin-waterfall/index.html) - Explain gross margin from sales through markdowns, shrink, labor, and logistics.
- [Store Score Radar](retail/store-score-radar/index.html) - Score a store across traffic, conversion, availability, service, and shrink.

### Crypto

Token markets, DeFi liquidity, wallets, protocol revenue, on-chain behavior, risk, and exchange operations.

- [Token Price Line](crypto/token-price-line/index.html) - Track token price, index level, or protocol metric over time.
- [Liquidity Depth Chart](crypto/liquidity-depth-chart/index.html) - Visualize bid and ask liquidity around the current token price.
- [Wallet Cohort Retention](crypto/wallet-cohort-retention/index.html) - Track active wallet retention by first transaction cohort.
- [DeFi Flow Sankey](crypto/defi-flow-sankey/index.html) - Show value movement between wallets, pools, bridges, and protocols.
- [Protocol Treemap](crypto/protocol-treemap/index.html) - Map TVL, fees, or volume by protocol or chain.
- [Chain Heatmap](crypto/chain-heatmap/index.html) - Reveal transaction, gas, or fee intensity by chain and day.
- [Portfolio Donut](crypto/portfolio-donut/index.html) - Summarize wallet, fund, or treasury allocation by asset.
- [Yield Risk Scatter](crypto/yield-risk-scatter/index.html) - Position pools by yield and risk or impermanent loss.
- [Liquidation Waterfall](crypto/liquidation-waterfall/index.html) - Explain collateral movement from price shock, margin call, liquidation, fees, and residual.
- [Protocol Stress Test](crypto/protocol-stress-test/index.html) - Compare losses under depeg, oracle failure, bridge exploit, and liquidity drain scenarios.

### Fashion

Collections, merchandising, trend signals, inventory, brand performance, runway, and customer style analytics.

- [Trend Line](fashion/trend-line/index.html) - Track search, sell-through, or social buzz for a style trend.
- [Collection Mix Donut](fashion/collection-mix-donut/index.html) - Summarize assortment by category, fabric, color, or price tier.
- [Sell Through Stacked Bar](fashion/sell-through-stacked-bar/index.html) - Break sales by collection, channel, or lifecycle stage.
- [Color Heatmap](fashion/color-heatmap/index.html) - Map color demand by region, month, or product line.
- [Runway To Retail Funnel](fashion/runway-to-retail-funnel/index.html) - Track looks from concept to sample, buy, launch, and sold-through.
- [Assortment Treemap](fashion/assortment-treemap/index.html) - Map revenue or units by style, category, or collection.
- [Customer Cohort Retention](fashion/customer-cohort-retention/index.html) - Track repeat purchase behavior by customer cohort.
- [Brand Affinity Sankey](fashion/brand-affinity-sankey/index.html) - Show movement between inspiration, category, collection, and purchase.
- [Markdown Waterfall](fashion/markdown-waterfall/index.html) - Explain margin movement from full price through markdown, returns, and inventory cost.
- [Style Score Radar](fashion/style-score-radar/index.html) - Score a look across trend, fit, margin, availability, and brand fit.

### Sports

Team performance, player development, game operations, fan engagement, training, and commercial sports metrics.

- [Performance Line](sports/performance-line/index.html) - Track wins, points, pace, or rating across games and weeks.
- [Player Usage Stacked Bar](sports/player-usage-stacked-bar/index.html) - Break minutes, touches, or possessions by player or role.
- [Shot Heatmap](sports/shot-heatmap/index.html) - Map shot quality, attempts, or scoring zones.
- [Training Calendar](sports/training-calendar/index.html) - Reveal training load, recovery, or match congestion by day.
- [Fan Funnel](sports/fan-funnel/index.html) - Track fans from reach to engagement, ticket intent, purchase, and loyalty.
- [Roster Treemap](sports/roster-treemap/index.html) - Map salary, minutes, or contribution by player group.
- [Injury Risk Scatter](sports/injury-risk-scatter/index.html) - Position players by workload and injury risk or fatigue score.
- [Season Ticket Cohort](sports/season-ticket-cohort/index.html) - Track renewal or attendance by buyer cohort.
- [Match Flow Sankey](sports/match-flow-sankey/index.html) - Show possession or play flow between zones and outcomes.
- [Athlete Score Radar](sports/athlete-score-radar/index.html) - Score an athlete across skill, speed, endurance, decision, and availability.

### Pets

Pet health, care routines, marketplace behavior, adoption, insurance, services, and owner engagement.

- [Wellness Line](pets/wellness-line/index.html) - Track weight, activity, symptoms, or wellness score over time.
- [Care Calendar](pets/care-calendar/index.html) - Show feeding, medication, grooming, vaccination, or visit adherence by day.
- [Adoption Funnel](pets/adoption-funnel/index.html) - Track pets from listed to viewed, applied, visited, approved, and adopted.
- [Service Mix Donut](pets/service-mix-donut/index.html) - Summarize spending or bookings by grooming, vet, food, insurance, and toys.
- [Clinic Flow Sankey](pets/clinic-flow-sankey/index.html) - Show movement from appointment reason to diagnosis, treatment, and follow-up.
- [Breed Health Heatmap](pets/breed-health-heatmap/index.html) - Map common risk or care metrics by breed and age group.
- [Subscription Cohort Retention](pets/subscription-cohort-retention/index.html) - Track repeat orders or plan retention by signup cohort.
- [Product Treemap](pets/product-treemap/index.html) - Map pet product revenue by category or brand.
- [Claim Waterfall](pets/claim-waterfall/index.html) - Explain insurance claim value from invoice, deductible, exclusions, copay, and reimbursement.
- [Pet Profile Radar](pets/pet-profile-radar/index.html) - Score care needs across activity, diet, grooming, medical, training, and socialization.

## Maintenance

Maintainers should edit `catalog.json`, run
`python3 scripts/build_charts.py`, then run
`python3 scripts/validate_skill.py` before committing.
