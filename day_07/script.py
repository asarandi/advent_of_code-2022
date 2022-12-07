#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

S += ["$ cd .."]

path, size = [], []
seen = {}

for s in S:
    z = s.split()
    if s == "$ cd ..":
        n = size.pop()
        size[-1] += n
        p = "/".join(path)
        seen[p] = n
        path.pop()
    elif s.startswith("$ cd "):
        path.append(z[2])
        size.append(0)
    elif z[0].isdigit():
        n = int(z[0])
        size[-1] += n

p1 = sum(filter(lambda s: s <= 100000, seen.values()))
p2 = min(filter(lambda s: size[0] - 40000000 <= s, seen.values()))
print(p1, p2)
