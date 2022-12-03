#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

p1, p2 = 0, 0
f = lambda s: set(list(s))
g = lambda c: ord(c) - 96 if "a" <= c else ord(c) - 38
for i, s in enumerate(S):
    n = len(s) // 2
    u = f(s[:n]) & f(s[n:])
    p1 += g(u.pop())
    if i % 3 == 2:
        u = f(s) & f(S[i - 1]) & f(S[i - 2])
        p2 += g(u.pop())

print(p1)
print(p2)
