#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

p1, cy, x, G = 0, 0, 1, set()
for s in S:
    for _ in range({"noop": 1, "addx": 2}[s[:4]]):
        sy, sx, cy = cy // 40, cy % 40, cy + 1
        G.add((sy, sx) if sx in (x - 1, x, x + 1) else -1)
        p1 += cy * x if cy in (20, 60, 100, 140, 180, 220) else 0
    x += int(s[5:]) if s[:4] == "addx" else 0

print(p1)
for y in range(6):
    for x in range(40):
        print("#" if (y, x) in G else " ", end="\n" if x == 39 else "")
