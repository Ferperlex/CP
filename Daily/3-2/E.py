#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ferperlex
            _
       ----(O)
             \
              \
              ( `'--.,
               `,___/
                 |_\
                /|
                `|`
                 ^
"""


import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize


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

        l = list(map(int, input()[:-1]))

        m = l[-1]

        li = []
        for n in reversed(l):

            m = min(n, m)

            if m < n:
                li.append(min(9, n + 1))
            else:
                li.append(n)

        li.sort()

        for n in li:
            print(min(9, n), end="")
        print()
