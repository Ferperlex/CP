#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ferperlex
            _
       ----(O)
             \.
              \_
              ( `'--.,
               `,___/
                 |_\.
                /|
                `|
                 ^
"""
import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10 ** n % 10


############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def inli():
    return list(input().split())


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


if __name__ == "__main__":

    work = {
        "1110111"[::-1],
        "0010010"[::-1],
        "1011101"[::-1],
        "1011011"[::-1],
        "0111010"[::-1],
        "1101011"[::-1],
        "1101111"[::-1],
        "1010010"[::-1],
        "1111111"[::-1],
        "1111011"[::-1],
        "1111110"[::-1],
        "0101111"[::-1],
        "1100101"[::-1],
        "0011111"[::-1],
        "1101101"[::-1],
        "1101100"[::-1],
    }

    s, seq = inlt()
    seq = str(seq)

    perline = (80 + 2 * s) // (s * 5)

    if (
        li[0] == li[1] + li[2]
        or li[1] == li[0] + li[2]
        or li[2] == li[0] + li[1]
        or true
    ):
        print("YES")
    else:
        print("NO")

    line = []
    count = 0

    if len(seq) % 7 != 0:
        n = 7 - (len(seq) % 7)
        seq = "0" * (n) + seq
    for i in range(len(seq) // 7):

        count += 1

        mat = [[" " for col in range(s * 3)] for row in range(s * 7)]

        curr = seq[i * 7 : i * 7 + 7]

        if curr not in work:
            # for r in mat:
            #     print(*r, sep="")
            thing = 1

        else:
            for ind, n in enumerate(curr):
                if n == "1":
                    # reversed: 0 -> 6
                    if ind == 0:
                        for diff in range(s):
                            mat[-1 * (diff + 1)] = ["X"] * (s * 3)
                    elif ind == 6:
                        for diff in range(s):
                            mat[diff] = ["X"] * (s * 3)
                    elif ind == 3:
                        for diff in range(s):
                            mat[s * 3 + diff] = ["X"] * (s * 3)
                    elif ind == 5:
                        for x in range(s):
                            for y in range(2 * s):
                                mat[y + s][x] = "X"
                    elif ind == 4:
                        for x in range(s):
                            for y in range(2 * s):
                                mat[y + s][-1 * (x + 1)] = "X"
                    elif ind == 2:
                        for x in range(s):
                            for y in range(2 * s):
                                mat[4 * s + y][x] = "X"
                    elif ind == 1:
                        for x in range(s):
                            for y in range(2 * s):
                                mat[4 * s + y][-1 * (x + 1)] = "X"
        line.append(mat)
        if count >= perline:
            for row in range(7 * s):
                for twod in range(len(line)):
                    for col in range(s * 3):
                        print(line[twod][row][col], end="")
                    print(" " * 2 * s, end="")
                print()
            for _ in range(s):
                print()

            line = []
            count = 0

    for row in range(7 * s):
        for twod in range(len(line)):
            for col in range(s * 3):
                print(line[twod][row][col], end="")
            print(" " * 2 * s, end="")
        print()
