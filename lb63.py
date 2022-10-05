import math
a=float(input("a:"))
b=float(input("b:"))
h=float(input("h:"))
list_values = []
def f1(x):
    g=math.log((math.fabs(x + pow(math.e,x))),3)
    return(g)
if a==0 :
    print("Помилка, обрахунная неможливе")
else:
    for i in range (100):
        y=f1(b)
        a=round(a,2)
        y=round(y,4)
        list_values.append(y)
average=sum(list_values)/len(list_values)
print("Середнє:",average)