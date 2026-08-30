# Week 06 Sprint Kickoff & Task Sync Notes

**Date:** August 30, 2026  
**Project:** CadetX - Heavy Supplier Analytics  
**Phase:** 2 - Core Product, Inventory & Warehouse Analytics  
**Sprint Goal:** Analyze warehouse throughput, workload distribution, product variety, and operational bottlenecks.

---

## Attendees
* **Ifeanyi Njoku** (Data Analyst)
* **Saw Yu Nandar** (Data Scientist / Scrum Master)
* **Preethi.K** (Data Analyst)

---

## Task Assignments

### 1. Data Engineering Lead
**Assigned To:** Ifeanyi Njoku
* Execute `01_warehouse_efficiency.ipynb`.
* Merge `branches.csv`, `sales_orders_header.csv`, and line items.
* Compute Orders Processed, Units Processed, Revenue Handled, and Product Variety per facility.
* Calculate workload variance and average units/revenue per order.
* Export `warehouse_performance_summary.csv` to `data/processed/`.

### 2. Visualization Lead
**Assigned To:** Preethi.K
* Generate charts: Orders by warehouse, Units processed by warehouse, Revenue handled by warehouse, and Product range comparison.
* Create throughput and workload balance comparative visualizations.
* Save image assets directly into `week-06/visualisations/`.

### 3. Scrum Master & Documentation Lead
**Assigned To:** Saw Yu Nandar
* Draft operational insights report in `week-06/analysis/warehouse_efficiency_summary.md`.
* Update `week-06/README.md` with calculated KPIs, bottleneck identification, and operational recommendations.
* Manage Scrum tracking, PR reviews, and GitHub sprint logs.
