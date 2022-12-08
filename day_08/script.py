#!/usr/bin/env python3

import math

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

G, N, M = {}, len(S), len(S[0])
for r, row in enumerate(S):
    for c, col in enumerate(row):
        G[(r, c)] = int(col)

p1, p2 = 0, 0
for yx, height in G.items():
    y, x = yx
    visible, scores = False, []
    for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        sy, sx = y, x
        vis, ct = True, 0
        while vis:
            sy, sx = sy + i, sx + j
            if not (0 <= sy and sy < N and 0 <= sx and sx < M):
                break
            ct += 1
            vis &= G[(sy, sx)] < height
        visible |= vis
        scores.append(ct)
    p1 += 1 if visible else 0
    p = math.prod(scores)
    p2 = p if p > p2 else p2

print(p1, p2)
