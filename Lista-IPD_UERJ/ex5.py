#!/usr/bin/env python3

i = 16; vec = []; vec_trc = []
for j in range(0, i):
    vec.append(input("Entre o elemento da posição de número {:d} do vetor: ".format(j+1)))
for j in range(i//2, i):
    vec_trc.append(vec[j])
for j in range(0, i//2):
    vec_trc.append(vec[j])
print("Vetor original:\n", vec)
print("Vetor trocado:\n", vec_trc)
