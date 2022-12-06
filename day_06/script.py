#!/usr/bin/env python3


def play(n: int):
    s = open("input.txt").read().strip()
    for i in range(n, len(s)):
        p = set(list(s[i - n : i]))
        if len(p) == n:
            return i


print(play(4), play(14))
