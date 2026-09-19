import pandas as pd
df1=pd.read_csv('Merge1.csv')
df2=pd.read_csv('Merge2.csv')
df1
pd.merge(df1,df2,on=['date'])
pd.merge(df1,df2,on=['date'],how='outer')
pd.merge(df1,df2,on=['date'],how='left')
pd.merge(df1,df2,on=['date'],how='right')
df1.rename(columns={'date':'Date'},inplace=True)
df1
pd.merge(df1,df2,left_on=['date'],right_on=['date'])
df1.set_index(['Date'],inplace=True)
df2.set_index(['date'],inplace=True)
pd.merge(df1,df2,left_index=True,right_index=True)
pd.merge(df1,df2,left_index=True,right_index=True,suffixes=('_from_left','_from_right'))
