# pandas_investigation.py

import pandas as pd

# pandas creates a dataframe object
sales_records = pd.read_json("https://api.acodingtutor.com/sales_records")

print (sales_records.head())

pt = pd.pivot_table(sales_records, values="Quantity", index="Product", columns="Colour", aggfunc="sum")
pt.fillna(0, inplace=True)
pt["Total"] = pt.sum(axis=1)

print (pt)
totals_row = pt.sum(axis=0).to_frame().T
totals_row.index = ["Total"]
print (totals_row)

print ("*" * 50)
pt_with_totals = pd.concat([pt, totals_row])
print (pt_with_totals)


