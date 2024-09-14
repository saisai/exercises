import pandas as pd

# Data
data = [['Oceanside', 'Puerto Rico', '2023-05-01', '2023-07-31'],
        ['Lakeside', 'Michigan', '2023-06-01', '2023-07-31'],
        ['Mountaintop', 'Colorado', '2023-04-01', '2023-07-31'],
        ['Desert', 'Arizona', '2023-05-01', '2023-08-30'],
        ['Countryside', 'Tennessee', '2023-02-01', '2023-03-31']]

# Create pandas DataFrame
df = pd.DataFrame(data, columns=['Hotel Name', 'Location', 'Availability Start Date', 'Availability End Date'])

# Create columns with date format
df['Start_Date']= pd.to_datetime(df['Availability Start Date'], dayfirst=False)
df['End_Date']= pd.to_datetime(df['Availability End Date'], dayfirst=False)

# Create time series
#df = (pd.concat([pd.DataFrame(pd.date_range(r.Start_Date, r.End_Date, freq="MS"))
#               for r in df.itertuples()]))


col = 'Year/Month Available'
df[col] = df.apply(lambda r: pd.date_range(r['Start_Date'], r['End_Date'], freq='MS'), axis=1)
result = df[['Hotel Name', 'Location', col]].explode(col)

print(result)

# https://stackoverflow.com/questions/76813380/use-start-and-end-dates-to-create-time-series-dataset-with-python
