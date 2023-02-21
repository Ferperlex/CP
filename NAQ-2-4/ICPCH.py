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

    n, small, big = inlt()
    li = []
    founds = set()
    for i in range(n):
        li.append(inp())
        founds.add(li[i])
    li.sort()

    count = 0
    # print(li)
    failed = False
    lastgap = sys.maxsize * 2 + 1
    nextgap = sys.maxsize * 2 + 1
    for ind in range(n):
        # print(li, ind, lastgap, nextgap, count)
        if ind == n - 1:
            nextgap = sys.maxsize * 2 + 1
        else:
            # print(ind, n)
            nextgap = li[ind + 1] - li[ind]

        maxi = min(lastgap, nextgap)
        if maxi < small / 2:
            failed = True
            print(-1)
            break

        if li[ind] + maxi in founds or li[ind] - maxi in founds:
            maxi -= small / 2

        if maxi > big / 2:
            maxi = big / 2

        count += int(maxi * 2)

        lastgap = nextgap - maxi
    if not failed:
        print(count)
