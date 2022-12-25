#!/usr/bin/env python3

with open("input.txt") as fp:
    S = fp.read().splitlines()
    fp.close()


def stoi(s: str) -> int:
    n = len(s)
    i = 0
    for index, char in enumerate(s):
        j = 5 ** (n - index - 1)
        if char in "012":
            i += j * int(char)
        else:
            i += j * {"-": -1, "=": -2}[char]
    return i


def itos(i: int) -> str:
    # balanced quinary numeral system
    # https://www.ias.ac.in/article/fulltext/reso/023/12/1395-1410
    result = ""
    while i:
        remainder = i % 5
        i = i // 5
        if remainder <= 2:
            result = str(remainder) + result
        else:
            result = "-="[4 - remainder] + result
            i += 1  # carry
    return result


if __name__ == "__main__":
    i = 0
    for s in S:
        i += stoi(s)

    print(itos(i))
    assert i == stoi(itos(i))
