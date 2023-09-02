import pandas as pd 
import multiprocessing

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    }
)

def changeDF(df):
    df['Signal'] = 0
    return(df)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        df1, df2 = pool.map(changeDF, [df1, df2])