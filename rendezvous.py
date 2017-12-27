#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt
from control import *


# THIS IS THE ORIGINAL PROGRAM. DO NOT CHANGE ANYTHING


A=([-1,1],[1,-1])
B=([0],[0])
C=[1,1]
D=0
sys_plant=ss(A,B,C,D)
w,v=eig(A)
#Tt=input('total_time')
#n=input('number_of_steps')
t=r_[0:0.05:100j]
T,yout=step_response(1*sys_plant,t)
yout,T=impulse(sys_plant,t)
plt.plot(T,yout)
plt.show()
