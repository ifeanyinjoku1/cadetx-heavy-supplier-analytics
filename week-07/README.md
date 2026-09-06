# Week 07: Product–Warehouse Alignment & Performance Scoring

## Phase
**Phase 2 — Core Product, Inventory & Warehouse Analytics**

## Sprint Goal
Analyse product and warehouse performance together to identify high- and low-performing products, warehouse performance, product–warehouse alignment, and areas requiring further operational investigation.

---

## Main Tasks

- Analyse product performance across warehouses.
- Analyse product–warehouse sales distribution.
- Identify high-, medium-, and low-performing products.
- Calculate product performance scores.
- Calculate warehouse performance scores.
- Compare warehouse performance.
- Analyse product concentration across warehouses.
- Identify high- and low-performing warehouses.
- Identify potential product–warehouse performance patterns.

---

## Data Used

The analysis uses the integrated `product_sales` dataset.

Key fields include:

- `branch_id`
- `product_id`
- `product_name`
- `quantity`
- `line_total`
- `so_id`
- `customer_id`
- `order_date`

---

## Analysis Workflow

`Product Sales Data`
→ `Data Preparation`
→ `Product Performance`
→ `Warehouse Performance`
→ `Performance Scoring`
→ `Product–Warehouse Alignment`
→ `Performance Classification`
→ `Business Investigation`
→ `Key Findings`

---

## Key KPIs

| KPI | Purpose |
|---|---|
| Total Products Analysed | Measure product coverage |
| Total Warehouses/Branches | Measure operational locations |
| Total Units Sold | Measure product movement |
| Total Revenue | Measure business contribution |
| Average Revenue per Product | Compare product performance |
| Average Products per Warehouse | Measure product variety |
| Average Product Performance Score | Evaluate product performance |
| Average Warehouse Performance Score | Evaluate warehouse performance |
| High-Performing Products | Identify strong products |
| Low-Performing Products | Identify products requiring investigation |
| High-Performing Warehouses | Identify strong warehouses |
| Low-Performing Warehouses | Identify warehouses requiring investigation |

---

## Performance Scoring

### Product Performance Score

The product performance score combines:

- Revenue — 50%
- Units Sold — 30%
- Orders — 20%

Products are classified using relative performance thresholds:

- **High Performance** — Top 25%
- **Medium Performance** — Middle 50%
- **Low Performance** — Bottom 25%

### Warehouse Performance Score

The warehouse performance score combines:

- Revenue — 40%
- Orders — 25%
- Units Processed — 25%
- Product Variety — 10%

Warehouses are classified using relative performance thresholds:

- **High Performance** — Top 25%
- **Medium Performance** — Middle 50%
- **Low Performance** — Bottom 25%

> The performance scores are analytical scores created for this sprint to support relative comparison.

---

## Visualizations

- Top products by revenue
- Top products by units sold
- Revenue by warehouse
- Units processed by warehouse
- Warehouse performance score
- Product performance score
- Product–warehouse revenue alignment
- Product distribution across warehouses

---

## Business Questions

1. Which products generate the highest revenue?
2. Which products have the highest unit sales?
3. Which products are classified as high-performing?
4. Which products are classified as low-performing?
5. Which warehouses have the strongest overall performance?
6. Which warehouses have the lowest performance scores?
7. Which warehouses handle the strongest-performing products?
8. Which product–warehouse combinations contribute the most revenue?
9. Are some products concentrated in specific warehouses?
10. Which products or warehouses require further investigation?

---

## Key Findings

*To be completed after reviewing the final analysis results.*

Potential areas of discussion include:

- Highest-revenue products
- Highest-volume products
- High- and low-performing products
- Highest-performing warehouses
- Low-performing warehouses
- Product concentration across warehouses
- Strong product–warehouse combinations
- Areas requiring further operational investigation

---

## Business Insights

*To be completed after the final KPI results and visualisations are reviewed.*

The analysis can support decisions related to:

- Product prioritisation
- Warehouse performance monitoring
- Product distribution
- Resource allocation
- Operational investigation
- Product–warehouse alignment

---

## Limitations

- The analysis does not include warehouse capacity or storage-space utilisation because these fields were not available in the analysed dataset.
- `branch_id` is used as the operational warehouse/branch identifier.
- Performance scores are relative analytical measures and should be used for comparison rather than as absolute operational standards.
- Low-performing classifications indicate relative performance within the dataset and do not necessarily mean that a product or warehouse is operationally failing.

---

## Outputs

### Analysis Files

- `product_performance.csv`
- `warehouse_performance.csv`
- `product_warehouse_alignment.csv`
- `product_warehouse_distribution.csv`
- `week7_performance_kpis.csv`

---

## Notebook

`notebooks/01_product_warehouse_alignment.ipynb`

---

## GitHub Structure

```text
week-07/
├── notebooks/
│   └── 01_product_warehouse_alignment.ipynb
│
├── analysis/
│   ├── product_performance.csv
│   ├── warehouse_performance.csv
│   ├── product_warehouse_alignment.csv
│   ├── product_warehouse_distribution.csv
│   └── week7_performance_kpis.csv
│
│
└── README.md
