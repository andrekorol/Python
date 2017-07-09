def flatten(aList):
    result = []
    for x in aList:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(L))