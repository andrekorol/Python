end = 6

n = 1

m = 4



l = [n]

for i in range(1, end):
    l.append(n + i)


def soma_list(list_of_numbers):
    s = 0
    for i in list_of_numbers:
        s = s + i

    return s


print(soma_list(l))
