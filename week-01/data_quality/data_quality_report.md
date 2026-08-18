## Executive Summary

A comprehensive structural and statistical data quality audit was executed across all 12 relational datasets. Overall schema health is high, with low overall missingness and 0 duplicate records detected.

---

## 1. Missing Values Audit

| Dataset | Total Rows | Columns with Missing Values | Missing Count | Missing % | Impact Analysis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **branches** | 6 | None | 0 | 0.0% | Complete |
| **customers** | 500 | None | 0 | 0.0% | Complete |
| **inventory** | 180 | None | 0 | 0.0% | Complete |
| **invoices** | 18,033 | None | 0 | 0.0% | Complete |
| **payments** | 19,257 | None | 0 | 0.0% | Complete |
| **products** | 30 | None | 0 | 0.0% | Complete |
| **purchase_headers** | 24,000 | `received_date` | 2,370 | 9.88% | Expected missingness (represents pending/unfulfilled purchase orders) |
| **purchase_lines** | 155,495 | None | 0 | 0.0% | Complete |
| **sales_headers** | 20,000 | None | 0 | 0.0% | Complete |
| **sales_lines** | 130,402 | None | 0 | 0.0% | Complete |
| **stock_ledger** | 237,230 | None | 0 | 0.0% | Complete |
| **suppliers** | 8 | None | 0 | 0.0% | Complete |

---

## 2. Duplicate Record Verification

Every table was evaluated for full row duplication:
* **Result:** **0 duplicate rows** found across all 12 datasets.

---

## 3. Anomaly & Boundary Integrity Checks

1. **Negative Value Checks:**
   * `unit_cost` in Products: **0** negative values found.
   * `quantity` in Sales Lines: **0** negative values found.
   * `unit_price` in Sales Lines: **0** negative values found.
2. **Data Type Anomalies:**
   * All date fields (`order_date`, `delivery_date`, `invoice_date`, `received_date`) are currently parsed as `object` (string) data types and must be cast to `datetime64` in Week 2.
