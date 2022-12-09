#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sign = lambda n: 1 if n > 0 else -1 if n < 0 else 0


def play(N: int) -> int:
    seen = set()
    knots = [(0, 0) for _ in range(N)]
    for s in S:
        dir_, num = s.split()
        step = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[dir_]
        for _ in range(int(num)):
            knots[0] = add(knots[0], step)
            for i in range(len(knots) - 1):
                head, tail = knots[i], knots[i + 1]
                dy = head[0] - tail[0]
                dx = head[1] - tail[1]
                if 2 <= abs(dy) or 2 <= abs(dx):
                    knots[i + 1] = add(tail, (sign(dy), sign(dx)))
            seen.add(knots[-1])
    return len(seen)


print(play(2), play(10))
