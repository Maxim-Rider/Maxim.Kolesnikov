# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:17:19 2019

@author: User
"""

for x in range(1,11):
    for y in range(1,11):
        print("*",end='')
    print()
#---------------------------------
    
for x in range(1,11):
    for y in range(1,11):
        print('{0:>3}'.format(y*x),end='')
    print()
    
#---------------------
    
    