
from io import StringIO
import sys 
import pandas as pd
import numpy as np 

def p(msg):
    print(msg)

data = "col1,col2,col3\na,b,1\na,b,2\nc,d,3"

result = pd.read_csv(StringIO(data))
print(result)

r2 = pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ["COL1", "COL3"])
print(r2)

r3 = pd.read_csv(StringIO(data), skiprows=lambda x: x % 2 != 0)
print(r3)

data = "a,b,c,d\n1,2,3,4\n5,6,7,8\n9,10,11"

print(data)


df = pd.read_csv(StringIO(data), dtype=object)
print(df)
print()
print(df["a"][0])

df = pd.read_csv(StringIO(data), dtype={"b": object, "c": np.float64, "d": "Int64"})
print(df.dtypes)

print()

data = "col_1\n1\n2\n'A'\n4.22"

df = pd.read_csv(StringIO(data), converters={"col_1": str})
print(df)

print()
print(df["col_1"].apply(type).value_counts())

print()
df2 = pd.read_csv(StringIO(data))

df2["col_1"] = pd.to_numeric(df2["col_1"], errors="coerce")
print(df2)

p(df2["col_1"].apply(type).value_counts())

col_1 = list(range(500000)) + ["a", "b"] + list(range(500000))

df = pd.DataFrame({"col_1": col_1})
p(df)

#df.to_csv("foo.csv")
mixed_df = pd.read_csv("foo.csv")

p(mixed_df["col_1"].apply(type).value_counts())

p(mixed_df["col_1"].dtype)

# data = """a,b,c,d,e,f,g,h,i,j
# 1,2.5,True,a,,,,,12-31-2019,
# 3,4.5,False,b,6,7.5,True,a,12-31-2019,
# """

# df = pd.read_csv(StringIO(data), dtype_backend="numpy_nullable", parse_dates=["i"])
# p(df)

data = "col1,col2,col3\na,b,1\na,b,2\nc,d,3"

p(pd.read_csv(StringIO(data)))

p("\n")
p(pd.read_csv(StringIO(data)).dtypes)

p(pd.read_csv(StringIO(data), dtype="category").dtypes)

p(pd.read_csv(StringIO(data), dtype={"col1": "category"}).dtypes)

from pandas.api.types import CategoricalDtype
dtype = CategoricalDtype(["d", "c", "b", "a"], ordered=True)

p(pd.read_csv(StringIO(data), dtype={"col_1": dtype}).dtypes)

from io import BytesIO
data = b"word,length\n" b"Tr\xc3\xa4umen,7\n" b"Gr\xc3\xbc\xc3\x9fe,5"

data = data.decode("utf-8").encode("latin-1")

df = pd.read_csv(BytesIO(data), encoding="latin-1")

p(df)

with open("bar.csv", mode="w") as f:
    f.write("date,A,B,C\n20090101,a,1,2\n20090102,b,3,4\n20090103,c,4,5")
    
df = pd.read_csv("bar.csv", index_col=0, parse_dates=True)
p(df)


data = (
    "KORD,19990127, 19:00:00, 18:56:00, 0.8100\n"
    "KORD,19990127, 20:00:00, 19:56:00, 0.0100\n"
    "KORD,19990127, 21:00:00, 20:56:00, -0.5900\n"
    "KORD,19990127, 21:00:00, 21:18:00, -0.9900\n"
    "KORD,19990127, 22:00:00, 21:56:00, -0.5900\n"
    "KORD,19990127, 23:00:00, 22:56:00, -0.5900"
)

with open("tmp.csv", "w") as fh:
    fh.write(data)

df = pd.read_csv("tmp.csv", header=None, parse_dates=[[1, 2], [1, 3]])

p(df)

df = pd.read_csv(
    "tmp.csv", header=None, parse_dates=[[1, 2], [1, 3]], keep_date_col=True
)

p(df)

df = pd.DataFrame(np.random.randn(10, 4))

df.to_csv("tmp2.csv", sep="|")

table = pd.read_csv("tmp2.csv", sep="|")

p(table)

with pd.read_csv("tmp.csv", sep="|", chunksize=4) as reader:
    reader
    for chunk in reader:
        print(chunk)

p("\n")
# headers = {"User-Agent": "pandas"}
# df = pd.read_csv(
#     "https://download.bls.gov/pub/time.series/cu/cu.item",
#     sep="\t",
#     storage_options=headers
# )
# p(df)