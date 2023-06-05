
import pandas as pd
import numpy as np

index = pd.date_range("1/1/2023", periods=8)
print(index)

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
print(df)

long_series = pd.Series(np.random.randn(1000))
print(long_series.head())
print(long_series.tail(3))

print(df[:2])

df.columns = [x.lower() for x in df.columns]

print(df)

import statsmodels.formula.api as sm

bb = pd.read_csv("data/baseball.csv", index_col="id")

print(
    bb.query("h > 0")
    .assign(ln_h=lambda df: np.log(df.h))
    .pipe((sm.ols, "data"), "hr ~ ln_h + year + g + C(lg)")
    .fit()
    .summary()
)

print("\n")

df = pd.DataFrame(
    {"col1": np.random.randn(3), "col2": np.random.randn(3)}, index=["a", "b", "c"]
)

for col in df:
    print(col)
    
df = pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})

for index, row in df.iterrows():
    row["a"] = 10
    print(row)
    
for label, ser in df.items():
    print(label)
    print(ser)
    
print("\n")

for row_index, row in df.iterrows():
    print(row_index, row, sep="\n")
    
def subdtypes(dtype):
    subs = dtype.__subclasses__()
    if not subs:
        return dtype
    return [dtype, [subdtypes(dt) for dt in subs]]

print(subdtypes(np.generic))


https://pandas.pydata.org/docs/user_guide/basics.html