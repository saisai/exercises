import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())
print()

air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)

print(air_quality)
print()

print(titanic.sort_values(by="Age").head())
print()

print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())
print()

no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)

print()

no2_subset.pivot(columns="location", values="value")
print(no2.head())

print()
no2.pivot(columns="location", values="value").plot()
print()
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)

print()
air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
)

print()
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

print(no2_pivoted.head())

print()
no_2 = no2_pivoted.melt(id_vars="date.utc")

print(no_2.head())
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
print(no_2.head())


