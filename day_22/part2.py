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


N = 50


def get_region(t: tuple) -> int:
    regions = [
        [0, 1, 2],
        [0, 3, 0],
        [4, 5, 0],
        [6, 0, 0],
    ]
    (y, x) = t
    return regions[y // N][x // N]


#  ..1122
#  ..1122
#  ..33..
#  ..33..
#  4455..
#  4455..
#  66....
#  66....


def move(p: tuple, dir_: int) -> tuple:
    (oy, ox) = p
    (y, x) = p
    odir = dir_

    r = get_region(p)
    d = "RDLU"[dir_]

    if r == 1 and d == "L" and x % N == 0:
        y = (2 * N) + (N - (y % N) - 1)
        x = 0
        d = "R"

    elif r == 1 and d == "U" and y % N == 0:
        y = (3 * N) + (x % N)  #
        x = 0
        d = "R"

    elif r == 2 and d == "R" and x % N == N - 1:
        y = (2 * N) + (N - (y % N) - 1)
        x = (2 * N) - 1
        d = "L"

    elif r == 2 and d == "D" and y % N == N - 1:
        y = N + (x % N)
        x = (2 * N) - 1
        d = "L"

    elif r == 3 and d == "R" and x % N == N - 1:
        x = (2 * N) + (y % N)
        y = N - 1
        d = "U"

    elif r == 3 and d == "L" and x % N == 0:
        x = y % N
        y = 2 * N
        d = "D"

    elif r == 4 and d == "L" and x % N == 0:
        y = N - (y % N) - 1
        x = N
        d = "R"

    elif r == 4 and d == "U" and y % N == 0:
        y = N + (x % N)
        x = N
        d = "R"

    elif r == 5 and d == "R" and x % N == N - 1:
        y = N - (y % N) - 1
        x = (3 * N) - 1
        d = "L"

    elif r == 5 and d == "D" and y % N == N - 1:
        y = (3 * N) + (x % N)
        x = N - 1
        d = "L"

    elif r == 6 and d == "R" and x % N == N - 1:
        x = N + (y % N)
        y = (3 * N) - 1
        d = "U"

    elif r == 6 and d == "L" and x % N == 0:
        x = N + (y % N)
        y = 0
        d = "D"

    else:
        if r == 6 and d == "D" and y % N == N - 1:
            x = (2 * N) + x
            y = 0

        elif r == 2 and d == "U" and y % N == 0:
            y = (4 * N) - 1
            x = x - (2 * N)

        else:
            sy, sx = directions[dir_]
            y, x = y + sy, x + sx

    dir_ = "RDLU".index(d)
    r = get_region((y, x))
    #    print(oy, ox, odir, y, x)
    assert 1 <= r <= 6

    if grid[y][x] == "#":
        return (oy, ox), odir
    elif grid[y][x] == ".":
        return (y, x), dir_
    else:
        assert False


num = ""
for s in moves:
    if s.isdigit():
        num += s
    else:
        by, bx = py, px
        for _ in range(int(num)):
            (py, px), dir_ = move((py, px), dir_)
        num = ""
        dir_ = (dir_ + {"R": 1, "L": 3}[s]) % 4

for _ in range(int(num)):
    (py, px), dir_ = move((py, px), dir_)

p2 = 1000 * (py + 1) + 4 * (px + 1) + dir_
print(p2)
