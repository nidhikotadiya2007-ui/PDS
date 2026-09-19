import numpy as np
arr=np.array([[4,3,2],[10,1,0],[5,8,24]])
arr
np.amin(arr)
np.amin(arr,axis=0)
np.amin(arr,axis=1)
np.max(arr)
np.amax(arr,axis=0)
np.amax(arr,axis=1)
np.median(arr)
np.mean(arr)
np.std(arr)
np.var(arr)
np.percentile(arr,50)
deg=np.array([0,30,45,60,90])
np.sin(deg*np.pi/180)
np.cos(deg*np.pi/180)
np.tan(deg*np.pi/180)
'''
arcsin
arccos
arctan
'''
arr=np.array([0.1,0.8,-2.2,-9.87])
np.floor(arr)
np.ceil(arr)
#python code for dot product
def dot_product(x,y):
      return sum(i*j for i,j in zip(x,y,strict=True))
dot_product([3,2,6],[1,7,-2])
