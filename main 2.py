from datetime import datetime
from functools import reduce
import numpy as np
import calendar
import collections

n = int(input('Введите число: '))
array = []
for i in range(n):
    array.append(int(input()))

evens = list(filter(lambda n: n % 2 == 0, array))
odds = list(filter(lambda n: n % 2 != 0, array))

print(evens)
print(odds)

from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.time())

multiply = lambda x, y: x*y

def second_task(value, func):
    print(f"Удвоенное значение {value} = {func(value, 2)}")
    print(f"Утроенное значение {value} = {func(value, 3)}")

second_task(15, multiply)






check = lambda x: x**2 if x > 0 else x**3

print(check(-5))

lst = [4, 56, 98, 52, 963, 741, 25, 8]
newlist = list(filter(lambda n: n % 2 != 0, lst))
print(newlist)  


lst = [4, 56, 98, 52, 963, 741, 25, 8]
newlist = list(map(lambda n: n*2, lst))
print(newlist)



# Задание №1: Лямбда-функции

# 1. Добавление 15 к заданному числу:
add_15 = lambda x: x + 15
result_1 = add_15(10)
print(result_1)  # Выведет 25

# 2. Умножение аргумента x на аргумент y:
multiply = lambda x, y: x * y
result_2 = multiply(12, 4)
print(result_2)  # Выведет 48

# 3. Фильтрация списка целых чисел:
numbers = [78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Список четных чисел:", even_numbers)
print("Список нечетных чисел:", odd_numbers)

# 4. Вывод года, месяца, даты и времени:
current_datetime = datetime.now()
print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.strftime("%H:%M:%S.%f"))

# Задание №2: Функция для лямбды

def operate_on_value(value, lambda_function):
    result_double = lambda_function(value, 2)
    result_triple = lambda_function(value, 3)

    print(f"Удвоенное значение {value} = {result_double}")
    print(f"Утроенное значение {value} = {result_triple}")

operate_on_value(15, lambda x, y: x * y)

# Задание №3: Лямбда для подсчета четных и нечетных чисел в списке

numbers = [147, 241, 39, 5, 778, 18, 0, 10]
count_even = len(list(filter(lambda x: x % 2 == 0, numbers)))
count_odd = len(list(filter(lambda x: x % 2 != 0, numbers)))
print("Список целых чисел:", numbers)
print("Количество четных чисел:", count_even)
print("Количество нечетных чисел:", count_odd)

# Модули и пакеты

# Задание №1: Массив 10x10 со случайными значениями
array = np.random.random((10, 10))
min_value = np.min(array)
max_value = np.max(array)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)

# Задание №2: Случайный вектор размера 30 и среднее значение
vector = np.random.random(30)
average_value = np.mean(vector)
print("Случайный вектор:", vector)
print("Среднее значение:", average_value)

# Задание №3: Массив 2d с 1 на границе и 0 внутри
array_2d = np.ones((10, 10))
array_2d[1:-1, 1:-1] = 0
print(array_2d)

# Задание №4: Матрица 5x5 со значениями чуть ниже диагонали
matrix = np.diag([1, 2, 3, 4], k=-1)
print(matrix)

# Задание №5: Получение всех дат августа 2022 года
year = 2022
month = 8
dates_in_month = calendar.monthcalendar(year, month)
august_dates = [day for week in dates_in_month for day in week if day != 0]
print(august_dates)



c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1
    print(c)

