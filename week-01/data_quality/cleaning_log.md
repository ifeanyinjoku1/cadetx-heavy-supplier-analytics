# Data Quality Cleaning Log & Proposed Transformations

## Sprint: Week 1 Assessment

This log documents the required data transformations and cleaning rules identified during the Week 1 assessment to be implemented during Week 2.

---

| Issue ID | Target Dataset | Target Column | Identified Issue | Planned Action / Remediation | Target Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CL-01** | `purchase_headers` | `received_date` | 2,370 null values (9.88%) | Retain nulls for unfulfilled orders; construct a binary feature `is_delivered` flag (`1` if received, `0` if null). | Week 2 |
| **CL-02** | All Tables | `*_date` columns | Dates formatted as string `object` | Convert string dates into ISO `datetime64[ns]` timestamp objects. | Week 2 |
| **CL-03** | `sales_lines` | `line_total` | Derived field validation | Validate calculation `quantity * unit_price` matches `line_total` across all 130,402 records. | Week 2 |
| **CL-04** | `inventory` | `current_stock` | Valuation merging | Perform left join with `products.unit_cost` to establish static inventory total valuation. | Week 2 |
