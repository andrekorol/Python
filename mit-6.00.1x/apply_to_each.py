#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:18:59 2016

@author: andre
"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def absolut(x):
    if x >= 0:
        return x
    else:
        return x * (-1)

def add_1(x):
    return x + 1

def square(x):
    return x * x
