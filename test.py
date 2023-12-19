# def InsertionSort(A):
#     for i in range(1, len(A)):
#         key = A[i]
#         j = i - 1
#         while j >= 0 and key < A[j]:
#             A[j + 1] = A[j]
#             j -= 1
#         A[j + 1] = key
#     return A


# def SelectionSort(A):
#     sorted_list = []

#     while A:
#         min_index = arr.index(max(A))
#         sorted_list.append(A.pop(min_index))

#     return sorted_list
# arr=[1, 4, 2, 3, 4]
# print(SelectionSort(arr))


# def calculate_min_cost(prices):
#     sorted_prices = sorted(prices, reverse=True)
#     total_cost = 0
#     for i in range(len(sorted_prices)):
#         if (i + 1) % 3 != 0:
#             total_cost += sorted_prices[i]
#     return total_cost
# a = [int(x) for x in input().split(",")]
# prices = []
# b=prices.extend(a)

# print(calculate_min_cost(prices))


# def chisla(dvachisla):
#     sort_chisla = sorted(dvachisla)
#     chislo=(sort_chisla[0],sort_chisla[1])
#     min_diff = chislo[1] - chislo[0]
#     for i in range(len(sort_chisla)-1):
#         diff = sort_chisla[i + 1] - sort_chisla[i]
#         if diff<min_diff:
#             min_diff=diff
#             chislo=(sort_chisla[i],sort_chisla[i + 1])
#     return chislo

# a=[9, 4, 1, 6]
# print(chisla(a))



# strings = []
# M = int(input("Введите кол во слов: "))
# for _ in range(M):
#     strings.append(input("Введите слово: "))
# max_length = max(len(s) for s in strings)
# print(max_length)
# for s in strings:
#     stars = '*' * (max_length - len(s))
#     print(f"{stars}{s}")


# def balance_positive_negative(numbers):
#     positive_sum = sum(x for x in numbers if x > 0)
#     negative_sum = sum(x for x in numbers if x < 0)
#     new_element = -negative_sum - positive_sum
#     numbers.append(new_element)
#     return numbers

# numbers = [-3, -2, 1, 2, 3, 4]
# balanced_numbers = balance_positive_negative(numbers)
# print(balanced_numbers) 











