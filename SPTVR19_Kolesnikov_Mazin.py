# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:25:03 2019

@author: User
"""

#1.11.19 Maksim Kolesnikov; Mihail Mazin

#1111111111111111111111111111111111
#Здесь происходят вычеслительные дейтсвия, выводящую на экран все четырёхзначные числа последовательности 1000 1003 1006 1009 1012 1015 ….
i=1000
while i <= 9999:
    print(i)
    i = i + 3
#2222222222222222222222222222222222
#Здесь программа находит первые 55 элементов последовательности 1 3 5 7 9 11 13 15 17 ….
i=1
while i <= 55:
    print(i)
    i = i + 2
#3333333333333333333333333333333333
#Здесь программа ищет все неотрицательные элементы последовательности 90 85 80 75 70 65 60 ….
i=90
while i >= 0:
    print(i)
    i = i - 5
#4444444444444444444444444444444444
#Здесь написана программа, которая выводит на экран первые 20 элементов последовательности 2 4 8 16 32 64 128 ….
i=2
while i <= 1111111:
    print(i)
    i = i * 2
#5555555555555555555555555555555555
#Эта программа Выводит на экран все члены последовательности 2an-1–1, где a1=2, которые меньше 10000.
i=2
while i <=10000:
    print(i)
    i= 2*i -1
#6666666666666666666666666666666666
#Здесь программа, которая Выводит на экран все двузначные члены последовательности 2an-1+200, где a1= –166.
a = -166
i = 0
while a < 100:
    if(a > -100 and (a < -9 or a > 9)):
        print(a)
    a = 2 * a + 200
    i = i + 1
#7777777777777777777777777777777777
#Это программа, вычисляющая факториал натурального числа n, которое пользователь введёт с клавиатуры.
n=int(input('Введите число:'))
x=1
sum=1
for x in range(1,n+1):
    sum *=x
    x+=1
print(sum)
#8888888888888888888888888888888888
#Здесь у нас происходит вычисление всех положительных делителей натурального числа, введённого пользователем с клавиатуры.
a = int(input())
i = a
b = 0
while i > 0:
    b = a % i
    if(b == 0):
        print(i)
    i = i -1
#999999999999999999999999999999999
#Здесь программа проверяет, является ли введённое пользователем с клавиатуры натуральное число — простым.
a = int(input())
i = int(a ** 0.5)
while i >= 1:
    if(a % i == 0 and i != 1):
        print("Число составное")
        break
    if(i == 1):
        print("Число простое")
    i = i - 1
#10_10_10_10_10_10_10_10_10_10
#Программа, выводящая на экран 12 первых элементов последовательности 2an-2–2, где a1=3 и a2=2.
neChet = 3
chet = 2

i = 3

while i <=20:
    if(i%2 != 0):
        neChet= 2 * neChet - 2
        print(neChet)
    else:
        chet = 2 * chet -2
        print(chet)
    i = i + 1
#11_11_11_11_11_11_11_11_11_11_
#Эта программа выводит на экран первые 11 членов последовательности Фибоначчи. 
a = 1
b = 1
c = 0
print(a, " " , b)
i = 3
while i < 11:
    c = a + b
    a = b
    b = c
    print(c)
    i = i + 1
#12_12_12_12_12_12_12_12_12
#Эта программа находит для введённого пользователем с клавиатуры натурального числа сумму всех его цифр
n = int(input())
sum = 0
while(n != 0):
    sum = sum + (n % 10)
    n = n //10
print(sum)
#13_13_13_13_13_13_13_13_13
#С помощью этой программы система подсчитывает сколько счастливых билетов в одном рулоне
sum = 0
i = 1
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0
while i<= 999999:
    number1 = i / 100000
    number2 = (i/10000)%10
    number3 = (i/1000)%10%10
    number4 = (i/100)%10%10%10
    number5 = (i/10)%10%10%10%10
    number6 = i%10%10%10%10
    if (number1 + number2 + number3 == number4 + number5 + number6):
        sum = sum + 1
        i = i + 1
print("Рулон билетов с номерами от 000001 до 999999 имеет ", sum, " счастливых билетов.")











