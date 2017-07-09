def odd(x):
    """
    x: int or float.

    returns: True if x is odd, False otherwise
    """

    result = None

    while x % 2 != 0:
        return "Ímpar"
        break

    while x % 2 == 0:
        return "Par"
        break

    return result

num = int(input("Entre um número: "))

print(odd(num))
