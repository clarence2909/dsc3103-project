import pandas as pd


def rule_positive_price(df):
    neg_prices = df[df["price"] < 0].copy()
    neg_prices["Reason"] = "Negative price"
    return neg_prices

def rule_duplicate_ids(df):
    duplicate_id = df[df["id"].duplicated(keep=False)].copy()
    duplicate_id["Reason"] = "Duplicate ID"
    return duplicate_id

def rule_duplicate_rows(df):
    duplicate_rows = df[df.duplicated(keep=False)].copy()
    duplicate_rows["Reason"] = "Duplicate row"
    return duplicate_rows


def rule_valid_date(df):
    parsed_dates = pd.to_datetime(df["date"], errors="coerce")
    invalid_dates = df[parsed_dates.isna()].copy()
    invalid_dates["Reason"] = "Invalid date"    
    return invalid_dates

def rule_missing_market(df):
    missing_market = df[df["market"]=="none"].copy()
    missing_market["Reason"] = "Missing market"
    return missing_market

def rule_known_commodity(df):
    known_commodities = ["maize", "beans"]

    capitalized_commodities_df = df[
        df["commodity"].str.lower().isin(known_commodities)
        & df["commodity"].str.isupper()
    ].copy()

    capitalized_commodities_df["Reason"] = "Capitalized commodity"

    return capitalized_commodities_df

