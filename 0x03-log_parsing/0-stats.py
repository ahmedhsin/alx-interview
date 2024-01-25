#!/usr/bin/python3
"""this is a log parser"""
import sys
import re


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

ip_pattern = r'((\d{1,3}\.){0,3}\d{1,3})'
status_pattern = r'"\s(\d{3})\s'
size_pattern = r'"\s\d{3}\s(\d+)'


def printDict():
    print(f'File size: {total_size}')
    for k, v in statstics.items():
        if v > 0:
            print(f'{k}: {v}')


def run():
    global num, total_size
    try:
        for line in sys.stdin:
            num += 1
            ip = re.search(ip_pattern, line)
            status = re.search(status_pattern, line)
            size = re.search(size_pattern, line)
            if status is None or int(status.group(1)) not in statstics:
                continue

            if ip is None or size is None:
                continue
            ip = ip.group(1)
            status = status.group(1)
            size = size.group(1)
            statstics[int(status)] += 1
            total_size += int(size)
            if num % 10 == 0:
                printDict()
    except KeyboardInterrupt:
        printDict()
        raise
    printDict()


if __name__ == "__main__":
    run()
