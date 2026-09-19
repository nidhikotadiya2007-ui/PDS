import pandas as pd

df = pd.read_csv('HousePrices.csv')

df.head()
pd.pivot_table(df,index = ['city','date'])

df.groupby(['city','date']).max()

import numpy as np
  
pd.pivot_table(df,index = ['city','date'],aggfunc = np.max)
pd.pivot_table(df,index = ['city','date'],aggfunc = np.mean)
