def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        divisor = b

    else:
        divisor = a

    while a % divisor != 0 or b % divisor != 0:
        divisor -= 1

    return divisor


print(gcdIter(17, 12))