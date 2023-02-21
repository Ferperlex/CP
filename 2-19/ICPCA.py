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

    vt, vfg, vs, vat, vtp = inlt()
    ht, hfg, hs, hat, htp = inlt()

    print(
        (vt * 6 + vfg * 3 + vs * 2 + vat * 1 + vtp * 2),
        (ht * 6 + hfg * 3 + hs * 2 + hat * 1 + htp * 2),
    )
