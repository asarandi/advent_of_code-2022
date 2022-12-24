#!/usr/bin/env python3

from heapq import heappush, heappop
from collections import defaultdict

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

H, W = len(S), len(S[0])
G = defaultdict(list)

for y in range(H):
    for x in range(W):
        if y == 0 and S[y][x] == ".":
            start = (y, x)
        if y == H - 1 and S[y][x] == ".":
            finish = (y, x)
        if S[y][x] == ".":
            continue
        G[y, x] += [S[y][x]]


def t_state(G: dict) -> tuple:
    arr = []
    for k, lst in G.items():
        arr += [(k, tuple(lst))]
    return tuple(sorted(arr))


def step(G: dict) -> dict:
    new_G = defaultdict(list)
    for (y, x), lst in G.items():
        for s in lst:
            if s == "#":
                new_G[y, x] += [s]
                continue
            dy, dx = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[s]
            sy, sx = y + dy, x + dx
            if s == "<" and x == 1 and sx == 0:
                sx = W - 2
            elif s == "^" and y == 1 and sy == 0:
                sy = H - 2
            elif s == ">" and x == W - 2 and sx == W - 1:
                sx = 1
            elif s == "v" and y == H - 2 and sy == H - 1:
                sy = 1
            new_G[sy, sx] += [s]
    return new_G


def moves(curr: tuple, G: dict) -> [tuple]:
    y, x = curr
    if len(G[y, x]) == 0:
        yield y, x

    for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        sy, sx = y + dy, x + dx
        if sy < 0 or H <= sy:
            continue
        if sx < 0 or W <= sx:
            continue
        if len(G[sy, sx]) == 0:
            yield sy, sx


def render(p: tuple, G: dict) -> None:
    for y in range(H):
        for x in range(W):
            arr = G[y, x]
            print(arr[0] if len(arr) == 1 else len(arr), end="")
        print()
    print()


def manhattan(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


bliz_set = set()
bliz_arr = []

queue = [G]
while queue:
    bliz, queue = queue[0], queue[1:]
    t = t_state(bliz)
    if t in bliz_set:
        continue
    bliz_set.add(t)
    bliz_arr.append(bliz)
    queue.append(step(bliz))


def solve(p2: bool) -> int:
    route = [(start, finish)]
    if p2:
        route += [(finish, start), (start, finish)]

    bliz_index = 0
    results = [0, 0, 0]

    for index, (src, dst) in enumerate(route):
        s = (0, 0, src, bliz_index)
        queue = [s]
        seen = set()
        while queue:
            node = heappop(queue)
            fscore, depth, position, bindex = node
            if (depth, position) in seen:
                continue
            seen.add((depth, position))
            if position == dst:
                results[index] = depth
                bliz_index = bindex
                break
            for new_position in moves(position, bliz_arr[bindex % len(bliz_arr)]):
                distance = manhattan(new_position, dst)
                fscore = distance + depth + 1
                heappush(queue, (fscore, depth + 1, new_position, bindex + 1))

    return sum(results) - 1


print(solve(False), solve(True))
