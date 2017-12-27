#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt
from control import *


# THIS IS THE ORIGINAL PROGRAM. DO NOT CHANGE ANYTHING    ctms.control
c1=2.75e-6  #H
c2=4  #ohm
c3=0.0274  #Nm/amp
c4=0.274   #Nm/Amp
c5=3.5077e-6  #Nms
m2=3.2284e-6   #kg m2

A=([0,1,0,0],[((c1*c2/(c2*c5-c1*c4))),0,0,0],[0,0,0,1],[(-c1*c3)/(c5-c1*c4),0,0,0])
B=([0],[(c4*(c1*c4-c2*c5))],[0],[c5/(c5-c1*c4)])
C=[1,0,0,0]
D=0
#control_matrix=[B,A*B]
#ran=rank(control_matrix)
#print ran
p1=-10
p2=-2
p3=-1.5
p4=-2
k=place(A,B,[p1,p2,p3,p4])
sys_plant=ss(A-m2*k,B,C,D)
w,v=eig(A)

t=r_[0:0.05:4j]
T1,yout1=step_response(1*sys_plant,t)
yout2,T2=impulse(sys_plant,t)
plt.plot(T1,yout1)
plt.plot(T2,yout2)
plt.show()
