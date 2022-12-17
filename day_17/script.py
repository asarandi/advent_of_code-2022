#!/usr/bin/env pypy3

with open("input.txt") as fp:
    S = fp.read().strip()
    fp.close()

jet_index = 0
shape_index = 0
shapes = [
    0b_1111_0000_0000_0000,
    0b_0100_1110_0100_0000,
    0b_0010_0010_1110_0000,
    0b_1000_1000_1000_1000,
    0b_1100_1100_0000_0000,
]
chars = ["#", "@", "x", "o", "*"]

highest = 0

G = {}


def jet_push() -> int:
    global jet_index
    ret = -1 if S[jet_index] == "<" else 1
    jet_index = (jet_index + 1) % len(S)
    return ret


def next_shape_width():
    return [4, 3, 3, 1, 2][shape_index]


def next_shape_height():
    return [1, 3, 3, 4, 2][shape_index]


def can_place(y, x) -> bool:
    s = shapes[shape_index]
    for i in range(4):
        for j in range(4):
            bit = 1 << ((3 - i) * 4 + 3 - j)
            if bit & s:
                if (y + i, x + j) in G:
                    return False
    return True


def place(y, x):
    global highest, shape_index
    s = shapes[shape_index]
    for i in range(4):
        for j in range(4):
            bit = 1 << ((3 - i) * 4 + 3 - j)
            if bit & s:
                G[(y + i, x + j)] = chars[shape_index]
                highest = min(y + i, highest)
    shape_index = (shape_index + 1) % 5


def simulate():
    h = next_shape_height()
    w = next_shape_width()
    x = 2
    y = highest - 3 - h
    while True:
        j = jet_push()
        if 0 <= x + j < 7:
            if x + j + w <= 7:
                if can_place(y, x + j):
                    x += j
        if 0 > y + h and can_place(y + 1, x):
            y += 1
        else:
            place(y, x)
            break


arr = []
prev = 0
N = 2022  # 500000
for i in range(N):
    simulate()
    curr = -highest
    arr.append(curr - prev)
    prev = curr

print(-highest)

# solved p2 manually:
# for sample, repeating pattern of lenght 35, +53 points per pattern
# for input, pattern of length 1700, +2642 points per pattern


# plen = 1700
# M = 250000
# p = arr[M : M + plen]
# for i in range(M + plen, N - plen):
#     s = arr[i : i + plen]
#     if tuple(s) == tuple(p):
#         print("found", i, sum(s))
#         break
#
#
#    for y in range(-10, 0):
#        for x in range(0, 7):
#            print(G[(y,x)] if (y, x) in G else ".", end="")
#        print()
#
#    print()
#
# print(G)
