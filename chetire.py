import re

strochechka = input("Введите строку: ")
if re.match(r'^[A-Za-z]{2}\d{3}[A-Za-z]$', strochechka):
    print('Введённая строка может быть номером автомобиля')
else:
    print('Введённая строка не может быть номером автомобиля')
