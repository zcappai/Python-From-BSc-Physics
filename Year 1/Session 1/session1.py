######################################
# Code to calculate the length of a vector
# Akhilesh Pai
######################################

from numpy import sqrt

#rx = 3
#ry = 2.4
#rz = 3.5

#get the componentss of the vector from the user
rx = float(input("Input the x-component of r:"))
ry = float(input("Input the y-component of r:"))
rz = float(input("Input the z-component of r:"))

# calculate the length of the vector
length_squared = rx**2 + ry**2 + rz**2

length = sqrt(length_squared)

# output the length to the screen
print("The length of the vector is", length)