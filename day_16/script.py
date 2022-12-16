#!/usr/bin/env pypy3

import re, json
from collections import deque
from math import inf

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()

pat = r"^Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)$"

G, F = {}, {}
for s in S:
    src, flow, dest = re.findall(pat, s).pop()
    G[src] = {k: 1 for k in dest.split(", ")}
    F[src] = int(flow)

for k in G.keys():
    for i in G.keys():
        for j in G.keys():
            G[i][j] = min(G[i].get(j, inf), G[i].get(k, inf) + G[k].get(j, inf))

for key, val in F.items():
    if key != "AA" and val == 0:
        del G[key]
        continue
    for k, v in F.items():
        if v == 0:
            del G[key][k]

# print(json.dumps(obj=G, indent=2, sort_keys=True))


def search(p2=0, max_depth=30, score=0, opened=tuple()):
    seen = {}
    best = -inf
    queue = deque([(0, score, "AA", opened)])
    while queue:
        node = queue.popleft()
        depth, score, name, opened = node

        if node in seen or max_depth < depth:
            continue
        seen[node] = True

        if p2:
            score_p2 = search(0, max_depth, score, opened)
            best = score_p2 if score_p2 > best else best
        else:
            best = score if score > best else best

        if len(opened) == len(G) - 1:
            continue

        for neighbor in G[name]:
            if neighbor not in opened:
                duration = max_depth - (depth + G[name][neighbor] + 1)
                if duration > 0:
                    opened_ = tuple(sorted(list(opened) + [neighbor]))
                    depth_ = depth + G[name][neighbor] + 1
                    score_ = score + duration * F[neighbor]
                    queue.append((depth_, score_, neighbor, opened_))
    return best


print(search(0, 30))
print(search(1, 26))
