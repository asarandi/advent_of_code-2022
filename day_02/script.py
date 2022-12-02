#!/usr/bin/env python3

with open("input.txt") as fp:
    data = fp.read().splitlines()
    fp.close()

rock = "rock"
paper = "paper"
scissors = "scissors"

shapes = {rock: 1, paper: 2, scissors: 3}
win = {paper: rock, rock: scissors, scissors: paper}
lose = dict(zip(win.values(), win.keys()))


def play(f: bool) -> int:
    n = 0
    for s in data:
        l, r = s.strip().split()
        l = {"A": rock, "B": paper, "C": scissors}[l]

        if f:
            r = {"X": rock, "Y": paper, "Z": scissors}[r]
        else:
            r = {"X": win[l], "Y": l, "Z": lose[l]}[r]

        n += shapes[r]

        if l == r:
            n += 3
        elif win[r] == l:
            n += 6
    return n


print("part 1:", play(True))
print("part 2:", play(False))
