#!/usr/bin/env python3

i = 40; j = 1; result = 0
while i > 0:
    try:
        n = int(input("Entre um inteiro para a posição de número {:d} do vetor:".format(j)))
    except ValueError:
        print("Entre apenas inteiros!")
        continue
    result += n % 2 == 0
    i -= 1
    j += 1

if result == 1:
    print("De {:d} números do vetor, apenas {:d} é par".format(j-1, result))
else:
    print("De {:d} números do vetor, {:d} são pares".format(j-1, result))
