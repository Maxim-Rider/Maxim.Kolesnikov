'''Created on Mon Nov  4 12:14:32 2019

1 - Rock / Камень
2 - Scissors / Ножницы
3 - Paper / Бумага'''


for y in range(3):
    import random

player_score=0
bot_score=0


x = random.randint(1, 3)
y = input()

#lose
if x == 1 and y == "2":
    print("Бумага против камня! Победил компьютер!")
    bot_score=bot_score+1
elif x == 2 and y == "3":
    print("Бумага против ножниц! Победил компьютер!")
    bot_score=bot_score+1
elif x == 3 and y == "1":
    print("Камень против бумаги! Победил компьютер!")
    bot_score=bot_score+1

#won
elif x == 2 and y == "1":
    print("Камень против ножниц! Ты победил!")
    player_score=player_score+1
elif x == 3 and y == "2":
    print("Ножницы против бумаги! Ты победил!")
    player_score=player_score+1
elif x == 1 and y == "3":
    print("Бумага против камня! Ты победил!")
    player_score=player_score+1

#draw
elif x == 1 and y == "1":
    print("Камень против камня! Ничья!")
elif x == 2 and y == "2":
    print("Ножницы против ножниц! Ничья!")
elif x == 3 and y == "3":
    print("Бумага против бумаги! Ничья!")

else:
    print("Вы о чём вообще?")
    
if bot_score==2:
        print("Ты проиграл")
if player_score==2:
        print("Ты победил")

