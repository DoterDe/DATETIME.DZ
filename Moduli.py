# def print_board(a):
#     for row in a:
#         print("|", end=' ')
#         for cell in row:
#             print(cell, end=" | ")
#         print("\n-------------")

# def check_win(a, mark):
#     win_conditions = [
#         (a[0][0], a[0][1], a[0][2]), (a[1][0], a[1][1], a[1][2]), (a[2][0], a[2][1], a[2][2]),
#         (a[0][0], a[1][0], a[2][0]), (a[0][1], a[1][1], a[2][1]), (a[0][2], a[1][2], a[2][2]),
#         (a[0][0], a[1][1], a[2][2]), (a[0][2], a[1][1], a[2][0])
#     ]
#     for condition in win_conditions:
#         if condition[0] == condition[1] == condition[2] == mark:
#             return True
#     return False

# def make_move(a, mark):
#     while True:
#         try:
#             x = int(input(f"Куда поставить {mark}? "))
#             if a[(x-1)//3][(x-1)%3] not in ['x', 'o']:
#                 a[(x-1)//3][(x-1)%3] = mark
#                 break
#             else:
#                 print("Это место уже занято. Попробуйте другое.")
#         except (ValueError, IndexError):
#             print("Введите число от 1 до 9.")

# a = [[1,2,3],[4,5,6],[7,8,9]]
# h = "x"
# g = "o"

# for turn in range(9):
#     print_board(a)
#     make_move(a, h if turn % 2 == 0 else g)
#     if check_win(a, h if turn % 2 == 0 else g):
#         print_board(a)
#         print(f"Игрок {h if turn % 2 == 0 else g} выиграл!")
#         break
# else:
#     print("Ничья!")

f = ['Аскаров', 'Бекмуханов', 'Ернур', 'Пешая', 'Карим', 'Шаримазданов', 'Ернур', 'Ернур']

counts = {}
for i in f:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

max_votes = max(counts.values())

candidates = []
for candidate, votes in counts.items():
    if votes == max_votes:
        candidates.append(candidate)


winner = candidates[0]
for candidate in candidates:
    if len(candidate) < len(winner):
        winner = candidate

print(f"Победитель выборов: {winner}")
print(f"Количество голосов победителя: {counts[winner]}")





    


