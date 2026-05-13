## [2026-05-13 19:26] | Task: Ecommerce domain chart pass

### Execution Context

- Agent ID: `Codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Continue domain-by-domain cleanup so non-finance examples are no longer
> template-like; validate and commit each finished domain before moving on.

### Changes Overview

- Area: `ecommerce` chart examples and gallery cards.
- Key actions:
  - Reworked all 10 Ecommerce chart pages away from generic sample titles and
    metadata.
  - Updated chart purposes, headings, notes, and signals around actual
    merchandising, growth, inventory, and profitability decisions.
  - Manually synchronized the Ecommerce entries in `SKILL.md` and `index.html`.

### Design Intent

Ecommerce examples should support practical operating questions: campaign GMV
lift, checkout friction, channel mix, product contribution margin, inventory
coverage, repeat purchase quality, acquisition economics, basket affinity, SKU
concentration, and promotion profit sensitivity.

### Files Modified

- `index.html`
- `skills/visual-html-gen-ui/SKILL.md`
- `skills/visual-html-gen-ui/ecommerce/basket-affinity-sankey.html`
- `skills/visual-html-gen-ui/ecommerce/category-sales-stacked-bar.html`
- `skills/visual-html-gen-ui/ecommerce/checkout-funnel.html`
- `skills/visual-html-gen-ui/ecommerce/customer-cohort-retention.html`
- `skills/visual-html-gen-ui/ecommerce/inventory-heatmap.html`
- `skills/visual-html-gen-ui/ecommerce/ltv-cac-kpi.html`
- `skills/visual-html-gen-ui/ecommerce/product-margin-waterfall.html`
- `skills/visual-html-gen-ui/ecommerce/promo-sensitivity-tornado.html`
- `skills/visual-html-gen-ui/ecommerce/revenue-line.html`
- `skills/visual-html-gen-ui/ecommerce/sku-performance-treemap.html`
