#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ferperlex
            _
       ----(O)
             \
              \_
              ( `'--.,
               `,___/
                 |_\.
                /|
                `|`
                 ^
"""


import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10 ** n % 10


"""############ ---- Input Functions ---- ############"""


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def inli():
    return list(input().split())


def insr():
    return list(input()[:-1])


def invr():
    return map(int, input().split())


if __name__ == "__main__":
    for _ in range(inp()):
        li = inlt()

        if (
            li[0] == li[1] + li[2]
            or li[1] == li[0] + li[2]
            or li[2] == li[0] + li[1]
            or (li[0] == li[1] and li[2] % 2 == 0)
            or (li[0] == li[2] and li[1] % 2 == 0)
            or (li[1] == li[2] and li[0] % 2 == 0)
        ):
            print("YES")
        else:
            print("NO")
