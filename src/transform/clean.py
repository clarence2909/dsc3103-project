import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.validate import rules

raw_path = PROJECT_ROOT / "data" / "raw" / "prices.csv"
clean_path = PROJECT_ROOT / "data" / "processed" / "prices_clean.parquet"


def clean_data(path=raw_path):
    df = pd.read_csv(path)
    decisions = []

    # 1. Negative prices -> reject
    bad_price = rules.rule_positive_price(df)
    if len(bad_price) > 0:
        decisions.append({
            "rule": "rule_positive_price",
            "action": "reject",
            "rows_affected": len(bad_price)
        })
    df = df.drop(bad_price.index)

    # 2. Duplicate rows -> reject the extra copies
    exact_dupes = df[df.duplicated(keep=False)].copy()
    if len(exact_dupes) > 0:
        decisions.append({
            "rule": "rule_duplicate_rows",
            "action": "deduplicate",
            "rows_affected": len(exact_dupes)
        })
    df = df.drop_duplicates(keep="first").copy()

    # 3. Duplicate ids -> reject rows with clashing ids
    bad_ids = rules.rule_duplicate_ids(df)
    if len(bad_ids) > 0:
        decisions.append({
            "rule": "rule_duplicate_ids",
            "action": "reject",
            "rows_affected": len(bad_ids)
        })
    df = df.drop(bad_ids.index)

    # 4. Invalid dates -> reject
    bad_dates = rules.rule_valid_date(df)
    if len(bad_dates) > 0:
        decisions.append({
            "rule": "rule_valid_date",
            "action": "reject",
            "rows_affected": len(bad_dates)
        })
    df = df.drop(bad_dates.index)

    # 5. Missing market -> impute with "Unknown"
    missing_market = df[df["market"].isna()].copy()
    if len(missing_market) > 0:
        decisions.append({
            "rule": "rule_missing_market",
            "action": "impute",
            "rows_affected": len(missing_market)
        })
    df["market"] = df["market"].fillna("Unknown")

    # 6. Inconsistent commodity casing -> normalize
    df["commodity"] = df["commodity"].str.lower().str.capitalize()
    decisions.append({
        "rule": "commodity_casing",
        "action": "normalize",
        "rows_affected": len(df)
    })

    df.to_parquet(clean_path, index=False)
    decisions.append({
        "rule": "save_clean_data",
        "action": "save",
        "rows_affected": len(df)
    })

    return df, decisions


def save_clean_data(df, output_path=clean_path):
    df.to_parquet(output_path, index=False)
    print(f"Saved cleaned data to {output_path} ({len(df)} rows)")


if __name__ == "__main__":
    clean_df, decisions = clean_data()
    save_clean_data(clean_df)
    print(f"\nTotal decisions logged: {len(decisions)}")
    for d in decisions:
        print(f"  {d['rule']}: {d['action']} — {d['rows_affected']} rows")