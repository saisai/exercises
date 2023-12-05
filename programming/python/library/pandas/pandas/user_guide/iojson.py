import pandas as pd
import numpy as np

def p(msg):
    print(df)
    print("\n")
    
df = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": ["a", "b", "c"],
        "C": pd.date_range("2016-01-01", freq="d", periods=3),
    },
    index=pd.Index(range(3), name="idx"),
)
p(df)

r = df.to_json(orient="table", date_format="iso")
p(r)

from pandas.io.json import build_table_schema
s = pd.Series(pd.date_range("2016", periods=4))

p(build_table_schema(s))



