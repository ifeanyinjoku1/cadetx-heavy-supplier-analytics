# ============================================================
# DASHBOARD 5 — SALES FORECAST & DEMAND
# ============================================================

from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ------------------------------------------------------------
# Dashboard output folder
# ------------------------------------------------------------

dashboard_path.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Load forecast data
# ------------------------------------------------------------

forecast_file = Path("/content/future_sales_forecast.csv")

if forecast_file.exists():

    forecast_data = pd.read_csv(forecast_file)

    print("Forecast columns:", forecast_data.columns.tolist())

    # --------------------------------------------------------
    # Detect the actual columns in the Week 9 forecast file
    # --------------------------------------------------------

    date_candidates = [
        "forecast_date",
        "order_date",
        "date",
        "ds"
    ]

    revenue_candidates = [
        "forecasted_revenue",   # Actual column in your file
        "forecast_revenue",
        "forecast",
        "predicted_revenue",
        "yhat",
        "revenue"
    ]

    forecast_date_col = next(
        (
            col for col in date_candidates
            if col in forecast_data.columns
        ),
        None
    )

    forecast_value_col = next(
        (
            col for col in revenue_candidates
            if col in forecast_data.columns
        ),
        None
    )

    # --------------------------------------------------------
    # Check forecast columns
    # --------------------------------------------------------

    if forecast_date_col is None or forecast_value_col is None:

        print(
            "Forecast file found, but the required "
            "date/revenue columns were not detected."
        )

        print(
            "Available columns:",
            forecast_data.columns.tolist()
        )

    else:

        print(
            "Using forecast date column:",
            forecast_date_col
        )

        print(
            "Using forecast revenue column:",
            forecast_value_col
        )

        # ----------------------------------------------------
        # Clean forecast data
        # ----------------------------------------------------

        forecast_data[forecast_date_col] = pd.to_datetime(
            forecast_data[forecast_date_col],
            errors="coerce"
        )

        forecast_data[forecast_value_col] = pd.to_numeric(
            forecast_data[forecast_value_col],
            errors="coerce"
        )

        forecast_data = (
            forecast_data
            .dropna(
                subset=[
                    forecast_date_col,
                    forecast_value_col
                ]
            )
            .sort_values(forecast_date_col)
        )

        # ----------------------------------------------------
        # Prepare top product demand
        # ----------------------------------------------------

        if "product_demand" in globals():

            top_demand = (
                product_demand
                .nlargest(10, "total_units_sold")
                .sort_values(
                    "total_units_sold",
                    ascending=True
                )
            )

        else:

            product_demand = (
                week11_data
                .groupby(
                    ["product_id", "product_name"],
                    as_index=False
                )
                .agg(
                    total_units_sold=(
                        "quantity",
                        "sum"
                    )
                )
            )

            top_demand = (
                product_demand
                .nlargest(10, "total_units_sold")
                .sort_values(
                    "total_units_sold",
                    ascending=True
                )
            )

        # ----------------------------------------------------
        # Prepare monthly sales data
        # ----------------------------------------------------

        monthly_sales_dashboard = monthly_sales.copy()

        monthly_sales_dashboard["order_date"] = pd.to_datetime(
            monthly_sales_dashboard["order_date"],
            errors="coerce"
        )

        monthly_sales_dashboard = (
            monthly_sales_dashboard
            .dropna(subset=["order_date"])
            .sort_values("order_date")
        )

        # ----------------------------------------------------
        # Create dashboard
        # ----------------------------------------------------

        fig5 = make_subplots(
            rows=2,
            cols=2,

            subplot_titles=[
                "Historical Revenue",
                "Forecast Revenue",
                "Monthly Revenue Growth",
                "Top 10 Product Demand"
            ],

            horizontal_spacing=0.18,
            vertical_spacing=0.24,

            row_heights=[0.52, 0.48]
        )

        # ====================================================
        # 1. Historical Revenue
        # ====================================================

        fig5.add_trace(
            go.Scatter(
                x=monthly_sales_dashboard["order_date"],
                y=monthly_sales_dashboard["revenue"],
                mode="lines+markers",
                name="Historical Revenue",

                line=dict(width=2),
                marker=dict(size=5),

                hovertemplate=(
                    "<b>%{x|%b %Y}</b><br>"
                    "Revenue: £%{y:,.0f}"
                    "<extra></extra>"
                )
            ),
            row=1,
            col=1
        )

        # ====================================================
        # 2. Forecast Revenue
        # ====================================================

        fig5.add_trace(
            go.Scatter(
                x=forecast_data[forecast_date_col],
                y=forecast_data[forecast_value_col],
                mode="lines+markers",
                name="Forecast Revenue",

                line=dict(width=2),
                marker=dict(size=6),

                hovertemplate=(
                    "<b>%{x|%b %Y}</b><br>"
                    "Forecast Revenue: £%{y:,.0f}"
                    "<extra></extra>"
                )
            ),
            row=1,
            col=2
        )

        # ====================================================
        # 3. Monthly Revenue Growth
        # ====================================================

        fig5.add_trace(
            go.Scatter(
                x=monthly_sales_dashboard["order_date"],
                y=monthly_sales_dashboard["revenue_growth"],
                mode="lines+markers",
                name="Revenue Growth",

                line=dict(width=2),
                marker=dict(size=5),

                hovertemplate=(
                    "<b>%{x|%b %Y}</b><br>"
                    "Revenue Growth: %{y:.1f}%"
                    "<extra></extra>"
                )
            ),
            row=2,
            col=1
        )

        # ====================================================
        # 4. Top Product Demand
        # ====================================================

        fig5.add_trace(
            go.Bar(
                x=top_demand["total_units_sold"],
                y=top_demand["product_name"],
                orientation="h",
                name="Units Sold",

                hovertemplate=(
                    "<b>%{y}</b><br>"
                    "Units Sold: %{x:,.0f}"
                    "<extra></extra>"
                )
            ),
            row=2,
            col=2
        )

        # ====================================================
        # Dashboard Layout
        # ====================================================

        fig5.update_layout(

            title=dict(
                text="CadetX Week 11 — Sales Forecast & Demand",
                x=0.5,
                font=dict(size=28)
            ),

            height=1050,
            width=1800,

            template="plotly_white",

            showlegend=False,

            margin=dict(
                l=150,
                r=120,
                t=130,
                b=130
            )
        )

        # ====================================================
        # Axis Formatting
        # ====================================================

        # Historical Revenue
        fig5.update_xaxes(
            title_text="Date",
            automargin=True,
            row=1,
            col=1
        )

        fig5.update_yaxes(
            title_text="Revenue",
            tickformat="~s",
            automargin=True,
            row=1,
            col=1
        )

        # Forecast Revenue
        fig5.update_xaxes(
            title_text="Forecast Date",
            automargin=True,
            row=1,
            col=2
        )

        fig5.update_yaxes(
            title_text="Forecast Revenue",
            tickformat="~s",
            automargin=True,
            row=1,
            col=2
        )

        # Revenue Growth
        fig5.update_xaxes(
            title_text="Date",
            automargin=True,
            row=2,
            col=1
        )

        fig5.update_yaxes(
            title_text="Growth (%)",
            ticksuffix="%",
            automargin=True,
            row=2,
            col=1
        )

        # Product Demand
        fig5.update_xaxes(
            title_text="Units Sold",
            tickformat="~s",
            automargin=True,
            row=2,
            col=2
        )

        fig5.update_yaxes(
            title_text="",
            tickfont=dict(size=12),
            automargin=True,
            row=2,
            col=2
        )

        # ----------------------------------------------------
        # Export dashboard
        # ----------------------------------------------------

        fig5.write_html(
            dashboard_path / "05_sales_forecast_demand.html",
            include_plotlyjs="cdn"
        )

        # ----------------------------------------------------
        # Display dashboard
        # ----------------------------------------------------

        fig5.show()

else:

    print(
        "Forecast file not found at "
        "/content/future_sales_forecast.csv."
    )

    print(
        "Run the Week 9 forecasting notebook first, "
        "then rerun this Dashboard 5 cell."
    )
