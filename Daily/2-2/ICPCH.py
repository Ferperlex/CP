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

        s = insr()
        t = insr()

        spoint = len(s) - 1
        tpoint = len(t) - 1

        while spoint >= 0 and tpoint >= 0:

            if s[spoint] == t[tpoint]:
                spoint += -1
                tpoint += -1
            else:
                spoint += -2
        # print(spoint, tpoint)
        if tpoint < 0:
            print("YES")
        else:
            print("NO")
