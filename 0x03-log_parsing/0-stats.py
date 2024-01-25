#!/usr/bin/python3
"""this is a log parser"""
import sys


total_size = 0
num = 0
statstics = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0}


def printDict():
    print(f'File size: {total_size}')
    for k, v in sorted(statstics.items()):
        if v > 0:
            print(f'{k}: {v}')


def run():
    global num, total_size
    try:
        for line in sys.stdin:
            num += 1
            data = line.split()
            if len(data) != 9:
                continue
            try:
                sc = int(data[-2])
                if sc in statstics:
                    statstics[sc] += 1
            except Exception:
                pass
            try:
                total_size += int(data[-1])
            except Exception:
                pass
            if num % 10 == 0:
                printDict()
    except KeyboardInterrupt:
        printDict()
        raise
    printDict()


if __name__ == "__main__":
    run()
