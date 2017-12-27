#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint
#import math

# THIS IS THE PROGRAM FOR GO TO GOAL WITH CONSTANT LINEAR VELOCITY AND A PROPORTIONAL CONTROL ON ANGULAR VELOCITY. UNICYCLE MODEL
# vec=[x,y,phi]; [x_dot, y_dot, phi_dot] = [cos(phi), sin(phi), omega]


def d_eqn("""Input Three parameters as argument"""):
    return ["""return 3 parameters"""]

def make_quiver(y,v):
    ty,tv=[],[]
    for i in y:
        for j in v:
            [yy,vv]=d_eqn([i,j],0)
            ty.append(yy)
            tv.append(vv)
    return array(ty).reshape((size(y),size(v))).transpose(),array(tv).reshape((size(y),size(v))).transpose()



if __name__=="__main__":
    
    # destination
    xd = 5""" Enter X co-ordinate of your destination"""
    yd = 5""" Enter y co-ordinate of your destination"""
    
    start = 0
    vec_init =[1,1] """Put the intial condition of x,y and phi in a 			list"""
    yv = [vec_init] 
    curr_x, curr_y, curr_phi = yv[-1]
    phi_d=atan2((yd-vec_init[1])/(xd-vec_init[0]))   
    # calculate the desired angle.
    # NOTE: arctan2 takes 2 args, so it knows the sign of each argument, 
    # and returns an angle in the range of -pi to +pi 
    phid = arctan2(yd-curr_y, xd-curr_x)
    
    yvtotal = []  # array of yv, e.g. [[x, y, phi], ... ]
    ttotal = []   # array of time data
    vel = """Value of linear velocity""" # constant v0 
    K = """Value of proportional gain""     # proportional gain
    w = """Value of intial angular velocity"""     # angular velocity (turning)
    e = """ Initial error""" # error (= diff between desired angle and current angle towards destination)
    error_xy = """Value of accuracy needed""    # accuracy
    
    # repeat until we reached the desired x and y
    
    while """Write the condition""":
    
        # update w after 0.5 seconds.
        timeDiff = 0.5
        nsteps = 50
        stop = """ Define stop time interms of start time an time diff"""
        t = arange(start, stop, timeDiff/nsteps)
        
        # integrate
        yv = odeint("""Input the parameters similar to pendulum.py"" ,(w,))
        
        # we now have updated values for x,y,phi
        """Extract three values of current position x,y and angle phi from last list of yv list"""

	  """ Compute phi desired""

                
        # error = dest angle - current angle
        """ Compute the error""
        
        # angular velocity = Proportional gain * error
        """ Compute the angular velocity""
        """ Update the start time for the next loop"""

        
        # print phid, yv[-1]
        # accumulate x,y,phi and time data
        yvtotal.extend(yv)
        ttotal.extend(t)
        
    figure()
    grid(True)
    xlabel("Time")
    ylabel("state variables")
    plot(ttotal, yvtotal)
    
    figure()
    xy = zip(*yvtotal)
    plot(xy[0],xy[1])
    xlabel("positionx")
    ylabel("positiony")
    
    
    show()
    
