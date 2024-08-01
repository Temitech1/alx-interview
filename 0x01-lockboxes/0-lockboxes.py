#!/usr/bin/python3

# Set of unlocked boxes, start with box 0
# Set of available keys, start with keys in box 0

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
