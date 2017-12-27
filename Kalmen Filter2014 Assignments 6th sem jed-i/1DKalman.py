
initial_location=0. #initial location   x_d
initial_uncertainity=1000. # initial uncertainity  c_d
measurement_varience=4.   # measurement varience   q
motion_varience=2.  # motion varience   w
measurements=[5. , 6. , 7. , 9. , 10. ]# measurements  z
motion=[1. , 1. , 2. , 1. , 1.]  # motion  u

measurements_copy=[5. , 6. , 7. , 9. , 10. ]
motion_copy=[1. , 1. , 2. , 1. , 1.]
motion_copy_2=[1. , 1. , 2. , 1. , 1.]

# x_d updated as x_hat
# c_d updated as v_p


# predection
def predection():
    x_hat=motion_copy[0]+(measurement_varience*initial_location + initial_uncertainity*measurements[0])/(measurement_varience+initial_uncertainity)
    c1=motion_varience+1/(1/initial_uncertainity+1/measurement_varience)
    measurements.pop(0)
    motion_copy.pop(0)
    return x_hat,c1

# update

def update():
    global initial_location,initial_uncertainity
    x_hat,c1=predection()
    print 'x_hat',x_hat,'c1',c1
    for i in range (4):
        initial_location=x_hat
        initial_uncertainity=c1
        x_hat,c1=predection()
        print 'x_updateed',x_hat,'v_updated',c1
    
    



print 'Output TEAM 8'
update()

## output
##Output TEAM 8
##x_hat 5.98007968127 c1 5.98406374502
##x_updateed 6.99201915403 v_updated 4.39744612929
##x_updateed 8.99619844136 v_updated 4.09465881011
##x_updateed 9.99812144836 v_updated 4.02338796788
##x_updateed 10.9990634621 v_updated 4.00582994814










