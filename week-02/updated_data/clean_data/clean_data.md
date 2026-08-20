# Week 2 – Data Cleaning

## Notebook
`01_data_cleaning.ipynb`

## Objective
Clean and standardise the project's 12 datasets to create reliable, consistent, analysis-ready data for integration and validation.

## Datasets
- Branches
- Customers
- Inventory
- Invoices
- Payments
- Products
- Purchase Orders – Header
- Purchase Orders – Lines
- Sales Orders – Header
- Sales Orders – Lines
- Stock Ledger
- Suppliers

## Data Cleaning Activities
- Loaded all raw CSV datasets using the Week 1 DataFrame naming convention.
- Standardised column names to lowercase and `snake_case`.
- Removed unnecessary spaces from text fields.
- Identified and analysed missing values.
- Identified duplicate records.
- Standardised date columns to datetime format.
- Checked numeric fields for negative and zero values.
- Identified potential primary and foreign keys such as `product_id`, `customer_id`, `supplier_id`, `order_id`, and `branch_id`.
- Generated data-quality summaries and reports.
- Exported cleaned datasets without modifying the original raw files.

## Data Quality Checks

| Check | Purpose |
|---|---|
| Column names | Ensure consistent naming |
| Missing values | Identify incomplete records |
| Duplicate rows | Identify repeated records |
| Text fields | Remove unnecessary spaces |
| Date fields | Standardise date formats |
| Numeric fields | Identify unusual values |
| IDs/Keys | Support future data integration |

## Outputs

Cleaned datasets are saved in:

`week-02-cleaned-data/`

Main outputs:

```text
branches_clean.csv
customers_clean.csv
inventory_clean.csv
invoices_clean.csv
payments_clean.csv
products_clean.csv
purchase_headers_clean.csv
purchase_lines_clean.csv
sales_headers_clean.csv
sales_lines_clean.csv
stock_ledger_clean.csv
suppliers_clean.csv
