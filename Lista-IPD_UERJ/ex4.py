#!/usr/bin/env python3

i = 30; j = 1; vec = []
while i > 0:
    try:
        n = int(input("Entre um inteiro para a posição de número {:d} do vetor:".format(j)))
    except ValueError:
        print("Entre apenas inteiros!")
        continue
    vec.append(n); i -= 1; j += 1

while True:
    try:
        n = int(input("Entre um inteiro:"))
        break
    except ValueError:
        continue
result = 0
for k in vec:
    result += k == n

if result == 1:
    print("O número {:d} aparece apenas {:d} vez no vetor".format(n, result))
else:
    print("O número {:d} aparece {:d} vezes no vetor".format(n, result))
