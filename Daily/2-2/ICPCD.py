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
        a, b, c, m = map(int, input().split())
        a, b, c = sorted([a, b, c])
        x = c - 1 - a - b
        y = a + b + c - 3
        ans = "NO"
        if x <= m and m <= y:
            ans = "YES"
        print(ans)
