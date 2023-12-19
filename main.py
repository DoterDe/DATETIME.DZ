# import re
# import timeit

# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2

#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# my_array = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,]

# time_shell_sort = timeit.timeit(lambda: shell_sort(my_array.copy()), number=1000)
# print("Время выполнения (Shell Sort):", time_shell_sort, "секунд")

# my_array = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,]
# time_bubble_sort = timeit.timeit(lambda: bubble_sort(my_array.copy()), number=1000)
# print("Время выполнения (Bubble Sort):", time_bubble_sort, "секунд")

# my_array = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,]
# time_quick_sort = timeit.timeit(lambda: quick_sort(my_array.copy()), number=1000)
# print("Время выполнения (Quick Sort):", time_quick_sort, "секунд")

# my_array = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90,]
# time_merge_sort = timeit.timeit(lambda: merge_sort(my_array.copy()), number=1000)
# print("Время выполнения (Merge Sort):", time_merge_sort, "секунд")

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         mid_val = arr[mid]

#         if mid_val == target:
#             return mid
#         elif mid_val < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# my_array = [11, 12, 22, 25, 34, 64, 90]
# target = 25

# time_linear_search = timeit.timeit(lambda: linear_search(my_array, target), number=1000)
# print("Индекс (Линейный поиск):", linear_search(my_array, target))
# print("Время выполнения (Линейный поиск):", time_linear_search, "секунд")

# time_binary_search = timeit.timeit(lambda: binary_search(my_array, target), number=1000)
# print("Индекс (Бинарный поиск):", binary_search(my_array, target))
# print("Время выполнения (Бинарный поиск):", time_binary_search, "секунд")



def IsAscending(A):
    for i in range(1, len(A)):
        if A[i] <= A[i-1]:
            return "NO"
    return "YES"

# def KthAppearance(A, a, k):
#     count = 0
#     for i in range(len(A)):
#         if A[i] == a:
#             count += 1
#             if count == k:
#                 return i + 1
#     return -1


# def MaxUsersForArchiving(S, N, user_sizes):
#     user_sizes.sort()
#     total_size = 0
#     count = 0
#     for size in user_sizes:
#         if total_size + size <= S:
#             total_size += size
#             count += 1
#         else:
#             break
#     return count

# def MinTaxiPayment(distances, tariffs):
#     total_payment = 0
#     for i in range(len(distances)):
#         total_payment += distances[i] * tariffs[i]
#     return total_payment

# def CountNumbers(sequence):
#     counts = [0] * 9
#     for char in sequence:
#         if char.isdigit():
#             digit = int(char)
#             if 1 <= digit <= 9:
#                 counts[digit - 1] += 1
#     return counts

# def LinearSearch(numbers, target):
#     for i in range(len(numbers)):
#         if numbers[i] == target:
#             return True, i
#     return False, -1


# def ExtractFirstWord(sentence):
#     match = re.match(r'\b\w+\b', sentence)
#     if match:
#         return match.group()
#     return None

# def ExtractDate(text):
#     match = re.search(r'\b\d{2}\.\d{2}\.\d{4}\b', text)
#     if match:
#         return match.group()
#     return None

# def CheckPhoneNumberFormat(phone_number):
#     match = re.match(r'\+\d{1,3}-\d{1,}-\d{6,}', phone_number)
#     return bool(match)

# def ExtractInfoFromHTML(html_content):
#     match = re.search(r'<title>(.*?)</title>', html_content)
#     if match:
#         return match.group(1)
#     return None

# list_example_1 = [1, 7, 9]
# result_1 = IsAscending(list_example_1)
# print(result_1)

# list_example_2 = [1, 2, 1, 3, 2, 3, 2, 3, 2, 2]
# a = 3
# k = 2
# result_2 = KthAppearance(list_example_2, a, k)
# print(result_2)

# S = 100
# N = 2
# user_sizes_example = [200, 50]
# result_3 = MaxUsersForArchiving(S, N, user_sizes_example)
# print(result_3)

# distances_example = [10, 20, 30]
# tariffs_example = [50, 20, 30]
# result_4 = MinTaxiPayment(distances_example, tariffs_example)
# print(result_4)

# sequence_example = "1234516890"
# result_5 = CountNumbers(sequence_example)
# print(result_5)

# list_example_6 = [7, 9, 5, 6, -99, -32, 10, -6, 45, 14]
# target_6 = -32
# found, index_6 = LinearSearch(list_example_6, target_6)
# print(found)
# print("Index:", index_6 + 1)

# sentence_example = "Hello, this is a sample sentence."
# result_7_1 = ExtractFirstWord(sentence_example)
# print(result_7_1)

# text_example = "The meeting is scheduled for 23.11.2023."
# result_7_2 = ExtractDate(text_example)
# print(result_7_2)

# phone_number_example = "+123-456789012"
# result_7_3 = CheckPhoneNumberFormat(phone_number_example)
# print(result_7_3)

# html_content_example = "<html><head><title>Sample Title</title></head><body>Content...</body></html>"
# result_7_4 = ExtractInfoFromHTML(html_content_example)
# print(result_7_4)
#           0    1   2  3  4



import re

text = "Hello, 123 World! This is a test string with numbers: 456 and 789."
yes = '123456754323456'


# match_result = re.match(r'\d+', text)

# if match_result:
#     print("Match using re.match():", match_result.group())
# else:
#     print("Match not found using re.match()")

# search_result = re.search(r'\d+', text)
# if search_result:
#     print("Match using re.search():", search_result.group())
# else:
#     print("Match not found using re.search()")

# findall_result = re.findall(r'\d+', text)
# print("Matches using re.findall():", findall_result)

# split_result = re.split(r'\b\w{3}\b', text)
# print("Splitted parts using re.split():", split_result)

sub_result = re.sub(r'\d+', 'NUM', text)
# print("Modified string using re.sub():", sub_result)


pattern = re.compile(r'\b\w{3}\b')
compiled_result = pattern.findall(text)
print("Matches using re.compile():", compiled_result)

print(text)