##############################################################################################################
#Akhilesh Pai
#This is a program to use the Madhava/Gregory/Leibniz series to calculate a value for π/4
##############################################################################################################

tolerance = float(input('input the tolerance:')) #input for setting tolerance for convergence
n = 0       #initialise loop counter
newterm = 1 #initialise the new term 
value = 0   #initialise summation

from numpy import pi    #this is to import pi from numpy
x = pi/4                
print ("π/4 is", x)     #this prints the value of pi/4

while abs(newterm) > tolerance:     #should the magnitude of the newterm be greater than the tolerance, it loop the while statement again
    newterm = ((-1)**n)/((2*n)+1)   #Madhava/Gregory/Leibniz series formula
    #print("n is", n, ": Adding", newterm, "to our sum...")
    value = value + newterm
    n = n + 1
print ("Our value is calculated as", value)     #prints calculated value
print ("We used", n+1, "terms in the series")   #prints number of terms in series


print ("Value calculated is", value)
print ("Value of π/4 is", x)
print ("Difference between the two values is", abs(x-value))

#1e-4:
#5002 terms are used
#4.999000149941146e-05 is the difference
#1e-5:
#50002 terms are used
#4.9998999980260805e-06 is the difference
#1e-6:
#500002 terms are used
#4.999989747789257e-07 is the difference
#1e-7:
#5000002 terms are used
#4.999998659549476e-08 is the difference
#For a given tolerance value, the difference between the calculated value and the numpy value is one order of magnitude smaller, 
#therefore it is justified in claiming that the value obtained is accurate
#It took 33.55s to calculate the sum with a tolerance of 1e-8
#It took 357.12s to calculate the sum with a tolerance of 1e-9
#So it will take approximately 3.4e9s to calculate 16dp
#So it will take approximately 3.4e25s to calculate 32dp
#We extrapolated the results by first obtaining a value of time for calculating the value of pi/4 for a tolerance of 1e-8 and then 1e-9
#Then we realised a common ratio, as the values of time were approximately an order of magnitude in difference
#therefore we were able to extrapolate the values
#We do not believe it to be a good method to calculate pi because it takes too long to get an accurate value for pi.