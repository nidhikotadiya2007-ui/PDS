import pandas as pd
l=[x for x in range(5)]
s=pd.Series(l)
s
s[3]
s=pd.Series(l,index=['a','b','c','d','e'])
s
s['e']
s=pd.Series(l,index=['a','b','c','d','d'])
s['d']
data={'a':1,'b':2,'c':3,'d':4}
s=pd.Series(data)
s
s=pd.Series(data,index=['a','b'])
s
s=pd.Series(data,index=['a','b','c','f'])
s
