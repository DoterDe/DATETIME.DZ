print("Напишите 3 числа ?")
a=int(input())
b=int(input())
c=int(input())
print(a+b+c)
print(a*b*c)

print("Скалько ты зарабвтываешь за месяц ?")
зарплата=int(input())
print("Скалько ты должен месячного платежа по кредиту в банке ?")
долг=int(input())
print("Скалько ты должен за коммунальные услуги?")
задолжность=int(input())
print("У тебя осталось", зарплата-долг-задолжность, "тенге")

print("Введите длину одной из сторон и высоту ромбу что бы определить площадь ромба")
длина=int(input())
высота=int(input())
print("Площадь вашего ромба", длина*высота)

print("To", "be", "or", "not", "to", "be", sep="\n")

print("Life is what happens", "\n", "    "   "when", "\n",  "       ",  "you're busy making other plans", "\n", "                             ", "John Lennon")


print("Введите диаметр окружности круга")
d=int(input())
n=3.14
L=n*d
print('длина круга', L)


print("Введите радиус окружности круга")
R=int(input())
n=3.14
L=2*n*R
S=n*R**2
print('длина круга', L, 'периметр круга', S)



import math 
print("Введите 2 неотрицательных числа")
a=int(input())
b=int(input())
c=a*b
print("среднее геометрическое этих чисел", math.sqrt(c) )

print("введите длину окружности")
L=float(input())
n=3.14
N=2*n
R=L/N
S=n*R**2
print("радиус круга равен", R, "площадь круга равна", S)

print("введите любое число")
x=int(input())
y=3*x**2-6*x-7
print("значение y для уравнения y = 3x^2 - 6x равно", y)

print("введите любое число")
x=int(input())
y=4*(x-3) - 7*(x-3) + 2
print("значение y для уравнения 4(x−3) − 7(x−3) + 2 равно", y)