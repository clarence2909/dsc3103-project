# Data Source Classification

The café sales dataset is **structured data** because it is arranged in a table with a consistent set of named columns, and each row represents one transaction. Although some values are missing or suspicious, the dataset still follows a fixed row-and-column structure.

## Variables

- **Transaction ID:** A unique identifier for each sales transaction.
- **Item:** The café product purchased.
- **Quantity:** The number of units purchased in the transaction.
- **Price Per Unit:** The price charged for one unit of the item.
- **Total Spent:** The total amount spent in the transaction.
- **Payment Method:** The method used to pay, such as cash, credit card, or digital wallet.
- **Location:** Whether the purchase was made in-store or as takeaway.
- **Transaction Date:** The date on which the transaction occurred.

## Target and Candidate Features

The proposed **target variable** is **Total Spent**, because a useful modelling task would be to predict the total value of a transaction.

Candidate **features** are **Item**, **Quantity**, **Price Per Unit**, **Payment Method**, **Location**, and **Transaction Date**. **Transaction ID** is an identifier rather than a meaningful predictive feature, so it would normally not be used as a feature.
