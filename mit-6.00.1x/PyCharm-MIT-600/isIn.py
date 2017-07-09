def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0:
        return False

    if len(aStr) == 1:
        if aStr == char:
            return True
        else:
            return False

    if aStr[(len(aStr) // 2)] == char:
        return True


    elif aStr[(len(aStr)//2)] > char:
        return isIn(char, aStr[:(len(aStr) // 2)])

    elif len(aStr) > 1 and aStr[(len(aStr)//2)] < char:
        return isIn(char, aStr[(len(aStr)// 2) + 1:])



s = ''
t = 'c'

print(isIn('c', s))
print(isIn('c', t))
print(isIn('b', t))
print(isIn('l', 'cdhilnqs'))
print(isIn('o', 'abcfiknnpqtvz'))