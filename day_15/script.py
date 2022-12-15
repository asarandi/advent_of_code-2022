#!/usr/bin/env python3

import re
from math import inf


def manhattan(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# f = "sample.txt"
# p1_row = 10
# p2_range = 20


f = "input.txt"
p1_row = 2_000_000
p2_range = 4_000_000


G, D = {}, {}
for s in open(f).readlines():
    sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", s))
    src, dst = (sx, sy), (bx, by)
    G[src], G[dst] = "S", "B"
    D[src] = manhattan(src, dst)

xmin, ymin, xmax, ymax = inf, inf, -inf, -inf
for (sx, sy), distance in D.items():
    xmin = min(sx - distance, xmin)
    ymin = min(sy - distance, ymin)
    xmax = max(sx + distance, xmax)
    ymax = max(sy + distance, ymax)

y, count = p1_row, set()
for x in range(xmin, xmax + 1):
    point = (x, y)
    for sensor, distance in D.items():
        if manhattan(sensor, point) <= distance:
            if point not in G:
                count.add(point)
                break

print(len(count))

for y in range(p2_range):
    intervals = []
    for (sx, sy), distance in D.items():
        length = abs(sy - y)
        if distance <= length:
            continue
        delta = distance - length
        intervals += [(sx - delta, sx + delta)]

    intervals.sort()

    merged = []
    for (curr_left, curr_right) in intervals:
        if not merged:
            # first pair
            merged = [(curr_left, curr_right)]
            continue

        # avoid [..., (_, 5), (6, _), ...
        if curr_left > merged[-1][1] + 1:
            merged += [(curr_left, curr_right)]
            continue

        prev_left, prev_right = merged.pop()
        merged += [(prev_left, max(prev_right, curr_right))]

    if len(merged) > 1:
        assert len(merged) == 2
        assert (merged[0][1] + 1) == (merged[1][0] - 1)
        x = merged[0][1] + 1

        print(x * 4_000_000 + y)
        break
