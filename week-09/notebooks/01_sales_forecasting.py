import numpy as np
import pandas as pd
from statsmodels.tsa.api import Holt, ExponentialSmoothing

# 1. Load Processed Sales Data
df = pd.read_csv("data/processed/sales_data.csv", parse_dates=["order_date"])

# 2. Resample to Monthly Historical Revenue
monthly_sales = (
    df.set_index("order_date")["revenue"].resample("MS").sum().reset_index()
)
monthly_sales.columns = ["date", "actual_revenue"]

# 3. Fit Holt-Winters Exponential Smoothing Model
model = ExponentialSmoothing(
    monthly_sales["actual_revenue"],
    trend="add",
    seasonal="add",
    seasonal_periods=12,
).fit()

# 4. Forecast Next 6 Months
forecast_periods = 6
forecast_values = model.forecast(forecast_periods)

# 5. Calculate Model Metrics (MAPE & RMSE)
actuals = monthly_sales["actual_revenue"].iloc[-forecast_periods:].values
preds = model.fittedvalues.iloc[-forecast_periods:].values

mape = np.mean(np.abs((actuals - preds) / actuals)) * 100
rmse = np.sqrt(np.mean((actuals - preds) ** 2))

print(f"Model MAPE: {mape:.2f}%")
print(f"Model RMSE: ${rmse:,.2f}")

# 6. Export Results
monthly_sales.to_csv("data/processed/sales_forecast_results.csv", index=False)
