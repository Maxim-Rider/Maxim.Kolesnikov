#1111111111111
i=1
n=int(input())
while i**2<n:
    print(i**2)
    i+=1
#222222222222
b=2
a=int(input())
while a%b!=0:
    b+=1
print(b)
#3333333333333333
n=int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)
#444444444444
n=int(input('Км за первый день:'))
c=int(input("Км за какой-то день:"))
g=1
while n<=c:
    n*=1.1
    g+=1
print(g)
#55555555555555
x=int(input("Вклад:"))
p=int(input("(Только число)Проценты:"))
y=int(input("Итоговый вклад:"))
g=1
while x<=y:
    x=x*((p/100)+1)
    g+=1
print(g)
#66666666666
import random
b=1
h=0
while b!=0:
    b=random.randint(0,10)
    h+=1
    print("b= ", b)
print(h)
#77777777777
import random
b=1
h=0
while b!=0:
    b=random.randint(0,19)
    h+=b
print(h)
#88888888888
import random
b=1
y=0
g=0
max=0
while b!=0:
    b=random.randint(0,99)
    y+=1
    g+=b
    if b>max:
        max=b
print(int(g/y),max)
#99999999999999
import random
x=1
y=0
max=0
index=0
while x!=0:
    x=random.randint(0,10)
    print(x)
    y+=1
    if max<=x:
        max=x
        index=y
        print("Индекс-",index,"Число-",max)
#10_10_10_10_10_10_10_10
import random
b=1
y=0
g=0
max=0
while b!=0 and y<20:
    b=random.randint(0,99)
    y+=1
    g+=b
    if b>max:
        max=b
print(int(g/y),max)

#--------------------------------------


#33333
N=int(input())
a=2
b=1
while a<=N:
    a=a*2
b+=1
print(b,a//2)    

#---------------
x=1
y=1
while y<=10:
    print(x,"*",y,"=",x*y)
    x+=1
    while x>10:
        x=1
        y+=1
        print("")
        
