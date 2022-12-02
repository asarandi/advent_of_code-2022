#!/usr/bin/env python3

with open("input.txt") as fp:
    data = fp.read().splitlines()
    fp.close()

A, B, C = 1, 2, 3
win = {B: A, A: C, C: B}
lose = dict(zip(win.values(), win.keys()))


def play(i: int) -> int:
    n = 0
    for s in data:
        L, R = s.strip().split()
        L = {"A": A, "B": B, "C": C}[L]
        R = {"X": (A, win[L]), "Y": (B, L), "Z": (C, lose[L])}[R][i]
        n += 3 if L == R else 6 if win[R] == L else 0
        n += R
    return n


print("part 1:", play(0))
print("part 2:", play(1))
