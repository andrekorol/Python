def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    if exp == 0:
        return 1

    elif exp == 1:
        return base

    elif base < 0:
        result = base
        while exp > 1:
            result *= base
            exp -= 1
        return result

    elif base > 0 and type(base) is float:
        result = base
        while exp > 1:
            result *= base
            exp -= 1
        return result
    else:
        result = 0

        while exp > 0:
            result += base * base
            exp -= 1
        return result


print(iterPower(-5.6, 10))
