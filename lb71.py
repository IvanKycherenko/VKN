def func(a, b):
    return set(a.lower()) & set(b.lower())
    
row1 = input("Введіть перші символи : ")
row2 = input("Введіть другі символи : ")

print(func(row1, row2))