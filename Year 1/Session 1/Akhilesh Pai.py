######################################
#Akhilesh Pai
######################################
from numpy import sqrt
#this is the value for acceleration due to gravity
g = -9.81
#this is the initial velocity of an object thrown up in the air
v0 = 10
#this is the initial displacement of the object above the ground
z0 = 15
#this is the final displacement of the object above the ground
z = 0.0
#the below equation is the suvat equation v^2=u^2+2as
v2 = v0**2 + 2*g*(z-z0)
#this will calculate the final speed of the object that has been thrown
speed = sqrt(v2)
#determines the direction of the final velocity
if v0 > 0:
    print("v0 is positive")
else:
    print("v0 is less than or equal to zero")
#calculates the time taken for ball to travel its trajectory
time_taken = -(speed + v0)/g
#prints value of speed and time taken
print("The final speed is", speed, "m/s", "The time taken is", time_taken, "s")