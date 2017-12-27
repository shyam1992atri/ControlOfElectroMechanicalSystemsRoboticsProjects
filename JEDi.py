from numpy import *
from scipy import *
from pylab import *
from control import *
from scipy.integrate import odeint
from scipy.signal import lti,step
from matplotlib import pyplot as plt

a=([1,2],[3,4])
b=([5],[6])
c=[7,8]
d=1
sys_plant=ss(a,b,c,d)
w,v=eig(a)
Tt=input('total_time')
n=input('number_of_steps')
t=r_[0:Tt:n]
T,yout=step_response(1*sys_plant,t)
yout,T=impulse(sys_plant,t)
plt.plot(T,yout)
plt.show()

# control module was downloaded from
#http://sourceforge.net/projects/python-control/

# error being showed when i run this code
#Traceback (most recent call last):
#File "C:\Users\SHYAMPRASAD V ATRI\Desktop\Python  programe\JEDi.py", line 4, in <module>
#from control import *
#ImportError: No module named 'control'
