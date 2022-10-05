import math
def func(x,y,m):
    a = math.pow((x**3)+(math.pi**2),1/2)
    b = math.e**(y+1)
    c = math.pow(m+math.tan(m),1/2)
    return a+b+c
def main():
    x = int(input("Введіть х=")) 
    y = int(input("Введіть y=")) 
    m = int(input("Введіть m=")) 
    print(func(x,y,m))
if __name__ == "__main__":
    main()