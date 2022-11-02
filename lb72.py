text = input("Введать числа через пробіл : ")

result = ''
for i in text.split():
	result += 'x=' + i + " "
	
print(result)