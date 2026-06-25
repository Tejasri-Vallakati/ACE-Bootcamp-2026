import pandas as pd
fn="/workspaces/ACE-Bootcamp-2026/Day7/archive/WorldCupMatches.csv"
df=pd.read_csv(fn)
print(df.head(10))
print(df.shape)
print(df.tail(10))
print(df.info())
df.iloc[1]
print(df.head())