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

# Windows

import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10**n % 10


"""############ ---- Input Functions ---- ############"""


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
    for _ in range(inp()):
        n = inp()
        li = inlt()
        inc = True
        for i in range(1, n):
            if li[i - 1] > li[i]:
                inc = False
            elif li[i] > li[i - 1] and inc is False:
                print("NO")
                break
        else:
            print("YES")
