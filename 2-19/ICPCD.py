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

    n = insr()
    total = 0
    for i, num in enumerate(reversed(n)):
        total += int(num) * ((3 / 2) ** i)
    n, d = (total - total // 1).as_integer_ratio()

    if n == 0:
        print(int(total // 1))
    else:
        print(int(total // 1), str(n) + "/" + str(d))
