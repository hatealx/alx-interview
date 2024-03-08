#!/usr/bin/python3
"""pascal triangle program"""


def pascal_triangle(n):
    """function returning a pascal triangle array based on taken input"""
    if n <= 0:
        return ([])
    if n == 1:
        return ([[1]])
    pascal_triangle_array = [[1], [1, 1]]
    base = [1, 1]
    for i in range(2, n):
        new = []
        for h, n in enumerate(base):
            if (h + 1 < len(base)):
                new.append(n + base[h + 1])
        nb = [1]
        for n in new:
            nb.append(n)
        nb.append(1)
        base = nb
        pascal_triangle_array.append(base)
    return pascal_triangle_array
