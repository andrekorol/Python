def closest_power(base, num):
    exponent = 0
    num = int(num)
    while base ** exponent < num:
        exponent += 1

    if abs(num - base ** exponent) == abs(num - base ** (exponent - 1)):
        exponent -= 1

    return exponent


print(closest_power(9, 1))