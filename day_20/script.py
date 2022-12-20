#!/usr/bin/env python3

from collections import deque


def solve(p2=False) -> int:
    arr = deque([])
    lst = []
    f = "input.txt"
    for i, s in enumerate(open(f).readlines()):
        e = (i, int(s) * (811589153 if p2 else 1))
        arr.append(e)
        lst.append(e)

    for _ in range(10 if p2 else 1):
        for elem in lst:
            index = arr.index(elem)
            arr.rotate(-index)
            elem = arr.popleft()

            # https://stackoverflow.com/a/3883019/12128712
            val = elem[1] % len(arr)
            arr.rotate(-val)
            arr.appendleft(elem)
            # print([v for (i, v) in arr])

    for index, (i, v) in enumerate(arr):
        if v == 0:
            break

    res = 0
    for j in (1000, 2000, 3000):
        elem = arr[(index + j) % len(arr)]
        # print(elem)
        res += elem[1]
    return res


print(solve(False), solve(True))
