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


def setint():
    return set(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


# import time

if __name__ == "__main__":
    n, c, b = inlt()
    brokens = setint()
    returned = ""
    curr = n
    last = 0
    lastZero = True

    while curr > 0:
        if curr in brokens:
            returned += "0"
            last = 0
            b -= 1
            if not lastZero:
                c -= 1
            lastZero = True
        else:
            if c > 1:
                if lastZero:
                    returned += "1"
                    lastZero = False
                else:
                    returned += "0"
                    lastZero = True
                c -= 1

            elif c == 1:
                if lastZero:
                    if curr == 1:
                        returned += "1"
                        lastZero = False
                        c -= 1
                    else:
                        returned += "0"
                        lastZero = True
                else:
                    returned += "0"
                    c -= 1
                    lastZero = True

            elif c <= 0:
                returned += "0"
        curr -= 1

    print(*returned[::-1], sep="")
