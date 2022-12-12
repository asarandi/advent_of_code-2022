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

G[S], G[E] = ord("a"), ord("z") + 1


def moves(p: tuple):
    for q in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        step = (p[0] + q[0], p[1] + q[1])
        if step in G and G[step] <= G[p] + 1:
            yield step


def play(starting_points: [tuple]) -> int:
    best = len(F) * len(F[0])
    for sp in starting_points:
        seen, queue = {}, deque([(0, sp)])
        while queue:
            depth, pos = queue.popleft()
            if pos == E:
                best = depth if depth < best else best
                break
            if pos in seen:
                continue
            seen[pos] = True
            for step in moves(pos):
                if step in seen:
                    continue
                queue.append((depth + 1, step))
    return best


print(play([S]), play(candidates))
