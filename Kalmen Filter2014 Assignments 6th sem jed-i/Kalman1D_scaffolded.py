#!/usr/bin/env python

# This program is for implementing a 1D Kalman filter.
# positions of a car are being measured and location at next time instant is predicted based on past and current measurements.


from numpy import *
from scipy import *
from pylab import *

#define a function to update position measurements such that variance is minimized.

def update(   ):
    "enter your code here"
    return 
    
# this function predicts the location of the robot at the next time instant based on measurements made upto current time step.
    
def predict(   ):
    x_hat=(measurement_sig *mu + sig*measurements[0])/(q+c_d)
    return 

# set of measurements and motion (distance moved) are recorded. In real time, each element of these arrays will be available at each successive #timestep.
    
measurements = [5.,6.,7.,9.,10.]
motion = [1,1,2,1,1]
measurement_sig = 4.
motion_sig = 2.

#initial location given by mean zero and large uncertainty, robot has only a vague idea of where it is.

mu = 0
sig = 10000

#Now the update and predict loop begins. 
     "enter your code here."

    
    
print   'is the final location and' ,    'is the variance or uncertainty about knowing this location'
        
 


