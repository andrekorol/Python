def dig_pow(n, p):
    string_n = str(n)
    L = []
    for num in string_n:
        L.append(int(num) ** p)
        p += 1
    soma = sum(L)
    if (soma / n) % 1 == 0:
        return soma / n
    else:
        return -1