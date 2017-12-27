from numpy import *
from scipy import *
from pylab import *
from control import *
from scipy.integrate import  odeint 
from scipy.signal import lti,step
from matplotlib import pyplot as plt 

a=[[-1,2],[0,-2]]
b=[[0],[0]]

c=[1,-1]
d=0

xt=1#
xet=2#
xxt=vstack((xt,xet))

print xxt

sys_plant=ss(a,b,c,d)

l=place(matrix(a).T,matrix(c).T,) #

bk=2#
bk=array(bk)
m1=a-bk

lc=4#

lc=array(lc)
m2=a-lc

atvstack((hstack((m1,bk)),hstack((za,m2))))

print at

bt=vstack((b,zb))
ct=hstack((c,zc))

sys_plant_new=ss(a,b,c,d)

t=linspace(0,10,200)

T,yout,xout=lsim(sys_plant_new,nome,t,xxt)


