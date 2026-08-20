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

### Sales Validation

The Sales Header uses `so_id` as the sales order identifier and contains key financial fields:
* `total_order_value`
* `total_gst_amount`
* `grand_total`

Sales Lines contain corresponding line-level values:
* `line_total`
* `gst_amount`
* `line_grand_total`

#### Validation Process
The validation directly compares header and line-level aggregate totals:

$$\text{Sales Header } \texttt{grand\_total} \quad \longleftrightarrow \quad \text{Sales Lines } \sum \texttt{line\_grand\_total}$$

* **Reconciliation:** The difference between the two totals is calculated to identify potential financial inconsistencies.
* **Duplication Check:** The integrated Sales dataset is audited to verify that the integration process has not unexpectedly duplicated Sales Line records.

---

### Referential Integrity

Referential integrity checks are conducted across key entity relationships where keys are present:

1. **Sales Orders & Products Flow:**
   $$\text{Sales Orders} \longrightarrow \text{Sales Order Lines} \longrightarrow \text{Products}$$

2. **Sales Orders & Customers Flow:**
   $$\text{Sales Orders} \longrightarrow \text{Customers}$$

* **Unmatched Record Detection:** Unmatched records are flagged to identify whether any Sales Lines, Products, or Customers are missing corresponding parent or child records.

---

### Numeric and Date Validation

* **Numeric Validation:**
  Numeric fields are audited using minimum, maximum, mean, negative-value, and zero-value checks. This identifies unusual or invalid order quantities and financial amounts.

* **Date Validation:**
  Date fields are checked for:
  * Missing dates (null checks)
  * Invalid dates
  * Valid operational date ranges
  * Standardized `datetime` formatting
  
  *These checks ensure all datasets are reliable for time-series forecasting and KPI calculations.*

---

### Integration Validation

Integrated datasets are validated by comparing record counts before and after merging operations:

* **Row Preservation:** The original `sales_orders_lines` row count is compared against the final Integrated Sales row count to ensure no unexpected duplication occurred during joins.
* **Audit Checklist:**
  * Merge results & join integrity
  * Matched vs. unmatched record splits
  * Row-count preservation
  * Duplicate record detection
  * Key consistency across joined tables
  * Reconciled financial totals

---

### Validation Outputs

All generated validation reports are saved in the directory:
```text
week-02-validation/
