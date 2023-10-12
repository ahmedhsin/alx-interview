#!/usr/bin/python3
""""solution for minop"""


def minOperations(n):
    """min op"""
    counter = 0
    while (n != 1):
        for i in range(2, n):
            if n % i == 0:
                counter += i
                n /= i
                continue
        counter += n
        break
    return int(counter)
