#!/usr/bin/python3
# solve for pascal problem

def pascal_triangle(n):
    """solve pascal problem iterative way"""
    if n <= 0:
        return []
    pascal = [[1], [1, 1]]
    if n == 1:
        return [pascal[0]]
    elif n == 2:
        return pascal
    n -= 2
    for i in range(n):
        tmp = [1]
        for j in range(len(pascal[-1]) - 1):
            current = pascal[-1][j] + pascal[-1][j+1]
            tmp.append(current)
        tmp.append(1)
        pascal.append(tmp)
    return pascal
