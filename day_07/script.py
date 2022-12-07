#!/usr/bin/env python3

from collections import defaultdict

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

path, seen = [], defaultdict(int)
for s in S:
    args = s.split()
    if s == "$ cd ..":
        path.pop()
    elif s.startswith("$ cd "):
        path.append(args[2])
    elif args[0].isdigit():
        n = int(args[0])
        for i in range(1, len(path) + 1):
            seen["/".join(path[:i])] += n

print(sum([i for i in seen.values() if i <= 100_000]))
print(min([i for i in seen.values() if seen["/"] - 40_000_000 <= i]))
