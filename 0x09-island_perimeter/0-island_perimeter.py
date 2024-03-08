#!/usr/bin/python3
"""sol of the island problem"""


def calc_perimeter(grid, i, j):
    """calculate per for a unit"""
    cnt = 0
    if i + 1 < len(grid):
        cnt += 1 if grid[i + 1][j] == 0 else 0
    if i - 1 >= 0:
        cnt += 1 if grid[i - 1][j] == 0 else 0
    if j - 1 >= 0:
        cnt += 1 if grid[i][j - 1] == 0 else 0
    if j + 1 < len(grid[0]):
        cnt += 1 if grid[i][j + 1] == 0 else 0
    return cnt


def island_perimeter(grid):
    """island_per function"""
    n = len(grid)
    m = len(grid[0])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cnt += calc_perimeter(grid, i, j)
    return cnt
