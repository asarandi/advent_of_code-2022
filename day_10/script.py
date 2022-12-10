#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

screen, cycles = set(), {20, 60, 100, 140, 180, 220}
cy, x, p1 = 0, 1, 1
for s in S:
    cmd = s[:4]
    for _ in range({"noop": 1, "addx": 2}[cmd]):
        sy, sx = cy // 40, cy % 40
        if sx in (x - 1, x, x + 1):
            screen.add((sy, sx))
        cy += 1
        if cy in cycles:
            p1 += cy * x
    if cmd == "addx":
        x += int(s[5:])

print(p1 - 1)
for y in range(6):
    for x in range(40):
        if (y, x) in screen:
            print("#", end="")
        else:
            print(" ", end="")
    print()
