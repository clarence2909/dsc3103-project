

# %%
import pandas as pd
from src.validate.rules import rule_positive_price
df = pd.read_csv("data/raw/prices.csv")
negative_prices = rule_positive_price(df)
print(negative_prices)

# %%
import pandas as pd
from src.validate.rules import rule_duplicate_ids
df = pd.read_csv("data/raw/prices.csv")
duplicate_ids = rule_duplicate_ids(df)
print(duplicate_ids)


# %%
import pandas as pd
from src.validate.rules import rule_duplicate_rows
duplicate_rows = rule_duplicate_rows(df)
print(duplicate_rows)


# %%
import pandas as pd
from src.validate.rules import rule_valid_date
invalid_dates = rule_valid_date(df) 
print(invalid_dates)

# %%
import pandas as pd
from src.validate.rules import rule_missing_market
missing_market = rule_missing_market(df) 
print(missing_market)


# %%
from src.validate.rules import rule_known_commodity
capitalized_commodities = rule_known_commodity(df)
print(capitalized_commodities)



# %%
