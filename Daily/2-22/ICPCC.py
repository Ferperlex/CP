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
    for _ in range(inp()):
        n = inp()
        li = inlt()

        li = [(li[i], i + 1) for i in range(n)]
        li.sort(reverse=True)

        returned = [0] * (n + 1)
        count = 0
        total = 0
        for num, i in li:
            if count % 2 == 0:
                returned[i] = count // 2 + 1
            else:
                returned[i] = -1 * (count // 2 + 1)
            total += 2 * (count // 2 + 1) * num
            count += 1
        print(total)
        print(*returned)
