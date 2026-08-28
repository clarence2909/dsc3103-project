1. The `Location` column has a large number of missing values: only 6,735 of 10,000 rows are non-null.
2. The `Payment Method` column has many missing values: only 7,421 of 10,000 rows are non-null.
3. The `Total Spent` column contains the text value `ERROR`, even though it should represent a monetary amount.
4. The `Transaction Date` column contains the unexpected category `UNKNOWN`, which is not a valid date.
5. The `Item` column contains `UNKNOWN` values and missing values instead of identifiable product names.
6. The `Payment Method` column contains `UNKNOWN` and `ERROR` values, which are not valid payment methods.
7. The `Location` column contains `UNKNOWN` values in addition to missing values, although the observed valid categories appear to be `Takeaway` and `In-store`.
8. The `Quantity`, `Price Per Unit`, `Total Spent`, and `Transaction Date` columns were all loaded as strings rather than numeric or date types.
9. The `Total Spent` column has 19 unique text values, suggesting that invalid entries or inconsistent representations may be present in a field expected to contain calculated monetary totals.
