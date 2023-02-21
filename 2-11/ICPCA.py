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

    for _ in range(inp()):

        leng = inp()

        li = inlt()
        returned = deque([])

        l = 0
        r = leng - 1
        count = 0
        maxi = maxint()
        ended = False

        while l <= r:

            chosen = max(li[l], li[r])

            if li[l] == chosen:
                returned.appendleft(chosen)
                l += 1
            else:
                returned.append(chosen)
                r -= 1

            if chosen > maxi:
                print(-1)
                ended = True
                break

            if count == 0:
                maxi = chosen

            count += 1
        if not ended:
            for n in returned:
                print(n, end=" ")
            print()
