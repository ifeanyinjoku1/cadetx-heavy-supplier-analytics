# Week 2 – Data Integration

**Notebook:** `02_data_integration.ipynb`

## Objective
Integrate the cleaned datasets from `01_data_cleaning.ipynb` by identifying confirmed relationships, joining related tables, checking data integrity, and producing analysis-ready datasets.

## Input Data
- Branches
- Customers
- Inventory
- Invoices
- Payments
- Products
- Purchase Orders – Header & Lines
- Sales Orders – Header & Lines
- Stock Ledger
- Suppliers

## Integration Tasks
- Load cleaned datasets.
- Review columns and identify common fields.
- Identify potential primary and foreign keys.
- Confirm relationships using the actual dataset structure.
- Check referential integrity before merging.
- Integrate Sales Order Header with Sales Order Lines.
- Integrate sales data with Products and Customers where supported by confirmed keys.
- Integrate Purchase Order Header with Purchase Order Lines.
- Integrate purchase data with Suppliers and Products where supported by confirmed keys.
- Check matched and unmatched records.
- Compare row counts before and after merges.
- Identify unexpected duplication.
- Export integrated datasets and supporting reports.

## Key Relationships

```text
Customers → Sales Orders → Sales Order Lines → Products

Suppliers → Purchase Orders → Purchase Order Lines → Products
