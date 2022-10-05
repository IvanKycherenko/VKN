import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
n=1.0
def f1(x):
    j=math.log((math.fabs(x+pow(math.e,x))),3)
    return(j)
for i in range(100):
    y=f1(a)
    print(a,'  ',y)
    a=a+c
    if a>b:
        break