-pd.read_csv : csv
-pd.to_csv : csv
-np.genfromtxt : csv
-np.loadfromtxt : csv
-np.save : npy
-np.load : npy

#Let's cover the following methods in pandas.
1. writing json
2.Reading json
3. Writing excel
4. Reading excet
5. writing gzip files
6. Reading gzip files

import pandas as pd
df=pd.read_csv('Sample_File.csv')
df.head()
df.to_json('Sample_File_json.json')
df=pd.to_json('Sample_File_json.json')
df
df.to_excel('Sample_File_Excel.xls',index=False)
df=pd.read_excel('SampleExcelFile.xls')
df
df.to_csv('SampleFilegzip.gz',compression='gzip',index=False)
df=pd.read_csv('SampleFilegzip.gz')
df
