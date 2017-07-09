def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)

for num in range(9):
    f(num)
    print(num)
