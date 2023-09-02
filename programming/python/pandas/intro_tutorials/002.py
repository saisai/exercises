import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic)


print(titanic.head(8))

print()

print(titanic.dtypes)


#titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

print(titanic.head())

print()
print(titanic.info())


