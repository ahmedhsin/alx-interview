#!/usr/bin/python3
""""solution for lockboxes"""
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]


def helperFunc(boxes, k, keys):
    if len(boxes[k]) == 0:
        return
    for key in boxes[k]:
        tmp = keys.get(key, None)
        valid = tmp is not None or (tmp is not None and tmp >= len(boxes))
        if valid:
            continue
        else:
            keys[key] = True
            helperFunc(boxes, key, keys)


def canUnlockAll(boxes):
    keys = {0: True}
    helperFunc(boxes, 0, keys)
    for i in range(len(boxes)):
        if keys.get(i, None) is None:
            return False
    return True
