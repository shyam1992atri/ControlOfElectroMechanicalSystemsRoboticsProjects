## least square method

import math 
import numpy as np

a=0.5
t=0

time=np.zeros(11)
A=np.zeros([11,2])
b=np.zeros(11) # distance
d=[0.0,1.5,6.0,11.0,20.0,30.5,44.0,60.0,78.5,99.5,123]


## Ax=b format
## b= distance vector
## A=[t,t**2]
## x=[initial velocity , acc_due_to_gravity]
## Eqn:d=u*t+0.5*t**2
## simplified Eqn:2*d=2*u*t+g*t**2
## estimated vector=[~0,~9.8].T

#A=numpy.zeros(11,2)

for i in range(11):
    time[i]=t # time vector
    A[i,0]=t*2  # time
    A[i,1]=t*t  # time squaerd vector
    t=t+a
    b[i]=d[i]*2

time=np.matrix(time)
A=np.matrix(A)
b=np.matrix(b) # distance


k=A.T

f=b.T

l=k*A

h=l.I

p=h*k

x=p*f


print('x=',x)

## Least square method

h=[[1,2],[3,4]]
v=np.linalg.inv(h)
det_val=np.linalg.det(h)
print(v,det_val)










    
