import pandas as pd
df=pd.read_csv('HousePrices.csv')
df.head()
df.iloc[0]
df.iloc[10]
df.loc[15]
df.size
df.memory_usage()
df.head()
df['bedrooms']=df['bedrooms'].astype('int32')
df.size
df.memory_usage()
df.groupby(['city']).mean()
df.groupby(['city']).max()
df['date']=pd.to_datetime(df['date'])
df.set_index(['date'],inplace=True)
df.head()df.resample('7D').mean()
df.head()df.resample('M').mean()
df.head()df.resample('Y').mean()
df.plot()
df['price'].plot()df=(pd.read_csv('HousePrices.csv').query('city == "Seattle"').to_csv('Seattle.csv'))
df=pd.read_csv('Seattle.csv')
df.head()
