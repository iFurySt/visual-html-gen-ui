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

- [Active Users Line](social/active-users-line.html) - Track daily active users around launches, notification changes, and creator campaigns.
- [Engagement Area](social/engagement-area.html) - Emphasize accumulated reactions, comments, shares, and saves after content launches.
- [Activation Funnel](social/activation-funnel.html) - Track new users from signup through profile setup, first follow, first post, and day-7 return.
- [Creator Network Sankey](social/creator-network-sankey.html) - Show audience movement from creators into topics, communities, follows, and shares.
- [Topic Heatmap](social/topic-heatmap.html) - Reveal topic momentum by day, community segment, and moderation sensitivity.
- [Community Treemap](social/community-treemap.html) - Map communities by active members, post volume, and moderation workload.
- [User Cohort Retention](social/user-cohort-retention.html) - Track retained users by signup cohort, lifecycle age, and first community joined.
- [Influence Bubble](social/influence-bubble.html) - Compare creators by reach, engagement quality, audience size, and trust risk.
- [Moderation Waterfall](social/moderation-waterfall.html) - Explain moderation queue changes from report inflow, automation, review, appeals, and backlog.
- [Community Health Radar](social/community-health-radar.html) - Score community health across safety, activity, diversity, creator supply, retention, and trust.

### Entertainment

Streaming, music, film, live events, audience behavior, releases, and catalog performance.

- [Viewership Line](entertainment/viewership-line.html) - Track episode watch time before and after trailer, premiere, and finale drops.
- [Catalog Share Donut](entertainment/catalog-share-donut.html) - Summarize where a featured title's watch starts come from across discovery surfaces.
- [Box Office Stacked Bar](entertainment/box-office-stacked-bar.html) - Break weekly title demand by search, playlist, and recommendation channels after launch.
- [Audience Retention Cohort](entertainment/audience-retention-cohort.html) - Track how catalog, long-tail, prelaunch, launch, and weekly cohorts retain viewers over time.
- [Release Calendar Heatmap](entertainment/release-calendar-heatmap.html) - Show when catalog refreshes, long-tail pushes, trailers, premieres, and week-one activity collide.
- [Genre Momentum Heatmap](entertainment/genre-momentum-heatmap.html) - Reveal genre demand shifts as a release campaign changes audience attention week by week.
- [Playlist Flow Sankey](entertainment/playlist-flow-sankey.html) - Show how audiences move from owned channels and ticketing into merch, trailers, shows, and playlists.
- [Talent Score Radar](entertainment/talent-score-radar.html) - Score talent or titles before greenlight, booking, sponsorship, or cross-promotion decisions.
- [Campaign Funnel](entertainment/campaign-funnel.html) - Track a title campaign from audience follow-through to trailer exposure, intent, and purchase.
- [Title Portfolio Treemap](entertainment/title-portfolio-treemap.html) - Map catalog portfolio weight by genre to find hit concentration and underused long-tail shelves.

### Gaming

Game telemetry, player progression, economy balance, monetization, matchmaking, and live ops.

- [DAU Line](gaming/dau-line.html) - Track daily active players across season launch, finale event, patch, and D7 return windows.
- [Level Progression Funnel](gaming/level-progression-funnel.html) - Find where new players drop from tutorial completion through first PvP or co-op session and core-loop return.
- [Economy Sankey](gaming/economy-sankey.html) - Visualize premium currency and crafted-item movement between store, crafting, inventory, sinks, and wallet balances.
- [Session Calendar](gaming/session-calendar.html) - Reveal session intensity around season, finale, patch, event, and retention checkpoints.
- [Mode Popularity Stacked Bar](gaming/mode-popularity-stacked-bar.html) - Break engagement mix by boosts, events, and inventory activity across live-ops beats.
- [Matchmaking Heatmap](gaming/matchmaking-heatmap.html) - Show friction and quality signals across onboarding, PvP, co-op, store, and guild touchpoints during season beats.
- [Player Retention Cohort](gaming/player-retention-cohort.html) - Track retention for season, finale, patch, and early lifecycle cohorts through the first week.
- [Item Sales Treemap](gaming/item-sales-treemap.html) - Map monetization contribution by mode and social surface to separate store demand from gameplay-driven purchases.
- [Balance Tornado](gaming/balance-tornado.html) - Rank tuning variables by expected impact on match fairness, progression speed, and reward pacing.
- [Player Segment Radar](gaming/player-segment-radar.html) - Compare target player segments across risk, retention, skill, spend, social behavior, and completion.

### Content Creation

Creator workflow, publishing cadence, audience growth, monetization, editorial planning, and performance.

- [Publishing Cadence Line](content-creation/publishing-cadence-line.html) - Track publishing cadence across shorts, long-form, newsletters, and campaign assets.
- [Content Pipeline Funnel](content-creation/content-pipeline-funnel.html) - Track ideas through brief, draft, edit, review, scheduled, and published steps.
- [Channel Mix Donut](content-creation/channel-mix-donut.html) - Summarize audience reach or revenue by platform, owned channel, and paid surface.
- [Audience Growth Area](content-creation/audience-growth-area.html) - Emphasize cumulative followers, subscribers, and email capture after launches and collaborations.
- [Editorial Calendar Heatmap](content-creation/editorial-calendar-heatmap.html) - Show publishing load, review collisions, and campaign gaps by day.
- [Content Performance Treemap](content-creation/content-performance-treemap.html) - Map views, revenue, and engagement by series or format to reveal hits and long-tail shelves.
- [Creator Retention Cohort](content-creation/creator-retention-cohort.html) - Track repeat viewers, subscribers, and paid supporters by acquisition cohort and first content touch.
- [Platform Flow Sankey](content-creation/platform-flow-sankey.html) - Show audience movement from discovery platforms into follows, email, community, paid support, and purchase.
- [Monetization KPI](content-creation/monetization-kpi.html) - Compare RPM, support conversion, paid community mix, payback, and revenue per fan after a campaign.
- [Format Score Radar](content-creation/format-score-radar.html) - Score formats across reach, depth, effort, reuse, monetization, and audience fit for editorial planning.

### Enterprise Services

B2B sales, delivery, support, customer success, implementation, and account health analytics.

- [ARR Line](enterprise-services/arr-line.html) - Track ARR movement from new logos, expansion, renewals, churn, and contracted backlog across quarters.
- [Sales Pipeline Funnel](enterprise-services/sales-pipeline-funnel.html) - Track enterprise opportunities from lead through qualification, proposal, procurement, and closed won.
- [Implementation Sankey](enterprise-services/implementation-sankey.html) - Show customers moving from kickoff through setup, integration, training, go-live, and support handoff.
- [Ticket Heatmap](enterprise-services/ticket-heatmap.html) - Reveal support load by severity, product area, and daypart for customer escalations.
- [Account Health Radar](enterprise-services/account-health-radar.html) - Score renewal accounts across adoption, support burden, expansion readiness, sentiment, and risk.
- [Service Margin Waterfall](enterprise-services/service-margin-waterfall.html) - Explain services gross margin from contract value through labor, travel, support, and delivery overrun.
- [Customer Retention Cohort](enterprise-services/customer-retention-cohort.html) - Track logo and revenue retention by contract cohort, renewal quarter, and onboarding path.
- [SLA Calendar](enterprise-services/sla-calendar.html) - Show SLA breaches, incident pressure, and response-risk clusters by day.
- [Account Portfolio Treemap](enterprise-services/portfolio-treemap.html) - Map revenue and delivery effort by account segment or service line to spot concentration.
- [Sales Efficiency KPI](enterprise-services/sales-efficiency-kpi.html) - Compare CAC, payback, expansion, win rate, and sales-capacity efficiency for enterprise motions.

### Cybersecurity

Threat detection, incidents, vulnerability management, risk posture, response operations, and control health.

- [Incident Line](cybersecurity/incident-line.html) - Track confirmed incidents and high-fidelity alerts across releases, campaigns, and response shifts.
- [Severity Stacked Bar](cybersecurity/severity-stacked-bar.html) - Break open findings by severity across endpoint, identity, cloud, and application remediation waves.
- [Attack Path Sankey](cybersecurity/attack-path-sankey.html) - Show likely attacker movement from phishing or exposed services into lateral movement and data access.
- [Vulnerability Heatmap](cybersecurity/vulnerability-heatmap.html) - Map vulnerability risk by asset class, exploitability, and remediation priority.
- [Response Funnel](cybersecurity/response-funnel.html) - Track alert handling from trigger through triage, investigation, containment, eradication, and closure.
- [Asset Risk Treemap](cybersecurity/asset-risk-treemap.html) - Map residual cyber risk by critical application, host group, and business unit.
- [Control Maturity Radar](cybersecurity/control-maturity-radar.html) - Score core control maturity across identity, endpoint, network, detection, backup, and training.
- [Phishing Calendar](cybersecurity/phishing-calendar.html) - Reveal phishing simulations, reported messages, and training completion pressure by day.
- [Risk Reduction Waterfall](cybersecurity/risk-reduction-waterfall.html) - Explain residual risk movement from new findings, patches, control improvements, exceptions, and accepted risk.
- [Breach Stress Test](cybersecurity/breach-stress-test.html) - Compare estimated loss, downtime, and response capacity under ransomware, data leak, and outage scenarios.

### AI Agent

Agent workflows, model performance, tool use, evaluation, cost, latency, safety, and autonomy analytics.

- [Task Success Line](ai-agent/task-success-line.html) - Track agent task success rate across eval suites, product releases, and prompt or model changes.
- [Latency Area](ai-agent/latency-area.html) - Emphasize cumulative runtime and cost across planning, tool calls, code execution, browser work, and verification.
- [Tool Use Sankey](ai-agent/tool-use-sankey.html) - Show how agent work moves from planning into search, code edits, browser checks, tests, and final verification.
- [Eval Heatmap](ai-agent/eval-heatmap.html) - Map pass rate by task family and capability dimension to expose regressions and coverage gaps.
- [Failure Funnel](ai-agent/failure-funnel.html) - Track agent failures from detection through reproduction, root cause, fix, rerun, and verified pass.
- [Model Cost Scatter](ai-agent/model-cost-scatter.html) - Position model and prompt variants by eval quality, latency, token cost, and production fit.
- [Agent Cohort Retention](ai-agent/agent-cohort-retention.html) - Track repeat workflow success for task cohorts across agent versions, prompts, and tool policies.
- [Capability Radar](ai-agent/capability-radar.html) - Score an agent across planning, tool use, coding, browsing, safety, memory, and verification.
- [Token Waterfall](ai-agent/token-waterfall.html) - Explain token use from system context, retrieved docs, reasoning, tool output, scratch state, and final answer.
- [Safety Stress Test](ai-agent/safety-stress-test.html) - Compare failure rates under normal, adversarial, long-context, stale-context, and tool-error scenarios.

### Real Estate

Property valuation, leasing, occupancy, market supply, rent, cap rates, and asset operations.

- [Price Index Line](real-estate/price-index-line.html) - Track rent index, achieved rent, and cap-rate pressure across submarkets and lease cycles.
- [Occupancy Area](real-estate/occupancy-area.html) - Show leased area and physical occupancy buildup after deliveries, renewals, and move-ins.
- [Lease Funnel](real-estate/lease-funnel.html) - Track prospects from inquiry through tour, application, offer, lease signing, and move-in.
- [Asset Portfolio Treemap](real-estate/portfolio-treemap.html) - Map NOI, valuation, and square-foot exposure by asset, submarket, and property type.
- [Market Heatmap](real-estate/market-heatmap.html) - Compare rent growth, vacancy, absorption, and concession pressure by market and property type.
- [Development Waterfall](real-estate/development-waterfall.html) - Explain development return from land basis through hard costs, financing, lease-up, incentives, and exit value.
- [Tenant Cohort Retention](real-estate/tenant-cohort-retention.html) - Track tenant renewal, expansion, contraction, and move-out patterns by lease-start cohort.
- [Valuation Sensitivity Tornado](real-estate/valuation-sensitivity-tornado.html) - Rank value sensitivity to cap rate, market rent growth, vacancy, downtime, and debt cost assumptions.
- [Asset Score Radar](real-estate/asset-score-radar.html) - Score acquisition or hold decisions across location, income durability, asset condition, tenant quality, liquidity, and risk.
- [Cashflow Stress Test](real-estate/cashflow-stress-test.html) - Compare cashflow resilience under vacancy shock, rate reset, construction delay, refinancing gap, and recession scenarios.

### HR

Workforce planning, recruiting, performance, retention, engagement, compensation, and people operations.

- [Headcount Line](hr/headcount-line.html) - Track approved headcount, open requisitions, starts, exits, and hiring-plan variance by month.
- [Recruiting Funnel](hr/recruiting-funnel.html) - Track candidates from sourced through recruiter screen, hiring-manager review, onsite, offer, accepted, and start.
- [Department Mix Stacked Bar](hr/department-mix-stacked-bar.html) - Break workforce mix by function, level, location, employment type, and manager span.
- [Attrition Calendar](hr/attrition-calendar.html) - Reveal resignation, absence, PTO, and backfill risk patterns by week, month, team, or location.
- [Engagement Heatmap](hr/engagement-heatmap.html) - Map survey engagement scores, manager trust, workload, inclusion, and growth sentiment by team.
- [Compensation Scatter](hr/compensation-scatter.html) - Position employees or roles by compa-ratio, pay band, performance, tenure, and equity review priority.
- [Promotion Cohort](hr/promotion-cohort.html) - Track promotion, lateral move, retention, and time-in-level patterns by starting cohort and demographic segment.
- [Org Treemap](hr/org-treemap.html) - Map headcount, payroll, manager span, and open requisition load by org unit.
- [Performance Radar](hr/performance-radar.html) - Score a team or role family across impact, collaboration, execution, craft, ownership, and growth readiness.
- [Workforce Risk Stress Test](hr/workforce-risk-stress-test.html) - Compare staffing resilience under attrition shock, hiring freeze, demand spike, reorg, and skills-gap scenarios.

### Mobility

Urban mobility, ride hailing, fleet operations, routing, utilization, safety, and multimodal transport.

- [Trip Volume Line](mobility/trip-volume-line.html) - Track ride requests, completed trips, cancellations, ETA, and weather or event demand by hour or day.
- [Fleet Utilization Area](mobility/fleet-utilization-area.html) - Show active, idle, charging, maintenance, and repositioning vehicle capacity across service windows.
- [Dispatch Funnel](mobility/dispatch-funnel.html) - Track requests from open search through match, driver accept, arrival, pickup, completion, and rating.
- [Mobility Route Heatmap](mobility/route-heatmap.html) - Reveal demand, congestion, wait time, and supply gaps by zone, corridor, and time block.
- [Mode Share Donut](mobility/mode-share-donut.html) - Summarize trips by mode, purpose, distance band, and transfer behavior across a city or campus network.
- [Station Treemap](mobility/station-treemap.html) - Map dock, depot, station, or curb-zone usage by departures, arrivals, dwell time, and rebalance need.
- [Driver Cohort Retention](mobility/driver-cohort-retention.html) - Track driver activation, first-trip completion, weekly activity, churn, and reactivation by onboarding cohort.
- [Fare Waterfall](mobility/fare-waterfall.html) - Explain rider fare and driver earnings from base, time, distance, surge, incentives, fees, tolls, and platform margin.
- [Safety Radar](mobility/safety-radar.html) - Score operations across crash rate, harsh braking, compliance, training, vehicle health, and incident response.
- [Demand Stress Test](mobility/demand-stress-test.html) - Compare service capacity under storm, event surge, transit outage, driver shortage, and app incident scenarios.

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
