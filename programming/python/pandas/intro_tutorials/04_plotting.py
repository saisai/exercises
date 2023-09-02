import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality.head())
print()

print(air_quality.plot())

print()

print(air_quality["station_paris"].plot())
print()
print(air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5))

print([method_name for method_name in dir(air_quality.plot)
      if not method_name.startswith("_")])
