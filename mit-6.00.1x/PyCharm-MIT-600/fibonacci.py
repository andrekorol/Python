def fib(x):
    """
    :param x: an integer >= 0
    :return: Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def fib_efficient(x, d):

    if x in d:
        return d[x]
    else:
        ans = fib_efficient(x - 1, d) + fib_efficient(x - 2, d)
        d[x] = ans
        return ans


d = {1: 1, 2: 2}
arg = 8
print(fib_efficient(arg, d))
