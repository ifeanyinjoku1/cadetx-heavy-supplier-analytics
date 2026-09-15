# Week 09 — Sales Forecasting & Demand Analysis

## Phase
**Phase 3 — Advanced Analytics & Business Intelligence**

## Sprint Goal

Analyse historical sales trends and develop forecasting insights to understand future sales demand and support business planning and decision-making.

---

## Main Tasks

- Analyse historical sales trends over time.
- Analyse monthly and six-month sales patterns.
- Analyse sales growth and changes over time.
- Identify products with high and changing demand.
- Analyse product demand trends.
- Develop time-series forecasting models.
- Compare actual sales with forecasted sales.
- Evaluate forecasting model performance.
- Identify potential future demand patterns.
- Provide business insights and recommendations.

---

## Data Used

The analysis uses the integrated **`product_sales`** dataset developed during the previous Phase 2 sprints.

### Key Fields Used

- `order_date`
- `quantity`
- `line_total`
- `product_id`
- `product_name`
- `so_id`

### Data Preparation

- Converted `order_date` to datetime format.
- Converted sales quantity and revenue fields to numeric format.
- Checked missing values and duplicate records.
- Aggregated sales data by month for time-series analysis.
- Aggregated product demand into six-month periods for clearer trend comparison.

---

## Analysis Workflow

`Product Sales Data`
→ `Data Preparation`
→ `Historical Sales Analysis`
→ `Revenue Growth Analysis`
→ `Seasonality Analysis`
→ `Product Demand Analysis`
→ `Forecasting Models`
→ `Model Evaluation`
→ `Future Forecast`
→ `Business Insights`

---

## Key KPIs

- Total Historical Revenue
- Average Monthly Revenue
- Monthly Revenue Growth
- Peak Sales Month
- Lowest Sales Month
- Total Units Sold
- Top Products by Demand
- Forecasted Revenue
- Forecast Horizon
- Forecast Error
- Best Forecasting Model

---

## Historical Sales Analysis

Historical sales were analysed to identify:

- Revenue trends over time
- Changes in sales volume
- Monthly revenue growth
- Seasonal patterns
- Peak and low sales periods
- Changes in product demand

---

## Product Demand Analysis

Product demand was analysed using the `quantity` field.

The five products with the highest total unit sales were selected for detailed demand trend analysis.

To improve visual clarity, product demand was aggregated into **six-month periods**:

- H1 — January to June
- H2 — July to December

This allows demand patterns to be compared across products without excessive monthly fluctuations.

---

## Forecasting Models

The following forecasting approaches were evaluated:

### 1. Naive Forecast

Uses the previous observed value as the forecast for the next period.

### 2. Exponential Smoothing

Used to capture level, trend and seasonal patterns in historical revenue.

### 3. ARIMA

An autoregressive integrated moving-average model was applied to historical monthly revenue.

---

## Model Evaluation

Forecasting models were evaluated using:

- **MAE — Mean Absolute Error**
- **RMSE — Root Mean Squared Error**

Lower MAE and RMSE values indicate better forecasting performance.

The best-performing model was selected based on the lowest validation MAE.

---

## Visualizations

The analysis includes:

- Monthly revenue trend
- Monthly revenue growth trend
- Sales seasonality analysis
- Top product demand trends
- Actual vs forecasted revenue
- Forecast comparison by model
- Future revenue forecast

### Product Demand Visualization

A line chart / six-month trend analysis is used to compare demand for the top five products over time.

---

## Business Questions

1. How have sales changed over time?
2. Are there identifiable seasonal sales patterns?
3. Which months have the highest and lowest revenue?
4. Is overall sales performance increasing or decreasing?
5. Which products have the strongest demand?
6. Which products show significant changes in demand?
7. What is the expected future sales demand?
8. Which forecasting model performs best?
9. How accurate are the forecasts?
10. What future sales patterns may require business attention?

---

## Key Findings

*To be updated after final analysis.*

- Overall historical revenue trend: **Pending**
- Peak sales period: **Pending**
- Lowest sales period: **Pending**
- Monthly growth pattern: **Pending**
- Top-demand products: **Pending**
- Strongest product demand trend: **Pending**
- Best forecasting model: **Pending**
- Forecasted revenue: **Pending**

---

## Business Insights

*To be updated after final analysis.*

Potential business insights will focus on:

- Identifying periods of increasing or declining sales.
- Understanding seasonal demand patterns.
- Identifying products with consistently high demand.
- Identifying products with changing or unstable demand.
- Supporting inventory and procurement planning.
- Supporting future sales and resource planning.
- Using forecasts to support data-driven business decisions.

---

## Outputs

### Analysis Files

- `monthly_sales_analysis.csv`
- `product_demand_analysis.csv`
- `forecast_model_comparison.csv`
- `future_sales_forecast.csv`
- `week9_sales_forecasting_kpis.csv`

---

## GitHub Structure

```text
week-09/
├── notebooks/
│   └── 01_sales_forecasting.ipynb
├── analysis/
└── README.md
