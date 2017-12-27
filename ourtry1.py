#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt
from control import *


# THIS IS THE ORIGINAL PROGRAM. DO NOT CHANGE ANYTHING
l=2.75e-6  #H
r=4  #ohm
kt=0.0274  #Nm/amp
kb=0.274   #Nm/Amp
b=3.5077e-6  #Nms
j=3.2284e-6   #kg m2

A=([0,1,0],[0,-b/j,kt/j],[0,-kb/l,-r/l])
B=([0],[0],[1/l])
C=[1,0,0]
D=0
sys_plant=ss(A,B,C,D)
w,v=eig(A)
print w,v
#v =

# 1.0e+006 *
#
#        0
#  -0.0006
#   -1.4540
#Tt=input('total_time')
#n=input('number_of_steps')
# rank of [B,A*B]= 2
t=r_[0:0.05:100j]
T,yout=step_response(1*sys_plant,t)
yout,T=impulse(sys_plant,t)
plt.plot(T,yout)
plt.show()
