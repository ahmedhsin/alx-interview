#!/usr/bin/python3
""""solution for minop"""


def minOperations(n):
    """min op"""
    if type(n) == float or n <= 0:
        return 0
    counter = 0
    while (n != 1):
        ok = False
        for i in range(2, n):
            if n % i == 0:
                counter += i
                n //= i
                ok = True
                break
        if not ok:
            counter += n
            break
    return counter
