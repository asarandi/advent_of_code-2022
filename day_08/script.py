#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

G, N, M = {}, len(S), len(S[0])
for r, row in enumerate(S):
    for c, col in enumerate(row):
        G[(r, c)] = int(col)

p1, p2 = 0, 0
for (y, x), height in G.items():
    visible, score = False, 1
    for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        sy, sx = y, x
        vis, ct = True, 0
        while vis:
            sy, sx = sy + i, sx + j
            if not (0 <= sy < N and 0 <= sx < M):
                break
            ct += 1
            vis &= G[(sy, sx)] < height
        visible |= vis
        score *= ct
    p1 += 1 if visible else 0
    p2 = score if score > p2 else p2

print(p1, p2)
