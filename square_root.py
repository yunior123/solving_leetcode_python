import math

from numpy.core import double


def square_root(x: int):
    first = 0
    last = x

    while first <= last:
        midpoint = float(((first + last)/2))
        midpoint_square = midpoint * midpoint
        if midpoint_square == x:
            if round(midpoint)*round(midpoint) == x:
                return int(round(midpoint))
            return math.trunc(midpoint)
        elif midpoint_square < x:
            first = midpoint+0.00001
        else:
            last = midpoint-0.00001
    if round(first)*round(first) == x:
        return int(round(first))
    return math.trunc(first)