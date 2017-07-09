# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:19:44 2016

@author: andre
"""

x = int(input('Enter an integer'))

if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')

elif x % 3 ==0:
    print('Divisible by 3 and not by 2')