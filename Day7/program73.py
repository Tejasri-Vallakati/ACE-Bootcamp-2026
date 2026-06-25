import pandas as pd
fn="/workspaces/ACE-Bootcamp-2026/Day7/archive (1)/used_car_price_prediction_1M.csv"
df=pd.read_csv(fn)
print(df.head(10))
print(df.shape)
print(df.tail(10))
print(df.info())
print(df.iloc[1])
print(df.head())
print(df.loc[0,'Model'])
print(df.loc[:,'Brand']=='BMW')
filt=(df['Brand']=='BMW')
df.loc[filt].sort_index(ascending=False).head()