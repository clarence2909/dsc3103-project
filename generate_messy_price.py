#%%
import csv
import random
from datetime import datetime, timedelta


# %%6
random.seed(42)

## creating an empty  ##
markets = ["mukono", "bwaise", "nakasero", "kansanga", "none"]
commodities = ["maize","MAIZE","beans","BEANS"]

rows = []
base_date = datetime(2020,1,1)

for i in range(1000):
    row = {
        "id" : i if random.random() > 0.02 else i-1,
        "date" : (base_date + timedelta(days=random.randint(0, 500))).strftime("%Y-%m-%d") if random.random() > 0.03 else "2020-14-50",
        "market" : random.choice(markets),
        "commodity" : random.choice(commodities),
        "price" : random.randint (500,5000) if random.random() > 0.05 else -2000



    }

    rows.append(row)

rows += rows[20:30]
 
with open("data/raw/prices.csv", "w",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["id","date","market","commodity","price"])
    writer.writeheader()
    writer.writerows(rows)


