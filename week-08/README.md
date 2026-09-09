# Week 08 — Customer & Sales Performance Analysis

## Phase
**Phase 2 — Core Product, Inventory & Warehouse Analytics**

## Sprint Goal
Analyse customer and sales performance to identify key customer segments, purchasing patterns, revenue contribution, and opportunities for improving customer and sales performance.

---

## Main Tasks

- Analyse customer purchasing behaviour.
- Analyse customer revenue contribution.
- Segment customers based on purchasing activity and revenue.
- Analyse customer types and industry segments.
- Compare sales performance across customer segments.
- Identify high-value and low-value customers.
- Analyse purchasing patterns across regions and sales channels.
- Analyse customer revenue concentration.
- Identify potential customer and sales opportunities.

---

## Data Used

The analysis uses the integrated `product_sales` dataset developed for the Phase 2 analysis.

Key fields used include:

- `customer_id`
- `customer_type`
- `industry_segment`
- `city`
- `state`
- `region`
- `sales_channel`
- `so_id`
- `product_id`
- `quantity`
- `line_total`
- `order_date`

---

## Analysis Workflow

`Integrated Product Sales Data`
→ `Data Preparation`
→ `Customer Performance`
→ `Customer Segmentation`
→ `Customer Type Analysis`
→ `Industry & Regional Analysis`
→ `Sales Channel Analysis`
→ `Customer Revenue Concentration`
→ `Performance Scoring`
→ `Business Insights`

---

## Key KPIs

| KPI | Purpose |
|---|---|
| Total Customers | Measure customer base |
| Total Orders | Measure purchasing activity |
| Total Units Sold | Measure sales volume |
| Total Revenue | Measure overall sales contribution |
| Average Revenue per Customer | Compare customer value |
| Average Orders per Customer | Measure purchasing frequency |
| High-Value Customers | Identify important customers |
| Low-Value Customers | Identify customers requiring further analysis |
| Average Customer Performance Score | Compare customer performance |
| Top 10 Customer Revenue Share | Measure customer revenue concentration |

---

## Customer Performance Scoring

Customer performance is evaluated using:

- Revenue — 50%
- Orders — 30%
- Units Sold — 20%

Customers are classified using relative performance thresholds:

- **High Performance** — Top 25%
- **Medium Performance** — Middle 50%
- **Low Performance** — Bottom 25%

Customer value is also classified using revenue quartiles:

- **High Value** — Top 25%
- **Medium Value** — Middle 50%
- **Low Value** — Bottom 25%

> The performance score is an analytical measure created for this sprint to support relative comparison.

---

## Visualizations

- Top customers by revenue
- Top customers by order volume
- Revenue by customer type
- Revenue by industry segment
- Revenue by region
- Revenue by sales channel
- Customer performance distribution
- Customer value distribution
- Customer revenue concentration

---

## Business Questions

1. Which customers generate the highest revenue?
2. Which customers place the highest number of orders?
3. Which customer types contribute the most revenue?
4. Which industry segments generate the most revenue?
5. Which regions have the highest sales?
6. Which sales channels perform best?
7. Are revenues concentrated among a small number of customers?
8. Which customers are classified as high-value?
9. Which customers have relatively low performance?
10. Which customer segments may require further investigation?

---

## Key Findings

*To be completed after reviewing the final analysis results and visualisations.*

Potential areas of discussion include:

- Highest-revenue customers
- Highest-volume customers
- High-, medium-, and low-value customer groups
- High- and low-performing customers
- Customer types contributing the most revenue
- Highest-performing industry segments
- Regional sales differences
- Sales channel performance
- Customer revenue concentration

---

## Business Insights

*To be completed after reviewing the final KPI results.*

The analysis can support decisions related to:

- Customer prioritisation
- Customer relationship management
- Sales strategy
- Market segmentation
- Regional sales planning
- Sales channel optimisation
- Retention of high-value customers
- Investigation of low-performing customer segments

---

## Limitations

- Customer performance is based on sales activity available in the integrated `product_sales` dataset.
- Customer value categories are relative to the distribution of customers in the dataset.
- Performance scores are analytical measures rather than official business scoring standards.
- A high or low performance classification does not necessarily indicate customer satisfaction or profitability.

---

## Outputs

### Analysis Files

- `customer_performance.csv`
- `customer_type_analysis.csv`
- `industry_segment_analysis.csv`
- `regional_sales_analysis.csv`
- `sales_channel_analysis.csv`
- `customer_revenue_concentration.csv`
- `week8_customer_sales_kpis.csv`

---

## Notebook

`notebooks/Customer_&_Sales_Performance_Analysis.ipynb`

---

## GitHub Structure

```text
week-08/
├── notebooks/
│   └── 01_customer_sales_analysis.ipynb
│
├── analysis/
│   ├── customer_performance.csv
│   ├── customer_type_analysis.csv
│   ├── industry_segment_analysis.csv
│   ├── regional_sales_analysis.csv
│   ├── sales_channel_analysis.csv
│   ├── customer_revenue_concentration.csv
│   └── week8_customer_sales_kpis.csv
│
└── README.md
