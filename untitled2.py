# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:34:01 2019

@author: User
"""

from random import *
print("----Приветствуем в игре----")
print("====Камень, ножницы, бумага====")
print("Правила:")
print("Когда игра начнетса вам придложат зделать выбор: К- Камень, Н- ножницы или Б- бумага. Впишите букву соответствующую вашему выбору. Камень бйот ножницы, ножницы бют бумагу а бумага бйот камень")


player_score=0
bot_score=0
player_choise=0
bot_choise=0



print("====Начало игры====")
for i in range(3):
        print("Раунд №",str(i+1))
        bot_choise==random.choise["К","Н","Б"]
        player_choise==input()
        print("Вы",player_choise,"Бот",bot_choise)
        if player_choise==bot_choise:
                print("Ничья")
        if player_choise==К and bot_choise==Н:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Н and bot_choise==К:
                print("Бот победил")
                bot_score=bot_score+1
        elif player_choise==К and bot_choise==Б:
                print("Бот победил")
                bot_score=bot_score+1
        elif player_choise==Б and bot_choise==К:
                print("Tы победил")
                player_score=player_score+1
        elif player_choise==Н and bot_choise==Б:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Б and bot_choise==Н:
             print("Бот победил")
             bot_score=bot_score+1
        player_choise=0
        bot_choise=0
        print("Раунд №",str(i+1))
        bot_choise=random.choise["К","Н","Б"]
        player_choise=input("Ваш выбор")
        print("Вы",player_choise,"Бот",bot_choise)
        if player_choise==bot_choise:
                print("Ничья")
        elif player_choise==К and bot_choise==Н:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Н and bot_choise==К: 
                print("Бот победил")
                bot_score=bot_score+1
        elif player_choise==К and bot_choise==Б:
                print("Бот победил")
                bot_score=bot_score+1
        elif player_choise==Б and bot_choise==К:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Н and bot_choise==Б:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Б and bot_choise==Н:
                print("Бот победил")
                bot_score=bot_score+1
        player_choise=0
        bot_choise=0
        print("Раунд №",str(i+1))
        bot_choise=random.choise["К","Н","Б"]
        player_choise=input("Ваш выбор")
                print("Ви",player_choise,"Бот",bot_choise)
        if player_choise==bot_choise:
                print("Ничья")
        elif player_choise==К and bot_choise==Н:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Н and bot_choise==К: 
                print("Бот победил")
                bot_score=bot_score+1
        elif player_choise==К and bot_choise==Б:
                print("Бот победил")
                bot_score=bot_score+1 
        elif player_choise==Б and bot_choise==К:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Н and bot_choise==Б:
                print("Ты победил")
                player_score=player_score+1
        elif player_choise==Б and bot_choise==Н:
                print("Бот победил")
                bot_score=bot_score+1
        player_choise=0
        bot_choise=0
if bot_score==2:
        print("Ты проиграл")print("1:2")
if bot_score==3:
        print("Ты проиграл всухую")
if bot_score==1:
        print("Ты победил")
        print("2:1")
if bot_score==0:
        print("Ты победил всухую")