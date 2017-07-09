def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    odtp = ()
    index = 0
    for i in aTup:
        index += 1
        if index % 2 != 0:
            odtp += (i,)
    return odtp

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))