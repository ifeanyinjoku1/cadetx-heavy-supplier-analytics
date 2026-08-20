# Week 2 – Data Validation

**Notebook:** `03_data_validation.ipynb`

## Data Validation Summary

The Week 2 data validation process focused on checking the quality and reliability of the cleaned and integrated datasets before further analysis.

The validation covered:

- Row counts and dataset dimensions
- Duplicate records
- Missing values
- Primary and foreign keys
- Referential integrity
- Numeric and financial values
- Date fields
- Sales integration results
- Sales Header and Sales Lines totals

The Sales Header `grand_total` was compared with the Sales Lines `line_grand_total` to identify potential financial inconsistencies. The integrated Sales dataset was also checked to ensure that the integration process did not create unexpected duplicate Sales Line records.

Referential integrity was checked across the following relationships:

```text
Sales Orders
     ↓
Sales Order Lines
     ↓
Products

Sales Orders
     ↓
Customers
