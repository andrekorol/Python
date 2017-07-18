#!/usr/bin/env python3

def celcius_to_fahrenheit(t):
    return t * (9/5) + 32

n = 50; i = 1; temps = []

while n > 0:
    try:
        t = float(input("Entre a temperatura de número {:d}:".format(i)))
    except ValueError:
        print("Entre apenas inteiros ou floating points!")
        continue
    temps.append(celcius_to_fahrenheit(t))
    n -= 1
    i += 1
    
fahrenheit_avg = sum(temps) / 50
celsius_avg = (fahrenheit_avg - 32) * (5 / 9)
above_avg = 0

for t in temps:
    if t > fahrenheit_avg:
        above_avg += 1
print("A temperatura média foi de {:.3f} graus Fahrenheit = {:.3f} graus Celsius".format(fahrenheit_avg, celsius_avg))
print("{:d} temperaturas ficaram acima da média".format(above_avg))
