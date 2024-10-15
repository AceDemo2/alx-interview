#!/usr/bin/python3
"""pascal_tri"""


def pascal_triangle(n):
    """define func"""

    if n <= 0:
        return []
    res = [[1]]
    for i in range(1, n):
        val = [1] * (i + 1)
        for j in range(1, i):
            val[j] = res[i-1][j-1] + res[i-1][j]
        res.append(val)
    return res
