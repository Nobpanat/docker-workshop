import sys 

import pandas as pd

df = pd.DataFrame({"day": [1, 2],"passenger": [3, 4]})
print("arguments", sys.argv)

month = int(sys.argv[1])

df['month'] = month

print("this month is", month)

print(df.head())

df.to_parquet(f"output_{month}.parquet")