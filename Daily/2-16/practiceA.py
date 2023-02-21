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

    li = [2, 1]

    leng = inp()
    curr = 2
    if leng < 3:
        print(*li[:leng])
    else:
        for i in range(leng - 2):
            # print(li, i, curr+i-2, curr+)
            li.append(li[curr + i - 2] + li[curr + i - 1])
        print(*li)
