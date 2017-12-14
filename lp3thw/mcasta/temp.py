 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import threading, queue

que = queue.Queue()

def get_name(prompt):
    s = input(prompt)
    return s


t =threading.Thread(target=lambda q, arg1: q.put(get_name(arg1)), args=(que, "Enter name: "))
t.start()
t.join(2)

string = que.get()
 
print(string)
 