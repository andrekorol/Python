# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:32:23 2016

@author: andre
"""

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", int(x / y))

elif x < y:
    print("x is smaller")

else:
    print("y is smaller")
    
print("thanks!")
    