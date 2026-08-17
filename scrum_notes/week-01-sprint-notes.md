# Week 01 — Sprint Notes

## Sprint Details
* **Date:** 17 August 2026
* **Sprint Master:** Saw Yu Nandar *(Rotates weekly)*
* **Sprint Phase:** Phase 1 — Foundation & Exploration
* **Sprint Goal:** Establish repository structure, set up the data environment, conduct initial profiling and quality checks across all 12 datasets, and propose baseline KPIs.

## Team Members & Responsibilities
| Team Member | Project Role | Week 1 Assigned Focus |
| :--- | :--- | :--- |
| **Member 1** | Data Analyst | Data profiling, table relationships, and baseline KPI definitions (`01_data_exploration.ipynb`) |
| **Member 2** | Data Analyst | Data quality assessment, anomaly detection, and cleaning log (`02_data_quality.ipynb`) |
| **Member 3** | Data Scientist | Project Data Dictionary creation, structural validation, and preliminary feature planning (`03_initial_kpis.ipynb`) |

---

## Weekly Sprint Progress

### 1. Planning Meeting Summary
* Verified access to all 12 raw transactional CSV datasets provided by CadetX.
* Agreed on project structure standards (`data/`, `docs/`, `week-01/`, `meetings/`).
* Standardized environment setup (Python 3.x, Pandas, Jupyter, Git workflow).

### 2. Completed Tasks
- [x] Initialized Git repository and set up folder hierarchy.
- [x] Created `data/README.md` and organized raw dataset storage.
- [x] Ran exploratory notebooks (`01_data_exploration.ipynb`, `02_data_quality.ipynb`).
- [x] Built core project Data Dictionary (`docs/data_dictionary.md`).
- [x] Documented data quality findings and initial cleaning decisions (`data_quality_report.md`).
- [x] Drafted initial baseline KPI framework for Inventory, Sales, and Suppliers.

---

## Technical Discussion & Key Decisions

* **Repository Cleanliness:** Decided to store all 12 raw CSVs strictly inside the `data/` folder rather than the root directory to maintain a professional layout.
* **Date Parsing:** Identified date columns in `sales_orders_header.csv` and `invoices.csv` as string types; agreed to standardize all date fields to standard `datetime` format during data cleaning.
* **KPI Alignment:** Grouped initial metrics into four core buckets: **Inventory Health** (Turnover, Value), **Sales Performance** (Total Revenue, Quantity), **Supplier Efficiency** (Purchase Volume), and **Warehouse Operations** (Stock by Warehouse).

---

## Blockers & Risk Log
* **Issue:** GitHub commit timeouts caused by staging large CSV files at the root level.
* **Resolution:** Relocated files to `data/` and updated `.gitignore` rules where necessary.

---

## Next Steps (Sprint 2 Planning)
* Execute full data cleaning scripts based on Week 1 quality findings.
* Merge header and line-item tables (`sales_orders`, `purchase_orders`) into integrated analytical models.
* Begin deep-dive analysis into product movement (ABC/Pareto classification and fast/slow movers).
