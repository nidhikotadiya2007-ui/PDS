import pandas as pd
df=pd.read_csv('HousePrices.csv')
df.head()
df.columns
df.set_index(['date'],inplace=True)
df.head()
df.reset_index(inplace=True)
df=pd.read_csv('HousePrices.csv',index_col=['date'])
df.head()
df.reset_index(inplace=True)
df.set_index(['date','statezip'],inplace=True)
df.head()
