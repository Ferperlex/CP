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
from collections import deque

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
    li = []

    for _ in range(inp()):

        _, top, _, bottom = inlt()
        li.append((bottom, top))

    li.sort()
    # lims = deque[li]
    # print(lims)
    stack = deque([(0, maxint())])
    first = 0
    second = 0
    curr = 0
    uniques = set(li)

    for b, t in li:
        print(stack, curr, (b, t))
        if not b <= stack[-1][1]:
            if curr > first:
                second = first
                first = curr
            elif curr > second:
                second = curr

        while not (b <= stack[-1][1]):

            stack.pop()
            curr -= 1

        if b <= stack[-1][1]:
            if t < stack[-1][1]:
                stack.append((b, t))
            else:
                stack.append((b, stack[-1][1]))
            curr += 1

        # else:

    print(first, second)
