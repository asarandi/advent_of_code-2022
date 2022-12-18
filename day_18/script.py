#!/usr/bin/env pypy3

from collections import defaultdict, deque


def get_input(f: str) -> set:
    ret = set()
    for s in open(f).read().splitlines():
        x, y, z = map(int, s.split(","))
        ret.add((x, y, z))
    return ret


def add_vec3(a: tuple, b: tuple) -> tuple:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def add_sides(a: tuple, b: tuple) -> tuple:
    return (
        add_vec3(a[0], b[0]),
        add_vec3(a[1], b[1]),
        add_vec3(a[2], b[2]),
        add_vec3(a[3], b[3]),
    )


def make_cube(xyz: tuple):
    # 0,0,0 => b,l,d corner

    sides = [
        ((0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)),  # f
        ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)),  # b
        ((0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)),  # u
        ((0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)),  # d
        ((1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)),  # r
        ((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)),  # l
    ]

    origin = tuple(xyz for _ in range(4))
    cube = []
    for side in sides:
        new_side = add_sides(origin, side)
        cube.append(new_side)
    return tuple(cube)


def p1(inp: set) -> int:
    all_sides = defaultdict(int)
    for xyz in inp:
        cube = make_cube(xyz)
        for side in cube:
            all_sides[side] += 1
    return sum([v for v in all_sides.values() if v == 1])


def is_within(xyz: tuple) -> bool:
    N = 21
    return (0 <= xyz[0] <= N) and (0 <= xyz[1] <= N) and (0 <= xyz[2] <= N)


def moves(src: tuple) -> [tuple]:
    arr = []
    for t in [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]:
        p = add_vec3(src, t)
        if is_within(p):
            arr.append(p)
    return arr


def p2(inp: set) -> int:
    queue = deque([(0, 0, 0)])
    outside = set()
    while queue:
        xyz = queue.popleft()
        if xyz in outside:
            continue
        outside.add(xyz)
        for m in moves(xyz):
            if m in outside:
                continue
            if m in inp:
                continue
            queue.append(m)

    inside = set()
    for x in range(0, 22):
        for y in range(0, 22):
            for z in range(0, 22):
                xyz = (x, y, z)
                if xyz not in outside:
                    inside.add(xyz)

    return p1(inside)


inp = get_input("input.txt")
print(p1(inp), p2(inp))
