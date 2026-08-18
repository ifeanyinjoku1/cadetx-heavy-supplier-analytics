# Entity & Table Relationships Diagram

This document outlines the core relational links across the 12 datasets in the Heavy Supplier, Inventory & Warehouse Analytics platform.

---

## Relational Flow Map

```text
               +-------------------+
               |     SUPPLIERS     |
               +---------+---------+
                         |
                         | (1 : N)
                         v
           +-------------+-------------+
           |  PURCHASE_ORDERS_HEADER   |
           +-------------+-------------+
                         |
                         | (1 : N)
                         v
           +-------------+-------------+
           |    PURCHASE_ORDERS_LINES  |
           +-------------+-------------+
                         |
                         | (N : 1)
                         v
  +----------------------+----------------------+
  |                      |                      |
  v                      v                      v
+---+---+              +---+---+              +---+---+
|BRANCHES|------------>|PRODUCTS|<------------|CUSTOMERS|
+---+---+              +---+---+              +---+---+
  |                      ^                      |
  |                      |                      |
  | (1 : N)              | (N : 1)              | (1 : N)
  v                      |                      v
+---+--------------------+-----+              +---+--------------------+
|          INVENTORY           |              |   SALES_ORDERS_HEADER   |
+------------------------------+              +-----------+------------+
                                                          |
                                                          | (1 : N)
                                                          v
                                              +-----------+------------+
                                              |    SALES_ORDERS_LINES  |
                                              +-----------+------------+
                                                          |
                                                          | (1 : 1)
                                                          v
                                              +-----------+------------+
                                              |        INVOICES        |
                                              +-----------+------------+
                                                          |
                                                          | (1 : N)
                                                          v
                                              +-----------+------------+
                                              |        PAYMENTS        |
                                              +------------------------+
