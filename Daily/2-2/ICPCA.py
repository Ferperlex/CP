#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys
import math

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

        n = inp()

        start_col = int((n - 1) ** 0.5) + 1
        diff = n - ((start_col - 1) ** 2)

        if diff <= start_col:
            print(diff, start_col)
        else:
            print(start_col, 2 * start_col - diff)
        # print(n, start_col, diff)
        # print()
