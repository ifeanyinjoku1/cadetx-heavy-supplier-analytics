# ==============================================================================
# Task: 01_data_cleaning.py
# Author / Task Owner: Fatima Malik
# Sprint: Week 02 — Data Cleaning & Integration
# Project: CadetX Heavy Supplier, Inventory & Warehouse Analytics
# ==============================================================================

import pandas as pd
import numpy as np

# 1. Load Datasets
print("--- Loading Datasets ---")
suppliers_df = pd.read_csv("data/suppliers.csv")
inventory_df = pd.read_csv("data/inventory.csv")
warehouse_df = pd.read_csv("data/warehouse.csv")

# 2. Data Inspection
def inspect_dataset(df, name):
    print(f"\n=== Dataset: {name} ===")
    print(df.info())
    print("\nMissing Values Count:")
    print(df.isnull().sum())

inspect_dataset(suppliers_df, "Suppliers")
inspect_dataset(inventory_df, "Inventory")
inspect_dataset(warehouse_df, "Warehouse")

# 3. Handle Duplicates & Missing Values
print("\n--- Cleaning Duplicates & Null Values ---")
suppliers_df = suppliers_df.drop_duplicates()
inventory_df = inventory_df.drop_duplicates()
warehouse_df = warehouse_df.drop_duplicates()

if 'stock_quantity' in inventory_df.columns:
    inventory_df['stock_quantity'] = inventory_df['stock_quantity'].fillna(0)

if 'unit_cost' in inventory_df.columns:
    inventory_df['unit_cost'] = inventory_df['unit_cost'].fillna(inventory_df['unit_cost'].median())

# 4. Standardize Data Types & Formats
print("\n--- Formatting Fields & Data Types ---")
for df in [suppliers_df, inventory_df, warehouse_df]:
    for col in ['supplier_id', 'item_id', 'warehouse_id']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

if 'last_restock_date' in inventory_df.columns:
    inventory_df['last_restock_date'] = pd.to_datetime(inventory_df['last_restock_date'], errors='coerce')

if 'supplier_name' in suppliers_df.columns:
    suppliers_df['supplier_name'] = suppliers_df['supplier_name'].str.strip().str.title()

# 5. Outlier & Integrity Adjustments
print("\n--- Running Data Integrity Checks ---")
if 'stock_quantity' in inventory_df.columns:
    inventory_df['stock_quantity'] = inventory_df['stock_quantity'].apply(lambda x: max(0, x))

if 'unit_cost' in inventory_df.columns:
    inventory_df['unit_cost'] = inventory_df['unit_cost'].apply(lambda x: abs(x))

# 6. Export Cleaned Datasets
print("\n--- Exporting Cleaned Datasets ---")
suppliers_df.to_csv("data/cleaned_suppliers.csv", index=False)
inventory_df.to_csv("data/cleaned_inventory.csv", index=False)
warehouse_df.to_csv("data/cleaned_warehouse.csv", index=False)

print("\nData cleaning pipeline executed successfully by Fatima.")
