### Entity Relational Flow

$$\text{Suppliers} \longrightarrow \text{Purchase Orders} \longrightarrow \text{Purchase Order Lines} \longrightarrow \text{Products}$$

---

# Week 02 – Data Cleaning & Integration

## Sprint Goal

Clean, integrate, and validate the project datasets, establish reliable relationships between the main tables, and prepare analysis-ready datasets for the next stage of the project.

## Objectives

- Clean the main project datasets.
- Standardise column names and data types.
- Investigate missing values and duplicates.
- Identify invalid or suspicious values.
- Confirm relationships between datasets using the available keys.
- Integrate related datasets.
- Validate the integrated datasets.
- Document data-cleaning and integration decisions.

## Completed Tasks

- [x] Data cleaning
- [x] Missing-value analysis
- [x] Duplicate analysis
- [x] Data-type validation
- [x] Invalid-value investigation
- [x] Table relationship analysis
- [x] Referential integrity checks
- [x] Sales dataset integration
- [x] Purchase dataset integration
- [x] Integrated dataset validation
- [x] Numeric and date validation
- [x] Sales total validation
- [x] Cleaning and integration documentation

## Key Findings

- The cleaned datasets were prepared for integration and further analysis.
- Relationships between Sales Orders, Sales Order Lines, Products, and Customers were investigated and validated using the available keys.
- Purchase Order Header and Purchase Order Lines were integrated using the confirmed order relationship.
- The integrated Sales dataset contains **130,402 rows and 55 columns**.
- Sales Header financial fields include `total_order_value`, `total_gst_amount`, and `grand_total`.
- Sales Line financial fields include `line_total`, `gst_amount`, and `line_grand_total`.
- Sales Header `grand_total` and Sales Lines `line_grand_total` were compared to identify potential financial inconsistencies.
- Integrated datasets were checked for unexpected row duplication following the merge process.
- Numeric fields were reviewed for unusual, negative, or zero values.
- Date fields were reviewed for missing, invalid, and incorrectly formatted values.

## Data Quality Issues

Data-quality checks were performed across the cleaned and integrated datasets, including:

- Missing values
- Duplicate records
- Missing or inconsistent keys
- Invalid numeric values
- Invalid or missing dates
- Unexpected changes in row counts after integration

Missing values were reviewed according to their business meaning rather than automatically removed. Where a missing value represents a valid business condition, it was retained for future analysis.

## Integration Results

The main integration relationships were:

$$\text{Customers} \longrightarrow \text{Sales Orders} \longrightarrow \text{Sales Order Lines} \longrightarrow \text{Products}$$

## The output report files include:

- row_validation.csv

- duplicate_validation.csv

- missing_validation.csv

- numeric_validation.csv

- date_validation.csv

These outputs provide supporting audit evidence for the Week 02 validation process.

## Remaining Issues
No major blocking issues were identified that prevent the datasets from progressing to the next stage.

Any remaining missing values or unusual records should be evaluated during domain-specific analysis rather than removed without clear business justification.

## Sprint Outcome
Week 02 successfully completed the Data Cleaning, Data Integration, and Data Validation foundation work. The datasets are now fully prepared for deeper analysis, KPI development, and business insight generation.

## Next Sprint Plan
Week 03 – Exploratory Data Analysis & Business Analytics
The upcoming sprint will focus on:

- Feature engineering where required.

- Deeper exploratory data analysis (EDA).

- Product and inventory health analysis.

- Sales and purchasing trends.

- KPI development and refinement.

- Identifying initial actionable business insights.

- Preparing cleaned analysis outputs for future dashboards.
