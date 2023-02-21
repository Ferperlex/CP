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
    s = {0}
    dupes = {}
    for _ in range(inp()):
        ch, n = inli()
        n = int(n)

        if ch == "+":
            s.add(n)
        else:
            # print(s, n)
            cp = n
            if n in dupes:
                cp = dupes.get(n)

            while cp in s:
                cp += n
            dupes[n] = cp
            print(cp)
