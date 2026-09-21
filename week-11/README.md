# Week 11: Business Intelligence Dashboard & Decision Support
**Phase 3:** Advanced Analytics & Business Intelligence  
**Sprint Goal:** Integrate key sales, product, inventory, warehouse, customer, and forecasting insights into a unified business intelligence dashboard to support executive decision-making.

---

## 📌 Executive Summary
Week 11 serves as the consolidation sprint, unifying output metrics from across Phase 1 to Phase 3 into an executive-level performance matrix. By pairing historical sales trends with forecast trajectory, warehouse throughput, and customer concentration analysis, this dashboard provides a complete decision-support engine.

---

## 📈 Executive KPI Dashboard Summary

| Metric / KPI | Value / Result | Business Impact & Interpretation |
| :--- | :--- | :--- |
| **Total Revenue** | $1,842,500 | Aggregate historical revenue across all sales channels. |
| **Total Orders** | 12,450 | Total completed transactional orders processed. |
| **Total Units Sold** | 48,200 units | Total volume of inventory units moved. |
| **Average Order Value (AOV)** | $147.99 | Baseline purchase value per order transaction. |
| **Repeat Customer Rate** | 64.2% | Sustained multi-purchase account activity. |
| **Top Customer Segment** | Champions (RFM 555) | High-yield account cohort generating ~48% of total revenue. |
| **Customer Concentration** | Top 10% = 58% Revenue | High key-account dependency requiring operational risk mitigation. |
| **Forecasted Next Qtr Rev** | $520,000 | Model projection for baseline upcoming quarterly sales. |

---

## 📊 Business Intelligence Visualizations

The core script in `notebooks/01_business_intelligence_dashboard.ipynb` generates an integrated 6-panel executive dashboard covering:

1. **Revenue Trend & Forecast:** Historical revenue tracking alongside 3-month projected demand curve.
2. **Top Product Performance:** Combined analysis of revenue generation versus unit volume across top products.
3. **Warehouse Operational Throughput:** Comparative fulfillment capacity and error-rate monitoring across locations.
4. **Customer Revenue Concentration:** Decile analysis highlighting top customer account impact.
5. **Inventory Stocking Requirements:** Safety stock and reorder point thresholds per product line.
6. **Actual vs. Forecast Variance:** Deviation tracking between predictive baseline targets and realized performance.

---

## 💡 Key Business Findings & Exceptions

* **Warehouse Bottlenecks:** Central Warehouse manages 45% of overall fulfillment volume but experiences a **2.3% higher fulfillment delay rate** than regional hubs during peak velocity periods.
* **Inventory Stock-Out Risk:** High demand in Category A products threatens safety stock thresholds within the next 30 days without immediate reorder triggering.
* **Revenue Drivers:** Top 20% of SKU inventory generates **74% of gross revenue**, showing strong alignment with Pareto distribution.

---

## 🚀 Strategic Decision Support & Recommendations

1. **Reallocate Regional Inventory:** Shift 15% of Category A safety stock to Regional Hub East to alleviate fulfillment pressure on Central Warehouse.
2. **Automated Reorder Triggers:** Establish dynamic reorder thresholds tied directly to weekly demand velocity to prevent stock-outs.
3. **Key-Account Retention Safeguards:** Introduce proactive account management for top-decile customers to hedge against key-account churn.

---

## ⚙️ Repository Structure

```text
week-11/
├── notebooks/
│   └── 01_business_intelligence_dashboard.ipynb
├── analysis/
│   └── executive_kpi_summary.csv
└── README.md

