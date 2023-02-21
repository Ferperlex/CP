#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ferperlex
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

        leng, k = inlt()

        str = input()
        count = 1
        ind = str.index("*")
        while ind < str.rfind("*"):
            ind = str.rfind("*", ind, ind + k + 1)
            count += 1
        print(count)
