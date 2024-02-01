#!/usr/bin/python3
"""check utf8 data"""

px = [0b10, 0b0, 0b110, 0b1110, 0b11110]


def is_valid(byte, pattern):
    """check if byte has pattern"""
    mask = 1 << 7
    for _ in range(pattern):
        if not (byte & mask):
            return False
        mask >>= 1
    return not (byte & mask)


def valid(data, pattern, i, stop):
    if not stop:
        return i
    if i >= len(data) or not is_valid(data[i], pattern):
        return -1
    return valid(data, px[0], i + 1, stop - 1)


def validUTF8(data):
    """determine if this is a correct incoded in utf8"""
    index = 0
    i = 1
    while i < len(px) - 1:
        # print(index, i)
        index = valid(data, px[i], index, i)
        # print(index, px[i], i)
        if index == len(data):
            return True
        elif index == -1:
            i = i + 1
        else:
            i = 1
    return False
