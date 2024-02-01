#!/usr/bin/python3
"""check utf8 data"""

px = [0b10, 0b0, 0b110, 0b1110, 0b11110]


def is_valid(byte, pattern):
    """check if byte has pattern"""
    if len(bin(byte)) < 10:
        return pattern == 0b0
    elif len(bin(byte)) > 10:
        return False
    if pattern == 0b0:
        return (int(bin(byte)[2:3])) == 0
    elif pattern == 0b110:
        return (int(bin(byte)[2:5])) == 110
    elif pattern == 0b1110:
        return (int(bin(byte)[2:6])) == 1110
    elif pattern == 0b11110:
        return (int(bin(byte)[2:7])) == 11110
    else:
        return (int(bin(byte)[2:4])) == 10


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
