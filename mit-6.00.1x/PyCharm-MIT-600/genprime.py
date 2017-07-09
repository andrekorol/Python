def genPrimes():
    primes = []
    x = 2
    primes.append(x)
    while True:
        if all((x % p !=0) for p in primes):
            primes.append(x)
            yield x
        if len(primes) == 1:
            yield x
        x += 1