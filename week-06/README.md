# Week 06: Warehouse Operations & Efficiency

## Phase
**Phase 2 — Core Product, Inventory & Warehouse Analytics**

## Sprint Goal
Analyse warehouse operations, throughput, workload, and product distribution to identify efficiency issues and potential operational bottlenecks.

---

## Objectives

- Analyse warehouse/branch operational performance
- Measure order and unit throughput
- Compare revenue handled across warehouses
- Analyse product distribution across warehouses
- Evaluate delivery performance
- Identify workload imbalances and potential bottlenecks
- Create warehouse performance KPIs and visualisations

---

## Data Used

The analysis uses the integrated `product_sales` dataset.

Key fields used include:

- `branch_id`
- `so_id`
- `product_id`
- `product_name`
- `customer_id`
- `quantity`
- `line_total`
- `order_date`
- `delivery_date`
- `order_status`
- `sales_channel`

> **Note:** `branch_id` is used as the operational warehouse/branch identifier because a separate warehouse capacity field was not available in the analysed dataset.

---

## Analysis Workflow

`Product Sales Data`
→ `Data Preparation`
→ `Warehouse Performance`
→ `Throughput Analysis`
→ `Product–Warehouse Analysis`
→ `Delivery Performance`
→ `Workload Classification`
→ `Bottleneck Identification`
→ `Business Insights`

---

## Completed Tasks

- [x] Load and validate product sales data
- [x] Check required warehouse-related fields
- [x] Handle data types and dates
- [x] Check missing values and duplicates
- [x] Calculate delivery time
- [x] Calculate warehouse-level orders
- [x] Calculate units processed
- [x] Calculate revenue handled
- [x] Calculate products handled
- [x] Calculate customers served
- [x] Calculate average order value
- [x] Calculate average units per order
- [x] Analyse warehouse throughput
- [x] Analyse product–warehouse distribution
- [x] Analyse warehouse delivery performance
- [x] Analyse order status by warehouse
- [x] Analyse sales channels by warehouse
- [x] Classify warehouse workload
- [x] Identify potential operational bottlenecks
- [x] Create warehouse performance visualisations
- [ ] Finalise key findings
- [ ] Finalise business recommendations

---

## Key KPIs

- **Total Warehouses/Branches:** *Pending calculation*
- **Total Orders Processed:** *Pending calculation*
- **Total Units Processed:** *Pending calculation*
- **Total Revenue Handled:** *Pending calculation*
- **Products Handled:** *Pending calculation*
- **Customers Served:** *Pending calculation*
- **Average Orders per Warehouse:** *Pending calculation*
- **Average Units per Warehouse:** *Pending calculation*
- **Average Delivery Time:** *Pending calculation*
- **Potential Bottleneck Warehouses:** *Pending calculation*

---

## Visualisations

The following visualisations were created:

1. **Orders by Warehouse**
   - Compares the number of orders processed by each branch.

2. **Units Processed by Warehouse**
   - Shows the volume of units handled by each branch.

3. **Revenue by Warehouse**
   - Compares revenue handled across branches.

4. **Average Delivery Time by Warehouse**
   - Shows differences in delivery performance.

5. **Warehouse Workload Comparison**
   - Compares warehouse order and unit workloads.

6. **Warehouse Performance Comparison**
   - Provides an overall comparison of warehouse operational performance.

---

## Business Questions

1. Which warehouses handle the highest number of orders?
2. Which warehouses process the most units?
3. Which warehouses generate the most revenue?
4. Which warehouses handle the widest range of products?
5. Are workloads balanced across warehouses?
6. Which warehouses have longer delivery times?
7. Which warehouses may require further operational investigation?
8. Are high-workload warehouses also experiencing slower delivery performance?

---

## Bottleneck Identification

Potential bottlenecks are identified using a combination of:

- High order workload
- High unit workload
- Above-median delivery time

A warehouse is classified as a **Potential Bottleneck** when it has a high workload and an above-median average delivery time.

> This is a relative operational flag, not a confirmed warehouse capacity constraint.

---

## Business Insights

*To be completed after reviewing the final KPI results and visualisations.*

Potential areas of discussion include:

- High-volume warehouses requiring closer operational monitoring
- Differences in workload distribution between branches
- Warehouses with comparatively longer delivery times
- Product concentration across specific warehouses
- Opportunities to investigate workload balancing

---

## Limitations

- The dataset does not contain a confirmed warehouse capacity or storage-space field.
- Therefore, true warehouse space utilisation cannot be calculated.
- `branch_id` is used as the operational warehouse/branch identifier.
- Potential bottlenecks are based on relative workload and delivery performance rather than confirmed capacity constraints.

---

## Outputs

### Analysis Files

- `warehouse_performance.csv`
- `warehouse_throughput.csv`
- `product_warehouse_analysis.csv`
- `warehouse_delivery_performance.csv`
- `week6_warehouse_kpis.csv`


---

## Notebook

**Main Notebook:**

`notebooks/01_warehouse_efficiency.ipynb`

---
