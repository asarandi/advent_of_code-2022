#!/usr/bin/env python3

import functools

with open("input.txt") as fp:
    S = fp.read().strip().split("\n\n")
    fp.close()


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 1 if left > right else 0
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]

    m, n = len(left), len(right)
    if 0 in (m, n):
        return 0 if m == n else -1 if m == 0 else 1

    li, left = left[0], left[1:]
    ri, right = right[0], right[1:]

    ret = compare(li, ri)
    return ret if ret != 0 else compare(left, right)


two, six = [[2]], [[6]]
arr = [two, six]
p1, index = 0, 1
for s in S:
    left, right = map(eval, s.split("\n"))
    arr += [left, right]
    ret = compare(left, right)
    p1 += index if ret == -1 else 0
    index += 1


print(p1)

arr = sorted(arr, key=functools.cmp_to_key(compare))
print((arr.index(two) + 1) * (arr.index(six) + 1))
