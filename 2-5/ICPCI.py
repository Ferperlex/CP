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
    li = inlt()

    li.sort()
    rat = 1
    end = False
    for i in reversed(range(leng)):

        r = float(li[i] / (i + 1))

        if r > 1:
            end = True
            print(-1)
            break

        if r < rat:
            rat = r

    if not end:
        print(round(rat, 7))
