from scipy import odeint 
from pylab import * # for plotting commands 
 
def deriv(y,t): # return derivatives of the array y 
    a = -2.0 
    b = -0.1 
    return array([ y[1], a*y[0]+b*y[1] ])


if __name__== "__main__":
    time = linspace(0.0,10.0,1000) 
    yinit = array([0.0005,0.2]) # initial values 
    y = odeint(deriv,yinit,time) 
 
    figure() 
    plot(time,y[:,0]) # y[:,0] is the first column of y 
    show() 
