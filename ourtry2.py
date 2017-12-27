#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt
from control import *

# THIS IS THE ORIGINAL PROGRAM. DO NOT CHANGE ANYTHING
l=1e-3
r=1000
c=1e-6
k1=1
k2=2

A=([0,1],[-k1,-k2])
B=([0],[0])
C=[1,0]
D=0

sys_plant=ss(A,B,C,D)
w,v=eig(A)
#Tt=input('total_time')
#n=input('number_of_steps')
t=r_[0:02:30j]
T,yout=step_response(1*sys_plant,t,-2,0)
#yout,T=impulse(sys_plant,t)
plt.plot(T,yout)
plt.show()
