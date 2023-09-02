import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())

print()

print(titanic["Age"].mean())

print()
print(titanic[["Age", "Fare"]].median())
print()
print(titanic[["Age", "Fare"]].describe())

print()

print(
titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

        )

print()

print(titanic[["Sex", "Age"]].groupby("Sex").mean())

print()
print(titanic.groupby("Sex").mean())
print()


print(titanic.groupby("Sex")["Age"].mean())

print()
print(
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

        )

print()
print(titanic["Pclass"].value_counts())
print()
print(titanic.groupby("Pclass")["Pclass"].count())
print()

