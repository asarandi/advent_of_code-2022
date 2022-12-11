#!/usr/bin/env python3

import math

with open("input.txt") as fp:
    S = fp.read()
    fp.close()

monkeys = {}
for s in S.split("\n\n"):
    s = s.split("\n")
    num = int(s[0][7:8])
    items = [int(n) for n in s[1][18:].split(", ")]
    op = eval(s[2][17:].replace("=", "lambda old:"))
    div = int(s[3][21:])
    throw = {True: int(s[4][29:]), False: int(s[5][30:])}
    monkeys[num] = {"items": items, "op": op, "div": div, "throw": throw}

lcm = math.lcm(*map(lambda i: i["div"], monkeys.values()))


def play(p1: bool) -> int:
    res = [0 for _ in range(len(monkeys))]
    for _ in range(20 if p1 else 10000):
        for i in range(len(monkeys)):
            attr = monkeys[i]
            for item in attr["items"]:
                worry = attr["op"](item)
                worry = worry // 3 if p1 else worry % lcm
                throw = attr["throw"][worry % attr["div"] == 0]
                monkeys[throw]["items"] += [worry]
                res[i] += 1
            attr["items"] = []
            monkeys[i] = attr
    return math.prod(sorted(res)[-2:])


print(play(True), play(False))
