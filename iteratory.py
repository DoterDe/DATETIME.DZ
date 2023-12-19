# a = [1,2,3,4,5,6,7] 
# b = {x:x**3 for x in a if x % 2 != 0 }
# print(b)


# a= [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] 
# c = {число for число in a if a.count(число) > 1}
# b = [x for x in a if x % 2 == 0 and (x in c or x == 2)] 
# b = list(set(b))
# print(b)


# A = [i * 10 for i in range(1, 10)]
# print(A)


# def gencubes(n):
#     for x in n:
#         if x%7==0:
#             yield x
        

# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for cube in gencubes(n):
#     print(cube)



import itertools

# Входная последовательность символов
input_sequence = "k98.ok"

# Отфильтровываем только буквы из входной последовательности
letters = [char for char in input_sequence if char.isalpha()]

# Генерируем все возможные комбинации букв
all_combinations = set()
for i in range(1, len(letters) + 1):
    for combination in itertools.permutations(letters, i):
        all_combinations.add(''.join(combination))

# Сортируем комбинации по длине и выводим результаты
sorted_combinations = sorted(all_combinations, key=len)
print(len(sorted_combinations))
for word in sorted_combinations:
    print(word)