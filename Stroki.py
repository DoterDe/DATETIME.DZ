a=str(input("введите 2 слова "))
b=list(a)
c=b[::-1]
d=str("".join(map(str, c)))
print(d)
#map я знал еще до нашего курса 

a=input("введите слова: ")

if " " in a :
    b=a.count(" ")
    print("в этом предложении ", b+1, "слова")
else: 
    print(1)

a=str(input( "пишите заметку с датой "))
#скорее всего я сделал не правильно можно было использовать другой метод я это понял но у меня не вышло использовать str = "h3110 23 cat 444.4 rabbit 11 2 dog"[int(s) for s in str.split() if s.isdigit()] а задпние вроде выполнено 

b=a.replace("2020" , "2021").replace("2019", "2021").replace("2018", "2021").replace("2017", "2021").replace("2016", "2021").replace("2015", "2021").replace("2014", "2021").replace("2013", "2021").replace("2012", "2021").replace("2011", "2021").replace("2010", "2021").replace("2009", "2021").replace("2008", "2021").replace("2007", "2021").replace("2006", "2021").replace("2005", "2021").replace("2004", "2021").replace("2003", "2021").replace("2002", "2021").replace("2001", "2021").replace("2000", "2021")
print(b)
