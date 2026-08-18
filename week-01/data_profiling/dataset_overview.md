# Dataset Overview & Structural Summary

## Project Context
* **Project:** Heavy Supplier, Inventory & Warehouse Analytics
* **Team:** CX-2026-HSWA-19
  
---

## 1. High-Level Dataset Metrics

Below is the high-level structural overview of all 12 relational datasets analyzed during Week 1 Exploratory Data Analysis (EDA).

| Dataset | Rows | Columns | Memory Usage (MB) | Primary / Key Identifiers |
| :--- | :--- | :--- | :--- | :--- |
| **branches** | 6 | 13 | 0.00 | `branch_id` |
| **customers** | 500 | 15 | 0.29 | `customer_id` |
| **inventory** | 180 | 8 | 0.03 | (`product_id`, `branch_id`) |
| **invoices** | 18,033 | 10 | 7.28 | `invoice_id` |
| **payments** | 19,257 | 5 | 4.43 | `payment_id` |
| **products** | 30 | 23 | 0.02 | `product_id` |
| **purchase_headers** | 24,000 | 10 | 9.71 | `po_id` |
| **purchase_lines** | 155,495 | 9 | 24.76 | (`po_id`, `line_number`) |
| **sales_headers** | 20,000 | 11 | 9.19 | `so_id` |
| **sales_lines** | 130,402 | 9 | 20.77 | (`so_id`, `line_number`) |
| **stock_ledger** | 237,230 | 9 | 91.76 | `movement_id` |
| **suppliers** | 8 | 12 | 0.00 | `supplier_id` |

---

## 2. Key Transactional Financial Highlights

Derived from initial profiling of transactional line items (`sales_lines`):

* **Total Line Items Evaluated:** 130,402
* **Quantity per Order Line:** Mean = 10.49 (Min = 1, Max = 20)
* **Unit Price Range:** Min = £310.00, Median = £10,200.00, Max = £119,000.00
* **Line Total Range:** Min = £310.00, Median = £67,600.00, Max = £2,380,000.00
