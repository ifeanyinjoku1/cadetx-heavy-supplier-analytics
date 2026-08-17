# Data Sourcing & Storage Guide

## Overview
This directory holds the raw transactional CSV files provided for the **Heavy Supplier, Inventory & Warehouse Analytics** project. 

## Included Datasets

| File Name | Description | Key Entities / Primary Keys |
| :--- | :--- | :--- |
| `branches.csv` | Warehouse locations and branch profiles | `branch_id` |
| `customers.csv` | Customer master data and attributes | `customer_id` |
| `inventory_master.csv` | Current stock levels, reorder points, and storage units | `inventory_id`, `product_id`, `branch_id` |
| `invoices.csv` | Billing and financial records | `invoice_id`, `sales_order_id` |
| `payments.csv` | Payment transaction records | `payment_id`, `invoice_id` |
| `products.csv` | Product catalog, pricing, and category metadata | `product_id` |
| `purchase_orders_header.csv` | Procurement order headers | `po_header_id`, `supplier_id` |
| `purchase_orders_lines.csv` | Itemized procurement line details | `po_line_id`, `po_header_id`, `product_id` |
| `sales_orders_header.csv` | Sales transaction order headers | `sales_order_id`, `customer_id` |
| `sales_orders_lines.csv` | Itemized sales order line details | `sales_line_id`, `sales_order_id`, `product_id` |
| `stock_ledger.csv` | Detailed history of stock movements and inventory adjustments | `ledger_id`, `product_id`, `branch_id` |
| `suppliers.csv` | Supplier profile and performance attributes | `supplier_id` |

## Usage & Access Rules
* **Data Privacy & Large Files:** Do not commit modified versions of raw data directly to remote branches if file sizes exceed GitHub limits.
* **Schema Reference:** Refer to `docs/data_dictionary.md` for full field definitions, data types, and primary-foreign key linkages.
* **Local Pathing:** All scripts and notebooks reference datasets relative to this directory (`../../data/<filename>.csv`).
