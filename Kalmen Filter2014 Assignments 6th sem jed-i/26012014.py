#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt
from control import *


# THIS IS THE ORIGINAL PROGRAM. DO NOT CHANGE ANYTHING    ctms.control

m2=1
A=([-1,2],[0,-2])
B=([0],[0])
C=[1,-1]
D=0
#control_matrix=[B,A*B]
#ran=rank(control_matrix)
#print ran
p1=-1
p2=-1

k=place(A,B,[p1,p2])
sys_plant=ss(A-m2*k,B,C,D)
w,v=eig(A)
print w,v

t=r_[0:0.05:4j]
T1,yout1=step_response(1*sys_plant,t)
yout2,T2=impulse(sys_plant,t)
plt.plot(T1,yout1)
plt.plot(T2,yout2)
plt.show()
