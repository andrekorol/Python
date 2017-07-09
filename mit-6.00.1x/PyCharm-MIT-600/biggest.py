#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:15:38 2016

@author: andre
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    else:
        big = 0
        for key in aDict:
            L = aDict[key]
            if len(L) > big:
                big = len(L)
                higher_key = key
        return str(higher_key)
