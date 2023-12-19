##Реализуйте программу, чтобы получить номер недели.
# import datetime

# def get_week_number(year, month, day):
#     date = datetime.date(year, month, day)
#     return date.isocalendar()[1]

# print(get_week_number(2015, 6, 16))

##Реализуйте программу, чтобы найти дату первого понедельника данной недели. 
# import datetime

# def get_first_monday(year, week):
#     return datetime.datetime.strptime(f'{year}-W{int(week )- 1}-1', "%Y-W%W-%w")

# print(get_first_monday(2015, 50))


##Реализуйте программу, чтобы выбрать все воскресенья определенного года.
# import datetime

# def all_sundays(year):
#     dt = datetime.date(year, 1, 1)     
#     dt += datetime.timedelta(days = 6 - dt.weekday())  
#     while dt.year == year:
#         yield dt
#         dt += datetime.timedelta(days = 7)
          
# for s in all_sundays(2022):
#     print(s)


##Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить новую дату
# import datetime

# def addYears(d, years):
#     try:
#         return d.replace(year = d.year + years)
#     except :
#         return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1)) - datetime.timedelta(days=1)

# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29), 1))

# #Реализуйте программу, чтобы узнать время по Гринвичу и местное время.
# import datetime

# gmt_time = datetime.datetime.utcnow()
# local_time = datetime.datetime.now()

# print(f"Время по Гринвичу: {gmt_time.strftime('%H:%M:%S')}")
# print(f"Местное время: {local_time.strftime('%H:%M:%S')}")



# #Реализуйте программу, для вычисления количества дней между двумя датами
# import datetime

# date1 = datetime.date(2023, 1, 1)
# date2 = datetime.date(2023, 12, 31)

# delta = date2 - date1
# days = delta.days

# print(f"Количество дней между {date1} и {date2} равно {days}")


##Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и секунды

# import datetime

# delta1 = datetime.timedelta(days=10, hours=5, minutes=30, seconds=15)
# delta2 = datetime.timedelta(days=7, hours=12, minutes=45, seconds=20)

# total_delta = delta1 + delta2

# total_days = total_delta.days
# total_seconds = total_delta.seconds
# total_hours = total_seconds // 3600
# total_minutes = (total_seconds % 3600) // 60
# total_seconds = (total_seconds % 3600) % 60

# print(f"Общая разность дат равна {total_days} дней, {total_hours} часов, {total_minutes} минут, {total_seconds} секунд")


##Реализуйте программу на Python, для создания HTML-календаря с данными за определенный год и месяц.
# import calendar
# import datetime

# year = 2023
# month = 12

# cal = calendar.HTMLCalendar()

# html = cal.formatmonth(year, month)

# print(html)






# Создаем словарь для транслитерации с русского на английский[^1^][1]
ru_en = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "ie",
    "ы": "y",
    "ь": "'",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}

# Создаем словарь для транслитерации с английского на русский
en_ru = {v: k for k, v in ru_en.items()}

# Создаем функцию для транслитерации с русского на английский[^1^][1]
def translit_ru_en(text):
    return ''.join(ru_en.get(i, i) for i in text.lower())

# Создаем функцию для транслитерации с английского на русский
def translit_en_ru(text):
    return ''.join(en_ru.get(i, i) for i in text.lower())

# Запрашиваем у пользователя направление перевода
direction = input("Введите 1 для транслитерации с русского на английский, 2 - с английского на русский: ")

# Открываем файл с данными для чтения
with open("input.txt", "r", encoding="utf-8") as input_file:
    text = input_file.read()

# Выполняем транслитерацию в зависимости от выбранного направления
if direction == "1":
    result = translit_ru_en(text)
elif direction == "2":
    result = translit_en_ru(text)
else:
    print("Неверный ввод")

# Записываем результат в новый файл
with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(result)
