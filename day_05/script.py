#!/usr/bin/env python3

import re

W = ["DTWNL", "HPC", "JMGDNHPW", "LQTNSWC", "NCHP"]
W += ["BQWMDNHT", "LSGJRBM", "TRBVGWNZ", "LPNDGW"]


def play(p1: bool) -> str:
    q = list(map(list, W))
    for s in open("input.txt").read().splitlines():
        n, i, j = map(int, re.findall(r"(\d+)", s))
        i, j = i - 1, j - 1
        t, q[i] = q[i][:n], q[i][n:]
        q[j] = list(reversed(t)) + q[j] if p1 else t + q[j]
    return "".join(s[0] for s in q)


print(play(True), play(False))
