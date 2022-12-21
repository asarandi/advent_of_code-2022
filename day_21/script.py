#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

G = {}
for s in S:
    s = s.split(": ")
    k = s[0]
    v = s[1].split()
    G[k] = tuple(v)


def search(k: str, humn=None) -> int:
    val = G[k]
    if humn and k == "humn":
        val = (str(humn),)

    if len(val) == 1:
        return val[0]

    left, op, right = val
    if not left.isdigit():
        left = search(left, humn)
    if not right.isdigit():
        right = search(right, humn)

    if humn and k == "root":
        l, r = int(left), int(right)
        return -1 if l > r else 1 if l < r else 0
    return str(int(eval(" ".join([left, op, right]))))


def part1():
    return search("root")


def part2():
    left, right = 0, 40000000000000
    while left <= right:
        mid = (left + right) // 2
        ret = search("root", mid)
        if ret == -1:
            left = mid + 1
        elif ret == 1:
            right = mid - 1
        else:
            return mid


print(part1(), part2())
