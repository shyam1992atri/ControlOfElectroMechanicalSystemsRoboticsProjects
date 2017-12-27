from scipy import *
from pylab import *
from scipy.integrate import odeint
import math


init=[0,0]
final=[5,5]
vel=-5
phid=math.atan((final[1]-init[1])/(final[0]-init[0]))
t=0
start=[vel,vel]
phi=math.atan((final[1]-start[1])/(final[0]-start[0]))
omg=-3
phi=phi*omg
print(phi)
k=1.5  #pid term
x=[]
y=[]
while(phi!=phid and t<10):
    curr=[vel*math.cos(phi),vel*math.sin(phi)]
    phi=omg*(math.atan((final[1]-curr[1])/(final[0]-curr[0])))
    err=phid-phi    # error calculation for pid
    omg=k*err       # PID with only p taken to account
    phi=phi*omg
    
    x.append(curr[0])
    y.append(curr[1])
    t=t+0.1

plot(x,y,[-5,5],[-5,5])
show()
