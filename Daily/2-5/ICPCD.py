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


def maxint():
    return sys.maxsize * 2 + 1


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

        leng = inp()

        total = 0
        lids = insr()
        mags = inlt()
        consectotal = 0
        consecmin = maxint()

        for i in reversed(range(leng)):

            if lids[i] == "1":
                consectotal += mags[i]
                consecmin = min(consecmin, mags[i])

            else:
                if consectotal > 0:
                    consectotal += mags[i]
                    consecmin = min(consecmin, mags[i])

                    total += consectotal - consecmin
                    consectotal = 0
                    consecmin = maxint()

        print(total + consectotal)
