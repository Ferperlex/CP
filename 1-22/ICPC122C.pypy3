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


import time

if __name__ == "__main__":
    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    n = input()
    if n != "":
        n = int(n)

    states = {}

    for i in range(n):
        n, k = inlt()
        # pyramid = [[0] * n for _ in range(n)]
        upper = math.ceil(n / 2) + 1
        if k < upper:
            print(k - 1)
            continue
        pyr = {}
        start = 0

        if n in states:
            start, pyr = states[n]
        for balls in range(start, k):
            i, j = 0, 0

            while i + j != n - 1:
                if (i, j) not in pyr or pyr[(i, j)] == 0:
                    pyr[(i, j)] = 1
                    # if pyramid[i][j] == 0:
                    # pyramid[i][j] = 1
                    i += 1
                else:
                    # pyramid[i][j] = 0
                    pyr[(i, j)] = 0
                    j += 1
        if len(pyr) > 0:
            states[n] = (k, pyr)
            # print(pyramid)
        print(j)
    print("--- %s seconds ---" % (time.time() - start_time))
