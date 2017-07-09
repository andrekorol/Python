def dotProduct(listA, listB):
    new_list = []
    for a, b in zip(listA, listB):
        new_list.append(a * b)

    return sum(new_list)


print(dotProduct([1, 2, 3], [4, 5, 6]))
