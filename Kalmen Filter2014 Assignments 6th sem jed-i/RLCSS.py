#!/usr/bin/env python

# This program is for RLC circuit.
# Please write down the differential equation governing the RLC circuit.
# Represent this second order ODE as two first order ODEs and write in matrix form.
# Then go through this program, run it and see the output

#useful links: http://python-control.sourceforge.net/manual/matlab_strings.html

#IMPORT MODULES

from numpy import *
from scipy import *
from pylab import *
from control import *
from scipy.signal import lti, step
from matplotlib import pyplot as plt

#DEFINE PARAMETERS

R = 10
L = 10**-3 
CC = 10**-6   

#DEFINE MATRICES

A = ([0,1],[-1/(L*CC), -R/L])
B = [[0],[1/L]]

C = [-1/CC,-R]

D = [1]


#DEFINE LINEAR TIME INVARIANT SYSTEM "SS" IS STATE SPACE

sys_plant = ss(A,B,C,D)
print sys_plant

#DEFINE TIME STEPS
#t = r_[0:0.001:200j] 

t = linspace(0,0.001,200)

#RESPONSE OF SYSTEM TO UNIT STEP INPUT
T1, yout1 = step_response(1*sys_plant,t)

plt.plot(T1,yout1)

plt.show()

#RESPONSE OF SYSTEM TO IMPULSE INPUT
yout, T = impulse(sys_plant,t)

plt.plot(T,yout)

plt.show()

