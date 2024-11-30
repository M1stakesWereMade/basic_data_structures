# 4th program
s = '123.456'
number = float(s)  # Преобразуем строку в дробное число
first_digit = int(number * 10) % 10  # Умножаем на 10, затем получаем первую цифру после запятой
print(first_digit)
