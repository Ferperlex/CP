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

    leng = inp()
    li = []
    count = 0

    for ani in range(leng):
        li.append(inp())

    li.sort(reverse=True)

    currSum = 0
    ind = 0
    lastind = 0
    count = 0
    needed = 0

    while ind < leng:

        needed -= li[ind]
        # print(li, currSum, ind, lastind, leng, needed, count)
        currSum += li[ind]
        if needed <= 0:
            count += (ind - lastind) + 1
            needed = currSum
            lastind = ind + 1

        ind += 1

    print(count)
