import numpy as np
x=np.array([i for i in range(10)])
x
np.where(x%2==0,'Even','Odd')
condlist =[x<5,x>5]
Choicelist=[x**2,x**3]
np.select(condlist,choicelist,default=x)
