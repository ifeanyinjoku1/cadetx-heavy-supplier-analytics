# Data Quality & Profiling Report — Week 02

**Project:** CadetX Heavy Supplier, Inventory & Warehouse Analytics  
**Prepared By:** Ifeanyi Njoku (Data Validation & Scrum Lead) & Jaloliddin Sayfiddinov (QA & Review)  
**Sprint:** Week 02 — Data Cleaning & Integration  

---

## 1. Overview & Dataset Completeness
An audit across the 10 core relational tables was conducted to check for missing values, duplicate records, data type anomalies, and referential integrity.

* **Overall Completeness:** 9 out of 10 relational tables exhibit 100% data completeness with zero missing records.
* **Total Tables Audited:** 10 CSV datasets (`branches`, `suppliers`, `products`, `customers`, `inventory_master`, `sales_orders_header`, `invoices`, `payments`, `purchase_orders_header`, `purchase_orders_lines`).

---

## 2. Identified Data Quality Findings

### A. Missing Values
* **`purchase_orders_header.csv`**: Contains **2,370 null values** in the `received_date` column.
  * *Business Context / Reason:* These represent active, in-transit, or unfulfilled purchase orders where goods have been ordered from suppliers but not yet received at the warehouse facility.
  * *Resolution:* Retained nulls for open order tracking; backfilling is not required as null indicates an uncompleted delivery status.

### B. Duplicate Records
* Zero duplicate records found across primary key identifiers in all 10 datasets (`so_id`, `po_id`, `invoice_id`, `payment_id`, `customer_id`, `supplier_id`, `branch_id`, `product_id`).

### C. Data Type Validation
* Date fields across headers and transactional logs (`order_date`, `due_date`, `payment_date`, `received_date`) were standardized to ISO standard `YYYY-MM-DD` timestamp formats.
* Currency fields (`unit_cost`, `unit_price`, `total_amount`) verified as numerical floats with no non-numeric characters.

### D. Referential Integrity Checks
* Primary and foreign key relationships were verified across parent-child structures:
  * `sales_orders_header.csv` → `customers.csv` (Key: `customer_id`): **100% match, 0 orphaned records**.
  * `purchase_orders_lines.csv` → `purchase_orders_header.csv` (Key: `po_id`): **100% match, 0 orphaned records**.
  * `inventory_master.csv` → `products.csv` & `branches.csv` (Keys: `product_id`, `branch_id`): **100% match, 0 orphaned records**.

---

## 3. Summary & Quality Sign-Off
* **Validation Status:** PASSED — Dataset is fully validated and clean for relational table joins, KPI calculation, and integrated dataset creation.
* **Next Steps:** Proceed with merged table outputs for Week 3 exploratory analysis and feature engineering.
