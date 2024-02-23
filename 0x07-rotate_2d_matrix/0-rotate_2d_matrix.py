#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def cycle_frame_by_1(matrix, start):
    n = len(matrix)
    temp = -1
    for i in range(start, n - start):
        temp, matrix[start][i] = matrix[start][i], temp

    for i in range(start + 1, n - start):
        temp, matrix[i][n-1-start] = matrix[i][n-1-start], temp

    for i in range(n - 2 - start, start - 1, -1):
        temp, matrix[n - 1 - start][i] = matrix[n - 1 - start][i], temp

    for i in range(n - 2 - start, start, -1):
        temp, matrix[i][start] = matrix[i][start], temp

    temp, matrix[start][start] = matrix[start][start], temp


def rotate_2d_matrix(matrix):
    "rotate 2d martrix func"
    n = len(matrix)
    for layer in range(n // 2):
        for i in range(layer, n - 1 - layer):
            cycle_frame_by_1(matrix, layer)
