import pandas as pd

mydataset = {
        'cars' : ['BMW', 'Volov', 'Ford'],
        'passings': [3, 7, 2]
        }

df = pd.DataFrame(mydataset)
print(df)

print('\n')
print(df.loc[0])
print(df.loc[0][0])
print(df.loc[0][1])
print(df.loc[[0, 2]])
