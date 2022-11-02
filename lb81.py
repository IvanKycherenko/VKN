import math
import random
from array import *

n=int(input("Enter n = "))
mas=array('i',[0 for i in range(n)])

for i in range (n):
    mas[i]=random.randint(0,10)

var = mas[0]
for i in range(1, n):
    var *= mas[i]
var = pow(var, (1/n))

print(round(var,1))