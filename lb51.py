import math
x=float(input("Ведіть значення x="))
if x>=7.2:
    z=(math.log(4)*(math.fabs(x+1)))
elif x>-5.11 and x<7.2:
    z=(math.pow((math.log(10))*(math.fabs(math.cos(x))),1/2))
elif x<=-5.11:
    z=(x**2)+4(math.fabs(x-4))+(math.e*pow(math.e,x))
print (round(z,2))  