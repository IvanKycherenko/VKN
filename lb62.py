import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
n=1.0
def f1(x):
    z=math.log((math.fabs(x + pow(math.e,x))),3)
    return(z)
while a<b:
    y=f1(a)
    a=round(a,2)
    y=round(y,2)
    print(a,'  ',y)
    a=a+c