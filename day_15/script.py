#!/usr/bin/env python3

import re

# f = "sample.txt"
# p1_row = 10
# p2_range = 20

f = "input.txt"
p1_row = 2_000_000
p2_range = 4_000_000

G = {}
for s in open(f).readlines():
    sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", s))
    G[(sx, sy)] = abs(sx - bx) + abs(sy - by)

for y in range(p2_range):
    intervals = []
    for (sx, sy), distance in G.items():
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

    if y == p1_row:
        assert len(merged) == 1
        left, right = merged.pop()
        print("part 1:", right - left)

    if len(merged) > 1:
        assert len(merged) == 2
        assert (merged[0][1] + 1) == (merged[1][0] - 1)
        x = merged[0][1] + 1

        print("part 2:", x * 4_000_000 + y)
        break
