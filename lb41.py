import math as m
x = int(input("Введіть x="))
a = 4**2 * x
b = m.log1p(m.cos(x))
c = 2 - m.pow((m.pow(x, 2) + 1), 1/3)
if m.cos(x) <= 0:
    print("Логарифм відємний")
    exit()
print(round(a-(b/c),2))