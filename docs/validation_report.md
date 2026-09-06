# Validation Report

The raw file `data/raw/prices.csv` contained 1,010 rows. Each of the six rules in `src/validate/rules.py` was run before cleaning.

| Check | Rows found | What `clean.py` does |
|---|---:|---|
| Negative prices | 53 | Remove these rows. Prices cannot be negative. |
| Exact duplicate rows | 20 | Remove duplicate copies and keep the first row. |
| Duplicate IDs | 54 | Remove rows with duplicate IDs. |
| Invalid dates | 30 | Remove rows with dates that cannot be read. |
| Missing markets | 194 | The check finds the text `none`. The cleaner only fills blank values, so no market values were filled and `none` remains. |
| Inconsistent commodity names | 503 | Change names such as `MAIZE` and `BEANS` to `Maize` and `Beans`. |

