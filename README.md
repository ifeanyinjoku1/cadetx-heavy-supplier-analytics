# Heavy Supplier, Inventory & Warehouse Analytics

## Project Overview
This repository contains the deliverables for a 12-week, team-based applied work experience simulating a real-world analytics and data science department. The project transforms raw operational data into actionable, data-driven decisions across supply chain operations. Over 12 Agile sprints, the team builds analytics frameworks, BI dashboards, and predictive forecasting models.

## Business Problem & Objectives
Warehouses and supply-chain organizations handling heavy goods often rely on fragmented manual reports or intuition, leading to tied-up capital, frequent stockouts, and poor space utilization.

Our objectives:
* **Inventory Optimization:** Identify fast/slow movers and dead stock to balance inventory health.
* **Operational Efficiency:** Evaluate warehouse throughput and storage capacity utilization.
* **Supplier Performance:** Measure supplier delivery reliability, performance, and risk.
* **Predictive Capability:** Develop models for demand forecasting, stockout risk, and safety stock levels.

## Team Structure & Roles
The project operates in weekly Scrum sprints with a rotating Scrum Master role across a 4-person team:
* **Data Analyst 1:** Focuses on product performance, fast/slow-moving inventory, turnover, and stock health.
* **Data Analyst 2:** Focuses on warehouse operations, storage capacity, utilization, and throughput analytics.
* **Data Analyst 3:** Focuses on supplier performance, reliability, risk profiling, and customer analytics.
* **Data Scientist:** Focuses on demand forecasting models, stockout risk prediction, and inventory optimization algorithms.

## Core Datasets
Located in the `data/` directory[cite: 1, 2]:
* `branches.csv` | `customers.csv` | `inventory_master.csv`[cite: 1, 2]
* `invoices.csv` | `payments.csv` | `products.csv`[cite: 1, 2]
* `purchase_orders_header.csv` | `purchase_orders_lines.csv`[cite: 1, 2]
* `sales_orders_header.csv` | `sales_orders_lines.csv`[cite: 1, 2]
* `stock_ledger.csv` | `suppliers.csv`[cite: 1, 2]

## 12-Week Roadmap
* **Weeks 1–3 (Phase 1):** Foundation & Exploration — Data profiling, cleaning, data dictionary, and baseline KPIs.
* **Weeks 4–6 (Phase 2):** Core Analytics — Inventory health, fast/slow movers, turnover, space utilization, and throughput.
* **Weeks 7–9 (Phase 3):** Advanced & Predictive Analytics — Supplier risk, customer RFM segmentation, and demand forecasting.
* **Weeks 10–12 (Phase 4):** BI, Strategy & Delivery — Dashboards, anomaly detection, final business recommendations, and presentation.

## Current Sprint: Week 01 — Foundation & Exploration
* **Goal:** Establish repository structure, execute initial data profiling, conduct data quality assessments, and define table relationships.
* **Deliverables:**
  * Initial exploratory notebooks (`01_data_exploration.ipynb`, `02_data_quality.ipynb`, `03_initial_kpis.ipynb`)[cite: 1].
  * Project Data Dictionary (`docs/data_dictionary.md`)[cite: 1].
  * Data quality and profiling reports (`week-01/data_profiling/`, `week-01/data_quality/`)[cite: 1].

## Primary KPIs & Core Business Questions
* **Key KPIs:** Total Inventory Value/Quantity, Inventory Turnover, Total Revenue, On-Time In-Full (OTIF) Delivery Rate, Space Utilization Rate[cite: 1].
* **Core Questions:**
  1. Which products account for the top 80% of revenue versus dead stock tied up in capital?
  2. How efficiently are individual branch warehouses utilizing their storage capacity?
  3. Which suppliers pose operational risks due to delayed or cancelled orders?
  4. How accurately can future demand be predicted to minimize stockouts?

## Repository Structure
```text
heavy-supplier-warehouse-analytics/
├── README.md
├── data/
│   ├── README.md
│   ├── branches.csv
│   ├── customers.csv
│   └── ... (all 12 CSV files)
├── week-01/
│   ├── notebooks/
│   │   ├── 01_data_exploration.ipynb
│   │   ├── 02_data_quality.ipynb
│   │   └── 03_initial_kpis.ipynb
│   ├── data_profiling/
│   ├── data_quality/
│   ├── kpis/
│   └── README.md
├── docs/
│   └── data_dictionary.md
├── dashboards/
├── models/
└── meetings/
    └── week-01-sprint-notes.md
```[cite: 1]

## Quickstart Guide
1. **Clone repo & set up environment:**
   ```bash
   git clone [https://github.com/your-org/heavy-supplier-warehouse-analytics.git](https://github.com/your-org/heavy-supplier-warehouse-analytics.git)
   cd heavy-supplier-warehouse-analytics
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install pandas numpy matplotlib seaborn jupyter
