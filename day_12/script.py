#!/usr/bin/env python3

from collections import deque

with open("input.txt") as fp:
    F = fp.read().splitlines()
    fp.close()

G, S, E, candidates = {}, None, None, []
for y, row in enumerate(F):
    for x, col in enumerate(row):
        G[(y, x)] = ord(col)
        S = (y, x) if col == "S" else S
        E = (y, x) if col == "E" else E
        candidates += [(y, x)] if col == "a" else []

G[S], G[E] = ord("a"), ord("z")


def moves(p: tuple):
    for q in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        step = (p[0] + q[0], p[1] + q[1])
        if step in G and G[step] <= G[p] + 1:
            yield step


def play(yx: [tuple]) -> int:
    seen, queue = {}, deque(map(lambda p: (0, p), yx))
    while queue:
        depth, point = queue.popleft()
        if point == E:
            return depth
        if point in seen:
            continue
        seen[point] = True
        for step in moves(point):
            if step in seen:
                continue
            queue.append((depth + 1, step))


print(play([S]), play(candidates))
