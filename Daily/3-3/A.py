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
    print()
