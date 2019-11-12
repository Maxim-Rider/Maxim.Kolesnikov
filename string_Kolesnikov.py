# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:32:31 2019

@author: User
"""

#1111111111111111111111111111111111111
s='WhoIsThis'
print(s[2]) #1
print(s[7]) #2
print(s[0:5]) #3
print(s[0:7]) #4
print(s[::2]) #5
print(s[1::2]) #6
print(s[::-1]) #7
print(s[::-2]) #8
print(len(s)) #9
#22222222222222222222222222222222222
print(input().count(' ') + 1)
#333333333333333333333333333333333
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
#44444444444444444444444444444444444
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)
#5555555555555555555555555555555555555
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
#66666666666666666666666666666666666666
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
#777777777777777777777777777777777777
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
#888888888888888888888888888888888888
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
#99999999999999999999999999999999999
print(input().replace('1', 'one'))
#10_10_10_10_10_10_10_10_10_10_10_10_
print(input().replace('@', ''))
#11_11_11_11_11_11_11_11_11_11_11_11_
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
#12_12_12_12_12_12_12_12_12_12_12_12_
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)