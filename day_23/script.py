#!/usr/bin/env python3

from math import inf
from collections import defaultdict


def solve(f: str, p1: bool) -> int:
    lines = open(f).read().splitlines()

    positions = set()
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == "#":
                positions.add((y, x))

    neighbors = [(-1, 0), (-1, 1), (-1, -1)]
    neighbors += [(0, -1), (0, 1)]
    neighbors += [(1, 0), (1, 1), (1, -1)]

    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],  # N, NE, NW
        [(1, 0), (1, 1), (1, -1)],  # S, SE, SW
        [(0, -1), (-1, -1), (1, -1)],  # W, NW, SW
        [(0, 1), (-1, 1), (1, 1)],  # E, NE, SE
    ]
    dir_index = 0

    ymin, ymax, xmin, xmax = inf, -inf, inf, -inf
    for round_number in range(10 if p1 else 99999):
        made_moves = False

        propose = defaultdict(list)
        for (y, x) in positions:
            should_move = False
            for (dy, dx) in neighbors:
                sy, sx = y + dy, x + dx
                should_move |= (sy, sx) in positions
            if not should_move:
                continue

            for i in range(4):
                can_move = True
                for (dy, dx) in directions[(dir_index + i) % 4]:
                    sy, sx = y + dy, x + dx
                    can_move &= (sy, sx) not in positions

                if can_move:
                    dy, dx = directions[(dir_index + i) % 4][0]
                    sy, sx = y + dy, x + dx
                    propose[sy, sx].append((y, x))
                    break

        new_positions = set()
        for k, v in propose.items():
            if len(v) == 1:
                made_moves = True
                new_positions.add(k)
                positions.remove(v[0])
        for p in positions:
            new_positions.add(p)

        positions = new_positions
        dir_index = (dir_index + 1) % 4

        if (not p1) and (not made_moves):
            return round_number + 1

    for (y, x) in positions:
        ymin, ymax = min(y, ymin), max(y, ymax)
        xmin, xmax = min(x, xmin), max(x, xmax)

    ct = 0
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            ct += 1 if (y, x) not in positions else 0
    return ct


print(solve("input.txt", True), solve("input.txt", False))
