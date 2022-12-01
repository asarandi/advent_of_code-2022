#!/usr/bin/env python3

with open("input.txt") as fp:
    arr = fp.read().split("\n\n")
    fp.close()

arr = [[int(i) for i in s.splitlines()] for s in arr]
arr = sorted(list(map(sum, arr)))

print("part 1:", arr[-1])
print("part 2:", sum(arr[-3:]))
