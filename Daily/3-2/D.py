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
import math

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

        my_h, my_d = inlt()
        opp_h, opp_d = inlt()
        coin, upg_d, upg_h = inlt()

        for i in range(coin + 1):

            new_h = my_h + (i * upg_h)
            new_d = my_d + ((coin - i) * upg_d)

            if math.ceil(opp_h / new_d) <= math.ceil(new_h / opp_d):
                print("YES")
                break
        else:
            print("NO")
