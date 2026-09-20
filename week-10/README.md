# Week 10 — Advanced Customer & Sales Analytics

## Phase
**Phase 3 — Advanced Analytics & Business Intelligence**

## Sprint Goal

Analyse customer, sales, and product purchasing patterns to identify customer behaviour, high-value customers, purchasing frequency, customer segments, and potential sales opportunities.

---

## Main Tasks

- Analyse customer purchasing behaviour.
- Analyse customer revenue contribution.
- Identify high-value and low-value customers.
- Analyse customer purchasing frequency.
- Identify repeat and one-time customers.
- Segment customers based on revenue and order activity.
- Analyse customer types and industry segments.
- Analyse regional and sales channel performance.
- Analyse customer–product relationships.
- Analyse customer revenue concentration.
- Identify potential customer and sales opportunities.
- Develop visualizations to communicate key findings.

---

## Data Used

The analysis uses the integrated **`product_sales`** dataset.

### Key Fields Used

- `customer_id`
- `so_id`
- `product_id`
- `product_name`
- `quantity`
- `line_total`
- `order_date`
- `customer_type`
- `industry_segment`
- `region`
- `sales_channel`
- `branch_id`
- `customer_rating`

---

## Analysis Workflow

`Product Sales Data`
→ `Data Preparation`
→ `Customer Performance`
→ `Customer Segmentation`
→ `Purchase Frequency`
→ `Customer–Product Analysis`
→ `Revenue Concentration`
→ `Regional & Channel Analysis`
→ `Business Investigation`
→ `Key Findings`

---

## Key KPIs

| KPI | Purpose |
|---|---|
| Total Customers | Measure customer base |
| Active Customers | Measure customer activity |
| Total Orders | Measure sales activity |
| Total Revenue | Measure overall sales |
| Average Customer Revenue | Measure average customer contribution |
| Average Orders per Customer | Measure purchasing frequency |
| Repeat Customer Rate | Measure repeat purchasing |
| High-Value Customers | Identify valuable customers |
| One-Time Customers | Identify customers with a single order |
| Repeat Customers | Identify customers with multiple orders |
| Top 10 Customer Revenue Share | Measure customer revenue concentration |

---

## Customer Performance Analysis

Customer performance was analysed using:

- Total revenue
- Total units purchased
- Total orders
- Number of products purchased
- Number of branches used
- Average order value
- Customer performance score

A customer performance score was calculated using:

- Revenue — **50%**
- Orders — **30%**
- Units — **20%**

Customers were classified into:

- High Performance
- Medium Performance
- Low Performance

The classifications use relative quartiles.

---

## Customer Segmentation

Customers were segmented based on their purchasing behaviour.

### Customer Value Segments

- **High Value** — top 25% based on revenue
- **Medium Value** — middle 50%
- **Low Value** — bottom 25%

### Order Frequency Segments

- **High Frequency** — top 25% based on order count
- **Medium Frequency** — middle 50%
- **Low Frequency** — bottom 25%

This allows customer value and purchasing frequency to be analysed separately.

---

## Repeat Customer Analysis

Customers were classified according to the number of orders:

- **One-Time Customer** — one order
- **Repeat Customer** — more than one order

Repeat Customer Rate was calculated as:

`Repeat Customers / Total Customers × 100`

Customer order frequency was also analysed to understand how frequently customers make purchases.

---

## Customer–Product Analysis

Customer purchasing behaviour was analysed at product level to identify:

- Products purchased by individual customers
- Products generating the most revenue
- Products with the highest unit demand
- Products purchased by high-value customers
- Customer–product purchasing patterns

---

## Customer Revenue Concentration

Customer revenue concentration was analysed using cumulative revenue contribution.

This helps identify whether overall revenue is distributed across many customers or concentrated among a smaller number of customers.

The revenue contribution of the top 10 customers was also calculated.

---

## Customer Type & Industry Analysis

Sales performance was compared across:

- Customer types
- Industry segments
- Regions
- Sales channels

The analysis considers:

- Total revenue
- Total units
- Total orders
- Number of customers
- Average revenue per customer

---

## Business Questions

1. Which customers generate the highest revenue?
2. Which customers make the most purchases?
3. How frequently do customers place orders?
4. What proportion of customers are repeat customers?
5. Which customer segments generate the most revenue?
6. Which customer segments have the highest purchasing frequency?
7. Are sales concentrated among a small number of customers?
8. Which products are most popular among high-value customers?
9. Which regions and sales channels generate the most revenue?
10. Which customers or segments may require further investigation?
11. Which customer segments may provide potential sales opportunities?

---

## Key Findings

*To be updated after final analysis.*

- **Total Customers:** Pending calculation
- **Total Orders:** Pending calculation
- **Total Revenue:** Pending calculation
- **Average Customer Revenue:** Pending calculation
- **Average Orders per Customer:** Pending calculation
- **Repeat Customer Rate:** Pending calculation
- **High-Value Customers:** Pending calculation
- **Top Customer:** Pending calculation
- **Top Customer Segment:** Pending calculation
- **Top Industry Segment:** Pending calculation
- **Top Region:** Pending calculation
- **Top Sales Channel:** Pending calculation
- **Top 10 Customer Revenue Share:** Pending calculation

---

## Business Insights

*To be updated after final analysis.*

Potential business insights will focus on:

- Identifying high-value customers.
- Understanding customer purchasing frequency.
- Identifying repeat purchasing patterns.
- Understanding customer revenue concentration.
- Identifying important customer and industry segments.
- Identifying products preferred by high-value customers.
- Comparing regional and sales channel performance.
- Identifying potential opportunities for customer retention and sales development.

---

## Outputs

### Analysis Files

- `customer_performance.csv`
- `customer_type_analysis.csv`
- `industry_segment_analysis.csv`
- `regional_customer_analysis.csv`
- `sales_channel_analysis.csv`
- `customer_revenue_concentration.csv`
- `customer_product_analysis.csv`
- `high_value_customer_products.csv`
- `customer_retention_summary.csv`
- `monthly_customer_activity.csv`
- `monthly_repeat_customer_analysis.csv`
- `week10_customer_sales_kpis.csv`

---

## GitHub Structure

```text
week-10/
├── notebooks/
│   └── 01_advanced_customer_sales_analysis.ipynb
├── analysis/
└── README.md
