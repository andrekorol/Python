def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    """

    ordered_intersect = {}

    ordered_difference = {}

    d_one = d1.copy()

    d_two = d2.copy()

    for key in d_one:
        if key in d_two:
            ordered_intersect[key] = f(d_one[key], d_two[key])

            del d1[key]

            del d2[key]

    d1.update(d2)

    for k in sorted(d1.keys()):
        ordered_difference[k] = d1[k]

    return ordered_intersect, ordered_difference


def f(a, b):
    return a + b


d1 = {1: 30, 2: 20, 3: 30, 5: 80}
d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}

print(dict_interdiff(d1, d2))
