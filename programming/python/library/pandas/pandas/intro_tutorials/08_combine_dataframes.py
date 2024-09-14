import pandas as pd

air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)

air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]


print(air_quality_no2.head())
print()

air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",
                    parse_dates=True)

air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]

print(air_quality_pm25.head())

print()

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
print(air_quality.head())

print()
print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
print()
print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
print()
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)

air_quality = air_quality.sort_values("date.utc")
print(air_quality.head())

print()
air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
print(air_quality)

stations_coord = pd.read_csv("data/air_quality_stations.csv")
print(stations_coord.head())

print(air_quality.head())
print()
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
print(air_quality.head())

air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")
air_quality_parameters.head()
air_quality = pd.merge(air_quality, air_quality_parameters,
                       how='left', left_on='parameter', right_on='id')
print(air_quality.head())



