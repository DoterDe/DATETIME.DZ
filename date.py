#Реализуйте программу, чтобы получить номер недели.
import datetime

def get_week_number(year, month, day):
    date = datetime.date(year, month, day)
    return date.isocalendar()[1]

print(get_week_number(2015, 6, 16))

#Реализуйте программу, чтобы найти дату первого понедельника данной недели. 
import datetime

def get_first_monday(year, week):
    return datetime.datetime.strptime(f'{year}-W{int(week )- 1}-1', "%Y-W%W-%w")

print(get_first_monday(2015, 50))


#Реализуйте программу, чтобы выбрать все воскресенья определенного года.
import datetime

def all_sundays(year):
    dt = datetime.date(year, 1, 1)     
    dt += datetime.timedelta(days = 6 - dt.weekday())  
    while dt.year == year:
        yield dt
        dt += datetime.timedelta(days = 7)
          
for s in all_sundays(2022):
    print(s)


#Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить новую дату
import datetime

def addYears(d, years):
    try:
        return d.replace(year = d.year + years)
    except :
        return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1)) - datetime.timedelta(days=1)

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29), 1))

#Реализуйте программу, чтобы узнать время по Гринвичу и местное время.
import datetime

gmt_time = datetime.datetime.utcnow()
local_time = datetime.datetime.now()

print(f"Время по Гринвичу: {gmt_time.strftime('%H:%M:%S')}")
print(f"Местное время: {local_time.strftime('%H:%M:%S')}")



#Реализуйте программу, для вычисления количества дней между двумя датами
import datetime

date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 12, 31)

delta = date2 - date1
days = delta.days

print(f"Количество дней между {date1} и {date2} равно {days}")


#Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и секунды

import datetime

delta1 = datetime.timedelta(days=10, hours=5, minutes=30, seconds=15)
delta2 = datetime.timedelta(days=7, hours=12, minutes=45, seconds=20)

total_delta = delta1 + delta2

total_days = total_delta.days
total_seconds = total_delta.seconds
total_hours = total_seconds // 3600
total_minutes = (total_seconds % 3600) // 60
total_seconds = (total_seconds % 3600) % 60

print(f"Общая разность дат равна {total_days} дней, {total_hours} часов, {total_minutes} минут, {total_seconds} секунд")


#Реализуйте программу на Python, для создания HTML-календаря с данными за определенный год и месяц.
import calendar
import datetime

year = 2023
month = 12

cal = calendar.HTMLCalendar()

html = cal.formatmonth(year, month)

print(html)

