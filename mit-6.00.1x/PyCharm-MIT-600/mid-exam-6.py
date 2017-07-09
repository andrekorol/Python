def deep_reverse(L):
    L.reverse()
    for list in L:
        list.reverse()
    return L

print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))
