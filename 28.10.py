#11111111111111111111111
A=1
B=10
for A in range(A,B+1):
    print(A)
#22222222222222222222222
A=int(input('A:'))
B=int(input('B:'))
if A<B:
    for A in range(A,B+1):
        print(A)
else:
    for A in range(A,B-1,-1):
        print(A)
#33333333333333333333333
a=int(input())
b=int(input())
for i in range(a-(a+1)%2,b-b%2,-2):
    print(i,end='')
#44444444444444444444444
import random
sum=0
for i in range(1,11):
    a=random.randint(1,100)
    sum+=a
    print('#',i,'',a)
print('Сумма равна: ',sum)
#555555555555555555555555
import random
sum=0
n=int(input('N:'))
for i in range(0,n):
    a=random.randint(1,100)
    sum+=a
    print(i+1,':',a)
print(sum)
#6666666666666666666666666
import random
n=int(input("N:"))
sum=0
b=1
for i in range(n+1):
    z=b**3
    b+=1
    sum+=z
print(sum)
#77777777777777777777777777
n=int(input('n='))
b=1
sum=1
for i in range(n):
    sum*=b
    b+=1
print(sum)
#888888888888888888888888
n=int(input('n='))
b=1
z=1
sum=0
for i in range(n):
    z*=b
    b+=1
    sum+=z
print(sum)
#9999999999999999999999999
num_zero=0
for i in range(int(input())):
    a=input()
    if a == '0':
        num_zero+=1
    elif a == '':
        break
#10 10 10 10 10 10 10 10 10
n=int(input('введите количество ступенек: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,sep='',end='')
    print()
    








    
