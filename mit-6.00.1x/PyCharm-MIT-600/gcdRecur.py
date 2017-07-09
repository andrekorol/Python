def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """

    if b == 0:
        result = a

    else:
        result = gcdRecur(b, a % b)

    return result
