# 01 Feature Engineering Pipeline

import os
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

data_path = '../data/'

sales_df = pd.read_csv(os.path.join(data_path, 'validated_sales.csv'))
inventory_df = pd.read_csv(os.path.join(data_path, 'validated_inventory.csv'))
products_df = pd.read_csv(os.path.join(data_path, 'validated_products.csv'))

# Convert dates & calculate fulfillment lead time
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
sales_df['delivery_date'] = pd.to_datetime(sales_df['delivery_date'])
sales_df['order_year'] = sales_df['order_date'].dt.year
sales_df['order_month'] = sales_df['order_date'].dt.month
sales_df['order_day_of_week'] = sales_df['order_date'].dt.day_name()
sales_df['order_quarter'] = sales_df['order_date'].dt.to_period('Q')
sales_df['fulfillment_lead_time_days'] = (
    sales_df['delivery_date'] - sales_df['order_date']
).dt.days

# Merge pricing details & calculate financials
sales_engineered = sales_df.merge(
    products_df[['product_id', 'unit_cost', 'unit_price']],
    on='product_id',
    how='left',
)
sales_engineered['total_cost'] = (
    sales_engineered['quantity'] * sales_engineered['unit_cost']
)
sales_engineered['total_revenue'] = (
    sales_engineered['quantity'] * sales_engineered['unit_price']
)
sales_engineered['gross_profit'] = (
    sales_engineered['total_revenue'] - sales_engineered['total_cost']
)
sales_engineered['gross_profit_margin_pct'] = np.where(
    sales_engineered['total_revenue'] > 0,
    (sales_engineered['gross_profit'] / sales_engineered['total_revenue'])
    * 100,
    0,
)

# Aggregate turnover & inventory ratios
product_sales = (
    sales_engineered.groupby('product_id')['quantity'].sum().reset_index()
)
product_sales.rename(columns={'quantity': 'total_units_sold'}, inplace=True)
inventory_engineered = inventory_df.merge(
    product_sales, on='product_id', how='left'
).fillna({'total_units_sold': 0})

inventory_engineered['inventory_turnover_ratio'] = np.where(
    inventory_engineered['current_stock_level'] > 0,
    inventory_engineered['total_units_sold']
    / inventory_engineered['current_stock_level'],
    0,
)
inventory_engineered['days_of_inventory'] = np.where(
    inventory_engineered['inventory_turnover_ratio'] > 0,
    365 / inventory_engineered['inventory_turnover_ratio'],
    999,
)
inventory_engineered['stock_status'] = np.where(
    inventory_engineered['current_stock_level']
    <= inventory_engineered['reorder_point'],
    'Reorder Needed',
    'Sufficient',
)

# Save engineered datasets
output_path = '../data/engineered/'
os.makedirs(output_path, exist_ok=True)
sales_engineered.to_csv(
    os.path.join(output_path, 'engineered_sales.csv'), index=False
)
inventory_engineered.to_csv(
    os.path.join(output_path, 'engineered_inventory.csv'), index=False
)
