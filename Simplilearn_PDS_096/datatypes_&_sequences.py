# Numbers
a=1
b=1.0
c=-999

#string
a='1'

type(a)           

#lists
l=[]
l=list()
l=[1,2,3,4,5]
l[0]               
l[-1]              
l[2:4]             
l=[1,'string',[1,2,3]]
print(l)           
for i in l:      
    print(i)       
for i in range(len(l)):
    print(l[i])             

#tuple
t=('apple','bottle','car')
type(t)              
t[0]
len(t)
#dictionary
d={'a':1,'b':2}
d['a']
d['b']
d['c']=3
d
d.items()
d.keys()
d.values()
