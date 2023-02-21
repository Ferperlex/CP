#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys

input = sys.stdin.readline

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

        n, m, k = inlt()

        if (
            (k == 2 and n == 1 and m == 0)
            or (k == 3 and m == (((n) * (n - 1)) // 2))
            or (k > 3 and m >= n - 1 and m <= (((n) * (n - 1)) // 2))
        ):
            print("YES")
        else:
            print("NO")
