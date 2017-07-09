# -*- coding: utf-8 -*-
print("Pense em um número de 0 a 100!")

low = 0

high = 100

while True:
    my_guess = (high + low) / 2
    print("O seu número é %d?" % my_guess)
    ans = input("Aperte 'a' para indicar que o meu chute foi muito alto. Aperte 'b' para indicar que o "
        "meu chute foi muito baixo. Aperte 'c' para indicar que meu chute está correto.")
    if ans == 'a':
        high = my_guess

    elif ans == 'b':
        low = my_guess

    elif ans == 'c':
        break

    else:
        print("Desculpe, não entendi seu comando.")

print("Game over. Seu número era o número: %d" % my_guess)
