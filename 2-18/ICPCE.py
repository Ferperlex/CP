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


# import time

if __name__ == "__main__":

    for _ in range(inp()):

        n, k = inlt()
        li = inlt()

        mini = li[0] / (n - k + 1)
        curr = li[0]
        ended = False

        for i in li[1:]:
            if i - curr < mini:
                ended = True
                break
            else:
                mini = i - curr
                curr = i
        if ended:
            print("NO")
        else:
            print("YES")
