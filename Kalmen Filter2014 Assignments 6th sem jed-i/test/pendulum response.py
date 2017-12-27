#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt
from control import *

g=9.81
l=1

A=([0,1],[g/l,0])
B=([1],[0])
C=[1,0]
D=0
sys_plant=ss(A,B,C,D)
w,v=eig(A)

t=r_[0:0.05:100j]
T,yout=step_response(1*sys_plant,t)
yout,T=impulse(sys_plant,t)
plt.plot(T,yout)
plt.show()
