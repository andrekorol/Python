def isValidWalk(walk):
    time = 0
    s = 0
    e = 0
    w = 0
    n = 0
    for direction in walk:
        time += 1
        if direction == 'n':
            n += 1
        elif direction == 's':
            s += 1

        elif direction == 'w':
            w += 1

        elif direction == 'e':
            e += 1

    n_s = n - s
    w_e = w - e

    origin = n_s + w_e

    if origin == 0 and time == 10:
        return True

    else:
        return False