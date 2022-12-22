#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read()
    fp.close()

grid, moves = S.rstrip().split("\n\n")
grid = grid.split("\n")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R-D-L-U
dir_ = 0


py, px, found = None, None, False
for y, row in enumerate(grid):
    if found:
        break
    for x, col in enumerate(row):
        if col == ".":
            py, px, found = y, x, True
            break


def move(pypx: tuple) -> tuple:
    (py, px) = pypx
    sy, sx = py, px

    dy, dx = directions[dir_]
    while True:
        sy = sy + dy
        sy %= len(grid)

        if len(grid[sy]) < sx:
            continue

        sx = sx + dx
        sx %= len(grid[sy])

        if grid[sy][sx] == " ":
            continue
        elif grid[sy][sx] == "#":
            return (py, px)
        elif grid[sy][sx] == ".":
            return (sy, sx)
        else:
            assert False


num = ""
for s in moves:
    if s.isdigit():
        num += s
    else:
        by, bx = py, px
        for _ in range(int(num)):
            (py, px) = move((py, px))
        num = ""
        dir_ = (dir_ + {"R": 1, "L": 3}[s]) % 4

for _ in range(int(num)):
    (py, px) = move((py, px))

p1 = 1000 * (py + 1) + 4 * (px + 1) + dir_
print(p1)
