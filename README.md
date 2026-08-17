# cadetx-heavy-supplier-analytics
CadetX Virtual Work Experience - Heavy Supplier, Inventory &amp; Warehouse Analytics

# Phase 1: Data Foundation & Data Dictionary
**Project Name:** Heavy Supplier, Inventory & Warehouse Analytics  
**Phase:** Phase 1 — Data Foundation & Exploration (Weeks 1–3)  
**Prepared By:** CadetX Analytics Team  

---

## Executive Overview
This document contains the structural profiling, data quality audit, high-level business metrics, and a comprehensive data dictionary for the 10 relational tables included in the Heavy Supplier, Inventory & Warehouse dataset.

---

## 1. Dataset Overview & Structural Summary
The dataset consists of 10 relational CSV files representing end-to-end supply chain, procurement, inventory management, and customer sales activities across 6 regional warehouse branches.

| File Name | Record Count | Primary Key | Foreign Key(s) | Key Domain |
| :--- | :--- | :--- | :--- | :--- |
| `branches.csv` | 6 | `branch_id` | None | Regional Warehouse Operations |
| `suppliers.csv` | 8 | `supplier_id` | None | Vendor & Supplier Management |
| `products.csv` | 30 | `product_id` | None | Heavy Equipment & Parts Catalog |
| `customers.csv` | 500 | `customer_id` | `branch_id` | Client & B2B Profiles |
| `inventory_master.csv` | 180 | (`product_id`, `branch_id`) | `product_id`, `branch_id` | Branch Level Stock Levels |
| `sales_orders_header.csv` | 20,000 | `so_id` | `customer_id`, `branch_id` | Outbound Customer Orders |
| `invoices.csv` | 18,033 | `invoice_id` | `so_id`, `customer_id`, `branch_id` | Financial Billing Records |
| `payments.csv` | 19,257 | `payment_id` | `invoice_id` | Customer Cash Receipts |
| `purchase_orders_header.csv` | 24,000 | `po_id` | `supplier_id`, `branch_id` | Inbound Vendor Procurement |
| `purchase_orders_lines.csv` | 155,495 | (`po_id`, `line_number`) | `po_id`, `product_id` | Itemized Procurement Details |

---

## 2. Data Quality & Profiling Report
* **Completeness:** 9 out of 10 tables exhibit 100% data completeness with zero missing entries.
* **Identified Null Values:** `purchase_orders_header.csv` contains 2,370 null entries in `received_date` (unfulfilled/in-transit orders).
* **Referential Integrity:** Primary and foreign key relationships are strictly aligned across order headers, line items, customers, and inventory master tables.

---

## 3. High-Level Portfolio Metrics (Baseline KPIs)
* **Total Warehouse Branches:** 6 Active regional distribution hubs
* **Total Supplier Base:** 8 Primary heavy equipment vendors
* **Active Product Catalog:** 30 Unique SKUs / heavy machinery models
* **Total Customer Base:** 500 B2B client profiles across industrial sectors
* **Total Sales Orders Executed:** 20,000 Historical customer purchases
* **Total Sales Revenue:** $32,424,754,555.80 Cumulative customer order value
* **Total Purchase Orders Placed:** 24,000 Procurement orders submitted to vendors
* **Total Procurement Spend:** $441,686,308,240.89 Cumulative purchasing costs
* **Current On-Hand Stock:** 19,303,266 units Total combined inventory across all 6 warehouses

---

## 4. Comprehensive Data Dictionary

### 4.1 Branches (`branches.csv`)
* **branch_id** (String) - Primary Key: Unique identifier for warehouse branch
* **branch_name** (String): Official name of regional branch
* **city / state / region** (String): Geographic location details
* **warehouse_type** (String): Operational category of warehouse
* **warehouse_capacity** (Integer): Maximum unit storage capacity
* **service_center_available** (Boolean): Indicates whether repair services exist on-site
* **manager_id** (String): Unique code for branch manager
* **total_employees** (Integer): Staff headcount at location
* **avg_monthly_revenue** (Float): Average monthly earnings generated
* **monthly_operational_cost** (Float): Monthly fixed and variable operating expenses
* **market_demand_index** (Float): Local market demand index rating

### 4.2 Suppliers (`suppliers.csv`)
* **supplier_id** (String) - Primary Key: Unique vendor identification code
* **supplier_name** (String): Business name of supplier
* **supplier_type** (String): Classification of supplier
* **product_category** (String): Primary product domain supplied
* **city / province / region / pincode** (String): Location/Origin zone details
* **lead_time_days** (Integer): Average days required to fulfill orders
* **reliability_score** (Float): Vendor performance and delivery reliability score
* **import_duty_rate** (Float): Customs import duty tax percentage
* **china_tax_id** (String): Tax registration identifier for international vendors

### 4.3 Products (`products.csv`)
* **product_id** (String) - Primary Key: Unique SKU ID
* **product_name / category / machine_type / brand** (String): Product identification and classification
* **unit_cost / unit_price** (Float): Acquisition cost and selling price per unit
* **margin_percentage / gst_rate** (Float): Profit margin and tax percentages
* **reorder_level / safety_stock / max_stock_level** (Integer): Stock thresholds
* **lead_time_days** (Integer): Expected procurement lead time
* **criticality_level / usage_frequency** (String): Priority and demand velocity ratings

### 4.4 Customers (`customers.csv`)
* **customer_id** (String) - Primary Key: Unique customer identifier
* **branch_id** (String) - Foreign Key: Assigned servicing warehouse branch
* **customer_type / industry_segment** (String): Business segment and vertical
* **credit_limit / current_balance** (Float): Financial standing and balance
* **payment_terms** (String): Credit terms (e.g., Net 30, Net 60)

### 4.5 Inventory Master (`inventory_master.csv`)
* **product_id / branch_id** (String) - Foreign Keys: Product and branch identifiers
* **opening_stock / current_stock** (Integer): Inventory counts
* **reorder_level / safety_stock / max_stock** (Integer): Threshold limits for branch
* **warehouse_bin** (String): Physical storage aisle/bin coordinate tag

---

## Sprint 1 Standup Report (Scrum Master)
* **Scrum Master:** Ifeanyi
* **Sprint Goal:** Phase 1 Completion & Submission
* **Status:** Complete & Ready for Mentor Review
