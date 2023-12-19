# a = 0
# b = 0

# n = int(input())
# lst = [i for i in range(1, n + 1)]
# print(lst)

# for num in lst:
#     if num % 2 == 0:
#         a += 1
#     else:
#         b += 1

# if b > a:
#     print("Нет")
# else:
#     print("Да")



# lst=[[1,2,3], [4,5,6], [7,8,9]]
# print(lst)
# a=0
# for i in range(3):
#     a+=lst[i][i]
# print("сумма по диагонали : ", a )




# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# a=int(input())
# for i in range(1, a+1):
#     print("fibonacci number", i, "=", fibonacci(i))




# def stepen_2(n):
#     if n == 0:
#         return False
#     while n != 1:
#         if n % 2 != 0:
#             return False
#         n = n // 2
#     return True
# a=int(input())
# print(stepen_2(a))

# Предположим, у нас есть список чисел
числа = [1, 2, 2, 3, 4, 4, 4, 5]

# Найдем все числа, которые повторяются
повторяющиеся_числа = set([число for число in числа if числа.count(число) > 1])

# Создадим генератор списков, который берет только эти числа
результат = [число for число in числа if число in повторяющиеся_числа]

print(результат)