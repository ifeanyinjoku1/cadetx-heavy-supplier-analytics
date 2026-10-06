# Week 11 — Business Intelligence Dashboard & Decision Support

## Overview

Week 11 focuses on integrating the analytical outputs developed throughout the previous sprints into a consolidated Business Intelligence and Decision Support solution.

The objective is to bring together sales, product, inventory requirements, warehouse, customer, and forecasting analysis into an executive-level dashboard that communicates key business performance indicators, trends, opportunities, and areas requiring management attention.

Instead of using Power BI, the dashboard was developed in **Python using Plotly**, allowing the complete dashboard solution to be created and exported as interactive HTML files.

---

## Sprint Goal

> Integrate key sales, product, inventory, warehouse, customer, and forecasting insights into an interactive Business Intelligence dashboard to support performance monitoring and data-driven decision-making.

---

## Objectives

The main objectives of Week 11 were to:

- Consolidate outputs from previous analytical sprints.
- Develop an executive-level KPI framework.
- Analyse overall sales performance.
- Compare product performance.
- Analyse inventory requirements.
- Evaluate warehouse and branch performance.
- Analyse customer performance and revenue concentration.
- Integrate sales forecasting results from Week 9.
- Develop interactive Python dashboards using Plotly.
- Identify important business findings and potential areas for management attention.
- Produce a professional dashboard suitable for business reporting and presentation.

---

## Data Sources

The analysis uses the integrated sales and product dataset developed during the earlier project stages.

### Main Dataset

`sales_integrated.csv`

The integrated dataset contains information relating to:

- Sales orders
- Products
- Customers
- Branches
- Sales channels
- Product characteristics
- Customer characteristics
- Inventory planning parameters
- Historical sales activity

### Forecast Dataset

`future_sales_forecast.csv`

This dataset contains the future revenue forecast generated during Week 9.

Key forecast fields:

- `forecast_date`
- `forecasted_revenue`

---

## Key KPIs

The Week 11 dashboard consolidates the following KPIs:

| KPI | Purpose |
|---|---|
| Total Revenue | Measure overall sales contribution |
| Total Orders | Measure sales activity |
| Total Units Sold | Measure product movement |
| Total Products | Measure product coverage |
| Total Customers | Measure customer base |
| Total Branches | Measure operational locations |
| Average Order Value | Measure average order contribution |
| Repeat Customer Rate | Measure repeat purchasing behaviour |
| Average Product Performance Score | Compare product performance |
| Average Warehouse Performance Score | Compare branch performance |
| Safety Stock Value | Support inventory planning |
| Reorder Stock Value | Support replenishment planning |
| Maximum Stock Value | Estimate maximum planned stock value |

---

# Dashboard Structure

The Week 11 Python dashboard is divided into five interactive HTML dashboards.

---

## Dashboard 1 — Executive Overview

### Visualisations

- Monthly Revenue Trend
- Top 10 Products by Revenue
- Revenue by Region
- Executive KPI Summary

### Key Questions

- How has revenue changed over time?
- Which products generate the highest revenue?
- Which regions contribute the most revenue?
- What is the overall business performance?
- What are the main executive-level KPIs?

### Output

```text
01_executive_overview.html
