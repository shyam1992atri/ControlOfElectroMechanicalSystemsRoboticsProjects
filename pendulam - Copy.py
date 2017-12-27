#!/usr/bin/env python

from numpy import *
from scipy import *
from pylab import *
from scipy.integrate import odeint

# THIS IS THE ORIGINAL PROGRAM. DO NOT CHANGE ANYTHING

# vec=[y, v] [y_dot, v_dot] = [v, -ky - \alpha v]
def d_eqn(vec,t):
    return [vec[1] , -9.81*vec[0]]


def make_quiver(y,v):
    ty,tv=[],[]
    for i in y:
        for j in v:
            [yy,vv]=d_eqn([i,j],0)
            ty.append(yy)
            tv.append(vv)
    return array(ty).reshape((size(y),size(v))).transpose(),array(tv).reshape((size(y),size(v))).transpose()

if __name__=="__main__":
    t=arange(0,50,0.1)    
    vec_init=[0,0.5]
    yv=odeint(d_eqn , vec_init,t)
    

    figure()
    grid(True)
    xlabel("Time")
    ylabel("Position and Velocity")
    plot(t, yv)

    figure()
    y=arange(-1,1,0.1)
    v=arange(-1,1,0.1)
    Y, V = meshgrid(y,v)
    #TY, TV = V, -Y-0.1*V
    TY, TV = make_quiver(y,v)
    grid(True)
    quiver(Y,V,TY,TV)
    plot(yv[:,0],yv[:,1])
    xlabel("position")
    ylabel("velocity")
    show()

