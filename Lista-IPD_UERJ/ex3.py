#!/usr/bin/env python3

s = input("Entre uma frase:\n")
s_lwr = s.lower()
vwls = ['a', 'e', 'i', 'o', 'u']; vogais = 0; brancos = 0; resto = 0
for letter in s_lwr:
    if letter in vwls:
        vogais += 1
    elif letter == ' ':
        brancos += 1
    else:
        resto +=1
print("Vogais = {:d}".format(vogais))
print("Brancos = {:d}".format(brancos))
print("Resto = {:d}".format(resto))
