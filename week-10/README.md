# Week 10: Advanced Sales & Customer Analytics
**Phase 3:** Advanced Analytics & Business Intelligence  
**Sprint Goal:** Analyze sales, customer, and product patterns using advanced analytics to identify business opportunities, customer behavior, and key factors driving performance.

---

## 📌 Executive Summary
This sprint focuses on behavioral customer segmentation, purchase frequency, product affinity, and revenue concentration risk. Using RFM (Recency, Frequency, Monetary) modeling and cohort retention frameworks, we identified top-tier customer segments, revenue vulnerabilities, and high-impact retention opportunities.

---

## 📈 Key Metrics & KPI Summary

| Metric / KPI | Value / Result | Business Impact |
| :--- | :--- | :--- |
| **Total Customers** | 4,372 | Total registered purchasing accounts. |
| **Active Customers** | 3,105 | Accounts with active purchases in the last 90 days. |
| **Repeat Customer Rate** | 64.2% | High baseline loyalty; candidates for cross-selling. |
| **Average Customer Value** | $1,280.50 | Baseline customer revenue yield over 12 months. |
| **Average Orders per Customer**| 4.8 orders | Baseline purchasing frequency per active account. |
| **Top Customer Segment** | Champions (RFM 555) | Generates 48% of total revenue despite being 12% of users. |
| **Customer Concentration** | Top 10% = 58% Revenue | Significant concentration risk requiring retention focus. |

---

## 📊 Analytical Scope & Key Visualizations

The following core analyses and visualizations were generated in `notebooks/01_advanced_customer_sales_analysis.ipynb`:

1. **Customer Revenue Distribution:** Pareto analysis confirming top-decile revenue concentration.
2. **Purchase Frequency Histogram:** Breakdown of one-time vs. repeat purchasing cycles.
3. **RFM Customer Segmentation:** Categorization into Champions, Loyal, At-Risk, and Dormant groups.
4. **Cohort Retention Heatmap:** Tracking repeat order rates over 12 rolling months.
5. **Product-Customer Affinity Matrix:** Mapping top-performing products across customer tiers.

---

## 💡 Key Business Findings

* **High Concentration Risk:** The top 10% of customers contribute **58% of overall revenue**. Losing key accounts in this group poses a direct risk to revenue stability.
* **The "One-Time Purchaser" Gap:** 35.8% of customers make only one purchase and never return. Increasing the conversion of single buyers to 2-time buyers by 10% yields an estimated **$140,000 ARR lift**.
* **High-Value Product Preference:** Premium product bundles (Category A) account for 72% of purchases made by the "Champions" segment.

---

## 🚀 Strategic Recommendations

1. **VIP Loyalty & Concierge Program:** Implement dedicated account management for the top 10% of customers to prevent churn.
2. **Post-Purchase Re-engagement:** Launch automated email workflows at day 14 and day 30 post-first purchase to target single-buy customers with customized cross-sell offers.
3. **Cross-Selling Premium Bundles:** Market Category A products directly to the "Loyal" segment to upgrade them into the high-value "Champions" tier.

---

## ⚙️ Repository Structure

```text
week-10/
├── notebooks/
│   └── 01_advanced_customer_sales_analysis.ipynb
├── analysis/
│   └── rfm_segmentation_summary.csv
└── README.md

