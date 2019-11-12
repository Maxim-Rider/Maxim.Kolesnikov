# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:20:08 2019

@author: User
"""

#1111111111111111111111111111111111111111111111
a=int(input())
b=int(input())
if a<b:
    print(a)
elif b<a:
    print(b)
else:
    print("Они равны")
#2222222222222222222222222222222222222222222222
x=int(input())
if x>0:
    print(1)
elif x==0:
    print(0)
else:
    print(-1)
#3333333333333333333333333333333333333333333333
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if (x1+y1+x2+y2)%2==0:
    print('yes')
else:
    print('no')
#444444444444444444444444444444444444444444444444
x=int(input('год:'))
if (x%4==0) and (x%100!=0) or (x%400==0):
    print('год високосный')
else:
    print('год не високосный')
#5555555555555555555555555555555555555555555555555
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
if a<b and a<c:
    print('a:',a)
elif b<a and b<c:
    print('b:',b)
elif c<a and c<b:
    print('c:',c)
else:
    print('Несколько наименьших')
#6666666666666666666666666666666666666666666666666
a=int(input())
b=int(input())
c=int(input())
if a==b and b==c and a==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)
#7777777777777777777777777777777777777777777777
x1=int(input('введи число от 1 до 8:'))
y1=int(input('введи число от 1 до 8:'))
x2=int(input('введи число от 1 до 8:'))
y2=int(input('введи число от 1 до 8:'))
if x1==x2 or y1==y2:
    print('yes')
else:
    print('no')
#88888888888888888888888888888888888888888888
x1=int(input('введи число от 1 до 8:'))
y1=int(input('введи число от 1 до 8:'))
x2=int(input('введи число от 1 до 8:'))
y2=int(input('введи число от 1 до 8:'))
if -1<=(x1-x2)<=1 or -1<=(y1-y2)<=1:
    print('yes')
else:
    print('no')
#9999999999999999999999999999999999999999999
x1=int(input('введи число от 1 до 8:'))
y1=int(input('введи число от 1 до 8:'))
x2=int(input('введи число от 1 до 8:'))
y2=int(input('введи число от 1 до 8:'))
if (abs(x1-x2))==abs(y1-y2)
    print('yes')
else:
    print('no')
#10_10_10_10_10_10_10_10_10_10_10_10_10_10_10
x1=int(input('введи число от 1 до 8:'))
y1=int(input('введи число от 1 до 8:'))
x2=int(input('введи число от 1 до 8:'))
y2=int(input('введи число от 1 до 8:'))
if (abs(x1-x2)==abs(y1-y2)) or (x1==x2 or y1==y2):
    print('yes')
else:
    print('no')
#11_11_11_11_11_11_11_11_11_11_11_11_11_11_11
x1=int(input('введи число от 1 до 8:'))
y1=int(input('введи число от 1 до 8:'))
x2=int(input('введи число от 1 до 8:'))
y2=int(input('введи число от 1 до 8:'))
if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1==x2)==1 and abs (y1-y2))==2:
    print('yes')
else:
    print('no')
#12_12_12_12_12_12_12_12_12_12_12_12_12_12_12
n=int(input())
m=int(input())
k=int(input())
if (n*m)>=k or ((k%n==0) or (k%m==0):
    print('yes')
else:
    print('no')
#Яша
n=int(input())
m=int(input())
x=int(input())
y=int(input())
b=n-x
f=m-y
if x<y and x<b and x<f:
    print(x)
elif y<x and y<b and y<f:
    print(y)
elif b<x and b<y and b<f:
    print(b)
else:
    print(f)
#УГАДАЙКА
import random
h=int(input('кол-во игр'))
a=random.randint(1,50)
g=0
while h>0:
    n=int(input('1-50'))
    if n<50:
        print()
        if n==a:
            print('ты угадал')
            a=random.randint(1,50)
            g+=1
        elif n<a:
            print('ставка ниже')
        else:
            print('ставка выше')
    else:
        print('Вы ввели некорректное число')
    h-=1
print('Загадано было',a)
print
    

    
    
    
    
    
    
    
    
    
    
    

