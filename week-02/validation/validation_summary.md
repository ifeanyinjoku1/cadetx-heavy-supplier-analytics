# Integrated Dataset Validation Summary — Week 02

**Project:** CadetX Heavy Supplier, Inventory & Warehouse Analytics  
**Prepared By:** Ifeanyi Njoku (Data Validation & Scrum Lead) & Jaloliddin Sayfiddinov (QA & Review)  
**Sprint Goal:** Validate the cleanliness, structural integrity, and completeness of integrated relational datasets.

---

# Week 2 – Data Validation

**Notebook:** `03_data_validation.ipynb`

The purpose of this notebook is to validate the cleaned and integrated datasets produced during Week 2. The validation process checks data completeness, uniqueness, referential integrity, numeric and date values, and the correctness of the integrated sales and purchase datasets before further analysis.

## Validation Activities

The following datasets are validated:

- Sales Order Header
- Sales Order Lines
- Integrated Sales
- Purchase Order Header
- Purchase Order Lines
- Integrated Purchases
- Products
- Customers
- Suppliers

The validation process includes:

- Checking dataset row counts and dimensions.
- Checking duplicate records.
- Checking missing values.
- Validating important IDs and potential primary keys.
- Checking referential integrity between Sales Lines and Sales Header.
- Checking referential integrity between Sales Lines and Products.
- Checking referential integrity between Sales Orders and Customers.
- Checking numeric fields for minimum, maximum, mean, negative values, and zero values.
- Checking date fields for valid date ranges and invalid dates.
- Reviewing the structure and missing values of the integrated Sales dataset.
- Comparing original Sales Lines rows with Integrated Sales rows to identify unexpected row duplication.
- Validating sales-line calculations using `unit_price × quantity`.
- Comparing Sales Header `grand_total` with Sales Lines `line_grand_total`.
- Creating an overall Week 2 validation scorecard.

## Key Validation Checks

| Check | Purpose |
|---|---|
| Row counts | Confirm expected dataset sizes |
| Duplicates | Identify repeated records |
| Missing values | Identify incomplete data |
| Primary keys | Check uniqueness and missing IDs |
| Referential integrity | Confirm relationships between tables |
| Numeric values | Identify negative, zero, and unusual values |
| Dates | Check valid date ranges and invalid dates |
| Integration rows | Detect unexpected row duplication |
| Sales totals | Compare header and line-level totals |

## Sales Validation

The Sales Header uses `so_id` as the sales order identifier and contains financial fields including:

```text
total_order_value
total_gst_amount
grand_total

Sales Lines contain corresponding line-level values such as:

line_total
gst_amount
line_grand_total

The validation compares:

Sales Header grand_total
          ↕
Sales Lines line_grand_total

The difference between the two totals is calculated to identify potential inconsistencies.

The integrated Sales dataset is also checked to ensure that the integration process has not unexpectedly duplicated Sales Line records.

Referential Integrity

The following relationships are checked where the required keys are available:

Sales Orders
     ↓
Sales Order Lines
     ↓
Products
Sales Orders
     ↓
Customers

Unmatched records are identified to determine whether any Sales Lines, Products, or Customers are missing corresponding records.

Numeric and Date Validation

Numeric fields are reviewed using minimum, maximum, mean, negative-value, and zero-value checks. This helps identify unusual or potentially invalid quantities and financial values.

Date fields are checked for:

Missing dates
Invalid dates
Valid date ranges
Correct datetime formatting

These checks help ensure that the datasets are suitable for time-based analysis and KPI calculations.

Integration Validation

The integrated datasets are checked by comparing the number of records before and after integration.

For Sales integration, the original Sales Lines row count is compared with the Integrated Sales row count to identify unexpected duplication caused by the merge.

The following are also checked:

Merge results
Matched and unmatched records
Row-count preservation
Duplicate records
Key consistency
Financial totals
Validation Outputs

Validation reports are saved in:

week-02-validation/

The generated reports include:

row_validation.csv
duplicate_validation.csv
missing_validation.csv
numeric_validation.csv
date_validation.csv

These reports provide evidence of the validation checks performed during Week 2.

