def polysum(n, s):
    """

    :param n: number of sides of the polygon
    :param s: length of each side
    :return: the sum of the area and the square of the perimeter. The sum is rounded to 4 decimal places
    """
    from math import tan, pi
    area = (0.25 * n * (s**2)) / tan(pi / n)
    perimeter = n * s
    polygonsum = round(area + (perimeter ** 2), 4)
    return polygonsum
