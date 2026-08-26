# Issues Observed

- `Location` has only 6,735 non-null values out of 10,000, meaning 3,265 values are missing.
- `Payment Method` has only 7,421 non-null values out of 10,000, meaning 2,579 values are missing.
- The first five rows contain `UNKNOWN` values in both `Payment Method` and `Location`, suggesting that placeholders are being used in addition to null values.
- `Transaction Date` has 159 missing values, and `UNKNOWN` is also its most frequent displayed value, appearing 159 times.
- `Item` has 333 missing values.
- `Price Per Unit` has 179 missing values, even though it is needed to calculate transaction value.
- `Total Spent` has 173 missing values, even though it is the proposed target variable.
- `Quantity` has 138 missing values.
- `Quantity`, `Price Per Unit`, and `Total Spent` were loaded as text rather than numeric data types.
- `Transaction Date` was loaded as text rather than as a date data type.
