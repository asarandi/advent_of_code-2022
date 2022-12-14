#!/usr/bin/env python3


def get_data(f: str) -> ({}, int):
    G, D = {}, 0
    for s in open(f).readlines():
        s = s.split(" -> ")
        (px, py) = (None, None)
        for lst in map(lambda c: c.split(","), s):
            (x, y) = tuple(map(lambda i: int(i), lst))
            D = y if y > D else D
            if not px:
                (px, py) = (x, y)
                continue
            if x == px:
                for i in range(min(y, py), max(y, py) + 1):
                    G[(x, i)] = "#"
            else:
                for i in range(min(x, px), max(x, px) + 1):
                    G[(i, y)] = "#"
            (px, py) = (x, y)
    return G, D


def sink(G: {}, D: int, src: tuple) -> bool:
    x, y = src
    if y > D or src in G:
        return False

    for dst in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if not dst in G:
            return sink(G, D, dst)
    G[src] = "o"
    return True


def solve(p2: bool) -> int:
    G, D = get_data("input.txt")
    if p2:
        D += 2
        for i in range(-999, 999):
            G[(i, D)] = "#"
    ct = 0
    while sink(G, D, (500, 0)):
        ct += 1
    return ct


print(solve(False), solve(True))
