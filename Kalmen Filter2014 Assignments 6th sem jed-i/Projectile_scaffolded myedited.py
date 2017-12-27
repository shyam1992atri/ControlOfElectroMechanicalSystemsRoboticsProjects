# kalman_scaf.py

# Implements a multi-variable linear Kalman filter.

# Modified by Shyam Prasad V Atri

import pylab
import math
import random
from numpy import matrix
from numpy import eye as identity
from numpy import transpose
from numpy import zeros
from numpy import ones
from numpy.linalg  import inv as inverse

# acceleration due to gravity
G = 9.81
# angle of cannon
angle = 60
# muzzle speed
muzzle_velocity = 100
# noise level added to the measurements
noiselevel = 20

# Implements a linear Kalman filter.
class KalmanFilterLinear:
  def __init__(self,_A, _B, _H, _X, _C, _W, _Q):
    self.A = _A         # State transition matrix.
    self.B = _B         # Control matrix.
    self.H = _H         # Observation matrix.
    self.X  = _X 	# current_state_estimate: Initial state estimate.
    self.C = _C  	# current_prob_estimate: Initial covariance estimate.
    self.W = _W         # Estimated error in process.
    self.Q = _Q         # Estimated error in measurements.
    self.AT = transpose(self.A)
    self.HT = transpose(self.H)
    self.K = identity(4)
    self.V = identity(4)

  def getCurrentState(self):
      return self.X

  def predict(self, u, z):
      # u = control_vector, 
      # z = measurement_vector 

      # Prediction step
      # Predicted State Estimate X_p = AX + Bu
      X_p = self.A * self.X + self.W
      # Predicted Probability Estimate V_p = ACA_t + W
      V_p = self.A*self.C*self.AT+self.W

      # Observation step
      IC = 1
      # Kalman Gain K
      K = V_p*self.HT*inverse(self.H*V_p*self.HT+self.Q)
      self.X = X_p + K * (z-self.H*X_p)
      self.C = V_p - K * self.H*V_p
      self.K = K
      self.V = V_p

# Simulates the classic physics problem of a cannon shooting a ball in a
# parabolic arc.  In addition to giving "true" values back, you can also ask
# for noisy values back to test Kalman filters.

class Cannon:
  gravity = [0,-G]      # gravitational acceleration vector
 
  # The initial velocity of the cannonball
  theta = angle * math.pi/180
  velocity = [muzzle_velocity * math.cos(theta), muzzle_velocity * math.sin(theta)]
  pos = [0,10] 	 	# The initial location of the cannonball.
  acceleration = [0,0] 	# The initial acceleration of the cannonball.

  def __init__(self,_timeslice,_noiselevel):
      self.timeslice = _timeslice
      self.noiselevel = _noiselevel

  def add(self,x,y): 	return x + y
  def mult(self,x,y): 	return x * y
  def getX(self): 	return self.pos[0]
  def getY(self): 	return self.pos[1]
  def getXWithNoise(self): return random.gauss(self.getX(),self.noiselevel)
  def getYWithNoise(self): return max(0,random.gauss(self.getY(),self.noiselevel))
  def getXVelocity(self): 	return self.velocity[0]
  def getYVelocity(self): 	return self.velocity[1]

  # Increment through the next timeslice of the simulation.
  def step(self):
      # We're gonna use this vector to timeslice everything.
      timeslicevec = [self.timeslice,self.timeslice]

      # Break gravitational force into a smaller time slice.
      sliced_gravity = map(self.mult,self.gravity,timeslicevec)
      # The only force on the cannonball is gravity.
      sliced_acceleration = sliced_gravity
      # Apply the acceleration to velocity.
      self.velocity = map(self.add, self.velocity, sliced_acceleration)
      sliced_velocity = map(self.mult, self.velocity, timeslicevec )
      # Apply the velocity to location.
      self.pos = map(self.add, self.pos, sliced_velocity)

      # Cannonballs shouldn't go into the ground.
      if self.pos[1] < 0:
          self.pos[1] = 0
  
# These are arrays to store the data points we want to plot at the end.
x = []
y = []
nx = []
ny = []
kx = []
ky = []

# How many seconds should elapse per iteration?
timeslice = 0.1
# How many iterations should the simulation run for?
iterations = 500

# state variables: [X position, velocity in X direction, Y position, velocity in Y direction]
initX = -200
initY = 300
velX = 0
velY = 0

# This is our (random) guess of the initial state.  
initial_state = matrix([[initX],[velY],[initY],[velY]])
initial_probability = identity(4)

# fill in the matrices
state_transition = matrix([[1,timeslice,0,0],[0,1,0,0],[0,0,1,timeslice],[0,0,0,1]])
control_matrix = matrix([[0],[0],[0],[-timeslice]])
control_vector = matrix([[G]])

# we directly observe the variables, so
observation_matrix = identity(4)

# assume arbitrary values for process and measurement errors covariance
process_covariance = identity(4)*0.01 + ones(4)*random.randint(1,3)/1000
measurement_covariance = identity(4)*0.3 + ones(4)*random.randint(1,2)/10

kf = KalmanFilterLinear(state_transition, control_matrix, observation_matrix, initial_state, initial_probability, process_covariance, measurement_covariance)

def getMeasurements(can):
    # observed position
    newestX = can.getXWithNoise()
    newestY = can.getYWithNoise()
    # Iterate the cannon simulation to the next timeslice.
    vx = can.getXVelocity()
    vy = can.getYVelocity()
    return matrix([[newestX],[vx],[newestY],[vy]])

can = Cannon(timeslice,noiselevel)
# Iterate through the simulation.
for i in range(iterations):
    # true position
    x.append(can.getX())
    y.append(can.getY())

    # are we done?
    if y[-1] <= 0: break

    # predicted position
    state = kf.getCurrentState()
    kx.append(state[0,0])
    ky.append(state[2,0])

    measurement_vector = getMeasurements(can)
    nx.append(measurement_vector[0,0])
    ny.append(measurement_vector[2,0])

    # step through simulation
    can.step()
    kf.predict(control_vector, measurement_vector)

# Plot all the results we got.
pylab.figure()
pylab.title('Prediction of path of a projectile (Measurement noise level %d%%)' %noiselevel)
pylab.plot(x,y,'b:',nx,ny,'g^',kx,ky,'r-')
pylab.legend(('True','Measured','Predicted'))
pylab.xlabel('X position')
pylab.ylabel('Y position')

# the next 2 lines are for maximizing the plot window size
mng = pylab.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
pylab.show()
