def mult_iter(a, b):
    """
    :param a: The first number that you want to multiply
    :param b: The number that is going to be multiplyed by a
    :return: Returns a * b
    """
    result = 0
    while b > 0:
        result += a
        b -= 1

    return result