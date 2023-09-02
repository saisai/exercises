
import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())

print()

ages = titanic["Age"]

print(ages.head())


print(type(titanic["Age"]))

print()

print(titanic["Age"].shape)

print()

age_sex = titanic[["Age", "Sex"]]

print(age_sex.head())

print(type(titanic[["Age", "Sex"]]))

print(titanic[["Age", "Sex"]].shape)


print()
above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())


print()

print(titanic["Age"] > 35)


print()

print(above_35.shape)

print()

class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23.head())


print()

class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23.head())

print()
age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())

print()
print(age_no_na.shape)

print()

adult_name = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_name.head())


print()
print(titanic.iloc[9:25, 2:5])

print()

titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())



