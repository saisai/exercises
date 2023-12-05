
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
print(s.index)
print(pd.Series(np.random.randn(5)))

d = {"b": 1, "a": 0, "c": 2}

print(pd.Series(d))

d = {"a": 0.0, "b": 1.0, "c": 2.0}

print(pd.Series(d))

d = pd.Series(d, index=["b", "c", "d", "a"])
print(d)

s = pd.Series(np.random.randn(5), name="something")
print(s.name)

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d)
print(df)

print(pd.DataFrame(d, index=["d", "b", "a"]))

print(pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"]))

print(df.index)
print(df.columns)


# https://pandas.pydata.org/docs/user_guide/dsintro.html