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


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def dfs(x, y, s, n, dir):
    if n == 0:
        s.add((x, y))
    else:
        if dir == 0 or dir == -1:
            dfs(x, y + 1, s, n - 1, 1)
            dfs(x, y - 1, s, n - 1, 1)
        if dir == 1 or dir == -1:
            dfs(x + 1, y, s, n - 1, 0)
            dfs(x - 1, y, s, n - 1, 0)


if __name__ == "__main__":

    n = inp()

    # seen = set()
    # dfs(0, 0, seen, n, -1)
    # print(len(seen))

    print((n % 2 + 1) * ((n + 4) // 2 - 1) * (n - n // 2 + 1))
