#!/usr/bin/env python3

import re

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

p1, p2 = 0, 0
for s in S:
    a, b, c, d = map(int, re.findall(r"(\d+)", s))
    v, w = set(range(a, b + 1)), set(range(c, d + 1))
    u = v & w
    p1 += 1 if u == v or u == w else 0
    p2 += 1 if len(u) > 0 else 0

print(p1, p2)
