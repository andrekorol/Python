def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1

    elif exp == 1:
        return base

    else:
        result = base * recurPower(base, exp - 1)
        return result
