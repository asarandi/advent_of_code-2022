#!/usr/bin/env python3

import re
from math import inf
from collections import deque


def get_input(f: str) -> [tuple]:
    arr = []
    with open(f) as fp:
        for s in fp.read().strip().splitlines():
            t = tuple(map(int, re.findall(r"(\d+)", s)))
            arr.append(t)
    return arr


def search(inp: [tuple]):
    def moves(blueprint: tuple, node: tuple, max_depth: int, best: int) -> tuple:
        id_, b0r0, b1r0, b2r0, b2r1, b3r0, b3r2 = blueprint

        # (resource_index, resource_amount)
        # order is same as robots it produces
        costs = [
            [(4, b0r0)],
            [(4, b1r0)],
            [(4, b2r0), (5, b2r1)],
            [(4, b3r0), (6, b3r2)],
            [(4, inf)],  # noop
        ]

        geobots, geodes = node[3], node[7]
        for _ in range(max_depth - node[-1]):
            geodes += geobots
            geobots += 1

        if geodes < best:
            return []

        arr = []
        for index, rsrc in enumerate(costs):
            # b0, b1, b2, b3, --- r0, r1, r2, r3 --- depth
            lst = list(node)

            max_needed = [max(b0r0, b1r0, b2r0, b3r0), b2r1, b3r2]

            lst[0] = min(lst[0], max_needed[0])
            lst[1] = min(lst[1], max_needed[1])
            lst[2] = min(lst[2], max_needed[2])

            new_robots = [0, 0, 0, 0]

            can_build = True
            for (idx, amount) in rsrc:
                can_build &= amount <= lst[idx]

            if index in (0, 1, 2):
                if lst[index] == max_needed[index]:
                    can_build = False

            if can_build:
                for (idx, amount) in rsrc:
                    lst[idx] -= amount
                new_robots[index] += 1

            for i, val in enumerate(new_robots):
                lst[i + 4] += lst[i]  # new resources
                lst[i] += val  # new robots

            lst[-1] += 1  # depth
            arr.append(tuple(lst))

        return arr

    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

    part1 = 0
    part2 = 1

    max_depth = 32
    for blueprint in inp[:3]:
        # b0, b1, b2, b3, --- r0, r1, r2, r3 --- depth
        queue = deque([tuple([1, 0, 0, 0, 0, 0, 0, 0, 0])])
        seen = {}
        best = 0
        while queue:
            node = queue.popleft()

            if node[-1] > max_depth:
                continue

            if node in seen:
                continue
            seen[node] = True

            depth = node[-1]
            new_best = node[-2]

            if new_best > best:
                best = new_best
                print(
                    "blueprint",
                    blueprint[0],
                    "best",
                    best,
                    "depth",
                    depth,
                    "node",
                    node,
                )

            for move in moves(blueprint, node, max_depth, best):
                queue.append(move)

        print(best)
        part1 += best * blueprint[0]
        part2 *= best
    return part2


inp = get_input("input.txt")
print("part 2:", search(inp))
