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
                `|`
                 ^
"""

# Windows

import sys
import math

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
    return list(input()[:-1])


def invr():
    return map(int, input().split())


def gcd(a):
    x = 0
    for p in a:
        x = math.gcd(x, p)
    return x


if __name__ == "__main__":
    for _ in range(inp()):
        leng = inp()

        li = inlt()

        even = li[::2]
        odd = li[1::2]

        gcd_e = gcd(even)
        gcd_o = gcd(odd)

        if gcd_o != 0 and all(n % gcd_o != 0 for n in even):
            print(gcd_o)
        elif gcd_e != 0 and all(n % gcd_e != 0 for n in odd):
            print(gcd_e)
        else:
            print(0)
