# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:13:57 2019

@author: User
"""

#Условные опператоры и циклы 06,11,2019
sex=input('Выберите ваш пол(female or male):')
if sex='male':
age=int(input('Введите ваш возраст:'))
    if 15<age<19:
    print('Вы зачислены в футбольную команду')
    else:
        print('Вы не подходите')
else:
    print('Вы не подходите')
#----------------------------------------------
money=int(input('Сколько будете вкладывать:'))
time=int(input('На сколько лет?'))
p=0.05
y=0
for i in range(1,time):
    b=money*p
    print(i,'Начало года:',money, 'интресс',b,'наконец года:',(money+b))
    money+=b
    y+=b
print('Итог:',money)
print('Прибыль:',y)
#------------------------------------------








